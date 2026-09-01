# Reglas de Corrección — Laboratorio 2: Estructura y Semántica Web con HTML5

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 2. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

Fechas oficiales: apertura lunes 31/08/2026 00:00 — cierre lunes 07/09/2026
23:55. Entregas posteriores al cierre: marcar como tardías según criterio
general del curso (este documento no define penalización por atraso).

## Tono y estilo de la corrección

- Sin adulación. Sin emojis de aprobación ni frases de relleno motivacional.
- Señalar errores y omisiones citando el archivo y la tarea del enunciado.
- No inflar la nota por esfuerzo percibido. Si falta algo, se descuenta.
- Lo que está bien: una línea. El foco es lo que falta o está mal.

## Continuidad con el Lab 1

El repositorio de este laboratorio es, en la mayoría de los casos, el mismo
repo `peylw-2026-practicos-<token>` usado en el Lab 1, ahora extendido con
nuevos archivos. Puntos importantes:

- El `index.html` del Lab 1 se **reemplaza por completo** por la versión
  HTML5 semántica que pide este enunciado. El `<h1>` del Lab 1 (solo nombre)
  ya NO es válido: en Lab 2 el `<h1>` debe ser exactamente
  `Portal de [Nombre Completo] - [Token]` en ambas páginas.
- Si el alumno conservó la versión vieja del `index.html` (sin `<header>`,
  `<nav>`, `<main>`, `<footer>`, o con el `<h1>` viejo): incumplimiento de
  Tarea 1, no un tema de Lab 1.
- El `README.md` y el `REFLEXION.md` de este TP son documentos nuevos y
  distintos a los del Lab 1 (carátula y reflexión propias de TP2); no deben
  confundirse ni reutilizarse sin actualizar.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 2

| Ítem | Puntos |
|---|---|
| Carátula / README.md completo con todos los campos | 5 |
| Personalización (token en comentario + `<h1>` exacto en ambas páginas) (ver detalle) | 10 |
| **Tarea 1** — `index.html` semántico completo (ver detalle) | 25 |
| **Tarea 2** — `acercade.html` semántico completo (ver detalle) | 30 |
| **Tarea 3** — `styles.css` vinculado y commit exacto (ver detalle) | 10 |
| Estructura de archivos exacta (raíz del repo) | 5 |
| GitHub Pages desplegado y respondiendo 200 | 5 |
| **Reflexión** — `REFLEXION.md` con las 3 preguntas respondidas (ver detalle) | 10 |
| **TOTAL** | **100** |

#### Detalle Personalización (10 pts)

| Sub-ítem | Puntos |
|---|---|
| Comentario `<!-- TOKEN-ALUMNO: <token> -->` al inicio del `<body>` en **ambos** archivos | 5 |
| `<h1>` exactamente `Portal de [Nombre Completo] - [Token]` en **ambas** páginas | 5 |

Si el comentario o el `<h1>` está presente en un solo archivo de los dos:
⚠️ parcial (mitad del puntaje del sub-ítem).

#### Detalle Tarea 1 — `index.html` (25 pts)

| Sub-ítem | Puntos |
|---|---|
| Plantilla HTML5 válida con `<html lang="es">`, `charset utf-8` y `<title>` descriptivo en `<head>` | 5 |
| `<header>` con el `<h1>` personalizado | 5 |
| `<nav>` con `<ul>` y dos enlaces relativos: "Inicio" (`index.html`) y "Acerca de" (`acercade.html`) | 5 |
| `<main>` con `<section>` de bienvenida: `<h2>` "Bienvenidos a mi espacio" + al menos dos párrafos explicativos | 5 |
| `<footer>` con copyright (ej. © 2026 [Nombre]), dirección del nodo (CURZAS - UNCo, Viedma, Río Negro) y token en texto simple | 5 |

#### Detalle Tarea 2 — `acercade.html` (30 pts)

| Sub-ítem | Puntos |
|---|---|
| `<header>`, `<nav>` y `<footer>` idénticos (estructura y contenido) a los de `index.html` | 5 |
| `<article>` con biografía **real** (no lorem ipsum / texto de relleno) dividida en dos `<section>`, mínimo dos párrafos en total sobre su interés por la Tecnicatura en Desarrollo Web | 10 |
| `<figure>` + `<figcaption>` con imagen en `img/`, ruta relativa local, `<img>` con atributo `alt` personalizado (no genérico tipo "imagen" o "foto") | 10 |
| `<ul>` con lenguajes de programación o tecnologías de interés | 5 |

Si la biografía es texto de relleno genérico o copiado sin adaptar:
⚠️ parcial, máximo 5/10 en ese sub-ítem.

#### Detalle Tarea 3 — `styles.css` (10 pts)

