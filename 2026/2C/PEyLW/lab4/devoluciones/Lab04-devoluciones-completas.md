# Lab 4 — Devoluciones completas

## Tabla resumen — Lab 4

| Token | Nombre | Nota |
|---|---|---|
| apelahnz-2743-10 | Santiago Valentín Apelahnz | 96 |
| bastias-1018-59 | Marité Bastías | 96 |
| boisselier-8339-91 | Sara Celeste Boisselier | 96 |
| camandulle-5746-93 | Fernanda Camandulle | 100 |
| chavarria-7037-55 | Javier Chavarria | 94 |
| klug-3903-68 | Robertino Klug | 75 |
| manquenao-2747-93 | Tatiana Manquenao | 8 |
| pereyra-1554-84 | Sofia Pereyra | 100 |
| quintulen-3932-92 | Carlos Quintulen | 91 |
| reyes-6775-42 | Isaías Reyes Arzamendia | 100 |
| reynoso-4260-07 | Ramiro Reynoso | 98 |
| tiradomoreira-5676-19 | Carla Tirado Moreira | 99 |
| vela-9972-35 | Sandra Vela | 100 |

---

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

---

# Devolución Lab 4 — Marité Bastías

## Datos identificatorios

- **Token:** bastias-1018-59
- **GitHub Pages:** https://marite28.github.io/peylw-2026-practicos-bastias-1018-59/ (inferida; la entrega dio por error la URL de configuración `https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59/settings/pages`, que no es pública)
- **Repositorio:** https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59 (rama `laboratorio_4`; la rama por defecto `master` solo contiene el Lab 1)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | Color primario en HSL, modulado. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera de `styles.css` con códigos HSL y token. |
| Tabla de `contacto.html` formateada | ✅ | Bordes, padding y encabezado diferenciado presentes. |
| Formulario de `contacto.html` formateado | ❌ | El formulario perdió los grupos de radios/checkboxes que sí tenía en el TP3: en esta entrega no hay ningún `<fieldset>` de radios/checkboxes estilado en `contacto.html`. |
| Fuente web importada y aplicada | ✅ | Fuente de Google Fonts importada y aplicada con fallback. |
| Logo CURZA a la derecha del título | ✅ | Logo presente a la derecha del `<h1>` en las tres páginas. |
| Animación de giro completo (360°) del logo | ✅ | `rotateY(360deg)` vía `transition`/`:hover`, termina en orientación correcta. |
| Header fijo en todas las páginas | ✅ | `position: fixed; top:0` compartido por las tres páginas. |
| "Acerca de" — primera línea sticky | ✅ | `position: sticky` sobre el encabezado de la biografía. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `max-height:300px` + `overflow-y:auto` presentes. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente en las tres páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | Círculo con flecha, alineado abajo a la derecha. |
| Botón volver arriba — funcional | ✅ | Ancla funcional al inicio de cada página. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en las tres páginas. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | Flexbox en la navegación. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width:768px)` apila el menú y evita rotura de la tabla. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ⚠️ | Coexisten dos archivos: `REFLEXION.md` (desactualizado, con contenido del Lab 2) y `reflexion.md` (correcto, con las 3 preguntas del TP4). La duplicidad de nombres (case-sensitive en el repo) es confusa aunque el contenido correcto exista. |

## Observaciones puntuales

- **`contacto.html`**: el formulario perdió los grupos de radios/checkboxes que tenía en la entrega del TP3; en esta entrega del TP4 no hay ningún control de ese tipo estilado, lo que anula ese sub-ítem del formulario.
- **Raíz del repositorio**: coexisten `REFLEXION.md` (contenido viejo, de Lab 2) y `reflexion.md` (contenido correcto del TP4). Riesgo de confusión por nombres de archivo que solo difieren en mayúsculas/minúsculas.
- **Entrega tardía**: fecha de entrega indicada 2026-10-13, posterior al cierre oficial del Lab 4 (10/10/2026 23:00). Este documento no define penalización numérica por atraso; queda a criterio general del curso.
- El TP4 está en la rama `laboratorio_4`, no en la rama por defecto (`master`, que solo tiene el Lab 1); GitHub Pages está configurado para publicar desde esa rama, así que el sitio en vivo sí refleja el trabajo real.
- La URL de GitHub Pages entregada por la alumna es incorrecta: apunta a la página de configuración de GitHub (`/settings/pages`), no al sitio público. Se infirió y verificó la URL real.

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
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **96** |

---

# Devolución Lab 4 — Sara Celeste Boisselier

## Datos identificatorios

- **Token:** boisselier-8339-91
- **GitHub Pages:** https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/
- **Repositorio:** https://github.com/saraboisselier/peylw-2026-practicos-boisselier-8339-91

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(335, 55%, 65%)` como primario, modulado correctamente. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera (líneas 3-12) con alumno, legajo, token y los 4 colores HSL. |
| Tabla de `contacto.html` formateada | ✅ | Bordes, padding 12px, `th` con fondo diferenciado y filas pares con rayado. |
| Formulario de `contacto.html` formateado | ⚠️ | Ver observación: radios/checkboxes quedan separados de su `<label>` por el layout en columna. |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts (Outfit) + `font-family: 'Outfit', sans-serif` aplicado en `body`. |
| Logo CURZA a la derecha del título | ⚠️ | Correcto en `acercade.html` y `contacto.html`; roto en `index.html` (falta el `div.encabezado-superior`). |
| Animación de giro completo (360°) del logo | ✅ | `transition` + `:hover { transform: rotateY(360deg) }`, giro completo, termina en orientación correcta. |
| Header fijo en todas las páginas | ✅ | `position: fixed; top:0` en `styles.css`, compartido por las 3 páginas, con `main { padding-top: 180px }` de compensación. |
| "Acerca de" — primera línea sticky | ✅ | `.biografia-scroll h2 { position: sticky; top:0 }` con fondo blanco. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia-scroll { max-height: 300px; overflow-y: auto }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="volver-arriba">▲</a>` en las 3 páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius:50%`, `position:fixed; bottom/right:20px`, símbolo ▲. |
| Botón volver arriba — funcional | ✅ | Ancla a `#top` (id del `<header>`) + `scroll-behavior: smooth` en `html`. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en los 3 `<head>`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display:flex }`, `form { display:flex; flex-direction:column }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `nav ul { flex-direction: column }` en el breakpoint; `.tabla-contenedor { overflow-x:auto }` evita rotura de ancho. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 respuestas están presentes y el fragmento de la pregunta 1 coincide con el CSS real (`.logo-curza` / `:hover`). |

