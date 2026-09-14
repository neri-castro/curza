# Devolución Lab 2 — Luciano García Díaz

## Datos identificatorios

- **Nombre:** Luciano García Díaz (confirmado en `readme.md`, `index.html`, `acercade.html` y `REFLEXION.md` del repo)
- **Legajo:** CURZA-10019
- **Token:** garciadiaz-9325-19
- **Repositorio:** https://github.com/Lucho-GD/TP2-Estructuras-HTML-y-vinculacion-de-estilos
- **GitHub Pages:** https://lucho-gd.github.io/TP2-Estructuras-HTML-y-vinculacion-de-estilos/

## ⚠️ Hallazgo: repositorio nuevo que no sigue la convención de nombre pedida

En `entregas.md` esta entrega figura sin nombre ni token, solo con los dos enlaces de
arriba. El repositorio se llama `TP2-Estructuras-HTML-y-vinculacion-de-estilos`, **no**
`peylw-2026-practicos-garciadiaz-9325-19` como exige el enunciado y como se usó en el
Lab 1 (con la misma cuenta `Lucho-GD`). El repo `peylw-2026-practicos-garciadiaz-9325-19`
del Lab 1 sigue existiendo y es público, pero el alumno no continuó ahí: creó un
repositorio nuevo y completamente separado para este TP2.

El contenido en sí es identificable sin ambigüedad (nombre, token y datos coinciden en
`readme.md`, `REFLEXION.md` y ambos HTML), así que se corrige igual, pero se penaliza el
incumplimiento de la convención de nombres en el ítem "Estructura de archivos".

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Todos los campos (nombre, legajo, DNI, fecha, token, repo, Pages) completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ❌ | No existe el comentario `<!-- TOKEN-ALUMNO: ... -->` (ni ninguna variante) al inicio del `<body>` en `index.html` ni en `acercade.html`. |
| Personalización — `<h1>` exacto (ambos archivos) | ❌ | `index.html`: `<h1>` es "Laboratorio 2: Estructura y Semantica Web con HTML5" — ni nombre ni token, ni formato "Portal de...". `acercade.html`: `<h1>` es "Luciano Garcia Diaz - garciadiaz-9325-19" — le falta el prefijo "Portal de" y además difiere del de `index.html`. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ⚠️ | `lang="es"` y charset UTF-8 correctos, pero el `<title>` repite el nombre del laboratorio en vez de identificar el portal del alumno. |
| Tarea 1 — `index.html`: `<header>` | ❌ | Existe estructuralmente, pero el `<h1>` no identifica al alumno en absoluto (ver Personalización). |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | Rutas relativas correctas ("Inicio"/"Acerca de"), pero el markup es inválido: cada enlace está envuelto en su propio `<ul><a>...</a></ul>` sin `<li>`, en vez de un único `<ul>` con dos `<li>`. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright con corchete de plantilla sin remover (`[Luciano Garcia Diaz]`); dirección del nodo y token en texto simple correctos. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ⚠️ | `<nav>` y `<footer>` son idénticos entre páginas; el `<h1>` no lo es (ver Personalización). |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real y personal, dos párrafos, menciona explícitamente la Tecnicatura en Desarrollo Web. Sin embargo todo el texto está en un único `<article>` sin dividir en dos `<section>`; la segunda `<section>` del documento es la lista de tecnologías, no continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Imagen en `img/img-mifoto.jpg`, ruta relativa correcta, carga en producción. `alt="Foto de Luciano Garcia Diaz"` personalizado con nombre real (podría describir mejor la foto en sí, pero cumple). |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 4 tecnologías, en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con regla de `body` (font-family y background-color), vinculado en el `<head>` de ambos archivos. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` aparece tres veces en el historial, coincide letra por letra e incluye los archivos del TP2. |
| Estructura de archivos correcta | ❌ | El árbol interno del repo es correcto, pero el repositorio en sí no sigue la convención `peylw-2026-practicos-<token>` exigida (ver hallazgo arriba): es un repo nuevo con otro nombre, no una continuación del repo de Lab 1. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/img-mifoto.jpg` responden 200 en producción; la navegación entre páginas funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas: el nombre de imagen y el `alt` declarados coinciden con lo real, la justificación de semántica es sólida (accesibilidad, lectores de pantalla, SEO), y describe una verificación concreta en local y luego en GitHub Pages. |

## Observaciones puntuales

- **Repositorio con nombre no convencional (crítico):** ver hallazgo al inicio. Debe unificarse con el repo `peylw-2026-practicos-garciadiaz-9325-19` usado en Lab 1, o al menos declarar el cambio explícitamente en la entrega.
- **Comentario de token ausente por completo** en ambos archivos HTML, no solo con formato incorrecto: no hay ningún comentario de token.
- **`<h1>` no personalizado en `index.html`** (repite el título del enunciado) y **distinto entre páginas**: es el punto de mayor pérdida de puntaje.
- `<nav>` con markup inválido: `<a>` como hijo directo de `<ul>` sin `<li>`.
- Corchete de plantilla sin remover en el copyright del footer (`[Luciano Garcia Diaz]`).
- Biografía real y bien orientada a la Tecnicatura, pero no dividida en dos secciones como pide la consigna.
- CSS, commit, lista de tecnologías, imagen, GitHub Pages y reflexión están bien resueltos.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 0 |
| Tarea 1 — `index.html` | 25 | 17 |
| Tarea 2 — `acercade.html` | 30 | 23 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 1 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **71** |
