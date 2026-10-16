# Devolución Lab 4 — Santiago Valentín Apelahnz

## Datos identificatorios

- **Token:** apelahnz-2743-10
- **GitHub Pages:** https://officialsantos.github.io/peylw-2026-practicos-apelahnz-2743-10/
- **Repositorio:** https://github.com/officialsantos/peylw-2026-practicos-apelahnz-2743-10

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(355, 62%, 62%)` como primario, sin colores puros sin modular. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | `styles.css` líneas 3-9: comentario con token `apelahnz-2743-10` y los tres códigos HSL usados. |
| Tabla de `contacto.html` formateada | ⚠️ | Bordes, padding y filas alternas correctos; los `<th>` no tienen ninguna regla propia (color de fondo o `font-weight`) que los diferencie de los `<td>` más allá del bold por defecto del navegador. |
| Formulario de `contacto.html` formateado | ⚠️ | Campos de texto y labels bien alineados; el grupo de radios y el de checkboxes no reciben el layout en fila previsto por un bug de selector CSS (ver observaciones). |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts ("Outfit") aplicada en `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo">` ubicado entre el `<h1>` y el `<nav>`, header en `display:flex`. |
| Animación de giro completo (360°) del logo | ✅ | `.logo:hover { transform: rotateY(360deg); }` con `transition: transform 1s ease-in-out;`, termina en orientación correcta. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top:0; }` en `styles.css`, compartido por `index.html`, `acercade.html` y `contacto.html`; `main` compensa con `padding-top`. |
| "Acerca de" — primera línea sticky | ✅ | `.biografia h2 { position: sticky; top:0; background-color:#f4f4f9; }` en `acercade.html`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height:300px; overflow-y:auto; }`; aplicado sobre la `<section class="biografia">` que envuelve el texto (no sobre el `<article>` en sí, pero es el contenedor real del texto, admitido por la consigna). |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `.volver-arriba { border-radius:50%; position:fixed; bottom:20px; right:20px; }`, carácter "▲". |
| Botón volver arriba — funcional | ✅ | Ancla `href="#top"` hacia `<a id="top"></a>` presente en las tres páginas. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display:flex; }` y `.form-contacto { display:flex; flex-direction:column; }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width:768px)` apila `nav ul` y aplica `display:block; overflow-x:auto;` a `.tabla-resumen`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 respuestas del Lab 4 están completas; el fragmento de CSS citado en la pregunta 1 coincide textualmente con el `.logo`/`.logo:hover` real de `styles.css`. |

## Observaciones puntuales

- **`styles.css`, selectores `.radios` vs. `.radio-group`/`.checkbox-group`** (líneas 121-133): el `<fieldset>` de "Método de contacto preferido" usa `class="radio-group"` y el de "Suscripción de interés" usa `class="checkbox-group"` (ver `contacto.html` líneas 84 y 102), pero la regla que pretende alinear las opciones en fila apunta a `.radios label` — una clase que no existe en ningún HTML del repo. Como resultado, esas etiquetas quedan bajo la regla general `.form-contacto label { display:flex; flex-direction:column; }`, mostrando el input apilado arriba del texto en cada opción de radio/checkbox en lugar de en línea. Es un bug de nombre de clase, no una decisión de diseño.
- **`styles.css`, tabla de resumen** (líneas 142-164): no hay ninguna regla que diferencie visualmente el `<thead>`/`<th>` del resto de celdas (ni `background-color`, ni `font-weight` explícito); la única distinción que se ve es el bold por defecto del navegador sobre `<th>`, no un estilo agregado por el alumno.
- **`styles.css`, `.radio-group`/`.checkbox-group`** (líneas 121-123 y 131-133): `margin-right: 70%` sobre ambos fieldsets reduce fuertemente su ancho disponible; sumado al bug de arriba, puede angostar aún más la lectura de las opciones. No llega a haber superposición entre opciones distintas, por lo que no se descuenta a ❌, pero el layout no es el previsto por el alumno mismo (la regla muerta `.radios label` lo confirma).
- El `max-height:300px` + `overflow-y:auto` de "Acerca de" está aplicado sobre `<section class="biografia">`, no sobre el `<article>` que la contiene (`acercade.html` líneas 25-52). Se admite como "contenedor del texto" porque es la sección que agrupa efectivamente el `<h2>` y los párrafos de la biografía.
- Verificación en vivo: GitHub Pages responde 200 y el `styles.css` servido es idéntico byte a byte al del repo clonado; el HTML de `index.html` y `contacto.html` desplegados coincide con el contenido del clon local (título, `h1`, footer, campos del formulario y encabezados de tabla).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 10 |
| Formulario `contacto.html` | 12 | 10 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 12 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **96** |
