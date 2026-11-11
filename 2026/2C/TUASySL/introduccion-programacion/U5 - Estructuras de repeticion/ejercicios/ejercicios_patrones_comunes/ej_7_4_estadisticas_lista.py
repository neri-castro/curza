"""Ejercicio 7.4: positivos, negativos, suma y promedio en una pasada"""

numeros = [4, -2, 7, 0, -9, 15, 3]
cant_positivos = 0
cant_negativos = 0
suma_total = 0

for numero in numeros:
    if numero > 0:
        cant_positivos += 1
    elif numero < 0:
        cant_negativos += 1
    suma_total += numero

print(f"Positivos: {cant_positivos}")
print(f"Negativos: {cant_negativos}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {suma_total / len(numeros):.2f}")
