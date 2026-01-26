# Instalación

```
python -m venv .venv

.\.venv\Scripts\activate (Windows)


pip install -r requirements.txt
```

# Generador de mensajes HL7 ADT_A01 / ADT_A08

```
python .\hl7v2PatientGenerator.py --count COUNT --endpoint ENDPOINT [--threads THREADS] [--interval INTERVAL]

--count // numero de mensajes a generar
--endpoint // servidor y puerto TCP para envio de mensajes
--threads // número de hilos procesador
--interval // intervalo de tiempo cada cuanto enviar mensajes
```

ejemplo:
```
python .\hl7v2PatientGenerator.py --count 10 --endpoint 127.0.0.1:6001 --threads 1 --interval 0
```

# Generador de mensajes legacy 

sintaxis

```
python .\PatientGenerator.py --count COUNT [--interval INTERVAL] --target {file,http} [--threads THREADS] [--targetFolder TARGETFOLDER] [--endpoint ENDPOINT]
```

## ejemplo - Generar y enviar a un endpoint HTTP

```
python .\PatientGenerator.py \\
    --count 10 \\
    --interval 0 \\
    --target http \\
    --threads 1 \\
    --endpoint http://localhost:9001/base/pacientes
```


## ejemplo - Generar y enviar a una carpeta

```
python .\PatientGenerator.py \\
    --count 10 \\
    --interval 0 \\
    --target file \\
    --threads 1 \\
    --targetFolder /data/sample
```
