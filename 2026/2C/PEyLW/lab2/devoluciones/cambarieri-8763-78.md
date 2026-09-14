# Devolución Lab 2 — Matías Cambarieri Gentile

## Datos identificatorios

- **Nombre:** Matías Cambarieri Gentile
- **Legajo:** CURZA-10178
- **Token:** cambarieri-8763-78
- **Repositorio:** https://github.com/zaitamu/peylw-2026-practicos-cambarieri-8763-78 (rama por defecto `Laboratorio-2`)
- **GitHub Pages:** https://zaitamu.github.io/peylw-2026-practicos-cambarieri-8763-78/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ⚠️ | `index.html`: `<!--TOKEN ALUMNO: cambarieri-8763-78-->` (sin guion entre "TOKEN" y "ALUMNO", formato distinto al pedido). `acercade.html`: `<!--TOKEN-ALUMNO: cambarieri-8763-78-->` correcto. No son idénticos entre ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Matías Cambarieri Gentile - cambarieri-8763-78` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ❌ | Bug grave de markup: `<html lang="es"></html>` se cierra en la línea 2, dejando todo el `<head>` y el `<body>` fuera de las etiquetas `<html>`. Además el `<meta viewport>` tiene el atributo mal escrito: `width=device width` (falta el guion, debería ser `device-width`). |
| Tarea 1 — `index.html`: `<header>` | ✅ | `<h1>` correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas correctas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>` dice "¡Bienvenidos a mi Espacio!" (con signos de exclamación y "Espacio" en mayúscula) en vez del texto exacto "Bienvenidos a mi espacio". Dos párrafos reales y explicativos del sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | El copyright dice "© 2026 Zaitam Records S.A" en vez del nombre del alumno. Dirección "CURZAS- UNCo, Viedma, Río negro" (falta espacio antes del guion). Token presente en texto simple. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | `<nav>`: el segundo enlace dice "Biografia" en `acercade.html` contra "Acerca de" en `index.html` — no es idéntico. `<footer>`: en `acercade.html` la dirección es "CURZAS, Viedma, Río negro", omitiendo "UNCo" que sí aparece en `index.html`. El `<h1>` sí es idéntico. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Real y personal, dividida en dos `<section>`, menciona explícitamente el interés por la Tecnicatura en Desarrollo Web. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ⚠️ | Imagen en `img/foto_matias.jpg`, ruta relativa correcta, `<figcaption>` con contexto ("Foto en un rodaje."). El `alt="Foto de Matías"` es escueto, poco descriptivo de la imagen en sí. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ❌ | No existe ningún `<ul>` con lenguajes o tecnologías. Se mencionan "Python, Git y otras herramientas" dentro de un párrafo de prosa, no como lista, incumpliendo el ítem explícito del enunciado. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body` (font-family y background-color), vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye `acercade.html`, `index.html`, `styles.css` e `img/foto_matias.jpg`. |
| Estructura de archivos correcta | ⚠️ | Coincide con lo pedido, pero queda una carpeta `capturas/` residual del Lab 1 (`config_git.png`) sin limpiar. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/foto_matias.jpg` responden 200 en producción. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repo real (nombre de imagen y `alt` verificados) y están bien justificadas. |

## Observaciones puntuales

- **Bug de markup grave:** `<html lang="es"></html>` se cierra inmediatamente después de abrirse en `index.html` (línea 2) y en `acercade.html` (línea 2), dejando `<head>` y `<body>` completos fuera del elemento `<html>`. Los navegadores lo corrigen al renderizar, pero es HTML inválido en ambos archivos.
- Falta por completo la lista `<ul>` de tecnologías/lenguajes en `acercade.html`, un ítem explícito del enunciado (5 pts).
- El comentario de token no tiene el mismo formato en los dos archivos: `TOKEN ALUMNO` (sin guion) en `index.html` vs. `TOKEN-ALUMNO` (correcto) en `acercade.html`.
- El `<nav>` y el `<footer>` de `acercade.html` no son idénticos a los de `index.html` (texto del enlace "Biografia" vs. "Acerca de"; dirección del nodo sin "UNCo").
- El copyright del `<footer>` usa un nombre de fantasía ("Zaitam Records S.A") en vez del nombre del alumno.
- El `<h2>` de bienvenida no coincide textualmente con "Bienvenidos a mi espacio" (agrega signos de exclamación y mayúscula).
- Carpeta `capturas/` residual del Lab 1 sin eliminar.
- Todo lo demás (CSS, commit, biografía, reflexión, GitHub Pages) está bien resuelto.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 7.5 |
| Tarea 1 — `index.html` | 25 | 16 |
| Tarea 2 — `acercade.html` | 30 | 18 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 4 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **75.5** |
