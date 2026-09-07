# Devolución Lab 2 — Sofia Pereyra

## Datos identificatorios

- **Nombre:** Sofia Pereyra
- **Legajo:** CURZA-9984
- **Token:** pereyra-1554-84
- **Repositorio:** https://github.com/sofiaquino567-bot/peylw-2026-practicos-pereyra-1554-84/tree/Laboratorio2
- **GitHub Pages:** https://sofiaquino567-bot.github.io/peylw-2026-practicos-pereyra-1554-84/

## Nota metodológica

El trabajo del TP2 está en la rama `Laboratorio2`, no en `main`. El enlace entregado
declara explícitamente esa rama, por lo que no se considera ocultamiento; se descuenta
levemente en "Estructura de archivos" por no estar mergeado a la rama principal.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ❌ | En `index.html` el comentario es `<!-- TOKEN-ALUMNO: pereyra-1454-84 -->` — **token con dígitos transpuestos** (1454 en vez de 1554). En `acercade.html` el comentario **no existe**. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Sofia Pereyra - pereyra-1554-84` (con el token correcto) idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ❌ | `lang="es"` y charset UTF-8 correctos, pero el `<title>` es literalmente "Document" — el placeholder por defecto del editor, sin personalizar. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | El `<h1>` es correcto, pero dentro del `<header>` también está el `<link rel="stylesheet">`, que debería estar en el `<head>` del documento, no en el `<body>`. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas correctas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, con dos párrafos reales que sí explican el propósito del sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright y dirección correctos, pero el token mostrado es `[pereyra-1454-84]`, con los mismos dígitos transpuestos que el comentario. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Estructuralmente idénticos a `index.html` (incluido el mismo defecto de ubicación del `<link>` y el mismo token incorrecto en el footer). |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Un solo párrafo breve y genérico ("me interesa aprender sobre programación y diseño web"), sin desarrollo real sobre su interés en la Tecnicatura. La segunda `<section>` del artículo es la lista de intereses/tecnologías, no continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ⚠️ | Imagen funciona, `alt="Foto personal de Sofia"` es aceptable, pero el `<figcaption>` dice literalmente `Foto "personal"` con comillas sueltas, como si fuera un texto de prueba sin terminar de redactar. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 4 tecnologías, bien ubicada en su propia sección. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ❌ | El archivo `styles.css` existe en la raíz con la regla básica, pero el `<link>` está ubicado dentro del `<header>` (en el `<body>`), no en el `<head>` del documento, en **ambas** páginas. |
| Tarea 3 — Commit con mensaje exacto | ❌ | No existe en todo el historial (todas las ramas) ningún commit con el mensaje `TP2: Estructuras HTML y vinculacion de estilos` ni una variación cercana. El contenido del TP2 se agregó en el commit "Agrego archivos de Laboratorio 2", con otro mensaje. |
| Estructura de archivos correcta | ⚠️ | El árbol de la rama `Laboratorio2` coincide exactamente con lo pedido, pero no está mergeado a `main`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200 en producción y la navegación funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repositorio real y están muy bien justificadas (la pregunta 2 cubre claridad de código, SEO y accesibilidad). |

## Observaciones puntuales

- **Token incorrecto en dos lugares:** el comentario de `index.html` y el texto del `<footer>` en ambas páginas usan "pereyra-1454-84" en vez de "pereyra-1554-84" (dígitos 4 y 5 invertidos). El `<h1>`, en cambio, sí tiene el token correcto.
- **Comentario de token ausente en `acercade.html`.**
- **`<title>` de `index.html` sin personalizar:** queda como "Document", el placeholder por defecto.
- **`<link rel="stylesheet">` mal ubicado:** está dentro del `<header>` del `<body>` en ambas páginas, no en el `<head>` del documento. Aunque los navegadores actuales suelen aplicar igual el CSS, no es la ubicación válida ni la que pide el enunciado.
- **No existe el commit con el mensaje exacto del TP2** en ningún punto del historial ni de ninguna rama; el contenido del TP2 se subió bajo otros mensajes de commit.
- La biografía es real pero muy breve y genérica; no llega a los dos párrafos ni a la división en dos secciones que pide la consigna.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 6 |
| Tarea 1 — `index.html` | 25 | 19 |
| Tarea 2 — `acercade.html` | 30 | 20 |
| Tarea 3 — `styles.css` y commit | 10 | 4 |
| Estructura de archivos | 5 | 3.5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **73** |
