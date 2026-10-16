# Devolución Lab 4 — Carla Tirado Moreira

## Datos identificatorios

- **Token:** tiradomoreira-5676-19
- **GitHub Pages:** https://carlatmoreira98.github.io/peylw-2026-practicos-tiradomoreira-5676-19/
- **Repositorio:** https://github.com/carlatmoreira98/peylw-2026-practicos-tiradomoreira-5676-19

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(0, 65%, 45%)` como primario, modulado (S/L moderados), no es un color puro sin modular. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera (líneas 2-10) incluye alumna, token y los tres HSL (primario/fondo/texto). |
| Tabla de `contacto.html` formateada | ✅ | Bordes, padding 12px, encabezado `th` con fondo e color de contraste, filas alternadas. |
| Formulario de `contacto.html` formateado | ✅ | Inputs con padding/ancho consistente, labels con `for`/`id` correctos, radios/checkboxes agrupados en `div` sin superposición. |
| Fuente web importada y aplicada | ⚠️ | `@import` de Montserrat presente y `font-family` aplicado en `body`, pero el `@import` **no se ejecuta en el navegador** por el bug descripto en Observaciones (fences de Markdown al inicio/fin de `styles.css`). El fallback `sans-serif` sí es correcto. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo-curza">` después del `<h1>` dentro de `header` (flex), queda a la derecha. |
| Animación de giro completo (360°) del logo | ✅ | `transition: transform 1s ease-in-out` + `:hover { transform: rotateY(360deg) }`. Termina en 360° (visualmente idéntico a 0°), orientación correcta. Disparada por hover, variante admitida por la consigna. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top:0 }` en `styles.css` compartido por las 3 páginas; `nav { margin-top: 85px }` compensa la altura del header para que el contenido no quede tapado. |
| "Acerca de" — primera línea sticky | ✅ | `<h2 class="titulo-sticky">` con `position: sticky; top:0` dentro de `article.biografia`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height: 300px; overflow-y: auto }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente al final del `<body>` en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `.volver-inicio`: `border-radius: 50%`, 45×45px, `position: fixed; bottom/right`, carácter `▲`. |
| Botón volver arriba — funcional | ✅ | `href="#top"` + `<body id="top">` + `scroll-behavior: smooth` en `html`. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en el `<head>` de las 3 páginas. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display:flex }`, `form { display:flex; flex-direction:column }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `nav ul { flex-direction: column }` y `table { display:block; overflow-x:auto }` dentro del `@media (max-width: 768px)`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ⚠️ | Solo responde preguntas 1 y 2. Falta la pregunta 3 (cambio visual en pantallas <768px). El fragmento citado en la pregunta 1 sí coincide con el CSS real del proyecto. |

## Observaciones puntuales

1. **Bug sistemático — delimitadores de bloque de código Markdown commiteados dentro de los archivos fuente.** Los cuatro archivos de código (`styles.css`, `index.html`, `acercade.html`, `contacto.html`) tienen literalmente la línea `` ```css `` o `` ```html `` como primera línea del archivo, y `` ``` `` como última (confirmado con `cat -A`: `` ```css$ `` en la línea 1 de `styles.css`, `` ``` `` sin salto de línea al final). Esto no es un problema cosmético, tiene efectos reales de parseo:
   - **En `styles.css`:** según el algoritmo de recuperación de errores de CSS Syntax, el navegador interpreta los backticks iniciales como el comienzo de una regla cuyo selector (prelude) se extiende hasta la primera `{` real del archivo. Esa regla inválida "se traga" todo lo que hay en el medio — incluido el `@import url(.../Montserrat...)` de la línea 12 — porque un `@import` dentro del prelude de una regla no se procesa como at-rule independiente, queda como texto de selector. Resultado verificable: **la fuente Montserrat nunca se importa realmente**, aunque la línea esté en el archivo y el `font-family` esté bien declarado en `body`. También se pierde el reset `* { box-sizing: border-box; }` por el mismo motivo.
   - **En los HTML:** el `<!DOCTYPE html>` deja de ser el primer token del documento (lo precede el texto `` ```html ``), por lo que el navegador lo descarta como error de parseo (las tres páginas quedan en quirks mode) y el texto literal `` ```html `` se inserta como nodo de texto al inicio del `<body>` en las tres páginas. Las etiquetas `<meta>`/`<link>`/`<title>` del `<head>` se siguen procesando correctamente (el parser las redirige aunque el contexto esté roto), así que la metaetiqueta viewport y la hoja de estilos no se ven afectadas.
   - Se confirmó que GitHub Pages sirve los archivos tal cual (no hay build step), por lo que el defecto está también en el sitio publicado, no solo en el repositorio.
   - Esto es consistente con haber copiado una respuesta de un asistente de IA (bloque de código con fences) directamente al archivo fuente sin eliminar las marcas `` ``` `` antes de guardar.

2. **`REFLEXION.md`** (raíz del repositorio): falta la respuesta a la tercera pregunta de la sección "Reflexión Aplicada — Prevención de Copias" (qué cambio visual ocurre en pantallas menores a 768px). Solo están presentes las respuestas 1 y 2.

3. **Fecha de entrega — inconsistencia a señalar.** `entregas.md` registra "Fecha de Entrega: 2026-09-13", que es **anterior a la apertura oficial del Lab 4** (21/09/2026 00:00) y coincide con las fechas de los commits del TP2 (`5070b0c`, `166b8ea`, `ed5d046`, todos del 13/09/2026). Es razonable asumir que la alumna reutilizó la carátula de una entrega anterior sin actualizar la fecha, más que un intento de encubrir una entrega tardía. El commit real del TP4 es `8f4f651`, fechado **2026-10-10 23:01:10 -0300** — es decir, **70 segundos después del cierre oficial** (10/10/2026 23:00, mismo huso horario que el commit). Queda al límite justo del cierre; se señala para que quien aplique el criterio general de tardanza del curso lo tenga en cuenta, sin que este informe determine la penalización.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 12 |
| Formulario `contacto.html` | 12 | 12 |
| Fuente web | 8 | 3 |
| Animación título + logo | 12 | 12 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 4 |
| **TOTAL** | **100** | **94** |

El descuento principal es en Fuente web (3/8): el código declara e importa Montserrat correctamente a simple vista, pero el `@import` no llega a ejecutarse en el navegador por el bug de los fences de Markdown dejados en `styles.css` (ver Observación 1), por lo que en la práctica el sitio no muestra la tipografía importada. En `REFLEXION.md` se descuenta 1 punto por la pregunta 3 faltante.
