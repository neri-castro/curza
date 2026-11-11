"""Ejercicio 6.3: tabla pitagórica del 1 al 5"""

for fila in range(1, 6):
    for columna in range(1, 6):
        print(f"{fila * columna:4}", end="")
    print()
