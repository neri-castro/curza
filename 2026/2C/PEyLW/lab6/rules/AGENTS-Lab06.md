# Reglas de Corrección — Laboratorio 6: Juego con JavaScript

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 6. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

Fechas oficiales: apertura lunes 21/09/2026 00:00 — cierre sábado 21/11/2026
23:00. Entregas posteriores al cierre: marcar como tardías según criterio
general del curso (este documento no define penalización por atraso).

## Formato de entrega — igual a Labs 4 y 5

Este TP usa **formato avanzado**: el enunciado solo pide colocar la URL de
la página en GitHub (GitHub Pages) una vez finalizada, ya desplegada.

- **No** se exige carátula README.md con tabla de datos del alumno.
- **No** se exige `REFLEXION.md`.
- **No** hay un mensaje de commit exacto a verificar.
- **No** se exige comentario de token único adicional.

Si el alumno igual entrega un README/REFLEXION heredado de labs anteriores,
no se penaliza ni se exige actualizarlo. Si la entrega llega como PDF/DOCX
con un enlace (en vez de URL directa), extraer el enlace igual que en labs
anteriores (ver `context-Lab06.md`).

## Uso de IA explícitamente permitido

El enunciado autoriza expresamente usar IA para el desarrollo completo del
juego. **No penalizar** por indicios de código generado por IA (comentarios
genéricos, estilo de nombres, estructura "de manual"), ni exigir
originalidad o que el alumno explique el código línea por línea. La
corrección evalúa exclusivamente que el juego funcione y esté bien
integrado, no el origen del código.

## Tono y estilo de la corrección

- Sin adulación. Sin emojis de aprobación ni frases de relleno motivacional.
- Señalar errores y omisiones citando el archivo y la tarea del enunciado.
- No inflar la nota por esfuerzo percibido. Si falta algo, se descuenta.
- Lo que está bien: una línea. El foco es lo que falta o está mal.

## Continuidad con Labs 1-5

Este TP pide explícitamente "completar y refinar la página personal con
todos los elementos anteriores". Antes de evaluar el juego en sí, hacer una
verificación abreviada de continuidad (no se re-aplica la rúbrica completa
de cada lab anterior, alcanza con confirmar que cada elemento sigue
presente y funcionando):

- Lab 2: `index.html`/`acercade.html` con estructura semántica completa.
- Lab 3: `contacto.html` con formulario y tabla de resumen.
- Lab 4: header fijo en todas las páginas, fuente web, animación de
  logo+título, sticky en "Acerca de", botón volver arriba.
- Lab 5: `script.js` reflejando el formulario en la tabla en tiempo real,
  botón "Leer más" en "Acerca de".

Si algo de lo anterior dejó de funcionar o desapareció al integrar el
juego, registrar como incumplimiento del ítem "Página personal completa y
refinada" de este TP — no como regresión de un lab pasado.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 6

| Ítem | Puntos |
|---|---|
| Página personal completa y refinada (continuidad Labs 1-5) | 20 |
| Subpágina o sección del juego — presencia e integración visual (ver detalle) | 15 |
| Enlace de navegación al juego en todas las páginas del portal | 10 |
| Juego — reglas correctas y completas según el tipo elegido (ver detalle) | 20 |
| Juego — interactividad y manejo de estado en JavaScript | 15 |
| Juego — feedback claro al usuario (resultado de cada acción/ronda) | 10 |
| Juego — reinicio / jugar de nuevo sin recargar la página | 10 |
| **TOTAL** | **100** |

#### Detalle Subpágina/sección del juego (15 pts)

| Sub-ítem | Puntos |
|---|---|
| Existe una subpágina dedicada (ej. `juego.html`) o una sección claramente delimitada dentro de una página existente | 8 |
| Diseño visual consistente con el resto del portal (usa `styles.css`, mismo `<header>`/`<footer>`, misma fuente/paleta) | 7 |

