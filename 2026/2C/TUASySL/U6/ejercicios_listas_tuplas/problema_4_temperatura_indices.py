"""Problema 4 - Temperatura del rack (for con range(len()))"""

UMBRAL_FRIO = 15.0

lecturas = [18.0, 14.5, 20.0, 12.0, 16.5]
cant_alertas = 0

for i in range(len(lecturas)):
    if lecturas[i] < UMBRAL_FRIO:
        print(f"Medición {i + 1}: Temperatura baja de {lecturas[i]} °C")
        cant_alertas += 1

print("Total de alertas:", cant_alertas)
