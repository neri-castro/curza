# Práctica extra: Diccionarios y conjuntos

**TUASySL - Introducción a la Programación | CURZAS - UNCo**

Reglas: `snake_case`, constantes en `SCREAMING_SNAKE_CASE`, método de Polya.

## Problema 1: Diccionario básico
Crear `equipo = {"nombre": "PC-Lab01", "ram_gb": 8, "so": "Debian"}`. a) Mostrar `len` y el valor de `"so"`. b) Pedir `"disco"` con `.get()` (¿qué devuelve?). c) Cambiar `ram_gb` a 16, insertar `disco_gb` y agregar con `.update()` `sede` y `estado`. d) Verificar con `in` que existe `"sede"`. e) Borrar `"estado"` con `del`. f) Recorrer con `.items()` e imprimir `clave: valor`.

## Problema 2: Contar frecuencias
`sistemas = ["Linux","Windows","Linux","Linux","Windows","macOS"]`. Con un `for` y un diccionario vacío, contar cuántas veces aparece cada sistema. *Esperado: Linux 3, Windows 2, macOS 1.*

## Problema 3: Nómina por legajo
`nomina` es un diccionario cuyas claves son legajos y cuyos valores son diccionarios `{"nombre", "nota"}` (Brisa 8.5, Abel 7.0, Celeste 9.5). Constante `NOTA_PROMOCION = 8.0`. a) Mostrar la nota de Abel por acceso directo. b) Recorrer con `.items()`, acumular la suma y avisar quiénes promocionan. c) Mostrar promedio y cantidad de promocionados. *Esperado: 7.0, promedio 8.33, 2 promocionados.*

## Problema 4: Conjuntos
`asistencias = ["Brisa","Abel","Celeste","Brisa","Diego","Abel"]` e `inscriptos = {"Abel","Diego","Erika","Fabi"}`. Obtener `presentes = set(asistencias)` y mostrar (con `sorted`): cantidad de presentes, intersección `&`, unión `|`, diferencia `inscriptos - presentes` y diferencia simétrica `^`.

## Problema 5: ¿Set o dict?
a) `sin_repetidos(lista)` devuelve los elementos únicos ordenados. b) `buscar_precio(catalogo, producto)` devuelve el precio o `-1` si no existe (usar `.get(clave, -1)`). Probar con una lista de IPs repetidas y un catálogo de 3 productos. Justificar por escrito por qué cada caso usa `set` o `dict`.

Soluciones en `problema_N_*.py`.
