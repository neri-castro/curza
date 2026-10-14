# Estructuras de repetición en Python

Introducción a la Programación · Oct 7, 2026 · @Neri Castro

## 1. Introducción: ¿por qué repetir?

Una estructura de repetición (también llamada **bucle**, **ciclo** o **loop**) le dice a la computadora: "ejecutá este bloque de código varias veces". Sin ellas, para mostrar los números del 1 al 100 tendríamos que escribir 100 líneas `print`.

Sin bucle:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Con bucle:

```python
for numero in range(1, 6):
    print(numero)
```

Ambos programas muestran lo mismo, pero el segundo funciona igual de bien para 5, para 100 o para un millón de números. Esto aplica una idea clave de la programación: **no repetir código** (principio DRY, *Don't Repeat Yourself*).

Python tiene dos estructuras de repetición:

| Bucle | Se usa cuando... | Ejemplo típico |
| --- | --- | --- |
| `while` | No sabemos cuántas veces se va a repetir; depende de una condición | Pedir una contraseña hasta que sea correcta |
| `for` | Sabemos cuántas veces repetir, o queremos recorrer una colección | Mostrar cada elemento de una lista |

**Vocabulario básico**

- **Iteración**: cada una de las vueltas que da el bucle.
- **Cuerpo del bucle**: el bloque de código indentado (con sangría) que se repite.
- **Condición**: expresión que vale `True` o `False` y decide si el bucle sigue.
- **Variable de control**: la variable que cambia en cada vuelta y permite que el bucle avance o termine.

**Importante sobre la indentación**: en Python, lo que pertenece al bucle se escribe con 4 espacios de sangría. Lo que no tiene sangría queda fuera del bucle y se ejecuta una sola vez, al terminar.

```python
for i in range(3):
    print("Dentro del bucle")   # se repite 3 veces
print("Fuera del bucle")        # se ejecuta 1 vez
```

## 2. El bucle `while`

`while` significa "mientras". El bucle repite su cuerpo **mientras la condición sea verdadera**. Cuando la condición pasa a ser falsa, el bucle termina y el programa sigue con la línea siguiente.

**Sintaxis**

```python
while condicion:
    # cuerpo: instrucciones que se repiten
```

**¿Cómo funciona paso a paso?**

1. Python evalúa la condición.
2. Si es `True`, ejecuta el cuerpo completo y vuelve al paso 1.
3. Si es `False`, saltea el cuerpo y continúa después del bucle.

Si la condición es falsa desde el principio, el cuerpo **no se ejecuta ninguna vez**.

**Las tres partes de un `while` bien armado**

1. **Inicialización**: darle un valor inicial a la variable de control, antes del bucle.
2. **Condición**: la pregunta que se hace en cada vuelta.
3. **Actualización**: modificar la variable dentro del cuerpo, para que algún día la condición sea falsa.

### Ejemplo 1: contar del 1 al 5

```python
contador = 1              # 1. inicialización
while contador <= 5:      # 2. condición
    print(contador)
    contador = contador + 1   # 3. actualización
print("Fin")
```

Salida: `1 2 3 4 5 Fin` (cada número en una línea).

**Prueba de escritorio** (seguimiento a mano de las variables):

| Vuelta | `contador` antes | ¿`contador <= 5`? | Se imprime | `contador` después |
| --- | --- | --- | --- | --- |
| 1 | 1 | True | 1 | 2 |
| 2 | 2 | True | 2 | 3 |
| 3 | 3 | True | 3 | 4 |
| 4 | 4 | True | 4 | 5 |
| 5 | 5 | True | 5 | 6 |
| — | 6 | False | (sale del bucle) | — |

Tip: `contador = contador + 1` se puede escribir abreviado como `contador += 1`. Lo mismo vale para `-=`, `*=` y `/=`.

### Ejemplo 2: cuenta regresiva

```python
n = 3
while n > 0:
    print(n)
    n -= 1
print("¡Despegue!")
```

### Ejemplo 3: repetir hasta que el usuario quiera salir

Acá se ve la verdadera fortaleza de `while`: no sabemos de antemano cuántas vueltas va a dar.

```python
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribí algo (o 'salir' para terminar): ")
    print("Escribiste:", respuesta)
```

### Ejemplo 4: validar un dato ingresado

```python
edad = int(input("Ingresá tu edad: "))
while edad < 0:
    print("La edad no puede ser negativa.")
    edad = int(input("Ingresá tu edad: "))
print("Edad registrada:", edad)
```

### Cuidado: el bucle infinito

Si la condición nunca se vuelve falsa, el programa queda repitiendo para siempre. El error más común es olvidar la actualización:

```python
contador = 1
while contador <= 5:
    print(contador)
    # falta contador += 1 → imprime 1 para siempre
```

Si te pasa, detené el programa con **Ctrl + C**.

### Ejercicios: `while`

**Ejercicio 2.1 (fácil)**. Mostrar los números del 10 al 1, en orden descendente.

```python
# Solución
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1
```

**Ejercicio 2.2 (fácil)**. Mostrar los números pares entre 2 y 20 inclusive.

```python
# Solución
par = 2
while par <= 20:
    print(par)
    par += 2
```

**Ejercicio 2.3 (intermedio)**. Pedir números al usuario hasta que ingrese 0. Al final, mostrar la suma de todos los números ingresados.

```python
# Solución
suma = 0
numero = int(input("Ingresá un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingresá un número (0 para terminar): "))
print("La suma total es:", suma)
```

**Ejercicio 2.4 (intermedio)**. Pedir una contraseña hasta que el usuario escriba `python123`. Mostrar cuántos intentos le llevó.

```python
# Solución
intentos = 1
clave = input("Contraseña: ")
while clave != "python123":
    print("Incorrecta, probá de nuevo.")
    intentos += 1
    clave = input("Contraseña: ")
print("Acceso concedido en", intentos, "intento(s).")
```

**Ejercicio 2.5 (avanzado)**. Dado un número entero positivo, contar cuántos dígitos tiene, sin convertirlo a texto. Pista: dividir entero por 10 (`//`) le quita el último dígito.

```python
# Solución
numero = int(input("Ingresá un número entero positivo: "))
digitos = 0
while numero > 0:
    numero //= 10
    digitos += 1
print("Cantidad de dígitos:", digitos)
```

Prueba de escritorio con 345: 345 → 34 → 3 → 0, son 3 vueltas, entonces 3 dígitos. (Para pensar: ¿qué pasa si el usuario ingresa 0? ¿Cómo lo arreglarías?)

**Ejercicio 2.6 (avanzado)**. Juego de adivinar: la computadora elige un número al azar entre 1 y 50. El usuario intenta adivinarlo y el programa le dice "más alto" o "más bajo" hasta que acierte.

```python
# Solución
import random

secreto = random.randint(1, 50)
intento = int(input("Adiviná el número (1-50): "))
while intento != secreto:
    if intento < secreto:
        print("Más alto")
    else:
        print("Más bajo")
    intento = int(input("Probá otra vez: "))
print("¡Correcto! Era el", secreto)
```

## 3. El bucle `for` y la función `range()`

`for` significa "para cada". Recorre una secuencia de valores, uno por uno, y ejecuta el cuerpo una vez por cada valor. A diferencia de `while`, **no hay que inicializar ni actualizar la variable a mano**: Python lo hace solo.

**Sintaxis**

```python
for variable in secuencia:
    # cuerpo: se ejecuta una vez por cada elemento
```

En cada vuelta, `variable` toma el siguiente valor de la secuencia. Cuando no quedan valores, el bucle termina.

### La función `range()`

`range()` genera una secuencia de números enteros. Es la compañera natural de `for` cuando queremos repetir algo una cantidad conocida de veces.

| Forma | Genera | Ejemplo | Resultado |
| --- | --- | --- | --- |
| `range(fin)` | De 0 hasta `fin - 1` | `range(5)` | 0, 1, 2, 3, 4 |
| `range(inicio, fin)` | De `inicio` hasta `fin - 1` | `range(2, 6)` | 2, 3, 4, 5 |
| `range(inicio, fin, paso)` | De `inicio` hasta `fin - 1`, saltando de a `paso` | `range(0, 10, 3)` | 0, 3, 6, 9 |
| `range(inicio, fin, paso negativo)` | Cuenta hacia atrás | `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

**Regla de oro**: el valor `fin` **nunca se incluye**. Para llegar hasta 10 hay que escribir `range(1, 11)`.

### Ejemplo 1: repetir algo N veces

```python
for i in range(3):
    print("Hola")
```

Salida: `Hola` tres veces. Cuando no usamos la variable, es costumbre llamarla `_`: `for _ in range(3):`.

### Ejemplo 2: del 1 al 5

```python
for numero in range(1, 6):
    print(numero)
```

Comparalo con el Ejemplo 1 de `while`: hace lo mismo en menos líneas y sin riesgo de bucle infinito.

### Ejemplo 3: tabla de multiplicar

```python
n = 7
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
```

### Ejemplo 4: cuenta regresiva con paso negativo

```python
for n in range(10, 0, -1):
    print(n)
print("¡Feliz año nuevo!")
```

### `for` vs `while`: ¿cuál elijo?

Todo lo que hace un `for` se puede hacer con `while`, pero no al revés de forma tan cómoda. Como regla práctica:

- ¿Sé cuántas veces repetir, o tengo una colección para recorrer? → `for`.
- ¿Depende de algo que pasa durante la ejecución (lo que ingresa el usuario, un cálculo)? → `while`.

### Ejercicios: `for` y `range()`

**Ejercicio 3.1 (fácil)**. Mostrar los números del 1 al 20.

```python
# Solución
for i in range(1, 21):
    print(i)
```

**Ejercicio 3.2 (fácil)**. Mostrar los múltiplos de 5 entre 0 y 50, usando el tercer parámetro de `range()`.

```python
# Solución
for multiplo in range(0, 51, 5):
    print(multiplo)
```

**Ejercicio 3.3 (intermedio)**. Pedir un número N y mostrar su tabla de multiplicar del 1 al 10.

```python
# Solución
n = int(input("¿Qué tabla querés ver? "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

Nota: `f"..."` es un *f-string*; lo que va entre llaves `{}` se reemplaza por su valor.

**Ejercicio 3.4 (intermedio)**. Calcular la suma de los números del 1 al 100.

```python
# Solución
suma = 0
for i in range(1, 101):
    suma += i
print("La suma es:", suma)   # 5050
```

**Ejercicio 3.5 (intermedio)**. Pedir 5 notas al usuario y mostrar el promedio.

```python
# Solución
cantidad = 5
total = 0
for i in range(1, cantidad + 1):
    nota = float(input(f"Nota {i}: "))
    total += nota
print("Promedio:", total / cantidad)
```

**Ejercicio 3.6 (avanzado)**. Calcular el factorial de un número N. El factorial de N (N!) es el producto 1 × 2 × 3 × ... × N. Por ejemplo, 5! = 120.

```python
# Solución
n = int(input("Número: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
```

Observá que `factorial` arranca en 1 y no en 0: si arrancara en 0, todo producto daría 0.

**Ejercicio 3.7 (avanzado)**. Mostrar los primeros N términos de la sucesión de Fibonacci: 0, 1, 1, 2, 3, 5, 8... Cada término es la suma de los dos anteriores.

```python
# Solución
n = int(input("¿Cuántos términos? "))
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
```

## 4. Recorrer cadenas y listas con `for`

`for` no solo trabaja con números: puede recorrer **cualquier secuencia**. Las más usadas son las cadenas de texto (`str`) y las listas (`list`). En cada vuelta, la variable toma el siguiente elemento.

### Recorrer una cadena (letra por letra)

```python
palabra = "Python"
for letra in palabra:
    print(letra)
```

Salida: `P`, `y`, `t`, `h`, `o`, `n`, cada una en una línea.

### Recorrer una lista

```python
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print("Me gusta la", fruta)
```

**Buena práctica**: usar un nombre en plural para la lista y en singular para la variable (`frutas` → `fruta`, `alumnos` → `alumno`). El código se lee casi como castellano.

### Cuando también necesito la posición: `enumerate()`

`enumerate()` entrega en cada vuelta dos cosas: la posición (índice) y el elemento.

```python
alumnos = ["Ana", "Luis", "Sofía"]
for posicion, alumno in enumerate(alumnos, start=1):
    print(posicion, "-", alumno)
```

Salida:

```text
1 - Ana
2 - Luis
3 - Sofía
```

También se puede recorrer por índice con `range(len(lista))`, pero `enumerate()` es más claro y es la forma recomendada en Python:

```python
# Funciona, pero es menos legible
for i in range(len(alumnos)):
    print(i, alumnos[i])
```

### Construir una lista nueva dentro de un bucle

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for n in numeros:
    cuadrados.append(n * n)
print(cuadrados)   # [1, 4, 9, 16, 25]
```

### Ejercicios: recorrer secuencias

**Ejercicio 4.1 (fácil)**. Dada la lista `colores = ["rojo", "verde", "azul"]`, mostrar cada color en mayúsculas.

```python
# Solución
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color.upper())
```

**Ejercicio 4.2 (fácil)**. Pedir una palabra y mostrar cuántas letras tiene, contándolas con un bucle (sin usar `len`).

```python
# Solución
palabra = input("Palabra: ")
cantidad = 0
for _ in palabra:
    cantidad += 1
print("Tiene", cantidad, "letras")
```

**Ejercicio 4.3 (intermedio)**. Pedir una frase y contar cuántas vocales tiene.

```python
# Solución
frase = input("Frase: ")
vocales = 0
for letra in frase.lower():
    if letra in "aeiouáéíóú":
        vocales += 1
print("Cantidad de vocales:", vocales)
```

**Ejercicio 4.4 (intermedio)**. Dada una lista de números, crear una nueva lista solo con los pares.

```python
# Solución
numeros = [3, 8, 12, 7, 5, 20, 1]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)   # [8, 12, 20]
```

**Ejercicio 4.5 (avanzado)**. Invertir una palabra usando un bucle (sin usar `[::-1]`). Ejemplo: `"hola"` → `"aloh"`.

```python
# Solución
palabra = input("Palabra: ")
invertida = ""
for letra in palabra:
    invertida = letra + invertida   # cada letra se pone adelante
print(invertida)
```

**Ejercicio 4.6 (avanzado)**. Dada una lista de alumnos y otra de sus notas (en el mismo orden), mostrar quiénes aprobaron (nota ≥ 6) con su número de orden.

```python
# Solución
alumnos = ["Ana", "Luis", "Sofía", "Pedro"]
notas = [8, 4, 6, 9]
for i, alumno in enumerate(alumnos):
    if notas[i] >= 6:
        print(f"{i + 1}. {alumno} aprobó con {notas[i]}")
```

Variante para curiosos: `zip(alumnos, notas)` recorre las dos listas en paralelo: `for alumno, nota in zip(alumnos, notas):`.

## 5. Control del bucle: `break`, `continue` y `else`

Estas palabras permiten cambiar el recorrido normal de un bucle. Sirven tanto en `for` como en `while`.

| Instrucción | Qué hace |
| --- | --- |
| `break` | Corta el bucle inmediatamente y sale de él |
| `continue` | Saltea lo que queda de la vuelta actual y pasa a la siguiente |
| `else` (del bucle) | Se ejecuta al final **solo si el bucle terminó sin `break`** |

### `break`: salir antes de tiempo

```python
for numero in range(1, 11):
    if numero == 5:
        break
    print(numero)
print("Salí del bucle")
```

Salida: `1 2 3 4` y luego `Salí del bucle`. Al llegar a 5, el bucle se corta sin imprimirlo.

Un uso muy común es el menú con `while True` (un bucle que en principio es infinito) y una salida con `break`:

```python
while True:
    opcion = input("1) Saludar  2) Salir: ")
    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        break
    else:
        print("Opción inválida")
print("Chau")
```

### `continue`: saltear una vuelta

```python
for numero in range(1, 8):
    if numero % 2 == 0:
        continue      # si es par, no lo muestra y pasa al siguiente
    print(numero)
```

Salida: `1 3 5 7`.

**Atención con `while`**: si usás `continue` antes de actualizar la variable de control, generás un bucle infinito.

```python
i = 0
while i < 5:
    if i == 2:
        continue   # ¡i nunca llega a i += 1! Bucle infinito
    i += 1
```

### `else` en un bucle

Es poco común en otros lenguajes, pero útil para búsquedas: el `else` se ejecuta si el bucle **terminó normalmente**, es decir, sin pasar por un `break`.

```python
nombres = ["Ana", "Luis", "Sofía"]
buscado = "Pedro"
for nombre in nombres:
    if nombre == buscado:
        print("Encontrado")
        break
else:
    print("No está en la lista")
```

Como "Pedro" no está, el bucle recorre todo sin `break` y se ejecuta el `else`.

### Ejercicios: `break`, `continue` y `else`

**Ejercicio 5.1 (fácil)**. Mostrar los números del 1 al 20, salteando los múltiplos de 3.

```python
# Solución
for n in range(1, 21):
    if n % 3 == 0:
        continue
    print(n)
```

**Ejercicio 5.2 (fácil)**. Pedir números y sumarlos. Terminar cuando el usuario ingrese un número negativo (que no se suma). Usar `while True` y `break`.

```python
# Solución
suma = 0
while True:
    numero = int(input("Número (negativo para terminar): "))
    if numero < 0:
        break
    suma += numero
print("Suma:", suma)
```

**Ejercicio 5.3 (intermedio)**. Dada una lista de números, mostrar el primero que sea mayor a 100. Si no hay ninguno, informarlo (usar `else`).

```python
# Solución
numeros = [12, 45, 99, 150, 300]
for n in numeros:
    if n > 100:
        print("El primero mayor a 100 es:", n)
        break
else:
    print("Ninguno supera 100")
```

**Ejercicio 5.4 (intermedio)**. Login con 3 intentos como máximo. Si acierta, mostrar "Bienvenido"; si agota los intentos, "Cuenta bloqueada".

```python
# Solución
CLAVE = "1234"
for intento in range(1, 4):
    ingresada = input(f"Intento {intento} - Clave: ")
    if ingresada == CLAVE:
        print("Bienvenido")
        break
    print("Clave incorrecta")
else:
    print("Cuenta bloqueada")
```

Nota: escribir `CLAVE` en mayúsculas es una convención para indicar que es una **constante** (un valor que no debería cambiar).

**Ejercicio 5.5 (avanzado)**. Determinar si un número N es primo (solo divisible por 1 y por sí mismo).

```python
# Solución
n = int(input("Número: "))
if n < 2:
    print(n, "no es primo")
else:
    for divisor in range(2, n):
        if n % divisor == 0:
            print(n, "no es primo, es divisible por", divisor)
            break
    else:
        print(n, "es primo")
```

Mejora para pensar: alcanza con probar divisores hasta la raíz cuadrada de N, es decir `range(2, int(n ** 0.5) + 1)`. ¿Por qué?

## 6. Bucles anidados

Un bucle anidado es **un bucle dentro de otro**. Por cada vuelta del bucle externo, el bucle interno se ejecuta **completo**. Una buena analogía es un reloj: por cada hora (bucle externo), el minutero da 60 vueltas (bucle interno).

```python
for externo in range(1, 4):
    for interno in range(1, 3):
        print(f"externo={externo}, interno={interno}")
```

Salida:

```text
externo=1, interno=1
externo=1, interno=2
externo=2, interno=1
externo=2, interno=2
externo=3, interno=1
externo=3, interno=2
```

Cantidad total de vueltas del interno = vueltas del externo × vueltas del interno = 3 × 2 = 6.

### Ejemplo 1: todas las tablas del 1 al 3

```python
for tabla in range(1, 4):
    print(f"--- Tabla del {tabla} ---")
    for i in range(1, 11):
        print(f"{tabla} x {i} = {tabla * i}")
```

### Ejemplo 2: dibujar un rectángulo de asteriscos

El bucle externo maneja las **filas** y el interno las **columnas**.

```python
filas = 3
columnas = 5
for f in range(filas):
    for c in range(columnas):
        print("*", end="")   # end="" evita el salto de línea
    print()                  # salto de línea al terminar cada fila
```

Salida:

```text
*****
*****
*****
```

**Sobre `break` en bucles anidados**: `break` solo corta el bucle **más cercano** (el interno). El externo sigue con su próxima vuelta.

### Ejercicios: bucles anidados

**Ejercicio 6.1 (fácil)**. Pedir un número N y dibujar un cuadrado de N × N con el carácter `#`.

```python
# Solución
n = int(input("Tamaño: "))
for fila in range(n):
    for columna in range(n):
        print("#", end="")
    print()
```

**Ejercicio 6.2 (intermedio)**. Dibujar un triángulo rectángulo de N filas, donde la fila i tiene i asteriscos.

```text
*
**
***
****
```

```python
# Solución
n = int(input("Altura: "))
for fila in range(1, n + 1):
    for _ in range(fila):
        print("*", end="")
    print()
```

El rango del bucle interno **depende** de la variable del externo: esa es la clave de muchos dibujos.

**Ejercicio 6.3 (intermedio)**. Mostrar la tabla pitagórica del 1 al 5 en forma de grilla.

```python
# Solución
for fila in range(1, 6):
    for columna in range(1, 6):
        print(f"{fila * columna:4}", end="")   # :4 reserva 4 espacios
    print()
```

**Ejercicio 6.4 (avanzado)**. Dibujar una pirámide centrada de N filas.

```text
   *
  ***
 *****
*******
```

```python
# Solución
n = int(input("Altura: "))
for fila in range(1, n + 1):
    espacios = n - fila
    asteriscos = 2 * fila - 1
    for _ in range(espacios):
        print(" ", end="")
    for _ in range(asteriscos):
        print("*", end="")
    print()
```

Versión corta, usando que en Python se puede multiplicar texto: `print(" " * espacios + "*" * asteriscos)`.

**Ejercicio 6.5 (avanzado)**. Mostrar todos los números primos entre 2 y 50, combinando un bucle externo (candidatos) con uno interno (divisores) y `for...else`.

```python
# Solución
for candidato in range(2, 51):
    for divisor in range(2, candidato):
        if candidato % divisor == 0:
            break
    else:
        print(candidato, end=" ")
print()
```

## 7. Patrones comunes con bucles

Muchos problemas se resuelven combinando un bucle con alguno de estos cinco "moldes". Reconocerlos ahorra mucho tiempo.

| Patrón | Para qué sirve | Valor inicial típico |
| --- | --- | --- |
| Contador | Contar cuántas veces pasa algo | `contador = 0` |
| Acumulador (suma) | Sumar valores | `suma = 0` |
| Acumulador (producto) | Multiplicar valores | `producto = 1` |
| Máximo / mínimo | Encontrar el mayor o menor valor | El primer elemento |
| Bandera (flag) | Recordar si algo ocurrió alguna vez | `encontrado = False` |
| Validación de entrada | Repetir el pedido hasta que el dato sea correcto | Primer pedido antes del `while` |

### Contador

```python
notas = [7, 4, 9, 5, 10]
aprobados = 0
for nota in notas:
    if nota >= 6:
        aprobados += 1
print("Aprobados:", aprobados)   # 3
```

### Acumulador

```python
precios = [1500, 2300, 800]
total = 0
for precio in precios:
    total += precio
print("Total a pagar:", total)   # 4600
```

### Máximo y mínimo

Se toma el primer elemento como "el mejor hasta ahora" y se compara con cada uno de los demás.

```python
temperaturas = [18, 25, 12, 30, 22]
maxima = temperaturas[0]
minima = temperaturas[0]
for t in temperaturas:
    if t > maxima:
        maxima = t
    if t < minima:
        minima = t
print("Máxima:", maxima, "- Mínima:", minima)   # 30 - 12
```

Python ya trae `max()`, `min()` y `sum()`, pero conviene saber construirlos a mano: es la base para problemas más complejos.

### Bandera

```python
numeros = [3, 7, 11, 4, 9]
hay_par = False
for n in numeros:
    if n % 2 == 0:
        hay_par = True
if hay_par:
    print("Hay al menos un número par")
else:
    print("Todos son impares")
```

### Validación de entrada

```python
nota = int(input("Nota (1 a 10): "))
while nota < 1 or nota > 10:
    print("Valor fuera de rango.")
    nota = int(input("Nota (1 a 10): "))
```

### Ejercicios: patrones

**Ejercicio 7.1 (fácil)**. Dada una lista de edades, contar cuántas personas son mayores de edad (18 o más).

```python
# Solución
edades = [15, 22, 17, 30, 18, 12]
mayores = 0
for edad in edades:
    if edad >= 18:
        mayores += 1
print("Mayores de edad:", mayores)   # 3
```

**Ejercicio 7.2 (intermedio)**. Pedir N números y mostrar el mayor, sin usar `max()`.

```python
# Solución
n = int(input("¿Cuántos números? "))
mayor = int(input("Número 1: "))
for i in range(2, n + 1):
    numero = int(input(f"Número {i}: "))
    if numero > mayor:
        mayor = numero
print("El mayor es:", mayor)
```

**Ejercicio 7.3 (intermedio)**. Pedir una nota válida (entre 1 y 10) y repetir el pedido mientras sea inválida. Luego informar si aprobó.

```python
# Solución
nota = int(input("Nota (1 a 10): "))
while nota < 1 or nota > 10:
    nota = int(input("Inválida. Nota (1 a 10): "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
```

**Ejercicio 7.4 (avanzado)**. Dada una lista de números, informar en una sola pasada: cantidad de positivos, cantidad de negativos, suma total y promedio.

```python
# Solución
numeros = [4, -2, 7, 0, -5, 10]
positivos = 0
negativos = 0
suma = 0
for n in numeros:
    suma += n
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
promedio = suma / len(numeros)
print("Positivos:", positivos)    # 3
print("Negativos:", negativos)    # 2
print("Suma:", suma)              # 14
print("Promedio:", round(promedio, 2))   # 2.33
```

**Ejercicio 7.5 (avanzado)**. Pedir el nombre y la nota de alumnos hasta que se ingrese el nombre "fin". Mostrar quién tuvo la nota más alta.

```python
# Solución
mejor_nombre = ""
mejor_nota = -1
nombre = input("Nombre (fin para terminar): ")
while nombre != "fin":
    nota = float(input(f"Nota de {nombre}: "))
    if nota > mejor_nota:
        mejor_nota = nota
        mejor_nombre = nombre
    nombre = input("Nombre (fin para terminar): ")

if mejor_nombre == "":
    print("No se ingresaron alumnos")
else:
    print(f"Mejor nota: {mejor_nombre} con {mejor_nota}")
```

## 8. Errores frecuentes y cómo evitarlos

| Error | Ejemplo con problema | Cómo se corrige |
| --- | --- | --- |
| Bucle infinito por no actualizar la variable | `while i < 5: print(i)` | Agregar `i += 1` dentro del cuerpo |
| Olvidar que `range` excluye el final | `range(1, 10)` para llegar a 10 | `range(1, 11)` |
| Inicializar dentro del bucle | `for n in nums: suma = 0; suma += n` | Poner `suma = 0` **antes** del bucle |
| Acumulador de producto en 0 | `producto = 0` | Arrancar en `producto = 1` |
| Indentación incorrecta | `print` del resultado dentro del bucle | Quitar la sangría para que quede afuera |
| Olvidar los dos puntos | `for i in range(5)` | `for i in range(5):` |
| Modificar la lista mientras se la recorre | `lista.remove(x)` dentro de `for x in lista` | Construir una lista nueva con lo que se quiere conservar |
| `continue` antes de actualizar en `while` | Ver sección 5 | Actualizar la variable antes del `continue` |

**Ejemplo de indentación incorrecta** (muy frecuente en los primeros parciales):

```python
suma = 0
for i in range(1, 4):
    suma += i
    print("Total:", suma)   # se imprime 3 veces: 1, 3, 6
```

```python
suma = 0
for i in range(1, 4):
    suma += i
print("Total:", suma)       # se imprime 1 vez: 6
```

**Consejo para estudiar**: ante cualquier duda, hacé una **prueba de escritorio** (tabla con las variables y su valor en cada vuelta, como en la sección 2). Es la herramienta más efectiva para entender qué hace un bucle y encontrar errores.

## 9. Ejercicios integradores

Estos ejercicios combinan todo lo visto: `while`, `for`, `range`, recorridos, `break`/`continue`, bucles anidados y patrones.

**Ejercicio 9.1 (intermedio). Cajero de supermercado.** Pedir precios de productos hasta que se ingrese 0. Mostrar la cantidad de productos, el total y el producto más caro. Si el total supera $10.000, aplicar un 10% de descuento.

```python
# Solución
cantidad = 0
total = 0
mas_caro = 0

precio = float(input("Precio (0 para terminar): "))
while precio != 0:
    if precio < 0:
        print("Precio inválido, se ignora.")
    else:
        cantidad += 1
        total += precio
        if precio > mas_caro:
            mas_caro = precio
    precio = float(input("Precio (0 para terminar): "))

if total > 10000:
    total = total * 0.9
    print("Se aplicó 10% de descuento")

print("Productos:", cantidad)
print("Más caro:", mas_caro)
print("Total a pagar:", round(total, 2))
```

**Ejercicio 9.2 (intermedio). Menú de calculadora.** Mostrar un menú repetidamente: 1) Sumar, 2) Restar, 3) Multiplicar, 4) Salir. Para las opciones 1 a 3, pedir dos números y mostrar el resultado.

