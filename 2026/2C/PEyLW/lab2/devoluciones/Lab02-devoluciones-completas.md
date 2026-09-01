# Devoluciones Lab 2 — Estructura y Semántica Web con HTML5

## Tabla resumen — Lab 2

| Token | Nombre | Nota |
|---|---|---|
| fierro-6000-26 | Diego Esteban Vergara Fierro | 91 |
| antinao-1377-40 | Diego Antinao | 69 |

---

# Devolución Lab 2 — Diego Esteban Vergara Fierro

## Datos identificatorios

- **Nombre:** Diego Esteban Vergara Fierro
- **Legajo:** CURZA-1626
- **Token:** fierro-6000-26
- **Repositorio:** https://github.com/DiegoFierro/peylw-2026-practicos-fierro-6000-26/
- **GitHub Pages:** https://diegofierro.github.io/peylw-2026-practicos-fierro-6000-26/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Todos los campos completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: fierro-6000-26 -->` presente y con formato exacto al inicio del `<body>` en `index.html` y `acercade.html`. |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | `Portal de Diego Esteban Vergara Fierro - fierro-6000-26.` — agrega un punto final que no pide el enunciado; el resto coincide exactamente y es igual en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `<html lang="es">`, `charset utf-8` y `<title>` descriptivo correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas correctas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<section>` con `<h2>Bienvenidos a mi espacio</h2>` (texto exacto) y dos párrafos explicativos reales. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Solo hay **un párrafo** de biografía (el enunciado pide mínimo dos) y es genérico: no menciona explícitamente el interés por la Tecnicatura en Desarrollo Web. La segunda `<section>` del artículo es la lista de tecnologías, no continuación de la biografía, por lo que la biografía en sí no queda "dividida en dos secciones" como pide el enunciado. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Funciona correctamente (ruta relativa `img/mi_foto.jpg`, imagen válida). El `alt` ("Fotografía de perfil personal") y el `figcaption` son genéricos, podrían ser más específicos/personalizados. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` correcto y bien ubicado semánticamente. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica pedida, y vinculado con `<link>` en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra. |
| Estructura de archivos correcta | ✅ | Coincide exactamente con el árbol pedido en el enunciado. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/mi_foto.jpg` responden 200 en producción. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repo real y están bien justificadas. |

## Observaciones puntuales

- El `<h1>` de ambas páginas tiene un punto final agregado (`...fierro-6000-26.`) que el enunciado no pide; no afecta la identidad pero no es una copia exacta de la consigna.
- La biografía en `acercade.html` es de un solo párrafo y de tono genérico ("Soy estudiante universitario enfocado en el aprendizaje y desarrollo de tecnologías web..."), sin mención explícita a la Tecnicatura en Desarrollo Web. El enunciado pide explícitamente "una biografía real de al menos dos párrafos sobre su interés por la Tecnicatura en Desarrollo Web" (sección 3.1) y que esté "dividida en dos secciones" (Tarea 2). Ninguna de las dos condiciones se cumple del todo.
- El `alt` y el `figcaption` de la foto son válidos pero genéricos; podrían personalizarse más (nombre, contexto de la foto).
- Todo lo demás (estructura semántica, navegación, CSS, commit, Pages, reflexión) está bien resuelto y sin errores técnicos.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 9 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 22 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **91** |

---

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
