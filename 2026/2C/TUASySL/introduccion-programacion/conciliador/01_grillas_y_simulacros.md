# Grillas de Evaluación y Simulacros de Parcial / Coloquio

**Asignatura:** Introducción a la Programación (2° Cuatrimestre 2026)  
**Carrera:** Tecnicatura Universitaria en Administración de Sistemas y Software Libre (TUASySL)  
**Institución:** CURZAS - Universidad Nacional del Comahue  

---

## Parte 1: Grillas de Evaluación (Rúbricas de Cátedra)

### 1.1. Rúbrica para Examen Parcial Sincrónico Teórico-Práctico
* **Condición para Regularizar:** $\ge 40 / 100$ puntos.
* **Condición para Promocionar:** $\ge 70 / 100$ puntos (en primera instancia).

| Dimensión Evaluada | Unidades | Peso | Logrado Destacado (100%) | Logrado Aceptable (60% - 80%) | Insuficiente (< 40%) |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **1. Análisis y Diseño Algorítmico (Polya)** | U1, U2 | **15%** | Identifica correctamente entradas, salidas, constantes y plantea una estrategia algorítmica clara antes de codificar. | Identifica entradas y salidas pero omite casos borde o presenta imprecisiones menores en el planteo. | No comprende el enunciado o codifica por prueba y error sin estructura lógica. |
| **2. Modularización y Funciones** | U4 | **25%** | Define funciones con encabezado correcto, parámetros formales pertinentes, *docstring*, respeta el ámbito local y retorna valores (`return`) aplicando *Divide y Vencerás*. | Define funciones pero mezcla lógica de impresión con cálculo, o presenta acoplamiento innecesario con variables del programa principal. | No utiliza funciones cuando se solicita, usa variables globales indebidamente o confunde `print()` con `return`. |
| **3. Estructuras de Control (Alternativas y Repetitivas)** | U3, U5 | **25%** | Selecciona adecuadamente `if/elif/else`, `for` (recorrido/rango) o `while` (condición de corte). Inicializa contadores, acumuladores y banderas en el lugar correcto. | Resuelve el problema pero utiliza condiciones redundantes, o emplea `while` cuando correspondía un `for` directo sobre la colección. | Bucles infinitos, reinicio de acumuladores dentro del ciclo, condiciones booleanas mal formadas (`=` en vez de `==`). |
| **4. Estructuras de Datos** | U6 | **25%** | Elige y manipula correctamente `list`, `tuple`, `set` o `dict` según el problema (ej. `.items()`, `.get()`, desempaquetado, `in`, *slicing*). | Utiliza las estructuras solicitadas pero realiza recorridos ineficientes (ej. buscar claves con un `for` en lugar de `in` o `.get()`). | Errores de tipo (`TypeError` al intentar mutar tuplas, `KeyError`, `IndexError`) o no aplica la estructura pedida. |
| **5. Sintaxis, Ejecución y Estilo (PEP 8)** | U2–U6 | **10%** | El script ejecuta sin errores en Python 3, produce la salida exacta y respeta `snake_case` y `SCREAMING_SNAKE_CASE`. | Ejecuta con errores menores de formato en la salida o nombres de variables poco descriptivos. | El código no ejecuta (`SyntaxError`, `IndentationError`) o no resuelve el caso de prueba dado. |

---

### 1.2. Rúbrica para Coloquio de Promoción (Sistemas - TUASySL)
De acuerdo con el **Programa 2026** (Sección 7) y el **Banco de Ejercicios para Coloquio**, cada estudiante resuelve **2 ejercicios sorteados** (o 3 si se incluye lectura de código):
1. **Ejercicio Práctico de Sistemas (con Modularización U4 y Estructuras U5/U6).**
2. **Ejercicio de Depuración / Análisis de Código (explicar qué hace o corregir un código que falla).**

| Criterio de Evaluación | Ponderación | Indicadores de Desempeño | Puntaje Obtenido |
| :--- | :---: | :--- | :---: |
| **1. Ejecución y Funcionamiento del Código** | **40%** | • El script corre en Python 3 sin errores de sintaxis ni excepciones en tiempo de ejecución.<br>• Produce la salida esperada para los datos de partida y contempla casos borde (ej. lista vacía, clave inexistente). | ___ / 40 |
| **2. Uso de Estructuras y Modularización** | **40%** | • Emplea las estructuras de datos indicadas en la consigna (`list`, `tuple`, `dict`, `set`).<br>• Encapsula la lógica en funciones reutilizables (U4) con parámetros y retorno.<br>• Utiliza los ciclos (`for`/`while`) y condicionales apropiados sin código muerto. | ___ / 40 |
| **3. Defensa Oral y Lenguaje Técnico de Cátedra** | **20%** | • Explica con precisión el flujo de ejecución (traza), diferenciando parámetros formales de actuales, claves de valores, e inmutabilidad.<br>• En el bloque con errores: identifica el tipo de excepción (`KeyError`, `TypeError`, `IndexError` o error lógico), explica su causa raíz y justifica la corrección. | ___ / 20 |
| **CALIFICACIÓN FINAL DEL COLOQUIO** | **100%** | *(Requiere demostrar solvencia integral para acreditar la promoción)* | **___ / 100** |

