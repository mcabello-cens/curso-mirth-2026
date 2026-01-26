

# Listar las variables definidas a nivel de servidor (ConfigurationMap)

```
var configs = listConfigurationMaps(true);

/**
 * Lista todas las entradas del Configuration Map del canal actual
 * ordenadas alfabéticamente por clave (A → Z)
 *
 * @param {boolean} logValues - si es true, imprime clave y valor
 * @return {Object} objeto JS con claves ordenadas
 */
function listConfigurationMaps(logValues) {
    var result = {};

    if (typeof configurationMap === 'undefined' || configurationMap == null) {
        logger.warn('No existe configurationMap en este contexto');
        return result;
    }

    // 1. Obtener claves
    var keys = configurationMap.keySet().toArray();

    // 2. Convertir a String y ordenar alfabéticamente
    var stringKeys = [];
    for (var i = 0; i < keys.length; i++) {
        stringKeys.push(String(keys[i]));
    }

    stringKeys.sort(function (a, b) {
        return a.localeCompare(b);
    });

    // 3. Construir resultado ordenado
    for (var j = 0; j < stringKeys.length; j++) {
        var key = stringKeys[j];
        var value = configurationMap.get(key);

        result[key] = value;

        if (logValues === true) {
            logger.info('[CONFIG_MAP] ' + key + ' = ' + value);
        }
    }

    return result;
}
```



# Listar variables a nivel de SourceMap
```
/**/
function listSourceMap() {
    logger.info("===== SOURCE MAP VARIABLES =====");
    var it = sourceMap.keySet().iterator();
    while (it.hasNext()) {
        var key = it.next();
        var value = sourceMap.get(key);
        logger.info("sourceMap[" + key + "] = " + value);
    }
}
```

# Listar variables a nivel de ConnectorMap
```
function listConnectorMap() {
    logger.info("===== CONNECTOR MAP VARIABLES =====");
    var it = connectorMap.keySet().iterator();
    while (it.hasNext()) {
        var key = it.next();
        var value = connectorMap.get(key);
        logger.info("connectorMap[" + key + "] = " + value);
    }
}

logger.info(msg);
```
