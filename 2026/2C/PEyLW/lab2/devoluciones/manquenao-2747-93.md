# Devolución Lab 2 — Tatiana Manquenao (reevaluación)

Reevaluación tras la actualización del repositorio (commit `de7a8de`, 22/09/2026, posterior al cierre del 07/09). Nota anterior: 44.5.

## Datos identificatorios

- **Nombre:** Tatiana Manquenao (declarado así en `Readme.md`; el `<h1>` y el `<footer>` de ambas páginas HTML usan "Rocio Manquenao", y la biografía en `acercade.html` se autodenomina "Rocio Tatiana" — identidad inconsistente entre archivos)
- **Legajo:** 7093 (declarado así en la primera mitad de `Readme.md`; la segunda mitad, duplicada, deja el campo como `TU_LEGAJO`)
- **Token:** manquenao-2747-93 (el HTML usa un token equivocado, `manquenao-4567-89`)
- **Repositorio:** https://github.com/tati99-web/manquenao-2747-93 (no sigue la convención `peylw-2026-practicos-<token>`; el repo `tati99-web/peylw-2026-practicos-manquenao-2747-93` solo contiene el `index.html` del Lab 1 y no es la entrega real)
- **GitHub Pages:** https://tati99-web.github.io/manquenao-2747-93/ (responde 200 tras la actualización)

## Qué cambió con la actualización

- Se subieron copias de `index.html`, `acercade.html`, `styles.css`, `Readme.md`, `Reflexion.md` e imagen a la **raíz** del repo. Pages ahora responde 200 en `/`, `/acercade.html` y `/styles.css`.
- La subcarpeta `manquenao-2747-93/` con la copia anterior **sigue en el repo** (duplicada).
- **El contenido de los archivos es idéntico al de la entrega anterior** (la única diferencia es el formato de saltos de línea). No se corrigió ninguno de los errores de contenido.
- El commit nuevo se llama `Subida inicial de archivos del sitio`; sigue sin existir el mensaje exacto `TP2: Estructuras HTML y vinculacion de estilos`.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ❌ | `Readme.md` sigue con el contenido duplicado; la segunda copia deja `TU_LEGAJO` y `TU_ENLACE` sin reemplazar, y el enlace al repo y a Pages nunca se completa correctamente (aparece una URL `.git` del repo `peylw-2026-practicos-...` que no es la entrega). |
| Personalización — Token en comentario (ambos archivos) | ❌ | `<!-- TOKEN-ALUMNO: TU-TOKEN -->` en ambos archivos, sin reemplazar. |
| Personalización — `<h1>` exacto (ambos archivos) | ❌ | `Portal de Rocio Manquenao - TU-TOKEN` en ambas páginas: placeholder sin reemplazar y nombre distinto al del README. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ❌ | `<!DOCTYPE html>` duplicado y línea ` ```html ` suelta antes del documento; ` ``` ` suelta al final. `<title>` no incluye el token. `lang="es"` y charset correctos. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | Etiqueta presente, `<h1>` sin personalizar. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas; verificado que ambas páginas responden 200 en Pages. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` y dos párrafos reales. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright y dirección del nodo correctos; token `Token: TU-TOKEN: manquenao-4567-89--` con placeholder y token equivocado. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ⚠️ | Equivalentes a `index.html` con los mismos errores; el footer difiere en redacción (`Token TU-TOKEN: ...`). Arrastra ` ```html ` al inicio y ` ``` ` al final. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Biografía personal en dos `<section>`. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ❌ | `src="img/mi_foto.jpg"` sigue devolviendo **404** en Pages y no existe en el repo. La imagen real está en `img - copia/2e3a2121-c141-45ef-a85e-b34900a7cfe7.jpg` (carpeta y nombre incorrectos). El `alt` dice "Rocio Manquenao". |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con HTML5, CSS, JavaScript y Python. |
| Tarea 3 — `styles.css` en la raíz, con regla de `body` | ✅ | Ahora está en la raíz con `font-family` y `background-color`. |
| Tarea 3 — `<link>` en ambas páginas | ✅ | Presente en ambas y resuelve (200) en Pages. |
| Tarea 3 — Commit con mensaje exacto | ❌ | Historial: `Initial commit`, `Add files via upload`, `Subida inicial de archivos del sitio`. Ninguno usa el mensaje pedido. |
| Estructura de archivos correcta | ⚠️ | Los archivos ya están en la raíz, pero la imagen está en `img - copia/` y no en `img/`, queda una copia duplicada en `manquenao-2747-93/`, y el repo no sigue la convención de nombre. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `/` y `/acercade.html` responden 200 y la navegación entre ambas funciona. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Pregunta 1 no coincide con el repo (`mi_foto.jpg` no existe; el `alt` real dice "Rocio", no "Tatiana"). Pregunta 2 correcta y argumentada. Pregunta 3 correcta en forma, aunque genérica. |

## Observaciones puntuales

- **Corregido:** Pages responde 200 y `styles.css` está en la raíz.
- **Sin corregir (crítico):** placeholders `TU-TOKEN` en comentario, `<h1>` y footer de ambas páginas; token equivocado `manquenao-4567-89`.
- **Sin corregir (crítico):** restos de Markdown (` ```html `, ` ``` `, `<!DOCTYPE>` duplicado) en ambos HTML.
- **Sin corregir:** la imagen sigue rota en producción (`img/mi_foto.jpg` → 404).
- **Sin corregir:** identidad inconsistente (Tatiana / Rocio / Rocio Tatiana) entre README, HTML y reflexión.
- **Sin corregir:** `Readme.md` duplicado con `TU_LEGAJO`/`TU_ENLACE`.
- **Sin corregir:** falta el commit con el mensaje exacto.
- El sitio aparece publicado en la URL declarada, pero muestra `TU-TOKEN` en el `<h1>` y una imagen rota.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 1 |
| Personalización (token + `<h1>`) | 10 | 0 |
| Tarea 1 — `index.html` | 25 | 14 |
| Tarea 2 — `acercade.html` | 30 | 17 |
| Tarea 3 — `styles.css` y commit | 10 | 6 |
| Estructura de archivos | 5 | 2 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 5.5 |
| **TOTAL** | **100** | **50.5** |