```python
# Solución
while True:
    print("\n1) Sumar  2) Restar  3) Multiplicar  4) Salir")
    opcion = input("Opción: ")

    if opcion == "4":
        print("¡Hasta luego!")
        break
    if opcion not in ("1", "2", "3"):
        print("Opción inválida")
        continue

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    if opcion == "1":
        print("Resultado:", a + b)
    elif opcion == "2":
        print("Resultado:", a - b)
    else:
        print("Resultado:", a * b)
```

**Ejercicio 9.3 (avanzado). Palíndromos.** Pedir una frase e indicar si es palíndromo (se lee igual al derecho y al revés), ignorando espacios y mayúsculas. Ejemplo: "Anita lava la tina". Resolverlo comparando letras con un bucle.

```python
# Solución
frase = input("Frase: ")

# 1) limpiar: solo letras, en minúscula
limpia = ""
for caracter in frase.lower():
    if caracter != " ":
        limpia += caracter

# 2) comparar extremos hacia el centro
es_palindromo = True
izquierda = 0
derecha = len(limpia) - 1
while izquierda < derecha:
    if limpia[izquierda] != limpia[derecha]:
        es_palindromo = False
        break
    izquierda += 1
    derecha -= 1

if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")
```

**Ejercicio 9.4 (avanzado). Estadísticas de un curso.** Pedir la cantidad de alumnos. Para cada alumno, pedir 3 notas (validando que estén entre 1 y 10) y mostrar su promedio. Al final, mostrar el promedio general del curso y cuántos alumnos promocionaron (promedio ≥ 8).

