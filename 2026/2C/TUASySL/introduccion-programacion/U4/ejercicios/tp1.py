# ============================================================
# PROBLEMA 1: Sensor de Temperatura del Servidor "Limay"
# ============================================================

UMBRAL_CRITICO = 45.0


def es_temperatura_critica(temperatura_actual):
    """Retorna True si la temperatura supera o iguala el umbral crítico."""
    # temperatura_actual : float
    return temperatura_actual >= UMBRAL_CRITICO


# --- Programa Principal ---
temp: float = float(input("Ingrese temperatura actual del servidor (°C): "))
if es_temperatura_critica(temp):
    print("ALERTA: Activar refrigeración")
else:
    print("Estado normal")