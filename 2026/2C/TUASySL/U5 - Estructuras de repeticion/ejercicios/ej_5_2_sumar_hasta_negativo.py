"""Ejercicio 5.2: sumar hasta que se ingrese un negativo"""

suma = 0
while True:
    numero = float(input("Ingrese un número (negativo para terminar): "))
    if numero < 0:
        break
    suma += numero

print(f"La suma es: {suma}")
