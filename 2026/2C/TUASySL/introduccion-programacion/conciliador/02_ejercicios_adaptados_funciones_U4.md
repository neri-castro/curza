# Banco de Ejercicios Adaptados a Modularización y Funciones (Unidad 4)

**Asignatura:** Introducción a la Programación (2° Cuatrimestre 2026)  
**Carrera:** Tecnicatura Universitaria en Administración de Sistemas y Software Libre (TUASySL)  

> **Propósito de esta adaptación:**  
> En el archivo original `Banco_ejercicios_Python.pdf`, los 50 ejercicios están resueltos de forma secuencial en el bloque principal. Para alinearlos con la **Unidad 4 (Modularización)** y la **Unidad 6 (Conjuntos y Estructuras)** del Programa 2026, aquí se presentan **10 ejercicios representativos adaptados con funciones** (`def`), parámetros formales/actuales, *docstrings*, ámbito local de variables y retorno de resultados (`return`), aplicando la estrategia *Divide y Vencerás*.

---

## 1. Instalación desatendida: paquetes faltantes (Adaptado del Ej. 1)
**Temas:** *Funciones (U4), listas y conjuntos (U6), `for`, `if`.*

### Enunciado
Un script de instalación desatendida debe asegurar que estén todos los paquetes requeridos.
1. Escribir la función `obtener_faltantes(requeridos, instalados)` que reciba ambas listas y **retorne** una nueva lista con los paquetes que están en `requeridos` pero no en `instalados` (respetando el orden original).
2. Escribir la función `armar_comando_apt(paquetes_faltantes)` que reciba la lista de faltantes y retorne el comando `"sudo apt-get install -y paquete1 paquete2 ..."` o `"Sistema listo"` si la lista está vacía.
3. Invocar ambas funciones desde el programa principal con los datos de partida. *(Nota adicional para coloquio: mostrar cómo se resolvería `obtener_faltantes` usando diferencia de conjuntos `set`).*

### Datos de partida
```python
requeridos = ["git", "curl", "python3", "apache2", "mysql-server", "ufw"]
instalados = ["curl", "python3", "nano", "ufw"]
```

### Resolución con Funciones (Unidad 4)
```python
def obtener_faltantes(lista_requeridos, lista_instalados):
    """Retorna la lista de paquetes requeridos que aún no están instalados."""
    # lista_requeridos : list[str]
    # lista_instalados : list[str]
    instalados_set = set(lista_instalados)  # búsqueda eficiente con set (U6)
    faltantes = []
    for paquete in lista_requeridos:
        if paquete not in instalados_set:
            faltantes.append(paquete)
    return faltantes


def armar_comando_apt(faltantes):
    """Retorna el comando apt-get de instalación o 'Sistema listo' si no faltan."""
    # faltantes : list[str]
    if faltantes:
        return "sudo apt-get install -y " + " ".join(faltantes)
    return "Sistema listo"


# Programa principal
requeridos = ["git", "curl", "python3", "apache2", "mysql-server", "ufw"]
instalados = ["curl", "python3", "nano", "ufw"]

pendientes = obtener_faltantes(requeridos, instalados)
if pendientes:
    print("Faltan:", pendientes)
print(armar_comando_apt(pendientes))
```

### Salida esperada
```text
Faltan: ['git', 'apache2', 'mysql-server']
sudo apt-get install -y git apache2 mysql-server
```

---

## 2. Requisitos mínimos del equipo (Adaptado del Ej. 2)
**Temas:** *Funciones (U4), diccionarios, tuplas (U6), condicionales (U3).*

