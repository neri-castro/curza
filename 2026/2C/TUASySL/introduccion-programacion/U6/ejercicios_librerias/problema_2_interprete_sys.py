"""Problema 2 - Datos del intérprete (módulo sys)"""

import sys

# a) Versión mayor y menor con sys.version_info
mayor = sys.version_info[0]
menor = sys.version_info[1]
print(f"Versión de Python: {mayor}.{menor}")

# b) Plataforma según sys.platform
print("Plataforma:", sys.platform)

# c) Palabras de sys.version: cantidad y la primera
palabras = sys.version.split()
print("Cantidad de palabras en sys.version:", len(palabras))
print("Primera palabra:", palabras[0])

# d) Verificar versión mínima
if mayor >= 3:
    print("Versión compatible con el curso.")
else:
    print("Versión demasiado antigua.")
