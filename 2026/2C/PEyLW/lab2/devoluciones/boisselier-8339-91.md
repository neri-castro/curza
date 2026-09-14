# Devolución Lab 2 — Sara Celeste Boisselier

## Datos identificatorios

- **Nombre:** Sara Celeste Boisselier
- **Legajo:** N° CURZA 8691
- **Token:** boisselier-8339-91
- **Repositorio:** https://github.com/SaraBoisselier/peylw-2026-practicos-boisselier-8339-91
- **GitHub Pages:** https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/

## ⚠️ Hallazgo crítico: el TP2 no está en la rama `main` y el enlace entregado no lo declara

Todo el trabajo del Lab 2 (`acercade.html`, `styles.css`, `img/mi_personaje.png`, y las
versiones nuevas de `index.html`, `README.md` y `REFLEXION.md`) está commiteado
únicamente en la rama `lab2`. La rama `main` (rama por defecto) sigue teniendo solo el
`index.html` viejo del Lab 1, `README.md`, `REFLEXION.md` y una carpeta `capturas/`
residual.

El enlace entregado en `entregas.md` no declara ninguna rama. Cualquiera que abra ese
enlace o clone el repositorio sin buscar en otras ramas ve únicamente la entrega del Lab
1. GitHub Pages sí está configurado para desplegar desde `lab2` (el sitio publicado
funciona correctamente y responde 200 en todos sus archivos). Se penaliza en
"Estructura de archivos".

La corrección de contenido a continuación se hizo sobre el trabajo real (rama `lab2`,
que es lo que está publicado).

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: boisselier-8339-91 -->` exacto e idéntico en `index.html` y `acercade.html`. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Sara Celeste Boisselier - boisselier-8339-91` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` descriptivo y personalizado. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas correctas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos `<p>`, pero ninguno explica realmente el sitio: uno dice que es su primera página y el otro es una broma ("Nota importante: No juzgar🐱"). No cumple con "párrafos explicativos del sitio". |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Un solo párrafo, real y específico (menciona que complementa la Licenciatura en Nutrición con Desarrollo Web), pero el enunciado pide mínimo dos párrafos divididos en dos `<section>` de biografía; acá la segunda `<section>` del artículo es la lista de tecnologías, no continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Ruta relativa `img/mi_personaje.png` válida (200 en producción), `alt="Mi keko de Hartico/Habbo"` específico y personalizado, `figcaption` coherente. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 3 tecnologías, en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body` (font-family y background-color), vinculado en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye todos los archivos del TP2. |
| Estructura de archivos correcta | ❌ | El TP2 completo vive únicamente en la rama `lab2`, no declarada en el enlace entregado (ver hallazgo crítico arriba). El árbol de esa rama sí coincide con lo pedido (sin residuos de `capturas/`). |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/mi_personaje.png` responden 200 en producción; la navegación funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repo real (nombre de imagen y `alt` exactos) y están bien justificadas. |

## Observaciones puntuales

- **Rama sin declarar (crítico):** el enlace entregado no especifica rama; la vista por defecto (`main`) no tiene el TP2, solo la entrega vieja del Lab 1.
- Los dos párrafos de bienvenida en `index.html` no cumplen la función pedida (explicar el sitio); uno es una broma sin contenido informativo.
- La biografía de `acercade.html` es real y específica pero de un solo párrafo, sin dividirse en dos secciones de biografía como exige el enunciado.
- El resto (personalización, CSS, commit, imagen, lista de tecnologías, Pages, reflexión) está resuelto correctamente.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 23 |
| Tarea 2 — `acercade.html` | 30 | 26 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 1 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **90** |
