# Bloques de Código de Mediana Complejidad: "¿Qué hace este código?"

**Asignatura:** Introducción a la Programación (2° Cuatrimestre 2026)  
**Carrera:** Tecnicatura Universitaria en Administración de Sistemas y Software Libre (TUASySL)  

> **Consigna general para el estudiante:**  
> Analizá el siguiente bloque de código sin ejecutarlo primero (o realizando una traza / prueba de escritorio). Indicá:
> 1. **Propósito general:** ¿Qué problema de administración de sistemas resuelve el programa?
> 2. **Explicación paso a paso:** ¿Qué recibe, cómo procesa los datos y qué retorna cada función? ¿Por qué se eligieron esas estructuras de control y de datos?
> 3. **Salida por pantalla:** ¿Qué muestra exactamente al ejecutarse con los datos provistos?

---

## Bloque 1: Agrupación de procesos por usuario y detección de consumo elevado
**Temas integrados:** *Funciones (U4), lista de tuplas (U6), diccionarios de listas y acumuladores (U6/U5), condicionales (U3).*

### Código a analizar
```python
def analizar_procesos(tabla_procesos, limite_ram):
    por_usuario = {}
    pesados = []
    for pid, usuario, comando, ram_mb in tabla_procesos:
        por_usuario[usuario] = por_usuario.get(usuario, 0) + ram_mb
        if ram_mb > limite_ram:
            pesados.append((pid, comando))
    return por_usuario, pesados


procesos = [
    (101, "root", "systemd", 45),
    (204, "www-data", "apache2", 320),
    (205, "www-data", "apache2", 290),
    (310, "mysql", "mysqld", 850),
    (412, "root", "sshd", 25),
]

consumo_usuarios, alerta_procesos = analizar_procesos(procesos, 300)
print("RAM por usuario (MB):", consumo_usuarios)
print("Procesos que superan 300 MB:", alerta_procesos)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Procesa una lista de procesos activos en un servidor (donde cada tupla representa `(PID, usuario, comando, consumo_RAM_MB)`) para calcular cuánta memoria RAM total consume cada usuario del sistema y separar aquellos procesos individuales que exceden un umbral (`300 MB`).
* **Detalle técnico paso a paso:**
  1. La función `analizar_procesos(tabla_procesos, limite_ram)` inicializa un diccionario vacío `por_usuario` (que actúa como acumulador por clave) y una lista vacía `pesados`.
  2. Recorre la lista de tuplas desempaquetando las 4 componentes en cada iteración del `for`.
  3. Usa `por_usuario.get(usuario, 0) + ram_mb` para sumar la memoria al usuario correspondiente (si el usuario no existía aún en el diccionario, comienza desde `0`).
  4. Si el consumo individual `ram_mb` supera estrictamente `limite_ram` (`300`), agrega una tupla reducida `(pid, comando)` a la lista `pesados`.
  5. Retorna ambos resultados en una tupla `(por_usuario, pesados)`, que se desempaqueta en el programa principal.
* **Salida exacta por pantalla:**
```text
RAM por usuario (MB): {'root': 70, 'www-data': 610, 'mysql': 850}
Procesos que superan 300 MB: [(204, 'apache2'), (310, 'mysqld')]
```

---

## Bloque 2: Comparación de paquetes entre dos servidores con Conjuntos (`set`)
**Temas integrados:** *Funciones (U4), operaciones de conjuntos (U6: intersección `&`, diferencia `-`, diferencia simétrica `^`), `sorted()`.*

### Código a analizar
```python
def auditar_espejo(srv_produccion, srv_contingencia):
    set_prod = set(srv_produccion)
    set_cont = set(srv_contingencia)

    faltan_en_contingencia = sorted(set_prod - set_cont)
    sobran_en_contingencia = sorted(set_cont - set_prod)
    comunes = len(set_prod & set_cont)

    return faltan_en_contingencia, sobran_en_contingencia, comunes


prod = ["nginx", "ufw", "fail2ban", "postgresql", "curl", "git"]
backup = ["nginx", "ufw", "curl", "vim", "htop"]

