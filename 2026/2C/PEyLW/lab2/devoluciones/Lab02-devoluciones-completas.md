# Devoluciones Lab 2 — Estructura y Semántica Web con HTML5

## Tabla resumen — Lab 2

| Token | Nombre | Nota |
|---|---|---|
| fierro-6000-26 | Diego Esteban Vergara Fierro | 91 |
| robles-3587-46 | Matías Leonardo Ezequiel Robles | 78 |
| quintulen-3932-92 | Carlos Quintulen | 83 |
| bastias-1018-59 | Marité Bastías | 76 |
| pereyra-1554-84 | Sofia Pereyra | 73 |
| antinao-1377-40 | Diego Antinao | 69 |
| klug-3903-68 | Robertino Klug | 66 |
| vela-9972-35 | Sandra Vela | 92 |
| apelahnz-2743-10 | Santiago Valentín Apelahnz | 72 |
| hidalgo-4589-59 | Alexis Hidalgo | 68 |
| chavarria-7037-55 | Javier Chavarria | 98 |
| boisselier-8339-91 | Sara Celeste Boisselier | 90 |
| reyes-6775-42 | Isaías Reyes Arzamendia | 94 |
| reynoso-4260-07 | Ramiro Javier Reynoso Bascary | 77 |
| cobis-5580-89 | Rolando Cobis | 100 |
| garciadiaz-9325-19 | Luciano García Díaz | 71 |
| camandulle-5746-93 | Fernanda Camandulle | 98.5 |
| tiradomoreira-5676-19 | Carla Tirado Moreira | 98 |
| cambarieri-8763-78 | Matías Cambarieri Gentile | 75.5 |
| duarte-6881-34 | Elizabeth Priscila Duarte Nuñez | 86 (antes: 37) |
| manquenao-2747-93 | Tatiana Manquenao | 50.5 (antes: 44.5) |

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

# Devolución Lab 2 — Matías Leonardo Ezequiel Robles

## Datos identificatorios

- **Nombre:** Matías Leonardo Ezequiel Robles
- **Legajo:** 4646
- **Token:** robles-3587-46
- **Repositorio:** https://github.com/JalAkat/peylw-2026-practicos-robles-3587-46/
- **GitHub Pages:** https://jalakat.github.io/peylw-2026-practicos-robles-3587-46/ (no declarado en la entrega ni en el README; inferido por convención y verificado en vivo)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Falta el campo obligatorio "Enlace a la Página en GitHub Pages" (no está ni en el README ni en la entrega). |
| Personalización — Token en comentario (ambos archivos) | ⚠️ | `<!-- robles-3587-46 -->` en ambos archivos: falta la etiqueta `TOKEN-ALUMNO:` que exige el enunciado. Consistente en los dos archivos pero con formato incorrecto. |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | Correcto en `index.html`. En `acercade.html` el `<h1>` es `Acerca de mí`, no el formato pedido. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` descriptivo correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Presente con el `<h1>` correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | El enlace "Inicio" apunta a `href="#"` en vez de `index.html`. No rompe la navegación (es la página actual) pero no sigue la consigna literal. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>` dice "Bienvenido a mi espacio." (singular y con punto final) en vez de "Bienvenidos a mi espacio" exacto. Los dos párrafos son reales pero genéricos. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | El `<h1>` no coincide con el de `index.html`. El `<nav>` tampoco es idéntico: aquí es "Acerca de mí" el que apunta a `href="#"`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real y personal, menciona explícitamente la carrera. Dividida en dos `<section>`, pero la lista de lenguajes está mezclada dentro de la primera. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Dos imágenes con `alt` personalizado y rutas relativas correctas, cargan en producción. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ⚠️ | Lista correcta pero embebida dentro de la sección de biografía. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ⚠️ | El archivo se llama `estilos.css`, no `styles.css`. Contiene la regla básica y está correctamente vinculado con el nombre real en ambas páginas. |
| Tarea 3 — Commit con mensaje exacto | ⚠️ | `TP2: Estructuras HTML y vinculación de estilos.` — agrega tilde y punto final. |
| Estructura de archivos correcta | ⚠️ | Coincide salvo por `estilos.css` en vez de `styles.css`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200 en producción; la navegación funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Preguntas 1 y 2 bien respondidas. Pregunta 3 explica el razonamiento pero no describe una verificación concreta realizada. |

## Observaciones puntuales

- El comentario de token no usa el formato `<!-- TOKEN-ALUMNO: <token> -->`; falta la etiqueta en ambos archivos.
- El `<h1>` de `acercade.html` no es el "Portal de..." exigido.
- El README no declara el enlace a GitHub Pages en ningún lugar.
- `estilos.css` en vez de `styles.css`: el enunciado pide ese nombre exacto.
- El `<h2>` de bienvenida no coincide textualmente con "Bienvenidos a mi espacio".
- Los enlaces "actuales" de cada página usan `href="#"` en lugar de apuntar al archivo real, lo que además hace que el `<nav>` no sea idéntico entre páginas.
- El mensaje de commit tiene tilde y punto final agregados.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 4 |
| Personalización (token + `<h1>`) | 10 | 4.5 |
| Tarea 1 — `index.html` | 25 | 22 |
| Tarea 2 — `acercade.html` | 30 | 22.5 |
| Tarea 3 — `styles.css` y commit | 10 | 7.5 |
| Estructura de archivos | 5 | 3.5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 8.5 |
| **TOTAL** | **100** | **78** |

---

# Devolución Lab 2 — Carlos Quintulen

## Datos identificatorios

- **Nombre:** Carlos Quintulen (no se declaró apellido materno ni legajo/DNI en `entregas.md`; tomados del README del repo)
- **Legajo:** CURZAS-8092
- **Token:** quintulen-3932-92
- **Repositorio:** https://github.com/CaarlosQ/peylw-2026-practicos-quintulen-3932-92
- **GitHub Pages:** https://caarlosq.github.io/peylw-2026-practicos-quintulen-3932-92/

## ⚠️ Hallazgo crítico: el TP2 no está en la rama `main` y el enlace entregado no lo declara

Todo el trabajo del laboratorio está commiteado únicamente en la rama `laboratorio_2`. La
rama `main` (rama por defecto) sigue teniendo solo `index.html` (versión vieja, sin `<h1>`
personalizado ni vínculo a `styles.css`), `README.md`, `REFLEXION.md` y una carpeta
`capturas/` residual del Lab 1.

