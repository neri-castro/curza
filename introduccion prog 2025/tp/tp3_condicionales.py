# TP 3 - Estructuras de Control Condicionales

print("=== TRABAJO PRÁCTICO 3: Estructuras de Control Condicionales ===\n")

# EJERCICIO 1: Números ordenados en forma creciente
def numeros_ordenados_creciente():
    print("EJERCICIO 1: Determinar si dos números están ordenados en forma creciente")
    a = float(input("Ingrese el primer número (a): "))
    b = float(input("Ingrese el segundo número (b): "))
    
    if a <= b:
        print(f"Los números {a} y {b} están ordenados en forma creciente.")
    else:
        print(f"Los números {a} y {b} NO están ordenados en forma creciente.")

# EJERCICIO 2: Beca del comedor universitario
def beca_comedor():
    print("\nEJERCICIO 2: Elegibilidad para beca del comedor universitario")
    promedio = float(input("Ingrese su promedio de secundario: "))
    edad = int(input("Ingrese su edad: "))
    distancia = float(input("Ingrese la distancia de su localidad a Viedma (km): "))
    
    # Condición: (promedio > 7 AND edad < 25) OR distancia > 30
    if (promedio > 7 and edad < 25) or distancia > 30:
        print("¡Felicitaciones! PUEDE acceder a la beca del comedor.")
    else:
        print("Lo siento, NO puede acceder a la beca del comedor.")
        print("Debe cumplir: (promedio > 7 Y edad < 25) O vivir a más de 30 km de Viedma")

# EJERCICIO 3: Precio de helado
def precio_helado():
    print("\nEJERCICIO 3: Calculadora de precio de helado")
    print("Opciones:")
    print("1. 1/4 kilo - $6000")
    print("2. 1/2 kilo - $10000") 
    print("3. 1 kilo - $18000")
    
    opcion = input("Ingrese la cantidad deseada (1/4, 1/2, 1): ").strip()
    es_socio = input("¿Es socio? (s/n): ").strip().lower()
    
    if opcion == "1/4":
        precio = 6000
    elif opcion == "1/2":
        precio = 10000
    elif opcion == "1":
        precio = 18000
    else:
        print("Opción no válida")
        return
    
    if es_socio == 's':
        descuento = precio * 0.15
        precio_final = precio - descuento
        print(f"Precio original: ${precio}")
        print(f"Descuento socio (15%): ${descuento}")
        print(f"Precio final: ${precio_final}")
    else:
        print(f"Precio final: ${precio}")

# EJERCICIO 4: Análisis de programas
def analizar_programas():
    print("\nEJERCICIO 4: Análisis de programas")
    
    print("\n--- Programa 1: Juego de adivinanza ---")
    print("Descripción: Es un juego donde un jugador piensa un número y otro lo adivina")
    print("Salidas posibles:")
    print("- Si adivina exacto: 'Acertaste!!'")
    print("- Si está a ±1: 'Casi asiertas'")
    print("- Si no: 'Sige intentando'")
    
    print("\n--- Programa 2: Calculadora básica ---")
    print("Descripción: Es una calculadora que realiza operaciones básicas (+, -, *, /)")
    print("Solicita dos números y un operador, luego realiza la operación")
    print("Maneja el error de división por cero")

# EJERCICIO 5: Número par o impar
def par_o_impar():
    print("\nEJERCICIO 5: Determinar si un número es par o impar")
    numero = int(input("Ingrese un número entero: "))
    
    if numero % 2 == 0:
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")

# EJERCICIO 6: Intercambiar valores de variables
def intercambiar_variables():
    print("\nEJERCICIO 6: Intercambiar valores de variables")
    print("Ingrese dos valores para intercambiar:")
    variable1 = input("Ingrese el valor para variable1: ")
    variable2 = input("Ingrese el valor para variable2: ")
    
    print(f"Antes del intercambio:")
    print(f"variable1 = {variable1}")
    print(f"variable2 = {variable2}")
    
    # Intercambio usando una variable temporal
    temp = variable1
    variable1 = variable2
    variable2 = temp
    
    print(f"Después del intercambio:")
    print(f"variable1 = {variable1}")
    print(f"variable2 = {variable2}")