faltantes, extras, coincidencias = auditar_espejo(prod, backup)
print("Instalar en contingencia:", faltantes)
print("Desinstalar de contingencia:", extras)
print("Paquetes sincronizados:", coincidencias)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Compara los paquetes instalados en un servidor de producción contra un servidor de contingencia (réplica/backup) para determinar qué paquetes faltan instalar en el servidor de contingencia, cuáles están instalados de más y cuántos coinciden en ambos.
* **Detalle técnico paso a paso:**
  1. Convierte ambas listas a conjuntos (`set_prod` y `set_cont`) para habilitar operaciones algebraicas de conjuntos en tiempo constante.
  2. Calcula la diferencia `set_prod - set_cont` (paquetes que están en producción pero no en contingencia) y la ordena alfabéticamente con `sorted()`.
  3. Calcula la diferencia inversa `set_cont - set_prod` (paquetes que están en contingencia pero no en producción).
  4. Calcula la intersección `set_prod & set_cont` y obtiene su cardinalidad con `len()`.
* **Salida exacta por pantalla:**
```text
Instalar en contingencia: ['fail2ban', 'git', 'postgresql']
Desinstalar de contingencia: ['htop', 'vim']
Paquetes sincronizados: 3
```

---

## Bloque 3: Parseo de archivo de configuración `.conf` ignorando comentarios
**Temas integrados:** *Funciones (U4), manipulación de strings (`strip`, `startswith`, `split`, `isdigit`), diccionarios (U6), `for` (U5).*

### Código a analizar
```python
def cargar_configuracion(lineas_archivo):
    config = {}
    for linea in lineas_archivo:
        limpia = linea.strip()
        if limpia != "" and not limpia.startswith("#"):
            clave, valor = limpia.split("=", 1)
            clave = clave.strip()
            valor = valor.strip()
            if valor.isdigit():
                config[clave] = int(valor)
            elif valor.lower() in ("true", "false"):
                config[clave] = valor.lower() == "true"
            else:
                config[clave] = valor
    return config


archivo_sshd = [
    "# Configuración del servidor SSH",
    "Port = 2222",
    "  ",
    "PermitRootLogin = false",
    "AllowUsers = ana, neri",
    "# Fin de archivo",
]

parametros = cargar_configuracion(archivo_sshd)
print(parametros)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Simula un *parser* (analizador) de archivos de configuración estilo Linux (`clave = valor`). Ignora líneas en blanco y comentarios (que empiezan con `#`), y convierte automáticamente los valores numéricos a `int` y los booleanos `"true"`/`"false"` a tipo `bool` de Python.
* **Detalle técnico paso a paso:**
  1. Por cada línea aplica `.strip()` para quitar espacios iniciales y finales.
  2. Filtra con `if limpia != "" and not limpia.startswith("#"):` para procesar solo directivas activas.
  3. Divide por el primer signo `"="` usando `split("=", 1)` y limpia espacios de `clave` y `valor`.
  4. Si `valor.isdigit()` es verdadero, lo guarda como entero (`int(valor)`). Si en minúsculas es `"true"` o `"false"`, evalúa la expresión booleana `valor.lower() == "true"` (que da `True` o `False`). En cualquier otro caso, conserva el `str`.
* **Salida exacta por pantalla:**
```text
{'Port': 2222, 'PermitRootLogin': False, 'AllowUsers': 'ana, neri'}
```

---

## Bloque 4: Ventana de mantenimiento y ejecución de tareas por tiempo (`while`)
**Temas integrados:** *Funciones (U4), ciclo `while` con doble condición de corte (U5), lista de tuplas (U6), acumuladores.*