### Enunciado
Antes de instalar un servicio, el script verifica si un servidor cumple los requisitos mínimos `(ram_min_gb, disco_min_gb)`.
1. Definir la función `verificar_requisitos(datos_equipo, req_minimos)` que reciba el diccionario del equipo y la tupla de requisitos, y **retorne** una lista con los motivos de incumplimiento (si cumple todo, retorna una lista vacía `[]`).
2. Definir la función `es_ubuntu(datos_equipo)` que retorne `True` si el sistema operativo comienza con `"Ubuntu"` y `False` en caso contrario.
3. En el programa principal, mostrar los fallos detectados, informar `"APTO"` o `"NO APTO"` y mostrar la advertencia si el SO no es Ubuntu.

### Datos de partida
```python
requisitos = (4, 20)
equipo = {"hostname": "lab2-pc07", "ram_gb": 2, "disco_libre_gb": 35, "so": "Debian 12"}
```

### Resolución con Funciones (Unidad 4)
```python
def verificar_requisitos(datos_equipo, req_minimos):
    """Retorna una lista de mensajes con los requisitos no cumplidos por el equipo."""
    # datos_equipo : dict
    # req_minimos : tuple[int, int]
    ram_min, disco_min = req_minimos
    fallos = []
    if datos_equipo["ram_gb"] < ram_min:
        fallos.append(f"RAM insuficiente: {datos_equipo['ram_gb']} GB")
    if datos_equipo["disco_libre_gb"] < disco_min:
        fallos.append(f"Disco insuficiente: {datos_equipo['disco_libre_gb']} GB")
    return fallos


def es_ubuntu(datos_equipo):
    """Retorna True si el sistema operativo del equipo empieza con 'Ubuntu'."""
    # datos_equipo : dict
    return datos_equipo["so"].startswith("Ubuntu")


# Programa principal
requisitos = (4, 20)
equipo = {"hostname": "lab2-pc07", "ram_gb": 2, "disco_libre_gb": 35, "so": "Debian 12"}

incumplimientos = verificar_requisitos(equipo, requisitos)
for motivo in incumplimientos:
    print(motivo)

estado = "APTO" if not incumplimientos else "NO APTO"
print(equipo["hostname"], estado)

if not es_ubuntu(equipo):
    print("Advertencia: el SO no es Ubuntu")
```

### Salida esperada
```text
RAM insuficiente: 2 GB
lab2-pc07 NO APTO
Advertencia: el SO no es Ubuntu
```

---

## 3. Análisis de un log del sistema (Adaptado del Ej. 3)
**Temas:** *Funciones (U4), listas, diccionarios (U6), `for`, `split()`.*

### Enunciado
Modularizar el análisis de líneas de un archivo de log con formato `"AAAA-MM-DD HH:MM NIVEL Mensaje"`:
1. Escribir la función `contar_niveles_log(lineas_log)` que reciba la lista de cadenas y **retorne un diccionario** con la cantidad de apariciones de cada nivel (`INFO`, `WARNING`, `ERROR`).
2. Escribir la función `extraer_mensajes_por_nivel(lineas_log, nivel_buscado)` que **retorne una lista** únicamente con el texto del mensaje de aquellas líneas que coincidan con `nivel_buscado`.
3. Invocar ambas funciones desde el programa principal para mostrar el conteo y listar los errores.

### Datos de partida
```python
log = [
    "2026-11-03 10:15 INFO Servicio apache2 iniciado",
    "2026-11-03 10:16 WARNING Disco al 75%",
    "2026-11-03 10:20 ERROR Falló conexión a mysql",
    "2026-11-03 10:21 INFO Reintentando conexión",
    "2026-11-03 10:22 ERROR Timeout en mysql",
    "2026-11-03 10:30 INFO Backup finalizado",
]
```

