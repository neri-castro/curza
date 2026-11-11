"""Ejercicio 6.4: pirámide centrada de N filas"""

n = int(input("Ingrese la cantidad de filas: "))
for fila in range(1, n + 1):
    for _ in range(n - fila):
        print(" ", end="")
    for _ in range(2 * fila - 1):
        print("*", end="")
    print()
