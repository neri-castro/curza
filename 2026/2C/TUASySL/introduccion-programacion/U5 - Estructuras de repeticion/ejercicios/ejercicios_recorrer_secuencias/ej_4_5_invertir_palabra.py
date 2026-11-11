"""Ejercicio 4.5: invertir una palabra con un bucle"""

palabra = input("Ingrese una palabra: ")
invertida = ""
for letra in palabra:
    invertida = letra + invertida

print(invertida)