```python
# Solución
cantidad_alumnos = int(input("Cantidad de alumnos: "))
suma_promedios = 0
promocionados = 0

for alumno in range(1, cantidad_alumnos + 1):
    print(f"\nAlumno {alumno}")
    suma_notas = 0
    for parcial in range(1, 4):
        nota = int(input(f"  Nota {parcial}: "))
        while nota < 1 or nota > 10:
            nota = int(input("  Inválida (1 a 10): "))
        suma_notas += nota
    promedio = suma_notas / 3
    print(f"  Promedio: {promedio:.2f}")
    suma_promedios += promedio
    if promedio >= 8:
        promocionados += 1

if cantidad_alumnos > 0:
    print(f"\nPromedio del curso: {suma_promedios / cantidad_alumnos:.2f}")
    print("Promocionados:", promocionados)
```

Este ejercicio usa los tres niveles: un `for` externo (alumnos), un `for` interno (notas) y un `while` de validación dentro de él.

**Ejercicio 9.5 (desafío). Número perfecto.** Un número es perfecto si es igual a la suma de sus divisores propios (sin contarse a sí mismo). Por ejemplo, 6 = 1 + 2 + 3. Mostrar todos los números perfectos entre 1 y 10.000.

```python
# Solución
for numero in range(2, 10001):
    suma_divisores = 0
    for divisor in range(1, numero // 2 + 1):
        if numero % divisor == 0:
            suma_divisores += divisor
    if suma_divisores == numero:
        print(numero, "es perfecto")
# Resultado: 6, 28, 496, 8128
```

