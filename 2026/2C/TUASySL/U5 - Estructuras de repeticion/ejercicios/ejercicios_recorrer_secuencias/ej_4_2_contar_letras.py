"""Ejercicio 4.2: contar letras de una palabra sin len()"""

palabra = input("Ingrese una palabra: ")
cantidad = 0
for _ in palabra:
    cantidad += 1

print(f"La palabra tiene {cantidad} letras")
