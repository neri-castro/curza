"""Ejercicio 3.7: primeros N términos de Fibonacci"""

n = int(input("¿Cuántos términos? "))
anterior, actual = 0, 1
for _ in range(n):
    print(anterior)
    anterior, actual = actual, anterior + actual
