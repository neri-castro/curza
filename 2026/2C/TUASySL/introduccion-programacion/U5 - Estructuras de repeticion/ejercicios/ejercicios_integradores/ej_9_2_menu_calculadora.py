"""Ejercicio 9.2: menú de calculadora"""

opcion = ""
while opcion != "4":
    print("\n1) Sumar  2) Restar  3) Multiplicar  4) Salir")
    opcion = input("Opción: ")
    if opcion in ("1", "2", "3"):
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        if opcion == "1":
            print(f"Resultado: {a + b}")
        elif opcion == "2":
            print(f"Resultado: {a - b}")
        else:
            print(f"Resultado: {a * b}")
    elif opcion != "4":
        print("Opción inválida")
