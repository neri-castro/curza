# Devolución Lab 4 — Marité Bastías

## Datos identificatorios

- **Token:** bastias-1018-59
- **GitHub Pages:** https://marite28.github.io/peylw-2026-practicos-bastias-1018-59/ (URL pública inferida; la entregada por el alumno fue la de configuración, ver observaciones)
- **Repositorio:** https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(222, 47%, 32%)` como primario, modulado, no es color puro. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Presente en la cabecera de `styles.css` (líneas 1-9) con los 4 colores y el nombre/token, pero quedaron corchetes de plantilla sin completar y el token está mal tipeado (ver observaciones). |
| Tabla de `contacto.html` formateada | ✅ | Bordes (`border-bottom`), padding consistente (`0.7rem 1rem`) y encabezado diferenciado (`thead th` con fondo `var(--primario)` y texto blanco). |
| Formulario de `contacto.html` formateado | ⚠️ | Campos y labels con tamaño/padding consistentes y alineados por grid. El formulario actual no tiene ningún grupo de radios/checkboxes para evaluar ese sub-ítem (ver observaciones: se perdió el formulario del TP3, que sí los tenía). |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts ("Outfit") aplicada en `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo-curza">` ubicado después del `<h1>` dentro de `.titulo-cabecera` (flex), en las tres páginas. |
| Animación de giro completo (360°) del logo | ✅ | `transition: transform 1s ease-in-out` + `:hover { transform: rotateY(360deg) }`. Mecanismo de transición disparada (permitido por el enunciado como alternativa a `@keyframes`); no se dispara automáticamente al cargar la página, solo con `:hover`. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top: 0; }` en `styles.css`, compartido por `index.html`, `acercade.html` y `contacto.html`. Compensación con `padding-top: calc(var(--alto-header) + 1.5rem)` en `main`. |
| "Acerca de" — primera línea sticky | ✅ | `.caja-biografia h2 { position: sticky; top: 0; background-color: var(--fondo); z-index: 10; }`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.caja-biografia { max-height: 300px; overflow-y: auto; }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="volver-arriba">` en las tres páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius: 50%`, `position: fixed; bottom: 20px; right: 20px;`, carácter `&#9650;` (▲). |
| Botón volver arriba — funcional | ✅ | Ancla a `#top` (presente en `<body id="top">` de las tres páginas) combinada con `html { scroll-behavior: smooth }`. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display: flex }` y `form { display: grid; grid-template-columns: 140px 1fr }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width: 768px)` apila `nav ul` (`flex-direction: column`) y la tabla queda en `.contenedor-tabla { overflow-x: auto }` con `min-width: 480px` para no romper el ancho. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ⚠️ | Las 3 respuestas están completas y el fragmento de CSS citado coincide exactamente con el real, pero el archivo se llama `reflexion.md` (minúsculas) y no `REFLEXION.md`. El `REFLEXION.md` que sí existe en el repo conserva contenido viejo de un TP anterior (git status/staging area), no las respuestas de este TP. |

## Observaciones puntuales

- **URL de entrega incorrecta**: el alumno entregó `https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59/settings/pages`, que es la URL de **configuración** de GitHub Pages dentro del repositorio, no la URL pública del sitio. Se verificó con WebFetch que esa URL devuelve **404** para un visitante no autenticado. La URL pública real, inferida a partir del patrón `https://<usuario>.github.io/<repo>/`, es `https://marite28.github.io/peylw-2026-practicos-bastias-1018-59/`, y esa sí responde 200 con contenido que coincide con el repositorio (`index.html` y `contacto.html` verificados). Este es un error de entrega que debe registrarse aparte del contenido técnico.
- **Cabecera de `styles.css` (líneas 1-9)**: quedaron corchetes de plantilla sin reemplazar, `[Marité Bastías]` y `[bastias1018-59]`, y el token tiene un error de tipeo (falta un guion: `bastias1018-59` en vez de `bastias-1018-59`).
- **`contacto.html` perdió contenido del TP3**: el commit `6464201 "Add files via upload"` reemplazó por completo el `contacto.html` del TP3 (commit `8347ed4`), que tenía dos `<fieldset>` con radios ("Método de contacto preferido") y checkboxes ("Suscripciones de interés"), `datalist` de provincias, validación por `pattern` de código postal, y una tabla de "Resumen de datos". La versión actual del formulario solo tiene `input` de texto/email, un `select` y un `textarea`: no quedó ningún grupo de radios/checkboxes, lo cual impide evaluar ese sub-ítem del formulario como cumplido.
- **`acercade.html` perdió contenido del TP2**: se descartaron el `<figure>`/`<figcaption>` con la imagen `img/Danza.jpg` (que además fue eliminada del repositorio) y la lista `<ul>` de tecnologías (HTML, CSS, JavaScript, Python, SQL), reemplazados por un único `<article>` con párrafos de biografía nuevos.
- **`index.html` perdió contenido del TP1/TP2**: el texto personal sobre danza folclórica y repostería fue reemplazado por un texto de bienvenida genérico sobre el portal.
- El enunciado de este TP pide "modificar las páginas creadas hasta el momento" (TP es de estilos y posicionamiento sobre lo existente), no reescribirlas. Los tres reemplazos de contenido señalados arriba exceden ese alcance; no se penalizan con un ítem de rúbrica propio, pero sí redujeron directamente lo evaluable en el formulario.
- **Dos archivos de reflexión**: `REFLEXION.md` (mayúsculas) quedó con contenido de un TP anterior (salida de `git status`, diferencia staging/working directory); las 3 respuestas de este TP están en un archivo nuevo `reflexion.md` (minúsculas). El contenido de las respuestas es correcto y el fragmento de CSS citado en la pregunta 1 coincide textualmente con el bloque real de `styles.css` (`transition` + `:hover { transform: rotateY(360deg) }`).
- La animación del logo se dispara solo con `:hover`, no automáticamente al cargar la página; es una alternativa válida según el enunciado pero no se pudo verificar interactivamente en vivo porque el método de verificación usado en esta corrección fue código + reachability por WebFetch, sin navegador.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 12 |
| Formulario `contacto.html` | 12 | 8 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 12 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 4 |
| **TOTAL** | **100** | **95** |