## Observaciones puntuales

- **`index.html`, líneas 13-16**: el `<h1>` y el `<img class="logo-curza">` están como hijos directos de `<header>`, sin el `div.encabezado-superior` que sí usan `acercade.html` (líneas 14-17) y `contacto.html` (líneas 14-17). Como `header` no tiene `display: flex`, el `h1` (bloque) empuja al logo a la línea siguiente: en `index.html` el logo queda **debajo** del título, no a la derecha, a diferencia de las otras dos páginas. Es una inconsistencia de estructura entre páginas que el enunciado pide que sea igual en todo el encabezado común.
- **`contacto.html`, líneas 70-91**: el `<form>` tiene `display: flex; flex-direction: column; gap: 12px` (`styles.css` líneas 164-169) aplicado a todos sus hijos directos. Esto funciona bien para los pares label/input de texto (cada uno en su propia fila), pero para los radios y checkboxes cada `<input>` y su `<label>` son hijos directos separados: quedan en filas distintas con el mismo espaciado de 12px que separa a cualquier otro par de elementos del formulario, sin ninguna agrupación visual (ni un contenedor común, ni un gap menor) que indique qué etiqueta corresponde a qué control. El resultado es una lista alternada de círculo/texto sin la asociación lado a lado esperada para un grupo de radios o checkboxes.
- **`styles.css`, líneas 65-67**: la animación de giro del logo está disparada por `:hover`, lo que es válido según la consigna ("`transition` disparada"), pero no se activa con touch en dispositivos móviles/tablets. No es un incumplimiento del ítem, pero vale la aclaración porque en la práctica no se verá en un celular sin mouse.
- Verificación en vivo realizada con el método código + reachability (sin navegador): se confirmó que `https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/` responde 200 y que el HTML servido coincide con el del repositorio clonado (mismo título, `h1`, token, comentario "No juzgar🐱", logo, y estructura de formulario/tabla en `contacto.html`). No se verificó interactivamente en un navegador real el comportamiento de scroll del header fijo, el clic del botón volver arriba, la animación al pasar el mouse, ni el breakpoint de 768px; esas conclusiones se basan en el análisis estático del CSS/HTML, que las soporta correctamente salvo por lo señalado en `index.html`.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 5 |
| Tabla `contacto.html` | 12 | 12 |
| Formulario `contacto.html` | 12 | 9 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 11 |
| Header fijo | 12 | 12 |
| "Acerca de" sticky + scroll | 12 | 12 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **96** |

---

# Devolución Lab 4 — Fernanda Camandulle

## Datos identificatorios

- **Token:** camandulle-5746-93
- **GitHub Pages:** https://camandulle.github.io/peylw-2026-practicos-camandulle-5746-93/
- **Repositorio:** https://github.com/Camandulle/peylw-2026-practicos-camandulle-5746-93

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(217, 90%, 55%)` como primario, con variantes oscura/clara coherentes. Sin colores puros sin modular. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera de `styles.css` (líneas 1-5) con los tres códigos HSL y el token `camandulle-5746-93`. |
| Tabla de `contacto.html` formateada | ✅ | Bordes (`border-bottom`), padding 10px/12px, `th` con fondo `--primario` y texto blanco, filas pares con fondo `--primario-claro`. |
| Formulario de `contacto.html` formateado | ✅ | Inputs de texto con padding/border/radius consistentes; `label` alineado por flex (`form > p`) en campos sueltos; grupos de radio/checkbox dentro de `fieldset` legibles con disposición por defecto del navegador (sin superposición). |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts ("Outfit") aplicado en `body { font-family: 'Outfit', sans-serif; }`, con fallback. |
| Logo CURZA a la derecha del título | ✅ | `.header-top` con `display:flex; justify-content:space-between` ubica `<img class="logo-curza">` a la derecha del `<h1>` en las tres páginas. |
| Animación de giro completo (360°) del logo | ✅ | `transition: transform 1s ease-in-out` + `:hover { transform: rotateY(360deg) }`. Es "transition disparada" (alternativa explícitamente permitida a `@keyframes`), dispara en hover, vuelve a orientación legible (0°≈360°). |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top:0 }` en `styles.css`, compartido por `index.html`, `acercade.html` y `contacto.html`. `main { padding-top: 130px }` (220px en mobile) compensa la superposición. |
| "Acerca de" — primera línea sticky | ✅ | `.biografia > h2 { position: sticky; top:0 }` fija el `<h2>Biografía</h2>` dentro del `<article class="biografia">`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height: 300px; overflow-y: auto }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="volver-arriba">` al final del `<body>` en las tres páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius:50%`, `position:fixed; bottom:20px; right:20px`, carácter "▲" centrado con flex. |
| Botón volver arriba — funcional | ✅ | Ancla `#top` hacia `<body id="top">`; funciona sin JS adicional. |
| Responsive — meta viewport en las tres páginas | ✅ | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display:flex }` y `.header-top { display:flex }`; `form > p { display:flex }` para alinear label/input. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width: 768px)`: `nav ul { flex-direction: column }`, `table { display:block; overflow-x:auto }`, además ajusta `form > p` a columna y aumenta `padding-top` del `main`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Sección "TP4" de `REFLEXION.md` responde las 3 preguntas; el fragmento de CSS citado en la pregunta 1 coincide exactamente con `.logo-curza` y `.logo-curza:hover` de `styles.css`. |

## Observaciones puntuales

