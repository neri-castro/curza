"""Lab for - Problema 1: exceso de consumo de energía de 5 servidores"""

UMBRAL_EFICIENCIA = 120.0
total_exceso_kwh = 0.0

for servidor in range(1, 6):
    consumo_actual = float(input(f"Ingrese consumo kWh servidor {servidor}: "))
    if consumo_actual > UMBRAL_EFICIENCIA:
        total_exceso_kwh += consumo_actual - UMBRAL_EFICIENCIA

print(f"Total acumulado de consumo en exceso: {total_exceso_kwh} kWh")
