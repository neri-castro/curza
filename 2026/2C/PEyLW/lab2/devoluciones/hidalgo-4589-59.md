# Devolución Lab 2 — Alexis Hidalgo

## Datos identificatorios

- **Nombre:** Alexis Hidalgo
- **Legajo:** Curza-9159
- **Token:** hidalgo-4589-59
- **Repositorio:** https://github.com/aletemp52-cmd/peylw-2026-practicos-hidalgo-4589-59
- **GitHub Pages:** https://aletemp52-cmd.github.io/peylw-2026-practicos-hidalgo-4589-59/

## ⚠️ Hallazgo: quedaron corchetes de plantilla sin completar en el sitio publicado

En varios lugares clave el alumno dejó el texto de plantilla entre corchetes tal cual,
sin reemplazarlo por sus datos reales:

- `index.html`: `<title>` y `<h1>` dicen literalmente `Portal de [Alexis Hidalgo] - hidalgo-4589-59` (con los corchetes incluidos).
- `acercade.html`: el `<title>` y el `<h1>` dicen literalmente `Portal de [Tu Nombre Completo] - hidalgo-4589-59` — **ni siquiera llegó a poner su nombre real**, quedó el placeholder genérico de la plantilla.
- El `alt` de la imagen en `acercade.html` también conserva los corchetes: `alt="Fotografía de perfil de [Alexis Hidalgo], estudiante de Desarrollo Web"`.
- El `README.md` completo tiene todos los campos entre corchetes sin remover (`[Alexis Hidalgo]`, `[Curza-9159]`, `[4589]`, `[https://...]`).

Esto afecta directamente la personalización y la consistencia entre páginas, y se
penaliza en los ítems correspondientes.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Los seis campos están presentes con la información correcta, pero todos quedaron entre corchetes de plantilla sin remover (`[Alexis Hidalgo]`, `[Curza-9159]`, etc.), dando la impresión de un trabajo sin terminar. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: hidalgo-4589-59 -->` exacto e idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ❌ | En `index.html` el nombre está entre corchetes sin remover (`[Alexis Hidalgo]`). En `acercade.html` el `<h1>` literalmente dice `[Tu Nombre Completo]`, el placeholder de la plantilla sin completar. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ⚠️ | `lang="es"` y charset correctos, pero el `<title>` conserva los corchetes de plantilla. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | Presente, pero el `<h1>` tiene los corchetes sin remover. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>Bienvenidos a mi espacio</h2>` exacto, pero los dos párrafos hablan del trabajo práctico en sí ("Este sitio web es parte de el laboratorio numero 2...") en vez de dar la bienvenida al visitante. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Contenido correcto (copyright con corchetes sin remover, dirección exacta, token), pero además hay una etiqueta `</footer>` de cierre duplicada y huérfana justo después del footer real (HTML inválido). |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | El `<h1>` y el `<footer>` de `acercade.html` usan el placeholder `[Tu Nombre Completo]`, distinto al `[Alexis Hidalgo]` de `index.html`. No son idénticos entre páginas. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real y personal (cuenta el cambio de carrera de Administración de Sistemas a esta Tecnicatura), con dos párrafos completos. Sin embargo, todo el texto biográfico está en una sola `<section>` ("Sobre mi interés por la carrera"); la segunda sección mezcla imagen y lista de tecnologías, no es continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ⚠️ | Imagen en `img/perfil.jpeg`, ruta correcta, `<figcaption>` presente y bien redactado. Pero el `alt` conserva los corchetes de plantilla (`[Alexis Hidalgo]`), por lo que un lector de pantalla leería literalmente los corchetes. Además, `<main>` está duplicado y anidado (ver más abajo), lo que rompe la validez del documento. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 4 tecnologías, correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body`, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ❌ | Ningún commit del historial usa el mensaje exacto `TP2: Estructuras HTML y vinculacion de estilos`. Los commits reales son "Entrega Laboratorio 2 completa", "Actualizacion de links en README" y "Renombra imagen a perfil.jpeg y corrige ruta". |
| Estructura de archivos correcta | ✅ | Coincide exactamente con el árbol pedido: `index.html`, `acercade.html`, `styles.css`, `img/perfil.jpeg`, `README.md`, `REFLEXION.md`, sin residuos del Lab 1. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200 en producción y la navegación funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ❌ | El `REFLEXION.md` responde preguntas distintas a las tres que pide el enunciado de este laboratorio (ver detalle abajo). |

## Observaciones puntuales

- **Corchetes de plantilla sin completar (crítico):** aparecen en el `<h1>` y `<title>` de ambas páginas, en el `alt` de la imagen y en todos los campos del `README.md`. En `acercade.html` esto es especialmente grave porque el `<h1>` queda literalmente como `[Tu Nombre Completo]`, sin ningún dato real del alumno.
- **`REFLEXION.md` no responde las preguntas del enunciado de Lab 2.** En vez de "indique el nombre de la imagen y el alt usado", responde "qué diferencia hay entre ruta relativa y absoluta"; en vez de "cómo verificó las rutas de navegación en local y en GitHub Pages", responde "qué dificultades se presentaron durante el laboratorio". Solo la pregunta sobre HTML semántico vs. `<div>` coincide en espíritu con lo pedido (pregunta 2 del enunciado) y está bien respondida.
- **`<main>` duplicado y anidado** en `acercade.html`: hay un `<main>` dentro de otro `<main>`, algo no válido en HTML5 (el elemento `<main>` no puede anidarse).
- **`</footer>` huérfano** en `index.html`: hay una etiqueta de cierre de más sin apertura correspondiente.
- El resto (CSS, lista de tecnologías, estructura de archivos, GitHub Pages, comentario de token) está resuelto correctamente.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 3 |
| Personalización (token + `<h1>`) | 10 | 6.5 |
| Tarea 1 — `index.html` | 25 | 18.5 |
| Tarea 2 — `acercade.html` | 30 | 18.5 |
| Tarea 3 — `styles.css` y commit | 10 | 6 |
| Estructura de archivos | 5 | 5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 5 |
| **TOTAL** | **100** | **68** |
