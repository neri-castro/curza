"""Problema 4 - Contar archivos .txt de una carpeta (os + función + for)"""

import os

EXTENSION = ".txt"


def contar_por_extension(lista_archivos, extension):
    """Devuelve cuántos nombres de la lista terminan con la extensión dada."""
    # contador: int
    contador = 0
    for nombre in lista_archivos:
        if nombre.endswith(extension):
            contador += 1
    return contador


ruta = os.getcwd()
elementos = os.listdir(ruta)
total = contar_por_extension(elementos, EXTENSION)

print("Carpeta analizada:", ruta)
print("Elementos totales:", len(elementos))
print(f"Archivos {EXTENSION} encontrados:", total)

# Prueba con una lista fija
prueba = ["a.txt", "b.py", "c.txt", "notas.TXT", "txt"]
print("Prueba (esperado 2):", contar_por_extension(prueba, EXTENSION))