A diferencia de otros alumnos de esta tanda, el enlace entregado en `entregas.md` (sin
sufijo de rama) **no declara** la rama `laboratorio_2`. Cualquiera que abra ese enlace o
clone el repositorio sin buscar en otras ramas ve una entrega incompleta del TP2. GitHub
Pages sí está configurado para desplegar desde `laboratorio_2` (el sitio publicado
funciona correctamente). Se penaliza en "Estructura de archivos".

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Nombre, legajo, DNI, fecha y enlace al repo presentes; falta "Enlace a la Página en GitHub Pages". |
| Personalización — Token en comentario (ambos archivos) | ✅ | Presente e idéntico en ambos archivos (falta un espacio antes del cierre `-->`, detalle menor). |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Carlos Quintulen - quintulen-3932-92` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ⚠️ | `<h2>` exacto. Los dos párrafos son reales pero muy meta, no explican realmente el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright y token presentes, pero la dirección dice "Ingeniero Jacobacci" en vez de "Viedma" como pide el enunciado. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | El `<footer>` de `acercade.html` no es idéntico: falta la línea con el token que sí aparece en `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real y bien escrita, menciona explícitamente la Tecnicatura. Todo el texto está en una sola `<section>`; la segunda es la lista de tecnologías. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | `alt="Foto de Carlos Quintulen"` personalizado, aunque podría ser más descriptivo. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 7 tecnologías, en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | Coincide letra por letra e incluye los archivos del TP2. |
| Estructura de archivos correcta | ❌ | El TP2 vive únicamente en la rama `laboratorio_2`, no declarada en el enlace entregado. Queda además una carpeta `capturas/` residual del Lab 1. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | El sitio responde 200 y la navegación funciona correctamente. |
| Reflexión — 3 preguntas respondidas | ✅ | Coinciden con el repositorio real; la pregunta 2 solo menciona SEO, no accesibilidad. |

## Observaciones puntuales

- **Rama sin declarar (crítico):** el enlace entregado no especifica rama; la vista por defecto no tiene el TP2.
- La dirección del nodo en el `<footer>` dice "Ingeniero Jacobacci" en lugar de "Viedma".
- El `<footer>` de `acercade.html` omite la línea del token.
- La biografía no está dividida en dos secciones como pide el enunciado.
- Falta el campo de enlace a GitHub Pages en el README.
- Queda una carpeta `capturas/` sin limpiar.

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

---

# Devolución Lab 2 — Marité Bastías

## Datos identificatorios

- **Nombre:** Marité Bastías
- **Legajo:** CURZA-9959
- **Token:** bastias-1018-59
- **Repositorio:** https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59/tree/laboratorio_2
- **GitHub Pages:** https://marite28.github.io/peylw-2026-practicos-bastias-1018-59/

## Nota metodológica

El trabajo está en la rama `laboratorio_2`, declarada explícitamente en el enlace
entregado (no se considera ocultamiento); se descuenta levemente en "Estructura de
archivos" por no estar mergeado a la rama principal.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ❌ | Faltan Legajo/Matrícula, DNI, enlace al repositorio y enlace a GitHub Pages. |
| Personalización — Token en comentario (ambos archivos) | ⚠️ | `<!--token-alumno: bastias-1018-59-->`: formato en minúsculas y sin los espacios exactos pedidos. Consistente en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | `Portal de Marité - bastias-1018-59`: falta el apellido, no es el nombre completo. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | Presente, pero el `<h1>` no tiene el nombre completo. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | Rutas correctas, pero el texto es "inicio" en minúscula. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ❌ | Usa `<seccion>` (sin la "t"), que no es la etiqueta semántica `<section>` de HTML5. `<h2>` exacto, dos párrafos, pero más biográficos que explicativos del sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright dice solo "Marité" (falta apellido); dirección exacta; token presente. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Real y personal, dividida en dos `<section>`, mencionando explícitamente la Tecnicatura. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ❌ | El `<img>` no cierra con `>` antes de `<figcaption>`, lo que rompe la etiqueta `<figcaption>` como elemento propio. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 5 tecnologías, correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica, vinculado en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ⚠️ | Doble espacio entre "y" y "vinculacion". El `<link>` de `acercade.html` y la imagen se agregaron en commits posteriores. |
| Estructura de archivos correcta | ⚠️ | El árbol coincide, pero el trabajo no está mergeado a `master`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200 y la navegación funciona. |
| Reflexión — 3 preguntas respondidas | ✅ | Correctas, coinciden con el repo real y bien justificadas. |

## Observaciones puntuales

- README incompleto: falta Legajo, DNI, y ambos enlaces.
- `<h1>` y copyright con nombre incompleto (falta "Bastías").
- Bug de markup grave: `<img>` sin cerrar antes de `<figcaption>`.
- `<seccion>` en vez de `<section>` en `index.html`: no es una etiqueta HTML5 válida.
- El resto de la estructura está resuelto correctamente.

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

---

# Devolución Lab 2 — Sofia Pereyra

## Datos identificatorios

- **Nombre:** Sofia Pereyra
- **Legajo:** CURZA-9984
- **Token:** pereyra-1554-84
- **Repositorio:** https://github.com/sofiaquino567-bot/peylw-2026-practicos-pereyra-1554-84/tree/Laboratorio2
- **GitHub Pages:** https://sofiaquino567-bot.github.io/peylw-2026-practicos-pereyra-1554-84/

## Nota metodológica

