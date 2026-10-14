def saludar_usuario(nombre_usuario):
    """Retorna un saludo personalizado para el usuario."""
    # nombre_usuario : str
    mensaje: str = f"Bienvenido/a, {nombre_usuario}!"
    return mensaje


# --- Programa Principal ---
nombre: str = input("Ingrese su nombre: ")
resultado: str = saludar_usuario(nombre)
print(resultado)