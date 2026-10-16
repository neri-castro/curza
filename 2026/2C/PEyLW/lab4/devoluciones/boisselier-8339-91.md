# Devolución Lab 4 — Sara Celeste Boisselier

## Datos identificatorios

- **Token:** boisselier-8339-91
- **GitHub Pages:** https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/
- **Repositorio:** https://github.com/saraboisselier/peylw-2026-practicos-boisselier-8339-91

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `styles.css` líneas 1-12: primario `hsl(335, 55%, 65%)`, secundario, fondo y texto en HSL modulado, ningún color puro. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | `styles.css` líneas 3-12: comentario de cabecera con nombre, legajo, token y los 4 HSL. |
| Tabla de `contacto.html` formateada | ✅ | `styles.css` líneas 141-160: bordes, `padding: 12px`, `th` con fondo `hsl(335,55%,80%)` diferenciado y filas alternadas. |
| Formulario de `contacto.html` formateado | ✅ | `styles.css` líneas 164-205: inputs con padding/borde consistentes, labels en negrita sobre su campo, radios/checkboxes con `align-self: flex-start`. |
| Fuente web importada y aplicada | ✅ | `styles.css` línea 1: `@import` de Google Fonts "Outfit"; línea 24: `body { font-family: 'Outfit', sans-serif; }`, con fallback. |
| Logo CURZA a la derecha del título | ⚠️ | Cumple en `acercade.html` y `contacto.html` (`div.encabezado-superior` con `display:flex`), pero `index.html` (líneas 13-16) no incluye ese `div`: el `<h1>` y el `<img class="logo-curza">` quedan como hijos directos del `<header>`, que no tiene `display:flex`, por lo que el logo se apila debajo del título en vez de a la derecha. |
| Animación de giro completo (360°) del logo | ✅ | `styles.css` líneas 57-67: `transition: transform 1s ease-in-out` + `.logo-curza:hover { transform: rotateY(360deg); }`. Termina en orientación correcta (360°≡0° visualmente). Disparada por `:hover`, válido según rúbrica ("transition disparada"). |
| Header fijo en todas las páginas | ⚠️ | `position: fixed; top:0` está declarado una sola vez en `styles.css` (línea 32) y aplica a las tres páginas por igual estructuralmente. Pero como el `index.html` no tiene el wrapper flex (ítem anterior), su header queda con altura distinta (título e imagen apilados) a la de `acercade.html`/`contacto.html`, mientras que `main { padding-top: 180px }` es el mismo valor fijo para las tres páginas — riesgo de que en `index.html` el contenido quede parcialmente tapado por el header, al ser éste más alto que en las otras dos páginas. |
| "Acerca de" — primera línea sticky | ✅ | `acercade.html` línea 31 + `styles.css` líneas 125-132: `.biografia-scroll h2 { position: sticky; top:0; background-color: white; }`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `styles.css` líneas 117-123: `.biografia-scroll { max-height: 300px; overflow-y: auto; }` sobre el contenedor de texto dentro del `<article>`. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente al final del `<body>` en `index.html`, `acercade.html` y `contacto.html` (`<a href="#top" class="volver-arriba">▲</a>`). |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `styles.css` líneas 209-224: `border-radius: 50%`, `position: fixed; bottom:20px; right:20px`, carácter `▲`. |
| Botón volver arriba — funcional | ⚠️ | El enlace apunta a `#top`, que es el `id` del propio `<header>`. Como el header tiene `position: fixed`, su `getBoundingClientRect().top` es siempre `0` respecto del viewport sin importar el scroll actual — el navegador calcula que el destino "ya está visible" y, en la práctica, el salto de ancla no produce ningún desplazamiento real de la página (bug conocido de anclar a un elemento `fixed`). No se pudo confirmar en vivo porque el método acordado excluye automatización de navegador; se señala como riesgo de código concreto, no como hecho confirmado por clic real. |
| Responsive — meta viewport en las tres páginas | ✅ | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` presente en el `<head>` de `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `styles.css` línea 72 (`nav ul { display:flex }`) y línea 165 (`form { display:flex; flex-direction:column }`). |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `styles.css` líneas 236-276: `@media (max-width:768px)` con `nav ul { flex-direction: column }` y `.tabla-contenedor { overflow-x:auto }` reforzado. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 preguntas están respondidas; el fragmento citado en la respuesta 1 coincide con el `transition`/`:hover` real de `styles.css` (líneas 62-67). |

## Observaciones puntuales

- `index.html` (líneas 13-16): falta el `<div class="encabezado-superior">` que sí está en `acercade.html` (línea 14) y `contacto.html` (línea 14). Sin ese `div`, el `<h1>` y el logo quedan como bloques apilados verticalmente dentro del `<header>` en vez de en fila, rompiendo la consistencia visual del encabezado entre las tres páginas y, probablemente, la altura fija asumida por `main { padding-top: 180px }`.
- `styles.css` (botón "volver arriba", líneas 209-224 + header líneas 31-40): el ancla `href="#top"` apunta al `<header id="top">`, que tiene `position: fixed`. Al estar fuera del flujo normal del documento, saltar a su ancla no desplaza efectivamente el scroll en los navegadores modernos. Se recomienda anclar a un elemento no fijo (por ejemplo un `<div id="top">` al inicio del `<body>`, antes del header) o usar `onclick="window.scrollTo(0,0)"`/JS equivalente.
- El resto de los ítems de tabla, formulario, fuente web, sticky/scroll en "Acerca de" y responsive están bien resueltos y sin observaciones adicionales más allá de lo ya señalado.
- Verificación en vivo: las tres URLs de GitHub Pages responden `200` y el contenido (título, `h1`, campos del formulario, tabla) coincide con el repositorio clonado. No se verificó el comportamiento interactivo (clic en "volver arriba", hover de la animación, scroll del header) por no usar automatización de navegador, según el método acordado para esta corrección.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 12 |
| Formulario `contacto.html` | 12 | 12 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 11 |
| Header fijo | 12 | 11 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 10 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **96** |
