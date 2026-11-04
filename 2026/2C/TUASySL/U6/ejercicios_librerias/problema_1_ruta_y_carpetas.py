"""Problema 1 - Rutas y carpetas (módulo os)"""

import os

RUTA_HOME = "/home"
RUTA_INEXISTENTE = "/carpeta_que_no_existe"

# a) Directorio de trabajo actual y solo el nombre de la carpeta
ruta_actual = os.getcwd()
nombre_carpeta = os.path.basename(ruta_actual)
print("Ruta actual:", ruta_actual)
print("Nombre de la carpeta:", nombre_carpeta)

# b) Verificar si existen dos rutas y si son carpetas
for ruta in (RUTA_HOME, RUTA_INEXISTENTE):
    if os.path.exists(ruta):
        if os.path.isdir(ruta):
            print(ruta, "-> existe y es un directorio")
        else:
            print(ruta, "-> existe pero NO es un directorio")
    else:
        print(ruta, "-> no existe")