El trabajo está en la rama `Laboratorio2`, declarada explícitamente en el enlace
entregado; se descuenta levemente en "Estructura de archivos" por no estar mergeado a
`main`.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ❌ | En `index.html`: `pereyra-1454-84` — dígitos transpuestos (1454 en vez de 1554). En `acercade.html` el comentario **no existe**. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Sofia Pereyra - pereyra-1554-84` (token correcto) idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ❌ | `<title>` es literalmente "Document", el placeholder por defecto sin personalizar. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | `<h1>` correcto, pero el `<link rel="stylesheet">` está dentro del `<header>` en vez de en el `<head>`. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright y dirección correctos, pero el token muestra `[pereyra-1454-84]`, dígitos transpuestos. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Estructuralmente idénticos (incluidos los mismos defectos). |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Un solo párrafo breve y genérico. La segunda `<section>` es la lista de intereses, no continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ⚠️ | Imagen funciona, `alt` aceptable, pero `<figcaption>` dice literalmente `Foto "personal"` con comillas sueltas. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 4 tecnologías, correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ❌ | El `<link>` está dentro del `<header>` (en el `<body>`), no en el `<head>`, en ambas páginas. |
| Tarea 3 — Commit con mensaje exacto | ❌ | No existe en todo el historial ningún commit con el mensaje exacto del TP2. |
| Estructura de archivos correcta | ⚠️ | El árbol coincide, pero no está mergeado a `main`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200 y la navegación funciona. |
| Reflexión — 3 preguntas respondidas | ✅ | Correctas y muy bien justificadas. |

## Observaciones puntuales

- Token incorrecto (dígitos invertidos) en el comentario de `index.html` y en el footer de ambas páginas; el `<h1>` sí tiene el token correcto.
- Comentario de token ausente en `acercade.html`.
- `<title>` de `index.html` sin personalizar ("Document").
- `<link rel="stylesheet">` mal ubicado en ambas páginas.
- No existe el commit con el mensaje exacto del TP2 en ningún punto del historial.
- Biografía real pero muy breve y genérica.

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

---

# Devolución Lab 2 — Robertino Klug

## Datos identificatorios

- **Nombre:** Robertino Klug
- **Legajo:** CURZA-10268
- **Token:** klug-3903-68
- **Repositorio:** https://github.com/Robertino512/peylw-2026-practicos-klug-3903-68/tree/lab2
- **GitHub Pages:** https://robertino512.github.io/peylw-2026-practicos-klug-3903-68/

## Nota metodológica

El trabajo está en la rama `lab2`, declarada explícitamente en el enlace entregado; se
descuenta levemente en "Estructura de archivos" por no estar mergeado a `main`.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos. |
| Personalización — Token en comentario (ambos archivos) | ❌ | `Klug-3909-68` en ambos archivos: **dígitos incorrectos** (3909 en vez de 3903), además de mayúscula. Error real de token. |
| Personalización — `<h1>` exacto (ambos archivos) | ❌ | `index.html`: "Pagina principal". `acercade.html`: "Pagina bibliografica de Robertino". Ninguna coincide con el formato pedido. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<header>` | ❌ | Falta `</header>` de cierre: envuelve también `<nav>`, `<main>` y `<footer>`. Además el `<h1>` no tiene el formato pedido. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | Rutas correctas, pero el texto es "Principal (esta pagina)"/"Biografia" en vez de "Inicio"/"Acerca de". |
| Tarea 1 — `index.html`: `<main>` bienvenida | ❌ | Anidado dentro del `<header>` sin cerrar. `<h2>` exacto, pero un solo párrafo (mínimo pedido: dos). |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | También anidado dentro del `<header>`. Copyright sin apellido, dirección exacta, token con dígitos incorrectos. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ❌ | El `<h1>` no coincide entre páginas. Además, en `acercade.html` el `</header>` sí cierra correctamente, a diferencia de `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Biografía real, extensa y personal, dividida en dos secciones, mencionando explícitamente el motivo de elegir la Tecnicatura. La mejor de esta tanda. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ⚠️ | Nombre de imagen con espacios sin codificar en el `src`; funciona igual (200 verificado en producción). `alt` personalizado. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ⚠️ | Contenido correcto, pero `<h3>` metido dentro del `<ul>` (HTML inválido) y la lista queda fuera de `<main>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ⚠️ | Usa el selector de clase `.body` en lugar del selector de elemento `body`; funciona pero no es la regla básica pedida. `<link>` bien ubicado. |
| Tarea 3 — Commit con mensaje exacto | ✅ | Coincide letra por letra e incluye todos los archivos del TP2. |
| Estructura de archivos correcta | ⚠️ | El árbol coincide, pero no está mergeado a `main`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200, incluida la imagen con espacios en el nombre. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Preguntas 1 y 3 concretas. Pregunta 2 casi de una línea, sin desarrollar accesibilidad ni SEO. |

## Observaciones puntuales

- **Token incorrecto (crítico):** comentario y footer de ambas páginas usan dígitos equivocados.
- **`<h1>` no cumple el formato exacto** en ninguna página.
- **Bug estructural grave:** falta `</header>` en `index.html`.
- **`<ul>` con un `<h3>` como hijo directo**, HTML inválido, y ubicada fuera de `<main>`.
- **Nombre de imagen con espacios sin codificar** en el `src`.
- La biografía es sobresaliente: real, bien dividida, con motivación explícita.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 2 |
| Tarea 1 — `index.html` | 25 | 12 |
| Tarea 2 — `acercade.html` | 30 | 21.5 |
| Tarea 3 — `styles.css` y commit | 10 | 9 |
| Estructura de archivos | 5 | 3.5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 8 |
| **TOTAL** | **100** | **66** |

---

# Devolución Lab 2 — Sandra Vela

## Datos identificatorios

- **Nombre:** Sandra Vela (nombre, legajo y DNI no se declararon en `entregas.md`; el nombre se tomó del contenido del repositorio. Legajo y DNI no pudieron determinarse: no figuran en ningún archivo del repositorio)
- **Legajo:** no declarado
- **Token:** vela-9972-35
- **Repositorio:** https://github.com/Shalom198424/peylw-2026-practicos-vela-9972-35/tree/lab2
- **GitHub Pages:** https://shalom198424.github.io/peylw-2026-practicos-vela-9972-35/index.html

## Nota metodológica

El trabajo está en la rama `lab2`, declarada explícitamente en el enlace entregado; se
descuenta levemente en "Estructura de archivos" por no estar mergeado a `main`.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ❌ | El README es una descripción de proyecto, pero **no** es la carátula pedida: no tiene Legajo/Matrícula, DNI ni Fecha de Entrega, ni los enlaces al repositorio o a GitHub Pages como campos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | Exacto, idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Sandra Vela - vela-9972-35` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto, bien cerrado. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | Exacto. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>` exacto, dos párrafos completos que explican el sitio y mencionan la Tecnicatura. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección exacta y token en texto simple. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Real, bien escrita, con dos párrafos completos, pero todo en una sola `<section>` ("Sobre mí"); las otras secciones son la lista de tecnologías y la imagen. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | `alt` descriptivo y personalizado, el mejor de esta tanda. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 10 tecnologías, en su propia sección. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ⚠️ | Falta la "s" de "Estructuras" (singular en vez de plural); por lo demás coincide. |
| Estructura de archivos correcta | ⚠️ | El árbol coincide, pero no está mergeado a `main`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | Todos los archivos responden 200 y la navegación funciona. |
| Reflexión — 3 preguntas respondidas | ✅ | Correctas y muy bien justificadas. |

