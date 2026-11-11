# Bloques de Código que No Funcionan: Diagnóstico, Corrección y Descripción

**Asignatura:** Introducción a la Programación (2° Cuatrimestre 2026)  
**Carrera:** Tecnicatura Universitaria en Administración de Sistemas y Software Libre (TUASySL)  

> **Consigna general para el estudiante:**  
> El siguiente bloque de código contiene uno o más errores (de sintaxis, de tipos en tiempo de ejecución o de lógica) que impiden que cumpla su objetivo.
> 1. **Diagnosticá el fallo:** Indicá qué excepción muestra Python (o por qué la salida es incorrecta) y explicá la causa técnica con tus palabras.
> 2. **Aplicá la solución:** Reescribí el código corregido respetando las estructuras y funciones planteadas.
> 3. **Explicá qué hace:** Describí brevemente cómo funciona la versión corregida y cuál es su salida exacta.

---

## Bloque 1: Retorno prematuro (`return` dentro del ciclo `for`) en verificación de puertos
**Temas evaluados:** *Funciones (U4), `for` (U5), condicionales (U3), listas (U6).*

### Código que no funciona
```python
def todos_puertos_seguros(lista_puertos, prohibidos):
    for p in lista_puertos:
        if p in prohibidos:
            return False
        else:
            return True


abiertos = [22, 80, 23, 443]
inseguros = (21, 23, 69)  # FTP, Telnet, TFTP
print("¿Servidor seguro?:", todos_puertos_seguros(abiertos, inseguros))
```

### Diagnóstico del problema
* **Qué muestra Python:** Imprime `¿Servidor seguro?: True` (resultado **incorrecto**, ya que el puerto `23` está abierto y figura entre los prohibidos).
* **Causa del fallo:** El `else: return True` está **dentro del ciclo `for`**. En la primera iteración evalúa `p = 22`; como `22` no está en `prohibidos`, ejecuta `return True` y **corta inmediatamente la función** sin revisar los demás elementos de la lista (`80`, `23`, `443`).

### Código corregido y descripción de lo que hace
```python
def todos_puertos_seguros(lista_puertos, prohibidos):
    """Retorna False si algún puerto abierto está prohibido; True si todos son seguros."""
    for p in lista_puertos:
        if p in prohibidos:
            return False
    return True


abiertos = [22, 80, 23, 443]
inseguros = (21, 23, 69)
print("¿Servidor seguro?:", todos_puertos_seguros(abiertos, inseguros))
```
* **Descripción de lo que hace:** La función recorre todos los puertos abiertos buscando si alguno pertenece a la tupla `prohibidos`. Si encuentra al menos uno inseguro (como el `23`), retorna `False` de inmediato. Recién cuando el bucle `for` termina de revisar toda la lista sin haber encontrado ningún puerto prohibido, retorna `True` fuera del ciclo.
* **Salida esperada:**
```text
¿Servidor seguro?: False
```

---

## Bloque 2: Función que imprime en lugar de retornar (`NoneType`)
**Temas evaluados:** *Funciones: `print` vs `return` (U4), operaciones aritméticas, listas (U6).*

### Código que no funciona
```python
def calcular_memoria_total(modulos_ram):
    suma = 0
    for mb in modulos_ram:
        suma += mb
    print(suma)


instalada = [4096, 4096, 8192]
total_mb = calcular_memoria_total(instalada)
total_gb = total_mb / 1024
print("Memoria en GB:", total_gb)
```

### Diagnóstico del problema
* **Qué muestra Python:**
  `TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'`
* **Causa del fallo:** La función `calcular_memoria_total()` usa `print(suma)` pero **no tiene sentencia `return`**. En Python, toda función sin `return` explícito devuelve `None`. Al asignarse `total_mb = None`, la línea siguiente intenta dividir `None / 1024`, provocando el `TypeError`.

### Código corregido y descripción de lo que hace
```python
def calcular_memoria_total(modulos_ram):
    """Suma los módulos de RAM en MB y retorna el total numérico."""
    suma = 0
    for mb in modulos_ram:
        suma += mb
    return suma


instalada = [4096, 4096, 8192]
total_mb = calcular_memoria_total(instalada)
total_gb = total_mb / 1024
print("Memoria en MB:", total_mb)
print("Memoria en GB:", total_gb)
```
* **Descripción de lo que hace:** La función acumula la capacidad de todos los módulos de memoria de la lista `instalada` y **retorna** el entero resultante (`16384`). El programa principal captura ese valor en `total_mb`, lo convierte a GB dividiendo por `1024` y muestra ambos valores.
* **Salida esperada:**
```text
Memoria en MB: 16384
Memoria en GB: 16.0
```