### Resolución con Funciones (Unidad 4)
```python
def contar_niveles_log(lineas_log):
    """Retorna un diccionario con la frecuencia de cada nivel de severidad."""
    # lineas_log : list[str]
    conteo = {}
    for linea in lineas_log:
        partes = linea.split(" ", 3)
        nivel = partes[2]
        conteo[nivel] = conteo.get(nivel, 0) + 1
    return conteo


def extraer_mensajes_por_nivel(lineas_log, nivel_buscado):
    """Retorna una lista con los mensajes correspondientes al nivel indicado."""
    # lineas_log : list[str]
    # nivel_buscado : str
    mensajes = []
    for linea in lineas_log:
        partes = linea.split(" ", 3)
        if partes[2] == nivel_buscado:
            mensajes.append(partes[3])
    return mensajes


# Programa principal
log = [
    "2026-11-03 10:15 INFO Servicio apache2 iniciado",
    "2026-11-03 10:16 WARNING Disco al 75%",
    "2026-11-03 10:20 ERROR Falló conexión a mysql",
    "2026-11-03 10:21 INFO Reintentando conexión",
    "2026-11-03 10:22 ERROR Timeout en mysql",
    "2026-11-03 10:30 INFO Backup finalizado",
]

resumen = contar_niveles_log(log)
errores = extraer_mensajes_por_nivel(log, "ERROR")

print(resumen)
for msg in errores:
    print("ERROR:", msg)
```

### Salida esperada
```text
{'INFO': 3, 'WARNING': 1, 'ERROR': 2}
ERROR: Falló conexión a mysql
ERROR: Timeout en mysql
```

---

## 4. Reintentos de conexión a servidor (Adaptado del Ej. 4)
**Temas:** *Funciones (U4), `while` (U5), listas y tuplas (U6), condicionales (U3).*

### Enunciado
Un script intenta conectarse a un servidor de paquetes como máximo `max_intentos` veces.
1. Escribir la función `simular_conexion(lista_respuestas, limite_intentos)` que utilice un ciclo `while` para recorrer los intentos hasta lograr conectar o agotar `limite_intentos`. Debe imprimir el estado de cada intento y **retornar una tupla `(conectado, intentos_realizados)`** donde `conectado` es `bool` e `intentos_realizados` es `int`.
2. En el programa principal, invocar la función y, si no logró conectarse, mostrar `"Instalación abortada"`.

### Datos de partida
```python
respuestas = [False, False, False, True, False]
max_intentos = 5
```

### Resolución con Funciones (Unidad 4)
```python
def simular_conexion(lista_respuestas, limite_intentos):
    """Ejecuta intentos de conexión con while y retorna (conectado, intentos_usados)."""
    # lista_respuestas : list[bool]
    # limite_intentos : int
    intento = 0
    conectado = False
    while intento < limite_intentos and intento < len(lista_respuestas) and not conectado:
        if lista_respuestas[intento]:
            print("Intento", intento + 1, ": conectado")
            conectado = True
        else:
            print("Intento", intento + 1, ": falló")
        intento += 1
    return conectado, intento


# Programa principal
respuestas = [False, False, False, True, False]
max_intentos = 5

exito, usados = simular_conexion(respuestas, max_intentos)
if not exito:
    print("Instalación abortada")
```

### Salida esperada
```text
Intento 1 : falló
Intento 2 : falló
Intento 3 : falló
Intento 4 : conectado
```

---

## 5. Estado de servicios y alerta crítica (Adaptado del Ej. 7)
**Temas:** *Funciones (U4), diccionarios, listas (U6), condicionales (U3).*

### Enunciado
1. Escribir la función `obtener_servicios_caidos(mapa_servicios)` que reciba el diccionario `{servicio: estado}` y **retorne una lista** con los nombres de los servicios cuyo estado sea distinto de `"activo"`.
2. Escribir la función `hay_riesgo_acceso_remoto(lista_caidos, servicio_remoto)` que retorne `True` si `servicio_remoto` (por ejemplo `"ssh"`) se encuentra dentro de la lista de caídos.
3. En el programa principal, utilizar ambas funciones para informar los servicios caídos y emitir `"ALERTA CRÍTICA: sin acceso remoto"` si corresponde.

### Datos de partida
```python
servicios = {
    "apache2": "activo",
    "mysql": "inactivo",
    "ssh": "inactivo",
    "cron": "activo",
    "ufw": "activo",
}
```

