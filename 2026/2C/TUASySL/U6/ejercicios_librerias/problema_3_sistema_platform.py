"""Problema 3 - Informe del sistema (módulo platform)"""

import platform

sistema = platform.system()
equipo = platform.node()
arquitectura = platform.machine()
version_python = platform.python_version()

# a) Datos básicos
print("Sistema operativo:", sistema)
print("Nombre del equipo:", equipo)
print("Arquitectura:", arquitectura)
print("Versión de Python:", version_python)

# b) Mensaje según el sistema
if sistema == "Linux":
    print("Es un sistema Linux: usar comandos de terminal bash.")
elif sistema == "Windows":
    print("Es un sistema Windows: usar PowerShell o cmd.")
else:
    print("Sistema no contemplado:", sistema)

# c) Recorrer platform.uname() con etiquetas
etiquetas = ["Sistema", "Nodo", "Release", "Versión", "Máquina"]
datos = platform.uname()
for i in range(5):
    print(f"{etiquetas[i]:<10} | {datos[i]}")
