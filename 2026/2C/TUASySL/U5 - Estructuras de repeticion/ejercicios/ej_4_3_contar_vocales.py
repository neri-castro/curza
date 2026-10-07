"""Ejercicio 4.3: contar vocales de una frase"""

VOCALES = "aeiouáéíóúü"
frase = input("Ingrese una frase: ")
cantidad_vocales = 0
for caracter in frase.lower():
    if caracter in VOCALES:
        cantidad_vocales += 1

print(f"La frase tiene {cantidad_vocales} vocales")
