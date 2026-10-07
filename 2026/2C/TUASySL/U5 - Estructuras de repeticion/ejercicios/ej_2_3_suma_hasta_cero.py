"""Ejercicio 2.3: sumar números hasta que se ingrese 0"""

suma = 0
numero = float(input("Ingrese un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = float(input("Ingrese un número (0 para terminar): "))

print(f"La suma total es: {suma}")