---

## Bloque 3: Modificación de lista mientras se la recorre con `for` y acceso inexistente en diccionario
**Temas evaluados:** *Listas y diccionarios (U6), iteración segura (U5), funciones (U4).*

### Código que no funciona
```python
def depurar_usuarios_inactivos(lista_usuarios, estados):
    for u in lista_usuarios:
        if estados[u] == "baja":
            lista_usuarios.remove(u)
    return lista_usuarios


usuarios = ["ana", "luis", "pedro", "caro", "invitado"]
padron = {"ana": "activo", "luis": "baja", "pedro": "baja", "caro": "activo"}
print("Activos:", depurar_usuarios_inactivos(usuarios, padron))
```

### Diagnóstico del problema
* **Qué muestra Python (dos errores combinados):**
  1. Primero, al borrar `"luis"` con `lista_usuarios.remove(u)` mientras se recorre `lista_usuarios`, los elementos siguientes se desplazan un índice hacia la izquierda y el `for` **se saltea a `"pedro"`** (que también tenía `"baja"`).
  2. Segundo, al llegar a `"invitado"`, falla con `KeyError: 'invitado'` porque esa clave no existe en el diccionario `padron` y se accedió con corchetes `estados[u]` en vez de `.get()`.

### Código corregido y descripción de lo que hace
```python
def depurar_usuarios_inactivos(lista_usuarios, estados):
    """Retorna una nueva lista solo con los usuarios cuyo estado en el padrón es 'activo'."""
    activos = []
    for u in lista_usuarios:
        if estados.get(u, "baja") != "baja":
            activos.append(u)
    return activos


usuarios = ["ana", "luis", "pedro", "caro", "invitado"]
padron = {"ana": "activo", "luis": "baja", "pedro": "baja", "caro": "activo"}
print("Activos:", depurar_usuarios_inactivos(usuarios, padron))
```
* **Descripción de lo que hace:** Recorre la lista original sin mutarla y construye una nueva lista `activos`. Consulta el estado de cada usuario mediante `estados.get(u, "baja")`: si el usuario tiene `"baja"` o no está registrado en el diccionario (como `"invitado"`), se descarta sin lanzar `KeyError` y sin saltear elementos.
* **Salida esperada:**
```text
Activos: ['ana', 'caro']
```

---

## Bloque 4: Intento de modificar tuplas e inicializar mal el acumulador
**Temas evaluados:** *Inmutabilidad de tuplas (U6), acumuladores en `for` (U5), funciones (U4).*

### Código que no funciona
```python
def aplicar_aumento_cuota(cuotas_usuarios, extra_gb):
    for i in range(len(cuotas_usuarios)):
        total_asignado = 0
        cuotas_usuarios[i][1] = cuotas_usuarios[i][1] + extra_gb
        total_asignado += cuotas_usuarios[i][1]
    return cuotas_usuarios, total_asignado


cuotas = [("ana", 10), ("luis", 15), ("caro", 20)]
nuevas, suma = aplicar_aumento_cuota(cuotas, 5)
print("Nuevas cuotas:", nuevas)
print("Total GB asignados:", suma)
```

### Diagnóstico del problema
* **Qué muestra Python:**
  1. `TypeError: 'tuple' object does not support item assignment` en la línea `cuotas_usuarios[i][1] = ...` porque cada elemento de la lista es una **tupla** `("ana", 10)` y las tuplas son inmutables.
  2. Además, hay un error lógico: `total_asignado = 0` está **dentro del `for`**, por lo que el acumulador se reinicia en cada vuelta y solo guardaría el valor del último usuario.

### Código corregido y descripción de lo que hace
```python
def aplicar_aumento_cuota(cuotas_usuarios, extra_gb):
    """Genera una nueva lista de tuplas incrementando la cuota en extra_gb y suma el total."""
    actualizadas = []
    total_asignado = 0
    for usuario, gb in cuotas_usuarios:
        nuevo_gb = gb + extra_gb
        actualizadas.append((usuario, nuevo_gb))
        total_asignado += nuevo_gb
    return actualizadas, total_asignado


cuotas = [("ana", 10), ("luis", 15), ("caro", 20)]
nuevas, suma = aplicar_aumento_cuota(cuotas, 5)
print("Nuevas cuotas:", nuevas)
print("Total GB asignados:", suma)
```
* **Descripción de lo que hace:** Inicializa el acumulador `total_asignado = 0` antes del ciclo. Recorre cada tupla desempaquetando `usuario, gb`, calcula la nueva cuota y crea una **nueva tupla** `(usuario, nuevo_gb)` que agrega a la lista `actualizadas`, acumulando el total de GB asignados en el servidor.
* **Salida esperada:**
```text
Nuevas cuotas: [('ana', 15), ('luis', 20), ('caro', 25)]
Total GB asignados: 60
```

