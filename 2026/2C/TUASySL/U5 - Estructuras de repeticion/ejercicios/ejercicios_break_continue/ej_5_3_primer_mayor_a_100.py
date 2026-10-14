"""Ejercicio 5.3: primer número mayor a 100 (for...else)"""

numeros = [12, 45, 99, 130, 7, 250]

for numero in numeros:
    if numero > 100:
        print(f"El primero mayor a 100 es: {numero}")
        break
else:
    print("Ningún número es mayor a 100")