### Resolución con Funciones (Unidad 4)
```python
SERVICIO_CRITICO = "ssh"


def obtener_servicios_caidos(mapa_servicios):
    """Retorna una lista con los nombres de los servicios que no están activos."""
    # mapa_servicios : dict[str, str]
    caidos = []
    for nombre, estado in mapa_servicios.items():
        if estado != "activo":
            caidos.append(nombre)
    return caidos


def hay_riesgo_acceso_remoto(lista_caidos, servicio_remoto):
    """Retorna True si el servicio de acceso remoto está entre los caídos."""
    # lista_caidos : list[str]
    # servicio_remoto : str
    return servicio_remoto in lista_caidos


# Programa principal
servicios = {
    "apache2": "activo",
    "mysql": "inactivo",
    "ssh": "inactivo",
    "cron": "activo",
    "ufw": "activo",
}

caidos = obtener_servicios_caidos(servicios)
if not caidos:
    print("Todos los servicios OK")
else:
    print("Caídos:", caidos)
    if hay_riesgo_acceso_remoto(caidos, SERVICIO_CRITICO):
        print("ALERTA CRÍTICA: sin acceso remoto")
```

### Salida esperada
```text
Caídos: ['mysql', 'ssh']
ALERTA CRÍTICA: sin acceso remoto
```

---

## 6. Clasificación de uso de disco por partición (Adaptado del Ej. 8)
**Temas:** *Funciones (U4), lista de tuplas (U6), `if/elif/else` (U3).*

### Enunciado
1. Definir las constantes `UMBRAL_CRITICO = 90` y `UMBRAL_ADVERTENCIA = 70`.
2. Escribir la función `clasificar_uso_disco(porcentaje)` que reciba un entero y **retorne** `"CRÍTICO"` ($\ge 90$), `"ADVERTENCIA"` ($70$ a $89$) u `"OK"` ($< 70$).
3. En el programa principal, recorrer la lista de tuplas `particiones` invocando a `clasificar_uso_disco()` para mostrar el reporte de cada punto de montaje.

### Datos de partida
```python
particiones = [("/", 45), ("/home", 71), ("/var", 92), ("/boot", 89), ("/tmp", 10)]
```

### Resolución con Funciones (Unidad 4)
```python
UMBRAL_CRITICO = 90
UMBRAL_ADVERTENCIA = 70


def clasificar_uso_disco(porcentaje):
    """Clasifica el porcentaje de uso de disco en CRÍTICO, ADVERTENCIA u OK."""
    # porcentaje : int
    if porcentaje >= UMBRAL_CRITICO:
        return "CRÍTICO"
    elif porcentaje >= UMBRAL_ADVERTENCIA:
        return "ADVERTENCIA"
    else:
        return "OK"


# Programa principal
particiones = [("/", 45), ("/home", 71), ("/var", 92), ("/boot", 89), ("/tmp", 10)]

for punto, uso in particiones:
    estado = clasificar_uso_disco(uso)
    print(f"{punto} -> {uso}% {estado}")
```

### Salida esperada
```text
/ -> 45% OK
/home -> 71% ADVERTENCIA
/var -> 92% CRÍTICO
/boot -> 89% ADVERTENCIA
/tmp -> 10% OK
```

---

## 7. Validación de direcciones IPv4 (Adaptado del Ej. 11)
**Temas:** *Funciones (U4), cadenas, listas (U6), `for`, condicionales (U3).*

### Enunciado
1. Escribir la función booleana `es_ip_valida(direccion_ip)` que reciba una cadena y **retorne `True`** si tiene exactamente 4 octetos separados por `"."`, donde cada octeto es numérico y su valor entero está entre `0` y `255` inclusive; en caso contrario debe retornar `False`.
2. En el programa principal, recorrer la lista `ips` e informar cuáles son válidas e inválidas invocando la función.

