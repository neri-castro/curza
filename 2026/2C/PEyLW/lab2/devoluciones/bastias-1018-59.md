# Devolución Lab 2 — Marité Bastías

## Datos identificatorios

- **Nombre:** Marité Bastías
- **Legajo:** CURZA-9959
- **Token:** bastias-1018-59
- **Repositorio:** https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59/tree/laboratorio_2
- **GitHub Pages:** https://marite28.github.io/peylw-2026-practicos-bastias-1018-59/

## Nota metodológica

El trabajo del TP2 está en la rama `laboratorio_2`, no en `main`. A diferencia de otros
casos de esta tanda, el enlace entregado **sí declara explícitamente** la rama
(`.../tree/laboratorio_2`), por lo que no se considera un ocultamiento del trabajo; se
descuenta solo levemente en "Estructura de archivos" por no estar mergeado a la rama
principal.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ❌ | El README no sigue el formato de carátula pedido: tiene nombre, token y fecha, pero **faltan** Legajo/Matrícula, DNI, enlace al repositorio y enlace a GitHub Pages. |
| Personalización — Token en comentario (ambos archivos) | ⚠️ | `<!--token-alumno: bastias-1018-59-->` en ambos archivos: formato en minúsculas y sin los espacios que pide el `<!-- TOKEN-ALUMNO: <token> -->` exacto. Consistente en ambos, pero no cumple el formato. |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | `Portal de Marité - bastias-1018-59` en ambas páginas: falta el apellido, no es el "Nombre Completo" que exige la consigna. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` correctos. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | Presente, pero el `<h1>` no tiene el nombre completo (ver Personalización). |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | Rutas relativas correctas, pero el texto del enlace es "inicio" en minúscula en vez de "Inicio". |
| Tarea 1 — `index.html`: `<main>` bienvenida | ❌ | La etiqueta usada es `<seccion>` (sin la "t"), que **no es** la etiqueta semántica `<section>` de HTML5: el navegador la trata como un elemento desconocido, no como contenedor semántico. El `<h2>` sí dice "Bienvenidos a mi espacio" exacto, y hay dos párrafos, pero son más biográficos que explicativos del sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright dice solo "Marité" (falta el apellido); dirección del nodo exacta; token presente en texto simple. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html` (mismos textos y estructura, incluidas las mismas limitaciones ya señaladas). |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Biografía real y personal, dividida en dos `<section>` (una sobre la carrera, mencionando explícitamente la Tecnicatura en Desarrollo Web, y otra sobre su vida personal), con dos párrafos completos. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ❌ | El `<img>` no cierra con `>` (línea del `src`/`alt` sigue directo a `<figcaption>` sin cerrar la etiqueta), lo que hace que el navegador interprete `<figcaption` como un atributo más de `<img>` y el `</figcaption>` quede huérfano: el `<figcaption>` real no se renderiza como tal. La imagen en sí probablemente carga (src y alt se parsean antes del error), pero el subtítulo semántico se rompe. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 5 tecnologías, contenido correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body`, vinculado en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ⚠️ | `TP2: Estructuras HTML y  vinculacion de estilos` (doble espacio entre "y" y "vinculacion"). Ese commit puntual solo agrega `index.html` y `styles.css`; el `<link>` en `acercade.html` y la imagen se agregaron en commits posteriores, aunque forman parte del mismo desarrollo del TP2. |
| Estructura de archivos correcta | ⚠️ | El árbol de la rama `laboratorio_2` coincide exactamente con lo pedido, pero el trabajo no está mergeado a `master` (rama por defecto), que sigue en el estado del Lab 1. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos (HTML, CSS, imagen) responden 200 en producción y la navegación funciona. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repositorio real y están bien justificadas (menciona lectores de pantalla y buscadores en la pregunta 2, y describe el proceso concreto de verificación local y en GitHub Pages en la pregunta 3). |

## Observaciones puntuales

- **README incompleto:** falta Legajo, DNI, y ambos enlaces (repo y Pages). No cumple el formato de carátula pedido.
- **`<h1>` y copyright con nombre incompleto:** en ambos casos falta el apellido "Bastías".
- **Bug de markup grave:** en `acercade.html`, el `<img>` de la figura no cierra su etiqueta antes de `<figcaption>`, rompiendo la estructura de la figura.
- **`<seccion>` en vez de `<section>`** en `index.html`: no es una etiqueta HTML5 válida, pierde el valor semántico de la sección de bienvenida.
- El resto de la estructura (biografía, lista de tecnologías, CSS, commit, Pages, reflexión) está resuelto correctamente.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 1 |
| Personalización (token + `<h1>`) | 10 | 6 |
| Tarea 1 — `index.html` | 25 | 19 |
| Tarea 2 — `acercade.html` | 30 | 22 |
| Tarea 3 — `styles.css` y commit | 10 | 9 |
| Estructura de archivos | 5 | 3.5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **76** |