Para discutir en clase: este programa tarda varios segundos. ¿Por qué? ¿Cuántas vueltas da en total el bucle interno? ¿Cómo se podría reducir?

## 10. Trabajo práctico: calculadora con `for` y funciones

### Enunciado

Construir una calculadora de consola que realice las cuatro operaciones básicas: **suma, resta, multiplicación y división**. El programa debe organizarse en **funciones** y usar **bucles `for`** para repetir operaciones y para mostrar información.

**Funcionamiento esperado**

1. Al iniciar, el programa pregunta cuántas operaciones quiere realizar el usuario.
2. Con un `for`, repite esa cantidad de veces:
   1. Muestra el menú de operaciones, numerado del 1 al 4. El menú se arma **recorriendo una lista** con un `for`, no con cuatro `print` sueltos.
   2. Pide la opción y la valida: si no está entre 1 y 4, la vuelve a pedir.
   3. Pide dos números (pueden tener decimales).
   4. Calcula el resultado llamando a la función de la operación elegida y lo muestra.
   5. Guarda la operación realizada en una lista llamada `historial`.
3. Si se intenta dividir por cero, se muestra un mensaje de error, esa operación **no se guarda** en el historial y el programa sigue con la próxima.
4. Al terminar, muestra el historial completo recorriéndolo con un `for`. Si no hubo operaciones válidas, lo informa.