### Datos de partida
```python
ips = ["192.168.1.10", "10.0.0.256", "172.16.5", "8.8.8.8", "192.168.a.1"]
```

### Resolución con Funciones (Unidad 4)
```python
def es_ip_valida(direccion_ip):
    """Retorna True si direccion_ip tiene formato IPv4 válido (4 octetos de 0 a 255)."""
    # direccion_ip : str
    partes = direccion_ip.split(".")
    if len(partes) != 4:
        return False
    for octeto in partes:
        if not octeto.isdigit() or not (0 <= int(octeto) <= 255):
            return False
    return True


# Programa principal
ips = ["192.168.1.10", "10.0.0.256", "172.16.5", "8.8.8.8", "192.168.a.1"]

for ip in ips:
    resultado = "válida" if es_ip_valida(ip) else "inválida"
    print(ip, resultado)
```

### Salida esperada
```text
192.168.1.10 válida
10.0.0.256 inválida
172.16.5 inválida
8.8.8.8 válida
192.168.a.1 inválida
```

---

## 8. Configuración por defecto y personalizada (Adaptado del Ej. 14)
**Temas:** *Funciones (U4), diccionarios, tuplas (U6), `for`, `in`.*

### Enunciado
1. Escribir la función `combinar_configuracion(config_base, config_usuario)` que reciba ambos diccionarios (sin modificar el diccionario original `config_base`) y **retorne una tupla `(config_final, claves_desconocidas)`**, donde `config_final` tiene los valores actualizados de las claves válidas y `claves_desconocidas` es una lista con las claves que puso el usuario pero no existen en `config_base`.
2. Mostrar desde el programa principal las claves desconocidas y el diccionario final resultante.

### Datos de partida
```python
por_defecto = {
    "puerto": 80,
    "idioma": "es",
    "zona_horaria": "America/Argentina/Buenos_Aires",
    "firewall": True,
}
usuario = {"puerto": 8080, "firewal": False, "idioma": "es"}
```

### Resolución con Funciones (Unidad 4)
```python
def combinar_configuracion(config_base, config_usuario):
    """Combina config_usuario sobre una copia de config_base y retorna (final, desconocidas)."""
    # config_base : dict
    # config_usuario : dict
    final = config_base.copy()
    desconocidas = []
    for clave, valor in config_usuario.items():
        if clave in final:
            final[clave] = valor
        else:
            desconocidas.append(clave)
    return final, desconocidas


# Programa principal
por_defecto = {
    "puerto": 80,
    "idioma": "es",
    "zona_horaria": "America/Argentina/Buenos_Aires",
    "firewall": True,
}
usuario = {"puerto": 8080, "firewal": False, "idioma": "es"}

config_activa, ignoradas = combinar_configuracion(por_defecto, usuario)
for clave_erronea in ignoradas:
    print("Clave desconocida:", clave_erronea)
print(config_activa)
```

### Salida esperada
```text
Clave desconocida: firewal
{'puerto': 8080, 'idioma': 'es', 'zona_horaria': 'America/Argentina/Buenos_Aires', 'firewall': True}
```

---

## 9. Validador de contraseñas temporales (Adaptado del Ej. 16)
**Temas:** *Funciones (U4), cadenas, listas (U6), `for`, condicionales (U3).*

### Enunciado
1. Escribir la función `diagnosticar_clave(clave, largo_minimo)` que verifique si `clave` tiene al menos `largo_minimo` caracteres, al menos un dígito y al menos una letra mayúscula. Debe **retornar una lista** con los requisitos faltantes (si es válida, retorna `[]`).
2. En el programa principal, evaluar todas las contraseñas de la lista `claves` con `largo_minimo = 8`.

### Datos de partida
```python
claves = ["Comahue2026", "abc123", "PasswordSegura", "sistemas99", "Lab3pc07"]
```