## Observaciones puntuales

- README no es una carátula: falta Legajo, DNI, Fecha de Entrega y los enlaces como campos explícitos.
- La biografía no está dividida en dos secciones como exige la consigna.
- El mensaje de commit dice "Estructura" en singular en vez de "Estructuras".
- En términos de calidad de código HTML, es la entrega más prolija de esta tanda.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 1 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 28 |
| Tarea 3 — `styles.css` y commit | 10 | 9 |
| Estructura de archivos | 5 | 3.5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **92** |

---

# Devolución Lab 2 — Santiago Valentín Apelahnz

## Datos identificatorios

- **Nombre:** Santiago Valentín Apelahnz
- **Legajo:** CURZA-10010
- **Token:** apelahnz-2743-10
- **Repositorio:** https://github.com/officialsantos/peylw-2026-practicos-apelahnz-2743-10
- **GitHub Pages:** https://officialsantos.github.io/peylw-2026-practicos-apelahnz-2743-10/ (no declarado en la entrega ni en el README; inferido por convención)

## ⚠️ Hallazgo: el repositorio y GitHub Pages responden 404 en la verificación en vivo

Al momento de la corrección, `git clone` sobre el repositorio **funciona correctamente**
(se pudo clonar y verificar todo el contenido descripto en este informe, incluso repitiendo
el clonado en un directorio nuevo). Sin embargo:

- La página del repositorio en `github.com/officialsantos/peylw-2026-practicos-apelahnz-2743-10` responde **404** (verificado con `curl` y con una herramienta de fetch independiente).
- `raw.githubusercontent.com` para archivos de ese repo también responde **404**.
- La URL de GitHub Pages inferida responde **404**.
- La pestaña de repositorios del usuario `officialsantos` no lista este repositorio entre los suyos (aunque esa misma página mostró un error de carga genérico para todos sus repositorios, por lo que podría tratarse de una falla puntual de GitHub y no necesariamente de que el repositorio no exista o sea privado).

Esto es inusual: normalmente si el repositorio es privado, `git clone` anónimo falla. Como
el clonado anónimo funciona, el contenido es real y público a nivel de protocolo git, pero
no se pudo confirmar el acceso vía la interfaz web ni confirmar que GitHub Pages esté
sirviendo el sitio. Siguiendo el criterio de no asumir que "estará bien después", se
registra como incumplimiento del ítem de GitHub Pages y se recomienda que el alumno
verifique la configuración de Pages y la visibilidad del repositorio cuanto antes.

La corrección de contenido a continuación se hizo igual sobre el clon local, que refleja
fielmente lo que el alumno entregó.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Nombre, legajo, DNI, fecha y enlace al repo presentes; falta el campo "Enlace a la Página en GitHub Pages". |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: apelahnz-2743-10 -->` exacto e idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | `Portal de Santiago Apelahnz - apelahnz-2743-10` en ambas páginas: falta el segundo nombre "Valentín" que sí figura en el README como parte del nombre completo. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ⚠️ | `lang="es"` y charset correctos (aunque el `<meta charset="UTF-8" lang="es">` tiene un atributo `lang` inválido en esa etiqueta), pero el `<title>` es "Título de Mi Portal", un placeholder genérico sin personalizar. |
| Tarea 1 — `index.html`: `<header>` | ⚠️ | Presente, pero el `<h1>` no tiene el nombre completo (ver Personalización). |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, con dos párrafos reales que explican bien el propósito del sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | El copyright dice solo "Apelahnz" (apellido, sin nombre); dirección del nodo exacta; token presente en texto simple. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html` en texto y estructura. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real y extensa (cuatro párrafos), menciona explícitamente la Tecnicatura en Desarrollo Web y su trayectoria educativa. Sin embargo, todo el texto biográfico está en una sola `<section>` (que además reutiliza por error el encabezado "Bienvenidos a mi espacio", el mismo texto de `index.html`, en vez de un título propio como "Sobre mí"); la otra `<section>` del artículo contiene solo la imagen. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ❌ | La imagen está en `capturas/mi_img.jpg`, **no en `img/`** como exige el enunciado. Además el `<figure>` **no tiene `<figcaption>`**. El `alt="Mi imagen personal"` es genérico, no describe la imagen en sí. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 4 tecnologías de interés, correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body`, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye todos los archivos del TP2 en un único commit. |
| Estructura de archivos correcta | ❌ | No existe carpeta `img/`: la imagen de perfil quedó en `capturas/`, mezclada con una captura residual del Lab 1 (`config_git.png`). |
| GitHub Pages desplegado y respondiendo 200 | ❌ | La URL de Pages responde 404 al momento de la corrección (ver hallazgo arriba). |
| Reflexión — 3 preguntas respondidas | ⚠️ | Preguntas 1 y 2 bien respondidas, con justificación real. La pregunta 3 explica en términos generales por qué funcionan las rutas relativas, pero no describe una verificación concreta realizada (no menciona haber abierto el navegador, clickeado los enlaces o probado en GitHub Pages). |

## Observaciones puntuales

- **Repositorio y Pages no verificables en vivo (crítico):** ver hallazgo al inicio de este informe. El contenido es real y se pudo revisar vía `git clone`, pero la interfaz web de GitHub y la URL de Pages responden 404.
- **Imagen fuera de `img/`:** está en `capturas/mi_img.jpg`, junto con una captura residual del Lab 1. El enunciado pide explícitamente que la imagen esté dentro de `img/`.
- **Falta `<figcaption>`** en la figura de `acercade.html`.
- El `<h1>` y el copyright omiten parte del nombre completo del alumno (falta "Valentín" en el `<h1>`, falta el nombre de pila en el footer).
- El `<title>` de `index.html` no está personalizado ("Título de Mi Portal").
- La sección de biografía reutiliza por error el título "Bienvenidos a mi espacio" (el mismo de `index.html`) en lugar de un encabezado propio, y no está dividida en dos secciones de biografía como pide la consigna (la segunda sección es solo la imagen).
- El resto (CSS, commit, lista de tecnologías, estructura semántica general) está bien resuelto.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 4 |
| Personalización (token + `<h1>`) | 10 | 9 |
| Tarea 1 — `index.html` | 25 | 21 |
| Tarea 2 — `acercade.html` | 30 | 19 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 1.5 |
| GitHub Pages | 5 | 0 |
| Reflexión | 10 | 7.5 |
| **TOTAL** | **100** | **72** |

---

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

---

# Devolución Lab 2 — Javier Chavarria

## Datos identificatorios

- **Nombre:** Javier Chavarria
- **Legajo:** CURZA-6755
- **Token:** chavarria-7037-55
- **Repositorio:** https://github.com/javi-jav/peylw-2026-practicos-chavarria-7037-55
- **GitHub Pages:** https://javi-jav.github.io/peylw-2026-practicos-chavarria-7037-55/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: chavarria-7037-55 -->` exacto e idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Javier Chavarria - chavarria-7037-55` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` descriptivo correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Real y personal, dividida en dos `<section>`, menciona explícitamente el motivo de elegir la Tecnicatura en Desarrollo Web. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Ruta relativa `img/foto_javier.jpg`, imagen válida (200 en producción). `alt` y `figcaption` incluyen el nombre, aunque son algo escuetos. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 3 tecnologías, ubicada en `<aside>` (uso semántico válido para contenido lateral). |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body`, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye todos los archivos del TP2. |
| Estructura de archivos correcta | ✅ | Coincide exactamente con el árbol pedido; la carpeta `capturas/` residual del Lab 1 fue eliminada en el mismo commit. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/foto_javier.jpg` responden 200 en producción. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repo real y están bien justificadas. |