### Código a analizar
```python
def ejecutar_ventana_mantenimiento(cola_tareas, minutos_disponibles):
    completadas = []
    tiempo_usado = 0
    i = 0

    while i < len(cola_tareas) and (tiempo_usado + cola_tareas[i][1]) <= minutos_disponibles:
        nombre_tarea, duracion = cola_tareas[i]
        completadas.append(nombre_tarea)
        tiempo_usado += duracion
        i += 1

    pendientes = len(cola_tareas) - len(completadas)
    return completadas, tiempo_usado, pendientes


tareas = [
    ("snapshot_disco", 10),
    ("actualizar_kernel", 15),
    ("migrar_tablas", 20),
    ("optimizar_indices", 10),
]

hechas, minutos, restantes = ejecutar_ventana_mantenimiento(tareas, 30)
print("Ejecutadas:", hechas)
print(f"Tiempo empleado: {minutos} min | Pendientes: {restantes}")
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Simula la ejecución secuencial de una cola de tareas de mantenimiento dentro de una ventana de tiempo máxima (`30` minutos). Ejecuta tareas en orden mientras la siguiente tarea entre en el tiempo restante; apenas una tarea excede el tiempo disponible, detiene la ejecución.
* **Detalle técnico paso a paso:**
  1. Utiliza un ciclo `while` que verifica dos condiciones antes de entrar: que queden tareas (`i < len(cola_tareas)`) y que sumar la duración de la tarea actual `cola_tareas[i][1]` no supere `minutos_disponibles`.
  2. En la primera vuelta (`i=0`), `"snapshot_disco"` dura `10` (`10 <= 30`): se agrega y `tiempo_usado` pasa a `10`.
  3. En la segunda vuelta (`i=1`), `"actualizar_kernel"` dura `15` (`10 + 15 = 25 <= 30`): se agrega y `tiempo_usado` pasa a `25`.
  4. Al evaluar `i=2` (`"migrar_tablas"`, duración `20`), `25 + 20 = 45 > 30`, por lo que la condición del `while` da `False` y el bucle corta sin ejecutar `"migrar_tablas"` ni `"optimizar_indices"`.
* **Salida exacta por pantalla:**
```text
Ejecutadas: ['snapshot_disco', 'actualizar_kernel']
Tiempo empleado: 25 min | Pendientes: 2
```

---

## Bloque 5: Resolución de nombres DNS local con caché y conteo de fallos
**Temas integrados:** *Funciones (U4), diccionarios (U6), listas (U6), método `.get()`, condicionales (U3).*

### Código a analizar
```python
def resolver_dominios(consultas, tabla_hosts):
    resueltos = []
    no_encontrados = set()

    for dominio in consultas:
        ip = tabla_hosts.get(dominio)
        if ip is not None:
            resueltos.append((dominio, ip))
        else:
            no_encontrados.add(dominio)

    return resueltos, sorted(no_encontrados)


hosts = {
    "intranet.curza.edu.ar": "10.10.1.5",
    "pedco.uncoma.edu.ar": "170.210.80.12",
    "git.interno.lan": "10.10.1.20",
}
peticiones = [
    "intranet.curza.edu.ar",
    "correo.uncoma.edu.ar",
    "git.interno.lan",
    "correo.uncoma.edu.ar",
]

exitos, fallos_unicos = resolver_dominios(peticiones, hosts)
print("Resueltos:", exitos)
print("Dominios sin registro (únicos):", fallos_unicos)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Simula la resolución de nombres de dominio contra un diccionario local (similar a `/etc/hosts`). Devuelve una lista de tuplas `(dominio, ip)` para cada consulta exitosa y una lista ordenada sin duplicados de los dominios que no pudieron resolverse.
* **Detalle técnico paso a paso:**
  1. Recorre la lista `consultas` y busca cada dominio en `tabla_hosts` usando `.get(dominio)`, que devuelve `None` si la clave no existe (evitando un `KeyError`).
  2. Si encuentra la IP, guarda el par `(dominio, ip)` en la lista `resueltos`.
  3. Si es `None`, agrega el dominio al conjunto `no_encontrados` (`set`), lo que descarta automáticamente las consultas repetidas a `"correo.uncoma.edu.ar"`.
* **Salida exacta por pantalla:**
```text
Resueltos: [('intranet.curza.edu.ar', '10.10.1.5'), ('git.interno.lan', '10.10.1.20')]
Dominios sin registro (únicos): ['correo.uncoma.edu.ar']
```

---

## Bloque 6: Rotación y clasificación de logs por tamaño y extensión
**Temas integrados:** *Funciones (U4), cadenas (`endswith`), lista de tuplas, *slicing*, acumuladores.*

