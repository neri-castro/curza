"""Ejercicio 7.5: alumno con la nota más alta (termina con 'fin')"""

mejor_nombre = None
mejor_nota = 0.0

nombre = input("Nombre del alumno ('fin' para terminar): ")
while nombre != "fin":
    nota = float(input(f"Nota de {nombre}: "))
    if mejor_nombre is None or nota > mejor_nota:
        mejor_nombre = nombre
        mejor_nota = nota
    nombre = input("Nombre del alumno ('fin' para terminar): ")

if mejor_nombre is None:
    print("No se ingresaron alumnos")
else:
    print(f"Mejor nota: {mejor_nombre} con {mejor_nota}")
