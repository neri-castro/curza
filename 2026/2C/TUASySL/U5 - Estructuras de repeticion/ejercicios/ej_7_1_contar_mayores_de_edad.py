"""Ejercicio 7.1: contar mayores de edad (patrón contador)"""

edades = [12, 25, 17, 40, 18, 9, 33]
cant_mayores = 0
for edad in edades:
    if edad >= 18:
        cant_mayores += 1

print(f"Mayores de edad: {cant_mayores}")