---

## Bloque 5: Bucle infinito en `while` y falta de conversión de tipo en `split()`
**Temas evaluados:** *Ciclo `while` (U5), conversión `str` a `int` (U2), cadenas `split()` (U6).*

### Código que no funciona
```python
def buscar_primer_puerto_alto(reglas_texto):
    i = 0
    encontrado = None
    while i < len(reglas_texto) and encontrado is None:
        servicio, puerto = reglas_texto[i].split(":")
        if puerto >= 1024:
            encontrado = (servicio, puerto)
    return encontrado


config = ["ssh:22", "http:80", "mysql:3306", "redis:6379"]
print("Primer puerto >= 1024:", buscar_primer_puerto_alto(config))
```

### Diagnóstico del problema
* **Qué muestra Python:**
  1. Falla inmediatamente con `TypeError: '>=' not supported between instances of 'str' and 'int'` porque `.split(":")` devuelve cadenas de texto (`"22"`) y no se puede comparar `str >= int`.
  2. Si se corrigiera solo el `int(puerto)`, el programa entraría en un **bucle infinito** porque la variable de control `i` nunca se incrementa (`i += 1`) dentro del `while`.

### Código corregido y descripción de lo que hace
```python
def buscar_primer_puerto_alto(reglas_texto):
    """Busca con while el primer servicio que utilice un puerto no privilegiado (>= 1024)."""
    i = 0
    encontrado = None
    while i < len(reglas_texto) and encontrado is None:
        servicio, puerto_str = reglas_texto[i].split(":")
        puerto = int(puerto_str)
        if puerto >= 1024:
            encontrado = (servicio, puerto)
        i += 1
    return encontrado


config = ["ssh:22", "http:80", "mysql:3306", "redis:6379"]
print("Primer puerto >= 1024:", buscar_primer_puerto_alto(config))
```
* **Descripción de lo que hace:** Recorre la lista de cadenas `"servicio:puerto"` mediante un bucle `while` con bandera `encontrado is None`. Separa cada cadena por `":"`, convierte el puerto a entero con `int()` y, apenas halla el primero mayor o igual a `1024` (`"mysql"`, puerto `3306`), lo guarda en `encontrado` e incrementa `i`, deteniendo la búsqueda sin revisar el resto de la lista.
* **Salida esperada:**
```text
Primer puerto >= 1024: ('mysql', 3306)
```

---

## Bloque 6: Ámbito de variables (Scope local vs global) en contador de alertas
**Temas evaluados:** *Ámbito de variables y parámetros en funciones (U2, U4), `UnboundLocalError`.*

### Código que no funciona
```python
total_alertas = 0


def registrar_eventos(temperaturas_cpu, umbral):
    for temp in temperaturas_cpu:
        if temp > umbral:
            print("Alerta de temperatura:", temp)
            total_alertas += 1


lecturas = [55, 62, 85, 49, 91]
registrar_eventos(lecturas, 80)
print("Total de alertas registradas:", total_alertas)
```

### Diagnóstico del problema
* **Qué muestra Python:**
  `UnboundLocalError: cannot access local variable 'total_alertas' where it is not associated with a value`
* **Causa del fallo:** Al intentar hacer `total_alertas += 1` dentro de la función, Python asume que `total_alertas` es una **variable local** de `registrar_eventos`, pero no fue inicializada localmente antes de sumarle `1`. Según las buenas prácticas de la Unidad 4, las funciones no deben modificar variables globales directamente, sino inicializar su propio contador local y **retornarlo**.

### Código corregido y descripción de lo que hace
```python
def registrar_eventos(temperaturas_cpu, umbral):
    """Imprime las temperaturas que superan el umbral y retorna cuántas alertas hubo."""
    alertas_locales = 0
    for temp in temperaturas_cpu:
        if temp > umbral:
            print("Alerta de temperatura:", temp)
            alertas_locales += 1
    return alertas_locales


lecturas = [55, 62, 85, 49, 91]
total_alertas = registrar_eventos(lecturas, 80)
print("Total de alertas registradas:", total_alertas)
```
* **Descripción de lo que hace:** La función define una variable local `alertas_locales = 0`, recorre las lecturas de temperatura de la CPU, informa por pantalla aquellas que superan los `80` grados y retorna la cantidad total contada para asignarla a `total_alertas` en el programa principal.
* **Salida esperada:**
```text
Alerta de temperatura: 85
Alerta de temperatura: 91
Total de alertas registradas: 2
```