**Requisitos obligatorios**

- Una función por operación: `sumar(a, b)`, `restar(a, b)`, `multiplicar(a, b)` y `dividir(a, b)`. Cada una **devuelve** el resultado con `return`; ninguna usa `print`.
- `dividir(a, b)` devuelve `None` cuando `b` es 0.
- Funciones auxiliares: `mostrar_menu()`, `pedir_opcion()`, `pedir_numero(mensaje)`, `calcular(opcion, a, b)` y `mostrar_historial(historial)`.
- Una función `main()` que coordine todo el programa.
- Al menos tres bucles `for`: uno para las operaciones, uno para el menú y uno para el historial.

**Conceptos que se evalúan**: definición y llamada de funciones, parámetros y `return`, `for` con `range()`, recorrido de listas con `enumerate()`, validación con `while`, uso de `continue` y listas con `append()`.

**Ejemplo de ejecución**

```text
¿Cuántas operaciones querés hacer? 2

Operación 1 de 2

--- Calculadora ---
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
Elegí una operación (1-4): 3
Primer número: 4
Segundo número: 2.5
Resultado: 4.0 x 2.5 = 10.0

Operación 2 de 2

--- Calculadora ---
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
Elegí una operación (1-4): 4
Primer número: 7
Segundo número: 0
Error: no se puede dividir por cero.

--- Historial ---
1. 4.0 x 2.5 = 10.0
```