---

### 1.3. Planilla Rápida de Seguimiento por Estudiante (Coloquio / Parcial)

```markdown
Estudiante: ________________________________________ Legajo: ______________
Fecha: ___/___/2026   Modalidad: [ ] Presencial   [ ] Remoto Sincrónico (Cámara/DNI validados)

[ ] Ejercicio 1 (Desarrollo / Sistemas): N° ___ - Tema: ___________________________
    - Corre sin errores (20 pts):      ___
    - Estructuras y Funciones (20 pts): ___
    - Explicación y Traza (10 pts):    ___

[ ] Ejercicio 2 (Análisis / Depuración): N° ___ - Tema: ___________________________
    - Identifica fallo / propósito (20 pts): ___
    - Corrección con estructuras (20 pts):   ___
    - Precisión en lenguaje técnico (10 pts): ___

Observaciones docentes: ___________________________________________________________
Resultado Final: ___ / 100   Condición: [ ] PROMOCIONA   [ ] PASA A FINAL REGULAR
Firma Docente: _______________________
```

---

## Parte 2: Simulacro de 2° Parcial Sincrónico (Unidades 3, 4, 5 y 6)

**Duración estimada:** 90 minutos.  
**Pautas obligatorias:**
* Utilizar convención `snake_case` para variables y funciones, y `SCREAMING_SNAKE_CASE` para constantes.
* Todo procesamiento principal debe estar modularizado en **funciones** (Unidad 4) con su correspondiente *docstring*.
* No utilizar librerías externas.

---

### Ejercicio 1 (35 puntos): Auditoría de Cuentas del Sistema (`/etc/passwd`)
**Temas evaluados:** *Funciones (U4), lista de tuplas (U6), conjuntos (U6), ciclo `for` (U5), condicionales compuestos (U3).*

En un servidor Linux se extrajo una lista de tuplas con el formato `(usuario, uid, shell, grupo_primario)`.
1. Definir la constante `UID_MIN_HUMANO = 1000` y la tupla `SHELLS_INTERACTIVOS = ("/bin/bash", "/bin/zsh")`.
2. Escribir la función `filtrar_usuarios_interactivos(registros, uid_minimo, shells_validos)` que reciba la lista de tuplas y devuelva una **nueva lista** con los nombres de usuario que tienen `uid >= uid_minimo` y cuyo shell esté dentro de `shells_validos`.
3. Escribir la función `obtener_grupos_unicos(registros)` que reciba la lista de tuplas y devuelva un **conjunto (`set`)** con todos los grupos primarios presentes sin repeticiones.
4. En el programa principal, invocar ambas funciones con los datos de partida y mostrar los resultados.

#### Datos de partida:
```python
cuentas = [
    ("root", 0, "/bin/bash", "root"),
    ("daemon", 1, "/usr/sbin/nologin", "daemon"),
    ("ana", 1000, "/bin/bash", "sysadmin"),
    ("luis", 1001, "/bin/sh", "desarrollo"),
    ("caro", 1002, "/bin/zsh", "sysadmin"),
    ("www-data", 33, "/usr/sbin/nologin", "www-data"),
    ("neri", 1003, "/bin/bash", "desarrollo"),
]
```

#### Resolución Modelo (Ejercicio 1):
```python
"""Simulacro Parcial - Ejercicio 1: Auditoría de cuentas /etc/passwd."""

UID_MIN_HUMANO = 1000
SHELLS_INTERACTIVOS = ("/bin/bash", "/bin/zsh")


def filtrar_usuarios_interactivos(registros, uid_minimo, shells_validos):
    """Retorna una lista de usuarios con UID >= uid_minimo y shell interactivo."""
    # registros : list[tuple]
    # uid_minimo : int
    # shells_validos : tuple[str]
    usuarios_filtrados = []
    for usuario, uid, shell, _ in registros:
        if uid >= uid_minimo and shell in shells_validos:
            usuarios_filtrados.append(usuario)
    return usuarios_filtrados


def obtener_grupos_unicos(registros):
    """Retorna un conjunto con los nombres de grupos primarios únicos."""
    # registros : list[tuple]
    grupos = set()
    for _, _, _, grupo in registros:
        grupos.add(grupo)
    return grupos


# Programa principal
cuentas = [
    ("root", 0, "/bin/bash", "root"),
    ("daemon", 1, "/usr/sbin/nologin", "daemon"),
    ("ana", 1000, "/bin/bash", "sysadmin"),
    ("luis", 1001, "/bin/sh", "desarrollo"),
    ("caro", 1002, "/bin/zsh", "sysadmin"),
    ("www-data", 33, "/usr/sbin/nologin", "www-data"),
    ("neri", 1003, "/bin/bash", "desarrollo"),
]

interactivos = filtrar_usuarios_interactivos(cuentas, UID_MIN_HUMANO, SHELLS_INTERACTIVOS)
grupos_sistema = obtener_grupos_unicos(cuentas)

print("Usuarios humanos con shell interactivo:", interactivos)
print("Total encontrados:", len(interactivos))
print("Grupos únicos (ordenados):", sorted(grupos_sistema))
```

