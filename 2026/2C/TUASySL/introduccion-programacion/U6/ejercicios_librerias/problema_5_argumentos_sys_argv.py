"""Problema 5 - Argumentos por línea de comandos (sys.argv)

Ejecutar:  python3 problema_5_argumentos_sys_argv.py 4 10 7
"""

import sys

argumentos = sys.argv[1:]  # sys.argv[0] es el nombre del script

if len(argumentos) == 0:
    print("Uso: python3 problema_5_argumentos_sys_argv.py n1 n2 ...")
else:
    suma = 0
    for texto in argumentos:
        suma += int(texto)
    promedio = suma / len(argumentos)
    print("Script:", sys.argv[0])
    print("Cantidad de números:", len(argumentos))
    print("Suma:", suma)
    print("Promedio:", promedio)