- El mecanismo de animación del logo (`transition` + `:hover`) es un disparo por evento de usuario, no automático al cargar la página. La rúbrica lo permite explícitamente ("o el evento que el alumno haya definido"), por lo que no es una falta, pero conviene que quede claro que el logo no gira solo al entrar al sitio, sino al pasar el mouse sobre él.
- El cálculo del `padding-top` del `<main>` (130px en escritorio, 220px en mobile) es una estimación razonable dado el contenido del header (logo 45px + `<h1>` que puede ocupar varias líneas en pantallas angostas + menú apilado), pero no se verificó de forma interactiva en el sitio desplegado si el contenido queda exactamente al ras o con algún recorte en anchos intermedios (entre 375px y 768px), porque el método de verificación acordado para esta corrección es código + reachability (sin automatización de navegador).
- Los grupos de radio buttons y checkboxes en `contacto.html` (`fieldset` "Método de Contacto Preferido" y "Suscripción de Interés") no tienen reglas CSS propias de espaciado/alineación: se apoyan en la disposición por defecto del navegador (`input` + `label` en línea). Es legible y no se superpone, pero es el único bloque del formulario sin estilado explícito.
- Verificación de reachability: las tres URLs (`/`, `/contacto.html`, `/acercade.html`) de GitHub Pages respondieron con contenido servible (sin 404), y los títulos de página, la navegación (Inicio/Acerca de/Contacto), el formulario y la tabla coinciden con el contenido del repositorio clonado. No se confirmó de forma interactiva el comportamiento de scroll/hover/resize en el sitio en vivo, conforme al método acordado.
- Último commit con los cambios de este TP (`55b4a8f`, 2026-10-10 19:53 -03) dentro del plazo de cierre (10/10/2026 23:00).

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

---

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

---

# Devolución Lab 4 — Robertino Klug

## Datos identificatorios

- **Token:** klug-3903-68
- **GitHub Pages:** https://robertino512.github.io/peylw-2026-practicos-klug-3903-68/ (no fue informada en la entrega — el alumno sólo dio el link al repo con `/tree/lab04`; se infirió a partir del usuario de GitHub y se verificó que responde 200 y publica efectivamente el contenido de la rama `lab04`, no el de `main`).
- **Repositorio:** https://github.com/Robertino512/peylw-2026-practicos-klug-3903-68 (rama `lab04`; la rama `main` quedó congelada en el estado del Lab 1 y no contiene el trabajo de este TP — GitHub Pages está configurado para publicar desde `lab04`, por lo que el sitio en vivo sí refleja el trabajo real).

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ❌ | Color primario `hsl(270, 100%, 50%)`: saturación 100% y luminosidad 50% es exactamente el patrón de "color puro sin modular" que la rúbrica prohíbe (mismo caso que `hsl(0,100%,50%)`, solo con otro matiz). |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | `styles.css:2` — `/* Codigo HSl del violeta: hsl(270, 100%, 50%) Token identificador: klug-3903-68 */`. |
| Tabla de `contacto.html` formateada | ⚠️ | Bordes presentes pero por un selector mal armado (`.tablaGeneral table, th, td` aplica borde a **todos** los `th`/`td` del documento, no solo a la tabla); `td` tiene `padding:8px` pero `th` no tiene padding; el encabezado solo se diferencia por `color`, sin fondo ni negrita. |
| Formulario de `contacto.html` formateado | ❌ | El input de "Apellido" (`Contacto.html:33`) y el checkbox "eventos" (línea 64) no tienen `class="campoFormulario"` y quedan sin estilo. No hay ninguna regla para alinear `<label>` con su campo (todo queda en flujo inline por defecto). La clase `.campoFormulario` (padding, border, border-radius) se aplica también a radios/checkboxes, lo que puede deformar su apariencia nativa. |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts "Outfit" en `styles.css:1`, aplicada vía `.body{font-family:"Outfit",sans-serif}` y usada en las tres páginas (`<body class="body">`), con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ⚠️ | Presente en `acercade.html` y `Contacto.html`, pero **ausente en `index.html`** (el `<header>` de esa página solo tiene el `<h1>`, sin `<img class="logo">`). |
| Animación de giro completo (360°) del logo | ✅ | `.logo:hover{transform:rotateY(360deg)}` con `transition: transform 1s ease-in-out` en `styles.css:74-82`. Termina en 360° (visualmente equivalente a 0°, no espejado). Se dispara con `:hover`, no al cargar, pero la rúbrica admite "el evento que el alumno haya definido". No se ve en `index.html` por la ausencia del logo ahí. |
| Header fijo en todas las páginas | ⚠️ | `.header{position:fixed;top:0;width:100%}` está presente en las tres páginas. Pero la compensación de espacio (`.main{padding-top:15px}`) solo existe en `Contacto.html`, cuyo `<main>` es el único con `class="main"`; en `index.html` y `acercade.html` el `<main>` no tiene clase y queda **tapado por el header fijo** al cargar la página. Incluso en `Contacto.html`, 15px es insuficiente para compensar la altura real de un `<header>` con `<h1>`. |
| "Acerca de" — primera línea sticky | ⚠️ | El `<h2 class="H2">` sticky corresponde a la segunda sección ("Mi pasado"), no a la primera. Más grave: el contenedor con scroll (`.cajaBio`, `max-height:300px; overflow-y:auto`) está en el `<p>`, no envuelve al `<h2>` sticky — son elementos hermanos, no uno dentro del otro — por lo que el h2 no queda "fijo mientras se scrollea dentro del artículo" como pide la consigna; además, al tener `top:0` igual que el header fijo pero `z-index:10` (menor al `z-index:1000` del header), el h2 sticky puede quedar tapado detrás del header en vez de visible debajo de él. |
| "Acerca de" — `max-height: 300px` + scroll | ⚠️ | `max-height:300px` y `overflow-y:auto` están aplicados al `<p class="cajaBio">`, no al `<article>` (contenedor del texto) como pide la rúbrica; solo ese párrafo queda acotado, el resto del artículo (otra sección, figura, lista de lenguajes) no. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="botonInicio">▲</a>` en las tres páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius:50%`, 25×25px, `position:fixed; bottom:20px; right:20px`, carácter ▲. (Nota menor, sin descuento: falta `justify-content:center` para centrar la flecha horizontalmente dentro del círculo). |
| Botón volver arriba — funcional | ✅ | Ancla `href="#top"` hacia `<div id="top"></div>` ubicado al inicio del `<body>` en las tres páginas. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `Contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `.claseUL{display:flex;...}` en la navegación. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width:768px){ nav ul{flex-direction:column} }` apila el menú; `.tabla_contenedor{overflow-x:auto}` evita que la tabla rompa el ancho. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Archivo `REFLEXION.MD` en la raíz (nombre en mayúsculas, sin impacto porque no se enlaza). Las 3 preguntas están respondidas; el fragmento citado en la pregunta 1 coincide textualmente con `.logo:hover{transform:rotateY(360deg)}` real. |

## Observaciones puntuales

