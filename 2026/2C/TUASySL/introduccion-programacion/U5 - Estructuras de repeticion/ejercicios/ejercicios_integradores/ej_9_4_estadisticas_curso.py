"""Ejercicio 9.4: estadísticas de un curso (for + for + while)"""

NOTAS_POR_ALUMNO = 3
PROMEDIO_PROMOCION = 8

cant_alumnos = int(input("Cantidad de alumnos: "))
suma_promedios = 0.0
cant_promocionados = 0

for alumno in range(1, cant_alumnos + 1):
    suma_notas = 0.0
    for i in range(1, NOTAS_POR_ALUMNO + 1):
        nota = float(input(f"Alumno {alumno}, nota {i}: "))
        while nota < 1 or nota > 10:
            nota = float(input("Nota inválida (1-10). Reingrese: "))
        suma_notas += nota
    promedio = suma_notas / NOTAS_POR_ALUMNO
    print(f"Promedio del alumno {alumno}: {promedio:.2f}")
    suma_promedios += promedio
    if promedio >= PROMEDIO_PROMOCION:
        cant_promocionados += 1

if cant_alumnos > 0:
    print(f"Promedio general: {suma_promedios / cant_alumnos:.2f}")
print(f"Alumnos que promocionaron: {cant_promocionados}")
