"""Ejercicio 5.5: determinar si N es primo"""

n = int(input("Ingrese un número: "))

if n < 2:
    print(f"{n} no es primo")
else:
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            print(f"{n} no es primo (divisible por {divisor})")
            break
    else:
        print(f"{n} es primo")
