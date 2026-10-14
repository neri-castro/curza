# ============================================================
# PROBLEMA 2: Conversor de Temperatura F → C
# ============================================================

OFFSET = 32
FACTOR = 5 / 9


def fahrenheit_a_celsius(temp_fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    # temp_fahrenheit : float
    temp_celsius: float = (temp_fahrenheit - OFFSET) * FACTOR
    return temp_celsius


# --- Programa Principal ---
temp_f: float = float(input("Ingrese temperatura en Fahrenheit: "))
temp_c: float = fahrenheit_a_celsius(temp_f)
print(f"Resultado: {round(temp_c, 2)} °C")