#### Detalle Juego — reglas según el tipo elegido (20 pts)

El enunciado permite elegir **uno** de 4 juegos. Identificar cuál eligió el
alumno y verificar sus reglas mínimas específicas:

**Adivinanza de Números:**
- Genera un número aleatorio en un rango definido (`Math.random`).
- El usuario puede ingresar intentos.
- El sistema da una pista tras cada intento (mayor/menor).
- Detecta el acierto y lo comunica.

**Preguntas y Respuestas (trivia):**
- Presenta varias preguntas (mínimo 3-5) sobre un tema definido.
- Verifica si la respuesta elegida es correcta o incorrecta.
- Muestra un puntaje o resultado final al terminar.

**Memoria con Cartas:**
- Grid de cartas ocultas (boca abajo).
- Al hacer clic se voltea una carta.
- Compara pares: si coinciden quedan reveladas, si no se vuelven a ocultar.
- Detecta cuando se completó el juego (todas las parejas encontradas).

**Piedra, Papel o Tijera:**
- El usuario elige una opción (botones u otro control).
- La computadora elige aleatoriamente.
- Determina el ganador según las reglas clásicas del juego.
- Muestra el resultado de cada ronda.

| Sub-ítem | Puntos |
|---|---|
| Reglas básicas del juego elegido implementadas correctamente (ver lista de arriba) | 12 |
| Casos borde manejados razonablemente (ej. empate en piedra/papel/tijera, número fuera de rango, todas las cartas ya emparejadas) | 8 |

Si el juego implementado no corresponde a ninguna de las 4 opciones del
enunciado: registrar como desvío del enunciado y evaluar igual la
interactividad/feedback/reinicio, pero descontar este sub-ítem a la mitad
como máximo.

## Verificación en internet

- Acceder a la URL de GitHub Pages entregada y confirmar que responde 200.
- Sobre el sitio ya desplegado (no alcanza con leer el código):
  - Navegar a la subpágina/sección del juego desde el `<nav>` del portal.
  - Jugar una partida completa del juego para confirmar que las reglas
    específicas del tipo elegido se cumplen (ver detalle arriba).
  - Provocar intencionalmente un caso borde (ej. ingresar un valor
    inválido, forzar un empate, completar el juego) para confirmar que no
    rompe la página ni deja al usuario sin poder continuar.
  - Confirmar que existe una forma de reiniciar/jugar de nuevo sin recargar
    manualmente la página (F5).
  - Abrir la consola del navegador para detectar errores de JavaScript
    durante la partida.
- Si Pages devuelve 404 o el juego no se puede reproducir en el sitio
  desplegado (aunque el código lo sugiera): registrar como incumplimiento
  del ítem correspondiente, no asumir que "andará".

## Clonado y revisión local

- Clonar (o reutilizar el clon de labs anteriores) en
  `lab6/repos-clonados/<token-del-alumno>/` y hacer `git pull` si ya existía.
- Revisar la subpágina/sección del juego y su JavaScript asociado sobre el
  clon local.
- No modificar ni commitear nada en el clon.
- No hay mensaje de commit exacto que verificar en este TP.

## Archivo de devolución por alumno

- Guardar en `lab6/devoluciones/<token-del-alumno>.md`.
- Al terminar todas las entregas del lab, generar el consolidado
  `lab6/devoluciones/Lab06-devoluciones-completas.md` con tabla resumen al
  inicio y la devolución completa de cada alumno a continuación.

## Formato del informe de corrección

Por cada alumno entregar:

1. **Datos identificatorios**: nombre (si se conoce por labs anteriores),
   token, enlace a GitHub Pages, y **qué juego eligió**.
2. **Checklist por ítem** con estado: ✅ cumple / ❌ no cumple / ⚠️ parcial
   y motivo concreto.
3. **Observaciones puntuales**: errores específicos con archivo y sección afectada.
4. **Nota final (0–100)** con desglose ítem por ítem que la justifica.
