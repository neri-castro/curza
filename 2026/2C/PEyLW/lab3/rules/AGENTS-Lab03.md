# Reglas de Corrección — Laboratorio 3: Captura de Datos y Validación Semántica con Formularios HTML5

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 3. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

Fechas oficiales: apertura domingo 06/09/2026 00:00 — cierre lunes 28/09/2026
23:55. Entregas posteriores al cierre: marcar como tardías según criterio
general del curso (este documento no define penalización por atraso).

## Tono y estilo de la corrección

- Sin adulación. Sin emojis de aprobación ni frases de relleno motivacional.
- Señalar errores y omisiones citando el archivo y la tarea del enunciado.
- No inflar la nota por esfuerzo percibido. Si falta algo, se descuenta.
- Lo que está bien: una línea. El foco es lo que falta o está mal.

## Continuidad con el Lab 2

El repositorio de este laboratorio es, en la mayoría de los casos, el mismo
repo `peylw-2026-practicos-<token>` usado en los Labs 1 y 2, ahora extendido
con `contacto.html`. Puntos importantes:

- `index.html` y `acercade.html` **no se reescriben**: solo se les agrega el
  enlace "Contacto" en el `<nav>`. Si el `<header>`, `<h1>` o `<footer>` de
  Lab 2 desaparecieron o se rompieron al editar el `<nav>`, es un
  incumplimiento de este TP (vinculación de navegación), no un tema de Lab 2.
- `contacto.html` es un archivo nuevo: debe respetar la misma cabecera,
  navegación y pie de página que las otras dos páginas del portal.
- El `README.md` y el `REFLEXION.md` de este TP son documentos nuevos y
  distintos a los de Labs 1 y 2; no deben confundirse ni reutilizarse sin
  actualizar.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 3

| Ítem | Puntos |
|---|---|
| Carátula / README.md completo con todos los campos | 5 |
| Personalización (token en comentario + `id="btn-cargar-[token]"`) (ver detalle) | 8 |
| Vinculación de navegación — enlace "Contacto" en las 3 páginas (ver detalle) | 7 |
| **Tarea 1** — Estructura base de `contacto.html` (ver detalle) | 8 |
| **Tarea 2** — Formulario y validaciones nativas (ver detalle) | 35 |
| **Tarea 3** — Tabla de resumen vacía con IDs únicos (ver detalle) | 10 |
| **Tarea 4** — `styles.css` vinculado y commit exacto (ver detalle) | 7 |
| Estructura de archivos exacta (raíz del repo) | 5 |
| GitHub Pages desplegado y respondiendo 200 | 5 |
| **Reflexión** — `REFLEXION.md` con las 3 preguntas respondidas (ver detalle) | 10 |
| **TOTAL** | **100** |

#### Detalle Personalización (8 pts)

| Sub-ítem | Puntos |
|---|---|
| Comentario de Token Único en el encabezado de `contacto.html` | 4 |
| Botón de envío con `id="btn-cargar-[tu-token-unico]"` exacto | 4 |

Si el `id` del botón tiene el formato correcto pero el token no coincide con
el del alumno: ⚠️ parcial.

#### Detalle Vinculación de navegación (7 pts)

| Sub-ítem | Puntos |
|---|---|
| `index.html` incluye enlace "Contacto" → `contacto.html` en `<nav>` | 2 |
| `acercade.html` incluye enlace "Contacto" → `contacto.html` en `<nav>` | 2 |
| `contacto.html` incluye los 3 enlaces del `<nav>` (Inicio, Acerca de, Contacto) | 3 |

Si el `<nav>` de alguna página quedó con estructura distinta (perdió la
`<ul>`, dejó de ser lista, etc.) respecto a las otras dos: ⚠️ parcial en ese
sub-ítem.

#### Detalle Tarea 1 — Estructura base `contacto.html` (8 pts)

