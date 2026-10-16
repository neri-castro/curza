# Devolución Lab 4 — Javier Chavarria

## Datos identificatorios

- **Token:** chavarria-7037-55
- **GitHub Pages:** https://javi-jav.github.io/peylw-2026-practicos-chavarria-7037-55/
- **Repositorio:** https://github.com/javi-jav/peylw-2026-practicos-chavarria-7037-55

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(205, 65%, 38%)` y derivados, modulados, sin colores puros. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera de `styles.css` (líneas 5-14) con alumno, token y los 4 tonos HSL usados. |
| Tabla de `contacto.html` formateada | ⚠️ | Bordes y espaciado correctos, pero la tabla no tiene ningún encabezado diferenciado visualmente (ver observaciones). |
| Formulario de `contacto.html` formateado | ✅ | Campos, labels y grupos de radio/checkbox con estilo consistente. |
| Fuente web importada y aplicada | ✅ | Montserrat vía `@import` de Google Fonts, aplicada en `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ⚠️ | Logo presente pero sin mecanismo de layout (flex/grid) en `header`; queda apilado debajo del `<h1>`, no a la derecha. |
| Animación de giro completo (360°) del logo | ✅ | `transition` disparada por `:hover` con `rotateY(360deg)`, giro completo y vuelve a orientación correcta. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed }` en `styles.css`, compartido por las 3 páginas; `main` compensa con `padding-top`. |
| "Acerca de" — primera línea sticky | ✅ | `.biografia > h2` con `position: sticky; top: 0` y `background-color: white`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height: 300px; overflow-y: auto; }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `.volver-inicio`: círculo (`border-radius: 50%`), `▲`, `position: fixed; bottom/right`. |
| Botón volver arriba — funcional | ✅ | Ancla `href="#top"` con `<body id="top">` en las 3 páginas. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en el `<head>` de `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display: flex }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width: 768px)`: `nav ul { flex-direction: column }`, `table { display: block; overflow-x: auto }`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 preguntas de TP4 están respondidas y el fragmento de CSS citado coincide con el código real. |

## Observaciones puntuales

- **`index.html`/`acercade.html`/`contacto.html` — header**: el `<header>` no tiene `display: flex` (ni ningún otro mecanismo de layout horizontal) en `styles.css`. Como `<h1>` es un elemento de bloque, la `<img class="logo-curza">` que lo sigue no se renderiza a la derecha del título como pide el enunciado, sino apilada debajo de él (el flujo normal del documento pone cada elemento de bloque/inline en una línea distinta tras un bloque). El valor llamativamente alto de `main { padding: 250px ... }` (línea 70 de `styles.css`) es consistente con un header de tres filas apiladas (título, logo, nav) en lugar de una sola fila con el logo a la derecha. Esto afecta directamente el primer sub-ítem del rubro "Animación de título + logo".
- **`contacto.html` — tabla "Resumen de datos"**: la tabla (líneas 124-165) no usa `<th>` en ninguna fila ni tiene estilo propio para distinguir una fila/columna de encabezado; `styles.css` solo define `td` y `tr:nth-child(even)` (zebra striping), sin ninguna regla que diferencie "encabezados" del resto de las celdas. El sub-ítem de encabezados diferenciados no se cumple.
- **`styles.css` — animación del logo**: la implementación usa `transition: transform 1s ease-in-out` + `:hover { transform: rotateY(360deg) }` en lugar de `@keyframes`/`animation`; esto está explícitamente permitido por la rúbrica ("transition disparada"), y funciona correctamente: gira 360° al pasar el cursor y vuelve a la orientación original al retirarlo. No hay objeción sobre este punto en sí, solo sobre la posición del logo (ver primer punto).
- Verificación en vivo (`WebFetch`, método código + reachability): `https://javi-jav.github.io/peylw-2026-practicos-chavarria-7037-55/`, `/acercade.html`, `/contacto.html` y `/styles.css` responden **200** y el contenido coincide con el clon local (mismo `h1`, mismo token en el footer, mismo CSS con header fijo, animación, sticky, tabla y responsive). No se detectan discrepancias entre repo y sitio desplegado.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 8 |
| Formulario `contacto.html` | 12 | 12 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 10 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **94** |