### Scaffolding (código base para el alumno)

Completá cada `# TODO`. Las firmas de las funciones y sus descripciones ya están armadas: no cambies los nombres ni los parámetros. Para probar funciones sueltas sin ejecutar todo el programa, podés comentar la última línea `main()` y llamar, por ejemplo, `print(sumar(2, 3))`.

```python
# calculadora.py

OPCIONES = ["Sumar", "Restar", "Multiplicar", "Dividir"]


def mostrar_menu():
    """Muestra las opciones numeradas recorriendo la lista OPCIONES."""
    print("\n--- Calculadora ---")
    # TODO: recorrer OPCIONES con un for y enumerate(..., start=1)
    #       para mostrar "1) Sumar", "2) Restar", etc.


def pedir_opcion():
    """Pide una opción válida (1 a 4) y la devuelve como entero."""
    opcion = int(input("Elegí una operación (1-4): "))
    # TODO: mientras la opción esté fuera del rango 1..4, volver a pedirla
    return opcion


def pedir_numero(mensaje):
    """Pide un número al usuario y lo devuelve como float."""
    # TODO: usar input(mensaje) y convertir a float
    pass


def sumar(a, b):
    # TODO: devolver la suma
    pass


def restar(a, b):
    # TODO: devolver la resta
    pass


def multiplicar(a, b):
    # TODO: devolver el producto
    pass


def dividir(a, b):
    """Devuelve a / b, o None si b es 0."""
    # TODO: si b es 0, devolver None; si no, devolver la división
    pass


def calcular(opcion, a, b):
    """Llama a la función que corresponde a la opción elegida."""
    # TODO: según la opción (1, 2, 3 o 4), llamar a la función
    #       correspondiente y devolver su resultado
    pass


def mostrar_historial(historial):
    """Recorre el historial y muestra cada operación realizada."""
    print("\n--- Historial ---")
    # TODO: si el historial está vacío, informarlo y terminar con return
    # TODO: recorrer el historial con un for y mostrar "1. ...", "2. ..."


def main():
    simbolos = ["+", "-", "x", "/"]
    historial = []

    cantidad = int(input("¿Cuántas operaciones querés hacer? "))
    # TODO: con un for, repetir 'cantidad' veces:
    #   1. mostrar "Operación N de cantidad"
    #   2. mostrar el menú y pedir la opción
    #   3. pedir los dos números
    #   4. calcular el resultado
    #   5. si el resultado es None: mostrar el error y pasar a la
    #      siguiente vuelta (continue)
    #   6. armar el texto, por ejemplo "8.0 + 2.0 = 10.0",
    #      usando simbolos[opcion - 1]
    #   7. mostrarlo y agregarlo al historial

    # TODO: mostrar el historial


main()
```

