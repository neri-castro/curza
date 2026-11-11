"""Problema 2 - Inventario de insumos (lista de tuplas + desempaquetado)"""

STOCK_MINIMO = 10

inventario = [("Mouse", "Periféricos", 25), ("Cable UTP", "Redes", 6),
              ("Teclado", "Periféricos", 8), ("Switch", "Redes", 12)]
cant_reponer = 0

for nombre, categoria, stock in inventario:
    if stock < STOCK_MINIMO:
        print(f"Reponer {nombre} ({categoria}): quedan {stock}")
        cant_reponer += 1

print("Productos a reponer:", cant_reponer)
