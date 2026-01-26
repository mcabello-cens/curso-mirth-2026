

A partir de un mensaje desde archivo de texto delimitado construya un canal que cumpla con lo siguiente:

Origen

Desde la ubicación c:\data\source se procesarán los archivos de texto. (File Reader)

Obtener los elementos rut, nombre, apellido y nacimiento del archivo de texto

Crear un recurso FHIR Patient

Destino

Hacer POST del recurso Patient en un servidor FHIR (HTTP Sender)

Mover el archivo a la carpeta c:\data\target (File Writer)
