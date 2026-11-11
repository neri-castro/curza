"""Ejercicio 9.5: números perfectos entre 1 y 10.000"""

for numero in range(1, 10001):
    suma_divisores = 0
    for divisor in range(1, numero // 2 + 1):
        if numero % divisor == 0:
            suma_divisores += divisor
    if suma_divisores == numero:
        print(numero)
