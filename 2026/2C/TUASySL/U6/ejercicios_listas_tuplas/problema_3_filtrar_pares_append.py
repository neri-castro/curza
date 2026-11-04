"""Problema 3 - Filtrar con .append(): inscriptos mayores de edad"""

EDAD_MINIMA = 18

edades = [17, 22, 19, 16, 30, 18, 15]
edades_mayores = []

for edad in edades:
    if edad >= EDAD_MINIMA:
        edades_mayores.append(edad)

promedio = sum(edades_mayores) / len(edades_mayores)
print("Mayores de edad:", edades_mayores)
print("Promedio de edad:", round(promedio, 2))
