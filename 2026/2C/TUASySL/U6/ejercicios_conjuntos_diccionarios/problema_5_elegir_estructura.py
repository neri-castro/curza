"""Problema 5 - Integrador: elegir set o dict según el caso"""


def sin_repetidos(lista):
    """Devuelve la lista de elementos únicos, ordenada."""
    return sorted(set(lista))


def buscar_precio(catalogo, producto):
    """Devuelve el precio del producto o -1 si no existe."""
    # precio: float
    precio = catalogo.get(producto, -1)
    return precio


ips = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7"]
catalogo = {"Mouse": 3500.0, "Teclado": 8200.0, "Monitor": 95000.0}

print("IPs distintas:", sin_repetidos(ips))   # set: unicidad
print("Precio Teclado:", buscar_precio(catalogo, "Teclado"))   # dict: búsqueda
print("Precio Webcam:", buscar_precio(catalogo, "Webcam"))