---

## Bloque 7: Error al desempaquetar diccionario sin `.items()` y uso de `.sort()` sobre `None`
**Temas evaluados:** *Recorrido de diccionarios (U6), diferencia entre `.sort()` y `sorted()` (U6), funciones (U4).*

### Código que no funciona
```python
def listar_servicios_activos_ordenados(mapa_servicios):
    activos = []
    for servicio, estado in mapa_servicios:
        if estado == "activo":
            activos.append(servicio)
    return activos.sort()


servicios = {"ssh": "activo", "cups": "inactivo", "apache2": "activo", "cron": "activo"}
print("Activos A-Z:", listar_servicios_activos_ordenados(servicios))
```

### Diagnóstico del problema
* **Qué muestra Python:**
  1. Primero lanza `ValueError: too many values to unpack (expected 2)` en `for servicio, estado in mapa_servicios:` porque iterar directamente sobre un diccionario devuelve solo sus **claves** (`"ssh"`, `"cups"`, etc.) y no pares `(clave, valor)`. Falta usar `.items()`.
  2. Segundo, `return activos.sort()` ordena la lista en el lugar (*in-place*) pero **devuelve `None`**. Se debe usar `return sorted(activos)` (o hacer `activos.sort()` en una línea y `return activos` en la siguiente).

### Código corregido y descripción de lo que hace
```python
def listar_servicios_activos_ordenados(mapa_servicios):
    """Filtra los servicios activos del diccionario y los retorna ordenados alfabéticamente."""
    activos = []
    for servicio, estado in mapa_servicios.items():
        if estado == "activo":
            activos.append(servicio)
    return sorted(activos)


servicios = {"ssh": "activo", "cups": "inactivo", "apache2": "activo", "cron": "activo"}
print("Activos A-Z:", listar_servicios_activos_ordenados(servicios))
```
* **Descripción de lo que hace:** Recorre los pares `(servicio, estado)` del diccionario mediante `.items()`, filtra los que tienen estado `"activo"` guardándolos en una lista y devuelve una nueva lista ordenada alfabéticamente con `sorted()`.
* **Salida esperada:**
```text
Activos A-Z: ['apache2', 'cron', 'ssh']
```

---

## Bloque 8: Condición booleana defectuosa (`or` en vez de `and` y trampa de *truthiness*)
**Temas evaluados:** *Expresiones booleanas y operadores lógicos (U2, U3), validación de entradas.*

### Código que no funciona
```python
def es_puerto_usable(puerto, estado_firewall):
    # Debe ser usable solo si el puerto es 80 o 443, y el firewall NO está en "bloqueo_total"
    if (puerto == 80 or 443) and estado_firewall != "bloqueo_total":
        return True
    return False


print("Puerto 80:", es_puerto_usable(80, "normal"))
print("Puerto 22:", es_puerto_usable(22, "normal"))
```

### Diagnóstico del problema
* **Qué muestra Python:** Imprime `True` tanto para el puerto `80` como para el puerto `22` (resultado **incorrecto**, el puerto `22` debería dar `False`).
* **Causa del fallo:** En Python, la expresión `(puerto == 80 or 443)` se evalúa como `(puerto == 80) or bool(443)`. Como cualquier número distinto de cero (`443`) tiene valor de verdad `True`, la condición completa del paréntesis da **siempre `True`** sin importar qué valor tenga `puerto`. Debe escribirse `puerto == 80 or puerto == 443` (o mejor aún: `puerto in (80, 443)`).

### Código corregido y descripción de lo que hace
```python
def es_puerto_usable(puerto, estado_firewall):
    """Retorna True únicamente si el puerto es 80 o 443 y el firewall no está en bloqueo_total."""
    return puerto in (80, 443) and estado_firewall != "bloqueo_total"


print("Puerto 80:", es_puerto_usable(80, "normal"))
print("Puerto 22:", es_puerto_usable(22, "normal"))
```
* **Descripción de lo que hace:** Verifica correctamente si el valor de `puerto` pertenece a la tupla `(80, 443)` y además comprueba que el estado del firewall sea distinto de `"bloqueo_total"`, retornando el booleano correspondiente.
* **Salida esperada:**
```text
Puerto 80: True
Puerto 22: False
```

