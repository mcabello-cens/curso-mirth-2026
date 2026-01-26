import time
import json
import os
import argparse
import requests
from faker import Faker
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Configuración de Faker
fake = Faker('es_ES')

def generate_patient(order_index):
    """
    Crea un diccionario con datos sintéticos.
    order_index: número entero (1, 2, 3...)
    """
    # Aplicamos la máscara de 5 dígitos (00001, 00002, etc.)
    order_masked = str(order_index).zfill(5)

    return {
        "order": order_masked,
        "id": fake.uuid4(),
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=0, maximum_age=90).isoformat(),
        "genero": fake.random_element(elements=("M", "F", "Otro")),
        "documento_identidad": fake.ssn(),
        "email": fake.email(),
        "telefono": fake.phone_number(),
        "direccion": fake.address().replace('\n', ', '),
        "timestamp": datetime.now().isoformat()
    }

def process_single_patient(i, args):
    # i empieza en 0, el orden real es i + 1
    order_id = i + 1
    patient_data = generate_patient(order_id)

    # Manejo de intervalo
    if args.interval > 0:
        time.sleep(args.interval)

    if args.target == 'file':
        filename = f"patient_{patient_data['order']}.json"
        filepath = os.path.join(args.targetFolder, filename)
        try:
            with open(filepath, 'w') as f:
                json.dump(patient_data, f, indent=4)
            return f"[{patient_data['order']}] Guardado: {filename}"
        except Exception as e:
            return f"[{patient_data['order']}] Error archivo: {e}"

    elif args.target == 'http':
        try:
            payload = json.dumps(patient_data)
            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                args.endpoint,
                data=payload,
                headers=headers,
                allow_redirects=False
            )
            # Retornamos el número formateado en el log de consola también
            return f"[{patient_data['order']}] Status: {response.status_code}"
        except Exception as e:
            return f"[{patient_data['order']}] Error HTTP: {e}"

def main():
    parser = argparse.ArgumentParser(description="Generador de pacientes con máscara en order.")
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--interval", type=float, default=0)
    parser.add_argument("--target", choices=['file', 'http'], required=True)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--targetFolder", type=str)
    parser.add_argument("--endpoint", type=str)

    args = parser.parse_args()

    start_time = datetime.now()

    if args.target == 'file' and args.targetFolder:
        os.makedirs(args.targetFolder, exist_ok=True)

    print(f"--- Iniciando generación de {args.count} pacientes ({args.threads} hilos) ---")
    print(f"Hora de inicio: {start_time.strftime('%H:%M:%S')}\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = list(executor.map(lambda i: process_single_patient(i, args), range(args.count)))

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