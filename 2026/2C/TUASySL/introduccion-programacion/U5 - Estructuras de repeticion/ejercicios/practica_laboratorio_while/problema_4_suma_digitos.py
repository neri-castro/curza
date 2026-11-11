"""Problema 4: Descomposición matemática de código de catálogo

1. COMPRENDER
   - Ruido: horario 8-20 hs, más de 4.500 libros, sistema KOHA.
   - Entradas: codigo (int positivo).
   - Constantes: ninguna.
   - Salidas: suma_digitos.

2. PLAN
   - Var. control: numero_actual
   - Condición while: numero_actual > 0
   - Actualización: numero_actual = numero_actual // 10

4. TRAZA (codigo 456)
   numero_actual | digito | suma_digitos
   456           | 6      | 6
   45            | 5      | 11
   4             | 4      | 15
   0             | fin    | 15
   Frontera: 7 -> una vuelta, suma 7.
"""

codigo = int(input("Ingrese el código numérico entero positivo: "))

numero_actual = codigo
suma_digitos = 0
while numero_actual > 0:
    digito = numero_actual % 10
    suma_digitos += digito
    numero_actual = numero_actual // 10

print(f"La suma de los dígitos de {codigo} es {suma_digitos}")