#### Salida esperada:
```text
Usuarios humanos con shell interactivo: ['ana', 'caro', 'neri']
Total encontrados: 3
Grupos únicos (ordenados): ['daemon', 'desarrollo', 'root', 'sysadmin', 'www-data']
```

---

### Ejercicio 2 (35 puntos): Monitoreo de Consumo en Clúster de Servidores
**Temas evaluados:** *Funciones (U4), diccionario de diccionarios (U6), recorrido `.items()` (U6), acumuladores (U5), condicionales (U3).*

Se dispone de un diccionario donde cada clave es el `hostname` de un servidor y su valor es otro diccionario con `{"cpu": int, "ram_gb": int, "activo": bool}`.
1. Definir la constante `UMBRAL_CPU_CRITICO = 85`.
2. Escribir la función `analizar_cluster(servidores, umbral_cpu)` que recorra el diccionario y retorne una **tupla de tres elementos**:
   * `alertas_cpu`: lista con los nombres de servidores **activos** cuyo uso de CPU sea mayor o igual a `umbral_cpu`.
   * `caidos`: lista con los nombres de servidores que tienen `"activo": False`.
   * `promedio_ram`: promedio de RAM (en GB) calculado **únicamente sobre los servidores activos** (si no hay activos, retornar `0.0`).
3. En el programa principal, desempaquetar el resultado de la función y mostrar el informe de estado.

#### Datos de partida:
```python
cluster = {
    "srv-web01": {"cpu": 92, "ram_gb": 16, "activo": True},
    "srv-db01": {"cpu": 88, "ram_gb": 32, "activo": True},
    "srv-cache": {"cpu": 10, "ram_gb": 8, "activo": False},
    "srv-proxy": {"cpu": 45, "ram_gb": 8, "activo": True},
    "srv-backup": {"cpu": 95, "ram_gb": 16, "activo": False},
}
```

#### Resolución Modelo (Ejercicio 2):
```python
"""Simulacro Parcial - Ejercicio 2: Monitoreo de Clúster de Servidores."""

UMBRAL_CPU_CRITICO = 85


def analizar_cluster(servidores, umbral_cpu):
    """Analiza el estado del clúster y retorna (alertas_cpu, caidos, promedio_ram_activos)."""
    # servidores : dict[str, dict]
    # umbral_cpu : int
    alertas_cpu = []
    caidos = []
    suma_ram_activos = 0
    cantidad_activos = 0

    for host, metricas in servidores.items():
        if not metricas["activo"]:
            caidos.append(host)
        else:
            cantidad_activos += 1
            suma_ram_activos += metricas["ram_gb"]
            if metricas["cpu"] >= umbral_cpu:
                alertas_cpu.append(host)

    promedio_ram = suma_ram_activos / cantidad_activos if cantidad_activos > 0 else 0.0
    return alertas_cpu, caidos, promedio_ram


# Programa principal
cluster = {
    "srv-web01": {"cpu": 92, "ram_gb": 16, "activo": True},
    "srv-db01": {"cpu": 88, "ram_gb": 32, "activo": True},
    "srv-cache": {"cpu": 10, "ram_gb": 8, "activo": False},
    "srv-proxy": {"cpu": 45, "ram_gb": 8, "activo": True},
    "srv-backup": {"cpu": 95, "ram_gb": 16, "activo": False},
}

sobrecargados, inactivos, ram_media = analizar_cluster(cluster, UMBRAL_CPU_CRITICO)

print("Servidores activos con CPU crítica:", sobrecargados)
print("Servidores caídos:", inactivos)
print(f"Promedio de RAM en servidores activos: {ram_media:.2f} GB")
```

#### Salida esperada:
```text
Servidores activos con CPU crítica: ['srv-web01', 'srv-db01']
Servidores caídos: ['srv-cache', 'srv-backup']
Promedio de RAM en servidores activos: 18.67 GB
```

---

