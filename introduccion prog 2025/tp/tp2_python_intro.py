# TP 2 - Introducción a Python
# Ejercicios para ejecutar en terminal Python

print("=== TRABAJO PRÁCTICO 2: Introducción a Python ===\n")

# EJERCICIO 1: Operaciones matemáticas
print("EJERCICIO 1: Operaciones matemáticas")
print("Resultados de las expresiones:")

# a) números enteros
print("\na) Números enteros:")
print(f"2 + 3 + 1 + 2 = {2 + 3 + 1 + 2}")
print(f"2 + 3 * 1 + 2 = {2 + 3 * 1 + 2}")  # Precedencia: multiplicación primero
print(f"(2 + 3) * 1 + 2 = {(2 + 3) * 1 + 2}")
print(f"(2 + 3) * (1 + 2) = {(2 + 3) * (1 + 2)}")
print(f"+---6 = {+---6}")  # Equivale a +(-(-(-6))) = +(-(6)) = +(-6) = -6
print(f"-+-+6 = {-+-+6}")  # Equivale a -(+(-(+6))) = -(+(-6)) = -(-6) = 6

# b) números reales o float
print("\nb) Números reales o float:")
print(f"1 / 2 / 4.0 = {1 / 2 / 4.0}")
print(f"1 / 2.0 / 4.0 = {1 / 2.0 / 4.0}")
print(f"1 / 2.0 / 4 = {1 / 2.0 / 4}")
print(f"4.0 ** (1 / 2) + 1 / 2 = {4.0 ** (1 / 2) + 1 / 2}")
print(f"4.0 ** (1.0 / 2) + 1 / 2.0 = {4.0 ** (1.0 / 2) + 1 / 2.0}")

# c) comparar resultados con //
print("\nc) Operador // (división entera):")
print(f"1 // 2 // 4.0 = {1 // 2 // 4.0}")
print(f"1 // 2.0 // 4.0 = {1 // 2.0 // 4.0}")
print("El operador // realiza división entera (floor division)")
print("Devuelve la parte entera del resultado de la división")

print("=" * 50)

# EJERCICIO 2: Tipo booleano
print("EJERCICIO 2: Tipo booleano")
print("Resultados de expresiones booleanas:")

print(f"2 == 3: {2 == 3}")
print(f"2 == 2: {2 == 2}")
print(f"2.1 == 2.1: {2.1 == 2.1}")
print(f"True == True: {True == True}")
print(f"True == False: {True == False}")
print(f"2 == 1+1: {2 == 1+1}")
print(f"True==True != False: {True==True != False}")  # Se evalúa como (True==True) != False
print(f"1<2<3<4<5: {1<2<3<4<5}")  # Comparaciones encadenadas
print(f"(1<2<3) and (4<5): {(1<2<3) and (4<5)}")
print(f"1<2<4<3<5: {1<2<4<3<5}")  # Falso porque 4 no es menor que 3
print(f"(1<2<4) and (3<5): {(1<2<4) and (3<5)}")

print("=" * 50)

# EJERCICIO 3: Programa desde pseudocódigo
print("EJERCICIO 3: Programa equivalente al pseudocódigo")
print("\nPseudocódigo convertido a Python:")
print("Enunciado: Programa que lee valores, calcula una suma y un promedio")

# Implementación del pseudocódigo
A = 5
print(f"A = {A}")

B = float(input("Ingrese el valor de B: "))
print(f"La suma es: {A + B}")

print("Ingrese el valor de A")
A = float(input())
print(f"La suma es: {A + B}")

print("Ingrese A")
A = float(input())

print("Ingrese B")
B = float(input())

print("Ingrese C")
C = float(input())

promedio = (A + B + C) / 3
print(f"El promedio es: {promedio}")

print("\nNota: Cada vez que el programa pide ingresar un dato, ingrese el valor 8.")
print("Al ingresar 8 en todas las solicitudes, el resultado será diferente")
print("dependiendo de cuándo se ingrese cada valor.")

print("=" * 50)
print("=== FIN DEL TP 2 ===")
