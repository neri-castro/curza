"""Ejercicio 7.3: validar nota entre 1 y 10 e informar si aprobó"""

nota = float(input("Ingrese una nota (1-10): "))
while nota < 1 or nota > 10:
    nota = float(input("Nota inválida. Ingrese una nota (1-10): "))

if nota >= 6:
    print("Aprobó")
else:
    print("Desaprobó")
