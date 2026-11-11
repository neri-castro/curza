"""Ejercicio 4.6: alumnos aprobados con su número de orden"""

NOTA_APROBACION = 6
alumnos = ["Ana", "Luis", "Marta", "Pedro"]
notas = [8, 4, 6, 3]

for orden, (alumno, nota) in enumerate(zip(alumnos, notas), start=1):
    if nota >= NOTA_APROBACION:
        print(f"{orden}. {alumno} aprobó con {nota}")
