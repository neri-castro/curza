"""Problema 2 - Contar frecuencias con un diccionario"""

sistemas = ["Linux", "Windows", "Linux", "Linux", "Windows", "macOS"]
cantidades = {}

for so in sistemas:
    if so in cantidades:
        cantidades[so] += 1
    else:
        cantidades[so] = 1

for clave, valor in cantidades.items():
    print(f"{clave}: {valor}")
