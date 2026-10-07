"""Lab for - Problema 3: condición de asistencia semanal"""

MINIMO_PROMOCION = 4
MINIMO_REGULAR = 3

registro_semana = input("Ingrese el registro semanal de 5 días (P/A): ")
cant_presentes = 0

for estado in registro_semana:
    if estado == "P":
        cant_presentes += 1

if cant_presentes >= MINIMO_PROMOCION:
    print("Condición: Promocionado en Asistencia")
elif cant_presentes >= MINIMO_REGULAR:
    print("Condición: Regular en Asistencia")
else:
    print("Condición: Libre por Inasistencias")