**Pistas**

- En `calcular`, si las opciones 1 a 3 ya tienen su `if`/`elif`, la opción 4 puede ir en el `else`, porque `pedir_opcion` ya garantizó que la opción es válida.
- Para comparar con `None` se usa `is`: `if resultado is None:`.
- Las listas `OPCIONES` y `simbolos` están en el mismo orden: el índice de una sirve para la otra (`opcion - 1`).

### Implementación completa (solución docente)

Esta solución fue ejecutada y probada con los casos de la tabla de abajo.

```python
# calculadora.py

OPCIONES = ["Sumar", "Restar", "Multiplicar", "Dividir"]


def mostrar_menu():
    """Muestra las opciones numeradas recorriendo la lista OPCIONES."""
    print("\n--- Calculadora ---")
    for numero, opcion in enumerate(OPCIONES, start=1):
        print(f"{numero}) {opcion}")


def pedir_opcion():
    """Pide una opción válida (1 a 4) y la devuelve como entero."""
    opcion = int(input("Elegí una operación (1-4): "))
    while opcion < 1 or opcion > len(OPCIONES):
        opcion = int(input("Opción inválida. Elegí entre 1 y 4: "))
    return opcion


def pedir_numero(mensaje):
    """Pide un número al usuario y lo devuelve como float."""
    return float(input(mensaje))


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    """Devuelve a / b, o None si b es 0."""
    if b == 0:
        return None
    return a / b


def calcular(opcion, a, b):
    """Llama a la función que corresponde a la opción elegida."""
    if opcion == 1:
        return sumar(a, b)
    elif opcion == 2:
        return restar(a, b)
    elif opcion == 3:
        return multiplicar(a, b)
    else:
        return dividir(a, b)


def mostrar_historial(historial):
    """Recorre el historial y muestra cada operación realizada."""
    print("\n--- Historial ---")
    if len(historial) == 0:
        print("No se realizaron operaciones válidas.")
        return
    for numero, linea in enumerate(historial, start=1):
        print(f"{numero}. {linea}")


def main():
    simbolos = ["+", "-", "x", "/"]
    historial = []

    cantidad = int(input("¿Cuántas operaciones querés hacer? "))
    for numero_operacion in range(1, cantidad + 1):
        print(f"\nOperación {numero_operacion} de {cantidad}")
        mostrar_menu()
        opcion = pedir_opcion()
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")

        resultado = calcular(opcion, a, b)
        if resultado is None:
            print("Error: no se puede dividir por cero.")
            continue

        linea = f"{a} {simbolos[opcion - 1]} {b} = {resultado}"
        print("Resultado:", linea)
        historial.append(linea)

    mostrar_historial(historial)


main()
```