# EJERCICIO 7: Año bisiesto
def año_bisiesto():
    print("\nEJERCICIO 7: Determinar si un año es bisiesto")
    año = int(input("Ingrese un año: "))
    
    # Un año es bisiesto si:
    # - Es divisible por 4 AND (no es divisible por 100 OR es divisible por 400)
    if (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0):
        print(f"El año {año} ES bisiesto")
    else:
        print(f"El año {año} NO es bisiesto")

# EJERCICIO 8: Ordenar tres números en forma decreciente
def ordenar_decreciente():
    print("\nEJERCICIO 8: Ordenar tres números en forma decreciente")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    
    # Encontrar el mayor, medio y menor
    numeros = [a, b, c]
    numeros.sort(reverse=True)  # Ordenar de mayor a menor
    
    print(f"Números ordenados en forma decreciente: {numeros[0]}, {numeros[1]}, {numeros[2]}")

# EJERCICIO 9: Ordenar con opción creciente o decreciente
def ordenar_con_opcion():
    print("\nEJERCICIO 9: Ordenar tres números (creciente o decreciente)")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    
    orden = input("¿Desea ordenar en forma creciente o decreciente? (c/d): ").strip().lower()
    
    numeros = [a, b, c]
    
    if orden == 'c':
        numeros.sort()  # Orden creciente
        print(f"Números ordenados en forma creciente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
    elif orden == 'd':
        numeros.sort(reverse=True)  # Orden decreciente
        print(f"Números ordenados en forma decreciente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
    else:
        print("Opción no válida. Use 'c' para creciente o 'd' para decreciente.")

# EJERCICIO 10: Ejemplo con match (Python 3.10+)
def calculadora_con_match():
    print("\nEJERCICIO 10: Calculadora usando match (Python 3.10+)")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ").strip()
        
        if operacion == '+':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacion == '-':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif operacion == '*':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operacion == '/':
            if num2 != 0:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            else:
                print("Error: División por cero")
        else:
            print("Operación no válida")
                
        print("\nConclusión sobre if/elif vs match:")
        print("- if/elif es más flexible para condiciones complejas")
        print("- match es más limpio cuando hay muchas comparaciones de igualdad (disponible desde Python 3.10)")
        
    except ValueError:
        print("Error: Ingrese números válidos")

# Función principal para ejecutar todos los ejercicios
def ejecutar_tp3():
    print("Seleccione qué ejercicio ejecutar:")
    print("1. Números ordenados")
    print("2. Beca comedor")  
    print("3. Precio helado")
    print("4. Análisis programas")
    print("5. Par o impar")
    print("6. Intercambiar variables")
    print("7. Año bisiesto")
    print("8. Ordenar decreciente")
    print("9. Ordenar con opción")
    print("10. Match vs if")
    print("0. Ejecutar todos")
    
    opcion = input("Ingrese su opción: ").strip()
    
    if opcion == "1":
        numeros_ordenados_creciente()
    elif opcion == "2":
        beca_comedor()
    elif opcion == "3":
        precio_helado()
    elif opcion == "4":
        analizar_programas()
    elif opcion == "5":
        par_o_impar()
    elif opcion == "6":
        intercambiar_variables()
    elif opcion == "7":
        año_bisiesto()
    elif opcion == "8":
        ordenar_decreciente()
    elif opcion == "9":
        ordenar_con_opcion()
    elif opcion == "10":
        calculadora_con_match()
    elif opcion == "0":
        print("Ejecutando demostración de todos los ejercicios...")
        analizar_programas()
        print("\nPara ejercicios interactivos, ejecute individualmente.")
    else:
        print("Opción no válida")

# Ejecutar
if __name__ == "__main__":
    ejecutar_tp3()
