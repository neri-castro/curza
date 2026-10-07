"""Ejercicio 6.2: triángulo rectángulo de N filas"""

n = int(input("Ingrese la cantidad de filas: "))
for fila in range(1, n + 1):
    for _ in range(fila):
        print("*", end="")
    print()