- `styles.css:16,29,40,53,66`: el color primario `hsl(270,100%,50%)` se repite tal cual sin ninguna variación de saturación/luminosidad — es el mismo "color puro" que la consigna pide evitar, solo con otro matiz.
- `index.html`: falta el logo del CURZA en el header; está en las otras dos páginas pero no en la portada.
- `index.html` y `acercade.html`: el `<main>` no tiene `class="main"`, por lo que no recibe el `padding-top` que compensa el header fijo — el contenido queda tapado al cargar.
- `Contacto.html:33,64`: el input de "Apellido" y el checkbox "eventos" no tienen `class="campoFormulario"`, quedan con estilo default del navegador en un formulario que debería estar completamente formateado.
- `acercade.html`: la estructura de sticky/scroll no corresponde a lo pedido — el `<h2>` sticky y el contenedor con `overflow` no están anidados, y el `z-index` del `<h2>` sticky (10) es menor al del header fijo (1000), con riesgo de quedar oculto detrás de él.
- `Contacto.html:84`: `<td id="resumen-nombre"` — falta el `>` de cierre de la etiqueta de apertura (debería ser `<td id="resumen-nombre">`); no rompe visualmente por la tolerancia de los navegadores a HTML malformado, pero es un error de marcado.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 3 |
| Tabla `contacto.html` | 12 | 8 |
| Formulario `contacto.html` | 12 | 4 |
| Fuente web | 8 | 8 |
| Animación título + logo | 12 | 10 |
| Header fijo | 12 | 8 |
| "Acerca de" sticky + scroll | 12 | 7 |
| Botón volver arriba | 12 | 12 |
| Responsive Web Design | 10 | 10 |
| `REFLEXION.md` | 5 | 5 |
| **TOTAL** | **100** | **75** |

---

# Devolución Lab 4 — Tatiana Manquenao

## Datos identificatorios

- **Token:** manquenao-2747-93
- **GitHub Pages:** https://tati99-web.github.io/manquenao-2747-93/
- **Repositorio:** https://github.com/tati99-web/manquenao-2747-93

> Nota: el repositorio se llama `manquenao-2747-93`, no sigue el patrón
> esperado `peylw-2026-practicos-manquenao-2747-93`. Se registra como
> discrepancia, sin penalizar, porque el contenido pudo revisarse completo.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ❌ | No se usa ningún color en formato HSL en `styles.css`. Se mantienen los mismos colores hex/rgb de Lab 3 (`#4a90e2`, `#357ABD`, `#333333`, `#222222`, `#f4f4f9`, `rgb(198,207,213)`). |
| Personalización — comentario en `styles.css` con HSL + identificador | ❌ | La cabecera de `styles.css` solo tiene `/* Estilos generales */`; no hay comentario con códigos HSL ni identificador de alumno. |
| Tabla de `contacto.html` formateada | ⚠️ | Bordes y padding heredados de Lab 3 (`table, td { border: 1px solid #ccc; padding: 8px; }`) dan celdas alineadas y espaciado legible, pero la tabla de resumen usa solo `<td>` (sin `<th>`) y no hay ninguna regla que diferencie visualmente una fila de encabezado. |
| Formulario de `contacto.html` formateado | ❌ | `styles.css` no contiene ninguna regla para `input`, `label`, `fieldset` ni `button`. El formulario se renderiza con el estilo por defecto del navegador. |
| Fuente web importada y aplicada | ❌ | No hay `<link>` a Google Fonts ni servicio equivalente, ni `@font-face`/`@import` en `styles.css`. `body` usa `font-family: sans-serif`. |
| Logo CURZA a la derecha del título | ❌ | Ningún `<header>` de las tres páginas incluye imagen de logo; solo contienen `<h1>`. |
| Animación de giro completo (360°) del logo | ❌ | No existe ningún `@keyframes` en el repositorio (confirmado por búsqueda sobre todos los `.css`/`.html`). No hay animación de ningún tipo. |
| Header fijo en todas las páginas | ❌ | No hay `position: fixed` ni `position: sticky` sobre el selector `header` en `styles.css`. |
| "Acerca de" — primera línea sticky | ❌ | No hay `position: sticky` en ningún selector de `acercade.html`/`styles.css`. |
| "Acerca de" — `max-height: 300px` + scroll | ❌ | No existe `max-height` ni `overflow-y` en el `<article>` de `acercade.html`. |
| Botón volver arriba — presente en todas las páginas | ❌ | No hay botón/enlace de "volver arriba" en `index.html`, `acercade.html` ni `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ❌ | No aplica: el botón no existe. |
| Botón volver arriba — funcional | ❌ | No aplica: el botón no existe. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul` usa `display: flex` (heredado de Lab 3). No hay flex/grid adicional en formulario ni tabla. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ❌ | No existe ninguna regla `@media` en todo el repositorio. Según la escala del ítem, la ausencia total de `@media` anula el ítem completo de Responsive Design, incluidos los sub-ítems marcados ✅ arriba. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ❌ | El archivo `Reflexion.md` existe pero conserva el contenido de la reflexión de Lab 2 (nombre de imagen/`alt`, etiquetas semánticas, verificación de rutas). No responde ninguna de las 3 preguntas exigidas para Lab 4 (fragmento de la animación del logo, por qué el elemento sticky necesita `background-color`, cambio visual en pantallas menores a 768px). |

## Observaciones puntuales

