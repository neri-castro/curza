# 
# 
# NOTA DE LA CÁTEDRA:
# COMENTARIOS Y ACLARACIONES REALIZADAS CON IA GEMINI NOTEBOOK
# 
#   Variable            |   Tipo de Ámbito      |   ¿Dónde existe y vive en memoria?
#   ----------------------------------------------------------------------------------------------------------------------
#   nombre              |   Variable Local      |   Solo dentro de la función saludo. Se destruye al terminar la función.
#   perfil (parámetro)  |   Variable Local      |   Recipiente interno de la función saludo.
#   tipo_perfil         |   Variable Local      |   Creada dentro del bloque condicional de la función.
#   persona             |   Variable Global     |   En el programa principal; accesible en todo el archivo.
#   perfil (ingreso)    |   Variable Global     |   Guardada en el programa principal al leer por teclado.
#   -----------------------------------------------------------------------------------------------------------------------
# 
# probemos como se hace una funcion

# ==============================================================================
# 1. DEFINICIÓN DE LA FUNCIÓN (Fase de Declaración)
# Las funciones se ubican en la parte superior del archivo para que el
# intérprete de Python las conozca antes de ser invocadas.
# ==============================================================================

# Definición de la función 'saludo' con dos parámetros de entrada.
# Parámetros formales:
#   - nombre: VARIABLE LOCAL (existe únicamente dentro de esta función).
#   - perfil: VARIABLE LOCAL (recibe la copia del valor enviado desde la llamada).
def saludo(nombre,perfil):
    
    # Estructura de selección condicional múltiple (if-elif-else)
    if perfil=='a':
        # tipo_perfil: VARIABLE LOCAL (creada e inicializada dentro de la función)
        tipo_perfil='alumn@'
    elif perfil=='p': 
        tipo_perfil='profesor'
    else:
        tipo_perfil='otro'
        
    # Salida por pantalla usando un f-string con las variables locales
    print(f'Hola {tipo_perfil} {nombre} bienvenido a clase')


# ==============================================================================
# 2. PROGRAMA PRINCIPAL (Flujo Global de Ejecución)
# Aquí inicia la ejecución secuencial del programa.
# Las variables creadas en esta sección pertenecen al ÁM BITO GLOBAL.
# ==============================================================================

# Paso 1: Solicitar el nombre del usuario por teclado
# persona: VARIABLE GLOBAL (almacena la cadena ingresada)
persona=str(input('Bienvenid@ ingrese su nombre: '))

# Paso 2: Solicitar el perfil del usuario por teclado
# perfil: VARIABLE GLOBAL (almacena el carácter ingresado)
# 💡 Nota didáctica para la clase: Esta variable 'perfil' es GLOBAL. Aunque comparte
# el mismo nombre con el parámetro de la función, en la memoria RAM son dos
# "cajas" o contenedores independientes.
perfil=str(input('Ingrese su perfil (a alumno, p profesor, o otro): '))

# Paso 3: Invocación o llamada a la función
# Le pasamos los argumentos o valores reales almacenados en las variables globales (persona, perfil).
# La función recibe estos datos en sus parámetros locales (nombre, perfil) y ejecuta sus instrucciones.
saludo(persona,perfil)