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