| Sub-ítem | Puntos |
|---|---|
| `styles.css` en la raíz con la regla básica de `body` (font-family y background-color) | 3 |
| `<link>` a `styles.css` presente en el `<head>` de **ambas** páginas | 3 |
| Commit en el historial con el mensaje exacto `TP2: Estructuras HTML y vinculacion de estilos` | 4 |

Si el mensaje de commit difiere en tildes, mayúsculas o puntuación menor:
⚠️ parcial (3/4). Si el contenido no corresponde a este commit (no incluye
los archivos HTML/CSS del TP2): ❌.

#### Detalle Reflexión — `REFLEXION.md` (10 pts)

| Sub-ítem | Puntos |
|---|---|
| Pregunta 1: nombre exacto de la imagen en `img/` y valor del `alt` usado en `acercade.html`, y ambos coinciden con lo que realmente está en el repo | 3 |
| Pregunta 2: justificación de por qué usar `<main>`/`<nav>` en vez de `<div>` genéricos (accesibilidad, SEO, semántica) | 4 |
| Pregunta 3: explica cómo verificó las rutas de navegación tanto en local como en GitHub Pages | 3 |

Respuesta de una línea sin justificación real, o copiada textual de internet
sin adaptación: ⚠️ parcial en esa pregunta.

## Verificación en internet

- Acceder al repositorio de GitHub del alumno para confirmar que es público
  y que contiene los archivos nuevos del TP2.
- Acceder a la URL de GitHub Pages para confirmar que responde 200 y que
  navegando desde "Inicio" a "Acerca de" (y viceversa) los enlaces
  funcionan realmente en el sitio desplegado, no solo en local.
  URL esperada: `https://<usuario>.github.io/peylw-2026-practicos-<token>/`
- Si Pages devuelve 404, o los enlaces de navegación rompen en producción:
  incumplimiento del ítem correspondiente.

## Clonado y revisión local

- Clonar (o reutilizar el clon del Lab 1) en
  `lab2/repos-clonados/<token-del-alumno>/` y hacer `git pull` si ya existía.
- Revisar estructura real con `find . -not -path "./.git*"`.
- Verificar historial con `git log --oneline --all --stat`:
  - Debe existir un commit con el mensaje exacto
    `TP2: Estructuras HTML y vinculacion de estilos` que incluya los
    archivos del TP2 (`index.html`, `acercade.html`, `styles.css`, y la
    imagen en `img/`).
  - Si hay commits adicionales, no penalizar por su existencia.
- Leer `index.html`, `acercade.html`, `styles.css`, `README.md` y
  `REFLEXION.md` sobre el clon local.
- No modificar ni commitear nada en el clon.
- Diferencias de casing en nombres de archivo no se penalizan.

## Verificaciones específicas de `index.html` y `acercade.html`

- Ambos archivos deben tener el comentario de token al inicio del `<body>`
  y el `<h1>` exacto (ver Detalle Personalización).
- Confirmar el uso real de etiquetas semánticas pedidas (`<header>`, `<nav>`,
  `<main>`, `<section>`, `<article>`, `<footer>`; `<aside>` no es
  obligatorio salvo que el alumno lo use). El uso de `<div>` genéricos en
  lugar de las etiquetas semánticas pedidas se penaliza en el sub-ítem
  correspondiente.
- Verificar que los enlaces del `<nav>` sean relativos (`index.html`,
  `acercade.html`), no absolutos ni rotos.
- El archivo no puede estar vacío ni ser un placeholder sin contenido real.

## Verificación de la imagen

- Confirmar que existe una imagen dentro de `img/` (no en la raíz ni en
  otra carpeta) y que `acercade.html` la referencia con ruta relativa local
  (ej. `img/mi_foto.jpg`).
- El atributo `alt` debe ser descriptivo y específico, no vacío ni genérico.
- Si la imagen no carga (ruta incorrecta, archivo faltante o con nombre que
  no coincide en mayúsculas/minúsculas con el `src`): ❌ en ese sub-ítem.

## Archivo de devolución por alumno

- Guardar en `lab2/devoluciones/<token-del-alumno>.md`.
- Al terminar todas las entregas del lab, generar el consolidado
  `lab2/devoluciones/Lab02-devoluciones-completas.md` con tabla resumen al
  inicio y la devolución completa de cada alumno a continuación.

## Formato del informe de corrección

Por cada alumno entregar:

1. **Datos identificatorios**: nombre, legajo, token, enlace al repo,
   enlace a GitHub Pages.
2. **Checklist por ítem** con estado: ✅ cumple / ❌ no cumple / ⚠️ parcial
   y motivo concreto.
3. **Observaciones puntuales**: errores específicos con archivo y sección afectada.
4. **Nota final (0–100)** con desglose ítem por ítem que la justifica.