## Observaciones puntuales

- El `alt` y el `figcaption` de la foto son correctos pero genéricos (solo el nombre); podrían describir mejor la imagen en sí.
- La imagen `img/foto_javier.jpg` pesa ~10 MB sin optimizar; no es un ítem de la rúbrica pero afecta el tiempo de carga real del sitio.
- Todo lo demás (estructura semántica, navegación, CSS, commit, Pages, reflexión) está bien resuelto y sin errores técnicos. Es una de las entregas más prolijas de esta tanda.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 28 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **98** |

---

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

---

# Devolución Lab 2 — Isaías Reyes Arzamendia

## Datos identificatorios

- **Nombre:** Isaías Reyes Arzamendia
- **Legajo:** 8542
- **Token:** reyes-6775-42
- **Repositorio:** https://github.com/isaiasreyesbjj16-ux/peylw-2026-practicos-reyes-6775-42
- **GitHub Pages:** https://isaiasreyesbjj16-ux.github.io/peylw-2026-practicos-reyes-6775-42/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos están presentes y correctos. Detalle menor: falta el cierre `**` en la línea de "Últimos 4 dígitos del DNI" (queda en negrita el resto del documento hasta el siguiente `**`), un error de formato Markdown sin impacto en el contenido. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: reyes-6775-42 -->` exacto e idéntico en `index.html` y `acercade.html`. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Isaías Reyes Arzamendia - reyes-6775-42` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` descriptivo ("Inicio \| Portal de..."). |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio (el primero tiene un error de tipeo: doble espacio y un punto suelto sobrante al final, sin impacto en el contenido). |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo exacta y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real, personal y con dos párrafos que mencionan explícitamente el interés por la Tecnicatura en Desarrollo Web, pero todo el texto está en una sola `<section>` ("Mi biografía"); la segunda `<section>` del artículo es la lista de tecnologías, no continuación de la biografía como pide el enunciado. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Imagen `img/img.png` carga correctamente (ruta relativa, 200 en producción), `alt` y `figcaption` personalizados con el nombre del alumno. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 5 tecnologías, correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body` (font-family y background-color), vinculado en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye `index.html`, `acercade.html`, `styles.css`, `img/mi_foto.png` y `README.md`/`REFLEXION.md` en el mismo commit. |
| Estructura de archivos correcta | ⚠️ | Además de los archivos pedidos, quedan tres residuos sueltos en la raíz del repo: `config_git.png` (captura del Lab 1), `images (2).jfif` (archivo con espacio y paréntesis en el nombre) y `laboratorio1` (archivo sin extensión, de contenido mínimo, de un commit temprano). Ninguno de los tres corresponde a la estructura pedida por el enunciado. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/img.png` responden 200 en producción; la navegación entre "Inicio" y "Acerca de" funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ✅ | Pregunta 1 coincide con el estado real del repo (`img/img.png` y el `alt` declarado). Pregunta 2 bien justificada (accesibilidad, SEO, mantenibilidad). Pregunta 3 describe una verificación concreta en local y tras el despliegue, aunque menciona de forma desactualizada el nombre de archivo anterior de la imagen (`img/mi_foto.png`, ya renombrada a `img.png` en un commit posterior). |

## Observaciones puntuales

- La biografía de `acercade.html` no está dividida en dos secciones propias: la segunda `<section>` del `<article>` es la lista de tecnologías, no una continuación de la biografía.
- Quedan tres archivos residuales en la raíz del repositorio (`config_git.png`, `images (2).jfif`, `laboratorio1`) que no forman parte de la estructura pedida y deberían eliminarse.
- El README tiene un error menor de formato Markdown (negrita sin cerrar) en el campo del DNI.
- La pregunta 3 de `REFLEXION.md` referencia un nombre de archivo de imagen (`mi_foto.png`) que ya no coincide con el actual (`img.png`); no afecta la respuesta a la Pregunta 1, que sí está actualizada.
- Todo lo demás (personalización, estructura semántica, navegación, CSS, commit, Pages) está resuelto correctamente.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 27 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 2 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **94** |

---

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

---

# Devolución Lab 2 — Rolando Cobis

## Datos identificatorios

- **Nombre:** Rolando Cobis
- **Legajo:** CURZA-9389
- **Token:** cobis-5580-89
- **Repositorio:** https://github.com/cRolandoJr/peylw-2026-practicos-cobis-5580-89
- **GitHub Pages:** https://crolandojr.github.io/peylw-2026-practicos-cobis-5580-89/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: cobis-5580-89 -->` exacto e idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Rolando Cobis - cobis-5580-89` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` descriptivo correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Real y personal, dividida en dos `<section>` ("Quién soy" y "Por qué elegí la Tecnicatura en Desarrollo Web"), mencionando explícitamente la carrera. La tercera `<section>` del artículo es la lista de tecnologías. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Ruta relativa `img/rolando-cobis.png`, `alt` específico y descriptivo, `figcaption` presente. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 6 tecnologías, en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body` (font-family y background-color), vinculado en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye todos los archivos del TP2. |
| Estructura de archivos correcta | ✅ | Coincide con el árbol pedido. Queda una carpeta `capturas/` residual del Lab 1 (no forma parte de lo pedido en este TP, pero tampoco está fuera de lugar: es contenido legítimo del Lab 1 que el mismo repo arrastra). |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/rolando-cobis.png` responden 200 en producción. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repo real y están bien justificadas (la pregunta 3 detalla verificación con `curl` en producción, no solo visual). |