---

## Bloque 9: Mutación accidental del diccionario original de configuración
**Temas evaluados:** *Referencias a diccionarios vs copia `.copy()` (U6), funciones (U4).*

### Código que no funciona
```python
def simular_modo_mantenimiento(config_produccion):
    temporal = config_produccion
    temporal["modo"] = "mantenimiento"
    temporal["max_usuarios"] = 0
    return temporal


produccion = {"modo": "activo", "max_usuarios": 500, "ssl": True}
simulacion = simular_modo_mantenimiento(produccion)
print("Simulación:", simulacion)
print("Producción original:", produccion)
```

### Diagnóstico del problema
* **Qué muestra Python:** Tanto `Simulación` como `Producción original` muestran `'modo': 'mantenimiento', 'max_usuarios': 0` (se corrompió el diccionario original de producción).
* **Causa del fallo:** Hacer `temporal = config_produccion` **no crea una copia** del diccionario, sino una referencia (alias) al mismo objeto en memoria. Al modificar `temporal`, se modifica también el diccionario `produccion` del programa principal. Se debe usar `config_produccion.copy()`.

### Código corregido y descripción de lo que hace
```python
def simular_modo_mantenimiento(config_produccion):
    """Retorna una copia de la configuración ajustada a modo mantenimiento sin alterar la original."""
    temporal = config_produccion.copy()
    temporal["modo"] = "mantenimiento"
    temporal["max_usuarios"] = 0
    return temporal


produccion = {"modo": "activo", "max_usuarios": 500, "ssl": True}
simulacion = simular_modo_mantenimiento(produccion)
print("Simulación:", simulacion)
print("Producción original:", produccion)
```
* **Descripción de lo que hace:** Crea una copia superficial independiente del diccionario recibido mediante `.copy()`, sobrescribe las claves `"modo"` y `"max_usuarios"` en la copia y la retorna, preservando intactos los datos de `produccion`.
* **Salida esperada:**
```text
Simulación: {'modo': 'mantenimiento', 'max_usuarios': 0, 'ssl': True}
Producción original: {'modo': 'activo', 'max_usuarios': 500, 'ssl': True}
```

---

## Bloque 10: Desbordamiento de índice (`IndexError`) al comparar mediciones consecutivas
**Temas evaluados:** *Recorrido por índices con `range()` (U5), listas (U6), funciones (U4).*

### Código que no funciona
```python
def detectar_picos_trafico(mediciones_mbps, salto_minimo):
    picos = []
    for i in range(len(mediciones_mbps)):
        diferencia = mediciones_mbps[i + 1] - mediciones_mbps[i]
        if diferencia >= salto_minimo:
            picos.append((mediciones_mbps[i], mediciones_mbps[i + 1]))
    return picos


red = [100, 110, 250, 240, 400]
print("Saltos bruscos:", detectar_picos_trafico(red, 100))
```

### Diagnóstico del problema
* **Qué muestra Python:**
  `IndexError: list index out of range`
* **Causa del fallo:** La lista tiene 5 elementos (índices `0` a `4`). Cuando el bucle llega a la última vuelta (`i = 4`), la expresión `mediciones_mbps[i + 1]` intenta acceder al índice `5`, que no existe. Cuando se comparan pares adyacentes (`i` con `i + 1`), el `range` debe detenerse un elemento antes: `range(len(mediciones_mbps) - 1)`.

### Código corregido y descripción de lo que hace
```python
def detectar_picos_trafico(mediciones_mbps, salto_minimo):
    """Compara mediciones consecutivas y retorna los pares donde el tráfico subió >= salto_minimo."""
    picos = []
    for i in range(len(mediciones_mbps) - 1):
        diferencia = mediciones_mbps[i + 1] - mediciones_mbps[i]
        if diferencia >= salto_minimo:
            picos.append((mediciones_mbps[i], mediciones_mbps[i + 1]))
    return picos


red = [100, 110, 250, 240, 400]
print("Saltos bruscos:", detectar_picos_trafico(red, 100))
```
* **Descripción de lo que hace:** Recorre los índices desde `0` hasta `len(mediciones_mbps) - 2` comparando cada medición con su siguiente inmediata. Detecta aquellos intervalos donde el incremento fue de al menos `100 Mbps` (`110 -> 250` y `240 -> 400`).
* **Salida esperada:**
```text
Saltos bruscos: [(110, 250), (240, 400)]
```