### Código a analizar
```python
def clasificar_archivos_var_log(archivos, tamano_max_mb):
    comprimir = []
    espacio_recuperable = 0

    for nombre, tamano_mb in archivos:
        if nombre.endswith(".log") and tamano_mb >= tamano_max_mb:
            comprimir.append(nombre + ".gz")
            espacio_recuperable += int(tamano_mb * 0.7)

    return comprimir, espacio_recuperable


directorio_log = [
    ("syslog.log", 50),
    ("auth.log", 12),
    ("kern.log.gz", 80),
    ("apache_access.log", 100),
    (" notas.txt", 40),
]

nuevos_gz, ahorro_mb = clasificar_archivos_var_log(directorio_log, 30)
print("Archivos a comprimir:", nuevos_gz)
print("Ahorro estimado (MB):", ahorro_mb)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Examina una lista de archivos de `/var/log` con su tamaño en MB y selecciona aquellos que terminan en `".log"` (aún no comprimidos) y cuyo tamaño es mayor o igual a `30 MB`. Genera sus futuros nombres `".log.gz"` y estima un ahorro de espacio del 70%.
* **Detalle técnico paso a paso:**
  1. Filtra con condición compuesta `nombre.endswith(".log") and tamano_mb >= tamano_max_mb`.
  2. Notar que `"kern.log.gz"` tiene `80 MB` pero no cumple `endswith(".log")`, por lo que se ignora correctamente. `"auth.log"` termina en `.log` pero pesa `12 MB` (`< 30`), así que también se ignora.
  3. Para `"syslog.log"` (`50 MB`) y `"apache_access.log"` (`100 MB`), concatena `".gz"` y acumula `int(50 * 0.7) = 35` más `int(100 * 0.7) = 70`.
* **Salida exacta por pantalla:**
```text
Archivos a comprimir: ['syslog.log.gz', 'apache_access.log.gz']
Ahorro estimado (MB): 105
```

---

## Bloque 7: Verificación de reglas de Firewall por puerto y protocolo
**Temas integrados:** *Funciones (U4), diccionarios con claves de tipo tupla `(puerto, protocolo)` (U6), recorrido de solicitudes.*

### Código a analizar
```python
def evaluar_trafico(paquetes_entrantes, reglas_ufw):
    bloqueados = 0
    for origen_ip, puerto, protocolo in paquetes_entrantes:
        clave_regla = (puerto, protocolo)
        accion = reglas_ufw.get(clave_regla, "DROP")
        print(f"{origen_ip} -> {puerto}/{protocolo}: {accion}")
        if accion == "DROP":
            bloqueados += 1
    return bloqueados


reglas = {
    (22, "TCP"): "ALLOW",
    (80, "TCP"): "ALLOW",
    (443, "TCP"): "ALLOW",
    (53, "UDP"): "ALLOW",
}

trafico = [
    ("192.168.1.50", 22, "TCP"),
    ("10.0.0.99", 22, "UDP"),
    ("172.16.0.4", 443, "TCP"),
    ("200.10.5.1", 3306, "TCP"),
]

total_drop = evaluar_trafico(trafico, reglas)
print("Total paquetes bloqueados:", total_drop)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Simula el filtrado de paquetes de un firewall (como `ufw` o `iptables`) con política por defecto denegada (`DROP`). Evalúa cada paquete entrante según el par `(puerto, protocolo)`.
* **Detalle técnico paso a paso:**
  1. Aprovecha que las **tuplas son inmutables** para usarlas como claves del diccionario `reglas` (ej. `(22, "TCP")`).
  2. Para cada paquete entrante arma la tupla `clave_regla = (puerto, protocolo)` y consulta `reglas_ufw.get(clave_regla, "DROP")`.
  3. El segundo paquete va al puerto `22` pero por protocolo `"UDP"`; como `(22, "UDP")` no está en el diccionario, devuelve el valor por defecto `"DROP"`. Lo mismo ocurre con `(3306, "TCP")`.
* **Salida exacta por pantalla:**
```text
192.168.1.50 -> 22/TCP: ALLOW
10.0.0.99 -> 22/UDP: DROP
172.16.0.4 -> 443/TCP: ALLOW
200.10.5.1 -> 3306/TCP: DROP
Total paquetes bloqueados: 2
```

---

## Bloque 8: Búsqueda del servidor con menor carga para balanceo (Mínimo condicional)
**Temas integrados:** *Funciones (U4), búsqueda de mínimo en diccionario de diccionarios (U6/U5), manejo de `None`.*

