# Devolución Lab 1 — Sara Celeste Boisselier

## Datos identificatorios

- **Nombre:** Sara Celeste Boisselier
- **Legajo:** N° CURZA 8691
- **Token:** boisselier-8339-91
- **Repositorio:** https://github.com/SaraBoisselier/peylw-2026-practicos-boisselier-8339-91
- **GitHub Pages:** https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los cinco campos están completos, sin placeholders sin reemplazar. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido de 75411 bytes. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | La captura muestra la salida completa de `git config --list`, incluyendo `user.name=Sara Celeste Boisselier` y `user.email=m4gicele@gmail.com`. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-boisselier-8339-91` respeta el formato pedido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Sara Celeste Boisselier</h1>` presente; comentario `<!--Token: boisselier-8339-91 -->` presente. El formato del comentario difiere del sugerido (`TOKEN-ALUMNO: <token>`) pero es equivalente semántico, no se penaliza. |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `cd9f359` con mensaje exacto `Commit inicial: Configurando el index con mi token unico`, contiene únicamente `index.html`. |
| Tarea 2 — Repositorio público | ✅ | Verificado en vivo: el repositorio muestra "Public" en GitHub. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ | `https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/` responde HTTP 200 y muestra el `<h1>` con el nombre de la alumna. |
| Estructura de archivos correcta | ✅ | `find . -not -path "./.git*"` devuelve exactamente `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png` — coincide con lo esperado. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Pregunta 1 y 3 correctas; pregunta 2 no cumple (ver observaciones). |

## Observaciones puntuales

- **`REFLEXION.md`, pregunta 2:** la alumna responde textualmente "No ejecuté el comando `git status` antes de realizar el primer commit, por lo tanto no cuento con la salida correspondiente para responder esta pregunta." No hay salida de terminal pegada. El enunciado pide la salida literal de `git status`; al no existir ninguna salida (ni siquiera parafraseada), el ítem se considera incumplido, no parcial. 0/3.
- **`index.html`:** el comentario con el token usa el formato `<!--Token: boisselier-8339-91 -->` en lugar de `<!-- TOKEN-ALUMNO: boisselier-8339-91 -->`. Se acepta como equivalente semántico, sin descuento, pero se señala como desvío menor del formato sugerido.
- **Consistencia del token:** el token declarado en `REFLEXION.md` (pregunta 1) coincide tanto con el nombre del repositorio como con el comentario en `index.html`. Sin observaciones.
- **Historial de commits:** además del commit inicial exigido, hay tres commits posteriores (`Entregables obligatorios lab 1`, `Nombre de captura corregido`, `Corregido`) que agregan README, REFLEXION y la captura, y corrigen un error de nombre de archivo de la captura (`config_git.png.png` → `config_git.png`). No se penaliza por su existencia, conforme a la consigna.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Tarea 1 — captura presente | 10 | 10 |
| Tarea 1 — captura con contenido correcto | 10 | 10 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 10 |
| Tarea 2 — comentario con token | 5 | 5 |
| Tarea 2 — mensaje de commit exacto | 10 | 10 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 10 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 10 |
| Estructura de archivos | 10 | 10 |
| Reflexión (P1: 3, P2: 3, P3: 4) | 10 | 7 (3 + 0 + 4) |
| **TOTAL** | **100** | **97** |
