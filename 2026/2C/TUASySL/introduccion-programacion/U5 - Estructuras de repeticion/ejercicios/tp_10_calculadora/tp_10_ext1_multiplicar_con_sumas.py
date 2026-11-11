"""Trabajo práctico 10, extensión 1: multiplicar enteros con sumas sucesivas"""


def multiplicar_con_sumas(a, b):
    """Multiplica dos enteros sumando 'a' una cantidad 'b' de veces."""
    resultado = 0
    for _ in range(abs(b)):
        resultado += a
    if b < 0:
        resultado = -resultado
    return resultado


print(multiplicar_con_sumas(4, 3))    # 12
print(multiplicar_con_sumas(4, -3))   # -12
