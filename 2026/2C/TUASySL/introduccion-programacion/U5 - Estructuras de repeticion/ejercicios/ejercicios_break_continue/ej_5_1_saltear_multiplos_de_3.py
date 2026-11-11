"""Ejercicio 5.1: números del 1 al 20 salteando múltiplos de 3"""

for numero in range(1, 21):
    if numero % 3 == 0:
        continue
    print(numero)
