"""Ejercicio 9.1: cajero de supermercado"""

LIMITE_DESCUENTO = 10000
DESCUENTO = 0.10

cantidad_productos = 0
total = 0.0
precio_mas_caro = 0.0

precio = float(input("Precio del producto (0 para terminar): "))
while precio != 0:
    cantidad_productos += 1
    total += precio
    if precio > precio_mas_caro:
        precio_mas_caro = precio
    precio = float(input("Precio del producto (0 para terminar): "))

if total > LIMITE_DESCUENTO:
    total -= total * DESCUENTO
    print("Se aplicó un 10% de descuento")

print(f"Productos: {cantidad_productos}")
print(f"Producto más caro: ${precio_mas_caro:.2f}")
print(f"Total: ${total:.2f}")
