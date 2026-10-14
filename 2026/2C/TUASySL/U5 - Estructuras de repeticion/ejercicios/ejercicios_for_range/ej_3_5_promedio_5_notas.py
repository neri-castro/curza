"""Ejercicio 3.5: promedio de 5 notas"""

suma_notas = 0.0
for i in range(1, 6):
    suma_notas += float(input(f"Nota {i}: "))

print(f"Promedio: {suma_notas / 5:.2f}")
