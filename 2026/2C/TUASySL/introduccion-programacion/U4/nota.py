# 
# NOTA DE LA CÁTEDRA:
# COMENTARIOS Y ACLARACIONES REALIZADAS CON IA GEMINI NOTEBOOK
# 
# 
# ==============================================================================
# 1. DEFINICIÓN DE FUNCIONES (Módulos reutilizables)
# Recordar: En Python las funciones se definen al inicio del archivo 
# ==============================================================================

# ------------------------------------------------------------------------------
# FUNCIÓN 1: Validación de Rango (Función Booleana)
# ------------------------------------------------------------------------------
# Propósito: Evalúa si un número está dentro del rango válido de 1 a 10
# Parámetro formal:
#   - n: VARIABLE LOCAL (existe únicamente dentro de esta función)
# Retorno:
#   - Devuelve True si la nota está entre 1 y 10, o False si no lo está 

def es_nota_valida(n):
    return  1<=n<=10

# ------------------------------------------------------------------------------
# FUNCIÓN 2: Cálculo Numérico
# ------------------------------------------------------------------------------
# Propósito: Calcula el promedio de tres notas usando división entera (//) 
# Parámetros formales:
#   - n1, n2, n3: VARIABLES LOCALES (reciben los valores enviados)
# Variable interna:
#   - prom: VARIABLE LOCAL (guarda el resultado del cálculo en la memoria local) 
# Retorno:
#   - Devuelve el valor guardado en 'prom' al programa principal

def promedio_notas(n1,n2,n3):
    prom=(n1+n2+n3)//3
    return prom

# ------------------------------------------------------------------------------
# FUNCIÓN 3: Evaluación de Estado (Función sin retorno)
# ------------------------------------------------------------------------------
# Propósito: Evalúa el promedio mediante condicionales e imprime el resultado 
# Parámetro formal:
#   - promedio: VARIABLE LOCAL (recibe el promedio calculado) 
# Interpretación del promedio:
    # nota < 4 desaprobado
    # nota >= 4 y nota <7  aprobado
    # nota >=7 y nota <= 10 promocionado
#
# Retorno:
#   - No utiliza 'return'; realiza directamente la acción de imprimir en consola (print)

def nota_final(promedio):
    if promedio < 4:
        print("Desaprobado")
    elif promedio >= 4 and promedio < 7:
        print("Aprobado")
    else:
        print("Promocionado")
    

# ==============================================================================
# 2. PROGRAMA PRINCIPAL (Flujo Global de Ejecución)
# Aquí comienza la ejecución real del programa
# Todas las variables creadas en esta sección son VARIABLES GLOBALES 
# ==============================================================================

# Paso 1: Pedir e ingresar la primera nota por teclado
# nota1: VARIABLE GLOBAL
nota1= int(input("Ingrese la nota1: "))

# Evaluamos 'nota1'. El valor de 'nota1' (global) se copia en 'n' (local) de la función
if es_nota_valida(nota1):
    
    # Paso 2: Si nota1 es válida, pedimos la segunda nota
    # nota2: VARIABLE GLOBAL
    nota2= int(input("Ingrese la nota2: "))
    
    # Validamos 'nota2' llamando nuevamente a la función
    if es_nota_valida(nota2):
        
        # Paso 3: Si nota2 es válida, pedimos la tercera nota
        # nota3: VARIABLE GLOBAL
        nota3= int(input("Ingrese la nota3: "))
        
        # Validamos 'nota3'
        if es_nota_valida(nota3):
            
            # --- TODAS LAS NOTAS SON VÁLIDAS ---
            
            # Secuencia A:
            # 1. Se llama a 'promedio_notas(nota1, nota2, nota3)' pasando las 3 variables globales
            # 2. La función calcula y retorna el promedio numérico
            # 3. Ese valor retornado ingresa inmediatamente como argumento a 'nota_final()',
            #    que imprime si el alumno está Desaprobado, Aprobado o Promocionado 
            nota_final(promedio_notas(nota1,nota2,nota3))
            
            # Secuencia B:
            # Se vuelve a invocar a 'promedio_notas()' para obtener el valor numérico
            # e imprimirlo formateado dentro del f-string.
            print(f'Su nota final es: {promedio_notas(nota1,nota2,nota3)}')
            
        else:
           # Mensaje de error si la nota3 es inválida
           print('Ingrese una nota valida entre 1 y 10')
    else:
        # Mensaje de error si la nota2 es inválida
        print('Ingrese una nota valida entre 1 y 10')
else:
    # Mensaje de error si la nota1 es inválida
    print('Ingrese una nota valida entre 1 y 10')