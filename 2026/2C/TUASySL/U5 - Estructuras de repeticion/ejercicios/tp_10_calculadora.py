"""Trabajo práctico 10: calculadora de consola con for y funciones"""

OPCIONES = ["Sumar", "Restar", "Multiplicar", "Dividir"]


def mostrar_menu():
    """Muestra las opciones numeradas recorriendo la lista OPCIONES."""
    print("\n--- Calculadora ---")
    for numero, opcion in enumerate(OPCIONES, start=1):
        print(f"{numero}) {opcion}")


def pedir_opcion():
    """Pide una opción válida (1 a 4) y la devuelve como entero."""
    opcion = int(input("Elegí una operación (1-4): "))
    while opcion < 1 or opcion > len(OPCIONES):
        opcion = int(input("Opción inválida. Elegí entre 1 y 4: "))
    return opcion


def pedir_numero(mensaje):
    """Pide un número al usuario y lo devuelve como float."""
    return float(input(mensaje))


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    """Devuelve a / b, o None si b es 0."""
    if b == 0:
        return None
    return a / b


def calcular(opcion, a, b):
    """Llama a la función que corresponde a la opción elegida."""
    if opcion == 1:
        return sumar(a, b)
    elif opcion == 2:
        return restar(a, b)
    elif opcion == 3:
        return multiplicar(a, b)
    else:
        return dividir(a, b)


def mostrar_historial(historial):
    """Recorre el historial y muestra cada operación realizada."""
    print("\n--- Historial ---")
    if len(historial) == 0:
        print("No se realizaron operaciones válidas.")
        return
    for numero, linea in enumerate(historial, start=1):
        print(f"{numero}. {linea}")


def main():
    simbolos = ["+", "-", "x", "/"]
    historial = []

    cantidad = int(input("¿Cuántas operaciones querés hacer? "))
    for numero_operacion in range(1, cantidad + 1):
        print(f"\nOperación {numero_operacion} de {cantidad}")
        mostrar_menu()
        opcion = pedir_opcion()
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        resultado = calcular(opcion, a, b)
        if resultado is None:
            print("Error: no se puede dividir por cero.")
            continue

        linea = f"{a} {simbolos[opcion - 1]} {b} = {resultado}"
        print("Resultado:", linea)
        historial.append(linea)

    mostrar_historial(historial)


main()
