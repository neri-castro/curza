# TP 1 - Algoritmos y Resolución de Problemas

print("=== TRABAJO PRÁCTICO 1 ===\n")

# ACTIVIDAD 1 - PROBLEMA 1: Asignación de ocupaciones
print("PROBLEMA 1: Asignación de ocupaciones")
print("Solución utilizando lógica deductiva:")
print("- Darío solo puede ser despachador → Darío = despachador")
print("- Alberto puede ser almacenero, portero o despachador, pero despachador ya está ocupado")
print("- Bernardo puede ser chofer o maquinista")
print("- Camilo puede ser chofer o almacenero")
print("- Gerardo puede ser almacenero o despachador, pero despachador ya está ocupado")
print("- Si Gerardo es almacenero, entonces Camilo debe ser chofer")
print("- Si Camilo es chofer, entonces Bernardo debe ser maquinista")
print("- Alberto debe ser portero (única opción restante)")
print()
print("SOLUCIÓN:")
print("Alberto: Portero")
print("Bernardo: Maquinista") 
print("Camilo: Chofer")
print("Darío: Despachador")
print("Gerardo: Almacenero")
print("=" * 50)

# PROBLEMA 2: Precio del traje y la camisa
print("PROBLEMA 2: Precio del traje y la camisa")
# traje + camisa = 1100
# traje = camisa + 1000
# Sustituyendo: (camisa + 1000) + camisa = 1100
# 2 * camisa + 1000 = 1100
# 2 * camisa = 100
# camisa = 50

precioCamisa = (1100 - 1000) / 2
precioTraje = precioCamisa + 1000

print(f"Precio de la camisa: ${precioCamisa}")
print(f"Precio del traje: ${precioTraje}")
print(f"Total: ${precioCamisa + precioTraje}")
print("=" * 50)

# ACTIVIDAD 2: Algoritmos
print("ACTIVIDAD 2: Algoritmos\n")

# (a) Calcular descuentos
def calcularDescuento(precioProducto, porcentajeDescuento):
    """Calcula el precio final aplicando descuento"""
    descuento = precioProducto * (porcentajeDescuento / 100)
    precioFinal = precioProducto - descuento
    return precioFinal

print("(a) Calcular descuentos:")
precio = float(input("Ingrese el precio del producto: $"))
descuento = float(input("Ingrese el porcentaje de descuento: "))
resultado = calcularDescuento(precio, descuento)
print(f"Precio final con {descuento}% de descuento: ${resultado:.2f}")
print()

# (b) Calcular recargo del 12%
def calcularRecargo(precioProducto):
    """Calcula el precio con 12% de recargo"""
    recargo = precioProducto * 0.12
    precioFinal = precioProducto + recargo
    return precioFinal

print("(b) Calcular recargo del 12%:")
precio = float(input("Ingrese el precio del producto: $"))
resultado = calcularRecargo(precio)
print(f"Precio con recargo del 12%: ${resultado:.2f}")
print()

# (c) Promedio de 3 notas
def calcularPromedio(nota1, nota2, nota3):
    """Calcula el promedio de 3 notas"""
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

print("(c) Promedio de 3 notas:")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = calcularPromedio(nota1, nota2, nota3)
print(f"El promedio es: {promedio:.2f}")
print()

# (d) Calcular tercera nota para obtener promedio deseado
def calcularTerceraNota(nota1, nota2, promedioDeseado):
    """Calcula la tercera nota necesaria para obtener el promedio deseado"""
    # promedio = (nota1 + nota2 + nota3) / 3
    # promedioDeseado = (nota1 + nota2 + nota3) / 3
    # nota3 = promedioDeseado * 3 - nota1 - nota2
    terceraNota = promedioDeseado * 3 - nota1 - nota2
    return terceraNota

print("(d) Calcular tercera nota para promedio deseado:")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
promedioDeseado = float(input("Ingrese el promedio deseado: "))
terceraNota = calcularTerceraNota(nota1, nota2, promedioDeseado)
print(f"La tercera nota debe ser: {terceraNota:.2f}")
print()

# (e) Metros nadados
def calcularMetrosNadados(piletasNadadas, longitudPileta):
    """Calcula los metros nadados"""
    metrosNadados = piletasNadadas * longitudPileta
    return metrosNadados

print("(e) Metros nadados:")
piletas = int(input("Ingrese el número de piletas nadadas: "))
longitud = float(input("Ingrese la longitud de la pileta (metros): "))
metros = calcularMetrosNadados(piletas, longitud)
print(f"Metros nadados: {metros} m")
print()

# (f) Porcentaje de entrenamiento
def calcularPorcentajeEntrenamiento(metrosANadar, metrosNadados):
    """Calcula el porcentaje de entrenamiento realizado"""
    porcentaje = (metrosNadados / metrosANadar) * 100
    return porcentaje

print("(f) Porcentaje de entrenamiento:")
metrosANadar = float(input("Ingrese los metros a nadar: "))
metrosNadados = float(input("Ingrese los metros efectivamente nadados: "))
porcentaje = calcularPorcentajeEntrenamiento(metrosANadar, metrosNadados)
print(f"Porcentaje de entrenamiento realizado: {porcentaje:.2f}%")
print()

# (g) Tarifa en JUS
def calcularTarifaJUS(cantidadJUS):
    """Calcula la tarifa en pesos basada en JUS"""
    valorJUS = 43958.00
    tarifaPesos = cantidadJUS * valorJUS
    return tarifaPesos

print("(g) Tarifa en JUS:")
jus = float(input("Ingrese la cantidad de JUS: "))
tarifa = calcularTarifaJUS(jus)
print(f"Tarifa a cobrar: ${tarifa:.2f}")
print()

# (h) Convertir pesos a JUS
def convertirPesosAJUS(tarifaPesos):
    """Convierte una tarifa en pesos a JUS"""
    valorJUS = 43958.00
    cantidadJUS = tarifaPesos / valorJUS
    return cantidadJUS

print("(h) Convertir pesos a JUS:")
tarifa = float(input("Ingrese la tarifa en pesos: $"))
jus = convertirPesosAJUS(tarifa)
print(f"Equivale a: {jus:.4f} JUS")
print()

# (i) Convertir pesos a dólares
def convertirPesosADolares(pesos, tipoCambio):
    """Convierte pesos a dólares"""
    dolares = pesos / tipoCambio
    return dolares

print("(i) Convertir pesos a dólares:")
pesos = float(input("Ingrese la cantidad en pesos: $"))
tipoCambio = float(input("Ingrese el tipo de cambio (pesos por dólar): "))
dolares = convertirPesosADolares(pesos, tipoCambio)
print(f"${pesos} pesos equivalen a: USD${dolares:.2f}")
print()

# (j) Convertir dólares a pesos
def convertirDolaresAPesos(dolares, tipoCambio):
    """Convierte dólares a pesos"""
    pesos = dolares * tipoCambio
    return pesos

print("(j) Convertir dólares a pesos:")
dolares = float(input("Ingrese la cantidad en dólares: USD$"))
tipoCambio = float(input("Ingrese el tipo de cambio (pesos por dólar): "))
pesos = convertirDolaresAPesos(dolares, tipoCambio)
print(f"USD${dolares} dólares equivalen a: ${pesos:.2f} pesos")
print()

print("=== FIN DEL TP 1 ===")
