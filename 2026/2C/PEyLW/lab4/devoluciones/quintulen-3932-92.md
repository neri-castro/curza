# Devolución Lab 4 — Carlos Quintulen

## Datos identificatorios

- **Token:** quintulen-3932-92
- **GitHub Pages:** https://caarlosq.github.io/peylw-2026-practicos-quintulen-3932-92/
- **Repositorio:** https://github.com/CaarlosQ/peylw-2026-practicos-quintulen-3932-92 (rama `laboratorio_4`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | Toda la paleta usa la misma familia `hsl(218, 35%, X%)`, sin colores puros sin modular. |
| Personalización — comentario en `styles.css` con HSL + identificador | ⚠️ | `styles.css` línea 1 solo trae el código HSL, sin el identificador del alumno. |
| Tabla de `contacto.html` formateada | ⚠️ | Bordes y espaciado correctos, pero los encabezados no tienen diferenciación CSS propia. |
| Formulario de `contacto.html` formateado | ✅ | Inputs, labels y fieldsets consistentes y alineados. |
| Fuente web importada y aplicada | ✅ | Google Fonts "Syne" aplicada a `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `img` ubicado después del `h1` dentro de `.title-image` (fila). |
| Animación de giro completo (360°) del logo | ✅ | `transform: rotateY(360deg)` en `:hover` con `transition` de 1s. |
| Header fijo en todas las páginas | ✅ | `position: fixed; top:0` en `header`, compartido por las 3 páginas, con compensación de `margin-top` en cada `main`. |
| "Acerca de" — primera línea sticky | ✅ | `article > h2` ("Biografía") con `position: sticky; top:0`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `article { max-height: 300px; overflow-y: auto; }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top">` presente en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ❌ | No hay forma circular (sin `border-radius:50%` ni fondo); además está oculto por debajo de 1200px de viewport. |
| Botón volver arriba — funcional | ⚠️ | El ancla `#top` sí hace scroll al inicio, pero el botón solo es visible/clickeable en viewports ≥1200px. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en las tres. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | Flexbox en `nav ul`, en los `div` del formulario y Grid en `#main-contacto` (≥1200px). |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | Apilado logrado con enfoque mobile-first (`@media (width >= 768px)`); resultado práctico equivalente al pedido. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Presente, 3 preguntas respondidas, fragmento citado coincide con el código real. |

## Observaciones puntuales

- **`styles.css`, línea 1**: el comentario de cabecera es `/* Color HSL: hsl(218, 35%, 12%) */`. Cumple con declarar el código HSL, pero no incluye el identificador del alumno (token o nombre) exigido por el punto 3.1 del enunciado. El token sí aparece, pero como comentario HTML en cada página (`<!-- TOKEN-ALUMNO: quintulen-3932-92 -->`), no en la cabecera del CSS, que es lo que pide específicamente la rúbrica.
- **`styles.css`, línea 1 (detalle menor)**: el valor citado en el comentario (`12%` de luminosidad) no coincide exactamente con ninguna variable del `:root` (la más cercana es `--title: hsl(218, 35%, 10%)`). Coherente en familia de color, pero no es el valor exacto usado.
- **`styles.css`, bloque `main > a` (línea 92-94) y `@media (width >= 1200px)` (líneas 441-449)**: el botón "volver arriba" tiene `visibility: hidden` por defecto y solo se vuelve `visible` dentro de la media query de 1200px. Esto significa que en mobile, tablet y en la mayoría de resoluciones de notebook estándar (hasta 1199px) el botón no se ve ni se puede usar, pese a estar presente en el HTML de las tres páginas.
- **`styles.css`, mismo bloque**: no se define ninguna forma circular para el botón (sin `border-radius: 50%` ni `background-color` sobre el `<a>` o el ícono SVG). Solo se fija `color` sobre el trazo del ícono. No cumple con "flecha apuntando hacia arriba dentro de un círculo" pedido en el enunciado.
- **`styles.css`, selector `section:nth-child(2) table th` (líneas 276-279)**: la única regla aplicada a los encabezados es `padding`. No hay `background-color`, `font-weight` explícito ni otro contraste agregado por CSS; la negrita que se ve depende únicamente del estilo por defecto del navegador para `<th>`, no de una regla propia del alumno.
- **`contacto.html` / `styles.css`**: el resto del formato de tabla (bordes vía `border="1"` + `border-collapse: collapse`, padding en `td`) está correcto y es legible.
- Verificación en vivo (GitHub Pages): la URL responde correctamente y el contenido coincide con el repo clonado en `laboratorio_4` (título, `h1`, nav de 3 enlaces, logo, estructura del formulario y columnas de la tabla "Resumen de Datos", y el ancla `#top` presente en el markup servido).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 3 |
| Tabla `contacto.html` | 12 | 10 |
| Formulario `contacto.html` | 12 | 12 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 12 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 7 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **91** |