### Código a analizar
```python
def elegir_nodo_destino(nodos):
    mejor_nodo = None
    menor_carga = None

    for nombre, estado in nodos.items():
        if estado["online"] and estado["conexiones"] < estado["max_conexiones"]:
            if menor_carga is None or estado["conexiones"] < menor_carga:
                menor_carga = estado["conexiones"]
                mejor_nodo = nombre

    return mejor_nodo, menor_carga


backend = {
    "app-node1": {"online": True, "conexiones": 45, "max_conexiones": 50},
    "app-node2": {"online": False, "conexiones": 0, "max_conexiones": 50},
    "app-node3": {"online": True, "conexiones": 18, "max_conexiones": 50},
    "app-node4": {"online": True, "conexiones": 50, "max_conexiones": 50},
}

elegido, conexiones_actuales = elegir_nodo_destino(backend)
print(f"Redirigir petición a: {elegido} ({conexiones_actuales} conexiones activas)")
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Implementa el algoritmo *Least Connections* (menor cantidad de conexiones) de un balanceador de carga. Busca entre los nodos del clúster aquel que esté en línea (`online == True`), no haya alcanzado su capacidad máxima y tenga el menor número de conexiones activas.
* **Detalle técnico paso a paso:**
  1. Descarta `"app-node2"` (aunque tiene `0` conexiones) porque `online` es `False`.
  2. Descarta `"app-node4"` porque `conexiones == max_conexiones` (`50 < 50` es `False`).
  3. Entre `"app-node1"` (`45`) y `"app-node3"` (`18`), actualiza el mínimo utilizando la técnica de iniciación con `None` (`if menor_carga is None or estado["conexiones"] < menor_carga`).
* **Salida exacta por pantalla:**
```text
Redirigir petición a: app-node3 (18 conexiones activas)
```

---

## Bloque 9: Normalización de nombres de usuario desde planilla de ingresantes
**Temas integrados:** *Funciones (U4), manejo de strings (`lower`, `split`), diccionarios para sufijos de colisión (U6).*

### Código a analizar
```python
def generar_cuentas_institucionales(nombres_completos):
    generados = []
    apariciones = {}

    for persona in nombres_completos:
        partes = persona.lower().split()
        base = partes[0][0] + partes[-1]
        cantidad = apariciones.get(base, 0) + 1
        apariciones[base] = cantidad

        if cantidad == 1:
            generados.append(base)
        else:
            generados.append(f"{base}{cantidad}")

    return generados


ingresantes = ["Ana Gomez", "Luis Perez", "Alberto Gomez", "Ana Lopez", "Andres Gomez"]
print(generar_cuentas_institucionales(ingresantes))
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Genera nombres de usuario para el sistema a partir de `"Nombre Apellido"` tomando la inicial del primer nombre más el apellido en minúsculas (ej. `"agomez"`). Si se produce una colisión (dos personas generan la misma base), le agrega un número secuencial (`"agomez2"`, `"agomez3"`).
* **Detalle técnico paso a paso:**
  1. `persona.lower().split()` convierte a minúsculas y separa en palabras.
  2. `partes[0][0]` obtiene la primera letra del nombre y `partes[-1]` el apellido.
  3. El diccionario `apariciones` lleva la cuenta de cuántas veces se generó cada `base`.
  4. `"Ana Gomez"` $\rightarrow$ `"agomez"` (1° vez); `"Alberto Gomez"` $\rightarrow$ `"agomez2"` (2° vez); `"Andres Gomez"` $\rightarrow$ `"agomez3"` (3° vez).
* **Salida exacta por pantalla:**
```text
['agomez', 'lperez', 'agomez2', 'alopez', 'agomez3']
```

---

## Bloque 10: Detección de cambios de integridad de archivos (Hashes)
**Temas integrados:** *Funciones (U4), comparación de dos diccionarios (U6), recorrido de claves.*

### Código a analizar
```python
def verificar_integridad(base_firmas, firmas_actuales):
    modificados = []
    eliminados = []
    nuevos = []

    for ruta, hash_original in base_firmas.items():
        if ruta not in firmas_actuales:
            eliminados.append(ruta)
        elif firmas_actuales[ruta] != hash_original:
            modificados.append(ruta)

    for ruta in firmas_actuales:
        if ruta not in base_firmas:
            nuevos.append(ruta)

    return modificados, eliminados, nuevos


ayer = {"/etc/passwd": "a1b2", "/etc/hosts": "c3d4", "/etc/crontab": "e5f6"}
hoy = {"/etc/passwd": "a1b2", "/etc/hosts": "9999", "/etc/sudoers": "7788"}

mod, elim, nue = verificar_integridad(ayer, hoy)
print("Modificados:", mod)
print("Eliminados:", elim)
print("Nuevos:", nue)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Simula una herramienta de monitoreo de integridad de archivos (estilo *Tripwire* o *AIDE*). Compara las firmas (hashes) de archivos críticos del sistema tomadas ayer contra las de hoy para detectar qué archivos fueron modificados, cuáles fueron borrados y cuáles aparecieron nuevos.
* **Detalle técnico paso a paso:**
  1. Primer ciclo `for`: recorre los archivos de `base_firmas` (`ayer`). Si una ruta no está en `hoy` (`/etc/crontab`), la agrega a `eliminados`. Si está pero su valor cambió (`/etc/hosts`: `"c3d4" != "9999"`), la agrega a `modificados`.
  2. Segundo ciclo `for`: recorre las claves de `firmas_actuales` (`hoy`). Si alguna clave no existía en `ayer` (`/etc/sudoers`), la agrega a `nuevos`.
* **Salida exacta por pantalla:**
```text
Modificados: ['/etc/hosts']
Eliminados: ['/etc/crontab']
Nuevos: ['/etc/sudoers']
```

---

## Bloque 11: Verificador de cuotas de disco y bloqueo preventivo
**Temas integrados:** *Funciones que modifican estructuras o retornan reportes (U4), listas por comprensión o filtrado (U6), porcentajes.*

### Código a analizar
```python
def auditar_cuotas(usuarios_home, cuota_mb):
    excedidos = []
    en_riesgo = []

    for usuario, carpetas in usuarios_home.items():
        total_usado = 0
        for mb in carpetas:
            total_usado += mb
        porcentaje = (total_usado * 100) / cuota_mb

        if porcentaje > 100:
            excedidos.append((usuario, round(porcentaje, 1)))
        elif porcentaje >= 80:
            en_riesgo.append((usuario, round(porcentaje, 1)))

    return excedidos, en_riesgo


