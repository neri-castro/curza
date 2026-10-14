"""Ejercicio 2.4: pedir contraseña y contar intentos"""

CLAVE = "python123"
intentos = 1
ingreso = input("Ingrese la contraseña: ")
while ingreso != CLAVE:
    intentos += 1
    ingreso = input("Incorrecta. Ingrese la contraseña: ")

print(f"Acertó en {intentos} intento(s)")
