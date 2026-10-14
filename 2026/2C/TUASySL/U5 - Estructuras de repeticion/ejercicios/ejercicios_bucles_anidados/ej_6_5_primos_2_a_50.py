"""Ejercicio 6.5: primos entre 2 y 50 con for...else"""

for candidato in range(2, 51):
    for divisor in range(2, candidato):
        if candidato % divisor == 0:
            break
    else:
        print(candidato)