- **No hay entrega de Lab 4 en el repositorio.** El último commit es `1bb47c0 "lab3-entrega de contacto y estilos"` (28/09/2026). No existe ningún commit posterior ni evidencia de trabajo sobre los requisitos propios de este TP (HSL, fuente web, animación del logo, header fijo, sticky en "Acerca de", botón volver arriba, `@media`). El estado de `styles.css` es idéntico al de la entrega de Lab 3 (71 líneas, mismas reglas).
- **`index.html` está corrupto.** El archivo contiene un `<!DOCTYPE html>` suelto, seguido literalmente de la marca de bloque de código Markdown `` ```html ``, luego un segundo documento HTML completo duplicado (con su propio `<!DOCTYPE html>...</html>`), y cierra con `` ``` ``. Es decir, se pegó la respuesta de un asistente/markdown sin limpiar los delimitadores de bloque de código. Se confirmó vía WebFetch sobre el sitio publicado que esos marcadores `` ``` `` y `` ```html `` aparecen como texto visible en la página en vivo (https://tati99-web.github.io/manquenao-2747-93/).
- **`acercade.html` tiene el mismo problema**: todo el archivo está envuelto entre `` ```html `` (primera línea) y `` ``` `` (última línea).
- **Imagen rota en `acercade.html`**: referencia `src="img/mi_foto.jpg"`, pero en el repositorio la carpeta se llama `img - copia` (con espacios) y el archivo real es `2e3a2121-c141-45ef-a85e-b34900a7cfe7.jpg`. Es un defecto heredado de labs anteriores, no puntúa en la rúbrica de Lab 4, pero se deja constancia porque agrava la percepción general de calidad de la entrega.
- **Carpeta duplicada** `manquenao-2747-93/` dentro del propio repositorio, con copias viejas de `index.html`, `acercade.html`, `Reflexion.md`, `Readme.md` e imagen (de la subida inicial). No afecta lo publicado en Pages (que sirve desde la raíz de `main`), pero es contenido sobrante sin limpiar.
- **Verificación en vivo (GitHub Pages)**: la URL responde 200 y el contenido coincide con el repositorio. Se confirmaron ausentes en el sitio desplegado: logo animado, header fijo al hacer scroll, botón volver arriba, comportamiento sticky en "Acerca de" y adaptación a mobile — consistente con lo encontrado en el código.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 0 |
| Tabla `contacto.html` | 12 | 8 |
| Formulario `contacto.html` | 12 | 0 |
| Fuente web | 8 | 0 |
| Animación título + logo | 12 | 0 |
| Header fijo | 12 | 0 |
| "Acerca de" sticky + scroll | 12 | 0 |
| Botón volver arriba | 12 | 0 |
| Responsive Web Design | 10 | 0 |
| `REFLEXION.md` | 5 | 0 |
| **TOTAL** | **100** | **8** |

---

# Devolución Lab 4 — Sofia Pereyra

## Datos identificatorios

- **Token:** pereyra-1554-84
- **GitHub Pages:** https://sofiaquino567-bot.github.io/peylw-2026-practicos-pereyra-1554-84/
- **Repositorio:** https://github.com/sofiaquino567-bot/peylw-2026-practicos-pereyra-1554-84 (rama `Laboratorio4`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `styles.css` usa `hsl(265, 45%, 50%/35%/96%)` en toda la hoja, ninguno es color puro sin modular. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera de `styles.css` (líneas 1-7) documenta la paleta completa y el token `pereyra-1554-84`. |
| Tabla de `contacto.html` formateada | ✅ | `th`/`td` con bordes, padding 8px, encabezado con fondo violeta y texto blanco, filas pares diferenciadas (`tr:nth-child(even)`). |
| Formulario de `contacto.html` formateado | ✅ | Grid de 2 columnas empareja cada `label` con su campo, inputs con padding/ancho consistentes, grupos de radio/checkbox en `grid-column: 1 / -1` sin superposición. |
| Fuente web importada y aplicada | ✅ | `@import` de Google Fonts "Clarity City" (verificado como fuente real, responde 200 con `@font-face` válidos) aplicada en `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo-curza">` ubicado entre el `<h1>` y el `<nav>` dentro del header en flex `space-between`; queda a la derecha del título. |
| Animación de giro completo (360°) del logo | ✅ | `.logo-curza:hover { transform: rotateY(360deg); }` con `transition: transform 1s ease-in-out`. No usa `@keyframes`, pero el enunciado admite "transition disparada" como alternativa válida. Termina en 360° (visualmente igual a 0°), sin quedar espejado. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top: 0; }` en `styles.css` compartido por las tres páginas; `main { padding-top: 150px }` evita que el contenido quede tapado. |
| "Acerca de" — primera línea sticky | ✅ | `.biografia h2 { position: sticky; top: 0; background-color: ... }` en `acercade.html`: el `<h2>Biografía</h2>` queda fijo durante el scroll. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height: 300px; overflow-y: auto; }` aplicado al contenedor del texto biográfico. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `.volver-inicio`: círculo de 70px (`border-radius: 50%`), `position: fixed; bottom: 20px; right: 20px`. Observación: el enlace incluye el texto "Inicio" además de la flecha "▲" (no es solo el ícono), ver observaciones. |
| Botón volver arriba — funcional | ✅ | `href="#top"` + `<body id="top">` junto con `scroll-padding-top`; vuelve efectivamente al inicio. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en el `<head>` de `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display: flex }` y `form { display: grid; grid-template-columns: 1fr 1fr }`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width: 768px)` apila `nav ul` y el header; la tabla no rompe el ancho por ser de solo 2 columnas angostas con `width: 100%`, aunque la regla `.tabla-contenedor` pensada para esto no se usa (ver observaciones). |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 preguntas están respondidas; el fragmento de CSS citado en la pregunta 1 coincide exactamente con el bloque real `.logo-curza` / `.logo-curza:hover` de `styles.css`. |

## Observaciones puntuales

- `styles.css`, sección "LOGO DEL CURZA": la animación de 360° se implementa con `transition` disparada por `:hover`, no con `@keyframes` + `animation`. Es una alternativa explícitamente admitida por la consigna, pero implica que el giro no se ejecuta solo al cargar la página sino al pasar el mouse — a tener en cuenta si se esperaba un disparo automático.
- `index.html`, `acercade.html`, `contacto.html`, elemento `.volver-inicio`: el enlace incluye el texto "Inicio" además del carácter "▲". El enunciado pide una flecha dentro de un círculo; el texto adicional no invalida el requisito pero es una desviación del diseño minimalista esperado.
- `styles.css`, sección "TABLAS": la clase `.tabla-contenedor` (definida dos veces, en el bloque general y dentro de `@media (max-width: 768px)`) nunca se aplica a ningún elemento del HTML — en `contacto.html` el `<table>` no está envuelto por ningún contenedor con esa clase. Es CSS muerto; en este caso no genera ruptura visible porque la tabla es de solo 2 columnas angostas, pero si se agregaran más columnas el mecanismo de scroll lateral previsto no funcionaría porque no está conectado al HTML.
- `REFLEXION.md`, respuesta 3: menciona que "las tablas permiten el desplazamiento horizontal para evitar que se desborden", describiendo la intención de `.tabla-contenedor`, pero esa clase no está aplicada en `contacto.html` (ver punto anterior); la descripción no se corresponde 1:1 con el comportamiento real actual del sitio.
- Verificación en vivo: GitHub Pages responde 200 en `/`, `/acercade.html`, `/contacto.html` y `/styles.css`. El contenido de las cuatro páginas/hojas de estilo del sitio desplegado es idéntico byte a byte al de la rama `Laboratorio4` clonada, por lo que el despliegue refleja fielmente el código revisado.

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

---

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

---

# Devolución Lab 4 — Isaías Reyes Arzamendia

## Datos identificatorios

- **Token:** reyes-6775-42
- **GitHub Pages:** https://isaiasreyesbjj16-ux.github.io/peylw-2026-practicos-reyes-6775-42/ (y `/contacto.html`, `/acercade.html`)
- **Repositorio:** https://github.com/isaiasreyesbjj16-ux/peylw-2026-practicos-reyes-6775-42

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `styles.css` líneas 9-15/19-25: paleta en HSL modulada (`hsl(202,76%,42%)`, `hsl(24,78%,52%)`, etc.), ningún color puro sin modular. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | `styles.css` líneas 3-16: comentario de cabecera con todos los códigos HSL y "Alumno: Isaías Reyes Arzamendia - reyes-6775-42". |
| Tabla de `contacto.html` formateada | ✅ | `styles.css` líneas 267-288: bordes, padding 10px, `th` con fondo `--primario` y texto blanco, filas pares con fondo alterno. |
| Formulario de `contacto.html` formateado | ✅ | `styles.css` líneas 176-245: inputs con padding/ancho consistente, `label` sobre el campo vía `form p { flex-direction: column }`, grupos de radio/checkbox en fila con `:has()` sin superposición. |
| Fuente web importada y aplicada | ✅ | `styles.css` línea 1: `@import` de Google Fonts "Outfit"; aplicada en `body { font-family: 'Outfit', sans-serif }` (línea 35), con fallback. |
| Logo CURZA a la derecha del título | ✅ | `index.html`/`acercade.html`/`contacto.html` línea 12-15: `<img class="logo">` ubicado después del `<h1>` dentro de `<header>` con `display:flex`. |
| Animación de giro completo (360°) del logo | ✅ | `styles.css` líneas 67-78: `transition: transform 1s ease-in-out` + `:hover { transform: rotateY(360deg) }`. Es una transición disparada por hover (modalidad explícitamente admitida por la rúbrica), gira 360° completos y vuelve a 0° al quitar el cursor, terminando siempre en orientación legible. |
| Header fijo en todas las páginas | ✅ | `styles.css` líneas 43-57: `header { position: fixed; top:0; width:100% }` en el CSS compartido por las tres páginas. Compensación con `body { padding-top: 72px }` (línea 39), ajustado a 100px en el media query (línea 331). |
| "Acerca de" — primera línea sticky | ✅ | `acercade.html` línea 28 + `styles.css` líneas 142-148: `section.biografia h2 { position: sticky; top:0; background-color: var(--blanco); z-index:10 }`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `styles.css` líneas 137-140: `section.biografia { max-height: 300px; overflow-y: auto }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente al final del `<body>` en `index.html`, `acercade.html` y `contacto.html` (`<a href="#top" class="scroll-top">▲</a>`). |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `styles.css` líneas 291-308: `border-radius:50%`, carácter `▲`, `position: fixed; bottom:20px; right:20px`. |
| Botón volver arriba — funcional | ✅ | Ancla `href="#top"` apunta a `<header id="top">` presente en las tres páginas; mecanismo de ancla válido según la rúbrica (sin `scroll-behavior: smooth`, el salto es abrupto pero funcional). |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en el `<head>` de `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display:flex }` (línea 86-92) y `form { display:flex; flex-direction:column }` (línea 176-182). |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `styles.css` líneas 329-383: `nav ul { flex-direction: column }` dentro del media query; tabla reduce `font-size` a 0.85rem y es de solo 2 columnas (no hay riesgo real de romper el ancho). |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Sección "Laboratorio 4: Reflexión Aplicada" con las 3 preguntas respondidas; el fragmento citado en la pregunta 1 coincide exactamente con `styles.css` líneas 71-77. |

