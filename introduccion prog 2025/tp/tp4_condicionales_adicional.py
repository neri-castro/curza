# TP 4 - Trabajo Práctico Adicional: Estructuras Alternativas - Condicionales - Decisión

import math

print("=== TRABAJO PRÁCTICO 4: Estructuras Alternativas Adicional ===\n")

# EJERCICIO 1: Fórmula de Bhaskara
def bhaskara():
    """
    Objetivo: Calcular las raíces de una ecuación cuadrática usando la fórmula de Bhaskara
    Datos de entrada: coeficientes a, b, c de la ecuación ax² + bx + c = 0
    """
    print("EJERCICIO 1: Fórmula de Bhaskara")
    print("Ecuación: ax² + bx + c = 0")
    
    # Datos de entrada
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    
    # Verificar que 'a' no sea cero
    if a == 0:
        print("Error: El coeficiente 'a' no puede ser cero en una ecuación cuadrática")
        return
    
    # Calcular discriminante
    discriminante = b**2 - 4*a*c
    
    print(f"\nDiscriminante = b² - 4ac = {b}² - 4({a})({c}) = {discriminante}")
    
    # Verificar si tiene solución real
    if discriminante < 0:
        print("La ecuación no tiene solución real (discriminante < 0)")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La ecuación tiene una raíz doble: x = {x}")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las raíces son:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

# EJERCICIO 2: Productividad mensual
def productividad_mensual():
    """
    Objetivo: Calcular la productividad de un mes dado según factores establecidos
    Datos de entrada: mes (1-12), número de artículos producidos
    """
    print("\nEJERCICIO 2: Cálculo de productividad mensual")
    
    mes = int(input("Ingrese el número del mes (1-12): "))
    articulos = int(input("Ingrese el número de artículos producidos: "))
    
    # Asignar factor según el mes
    if mes in [1, 2, 3]:  # Enero, febrero, marzo
        factor = 15
        nombre_mes = ["Enero", "Febrero", "Marzo"][mes-1]
    elif mes in [4, 5, 6]:  # Abril, mayo, junio
        factor = 17
        nombre_mes = ["Abril", "Mayo", "Junio"][mes-4]
    elif mes in [7, 8]:  # Julio, agosto
        factor = 19
        nombre_mes = ["Julio", "Agosto"][mes-7]
    elif mes in [9, 10, 11, 12]:  # Septiembre, octubre, noviembre, diciembre
        factor = 20
        nombre_mes = ["Septiembre", "Octubre", "Noviembre", "Diciembre"][mes-9]
    else:
        print("Mes inválido. Debe estar entre 1 y 12.")
        return
    
    productividad = articulos * factor
    print(f"Mes: {nombre_mes}")
    print(f"Factor: {factor}")
    print(f"Artículos producidos: {articulos}")
    print(f"Productividad: {productividad}")

# EJERCICIO 3: Corrección de errores sintácticos
def programas_corregidos():
    """
    Objetivo: Mostrar programas corregidos y explicar sus salidas
    """
    print("\nEJERCICIO 3: Programas corregidos")
    
    print("--- Programa a) Corregido ---")
    print("Errores encontrados:")
    print("1. Falta ':' después de 'if x > 0'")
    print("2. 'imprimir' debe ser 'print'") 
    print("3. 'if else:' debe ser 'else:'")
    
    # Programa corregido
    x = int(input("Ingrese un numero: "))
    if x > 0:
        print("Numero positivo")
    elif x == 0:
        print("Igual a 0")
    else:
        print("Numero negativo")
    
    print("\n--- Programa b) Corregido ---")
    print("Errores encontrados:")
    print("1. Variable 'b' no está definida, debería ser 'z'")
    print("2. 'a < z:' debe tener 'if' al inicio")
    print("3. Falta 'print' en la última línea")
    
    # Programa corregido
    x = input("Ingrese primer valor: ")
    z = input("Ingrese segundo valor: ")
    if x == z:
        print('Los números', x, 'y', z, 'son iguales')
    elif x < z:
        print('El número', x, 'es menor que', z)
    else:
        print('El número', x, 'es mayor que', z)

# EJERCICIO 4: Días del mes
def dias_del_mes():
    """
    Objetivo: Determinar cuántos días tiene un mes dado en un año específico
    Datos de entrada: número de mes (1-12), año
    """
    print("\nEJERCICIO 4: Días del mes")
    
    mes = int(input("Ingrese el número del mes (1-12): "))
    año = int(input("Ingrese el año: "))
    
    # Verificar si es año bisiesto
    def es_bisiesto(año):
        return (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0)
    
    # Días por mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
    elif mes in [4, 6, 9, 11]:
        dias = 30
    elif mes == 2:
        if es_bisiesto(año):
            dias = 29
        else:
            dias = 28
    else:
        print("Mes inválido")
        return
    
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    print(f"El mes {mes} ({nombres_meses[mes-1]}) del año {año} tiene {dias} días")

