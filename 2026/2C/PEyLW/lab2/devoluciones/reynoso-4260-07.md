# Devolución Lab 2 — Ramiro Javier Reynoso Bascary

## Datos identificatorios

- **Nombre:** Ramiro Javier Reynoso Bascary (README de este TP solo consigna "Ramiro Reynoso", igual que en Lab 1)
- **Legajo:** 8907
- **Token:** reynoso-4260-07
- **Repositorio:** https://github.com/Ramireybas/peylw-2026-practicos-reynoso-4260-07
- **GitHub Pages:** https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/index.html

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Falta el campo "Enlace a la Página en GitHub Pages". El campo "Últimos 4 dígitos del DNI" tiene el valor `37504260` (8 dígitos), no los últimos 4 como pide la consigna. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: reynoso-4260-07-->` presente e idéntico en ambos archivos (espaciado interno irregular, no afecta el cumplimiento). |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | `Portal de Ramiro Reynoso - reynoso-4260-07` idéntico en ambas páginas, pero usa el nombre corto declarado en su propio README, no el nombre completo (Ramiro Javier Reynoso Bascary, según Lab 1). |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ⚠️ | `lang="es"` y charset correctos, pero `<title>Practico 2</title>` es genérico, no descriptivo del sitio. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Presente con el `<h1>` personalizado. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | Rutas relativas correctas, pero el texto de los enlaces es "Acerca de" / "Index" en vez de "Inicio" / "Acerca de" que pide el enunciado. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>Bienvenido a mi espacio</h2>` (singular, falta la "s"). Los dos párrafos hablan del propio trabajo práctico ("Esta pagina es el segundo trabajo practico de la materia...") en vez de dar la bienvenida al visitante o explicar el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright y token presentes, pero la dirección del nodo dice "Nodo General Conesa" en vez de "Viedma, Río Negro" (CURZAS - UNCo) como pide el enunciado. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ⚠️ | El `<footer>` es idéntico. El `<nav>` tiene los mismos dos enlaces pero en **orden invertido** respecto de `index.html` (acá "Index" va primero, en `index.html` va segundo), por lo que no son estrictamente idénticos. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | La biografía (dos párrafos, reales y personales, menciona explícitamente la Tecnicatura en Desarrollo Web) está toda en **una sola** `<section>`; la otra `<section>` del artículo contiene la lista de tecnologías, no es continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Ruta relativa `img/Foto_mia.jpeg` correcta, imagen carga en producción. `alt="foto del autor"` y `figcaption` son válidos pero genéricos, podrían ser más específicos. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ⚠️ | `<ul>` con 5 tecnologías, contenido correcto, pero ubicada dentro de una `<section>` del `<article>` en vez de tener su propio espacio separado de la biografía. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body` (font-family y background-color), vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ⚠️ | `TP2 Estructuras HTML y vinculaciones de estilos` — falta el `:` después de "TP2" y dice "vinculaciones" (plural) en vez de "vinculacion". El commit sí incluye todos los archivos del TP2. |
| Estructura de archivos correcta | ⚠️ | Quedó un archivo residual en la raíz, `httpsgithub.comRamireybaspeylw-2026.png` (captura del Lab 1 sin limpiar); el resto del árbol coincide con lo pedido. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/Foto_mia.jpeg` responden 200 en producción; la navegación entre páginas funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Preguntas 1 y 3 correctas y concretas (coinciden con el repo real, describe cómo verificó las rutas en local y por qué usar rutas relativas para Pages). Pregunta 2 es vaga y poco desarrollada, no explica con claridad la ventaja de la semántica sobre `<div>` (accesibilidad, SEO, mantenibilidad). |

## Observaciones puntuales

- Falta el campo de enlace a GitHub Pages en el README, y el campo de DNI tiene un valor de 8 dígitos en vez de los últimos 4.
- El `<h2>` de bienvenida dice "Bienvenido" (singular) en vez de "Bienvenidos".
- Los textos del `<nav>` son "Acerca de" / "Index" en vez de "Inicio" / "Acerca de", y además el orden de los enlaces está invertido entre `index.html` y `acercade.html`.
- La dirección del nodo en el `<footer>` no coincide con la pedida en el enunciado (Viedma, Río Negro).
- La biografía no está dividida en dos secciones propias: una de las dos `<section>` del `<article>` es en realidad la lista de tecnologías.
- El mensaje de commit del TP2 difiere del exacto pedido (falta el `:` y cambia "vinculacion" por "vinculaciones").
- Queda un archivo de captura del Lab 1 sin limpiar en la raíz del repo.
- Todo lo demás (CSS, imagen, GitHub Pages, estructura semántica general) está resuelto correctamente.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 3 |
| Personalización (token + `<h1>`) | 10 | 9 |
| Tarea 1 — `index.html` | 25 | 19 |
| Tarea 2 — `acercade.html` | 30 | 20 |
| Tarea 3 — `styles.css` y commit | 10 | 9 |
| Estructura de archivos | 5 | 4 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 8 |
| **TOTAL** | **100** | **77** |
