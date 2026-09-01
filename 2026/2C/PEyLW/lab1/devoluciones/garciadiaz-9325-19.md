# Devolución Lab 1 — Luciano García Díaz

## Datos identificatorios

- **Nombre:** Luciano García Díaz
- **Legajo / DNI (últimos 4 dígitos):** 9325
- **Token:** garciadiaz-9325-19
- **Repositorio (tal como lo escribió el alumno):** https://github.com/Lucho-GD/peylw-2026-practicos-garciadiaz-9325-19/tree/main/garciadiaz-9325-19
- **Repositorio (raíz real):** https://github.com/Lucho-GD/peylw-2026-practicos-garciadiaz-9325-19
- **GitHub Pages:** https://lucho-gd.github.io/peylw-2026-practicos-garciadiaz-9325-19/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ❌ | `garciadiaz-9325-19/readme.md` tiene 0 bytes. No hay ningún campo completado. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `garciadiaz-9325-19/capturas/config_git.png`, PNG válido 900x456. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | Se ve `git config --list` completo, con `user.name=Luciano Garcia Diaz` y `user.email=lucianogarciadiazwd@gmail.com` legibles. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-garciadiaz-9325-19` respeta el formato pedido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Luciano Garcia Diaz</h1>` presente; comentario `<!-- Token único: garciadiaz-9325-19 -->` equivalente al formato pedido. |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `9307922`: `Commit inicial: Configurando el index con mi token unico`, incluye `index.html`. |
| Tarea 2 — Repositorio público | ✅ | Confirmado vía API de GitHub (`private: false`). |
| Tarea 3 — GitHub Pages configurado y funcionando | ❌ | La URL responde 404 (página "Page not found · GitHub Pages"). |
| GitHub Pages desplegado y respondiendo 200 | ❌ | Verificado con `curl`/WebFetch: `HTTP 404`, no `200`. Causa directa: `index.html` no está en la raíz del repo. |
| Estructura de archivos correcta (raíz del repo) | ❌ | Todos los archivos están anidados un nivel dentro de `garciadiaz-9325-19/` (subcarpeta), no en la raíz del repositorio. La raíz solo contiene esa subcarpeta. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Preguntas 1 y 2 correctas; Pregunta 3 contiene texto de plantilla/instrucción sin depurar (ver observaciones). |

## Observaciones puntuales

1. **`garciadiaz-9325-19/readme.md` vacío (0 bytes).** No hay carátula: falta nombre, legajo, DNI, fecha de entrega y enlace al repositorio. No se trata de un campo `[Completar]` sin reemplazar, sino de la ausencia total del archivo con contenido. Se calificó como incumplimiento total del ítem.

2. **Estructura de archivos fuera de la raíz del repo.** El repositorio `Lucho-GD/peylw-2026-practicos-garciadiaz-9325-19` tiene, en su raíz, únicamente la carpeta `garciadiaz-9325-19/`; dentro de ella están `index.html`, `readme.md`, `reflexion.md` y `capturas/config_git.png`. El enunciado pide `index.html`, `README.md`, `capturas/` y `REFLEXION.md` directamente en la raíz del repositorio. El enlace que el alumno puso en la carátula (`.../tree/main/garciadiaz-9325-19`) ya delataba este desvío, apuntando a la subcarpeta en lugar de a la raíz. Se calificó como incumplimiento total del ítem "Estructura de archivos exacta (raíz del repo)": la raíz del repo no contiene ninguno de los archivos pedidos, están todos un nivel más abajo.

3. **GitHub Pages responde 404, consecuencia directa del punto anterior.** GitHub Pages sirve el contenido de la raíz de la rama `main` (salvo configuración explícita de subcarpeta, que no está activada aquí), por lo que al no existir `index.html` en la raíz, `https://lucho-gd.github.io/peylw-2026-practicos-garciadiaz-9325-19/` devuelve un 404 real de GitHub Pages, verificado con `curl` (código `404`) y contenido "Page not found · GitHub Pages". Por regla, esto es incumplimiento total, sin excepciones, tanto para "Tarea 3" como para el ítem específico de despliegue respondiendo 200.

4. **`garciadiaz-9325-19/reflexion.md`, Pregunta 3, líneas 24-37.** El bloque contiene la cita textual del enunciado ("> Explique con sus palabras...") seguida de la instrucción "Podés explicarlo de manera sencilla:" y luego la respuesta envuelta en un bloque de código Markdown (```` ```markdown ````) sin cerrar. Esto es texto de plantilla/instrucción que no fue depurado antes de entregar — no corresponde a una respuesta redactada limpiamente por el alumno, sino a contenido pegado sin adaptar. El contenido conceptual de la respuesta (diferencia entre working directory y staging area, mención de `git add`) es correcto, pero la falta de depuración del texto pegado se penaliza parcialmente conforme a la regla de "respuesta sin adaptación".

5. **Punto positivo:** el token declarado en `reflexion.md` (`garciadiaz-9325-19`) coincide exactamente con el nombre del repositorio y con el comentario HTML en `index.html`. La salida de `git status` pegada en la Pregunta 2 es literal y corresponde a un estado previo al primer commit (`No commits yet`, `Changes to be committed: index.html`).

6. El mensaje del primer commit es exacto y correcto, e incluye `index.html`, aunque este viva en la subcarpeta y no en la raíz — el contenido de la Tarea 2 en sí (nombre del repo, `index.html`, comentario con token, commit, repo público) está completo y bien resuelto.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 0 |
| Tarea 1 — captura presente | 10 | 10 |
| Tarea 1 — captura con contenido correcto | 10 | 10 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 10 |
| Tarea 2 — comentario con token | 5 | 5 |
| Tarea 2 — mensaje de commit exacto | 10 | 10 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 0 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 0 |
| Estructura de archivos (raíz del repo) | 10 | 0 |
| Reflexión (P1: 3, P2: 3, P3: 2/4) | 10 | 8 |
| **TOTAL** | **100** | **63** |

Nota: la tabla de nota final desdobla el punto de GitHub Pages en dos ítems de 10 puntos cada uno ("configurado y funcionando" y "desplegado y respondiendo 200"), tal como figura en la tabla de pesos de `AGENTS-Lab01.md` (que tiene prioridad sobre `context-Lab01.md` en caso de conflicto de formato), para que la suma total cierre en 100.
