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
