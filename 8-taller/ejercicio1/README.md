
# Ejercicio 1: Convertir archivo de texto en recurso FHIR y persistirlo en servidor 

A partir de un mensaje desde archivo de texto delimitado construya un canal que cumpla con lo siguiente:

## Origen

* Desde la ubicación **c:\data\source** se procesarán los archivos de texto. (File Reader)

* Obtener los elementos rut, nombre, apellido y nacimiento del archivo de texto

* Crear un recurso FHIR Patient

## Destino

* Hacer POST del recurso Patient en un servidor FHIR (HTTP Sender)

* Mover el archivo a la carpeta **c:\data\target** (File Writer)


### Datos de origen
patient_dataset1.txt, patient_dataset2.txt, patient_dataset3.txt

### FHIR Servers:

https://fhir.cens.cl/baseR4

http://hapi.fhir.org/baseR4


