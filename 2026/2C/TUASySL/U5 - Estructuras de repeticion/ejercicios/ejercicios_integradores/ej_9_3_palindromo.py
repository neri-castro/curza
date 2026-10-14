"""Ejercicio 9.3: palíndromo comparando letras con un bucle"""

frase = input("Ingrese una frase: ")
letras = ""
for caracter in frase.lower():
    if caracter != " ":
        letras += caracter

es_palindromo = True
for i in range(len(letras) // 2):
    if letras[i] != letras[-1 - i]:
        es_palindromo = False
        break

if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")
