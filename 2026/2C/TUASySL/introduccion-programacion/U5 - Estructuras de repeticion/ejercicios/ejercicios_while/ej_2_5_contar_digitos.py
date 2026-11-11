"""Ejercicio 2.5: contar dígitos sin convertir a texto"""

numero = int(input("Ingrese un entero positivo: "))
cantidad_digitos = 0
restante = numero

if restante == 0:
    cantidad_digitos = 1
while restante > 0:
    restante //= 10
    cantidad_digitos += 1

print(f"{numero} tiene {cantidad_digitos} dígito(s)")
