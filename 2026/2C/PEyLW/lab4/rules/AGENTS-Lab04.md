# Reglas de Corrección — Laboratorio 4: CSS, Fuentes Web y Posicionamiento

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 4. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

Fechas oficiales: apertura lunes 21/09/2026 00:00 — cierre viernes 23/10/2026
23:00. Entregas posteriores al cierre: marcar como tardías según criterio
general del curso (este documento no define penalización por atraso).

## Formato de entrega — distinto a Labs 1-3

Este TP usa **formato avanzado**: el enunciado solo pide colocar la URL de
la página en GitHub (GitHub Pages) una vez finalizada, ya desplegada. A
diferencia de Labs 1-3:

- **No** se exige carátula README.md con tabla de datos del alumno.
- **No** se exige `REFLEXION.md`.
- **No** hay un mensaje de commit exacto a verificar.
- **No** se exige comentario de token único adicional.

Si el alumno igual entrega un README/REFLEXION heredado de labs anteriores,
no se penaliza ni se exige actualizarlo; simplemente no forma parte de la
rúbrica de este TP. Si la entrega llega como PDF/DOCX con un enlace (en vez
de URL directa), extraer el enlace igual que en labs anteriores (ver
`context-Lab04.md`).

## Tono y estilo de la corrección

- Sin adulación. Sin emojis de aprobación ni frases de relleno motivacional.
- Señalar errores y omisiones citando el archivo y la tarea del enunciado.
- No inflar la nota por esfuerzo percibido. Si falta algo, se descuenta.
- Lo que está bien: una línea. El foco es lo que falta o está mal.

## Alcance de los requisitos

El enunciado dice "Modificar las páginas creadas hasta el momento": los
requisitos de **header fijo** y **botón volver arriba** aplican a **todas**
las páginas del portal (`index.html`, `acercade.html`, `contacto.html`, y
cualquier otra página que el alumno haya agregado). Los requisitos de
**tabla** y **formulario** formateados aplican específicamente a
`contacto.html` (única página con tabla y formulario). La **fuente web** y
la **animación de título + logo** deben verse al menos en el encabezado,
que es común a todas las páginas.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 4

| Ítem | Puntos |
|---|---|
| Formato de tabla en `contacto.html` (ver detalle) | 15 |
| Formato de formulario en `contacto.html` (ver detalle) | 15 |
| Fuente web (ver detalle) | 10 |
| Animación de título + logo CURZA (ver detalle) | 15 |
| Header fijo en todas las páginas (ver detalle) | 15 |
| "Acerca de" — texto sticky + alto máximo con scroll (ver detalle) | 15 |
| Botón "volver arriba" en cada página (ver detalle) | 15 |
| **TOTAL** | **100** |

#### Detalle Tabla (15 pts)

| Sub-ítem | Puntos |
|---|---|
| Bordes/celdas visibles y alineados correctamente | 5 |
| Espaciado (padding/margin) consistente y legible | 5 |
| Encabezados de tabla diferenciados visualmente (color de fondo, negrita, u otro contraste) | 5 |

#### Detalle Formulario (15 pts)

| Sub-ítem | Puntos |
|---|---|
| Campos de entrada con tamaño y padding consistentes | 5 |
| `<label>` correctamente alineados con su campo correspondiente | 5 |
| Grupos de radios/checkboxes legibles, sin superposición ni desalineación | 5 |

Si la tabla o el formulario no tienen ningún estilo CSS aplicado más allá
del default del navegador: ❌ en el sub-ítem correspondiente, no ⚠️.

#### Detalle Fuente web (10 pts)

| Sub-ítem | Puntos |
|---|---|
| Fuente web importada correctamente (`@font-face`, Google Fonts u otro servicio, vía `<link>` o `@import`) | 4 |
| Aplicada de forma visible en al menos un elemento del sitio (no solo declarada sin uso real) | 3 |
| `font-family` con fallback razonable definido (ej. `"Nombre Fuente", sans-serif`) | 3 |

Si la fuente está importada pero el `font-family` nunca se aplica a ningún
selector real usado en el HTML: ❌ en el sub-ítem de "aplicada visible".

#### Detalle Animación de título + logo CURZA (15 pts)