| Sub-ítem | Puntos |
|---|---|
| Plantilla HTML5 válida con `<html lang="es">`, `charset utf-8` y `<title>` descriptivo | 2 |
| `<header>` y `<footer>` consistentes con `index.html`/`acercade.html` | 3 |
| `<main>` con sección de formulario y `<h2>` descriptivo | 3 |

#### Detalle Tarea 2 — Formulario y validaciones (35 pts)

| Sub-ítem | Puntos |
|---|---|
| Nombre — `type="text"`, `required`, `maxlength="20"` | 3 |
| Apellido — `type="text"`, `maxlength="20"` | 2 |
| Email — `type="email"`, `required` | 3 |
| Teléfono — placeholder exacto `Ej: +54 2920 123456` | 2 |
| Edad — `type="number"`, `min="16"`, `max="120"` | 3 |
| Dirección — campo de texto libre presente | 2 |
| Provincia — `<datalist>` con las 6 sugerencias pedidas (Río Negro, Neuquén, Chubut, Santa Cruz, Tierra del Fuego, La Pampa) | 4 |
| Código Postal — `pattern="^[A-Z]\d{4}[A-Z]{3}$"` y atributo `title` con advertencia de formato | 5 |
| Método de Contacto — 3 radios excluyentes con mismo `name`, "Correo electrónico" `checked` por defecto | 4 |
| Suscripción de Interés — 4 checkboxes, "Alertas" `checked` por defecto | 4 |
| Botón de envío `type="submit"` con etiqueta "Cargar" | 3 |

Si el `pattern` del Código Postal no es exactamente
`^[A-Z]\d{4}[A-Z]{3}$` (o una regex funcionalmente equivalente que rechace
"8500" y "R8500" y acepte "R8500AAF"): ⚠️ parcial. Si falta el atributo
`title`: descontar 1 pto adicional de ese sub-ítem. Si los radios de método
de contacto usan `name` distinto entre sí (permitiendo selección múltiple):
❌ en ese sub-ítem, no es un radio group funcional.

Cada campo debe tener su `<label>` asociado mediante `for`/`id`. La ausencia
de `<label>` en un campo no anula el puntaje de validación de ese campo,
pero se registra como observación y afecta la Pregunta 2 de la reflexión si
el alumno no lo usó en ningún campo.

#### Detalle Tarea 3 — Tabla de resumen vacía (10 pts)

| Sub-ítem | Puntos |
|---|---|
| `<table>` presente debajo del formulario con dos columnas (título / dato) | 2 |
| Los 10 campos del enunciado están representados como filas | 3 |
| Los 10 `id` de celda son exactos y están vacíos (ver lista abajo) | 5 |

IDs exactos esperados: `resumen-nombre`, `resumen-apellido`, `resumen-email`,
`resumen-telefono`, `resumen-edad`, `resumen-direccion`,
`resumen-provincia`, `resumen-cp`, `resumen-metodo`, `resumen-suscripciones`.

Si falta algún `id` o está mal escrito: descontar proporcionalmente dentro
del sub-ítem de 5 pts (0.5 pto por cada `id` ausente o incorrecto). Si una
celda tiene contenido de ejemplo en vez de estar vacía: ⚠️ parcial en ese
`id`.

#### Detalle Tarea 4 — `styles.css` y commit (7 pts)

| Sub-ítem | Puntos |
|---|---|
| `<link>` a `styles.css` presente en el `<head>` de `contacto.html` | 3 |
| Commit en el historial con el mensaje exacto `TP3: Implementacion de formulario contacto con validacion` | 4 |

Si el mensaje de commit difiere en tildes, mayúsculas o puntuación menor:
⚠️ parcial (3/4). Si el contenido no corresponde a este commit (no incluye
`contacto.html`): ❌.

#### Detalle Reflexión — `REFLEXION.md` (10 pts)

