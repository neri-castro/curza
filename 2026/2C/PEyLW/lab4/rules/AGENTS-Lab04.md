# Reglas de Corrección — Laboratorio 4: CSS, Fuentes Web y Posicionamiento

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 4. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

Fechas oficiales: apertura lunes 21/09/2026 00:00 — cierre sábado 10/10/2026
23:00. Entregas posteriores al cierre: marcar como tardías según criterio
general del curso (este documento no define penalización por atraso).

## Formato de entrega — distinto a Labs 1-3

Este TP usa **formato avanzado**: el enunciado pide colocar la URL de la
página en GitHub (GitHub Pages) una vez finalizada, ya desplegada. A
diferencia de Labs 1-3:

- **No** se exige carátula README.md con tabla de datos del alumno (los
  campos de "Información del Alumno" del enunciado son del encabezado del
  documento de entrega, no un archivo a versionar en el repositorio).
- **Sí** se exige `REFLEXION.md` (sección 5 del enunciado, "Reflexión
  Aplicada — Prevención de Copias") con las 3 preguntas respondidas: (1)
  fragmento de CSS de la animación de rotación del logo, (2) por qué hace
  falta `background-color` en el elemento `sticky`, (3) qué cambio visual
  ocurre en pantallas menores a 768px por las `@media` implementadas. Ver
  ítem de rúbrica dedicado más abajo.
- **No** hay un mensaje de commit exacto a verificar.
- **Sí** se exige el comentario en la cabecera de `styles.css` con los
  códigos HSL elegidos y el identificador de alumno (punto 3.1,
  "Personalización por Alumno"). Ver ítem de rúbrica dedicado más abajo.

Si la entrega llega como PDF/DOCX con un enlace (en vez de URL directa),
extraer el enlace igual que en labs anteriores (ver `context-Lab04.md`).

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

El requisito de **responsive design** (meta viewport, flexbox/grid, media
query de 768px) aplica a **todas** las páginas: la meta viewport se pide
en el `<head>` de cada HTML, y la navegación que debe apilarse en mobile es
común a las tres páginas. El requisito de **personalización** (paleta HSL
+ comentario de identificación) es un único bloque en la cabecera de
`styles.css`, por lo que se revisa una sola vez.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 4

| Ítem | Puntos |
|---|---|
| Personalización por alumno — paleta HSL + comentario (ver detalle) | 5 |
| Formato de tabla en `contacto.html` (ver detalle) | 12 |
| Formato de formulario en `contacto.html` (ver detalle) | 12 |
| Fuente web (ver detalle) | 8 |
| Animación de título + logo CURZA (ver detalle) | 12 |
| Header fijo en todas las páginas (ver detalle) | 12 |
| "Acerca de" — texto sticky + alto máximo con scroll (ver detalle) | 12 |
| Botón "volver arriba" en cada página (ver detalle) | 12 |
| Responsive Web Design (ver detalle) | 10 |
| `REFLEXION.md` — prevención de copias (ver detalle) | 5 |
| **TOTAL** | **100** |

#### Detalle Personalización por alumno (5 pts)

| Sub-ítem | Puntos |
|---|---|
| Color primario definido en HSL, coherente, sin colores puros sin modular (ej. `#ff0000`, `#0000ff`, `hsl(0,100%,50%)`) | 2 |
| Comentario en la cabecera de `styles.css` con los códigos HSL elegidos y el identificador de alumno | 3 |

Si no hay comentario alguno en la cabecera del CSS, o el color primario
usado es un color puro sin modular: ❌ en el sub-ítem correspondiente.

#### Detalle Tabla (12 pts)

| Sub-ítem | Puntos |
|---|---|
| Bordes/celdas visibles y alineados correctamente | 4 |
| Espaciado (padding/margin) consistente y legible | 4 |
| Encabezados de tabla diferenciados visualmente (color de fondo, negrita, u otro contraste) | 4 |

#### Detalle Formulario (12 pts)

| Sub-ítem | Puntos |
|---|---|
| Campos de entrada con tamaño y padding consistentes | 4 |
| `<label>` correctamente alineados con su campo correspondiente | 4 |
| Grupos de radios/checkboxes legibles, sin superposición ni desalineación | 4 |

Si la tabla o el formulario no tienen ningún estilo CSS aplicado más allá
del default del navegador: ❌ en el sub-ítem correspondiente, no ⚠️.

#### Detalle Fuente web (8 pts)

| Sub-ítem | Puntos |
|---|---|
| Fuente web importada correctamente (`@font-face`, Google Fonts u otro servicio, vía `<link>` o `@import`) | 3 |
| Aplicada de forma visible en al menos un elemento del sitio (no solo declarada sin uso real) | 3 |
| `font-family` con fallback razonable definido (ej. `"Nombre Fuente", sans-serif`) | 2 |

Si la fuente está importada pero el `font-family` nunca se aplica a ningún
selector real usado en el HTML: ❌ en el sub-ítem de "aplicada visible".

#### Detalle Animación de título + logo CURZA (12 pts)

| Sub-ítem | Puntos |
|---|---|
| Logo del CURZA visible a la derecha del título principal en el encabezado | 4 |
| Animación CSS de giro completo (360°) sobre el eje vertical (`rotateY`) implementada (`@keyframes` + `animation`, o `transition` disparada) | 4 |
| La animación termina en orientación correcta y legible (no queda invertida, espejada o detenida a mitad de giro) | 4 |

Un giro que termina en 180° (mostrando el logo "al revés"/espejado) o que no
completa la vuelta: ⚠️ parcial en el tercer sub-ítem, no pleno.

#### Detalle Header fijo (12 pts)

| Sub-ítem | Puntos |
|---|---|
| El encabezado permanece visible arriba al hacer scroll, en **cada una** de las páginas del portal (`position: fixed` o `sticky` con `top: 0`) | 8 |
| El contenido del `<main>` no queda tapado detrás del header fijo (compensación con `padding-top`/`margin-top` u otro método) | 4 |

Si el header es fijo en algunas páginas pero no en todas: descontar
proporcionalmente el sub-ítem de 8 pts según la fracción de páginas que
cumplen.

#### Detalle "Acerca de" — sticky + scroll (12 pts)

| Sub-ítem | Puntos |
|---|---|
| La primera línea del texto (o el `<h2>` "Biografía") queda fija (`position: sticky`) mientras se hace scroll dentro del artículo | 6 |
| El `<article>` (o contenedor del texto) tiene `max-height: 300px` | 3 |
| Aparece una barra de desplazamiento visible/funcional cuando el contenido excede los 300px (`overflow-y: auto` o `scroll`) | 3 |

Si el `max-height` está pero sin `overflow` (el contenido se corta sin
poder verse completo, sin scrollbar): ⚠️ parcial en el tercer sub-ítem.

#### Detalle Botón "volver arriba" (12 pts)

| Sub-ítem | Puntos |
|---|---|
| Presente en cada una de las páginas del portal | 4 |
| Estilo correcto: flecha apuntando hacia arriba dentro de un círculo, ubicado al final de la página y alineado a la derecha | 4 |
| Funcional: al hacer clic vuelve al inicio de la página (ancla `#`, JS `scrollTo`, `scroll-behavior: smooth`, etc.) | 4 |

Si el botón existe visualmente pero no vuelve al inicio al hacer clic: ❌ en
el sub-ítem de funcionalidad.

#### Detalle Responsive Web Design (10 pts)

| Sub-ítem | Puntos |
|---|---|
| Meta etiqueta `<meta name="viewport" content="width=device-width, initial-scale=1.0">` presente en las tres páginas | 2 |
| Flexbox o CSS Grid usado en la barra de navegación y/o en la maquetación del formulario/tabla | 3 |
| Regla `@media (max-width: 768px)` que apila verticalmente los enlaces de navegación | 3 |
| La tabla no rompe el ancho del dispositivo en mobile (scroll lateral controlado o reflujo adaptado) | 2 |

Si no hay ninguna regla `@media`: ❌ en la totalidad del ítem, no solo en el
sub-ítem de navegación.

#### Detalle `REFLEXION.md` — prevención de copias (5 pts)

| Sub-ítem | Puntos |
|---|---|
| Archivo presente con las 3 preguntas respondidas (fragmento de animación, por qué `background-color` en sticky, cambio visual en mobile) | 3 |
| El fragmento de CSS citado en la respuesta 1 corresponde realmente al código usado en el proyecto (no genérico/copiado de otra fuente) | 2 |

Si falta el archivo por completo: ❌ en el ítem completo. Si está incompleto
(responde menos de 3 preguntas): ⚠️ parcial, descontar proporcionalmente.

## Verificación en internet

- Acceder a la URL de GitHub Pages entregada y confirmar que responde 200.
- Verificar en el sitio desplegado (no solo en local) que:
  - El header queda fijo al hacer scroll en cada página.
  - El botón "volver arriba" funciona realmente al hacer clic.
  - La animación del logo se ejecuta al cargar la página (o al evento que
    el alumno haya definido).
  - El scroll dentro de "Acerca de" funciona y la primera línea queda fija.
  - Al angostar el viewport a menos de 768px (o emular un mobile), el menú
    de navegación se apila verticalmente y la tabla de `contacto.html` no
    rompe el ancho de la pantalla.
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