## Observaciones puntuales

- Sin errores de contenido ni de markup. Entrega prolija y completa en todos los ítems.
- Único punto a mencionar: la carpeta `capturas/` del Lab 1 sigue en el repo; no afecta la calificación de este TP.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 30 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 2 — Luciano García Díaz

## Datos identificatorios

- **Nombre:** Luciano García Díaz (confirmado en `readme.md`, `index.html`, `acercade.html` y `REFLEXION.md` del repo)
- **Legajo:** CURZA-10019
- **Token:** garciadiaz-9325-19
- **Repositorio:** https://github.com/Lucho-GD/TP2-Estructuras-HTML-y-vinculacion-de-estilos
- **GitHub Pages:** https://lucho-gd.github.io/TP2-Estructuras-HTML-y-vinculacion-de-estilos/

## ⚠️ Hallazgo: repositorio nuevo que no sigue la convención de nombre pedida

En `entregas.md` esta entrega figura sin nombre ni token, solo con los dos enlaces de
arriba. El repositorio se llama `TP2-Estructuras-HTML-y-vinculacion-de-estilos`, **no**
`peylw-2026-practicos-garciadiaz-9325-19` como exige el enunciado y como se usó en el
Lab 1 (con la misma cuenta `Lucho-GD`). El repo `peylw-2026-practicos-garciadiaz-9325-19`
del Lab 1 sigue existiendo y es público, pero el alumno no continuó ahí: creó un
repositorio nuevo y completamente separado para este TP2.

El contenido en sí es identificable sin ambigüedad (nombre, token y datos coinciden en
`readme.md`, `REFLEXION.md` y ambos HTML), así que se corrige igual, pero se penaliza el
incumplimiento de la convención de nombres en el ítem "Estructura de archivos".

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Todos los campos (nombre, legajo, DNI, fecha, token, repo, Pages) completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ❌ | No existe el comentario `<!-- TOKEN-ALUMNO: ... -->` (ni ninguna variante) al inicio del `<body>` en `index.html` ni en `acercade.html`. |
| Personalización — `<h1>` exacto (ambos archivos) | ❌ | `index.html`: `<h1>` es "Laboratorio 2: Estructura y Semantica Web con HTML5" — ni nombre ni token, ni formato "Portal de...". `acercade.html`: `<h1>` es "Luciano Garcia Diaz - garciadiaz-9325-19" — le falta el prefijo "Portal de" y además difiere del de `index.html`. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ⚠️ | `lang="es"` y charset UTF-8 correctos, pero el `<title>` repite el nombre del laboratorio en vez de identificar el portal del alumno. |
| Tarea 1 — `index.html`: `<header>` | ❌ | Existe estructuralmente, pero el `<h1>` no identifica al alumno en absoluto (ver Personalización). |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ⚠️ | Rutas relativas correctas ("Inicio"/"Acerca de"), pero el markup es inválido: cada enlace está envuelto en su propio `<ul><a>...</a></ul>` sin `<li>`, en vez de un único `<ul>` con dos `<li>`. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ⚠️ | Copyright con corchete de plantilla sin remover (`[Luciano Garcia Diaz]`); dirección del nodo y token en texto simple correctos. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ⚠️ | `<nav>` y `<footer>` son idénticos entre páginas; el `<h1>` no lo es (ver Personalización). |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ⚠️ | Biografía real y personal, dos párrafos, menciona explícitamente la Tecnicatura en Desarrollo Web. Sin embargo todo el texto está en un único `<article>` sin dividir en dos `<section>`; la segunda `<section>` del documento es la lista de tecnologías, no continuación de la biografía. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Imagen en `img/img-mifoto.jpg`, ruta relativa correcta, carga en producción. `alt="Foto de Luciano Garcia Diaz"` personalizado con nombre real (podría describir mejor la foto en sí, pero cumple). |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 4 tecnologías, en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con regla de `body` (font-family y background-color), vinculado en el `<head>` de ambos archivos. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` aparece tres veces en el historial, coincide letra por letra e incluye los archivos del TP2. |
| Estructura de archivos correcta | ❌ | El árbol interno del repo es correcto, pero el repositorio en sí no sigue la convención `peylw-2026-practicos-<token>` exigida (ver hallazgo arriba): es un repo nuevo con otro nombre, no una continuación del repo de Lab 1. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/img-mifoto.jpg` responden 200 en producción; la navegación entre páginas funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas: el nombre de imagen y el `alt` declarados coinciden con lo real, la justificación de semántica es sólida (accesibilidad, lectores de pantalla, SEO), y describe una verificación concreta en local y luego en GitHub Pages. |

## Observaciones puntuales

- **Repositorio con nombre no convencional (crítico):** ver hallazgo al inicio. Debe unificarse con el repo `peylw-2026-practicos-garciadiaz-9325-19` usado en Lab 1, o al menos declarar el cambio explícitamente en la entrega.
- **Comentario de token ausente por completo** en ambos archivos HTML, no solo con formato incorrecto: no hay ningún comentario de token.
- **`<h1>` no personalizado en `index.html`** (repite el título del enunciado) y **distinto entre páginas**: es el punto de mayor pérdida de puntaje.
- `<nav>` con markup inválido: `<a>` como hijo directo de `<ul>` sin `<li>`.
- Corchete de plantilla sin remover en el copyright del footer (`[Luciano Garcia Diaz]`).
- Biografía real y bien orientada a la Tecnicatura, pero no dividida en dos secciones como pide la consigna.
- CSS, commit, lista de tecnologías, imagen, GitHub Pages y reflexión están bien resueltos.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 0 |
| Tarea 1 — `index.html` | 25 | 17 |
| Tarea 2 — `acercade.html` | 30 | 23 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 1 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **71** |

---

# Devolución Lab 2 — Fernanda Camandulle

## Datos identificatorios

