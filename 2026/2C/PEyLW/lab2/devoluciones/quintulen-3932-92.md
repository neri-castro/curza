# Devolución Lab 2 — Carlos Quintulen

## Datos identificatorios

- **Nombre:** Carlos Quintulen (no se declaró apellido materno ni legajo/DNI en `entregas.md`; tomados del README del repo)
- **Legajo:** CURZAS-8092
- **Token:** quintulen-3932-92
- **Repositorio:** https://github.com/CaarlosQ/peylw-2026-practicos-quintulen-3932-92
- **GitHub Pages:** https://caarlosq.github.io/peylw-2026-practicos-quintulen-3932-92/

## ⚠️ Hallazgo crítico: el TP2 no está en la rama `main` y el enlace entregado no lo declara

Todo el trabajo del laboratorio (`acercade.html`, `styles.css`, `img/carlos-quintulen-foto.png`,
y las versiones finales de `index.html`, `README.md` y `REFLEXION.md`) está commiteado
únicamente en la rama `laboratorio_2`. La rama `main` (rama por defecto del repositorio)
sigue teniendo solo `index.html` (versión vieja, sin `<h1>` personalizado ni vínculo a
`styles.css`), `README.md`, `REFLEXION.md` y una carpeta `capturas/` residual del Lab 1.

A diferencia de otros alumnos de esta tanda, el enlace entregado en `entregas.md`
(`.../peylw-2026-practicos-quintulen-3932-92`, sin sufijo de rama) **no declara** la rama
`laboratorio_2`. Cualquiera que abra ese enlace o clone el repositorio sin buscar en otras
ramas ve una entrega incompleta del TP2. GitHub Pages sí está configurado para desplegar
desde `laboratorio_2` (el sitio publicado funciona correctamente), pero el repositorio en sí
no refleja el trabajo en su vista por defecto. Se penaliza en "Estructura de archivos".

La corrección de contenido a continuación se hizo sobre el trabajo real (rama `laboratorio_2`).

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Nombre, legajo, DNI, fecha y enlace al repo presentes; falta el campo "Enlace a la Página en GitHub Pages". |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: quintulen-3932-92-->` presente e idéntico en ambos archivos (falta un espacio antes del cierre `-->`, detalle menor que no afecta el cumplimiento). |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Carlos Quintulen - quintulen-3932-92` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>Bienvenidos a mi espacio</h2>` exacto. Los dos párrafos son reales pero muy meta ("voy a presentar mi biografía"), no explican realmente el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright y token presentes, pero la dirección del nodo dice "CURZAS - UNCo, Ingeniero Jacobacci, Río Negro" en vez de "CURZAS - UNCo, Viedma, Río Negro" como pide el enunciado. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | El `<footer>` de `acercade.html` no es idéntico al de `index.html`: falta la línea con el token (`Token: quintulen-3932-92`) que sí aparece en `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real, personal y bien escrita, menciona explícitamente la Tecnicatura en Desarrollo Web. Sin embargo, todo el texto de biografía está en una sola `<section>`; la segunda `<section>` del artículo es la lista de tecnologías, no continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Funciona correctamente; `alt="Foto de Carlos Quintulen"` es personalizado, aunque podría ser más descriptivo. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 7 tecnologías, bien ubicada en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica pedida, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye los archivos del TP2. |
| Estructura de archivos correcta | ❌ | El TP2 completo vive únicamente en la rama `laboratorio_2`, no declarada en el enlace entregado (ver hallazgo crítico). Además queda una carpeta `capturas/` residual del Lab 1 en la raíz. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | El sitio responde 200 y la navegación funciona correctamente en producción. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas coinciden con el repositorio real y están justificadas, aunque la pregunta 2 solo menciona el motivo de SEO y no accesibilidad. |

## Observaciones puntuales

- **Rama sin declarar (crítico):** el enlace entregado apunta al repositorio sin especificar rama; la vista por defecto (rama `main`) no tiene el TP2. Hay que declarar explícitamente la rama `laboratorio_2` en la entrega, o mejor, mergearla a `main`.
- La dirección del nodo en el `<footer>` de ambas páginas dice "Ingeniero Jacobacci" en lugar de "Viedma", que es lo que pide el enunciado textualmente.
- El `<footer>` de `acercade.html` omite la línea del token que sí tiene `index.html`; no son "idénticos" como exige la consigna.
- La biografía, aunque de buen contenido, no está dividida en dos secciones como pide el enunciado (la segunda sección es la lista de tecnologías).
- Falta el campo "Enlace a la Página en GitHub Pages" en el README del repositorio.
- Queda una carpeta `capturas/` del Lab 1 sin limpiar en la raíz del repositorio.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 4 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 21.5 |
| Tarea 2 — `acercade.html` | 30 | 22 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 1 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 9 |
| **TOTAL** | **100** | **83** |
