"""Problema 6 - Integrador: resumen de archivos por tipo (os + platform)"""

import os
import platform


def clasificar(nombre):
    """Devuelve 'python', 'texto' u 'otro' según la extensión del nombre."""
    # extension: str
    extension = os.path.splitext(nombre)[1]
    if extension == ".py":
        return "python"
    elif extension == ".txt":
        return "texto"
    else:
        return "otro"


def resumir(lista_nombres):
    """Devuelve (cantidad_python, cantidad_texto, cantidad_otros)."""
    # python, texto, otros: int
    python = 0
    texto = 0
    otros = 0
    for nombre in lista_nombres:
        tipo = clasificar(nombre)
        if tipo == "python":
            python += 1
        elif tipo == "texto":
            texto += 1
        else:
            otros += 1
    return python, texto, otros


ruta = os.getcwd()
solo_archivos = []
for nombre in os.listdir(ruta):
    if os.path.isfile(os.path.join(ruta, nombre)):
        solo_archivos.append(nombre)

cant_py, cant_txt, cant_otros = resumir(solo_archivos)

print("Equipo:", platform.node(), "-", platform.system())
print("Carpeta:", ruta)
print("Archivos .py :", cant_py)
print("Archivos .txt:", cant_txt)
print("Otros        :", cant_otros)
print("Total        :", cant_py + cant_txt + cant_otros)
