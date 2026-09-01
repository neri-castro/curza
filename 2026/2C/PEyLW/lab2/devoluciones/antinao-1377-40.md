# Devolución Lab 2 — Diego Antinao

## Datos identificatorios

- **Nombre:** Diego Antinao (declarado en `README.md` como "Diego Antinao"; el usuario de GitHub es `antinaodiegojavier`)
- **Legajo:** CURZA-10140
- **Token:** antinao-1377-40
- **Repositorio:** https://github.com/antinaodiegojavier/peylw-2026-practicos-antinao-1377-40
- **GitHub Pages:** https://antinaodiegojavier.github.io/peylw-2026-practicos-antinao-1377-40/

> **Nota metodológica:** el enlace enviado en la entrega (`entregas.md`) no incluía
> nombre, legajo ni DNI; estos datos se tomaron del `README.md` dentro del repositorio.

## ⚠️ Hallazgo crítico: el trabajo del TP2 no está en la rama `main`

Todo el contenido de este laboratorio (`acercade.html`, `css/styles.css`,
`img/img_mi_foto.jpg.jpeg`, y las versiones corregidas de `index.html`,
`README.md` y `reflexion.md`) fue commiteado **únicamente en la rama
`lab2`**, que nunca se fusionó a `main`. La rama `main` (rama por defecto
del repositorio) sigue teniendo la versión del **Lab 1**: `index.html` sin
estructura semántica, con el `<h1>` viejo (solo el nombre) y sin
`acercade.html` ni `styles.css`.

GitHub Pages, en este caso puntual, está configurado para desplegar desde
la rama `lab2` (no la default), por lo que el sitio publicado sí muestra el
trabajo completo. Pero si alguien clona el repositorio o revisa la rama
`main` (el comportamiento estándar y esperado), **no va a encontrar el TP2
entregado**. Esto es un problema de organización del repositorio que debe
corregirse: hay que mergear `lab2` a `main` cuanto antes.

La corrección de contenido a continuación se hizo igual sobre el trabajo
real (rama `lab2`, que es lo que está publicado), pero se penaliza este
punto en "Estructura de archivos".

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Todos los campos están completos, pero el enlace al repositorio tiene un espacio interno que rompe la URL (`.../antinaodiegojavier/    peylw-2026-practicos-...`) y falta el campo "Enlace a la Página en GitHub Pages" en la versión de `main` (sí está en `lab2`). |
| Personalización — Token en comentario (ambos archivos) | ❌ | En `index.html` el comentario es `<!--antinao-1377-40-->`, sin la etiqueta `TOKEN-ALUMNO:` que pide el enunciado. En `acercade.html` el comentario **no existe**. |
| Personalización — `<h1>` exacto (ambos archivos) | ❌ | El `<h1>` de `index.html` es `Mi Laboratorio de HTML5`, no `Portal de Diego Antinao - antinao-1377-40`. `acercade.html` directamente no tiene `<h1>` en su `<header>`. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ⚠️ | `lang="es"` y `<title>` correctos, pero el `<meta charset="UTF-8"` **no cierra con `>`**, lo que hace que el navegador fusione ese meta con el siguiente `<meta name="viewport">` y este último no se aplique como tag independiente. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | Existe y contiene `<h1>` y `<nav>`, pero el `<h1>` no es el texto pedido (ver arriba). |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas correctas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | Usa `<article><header><h2>` en vez de `<section>` como pide el enunciado. El texto de bienvenida (dos párrafos reales) sí está bien. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Contenido correcto (copyright, dirección del nodo, token), pero el `<footer>` está ubicado **después** del `</body>` de cierre en el código fuente (HTML inválido, aunque los navegadores lo reubican al renderizar). |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | El `<header>` de `acercade.html` solo tiene `<nav>`, sin el `<h1>` ni el comentario de token que sí tiene `index.html`. No son consistentes. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | La biografía es real, personal y bien escrita (dos párrafos, menciona la Tecnicatura en Desarrollo Web), pero está toda en **una sola** `<section>`, no dividida en dos como pide el enunciado. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Funciona correctamente, `alt` descriptivo y personalizado, `figcaption` con contexto. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ⚠️ | Contenido correcto (6 tecnologías), pero está envuelta en un `<nav>`, uso semántico incorrecto (un listado de intereses no es navegación). |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ⚠️ | El archivo está en `css/styles.css`, **no en la raíz** como pide explícitamente el enunciado. Sí está correctamente vinculado en ambas páginas y funciona (200 en producción). |
| Tarea 3 — Commit con mensaje exacto | ⚠️ | `TP2 : Estructuras HTML y vinculacion de estilos` — tiene un espacio de más antes de los dos puntos. |
| Estructura de archivos correcta | ❌ | El TP2 completo vive en la rama `lab2`, no en `main` (ver hallazgo crítico arriba). Además `styles.css` está en una subcarpeta `css/` en lugar de la raíz. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | El sitio responde 200 y los enlaces de navegación funcionan correctamente en producción (Pages está configurado sobre la rama `lab2`). |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas y coinciden con el contenido real del repositorio. |

## Observaciones puntuales

- **Rama sin mergear (crítico):** todo el TP2 está en `lab2`, no en `main`. Mergear a la brevedad; de lo contrario cualquier revisión que no busque en todas las ramas concluye que no se entregó nada.
- **Comentario de token incompleto/ausente:** falta el formato `<!-- TOKEN-ALUMNO: <token> -->` en `index.html` (falta la etiqueta) y en `acercade.html` (falta directamente).
- **`<h1>` no cumple el formato exacto pedido** en ninguna de las dos páginas — es el punto de mayor peso perdido en la personalización.
- **Bug de markup:** `<meta charset="UTF-8"` sin cerrar en el `<head>` de ambas páginas, lo que anula el `<meta viewport>` siguiente.
- **`<footer>` fuera de `<body>`** en el código fuente de ambas páginas (los navegadores lo corrigen al renderizar, pero es HTML inválido).
- **`styles.css` en `css/` en vez de la raíz**, contrario a la consigna explícita.
- Biografía de `acercade.html`: buena en contenido, pero no está dividida en dos `<section>` como pide el enunciado.
- Lista de tecnologías envuelta incorrectamente en `<nav>`.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 4 |
| Personalización (token + `<h1>`) | 10 | 2 |
| Tarea 1 — `index.html` | 25 | 18 |
| Tarea 2 — `acercade.html` | 30 | 22 |
| Tarea 3 — `styles.css` y commit | 10 | 7 |
| Estructura de archivos | 5 | 1 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **69** |
