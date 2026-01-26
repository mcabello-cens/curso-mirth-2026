






# Comandos SO

🔌 Ver puertos TCP abiertos (locales)
## 1️⃣ ss (el heredero moderno de netstat)

```
ss -tulnp
-t TCP
-u UDP
-l en escucha (listening)
-n sin resolver nombres
-p muestra el proceso
```

👉 Solo TCP en escucha:

```
ss -tlnp
```

## 2️⃣ netstat (vieja escuela, si está instalado)

```
netstat -tulnp
```

Solo TCP:

```
netstat -tlnpv
```
## 3️⃣ lsof (quién usa qué puerto)

```
lsof -iTCP -sTCP:LISTEN -P -n
```

Buscar un puerto específico:

```
lsof -i :8080
```

🌐 Ver endpoints HTTP locales

## 4️⃣ Probar si hay HTTP escuchando en un puerto

```
curl -I http://localhost:8080
```

O con más detalle:

```curl -v http://localhost:8080 ```

## 5️⃣ Listar endpoints comunes (si conoces la app)

Ejemplo con una API REST típica:

```
curl http://localhost:8080/health
curl http://localhost:8080/status
curl http://localhost:8080/api
```

🔍 Escanear puertos (local o remoto)
## 6️⃣ nmap (el bisturí)

Escaneo rápido de TCP:

```
nmap -sT localhost
```

Solo los más comunes:

```
nmap localhost
```

Buscar servicios HTTP:

```
nmap -p 80,443,8080,8000 --open localhost
```


Detectar endpoints HTTP:

```
nmap -p 80,8080 --script http-enum localhost
```

## 7️⃣ tcpdump

```
tcpdump -i any tcp port 80
```

Para HTTPS (solo metadatos):

```
tcpdump -i any tcp port 443
```

🧠 Combo rápido (mi favorito)

```
ss -tlnp | grep -E '80|443|8080'
```


