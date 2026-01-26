import time
import argparse
import socket
import random
import json
from faker import Faker
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

fake = Faker('es_ES')

def generate_hl7_adt(order_index):
    """Genera mensaje HL7v2 con MSH-10 secuencial y máscara."""
    msg_type = random.choice(["ADT^A01", "ADT^A08"])
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Aplicamos la máscara de 5 dígitos (00001, 00002, etc.)
    order_masked = str(order_index).zfill(5)

    # Limpieza rigurosa de datos para evitar saltos de línea dentro del PID
    pid_id = fake.ssn().replace("-", "")
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y%m%d")
    gender = fake.random_element(elements=("M", "F", "U"))
    full_name = f"{fake.last_name()}^{fake.first_name()}".replace("\n", "")
    address = fake.address().replace("\n", ", ").replace("\r", "").replace("|", " ")
    phone = fake.phone_number().replace("\n", "").replace("\r", "")

    # MSH-10 (Message Control ID) usa order_masked
    msh = f"MSH|^~\\&|PYTHON_GEN|HOSPITAL|MIRTH|SISTEMA|{now}||{msg_type}|{order_masked}|P|2.3"
    evn = f"EVN|{msg_type.split('^')[1]}|{now}"
    pid = f"PID|1||{pid_id}^^^MRN||{full_name}||{dob}|{gender}|||{address}||{phone}"
    pv1 = f"PV1|1|I|EMER|||||||||||||||{random.randint(100, 999)}|"

    # Estándar HL7v2 usa \r (ASCII 13) como terminador de segmento
    hl7_content = f"{msh}\r{evn}\r{pid}\r{pv1}\r"

    # Envolver en MLLP: <VT>HL7<FS><CR>
    mllp_wrapped = f"\x0b{hl7_content}\x1c\x0d"

    return mllp_wrapped.encode('utf-8'), order_masked, msg_type

def send_via_mllp(i, args):
    order_id = i + 1
    mllp_data, order_masked, msg_type = generate_hl7_adt(order_id)

    if args.interval > 0:
        time.sleep(args.interval)

    # Limpiar endpoint (ej: 127.0.0.1:6661)
    clean_endpoint = args.endpoint.replace("http://", "").replace("https://", "").rstrip('/')

    try:
        host, port = clean_endpoint.split(':')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(10)
            sock.connect((host, int(port)))

            sock.sendall(mllp_data)

            # Recibir ACK (Mirth confirma recepción)
            response = sock.recv(4096)
            return f"[{order_masked}] {msg_type} -> ACK recibido"

    except Exception as e:
        return f"[{order_masked}] Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Generador HL7 MLLP con MSH-10 secuencial.")
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--endpoint", type=str, required=True)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--interval", type=float, default=0)

    args = parser.parse_args()
    start_time = datetime.now()

    print(f"--- Iniciando envío de {args.count} mensajes ---")
    print(f"Inicio: {start_time.strftime('%H:%M:%S')}\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = list(executor.map(lambda i: send_via_mllp(i, args), range(args.count)))

    for res in results:
        print(res)

    end_time = datetime.now()
    duration = end_time - start_time

    print("-" * 50)
    print(f"PROCESO FINALIZADO")
    print(f"Inicio  : {start_time.strftime('%H:%M:%S')}")
    print(f"Término : {end_time.strftime('%H:%M:%S')}")
    print(f"Duración: {duration}")
    print("-" * 50)

if __name__ == "__main__":
    main()