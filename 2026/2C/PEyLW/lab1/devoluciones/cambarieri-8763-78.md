# Devolución Lab 1 — Matías Cambarieri Gentile

## Datos identificatorios

- **Nombre:** Matías Cambarieri Gentile (según `README.md` del repositorio; `index.html` agrega un segundo nombre, "Andrés" — ver observaciones)
- **Legajo:** CURZA-10178
- **Token:** cambarieri-8763-78
- **Repositorio:** https://github.com/zaitamu/peylw-2026-practicos-cambarieri-8763-78
- **GitHub Pages:** https://zaitamu.github.io/peylw-2026-practicos-cambarieri-8763-78/

Nota: los datos identificatorios de esta sección se tomaron de `README.md` en el repositorio, porque el PDF entregado como carátula (`Laboratorio 1 - Matías Cambarieri Gentile.pdf`) no los contiene (ver observaciones).

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ | El PDF entregado (carátula formal de la entrega) solo trae dos links (repositorio y Pages), sin nombre, legajo, DNI ni fecha. `README.md` en el repo sí tiene los cinco campos completos. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido 758x132. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | Se ve `git config --list` completo con `user.name=zaitam` y `user.email=matiasgentile2002@gmail.com`. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-cambarieri-8763-78` respeta el formato pedido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ⚠️ | `<h1>` con nombre completo presente; comentario con token presente y correcto. Pero el archivo carece de `<html>`, `<head>` y `<body>`: solo tiene `<!DOCTYPE html>` seguido directamente del `<h1>`. |
| Tarea 2 — Commit con mensaje exacto | ⚠️ | El commit inicial dice "Commit inicial: Configurando el index con mi token **único**" (con tilde); el mensaje exigido es "...mi token **unico**" (sin tilde). No es el string exacto. |
| Tarea 2 — Repositorio público | ✅ | Confirmado en vivo: el repo aparece marcado "Public". |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ | Verificado en vivo: la URL de Pages sirve contenido (el `<h1>` del alumno), no 404. |
| Estructura de archivos correcta | ✅ | `find .` sobre el clon devuelve exactamente `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png`. |
| Reflexión — 3 preguntas respondidas | ✅ | Token declarado coincide con repo e `index.html`; salida de `git status` pegada literal y corresponde a un estado previo al primer commit; explicación de staging area vs working directory correcta y en palabras propias. |

## Observaciones puntuales

1. **Carátula PDF entregada (`Laboratorio 1 - Matías Cambarieri Gentile.pdf`):** el archivo tiene una sola página y su único contenido son dos hipervínculos (Repositorio y Página de GitHub Pages). No incluye nombre completo, legajo, últimos 4 dígitos de DNI ni fecha de entrega, campos que el enunciado pide en la carátula. Esto se verificó con extracción de texto completa del PDF (`pdftotext`), confirmando que no hay más contenido en ninguna otra parte del documento. Los datos identificatorios sí están completos en `README.md` dentro del repositorio, pero la entrega formal (el documento subido) está incompleta.

2. **`index.html` — estructura básica incompleta:** el archivo es:
   ```html
   <!DOCTYPE html>
   <h1> 
       Matías Andrés Cambarieri Gentile
       <!--token: cambarieri-8763-78-->
   </h1>
   ```
   Falta `<html>`, `<head>` y `<body>`. El enunciado no exige HTML5 completo, pero un `<h1>` colgando directamente del `DOCTYPE` sin las etiquetas contenedoras básicas no llega al piso de "estructura HTML básica" que pide la Tarea 2. Además, el comentario con el token está anidado dentro del propio `<h1>`, lo cual es válido pero no es la forma esperada.

3. **Mensaje del primer commit (`git log`):** el commit `4d2974c` dice "Commit inicial: Configurando el index con mi token **único**" (con tilde en la ú). El enunciado pide el mensaje exacto "Commit inicial: Configurando el index con mi token **unico**" (sin tilde). La diferencia es mínima pero el string no es idéntico, así que no se otorga el puntaje completo.

4. **Inconsistencia de nombre entre archivos:** el PDF entregado usa "Matías Cambarieri Gentile" (también en `README.md`), pero `index.html` usa "Matías **Andrés** Cambarieri Gentile". No se penaliza aparte porque igual constituye un nombre completo válido en el `<h1>`, pero es una inconsistencia entre los documentos de la misma entrega.

5. **Detalle positivo:** el token declarado en `REFLEXION.md` ("cambarieri-8763-78") coincide exactamente con el nombre del repositorio y con el comentario de `index.html`; no hay inconsistencias ahí. La salida de `git status` en la pregunta 2 es literal (incluye "En la rama master", "No hay commits todavía", "nuevos archivos: index.html") y corresponde efectivamente a un estado previo al primer commit, cumpliendo lo pedido.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 3 |
| Tarea 1 — captura presente | 10 | 10 |
| Tarea 1 — captura con contenido correcto | 10 | 10 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 6 |
| Tarea 2 — comentario con token | 5 | 5 |
| Tarea 2 — mensaje de commit exacto | 10 | 8 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 10 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 10 |
| Estructura de archivos | 10 | 10 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **92** |

Nota de corrección: la tabla original omitía el ítem "GitHub Pages
desplegado y respondiendo 200" (10 pts, distinto del ítem "Tarea 3 —
GitHub Pages configurado y funcionando" según la tabla de pesos de
`AGENTS-Lab01.md`), ya verificado como cumplido en el checklist. Se
agrega aquí y el total pasa de 82 a 92.
