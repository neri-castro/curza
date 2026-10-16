# Devolución Lab 4 — Tatiana Manquenao

## Datos identificatorios

- **Token:** manquenao-2747-93
- **GitHub Pages:** https://tati99-web.github.io/manquenao-2747-93/
- **Repositorio:** https://github.com/tati99-web/manquenao-2747-93

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Personalización — paleta HSL sin colores puros | ❌ | `styles.css` no usa `hsl()` en ningún lado; todos los colores están en hex (`#4a90e2`, `#357ABD`, `#333333`, `#222222`, `#f4f4f9`) o `rgb()`. |
| Personalización — comentario en `styles.css` con HSL + identificador | ❌ | No existe comentario de cabecera con códigos HSL ni identificador de alumno. El único comentario inicial es genérico (`/* Estilos generales */`). |
| Tabla de `contacto.html` formateada | ⚠️ | Hay borde y padding genéricos (`table, td { border: 1px solid #ccc; padding: 8px; }`), pero la tabla no usa `<th>` en ningún lado (solo `<td>`), por lo que no hay diferenciación visual de encabezados. |
| Formulario de `contacto.html` formateado | ❌ | `styles.css` no define ninguna regla para `input`, `label`, `fieldset` ni grupos de radio/checkbox. El formulario se ve con el estilo por defecto del navegador. |
| Fuente web importada y aplicada | ❌ | No hay `<link>` a Google Fonts ni `@font-face` en ningún archivo. `body { font-family: sans-serif; }` es la única declaración de tipografía. |
| Logo CURZA a la derecha del título | ❌ | Ningún `<header>` de las tres páginas incluye una imagen de logo; solo contienen `<h1>`. |
| Animación de giro completo (360°) del logo | ❌ | No existe ningún `@keyframes` en el proyecto (se verificó con búsqueda en todos los `.css`/`.html`). |
| Header fijo en todas las páginas | ❌ | El selector `header` en `styles.css` no tiene `position: fixed` ni `sticky`; es un bloque estático con `padding` y `text-align`. |
| "Acerca de" — primera línea sticky | ❌ | No hay `position: sticky` en `acercade.html` ni en `styles.css`. |
| "Acerca de" — `max-height: 300px` + scroll | ❌ | El `<article>` de `acercade.html` no tiene `max-height` ni `overflow-y` definidos. |
| Botón volver arriba — presente en todas las páginas | ❌ | No existe ningún elemento de "volver arriba" en `index.html`, `acercade.html` ni `contacto.html`. |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ❌ | No aplica: el botón no existe. |
| Botón volver arriba — funcional | ❌ | No aplica: el botón no existe. |
| Responsive — meta viewport en las tres páginas | ✅ | Presente en `index.html`, `acercade.html` y `contacto.html`. |
| Responsive — flexbox/grid en nav y/o formulario/tabla | ✅ | `nav ul { display: flex; justify-content: center; }` en `styles.css`. |
| Responsive — `@media 768px` apila el menú y adapta la tabla | ❌ | No hay ninguna regla `@media` en todo el proyecto. Según la rúbrica, la ausencia total de `@media` invalida el ítem completo de Responsive, no solo este sub-ítem. |
| `REFLEXION.md` presente y con las 3 preguntas respondidas | ❌ | Existe `Reflexion.md` (minúsculas) pero su contenido es la reflexión del **Laboratorio 2** ("Imagen", "Etiquetas semánticas", "Verificación de rutas"), no las 3 preguntas de "Prevención de Copias" del Lab 4 (fragmento de animación, `background-color` en sticky, cambio visual bajo 768px). |

## Observaciones puntuales

- **`index.html` y `acercade.html`**: ambos archivos contienen restos literales de una cerca de markdown ("```html" al inicio y "```" al final), y `index.html` además tiene un `<!DOCTYPE html>` duplicado antes de esa cerca. Esto no es solo un problema de prolijidad: se reproduce igual en el sitio desplegado (confirmado con `curl` sobre `https://tati99-web.github.io/manquenao-2747-93/`), por lo que el texto suelto "```html" aparece renderizado en la página real.
- **`styles.css`**: no tiene ningún cambio respecto a la entrega del Lab 3. El historial de commits confirma que el último commit es `1bb47c0 "lab3-entrega de contacto y estilos"` (28/09/2026); no hay ningún commit posterior que incorpore personalización HSL, fuente web, animación, header fijo, sticky o media queries — es decir, no se registra trabajo del Lab 4 en el repositorio.
- **`contacto.html`**: la tabla "Resumen de Datos" (sección `<table>`) no usa `<th>` en ninguna fila; todas las celdas son `<td>`, por lo que no hay forma de diferenciar visualmente encabezados aunque exista borde/padding genérico.
- **`contacto.html` / `styles.css`**: el formulario no tiene ninguna regla CSS propia (no hay selectores `input`, `label`, `fieldset`, `input[type=radio]`, etc. en `styles.css`), se ve enteramente con estilo por defecto del navegador.
- **`Reflexion.md`** (raíz del repo): contiene la reflexión del Lab 2, no la del Lab 4. El archivo `Readme.md` tampoco cubre lo pedido: trae mezclada la reflexión del Lab 3 (código postal, `<label>`, radios) pegada debajo de la carátula. Ninguno de los dos documentos responde las 3 preguntas de "Prevención de Copias" del Lab 4.
- **Nombre del repositorio**: no sigue el patrón esperado `peylw-2026-practicos-manquenao-2747-93`; el repo es simplemente `manquenao-2747-93`. Se registra la discrepancia sin penalizar por este motivo en particular, conforme a lo indicado en `context-Lab04.md`.
- **Hallazgo adicional (no puntuado en la rúbrica de Lab 4)**: `acercade.html` referencia `img/mi_foto.jpg`, pero no existe carpeta `img/` en el repo — solo `img - copia/2e3a2121-c141-45ef-a85e-b34900a7cfe7.jpg` (nombre y carpeta distintos). La imagen de perfil está rota; es un defecto heredado de labs anteriores, no parte de este TP, pero se deja constancia.
- **Verificación en vivo**: `https://tati99-web.github.io/manquenao-2747-93/` responde 200, igual que `/acercade.html` y `/contacto.html`. El contenido servido coincide exactamente con el repo clonado, incluyendo el defecto de las cercas de markdown y la ausencia total de los estilos pedidos en el enunciado del Lab 4.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Personalización (paleta HSL + comentario) | 5 | 0 |
| Tabla `contacto.html` | 12 | 8 |
| Formulario `contacto.html` | 12 | 0 |
| Fuente web | 8 | 0 |
| Animación título + logo | 12 | 0 |
| Header fijo | 12 | 0 |
| "Acerca de" sticky + scroll | 12 | 0 |
| Botón volver arriba | 12 | 0 |
| Responsive Web Design | 10 | 0 |
| `REFLEXION.md` | 5 | 0 |
| **TOTAL** | **100** | **8** |