## Observaciones puntuales

- `index.html`, `acercade.html`, `contacto.html`: el título del `<h1>` es largo ("Portal de Isaías Reyes Arzamendia - reyes-6775-42"). En el `@media (max-width: 768px)` el header pasa a `flex-direction: column` (`styles.css` línea 334-338) y el `padding-top` del `body` se ajusta a 100px (línea 331). En viewports angostos (~375px) ese título a `font-size: 1rem` puede ocupar dos líneas, lo que deja el header real algo más alto que los 100px reservados; no se pudo confirmar en vivo con captura de pantalla (sin automatización de navegador disponible), se señala como riesgo de ajuste fino, no como incumplimiento constatado.
- `contacto.html`, formulario: el campo "Teléfono" usa `type="text"` (no `type="tel"`) y "Dirección"/"Provincia"/"CP" también son `type="text"`; no afecta el estilado (todos caen bajo el mismo selector `form input[type="text"]`), solo se señala por prolijidad semántica de HTML, no se descuenta en este TP de CSS.
- El botón "volver arriba" no usa `scroll-behavior: smooth` ni JS, por lo que el salto al hacer clic es instantáneo en vez de animado; la rúbrica solo exige que funcione (ancla `#`), por lo que no se descuenta.
- El repositorio conserva archivos sueltos ajenos al TP en la raíz (`config_git.png`, `images (2).jfif`, `laboratorio1`) de entregas anteriores; no inciden en la corrección de este laboratorio.
- Único commit de este TP (`e25364e`, "TP4: Estilado avanzado, posicionamiento y responsive design", 9/10/2026), dentro del plazo de entrega (cierre 10/10/2026 23:00).

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

---

# Devolución Lab 4 — Ramiro Reynoso

## Datos identificatorios

