"""Ejercicio 5.4: login con 3 intentos máximo"""

CLAVE = "python123"
MAX_INTENTOS = 3

for _ in range(MAX_INTENTOS):
    if input("Contraseña: ") == CLAVE:
        print("Bienvenido")
        break
else:
    print("Cuenta bloqueada")
