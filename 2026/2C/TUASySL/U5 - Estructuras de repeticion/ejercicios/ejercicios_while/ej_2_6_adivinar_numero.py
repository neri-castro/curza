"""Ejercicio 2.6: juego de adivinar un número entre 1 y 50"""

import random

secreto = random.randint(1, 50)
intento = int(input("Adivine el número (1-50): "))
while intento != secreto:
    if intento < secreto:
        print("Más alto")
    else:
        print("Más bajo")
    intento = int(input("Pruebe de nuevo: "))

print("¡Acertó!")
