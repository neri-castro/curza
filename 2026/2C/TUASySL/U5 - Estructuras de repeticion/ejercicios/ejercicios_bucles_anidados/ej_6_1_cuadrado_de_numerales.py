"""Ejercicio 6.1: cuadrado de N x N con '#'"""

n = int(input("Ingrese el lado del cuadrado: "))
for _ in range(n):
    for _ in range(n):
        print("#", end="")
    print()
