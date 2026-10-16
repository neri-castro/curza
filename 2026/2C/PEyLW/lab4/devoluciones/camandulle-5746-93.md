# Devolución Lab 4 — Fernanda Camandulle

## Datos identificatorios

- **Token:** camandulle-5746-93
- **GitHub Pages:** https://camandulle.github.io/peylw-2026-practicos-camandulle-5746-93/
- **Repositorio:** https://github.com/Camandulle/peylw-2026-practicos-camandulle-5746-93 (rama `main`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(217, 90%, 55%)` modulado, no es color puro. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera de `styles.css` (líneas 1-4) con los tres tonos HSL y `Alumno: camandulle-5746-93`. |
| Tabla de `contacto.html` formateada | ✅ | Bordes (`border-bottom`), padding 10px/12px, encabezado `th` con fondo `--primario` y texto blanco, filas pares con `--primario-claro`. |
| Formulario de `contacto.html` formateado | ✅ | Inputs con padding/border/radio consistentes; `label` alineado a la izquierda del input vía `form > p { display:flex }`. Grupos de radios/checkboxes dentro de `fieldset` son legibles (sin solapamiento), aunque no tienen una regla CSS propia más allá del flujo normal de `input`+`label` en un `<p>`. |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts "Outfit" en `styles.css`, aplicada en `body { font-family: 'Outfit', sans-serif }` (hereda a todo el sitio), con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `.header-top` con `display:flex; justify-content:space-between`, `h1` antes de `img.logo-curza` → el logo queda a la derecha. |
| Animación de giro completo (360°) del logo | ✅ | `transition: transform 1s ease-in-out` + `.logo-curza:hover { transform: rotateY(360deg) }`. Es una transición disparada por evento (hover), alternativa explícitamente admitida a `@keyframes`; termina en 360°, equivalente visual a 0°, orientación correcta. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top:0; width:100% }` en el único `styles.css` compartido por `index.html`, `acercade.html` y `contacto.html`. |
| "Acerca de" — primera línea sticky | ✅ | `.biografia > h2 { position: sticky; top:0 }` aplica solo al primer `<h2>` ("Biografía"), no a los `<h2>` internos de cada sección. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height: 300px; overflow-y: auto }`; el contenido (varias secciones + figura) excede los 300px, por lo que la barra aparece. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="volver-arriba">` al final del `<body>` en las tres páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius:50%`, `position:fixed; bottom:20px; right:20px`, carácter `▲` centrado con flex. |
| Botón volver arriba — funcional | ✅ | Ancla `#top` apunta a `<body id="top">`; vuelve al inicio del documento. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display:flex }` y `form > p { display:flex }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width:768px)`: `nav ul` pasa a `flex-direction:column`, `table` a `display:block; overflow-x:auto` (no rompe el ancho), y se ajusta el `padding-top` del `main` para compensar el header más alto. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Sección "TP4" del archivo con las 3 preguntas respondidas; el fragmento de CSS citado en la pregunta 1 coincide textualmente con `.logo-curza`/`.logo-curza:hover` de `styles.css`. |

## Observaciones puntuales

- `contacto.html`: los grupos de radios (`metodo-contacto`) y checkboxes (`suscripcion`) están envueltos en `<p>` dentro de `fieldset`, por lo que no son alcanzados por la regla `form > p` (selector de hijo directo). Quedan legibles por el flujo por defecto del navegador, pero no tienen tratamiento CSS propio como el resto de los campos; no genera superposición ni desalineación, así que no se descuenta.
- La tabla "resumen" de `contacto.html` tiene celdas vacías (`id="resumen-nombre"`, etc.) pensadas para completarse con JavaScript, que no está presente en el repositorio. Esto no afecta el ítem de formato de tabla (CSS), que es lo que corresponde evaluar en este TP.
- `README.md` conserva la carátula y la fecha de entrega del Laboratorio 2 (formato de labs anteriores); no corresponde descuento porque este TP no exige carátula, pero el dato quedó desactualizado.
- Verificación en vivo (código + reachability, sin navegador): las tres páginas y `styles.css` responden 200 en GitHub Pages; el comentario de cabecera y los selectores clave (`.logo-curza`, `.volver-arriba`, `.biografia`, `@media (max-width:768px)`) coinciden con el contenido del repositorio clonado. No se verificó interacción en vivo (hover, scroll, clic) por estar fuera del método de verificación acordado para esta corrección.
- Commit del TP4 (`55b4a8f`) fechado 2026-10-10 19:53:43 -03:00, dentro del plazo de cierre (10/10/2026 23:00).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 12 |
| Formulario `contacto.html` | 12 | 12 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 12 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **100** |
