"""Ejercicio 7.2: mayor de N números sin max()"""

n = int(input("¿Cuántos números? "))
mayor = float(input("Número 1: "))
for i in range(2, n + 1):
    numero = float(input(f"Número {i}: "))
    if numero > mayor:
        mayor = numero

print(f"El mayor es: {mayor}")
