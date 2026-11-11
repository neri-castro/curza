"""Problema 1: Carga indeterminada de notas con centinela

1. COMPRENDER
   - Ruido: Sede Atlántica, servidor Linux de 16 núcleos, fibra de 1 Gbps, PEDCO.
   - Entradas: notas (float), una a una.
   - Constantes: CENTINELA_SALIDA = -1.0, NOTA_MINIMA_APROBACION = 6.0
   - Salidas: cantidad de aprobados y promedio de las notas aprobadas.

2. PLAN
   - Var. control: nota (leída antes del bucle y al final de cada vuelta)
   - Condición while: nota != CENTINELA_SALIDA
   - Actualización: leer la siguiente nota al final del bloque

4. TRAZA (entradas 7.0, 4.0, 9.0, -1.0)
   nota | >= 6.0 | cant_aprobados | suma_aprobados
   7.0  | sí     | 1              | 7.0
   4.0  | no     | 1              | 7.0
   9.0  | sí     | 2              | 16.0
   -1.0 | fin    | 2              | 16.0  -> promedio 8.00
   Frontera: solo -1.0 -> 0 aprobados, se evita la división por cero.
"""

CENTINELA_SALIDA = -1.0
NOTA_MINIMA_APROBACION = 6.0

cant_aprobados = 0
suma_aprobados = 0.0

nota = float(input("Ingrese una nota (-1 para terminar): "))
while nota != CENTINELA_SALIDA:
    if nota >= NOTA_MINIMA_APROBACION:
        cant_aprobados += 1
        suma_aprobados += nota
    nota = float(input("Ingrese una nota (-1 para terminar): "))

if cant_aprobados > 0:
    print(f"Aprobados: {cant_aprobados}")
    print(f"Promedio de aprobados: {suma_aprobados / cant_aprobados:.2f}")
else:
    print("No hubo notas aprobadas")