| Sub-ítem | Puntos |
|---|---|
| Logo del CURZA visible a la derecha del título principal en el encabezado | 5 |
| Animación CSS de giro completo (360°) sobre el eje vertical (`rotateY`) implementada (`@keyframes` + `animation`, o `transition` disparada) | 5 |
| La animación termina en orientación correcta y legible (no queda invertida, espejada o detenida a mitad de giro) | 5 |

Un giro que termina en 180° (mostrando el logo "al revés"/espejado) o que no
completa la vuelta: ⚠️ parcial en el tercer sub-ítem, no pleno.

#### Detalle Header fijo (15 pts)

| Sub-ítem | Puntos |
|---|---|
| El encabezado permanece visible arriba al hacer scroll, en **cada una** de las páginas del portal (`position: fixed` o `sticky` con `top: 0`) | 10 |
| El contenido del `<main>` no queda tapado detrás del header fijo (compensación con `padding-top`/`margin-top` u otro método) | 5 |

Si el header es fijo en algunas páginas pero no en todas: descontar
proporcionalmente el sub-ítem de 10 pts según la fracción de páginas que
cumplen.

#### Detalle "Acerca de" — sticky + scroll (15 pts)

| Sub-ítem | Puntos |
|---|---|
| La primera línea del texto queda fija (`position: sticky`) mientras se hace scroll dentro del artículo | 7 |
| El `<article>` (o contenedor del texto) tiene `max-height: 300px` | 4 |
| Aparece una barra de desplazamiento visible/funcional cuando el contenido excede los 300px (`overflow-y: auto` o `scroll`) | 4 |

Si el `max-height` está pero sin `overflow` (el contenido se corta sin
poder verse completo, sin scrollbar): ⚠️ parcial en el tercer sub-ítem.

#### Detalle Botón "volver arriba" (15 pts)

| Sub-ítem | Puntos |
|---|---|
| Presente en cada una de las páginas del portal | 5 |
| Estilo correcto: flecha apuntando hacia arriba dentro de un círculo, ubicado al final de la página y alineado a la derecha | 5 |
| Funcional: al hacer clic vuelve al inicio de la página (ancla `#`, JS `scrollTo`, `scroll-behavior: smooth`, etc.) | 5 |

Si el botón existe visualmente pero no vuelve al inicio al hacer clic: ❌ en
el sub-ítem de funcionalidad.

## Verificación en internet

- Acceder a la URL de GitHub Pages entregada y confirmar que responde 200.
- Verificar en el sitio desplegado (no solo en local) que:
  - El header queda fijo al hacer scroll en cada página.
  - El botón "volver arriba" funciona realmente al hacer clic.
  - La animación del logo se ejecuta al cargar la página (o al evento que
    el alumno haya definido).
  - El scroll dentro de "Acerca de" funciona y la primera línea queda fija.
- Si Pages devuelve 404 o alguno de los efectos no se puede reproducir en
  el sitio desplegado (aunque el código lo sugiera): registrar como
  incumplimiento del ítem correspondiente, no asumir que "andará".

## Clonado y revisión local

- Clonar (o reutilizar el clon de labs anteriores) en
  `lab4/repos-clonados/<token-del-alumno>/` y hacer `git pull` si ya existía.
- Revisar `styles.css` (y cualquier CSS adicional) y los tres archivos HTML
  del portal sobre el clon local.
- No modificar ni commitear nada en el clon.
- No hay mensaje de commit exacto que verificar en este TP; alcanza con
  confirmar que los cambios de CSS/HTML están presentes en el repo.

## Archivo de devolución por alumno

- Guardar en `lab4/devoluciones/<token-del-alumno>.md`.
- Al terminar todas las entregas del lab, generar el consolidado
  `lab4/devoluciones/Lab04-devoluciones-completas.md` con tabla resumen al
  inicio y la devolución completa de cada alumno a continuación.

## Formato del informe de corrección

Por cada alumno entregar:

1. **Datos identificatorios**: nombre (si se conoce por labs anteriores),
   token, enlace a GitHub Pages.
2. **Checklist por ítem** con estado: ✅ cumple / ❌ no cumple / ⚠️ parcial
   y motivo concreto.
3. **Observaciones puntuales**: errores específicos con archivo y sección afectada.
4. **Nota final (0–100)** con desglose ítem por ítem que la justifica.
