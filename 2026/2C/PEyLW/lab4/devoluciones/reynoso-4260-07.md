# Devolución Lab 4 — Ramiro Reynoso

## Datos identificatorios

- **Token:** reynoso-4260-07
- **GitHub Pages:** https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/ (inferida — no fue entregada explícitamente; verificada con WebFetch: responde 200 y el HTML/CSS servido coincide con el repositorio clonado)
- **Repositorio:** https://github.com/Ramireybas/peylw-2026-practicos-reynoso-4260-07

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(215, 80%, 40%)` usado como color primario en `header h1`, `nav a:hover`, `th`, botones y `.btn-arriba`; color modulado, no puro. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | `styles.css` línea 1: `/* TOKEN-ALUMNO: reynoso-4260-07 - HSL: hsl(215, 80%, 40%) */`. |
| Tabla de `contacto.html` formateada | ✅ | `styles.css` líneas 141–160: bordes 1px, padding 10px, `th` con fondo `hsl(215,80%,40%)` y texto blanco, filas pares con `#f2f2f2`. |
| Formulario de `contacto.html` formateado | ⚠️ | Campos de texto bien formateados, pero los grupos de radio/checkbox quedan distorsionados. Ver observaciones. |
| Fuente web importada y aplicada | ✅ | `styles.css` línea 3: `@import` de Google Fonts "Montserrat"; aplicada en `body` (línea 6) con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo-curza">` ubicado entre `<h1>` y `<nav>` dentro de `.contendor_header` (flex, `justify-content: space-between`) en las tres páginas. |
| Animación de giro completo (360°) del logo | ✅ | `styles.css` líneas 38–45: `transition: transform 1s ease-in-out` en `.logo-curza` + `.logo-curza:hover { transform: rotateY(360deg) }`. Disparada por hover, variante admitida por la consigna ("transition disparada"). |
| Header fijo en todas las páginas | ✅ | `styles.css` líneas 13–22: `header { position: fixed; top: 0 }`, hoja compartida por `index.html`, `acercade.html` y `contacto.html`. `body { padding-top: 90px }` (línea 10, 130px en mobile, línea 199) compensa el contenido tapado. |
| "Acerca de" — primera línea sticky | ✅ | `styles.css` líneas 90–98: `.bio-box h2` (el `<h2>Biografía</h2>`) con `position: sticky; top: 0` y `background-color: #f9f9f9` sólido. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `styles.css` líneas 82–88: `.bio-box { max-height: 300px; overflow-y: auto }`. El contenedor con el límite de alto es el `<div class="bio-box">` que envuelve al `<h2>` y al `<article>`, no el `<article>` mismo — variante admitida por la consigna ("o contenedor del texto"). |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="btn-arriba">▲</a>` presente en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `styles.css` líneas 162–177: `border-radius: 50%`, `position: fixed; bottom: 20px; right: 20px`, carácter `▲` centrado. |
| Botón volver arriba — funcional | ✅ | Ancla `href="#top"` resuelve contra `<div id="top"></div>` al inicio del `<body>` en las tres páginas. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en el `<head>` de `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `styles.css` líneas 24–31 y 50–56: `.contendor_header` y `nav ul` con `display: flex`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `styles.css` líneas 188–205: `@media (max-width: 768px)` apila `.contendor_header` y `nav ul` en columna y aplica `table { display: block; overflow-x: auto }`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 preguntas están respondidas; el fragmento de CSS citado en la pregunta 1 (líneas 5–12 de `REFLEXION.md`) coincide textualmente con `.logo-curza` / `.logo-curza:hover` real en `styles.css` (líneas 38–45). |

## Observaciones puntuales

- **`styles.css`, líneas 107–120** (reglas `form label` y `form input`): ambas reglas son genéricas y se aplican a *todos* los `<label>` e `<input>` del formulario sin distinguir `type`. En los fieldsets "Método Preferido de contacto" y "Suscripción de Interés" (`contacto.html`, líneas 71–94) esto produce dos problemas combinados:
  - `form input { width: 100% }` se aplica también a los `input[type=radio]`/`checkbox`, estirándolos a barras horizontales de ancho completo en lugar de dejarlos como controles pequeños y circulares/cuadrados nativos.
  - `form label { display: block }` hace que cada `<label>` salte a una línea nueva en vez de quedar al lado de su radio/checkbox correspondiente, por lo que cada par queda en dos líneas separadas (control arriba, texto abajo) en lugar de alineados horizontalmente.
  Falta acotar ambos selectores (p. ej. `input[type="text"], input[type="email"], input[type="tel"], input[type="number"]` y una excepción de `display: inline`/`inline-block` para los labels de radio/checkbox) para que los grupos se vean legibles y alineados como controles estándar.
- La animación del logo solo se dispara con `:hover` (`styles.css` líneas 38–45); no hay ejecución automática al cargar la página ni al hacer clic. La consigna admite "el evento que el alumno haya definido", por lo que no se penaliza, pero se señala porque un usuario que no pase el mouse sobre el logo nunca ve el giro (en mobile, sin hover real, el efecto no se percibe).
- La entrega no incluyó la URL de GitHub Pages, solo el repositorio (ver `README.md`, campo "Enlace al Repositorio de GitHub"); el enunciado pide entregar la URL de Pages ya desplegada. Se infirió la URL estándar (`https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/`) y se verificó con WebFetch que responde 200 y que el HTML (título, h1, nav, footer) y el CSS servidos coinciden con el repositorio clonado.
- El resto de los ítems (personalización, tabla, fuente web, header fijo con compensación, sticky + scroll en "Acerca de", botón volver arriba, responsive, `REFLEXION.md`) cumple sin desvíos relevantes respecto del enunciado.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 12 |
| Formulario `contacto.html` | 12 | 10 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 12 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **98** |
