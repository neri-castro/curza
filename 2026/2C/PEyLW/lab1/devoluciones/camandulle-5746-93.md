# Devolución Lab 1 — Fernanda Camandulle

## Datos identificatorios

- **Nombre:** Fernanda Camandulle
- **Legajo:** 10093
- **Token:** camandulle-5746-93
- **Repositorio:** https://github.com/Camandulle/peylw-2026-practicos-camandulle-5746-93
- **GitHub Pages:** https://camandulle.github.io/peylw-2026-practicos-camandulle-5746-93/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Los cinco campos requeridos están presentes y completos en `README.md`. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido de 2132x538px. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | Se ve la salida completa de `git config --list` con `user.name=Fernanda Camandulle` y `user.email=fercamandulle@hotmail.com`. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-camandulle-5746-93` coincide con el formato pedido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Fernanda Camandulle</h1>` presente; comentario `<!-- Token único: camandulle-5746-93 -->` es equivalente semántico aceptado del formato pedido. |
| Tarea 2 — Commit con mensaje exacto | ❌ | Ningún commit del historial usa el mensaje `Commit inicial: Configurando el index con mi token unico`. Ver observaciones. |
| Tarea 2 — Repositorio público | ✅ | Verificado en vivo: el repositorio es accesible sin restricciones. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ | Verificado en vivo: la URL responde con el contenido de `index.html` (título y `<h1>` visibles), sin 404. |
| Estructura de archivos correcta | ⚠️ | Estructura pedida completa, pero hay un archivo `.DS_Store` (artefacto de macOS) commiteado en la raíz que no forma parte de la entrega. |
| Reflexión — 3 preguntas respondidas | ⚠️ | P1 y P3 correctas; P2 pega una salida de `git status` que no corresponde al estado previo al primer commit. |

## Observaciones puntuales

- **`git log` (historial de commits):** el commit inicial real es `eef74dc "first commit"`, y el commit que agrega `index.html` con el token es `63f2425 "Agregar caratula en README e index.html con token unico"`. Ninguno de los cuatro commits (`eef74dc`, `63f2425`, `891d733`, `eab4a68`) usa el mensaje exacto exigido por la consigna: `Commit inicial: Configurando el index con mi token unico`. Esto es un incumplimiento directo de la Tarea 2, no una diferencia de redacción menor: el enunciado pide ese mensaje literal y no aparece en ningún punto del historial.
- **Estructura de archivos (raíz del repo):** además de `index.html`, `README.md`, `REFLEXION.md` y `capturas/config_git.png` (correctos), se commiteó `.DS_Store`, un archivo de sistema de macOS que debería estar en `.gitignore` y no en el repositorio.
- **`REFLEXION.md`, Pregunta 2:** la salida de `git status` pegada muestra `On branch main / Your branch is up to date with 'origin/main'` y `modified: README.md` con `REFLEXION.md` y `capturas/` como *untracked*. Esto describe el estado previo al commit `891d733` (el que agrega README actualizado, captura y reflexión), no el estado previo al primer commit del `index.html` que la consigna pide documentar. La salida es literal (no parafraseada, cumple ese requisito), pero corresponde al momento equivocado del flujo de trabajo.
- **`remote.origin.url` en la captura de `capturas/config_git.png`:** apunta a `https://github.com/fercamandulle/...` mientras que el repositorio real y publicado está bajo el usuario `Camandulle`. No afecta la corrección porque el repositorio efectivamente accesible es el declarado en la carátula, pero es una inconsistencia a tener en cuenta si se reutiliza esa captura como evidencia de configuración del repo actual.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Tarea 1 — captura presente | 10 | 10 |
| Tarea 1 — captura con contenido correcto | 10 | 10 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 10 |
| Tarea 2 — comentario con token | 5 | 5 |
| Tarea 2 — mensaje de commit exacto | 10 | 0 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 10 |
| Estructura de archivos | 10 | 8 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 10 |
| Reflexión (P1: 3, P2: 3, P3: 4) | 10 | 9 |
| **TOTAL** | **100** | **87** |