homes = {
    "ana": [120, 80, 50],
    "luis": [300, 150, 100],
    "caro": [200, 220],
    "juan": [40, 30],
}

bloqueados, avisos = auditar_cuotas(homes, 500)
print("Cuota excedida (>100%):", bloqueados)
print("Advertencia (>=80%):", avisos)
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Calcula el espacio total utilizado por cada usuario en `/home` sumando los tamaños de sus subcarpetas (diccionario de listas con bucles `for` anidados) y compara el total contra una cuota fija de `500 MB`.
* **Detalle técnico paso a paso:**
  1. El bucle externo recorre `usuario, carpetas` en `usuarios_home.items()`.
  2. El bucle interno suma los MB de cada carpeta en el acumulador `total_usado` (que se reinicia correctamente en `0` para cada usuario).
  3. Calcula el porcentaje respecto de `500 MB`:
     * `"ana"`: `250 MB` ($50.0\%$) $\rightarrow$ normal.
     * `"luis"`: `550 MB` ($110.0\%$) $\rightarrow$ entra en `excedidos`.
     * `"caro"`: `420 MB` ($84.0\%$) $\rightarrow$ entra en `en_riesgo`.
     * `"juan"`: `70 MB` ($14.0\%$) $\rightarrow$ normal.
* **Salida exacta por pantalla:**
```text
Cuota excedida (>100%): [('luis', 110.0)]
Advertencia (>=80%): [('caro', 84.0)]
```

---

## Bloque 12: Compresión de ráfagas de eventos en logs (Corte de control / Agrupamiento consecutivo)
**Temas integrados:** *Funciones (U4), recorrido por índices o estado previo (U5), listas y tuplas (U6).*

### Código a analizar
```python
def comprimir_eventos_repetidos(eventos):
    if not eventos:
        return []

    compactados = []
    actual = eventos[0]
    contador = 1

    for e in eventos[1:]:
        if e == actual:
            contador += 1
        else:
            compactados.append((actual, contador))
            actual = e
            contador = 1

    compactados.append((actual, contador))
    return compactados


historial_servicio = ["OK", "OK", "OK", "TIMEOUT", "TIMEOUT", "OK", "ERROR"]
print(comprimir_eventos_repetidos(historial_servicio))
```

### Descripción de lo que hace (Guía Docente)
* **Propósito general:** Agrupa eventos consecutivos idénticos en una secuencia de monitoreo (técnica conocida como *Run-Length Encoding* o corte de control), igual a cuando `syslog` agrupa mensajes repetidos indicando *"last message repeated N times"*.
* **Detalle técnico paso a paso:**
  1. Toma el primer elemento `eventos[0]` como `actual` e inicia `contador = 1`.
  2. Recorre desde el segundo elemento usando *slicing* `eventos[1:]`.
  3. Mientras el evento sea igual al `actual`, incrementa `contador`. Cuando cambia de valor, guarda la tupla `(actual, contador)` en `compactados`, actualiza `actual = e` y reinicia `contador = 1`.
  4. Al salir del `for`, agrega la última ráfaga que quedó abierta (`("ERROR", 1)`).
  5. *(Nota clave para preguntar en coloquio)*: Si `"OK"` vuelve a aparecer más adelante, se cuenta en una tupla nueva porque solo agrupa repeticiones **consecutivas** (a diferencia de un diccionario de frecuencias globales).
* **Salida exacta por pantalla:**
```text
[('OK', 3), ('TIMEOUT', 2), ('OK', 1), ('ERROR', 1)]
```