### Cómo está organizada la solución

| Función | Responsabilidad | Bucle que usa |
| --- | --- | --- |
| `sumar`, `restar`, `multiplicar`, `dividir` | Hacer un único cálculo y devolverlo | Ninguno |
| `calcular` | Elegir qué operación ejecutar según la opción | Ninguno |
| `mostrar_menu` | Mostrar las opciones | `for` sobre `OPCIONES` |
| `pedir_opcion` | Pedir y validar la opción | `while` de validación |
| `pedir_numero` | Pedir un número | Ninguno |
| `mostrar_historial` | Mostrar las operaciones guardadas | `for` sobre `historial` |
| `main` | Coordinar todo el programa | `for` con `range()` |

Cada función hace **una sola cosa**. Las funciones de cálculo no imprimen nada: devuelven el valor y quien las llama decide qué hacer con él. Eso permite reutilizarlas y probarlas por separado. Además, si mañana se agrega una opción "Potencia", alcanza con sumarla a `OPCIONES` y `simbolos`, crear `potencia(a, b)` y agregar un caso en `calcular`: el menú se actualiza solo porque se arma con un `for`.

### Casos de prueba

| # | Opción | Primer número | Segundo número | Salida esperada | ¿Va al historial? |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 (Sumar) | 8 | 2 | `8.0 + 2.0 = 10.0` | Sí |
| 2 | 2 (Restar) | 10 | 15 | `10.0 - 15.0 = -5.0` | Sí |
| 3 | 3 (Multiplicar) | 4 | 2.5 | `4.0 x 2.5 = 10.0` | Sí |
| 4 | 9, luego 4 (Dividir) | 7 | 0 | `Opción inválida...` y luego `Error: no se puede dividir por cero.` | No |
| 5 | 4 (Dividir) | 9 | 2 | `9.0 / 2.0 = 4.5` | Sí |

Con esos 5 casos en una misma ejecución, el historial final muestra 4 líneas (todas menos la división por cero).

### Criterios de corrección sugeridos

| Criterio | Puntos |
| --- | --- |
| Las 4 funciones de operación devuelven el resultado correcto con `return` | 3 |
| `dividir` contempla la división por cero sin romper el programa | 1 |
| Menú armado con `for` sobre la lista | 1 |
| Validación de la opción con `while` | 1 |
| `for` con `range()` para la cantidad de operaciones | 2 |
| Historial guardado con `append` y mostrado con `for` | 1 |
| Nombres claros, indentación y organización en funciones | 1 |
| **Total** | **10** |

### Extensiones opcionales (para quienes terminan antes)

1. **Multiplicar con sumas sucesivas**: reescribir `multiplicar(a, b)` para enteros usando un `for` que sume `a` tantas veces como indique `b`. Probar qué pasa con `b` negativo.
2. **Potencia**: agregar la opción 5 "Potencia", calculada con un `for` (sin usar `**`).
3. **Resumen final**: además del historial, mostrar cuántas operaciones de cada tipo se hicieron, usando contadores.
4. **Datos inválidos**: si el usuario escribe letras en lugar de números, hoy el programa se corta. Investigar `try`/`except ValueError` para manejarlo.

Solución de la extensión 1:

```python
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
```
