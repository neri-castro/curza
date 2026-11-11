"""Problema 3 - Diccionario de diccionarios: nómina por legajo"""

NOTA_PROMOCION = 8.0

nomina = {
    "FAI-1": {"nombre": "Brisa", "nota": 8.5},
    "FAI-2": {"nombre": "Abel", "nota": 7.0},
    "FAI-3": {"nombre": "Celeste", "nota": 9.5},
}

# Acceso directo por clave
print("Nota de Abel:", nomina["FAI-2"]["nota"])

# Recorrer y acumular
suma = 0.0
cant_promocionados = 0
for legajo, ficha in nomina.items():
    suma += ficha["nota"]
    if ficha["nota"] >= NOTA_PROMOCION:
        print(f"{ficha['nombre']} ({legajo}) promociona")
        cant_promocionados += 1

print("Promedio del curso:", round(suma / len(nomina), 2))
print("Promocionados:", cant_promocionados)