| Sub-ítem | Puntos |
|---|---|
| Pregunta 1: código HTML literal del campo Código Postal con `pattern` y `title`, y coincide con lo que realmente está en `contacto.html` | 4 |
| Pregunta 2: explica para qué sirve `<label>` y cómo se asocia con `for` | 3 |
| Pregunta 3: explica el comportamiento de radios con `name` distinto vs. mismo `name` | 3 |

Respuesta de una línea sin justificación real, o copiada textual de internet
sin adaptación: ⚠️ parcial en esa pregunta. Si el código de la Pregunta 1 no
coincide con el `pattern`/`title` real usado en `contacto.html`: ⚠️ parcial.

## Verificación en internet

- Acceder al repositorio de GitHub del alumno para confirmar que es público
  y que contiene `contacto.html` y los cambios de navegación en las otras
  dos páginas.
- Acceder a la URL de GitHub Pages para confirmar que responde 200 y que
  navegando desde cualquiera de las tres páginas a las otras dos (incluido
  "Contacto") los enlaces funcionan realmente en el sitio desplegado, no
  solo en local.
  URL esperada: `https://<usuario>.github.io/peylw-2026-practicos-<token>/contacto.html`
- Si Pages devuelve 404, o los enlaces de navegación rompen en producción:
  incumplimiento del ítem correspondiente.
- La validación nativa del navegador (`pattern`, `required`, `min`/`max`,
  `maxlength`) no se puede verificar solo leyendo el HTML con certeza total;
  si es posible, abrir `contacto.html` desplegado y probar enviar el
  formulario con un CP inválido (ej. `"8500"`) para confirmar que el
  navegador bloquea el envío.

## Clonado y revisión local

- Clonar (o reutilizar el clon de Lab 1/Lab 2) en
  `lab3/repos-clonados/<token-del-alumno>/` y hacer `git pull` si ya existía.
- Revisar estructura real con `find . -not -path "./.git*"`.
- Verificar historial con `git log --oneline --all --stat`:
  - Debe existir un commit con el mensaje exacto
    `TP3: Implementacion de formulario contacto con validacion` que incluya
    `contacto.html` (y los cambios de `<nav>` en `index.html`/`acercade.html`
    si se hicieron en el mismo commit).
  - Si hay commits adicionales, no penalizar por su existencia.
- Leer `contacto.html`, `index.html`, `acercade.html`, `README.md` y
  `REFLEXION.md` sobre el clon local.
- No modificar ni commitear nada en el clon.
- Diferencias de casing en nombres de archivo no se penalizan.

## Verificaciones específicas de `contacto.html`

- Debe tener el comentario de Token Único al inicio del `<body>` (o en el
  encabezado, según lo haya ubicado el alumno) y el botón de envío con
  `id="btn-cargar-[token]"` exacto.
- Confirmar que cada uno de los 11 campos del formulario existe con el tipo
  y los atributos de validación pedidos exactamente (ver Detalle Tarea 2).
- Confirmar que el `<nav>` de `contacto.html` es equivalente al de
  `index.html`/`acercade.html`, con el tercer enlace agregado.
- El archivo no puede estar vacío ni ser un placeholder sin contenido real.

## Archivo de devolución por alumno

- Guardar en `lab3/devoluciones/<token-del-alumno>.md`.
- Al terminar todas las entregas del lab, generar el consolidado
  `lab3/devoluciones/Lab03-devoluciones-completas.md` con tabla resumen al
  inicio y la devolución completa de cada alumno a continuación.

## Formato del informe de corrección

Por cada alumno entregar:

1. **Datos identificatorios**: nombre, legajo, token, enlace al repo,
   enlace a GitHub Pages.
2. **Checklist por ítem** con estado: ✅ cumple / ❌ no cumple / ⚠️ parcial
   y motivo concreto.
3. **Observaciones puntuales**: errores específicos con archivo y sección afectada.
4. **Nota final (0–100)** con desglose ítem por ítem que la justifica.
