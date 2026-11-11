"""Ejercicio 3.6: factorial de N"""

n = int(input("Ingrese un número: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
