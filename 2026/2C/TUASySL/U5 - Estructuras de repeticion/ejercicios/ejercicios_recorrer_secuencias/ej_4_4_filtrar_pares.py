"""Ejercicio 4.4: nueva lista solo con los pares"""

numeros = [3, 8, 15, 22, 7, 10, 41, 6]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
