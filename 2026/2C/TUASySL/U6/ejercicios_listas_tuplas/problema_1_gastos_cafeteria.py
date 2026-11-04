"""Problema 1 - Gastos de la cantina (lista + for por elementos)"""

LIMITE_GASTO = 1500.0

gastos_semana = [800.0, 1200.5, 2300.0, 950.0, 1800.0]
total_gastado = 0.0
cant_gastos_altos = 0

for gasto in gastos_semana:
    total_gastado += gasto
    if gasto > LIMITE_GASTO:
        cant_gastos_altos += 1

print("Total gastado:", total_gastado)
print("Gastos que superaron el límite:", cant_gastos_altos)