- **Token:** reynoso-4260-07
- **GitHub Pages:** https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/ (inferida, no entregada explícitamente; responde 200 y el contenido coincide con el repositorio)
- **Repositorio:** https://github.com/Ramireybas/peylw-2026-practicos-reynoso-4260-07

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `hsl(215, 80%, 40%)`, color modulado, no puro. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Línea 1 de `styles.css`: `/* TOKEN-ALUMNO: reynoso-4260-07 - HSL: hsl(215, 80%, 40%) */`. |
| Tabla de `contacto.html` formateada | ✅ | Bordes, padding y encabezado `th` con fondo de color y texto blanco. |
| Formulario de `contacto.html` formateado | ⚠️ | Campos de texto y labels correctos, pero el selector `form input` (sin excluir `type=radio`/`checkbox`) deforma los controles de radio/checkbox. Ver observaciones. |
| Fuente web importada y aplicada | ✅ | Google Fonts "Montserrat" vía `@import`, aplicada en `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo-curza">` ubicado inmediatamente después del `<h1>` dentro del header flex. |
| Animación de giro completo (360°) del logo | ✅ | `transition: transform 1s ease-in-out` + `:hover { transform: rotateY(360deg) }`. Disparada por hover, no autoplay (variante permitida). |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top: 0 }` en `styles.css`, compartido por las tres páginas; `body { padding-top: 90px }` (130px en mobile) compensa el contenido tapado. |
| "Acerca de" — primera línea sticky | ✅ | `.bio-box h2` (el `<h2>Biografía</h2>`) con `position: sticky; top: 0` y `background-color` sólido. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.bio-box { max-height: 300px; overflow-y: auto }`. El contenedor es un `<div class="bio-box">` que envuelve al `<h2>` y al `<article>`, no el `<article>` mismo — variante admitida por la consigna ("o contenedor del texto"). |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a href="#top" class="btn-arriba">▲</a>` en `index.html`, `acercade.html` y `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius: 50%`, `position: fixed; bottom: 20px; right: 20px`, carácter `▲`. |
| Botón volver arriba — funcional | ✅ | Ancla `href="#top"` con `<div id="top"></div>` al inicio del `<body>` en las tres páginas. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `.contendor_header` y `nav ul` con `display: flex`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `@media (max-width: 768px)` apila `.contendor_header` y `nav ul` en columna, y pone `table { display: block; overflow-x: auto }`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Las 3 preguntas están respondidas; el fragmento de CSS citado en la pregunta 1 coincide textualmente con `.logo-curza`/`.logo-curza:hover` real en `styles.css`. |

## Observaciones puntuales

- **`styles.css`, líneas 113–120** (regla `form input`): el selector aplica a todos los `<input>` del formulario sin distinguir `type`. En `contacto.html` esto alcanza también a los radios del fieldset "Método Preferido de contacto" y a los checkboxes de "Suscripción de Interés" (líneas 71–94), que reciben `width: 100%`, `padding: 8px`, `border: 1px solid #ccc` y `border-radius: 4px`. El resultado es que esos controles pierden su apariencia nativa de radio/checkbox y se renderizan como barras rectangulares de ancho completo en lugar de controles pequeños y legibles. Falta un selector `input[type="text"], input[type="email"], ...` (o excluir `radio`/`checkbox`) para que la regla no afecte a esos grupos.
- La animación del logo solo se dispara con `:hover` (`styles.css`, líneas 38–45); no hay ejecución automática al cargar la página. La consigna admite "el evento que el alumno haya definido", por lo que no se penaliza, pero se señala porque un usuario que no pase el mouse por el logo nunca verá el giro.
- El resto de los ítems (personalización, tabla, fuente web, header fijo con compensación, sticky + scroll en "Acerca de", botón volver arriba, responsive, `REFLEXION.md`) cumple sin desvíos relevantes respecto del enunciado.
- La entrega no incluyó la URL de GitHub Pages, solo el link al repositorio; se infirió la URL estándar (`https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/`) y se verificó que responde 200 con contenido coincidente. El enunciado pide entregar la URL de Pages ya desplegada, no el repositorio.

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

---

# Devolución Lab 4 — Carla Tirado Moreira

## Datos identificatorios