### Ejercicio 3 (30 puntos): Cola de Despliegue con Condición de Corte (`while`)
**Temas evaluados:** *Funciones (U4), ciclo `while` con bandera de corte (U5), listas y tuplas (U6).*

Un sistema de integración continua procesa una lista de tareas de despliegue donde cada elemento es una tupla `(nombre_etapa, codigo_salida)`. Un `codigo_salida == 0` indica éxito; cualquier valor distinto de `0` indica fallo crítico y **debe detener inmediatamente** la ejecución de las etapas siguientes.
1. Escribir la función `ejecutar_pipeline(etapas)` que recorra la lista usando un ciclo **`while`** (sin usar `break`), deteniéndose si se completaron todas las etapas o si una etapa falló. Debe retornar una tupla `(ejecutadas_ok, etapa_fallida)` donde `ejecutadas_ok` es la lista de nombres de etapas exitosas y `etapa_fallida` es el nombre de la etapa que falló (o `None` si todas tuvieron éxito).
2. Probar la función en el programa principal e informar si el despliegue fue `"EXITOSO"` o `"ABORTADO EN: <etapa>"`.

#### Datos de partida:
```python
pipeline = [
    ("verificar_sintaxis", 0),
    ("correr_tests_unitarios", 0),
    ("migrar_base_de_datos", 127),
    ("reiniciar_nginx", 0),
]
```

#### Resolución Modelo (Ejercicio 3):
```python
"""Simulacro Parcial - Ejercicio 3: Cola de despliegue con while."""


def ejecutar_pipeline(etapas):
    """Ejecuta las etapas secuencialmente hasta terminar o encontrar un error != 0."""
    # etapas : list[tuple[str, int]]
    ejecutadas_ok = []
    etapa_fallida = None
    indice = 0
    error_detectado = False

    while indice < len(etapas) and not error_detectado:
        nombre, codigo = etapas[indice]
        if codigo == 0:
            ejecutadas_ok.append(nombre)
        else:
            etapa_fallida = nombre
            error_detectado = True
        indice += 1

    return ejecutadas_ok, etapa_fallida


# Programa principal
pipeline = [
    ("verificar_sintaxis", 0),
    ("correr_tests_unitarios", 0),
    ("migrar_base_de_datos", 127),
    ("reiniciar_nginx", 0),
]

completadas, fallo = ejecutar_pipeline(pipeline)
print("Etapas completadas:", completadas)
if fallo is None:
    print("Estado final: DESPLIEGUE EXITOSO")
else:
    print(f"Estado final: ABORTADO EN '{fallo}'")
```

#### Salida esperada:
```text
Etapas completadas: ['verificar_sintaxis', 'correr_tests_unitarios']
Estado final: ABORTADO EN 'migrar_base_de_datos'
```

---

## Parte 3: Modelos de Simulacro de Coloquio (Listos para Sortear)

Cada modelo combina los 3 ejes recomendados para evaluar la promoción en 20-30 minutos:
* **Parte A (Desarrollo con Funciones - 40%):** Adaptado del Bloque A del Banco de Ejercicios + Unidad 4.
* **Parte B (Comprensión / Traza de Código - 30%):** Explicar qué hace un bloque de mediana complejidad.
* **Parte C (Depuración de Código - 30%):** Encontrar el error, explicar su causa y corregirlo.

| Modelo | Parte A (Desarrollo con Funciones) | Parte B (¿Qué hace este código?) | Parte C (Código que no funciona) |
| :--- | :--- | :--- | :--- |
| **Modelo 1** | **Paquetes faltantes e innecesarios** (Ejercicio 1 del archivo `02_ejercicios_adaptados_funciones_U4.md`) | **Bloque 1:** Clasificador de logs por severidad y servicio (`03_bloques_que_hace_el_codigo.md`) | **Bloque 1:** Función que valida puertos pero olvida retornar / muta tupla (`04_bloques_codigo_con_errores.md`) |
| **Modelo 2** | **Bloqueo de IPs tipo `fail2ban`** (Ejercicio 10 del archivo `02_ejercicios_adaptados_funciones_U4.md`) | **Bloque 3:** Sincronizador de configuraciones con valores por defecto (`03_bloques_que_hace_el_codigo.md`) | **Bloque 4:** Limpieza de backups antiguos modificando la lista mientras se itera (`04_bloques_codigo_con_errores.md`) |
| **Modelo 3** | **Auditoría de uso de disco por partición** (Ejercicio 6 del archivo `02_ejercicios_adaptados_funciones_U4.md`) | **Bloque 5:** Verificador de dependencias con ciclo `while` (`03_bloques_que_hace_el_codigo.md`) | **Bloque 6:** Acumulador reiniciado dentro del bucle y `KeyError` en diccionario (`04_bloques_codigo_con_errores.md`) |
