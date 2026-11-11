"""Problema 5 - Mayor valor y su posición (sin usar max())"""

velocidades = [54.2, 98.7, 70.1, 98.9, 33.0]
mayor = velocidades[0]
posicion_mayor = 0

for i in range(len(velocidades)):
    if velocidades[i] > mayor:
        mayor = velocidades[i]
        posicion_mayor = i

print(f"Mayor velocidad: {mayor} Mbps en la posición {posicion_mayor}")
