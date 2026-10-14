"""Problema 2: Validación de clave de acceso al laboratorio

1. COMPRENDER
   - Ruido: 30 estaciones de trabajo, red local, proyector HD de 3800 lúmenes.
   - Entradas: clave (str), repetidamente.
   - Constantes: CLAVE_CORRECTA = 'python2026'
   - Salidas: mensaje de error por cada intento fallido y mensaje de acceso concedido.

2. PLAN
   - Var. control: clave
   - Condición while: clave != CLAVE_CORRECTA
   - Actualización: pedir la clave de nuevo dentro del bloque

4. TRAZA (entradas hola, Python2026, python2026)
   clave       | clave != CORRECTA | salida
   hola        | True              | Clave incorrecta...
   Python2026  | True              | Clave incorrecta...
   python2026  | False             | sale -> ¡Acceso concedido!
   Frontera: clave correcta al primer intento -> el bucle no se ejecuta.
"""

CLAVE_CORRECTA = 'python2026'

clave = input("Ingrese la clave: ")
while clave != CLAVE_CORRECTA:
    print("Clave incorrecta. Intente nuevamente.")
    clave = input("Ingrese la clave: ")

print("¡Acceso concedido al Laboratorio de Software Libre!")
