# Ejercicio 3: Encadenar canales

A partir de la lectura de un HL7v2 por TCP realizar:

## Origen

* Identificar si el tipo de mensaje es ADT_A01, ADT_A08 o es otro
* Si el mensaje es ADT_A01 --> Enviar mensaje por un canal **A** que muestre el resultado del mensaje.
* Si el mensaje es ADT_A08 --> Enviar mensaje por un canal **B** que muestre el resultado del mensaje.
* Puede enviar el mensaje desde un cliente HL7v2 o inyectarlo desde la GUI de Mirth

## Destino

* Canal A Channel Reader con logger.info del mensaje 
* Canal B Channel Reader con logger.info del mensaje

### Datos de origen

```
MSH|^~\&|SYSTEM|HOSPITAL|ADT|LAB|202501041030||ADT^A01|DDB91498|P|2.3|
PID|1||7650CE51||Jared Gray||19810101|M|||202 Unknown Blvd^^City^ST^00000^USA
EVN|A01|202501040900|||Admin^User
PV1|1|I|ICU^1234^1^Hospital|||12345^Physician^John^A^^Dr.|
```

```
MSH|^~\&|SYSTEM|HOSPITAL|ADT|LAB|202501041030||ADT^A08|5E181426|P|2.3|
PID|1||E2754CA2||Christopher Wilson||19810101|M|||202 Unknown Blvd^^City^ST^00000^USA
EVN|A08|202501040900|||Admin^User
PV1|1|I|ICU^1234^1^Hospital|||12345^Physician^John^A^^Dr.|
```


