"""Lab for - Problema 2: contar símbolos '#' en una clave"""

MINIMO_CARACTERES_ESPECIALES = 2

clave_usuario = input("Ingrese su clave institucional: ")
cantidad_simbolos = 0

for caracter in clave_usuario:
    if caracter == "#":
        cantidad_simbolos += 1

if cantidad_simbolos >= MINIMO_CARACTERES_ESPECIALES:
    print("Clave Segura Aprobada")
else:
    print("Clave Inválida: Se requieren al menos 2 símbolos #")