- **Nombre:** Fernanda Camandulle
- **Legajo:** 10093
- **Token:** camandulle-5746-93
- **Repositorio:** https://github.com/Camandulle/peylw-2026-practicos-camandulle-5746-93/tree/laboratorio-2
- **GitHub Pages:** https://camandulle.github.io/peylw-2026-practicos-camandulle-5746-93/

## Nota metodológica

El trabajo está en la rama `laboratorio-2`, declarada explícitamente en el enlace
entregado (no se considera ocultamiento); se descuenta levemente en "Estructura de
archivos" por no estar mergeado a `main`.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: camandulle-5746-93 -->` exacto e idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Fernanda Camandulle - camandulle-5746-93` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>` descriptivo correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio y mencionan la Tecnicatura. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Real, personal y bien escrita, dividida en dos `<section>` ("Sobre mí" y "Mi interés por el Desarrollo Web"), con mención explícita a la Tecnicatura en Desarrollo Web. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | `img/pic.jpeg`, ruta relativa correcta, `alt` personalizado y específico. `<figcaption>` es solo el nombre, podría ser más descriptivo pero no es genérico. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con 3 tecnologías, en su propia `<section>`. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body` (font-family y background-color), vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye `acercade.html`, `index.html`, `styles.css` e `img/pic.jpeg`. |
| Estructura de archivos correcta | ⚠️ | El árbol coincide (con un `.DS_Store` y una carpeta `capturas/` residuales, sin afectar la evaluación), pero el trabajo no está mergeado a `main`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e `img/pic.jpeg` responden 200 en producción. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas coinciden con el repo real (nombre de imagen y `alt` exactos) y están bien justificadas, incluyendo mención a accesibilidad, SEO y legibilidad del código en la pregunta 2. |

## Observaciones puntuales

- Único señalamiento real: el trabajo vive en la rama `laboratorio-2`, no en `main`.
- Quedan un `.DS_Store` y la carpeta `capturas/` (residual del Lab 1) en la raíz; no forman parte de lo pedido pero no rompen nada.
- Resto de la entrega resuelto de forma completa y prolija, sin errores de markup ni desvíos de la consigna.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 30 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 3.5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **98.5** |

---

# Devolución Lab 2 — Carla Tirado Moreira

## Datos identificatorios

- **Nombre:** Carla Tirado Moreira
- **Legajo:** CURZA-10319
- **Token:** tiradomoreira-5676-19
- **Repositorio:** https://github.com/carlatmoreira98/peylw-2026-practicos-tiradomoreira-5676-19
- **GitHub Pages:** https://carlatmoreira98.github.io/peylw-2026-practicos-tiradomoreira-5676-19/

## ⚠️ Entrega tardía

El cierre del laboratorio fue el 07/09/2026 23:55. El commit con el mensaje exacto del
TP2 (`TP2: Estructuras HTML y vinculacion de estilos`) es del **13/09/2026 15:36**, y hay
dos commits posteriores el mismo día. La entrega es real y completa, pero llegó casi seis
días después del cierre. Se deja constancia; la penalización por atraso queda a criterio
general del curso (no definida en `AGENTS-Lab02.md`).

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los seis campos requeridos están completos y correctos. |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: tiradomoreira-5676-19 -->` exacto e idéntico en ambos archivos. |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ | `Portal de Carla Tirado Moreira - tiradomoreira-5676-19` idéntico en ambas páginas. |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 correctos. `<title>` descriptivo ("Portal de Carla Tirado Moreira"). |
| Tarea 1 — `index.html`: `<header>` | ✅ | Correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas exactas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo exacta y token en texto simple. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Real y personal, dividida en dos `<section>` ("Sobre mí" y "Mi interés por el desarrollo web"), menciona explícitamente la Tecnicatura en Desarrollo Web. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ | Ruta relativa `img/diseno_web_ux.png` válida, `alt` descriptivo y específico, `figcaption` coherente. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ⚠️ | `<ul>` presente y bien ubicado en su propia `<section>`, pero solo tiene 2 ítems (HTML5, CSS); es escueta comparada con el resto de la entrega. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con `font-family` y `background-color` en `body`, vinculado correctamente en ambos `<head>`. |
| Tarea 3 — Commit con mensaje exacto | ✅ | `TP2: Estructuras HTML y vinculacion de estilos` — coincide letra por letra e incluye `index.html`, `acercade.html`, `styles.css` e imagen. |
| Estructura de archivos correcta | ✅ | Coincide con el árbol pedido; `capturas/` es residuo del Lab 1, no penalizado. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html`, `styles.css` e imagen responden 200 en producción; navegación funciona en ambos sentidos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas son correctas, coinciden con el repo real y están bien justificadas (pregunta 3 describe una verificación concreta en local y en Pages). |

## Observaciones puntuales

- **Entrega tardía (ver arriba):** commit de TP2 seis días después del cierre.
- La lista de tecnologías de interés en `acercade.html` tiene solo 2 elementos; podría ser más completa.
- Todo lo demás (estructura semántica, personalización, CSS, commit, Pages, reflexión) está resuelto correctamente y sin errores técnicos.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Personalización (token + `<h1>`) | 10 | 10 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 28 |
| Tarea 3 — `styles.css` y commit | 10 | 10 |
| Estructura de archivos | 5 | 5 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **98** *(entrega tardía, ver nota arriba — penalización a criterio del docente)* |

---

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

---

# Devolución Lab 2 — Elizabeth Priscila Duarte Nuñez

## Datos identificatorios

- **Nombre:** Elizabeth Priscila Duarte Nuñez
- **Legajo:** CURZA-9986
- **Token:** duarte-6881-34
- **Repositorio:** https://github.com/Elzzzzo-oss/peylw-2026-practicos-duarte-6881-34
- **GitHub Pages:** https://elzzzzo-oss.github.io/peylw-2026-practicos-duarte-6881-34/

## Historial de correcciones

| Entrega | Commit revisado | Nota | Motivo principal |
|---|---|---|---|
| 1 | `5eb4537` | 37 | `index.html` sin reemplazar (plantilla vieja del Lab 1, sin `<header>/<nav>/<main>/<footer>`), sin imagen en `acercade.html`, comentario de token ausente/incorrecto, commit con mensaje exacto vacío. |
| 2 (reentrega) | `b127f78` | 86 | `index.html` reemplazado con estructura semántica completa y navegación funcional; se agregaron token e imagen. Persisten: commit con mensaje exacto vacío, `REFLEXION.md` desactualizada (dice "no elegí imagen" pese a que ahora sí hay una), imagen en subcarpeta `img/imagen/` en vez de `img/`, y `reflexion.md` duplicado del Lab 1 sin limpiar. |