### Resolución con Funciones (Unidad 4)
```python
LARGO_MINIMO = 8


def diagnosticar_clave(clave, largo_min):
    """Retorna una lista con los requisitos de seguridad que le faltan a la clave."""
    # clave : str
    # largo_min : int
    faltas = []
    if len(clave) < largo_min:
        faltas.append(f"{largo_min} caracteres")

    tiene_digito = False
    tiene_mayus = False
    for caracter in clave:
        if caracter.isdigit():
            tiene_digito = True
        if caracter.isupper():
            tiene_mayus = True

    if not tiene_digito:
        faltas.append("un dígito")
    if not tiene_mayus:
        faltas.append("una mayúscula")

    return faltas


# Programa principal
claves = ["Comahue2026", "abc123", "PasswordSegura", "sistemas99", "Lab3pc07"]

for c in claves:
    requisitos_faltantes = diagnosticar_clave(c, LARGO_MINIMO)
    if not requisitos_faltantes:
        print(c, "válida")
    else:
        print(c, "le falta: " + ", ".join(requisitos_faltantes))
```

### Salida esperada
```text
Comahue2026 válida
abc123 le falta: 8 caracteres, una mayúscula
PasswordSegura le falta: un dígito
sistemas99 le falta: una mayúscula
Lab3pc07 válida
```

---

## 10. Bloqueo de IPs por intentos fallidos tipo `fail2ban` (Adaptado del Ej. 18)
**Temas:** *Funciones (U4), listas, diccionarios (U6), `for`, `split()`.*

### Enunciado
1. Escribir la función `contar_fallos_por_ip(registros_auth)` que reciba la lista de eventos `"RESULTADO IP"` y **retorne un diccionario** `{ip: cantidad_fallos}` contando solo los que tienen `"FAIL"`.
2. Escribir la función `generar_lista_negra(conteo_fallos, umbral)` que reciba el diccionario de conteos y un entero `umbral`, y **retorne una lista** con las IPs que superan estrictamente (`>`) dicho umbral.
3. Probar ambas funciones desde el programa principal con `UMBRAL_BLOQUEO = 3`.

### Datos de partida
```python
auth = [
    "FAIL 10.0.0.5", "OK 10.0.0.2", "FAIL 10.0.0.5", "FAIL 200.45.1.9",
    "FAIL 10.0.0.5", "FAIL 200.45.1.9", "FAIL 10.0.0.5", "OK 10.0.0.5", "FAIL 186.12.3.4",
]
```

### Resolución con Funciones (Unidad 4)
```python
UMBRAL_BLOQUEO = 3


def contar_fallos_por_ip(registros_auth):
    """Cuenta y retorna un diccionario con la cantidad de eventos FAIL por cada IP."""
    # registros_auth : list[str]
    fallos = {}
    for linea in registros_auth:
        resultado, ip = linea.split()
        if resultado == "FAIL":
            fallos[ip] = fallos.get(ip, 0) + 1
    return fallos


def generar_lista_negra(conteo_fallos, umbral):
    """Retorna la lista de IPs cuya cantidad de fallos es mayor al umbral."""
    # conteo_fallos : dict[str, int]
    # umbral : int
    bloqueadas = []
    for ip, cantidad in conteo_fallos.items():
        if cantidad > umbral:
            bloqueadas.append(ip)
    return bloqueadas


# Programa principal
auth = [
    "FAIL 10.0.0.5", "OK 10.0.0.2", "FAIL 10.0.0.5", "FAIL 200.45.1.9",
    "FAIL 10.0.0.5", "FAIL 200.45.1.9", "FAIL 10.0.0.5", "OK 10.0.0.5", "FAIL 186.12.3.4",
]

fallos_detectados = contar_fallos_por_ip(auth)
lista_negra = generar_lista_negra(fallos_detectados, UMBRAL_BLOQUEO)

print(fallos_detectados)
print("Lista negra:", lista_negra)
```

### Salida esperada
```text
{'10.0.0.5': 4, '200.45.1.9': 2, '186.12.3.4': 1}
Lista negra: ['10.0.0.5']
```
