# Práctica extra: Listas y tuplas (solo `for`, sin `while`)

**TUASySL - Introducción a la Programación | CURZAS - UNCo**

Reglas: `snake_case` para variables, `SCREAMING_SNAKE_CASE` para constantes, resolver con `for` y completar las 4 fases de Polya (comprender, planificar, ejecutar, verificar con prueba de escritorio).

## Problema 1: Gastos de la cantina
Lista `gastos_semana = [800.0, 1200.5, 2300.0, 950.0, 1800.0]` y constante `LIMITE_GASTO = 1500.0`. Con un `for` por elementos: acumular `total_gastado` y contar en `cant_gastos_altos` los gastos que superan el límite. Mostrar ambos. *Esperado: 7050.5 y 2.*

## Problema 2: Inventario de insumos
Lista de tuplas `(nombre, categoria, stock)`:
`[("Mouse","Periféricos",25), ("Cable UTP","Redes",6), ("Teclado","Periféricos",8), ("Switch","Redes",12)]`, constante `STOCK_MINIMO = 10`. Recorrer desempaquetando cada tupla; si `stock < STOCK_MINIMO`, imprimir aviso de reposición y contar. Mostrar el total a reponer. *Esperado: 2.*

## Problema 3: Mayores de edad con `.append()`
`edades = [17, 22, 19, 16, 30, 18, 15]`, constante `EDAD_MINIMA = 18`. Crear `edades_mayores = []`, recorrer con `for` y agregar con `.append()` las que cumplen. Imprimir la lista y el promedio. *Esperado: [22, 19, 30, 18] y 22.25.*

## Problema 4: Temperatura del rack
`lecturas = [18.0, 14.5, 20.0, 12.0, 16.5]`, constante `UMBRAL_FRIO = 15.0`. Recorrer con `for i in range(len(lecturas))`; si la lectura es menor al umbral, imprimir `f"Medición {i + 1}: Temperatura baja de {lecturas[i]} °C"` y contar. *Esperado: 2 alertas.*

## Problema 5: Mayor valor y su posición
`velocidades = [54.2, 98.7, 70.1, 98.9, 33.0]`. Sin usar `max()`, encontrar con `range(len())` el mayor valor y el índice donde está. *Esperado: 98.9 en la posición 3.*

Soluciones en los archivos `problema_N_*.py`.
