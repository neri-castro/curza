"""Problema 3: Monitoreo térmico continuo de servidores

1. COMPRENDER
   - Ruido: Data Center de Viedma, río Negro, rango óptimo 18-24 °C.
   - Entradas: lecturas de temperatura (float).
   - Constantes: CENTINELA_FIN = 0.0, UMBRAL_ALERTA = 35.0
   - Salidas: cant_alertas (lecturas > UMBRAL_ALERTA).

2. PLAN
   - Var. control: temperatura
   - Condición while: temperatura != CENTINELA_FIN
   - Actualización: leer la siguiente temperatura al final del bloque

4. TRAZA (entradas 22.0, 36.5, 35.0, 40.0, 0.0)
   temperatura | > 35.0 | cant_alertas
   22.0        | no     | 0
   36.5        | sí     | 1
   35.0        | no     | 1   (frontera: igual al umbral no alerta)
   40.0        | sí     | 2
   0.0         | fin    | 2
"""

CENTINELA_FIN = 0.0
UMBRAL_ALERTA = 35.0

cant_alertas = 0

temperatura = float(input("Temperatura (0 para terminar): "))
while temperatura != CENTINELA_FIN:
    if temperatura > UMBRAL_ALERTA:
        cant_alertas += 1
    temperatura = float(input("Temperatura (0 para terminar): "))

print(f"Lecturas críticas registradas: {cant_alertas}")