### Qué se corrigió

- `index.html` fue reemplazado por completo: ahora tiene `<header>`, `<nav>`, `<main>` con sección de bienvenida y `<footer>`, igual que `acercade.html`. La navegación entre ambas páginas ya funciona en producción.
- Se agregó el comentario `<!-- TOKEN-ALUMNO: duarte-6881-34 -->` en ambos archivos.
- El `<h1>` ahora usa el formato `Portal de ... - duarte-6881-34` en ambas páginas (con nombre abreviado, ver observaciones).
- Se agregó una imagen con `<figure>`/`<figcaption>`/`alt` en `acercade.html`.
- Se eliminó la carpeta `capturas/` residual del Lab 1.
- Se agregó el `<link rel="stylesheet">` a `index.html`, que antes faltaba.

### Qué no se corrigió

- El commit con el mensaje exacto (`4018dc5`) sigue con diff vacío; el trabajo real del TP2 sigue subido en commits con otros mensajes.
- El `reflexion.md` (minúscula) duplicado con contenido del Lab 1 sigue presente.
- El README sigue sin el campo "Enlace a la Página en GitHub Pages".

### Qué empeoró / quedó desactualizado

- `REFLEXION.md` no se actualizó tras agregar la imagen: la Pregunta 1 sigue respondiendo "no elegi imagen", lo cual ahora es falso y contradice el propio repositorio.
- La imagen se guardó en `img/imagen/yo.pnj.jpeg` (subcarpeta dentro de `img/`), no directamente en `img/` como exige la consigna.

## Checklist por ítem (entrega actual — commit `b127f78`)

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | Nombre, legajo, DNI y fecha presentes; sigue faltando "Enlace a la Página en GitHub Pages". |
| Personalización — Token en comentario (ambos archivos) | ✅ | `<!-- TOKEN-ALUMNO: duarte-6881-34 -->` exacto e idéntico en `index.html` y `acercade.html`. |
| Personalización — `<h1>` exacto (ambos archivos) | ⚠️ | `Portal de Elizabeth Duarte - duarte-6881-34` idéntico en ambas páginas, pero usa nombre abreviado ("Elizabeth Duarte"), no el nombre completo declarado en el README ("Elizabeth Priscila Duarte Nuñez"). |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ | `lang="es"`, charset UTF-8 y `<title>Inicio - Portal Personal</title>` correctos. |
| Tarea 1 — `index.html`: `<header>` | ✅ | Presente con el `<h1>` correcto. |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ | `<ul>` con "Inicio" y "Acerca de", rutas relativas correctas. |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ | `<h2>Bienvenidos a mi espacio</h2>` exacto, dos párrafos reales que explican el sitio. |
| Tarea 1 — `index.html`: `<footer>` | ✅ | Copyright, dirección del nodo (CURZAS - UNCo, Viedma, Río Negro) y token en texto simple, los tres presentes. |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ | Idénticos a `index.html`. |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ | Dos `<section>`, dos párrafos en total, biografía real que menciona el interés por la Tecnicatura en Desarrollo Web. |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ⚠️ | Imagen presente y carga correctamente (200 en producción), `alt` personalizado ("Fotografía de perfil de Elizabeth Duarte"). Pero la ruta es `img/imagen/yo.pnj.jpeg`: está en una subcarpeta dentro de `img/`, no directamente en `img/` como exige el enunciado. |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ | `<ul>` con HTML5/CSS3, JavaScript y Git/GitHub, correcto. |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ | En la raíz, con la regla básica de `body`, vinculado con `<link>` en ambos `<head>` (ya corregido en `index.html`). |
| Tarea 3 — Commit con mensaje exacto | ❌ | El commit `4018dc5` sigue teniendo el mensaje exacto pero diff vacío (0 líneas). No existe ningún otro commit con ese mensaje exacto que sí contenga el trabajo del TP2. |
| Estructura de archivos correcta | ⚠️ | `capturas/` ya no está, pero persiste el duplicado `reflexion.md` (Lab 1, sin actualizar) y la imagen quedó en una subcarpeta `img/imagen/` en vez de `img/`. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `index.html`, `acercade.html` e `img/imagen/yo.pnj.jpeg` responden 200 en producción; la navegación entre ambas páginas ahora funciona realmente en el sitio desplegado. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Pregunta 1 desactualizada: sigue diciendo "no elegi imagen" cuando el repo ya tiene una imagen cargada y referenciada en `acercade.html`, contradicción directa con el contenido real. Pregunta 2 correcta y personal. Pregunta 3 completa y bien justificada (verificación local y en GitHub Pages, incluso desde el celular). |

## Observaciones puntuales

- Mejora sustancial respecto de la entrega anterior: `index.html` ya no es la plantilla vieja del Lab 1 y la navegación real del sitio publicado funciona en ambos sentidos.
- El commit con el mensaje exacto del TP2 sigue sin contener el trabajo real; los cambios de esta reentrega se subieron con el mensaje `TP2: Correccion de estructuras semanticas, imagenes y tokens` (dos veces), que no es el pedido por la consigna.
- `REFLEXION.md` quedó desincronizada del repo real: la respuesta a la Pregunta 1 dice que no se eligió imagen, pero sí hay una (`img/imagen/yo.pnj.jpeg`) con `alt` propio. Esto es peor que no responder: es una respuesta que contradice el propio trabajo entregado.
- La imagen está en `img/imagen/`, una subcarpeta dentro de `img/`, no directamente en `img/` como pide el enunciado.
- El `<h1>` usa "Elizabeth Duarte" en lugar del nombre completo "Elizabeth Priscila Duarte Nuñez" declarado en el README.
- Sigue sin limpiarse `reflexion.md` (minúscula), duplicado con preguntas del Lab 1 (`git status`, staging area), y el README sigue sin el campo "Enlace a la Página en GitHub Pages".

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 4 |
| Personalización (token + `<h1>`) | 10 | 9 |
| Tarea 1 — `index.html` | 25 | 25 |
| Tarea 2 — `acercade.html` | 30 | 27 |
| Tarea 3 — `styles.css` y commit | 10 | 6 |
| Estructura de archivos | 5 | 3 |
| GitHub Pages | 5 | 5 |
| Reflexión | 10 | 7 |
| **TOTAL** | **100** | **86** |

---

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