# EJERCICIO 5: Tiempo de trayecto
def tiempo_trayecto():
    """
    Objetivo: Calcular el tiempo total de un trayecto considerando paradas
    Datos de entrada: kilómetros, paradas para comer
    """
    print("\nEJERCICIO 5: Cálculo de tiempo de trayecto")
    
    kilometros = float(input("Ingrese los kilómetros a recorrer: "))
    paradas_comer = int(input("Ingrese el número de paradas para comer: "))
    
    # Cálculos
    velocidad_promedio = 100  # km/h
    tiempo_viaje = kilometros / velocidad_promedio  # horas
    
    # Paradas de combustible: 1 inicial + 1 cada 500 km adicionales
    paradas_combustible = 1 + int(kilometros // 500)
    tiempo_combustible = paradas_combustible * 15 / 60  # convertir minutos a horas
    
    # Paradas para comer
    tiempo_comer = paradas_comer * 30 / 60  # convertir minutos a horas
    
    # Tiempo total
    tiempo_total = tiempo_viaje + tiempo_combustible + tiempo_comer
    
    horas = int(tiempo_total)
    minutos = int((tiempo_total - horas) * 60)
    
    print(f"El viaje en total será de {horas} horas y {minutos} minutos, "
          f"haciendo {paradas_combustible} paradas a cargar combustible y {paradas_comer} paradas a comer.")

# EJERCICIO 6: Validar URL
def validar_url():
    """
    Objetivo: Validar si un texto es una URL básica bien formada
    Datos de entrada: texto de URL
    """
    print("\nEJERCICIO 6: Validador de URL básica")
    
    url = input("Ingrese la URL a validar: ").strip()
    
    inicio_correcto = url.startswith("www.")
    fin_correcto = url.endswith(".com") or url.endswith(".com.ar")
    
    if inicio_correcto and fin_correcto:
        print("✓ URL válida y bien formada")
    else:
        if not inicio_correcto and not fin_correcto:
            print("✗ URL mal formada: error al principio (debe empezar con 'www.') y al final (debe terminar con '.com' o '.com.ar')")
        elif not inicio_correcto:
            print("✗ URL mal formada: error al principio (debe empezar con 'www.')")
        else:
            print("✗ URL mal formada: error al final (debe terminar con '.com' o '.com.ar')")

# EJERCICIO 7: Mezcla de colores
def mezcla_colores():
    """
    Objetivo: Determinar el color resultante de mezclar dos colores primarios
    Datos de entrada: dos códigos de color (az, ro, am)
    """
    print("\nEJERCICIO 7: Mezclador de colores primarios")
    print("Códigos: az=Azul, ro=Rojo, am=Amarillo")
    
    color1 = input("Ingrese el primer color (az/ro/am): ").strip().lower()
    color2 = input("Ingrese el segundo color (az/ro/am): ").strip().lower()
    
    # Diccionario de nombres completos
    nombres = {"az": "Azul", "ro": "Rojo", "am": "Amarillo"}
    
    # Validar códigos
    if color1 not in nombres or color2 not in nombres:
        print("Códigos de color inválidos. Use: az, ro, am")
        return
    
    # Ordenar colores para facilitar las comparaciones
    colores = tuple(sorted([color1, color2]))
    
    # Determinar resultado de la mezcla
    if color1 == color2:
        resultado = nombres[color1]
    elif colores == ("am", "az"):  # Amarillo + Azul = Verde
        resultado = "Verde"
    elif colores == ("az", "ro"):  # Azul + Rojo = Violeta
        resultado = "Violeta"  
    elif colores == ("am", "ro"):  # Amarillo + Rojo = Naranja
        resultado = "Naranja"
    
    print(f"{nombres[color1]} + {nombres[color2]} = {resultado}")

# FUNCIÓN PRINCIPAL
def ejecutar_tp4():
    """Ejecutar los ejercicios del TP4"""
    print("Seleccione qué ejercicio ejecutar:")
    print("1. Fórmula de Bhaskara")
    print("2. Productividad mensual")
    print("3. Programas corregidos")
    print("4. Días del mes")
    print("5. Tiempo de trayecto")
    print("6. Validar URL")
    print("7. Mezcla de colores")
    print("0. Ejecutar demo de todos")
    
    opcion = input("Ingrese su opción: ").strip()
    
    if opcion == "1":
        bhaskara()
    elif opcion == "2":
        productividad_mensual()
    elif opcion == "3":
        programas_corregidos()
    elif opcion == "4":
        dias_del_mes()
    elif opcion == "5":
        tiempo_trayecto()
    elif opcion == "6":
        validar_url()
    elif opcion == "7":
        mezcla_colores()
    elif opcion == "0":
        print("=== DEMOSTRACIÓN DE TODOS LOS EJERCICIOS ===")
        
        # Demo Bhaskara con valores de ejemplo
        print("\n--- Demo Bhaskara (con a=1, b=-5, c=6) ---")
        # x² - 5x + 6 = 0, raíces: x=2, x=3
        a, b, c = 1, -5, 6
        discriminante = b**2 - 4*a*c
        if discriminante >= 0:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            print(f"Para x² - 5x + 6 = 0: x1={x1}, x2={x2}")
        
        # Demo productividad
        print("\n--- Demo Productividad (Mes 5, 100 artículos) ---")
        mes, articulos, factor = 5, 100, 17
        productividad = articulos * factor
        print(f"Mayo: {articulos} artículos × factor {factor} = {productividad}")
        
        # Demo días del mes
        print("\n--- Demo Días del mes (Febrero 2024) ---")
        print("Febrero 2024 (año bisiesto): 29 días")
        
        # Demo URL
        print("\n--- Demo URL ---")
        urls_test = ["www.google.com", "google.com", "www.google", "ftp://ejemplo.com"]
        for url in urls_test:
            valido = url.startswith("www.") and (url.endswith(".com") or url.endswith(".com.ar"))
            print(f"{url}: {'✓ válida' if valido else '✗ inválida'}")
        
        # Demo colores
        print("\n--- Demo Mezcla de colores ---")
        mezclas = [("az", "ro", "Violeta"), ("am", "az", "Verde"), ("ro", "am", "Naranja")]
        nombres = {"az": "Azul", "ro": "Rojo", "am": "Amarillo"}
        for c1, c2, resultado in mezclas:
            print(f"{nombres[c1]} + {nombres[c2]} = {resultado}")
        
        print("\nPara ejercicios interactivos, ejecute individualmente.")
    else:
        print("Opción no válida")

# Ejecutar
if __name__ == "__main__":
    ejecutar_tp4()
    