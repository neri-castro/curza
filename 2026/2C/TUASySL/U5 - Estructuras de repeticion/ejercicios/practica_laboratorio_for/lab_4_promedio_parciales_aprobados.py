"""Lab for - Problema 4: promedio de 8 parciales aprobados"""

NOTA_APROBACION = 6.0
suma_notas_aprobadas = 0.0
cant_aprobados = 0

for parcial in range(1, 9):
    nota_ingresada = float(input(f"Ingrese la nota del parcial {parcial}: "))
    if nota_ingresada >= NOTA_APROBACION:
        suma_notas_aprobadas += nota_ingresada
        cant_aprobados += 1

if cant_aprobados > 0:
    print(f"Promedio de parciales aprobados: {suma_notas_aprobadas / cant_aprobados:.2f}")
else:
    print("No se registraron parciales aprobados")
