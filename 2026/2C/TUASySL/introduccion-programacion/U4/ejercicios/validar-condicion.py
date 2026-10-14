# ============================================================
# PROBLEMA 3: Validación y Condición Académica de Estudiantes
# ============================================================

def es_nota_valida(nota_evaluacion):
    """Retorna True si la nota está en el rango válido 0-10."""
    # nota_evaluacion : int
    return 0 <= nota_evaluacion <= 10


def determinar_condicion_alumno(nota_uno, nota_dos):
    """Determina la condición académica del alumno según sus dos notas."""
    # nota_uno : int
    # nota_dos : int
    condicion: str

    if nota_uno >= 7 and nota_dos >= 7:
        condicion = 'Promociona'
    elif nota_uno >= 4 and nota_dos >= 4:
        condicion = 'Aprueba'
    else:
        condicion = 'Recupera'

    return condicion


n1 = int(input("Nota del primer parcial (0-10): "))
n2 = int(input("Nota del segundo parcial (0-10): "))

if es_nota_valida(n1) and es_nota_valida(n2):
    resultado: str = determinar_condicion_alumno(n1, n2)
    print(f"Condición académica: {resultado}")
else:
    print("Error: alguna nota está fuera del rango válido (0-10)")