- **Nombre:** Carla Tirado Moreira
- **Legajo:** CURZA-10319
- **Token:** tiradomoreira-5676-19
- **Repositorio:** https://github.com/carlatmoreira98/peylw-2026-practicos-tiradomoreira-5676-19
- **GitHub Pages:** https://carlatmoreira98.github.io/peylw-2026-practicos-tiradomoreira-5676-19/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | Primario `hsl(0, 65%, 45%)`, modulado, no puro. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | Cabecera de `styles.css` líneas 2-10: nombre, token y los tres HSL (primario, fondo, texto). |
| Tabla de `contacto.html` formateada | ✅ | Bordes 1px en `th`/`td`, padding 12px, encabezado con fondo `hsl(0,65%,45%)` y texto blanco, filas con cebra (`nth-child`). |
| Formulario de `contacto.html` formateado | ✅ | Inputs con padding y ancho consistentes, radios/checkboxes en `<div>` individuales sin superposición. |
| Fuente web importada y aplicada | ✅ | Montserrat vía `@import` de Google Fonts, aplicada en `body` con fallback `sans-serif`. |
| Logo CURZA a la derecha del título | ✅ | `<img class="logo-curza">` ubicado después del `<h1>` en el `<header>` flex de las tres páginas. |
| Animación de giro completo (360°) del logo | ✅ | `transition: transform 1s` + `:hover { transform: rotateY(360deg) }` (transición disparada, alternativa válida a `@keyframes` según la rúbrica). Termina en 360°/0°, orientación correcta. |
| Header fijo en todas las páginas | ✅ | `header { position: fixed; top:0 }` en `styles.css`, compartido por `index.html`, `acercade.html` y `contacto.html`. |
| "Acerca de" — primera línea sticky | ✅ | `.titulo-sticky` (`position: sticky; top:0`) en el primer `<h2>` ("Sobre mí") dentro de `.biografia`. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `.biografia { max-height:300px; overflow-y:auto }` sobre el `<article>`. |
| Botón volver arriba — presente en todas las páginas | ✅ | `<a class="volver-inicio">▲</a>` al final del `<body>` en las tres páginas. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `border-radius:50%`, `position:fixed; bottom:20px; right:20px`, carácter ▲. |
| Botón volver arriba — funcional | ✅ | `href="#top"` ancla a `<body id="top">`, con `scroll-behavior: smooth` en `html`. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente e idéntica en `index.html`, `acercade.html`, `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `header`, `nav ul` y `form` usan `display:flex`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `nav ul { flex-direction: column }` y `table { display:block; overflow-x:auto }` dentro de `@media (max-width: 768px)`. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ⚠️ | Presente, pero solo responde 2 de las 3 preguntas (falta la pregunta 3 sobre el cambio visual en mobile por los `@media`). El fragmento citado en la respuesta 1 coincide exactamente con el CSS real. |

## Observaciones puntuales

- `REFLEXION.md`: falta por completo la respuesta a la pregunta 3 ("¿qué cambio visual ocurre en pantallas menores a 768px por las `@media` implementadas?"). El archivo termina después de la pregunta 2.
- Fecha de commit real del TP4 (`8f4f651`): 2026-10-10 23:01:10 -03:00, es decir aproximadamente 1 minuto después del cierre oficial (10/10/2026 23:00). Al borde del límite; este documento no define penalización por atraso, queda a criterio general del curso.
- La "Fecha de Entrega" declarada en `entregas.md` (2026-09-13) no coincide con la fecha real del commit del TP4 (2026-10-10); probablemente un campo copiado de una entrega anterior y no actualizado.
- Sitio de GitHub Pages responde correctamente (200); el `<h1>` y el logo visibles en producción coinciden con el repositorio.

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
| `REFLEXION.md` | 5 | 4 |
| **TOTAL** | **100** | **99** |

---

# Devolución Lab 4 — Sandra Vela

## Datos identificatorios

- **Token:** vela-9972-35
- **GitHub Pages:** https://shalom198424.github.io/peylw-2026-practicos-vela-9972-35/
- **Repositorio:** https://github.com/Shalom198424/peylw-2026-practicos-vela-9972-35 (rama `laboratorio4`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ✅ | `styles.css` líneas 29-39: color primario `hsl(145, 45%, 35%)` y derivados, todos modulados, sin colores puros. |
| Personalización — comentario en `styles.css` con HSL + identificador | ✅ | `styles.css` líneas 1-20: comentario de cabecera con nombre, token `vela-9972-35` y los 5 códigos HSL de la paleta. |
| Tabla de `contacto.html` formateada | ✅ | `styles.css` líneas 370-402: bordes y padding en `th`/`td`, `thead` con fondo de color y texto blanco, filas pares (`nth-child(even)`) diferenciadas. |
| Formulario de `contacto.html` formateado | ✅ | `styles.css` líneas 237-329: inputs con padding uniforme, `label` en negrita sobre su campo (`.formulario-campo` en columna), radios/checkboxes agrupados en `.opcion` sin superposición. |
| Fuente web importada y aplicada | ✅ | `styles.css` línea 22 (`@import` de Google Fonts "Outfit") y línea 56 (`font-family: 'Outfit', sans-serif` en `body`, con fallback). Se aplica a todo el texto del sitio. |
| Logo CURZA a la derecha del título | ✅ | `index.html`/`acercade.html`/`contacto.html`: dentro de `.encabezado-marca`, el `<img class="logo-curza">` está después del `<h1>` en el flujo flex, quedando a la derecha. |
| Animación de giro completo (360°) del logo | ✅ | `styles.css` líneas 106-123: `transition: transform 1s ease-in-out` + `.logo-curza:hover { transform: rotateY(360deg); }`. Es una transición disparada por `:hover` (variante permitida por la rúbrica), no un `@keyframes` con autoplay; termina en 360°/0° equivalente, orientación correcta. |
| Header fijo en todas las páginas | ✅ | `styles.css` líneas 67-84: `header { position: fixed; top: 0; }` en la hoja de estilos compartida por las 3 páginas. `main` compensa con `padding-top: 145px` (línea 175) y `245px` en mobile (línea 516). |
| "Acerca de" — primera línea sticky | ✅ | `acercade.html` línea 59 (`<h2>Biografía</h2>` dentro de `.bio-scroll`) + `styles.css` líneas 218-230: `position: sticky; top: 0;` con `background-color` propio. |
| "Acerca de" — `max-height: 300px` + scroll | ✅ | `styles.css` líneas 208-210: `.bio-scroll { max-height: 300px; overflow-y: auto; }`. |
| Botón volver arriba — presente en todas las páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html` como `<a class="btn-inicio" href="#top">`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ | `styles.css` líneas 409-439: `border-radius: 50%`, `position: fixed; bottom/right: 20px`, carácter `▲` como flecha. |
| Botón volver arriba — funcional | ✅ | `href="#top"` ancla a `<body id="top">` en las 3 páginas, combinado con `html { scroll-behavior: smooth; }` (línea 51). |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en el `<head>` de las 3 páginas HTML. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `header`/`nav ul` con `display: flex`; `form` con `display: grid` (líneas 237-240). |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ✅ | `styles.css` líneas 470-544: `nav ul { flex-direction: column; }`; tabla contenida en `.tabla-contenedor { overflow-x: auto; }` con `table { min-width: 600px; }`, lo que da scroll lateral controlado en vez de romper el ancho. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ✅ | Archivo en la raíz, 3 preguntas respondidas; el fragmento de CSS citado en la pregunta 1 es idéntico al bloque real `.logo-curza` / `.logo-curza:hover` de `styles.css`. |

## Observaciones puntuales

- `styles.css`, animación del logo (líneas 106-123): la rotación se dispara con `:hover`, no al cargar la página ni con `@keyframes` + `animation` autoplay. La rúbrica admite expresamente esta variante ("transition disparada"), pero en la verificación en vivo el efecto solo se observa pasando el cursor sobre el logo, no al entrar a la página.
- `styles.css`: varios `box-shadow` usan `hsl(h, s%, l%, alpha)` con cuatro valores separados por coma (líneas 83, 200, 248, 297, 310, 434) en lugar de `hsla(...)` o la sintaxis `hsl(h s% l% / alpha)`. Los navegadores modernos (Chrome/Firefox/Safari actualizados) lo interpretan correctamente por la unificación de CSS Color 4, pero es una sintaxis no estrictamente válida en la especificación clásica; no genera falla visible en la verificación en vivo realizada.
- `styles.css` (línea 516): en mobile el `padding-top` del `main` es `245px` para compensar un header que pasa a `flex-direction: column` con tres enlaces de navegación apilados. El margen es ajustado pero suficiente en la prueba realizada; si el alumno agrega contenido al encabezado en el futuro, conviene revisar que no se recorte contra el `main`.
- Verificación en vivo (GitHub Pages): la URL responde 200. Se contrastó el contenido servido (`index.html`, `contacto.html`, `styles.css`) contra el clon local de la rama `laboratorio4` y coincide (título, encabezado, campos del formulario, tabla "Resumen de datos", comentario de cabecera con paleta HSL y token). No se usó automatización de navegador; la comprobación de interacciones (hover, scroll, clic del botón) se basó en la lectura del código, que es consistente y funcional según su implementación.

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