---

## Bloque 11: Orden incorrecto de ramas `if/elif` en clasificación por rangos (Condición solapada)
**Temas evaluados:** *Estructuras alternativas múltiples `if/elif/else` (U3), funciones (U4).*

### Código que no funciona
```python
def clasificar_latencia_ms(milisegundos):
    if milisegundos > 0:
        return "ÓPTIMA"
    elif milisegundos > 100:
        return "MODERADA"
    elif milisegundos > 300:
        return "CRÍTICA"
    else:
        return "SIN RESPUESTA"


for ping in [25, 150, 420, -1]:
    print(ping, "ms ->", clasificar_latencia_ms(ping))
```

### Diagnóstico del problema
* **Qué muestra Python:** Clasifica `25`, `150` y `420` todos como `"ÓPTIMA"`.
* **Causa del fallo:** En una estructura `if/elif`, Python evalúa las condiciones de arriba hacia abajo y entra en la **primera que resulte verdadera**, descartando las demás. Como `150 > 0` y `420 > 0` son verdaderos en el primer `if`, nunca llega a los `elif` de `> 100` ni `> 300`. Al evaluar cotas inferiores con `>`, se debe ordenar desde el umbral **más estricto (mayor)** hacia el menor.

### Código corregido y descripción de lo que hace
```python
def clasificar_latencia_ms(milisegundos):
    """Clasifica la latencia en ms desde el umbral más crítico hacia el más bajo."""
    if milisegundos > 300:
        return "CRÍTICA"
    elif milisegundos > 100:
        return "MODERADA"
    elif milisegundos > 0:
        return "ÓPTIMA"
    else:
        return "SIN RESPUESTA"


for ping in [25, 150, 420, -1]:
    print(ping, "ms ->", clasificar_latencia_ms(ping))
```
* **Descripción de lo que hace:** Evalúa primero si la latencia supera los `300 ms` (`"CRÍTICA"`), luego si supera los `100 ms` (`"MODERADA"`), luego si es positiva (`"ÓPTIMA"`) y finalmente captura valores $\le 0$ como `"SIN RESPUESTA"`.
* **Salida esperada:**
```text
25 ms -> ÓPTIMA
150 ms -> MODERADA
420 ms -> CRÍTICA
-1 ms -> SIN RESPUESTA
```

---

## Bloque 12: Error al usar métodos de conjuntos y cadenas inmutables
**Temas evaluados:** *Inmutabilidad de `str` (U2), conjuntos `set.add()` vs `list.append()` (U6), funciones (U4).*

### Código que no funciona
```python
def normalizar_tags_servidor(lista_tags):
    unicos = set()
    for tag in lista_tags:
        tag.strip()
        tag.lower()
        unicos.append(tag)
    return sorted(unicos)


etiquetas = [" Produccion ", "WEB", "produccion", "  web ", "DB"]
print("Tags normalizados:", normalizar_tags_servidor(etiquetas))
```

### Diagnóstico del problema
* **Qué muestra Python (dos errores combinados):**
  1. `AttributeError: 'set' object has no attribute 'append'` porque los conjuntos (`set`) no tienen método `.append()` (que es de listas), sino **`.add()`**.
  2. Además, las cadenas (`str`) en Python son **inmutables**: llamar a `tag.strip()` y `tag.lower()` sin reasignar el resultado a la variable (`tag = tag.strip().lower()`) no modifica la cadena `tag`, por lo que quedarían con espacios y mayúsculas repetidas.

### Código corregido y descripción de lo que hace
```python
def normalizar_tags_servidor(lista_tags):
    """Limpia espacios, pasa a minúsculas y retorna una lista ordenada sin tags repetidos."""
    unicos = set()
    for tag in lista_tags:
        limpio = tag.strip().lower()
        unicos.add(limpio)
    return sorted(unicos)


etiquetas = [" Produccion ", "WEB", "produccion", "  web ", "DB"]
print("Tags normalizados:", normalizar_tags_servidor(etiquetas))
```
* **Descripción de lo que hace:** Recorre la lista de etiquetas, encadena `.strip().lower()` guardando la nueva cadena normalizada en `limpio`, y la inserta en el conjunto `unicos` mediante `.add()`. Al ser un conjunto, elimina automáticamente los duplicados (`"produccion"` y `"web"`) y finalmente retorna una lista ordenada alfabéticamente.
* **Salida esperada:**
```text
Tags normalizados: ['db', 'produccion', 'web']
```
