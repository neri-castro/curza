# Devolución Lab 1 — Ramiro Javier Reynoso Bascary

## Datos identificatorios

- **Nombre:** Ramiro Javier Reynoso Bascary (según `index.html` y GitHub; el `README.md` solo consigna "Ramiro Reynoso")
- **Legajo:** 8907
- **Token:** reynoso-4260-07
- **Repositorio:** https://github.com/Ramireybas/peylw-2026-practicos-reynoso-4260-07
- **GitHub Pages:** https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ⚠️ parcial | 4 de 5 campos conservan los corchetes `[ ]` sin remover: `[Ramiro Reynoso]`, `[8907]`, `[37504260]`, `[(https://...)]`. Solo "Fecha de Entrega" está limpio. Además el campo DNI contiene el DNI completo (8 dígitos) en vez de los últimos 4. |
| Tarea 1 — Captura `config_git.png` presente | ✅ cumple | Existe en `capturas/config_git.png`, PNG válido 710x403. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ cumple | La imagen muestra la salida completa de `git config --list`, con `user.name=ramiro_reynoso` y `user.email=ramiroreynosobascary@gmail.com` legibles. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ cumple | `peylw-2026-practicos-reynoso-4260-07` respeta el formato pedido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ⚠️ parcial | `<h1>` con nombre completo presente y correcto. El token se muestra en un `<h2>reynoso-4260-07</h2>` visible en la página, **no** como comentario HTML (`<!-- -->`). No cumple el formato pedido para el token. |
| Tarea 2 — Commit con mensaje exacto | ✅ cumple | Commit `2bb7050` con mensaje exacto `Commit inicial: Configurando el index con mi token unico`, incluye `index.html` (vacío en ese commit, el contenido se agrega en un commit posterior "Update index.html", lo cual el enunciado no penaliza). |
| Tarea 2 — Repositorio público | ✅ cumple | Confirmado en vivo: repo público. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ cumple | La URL responde y renderiza el `<h1>` con el nombre del alumno. |
| Estructura de archivos correcta | ✅ cumple | `find` sobre el clon coincide exactamente con la estructura esperada (`index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png`). |
| Reflexión — 3 preguntas respondidas | ⚠️ parcial | Ver detalle en observaciones. |

## Observaciones puntuales

- **`README.md`**: los campos "Nombre y Apellido", "Legajo/Matrícula", "Últimos 4 dígitos del DNI" y "Enlace al Repositorio de GitHub" quedaron con los corchetes de plantilla sin remover (ej. `Legajo/Matrícula: [8907]`), señal de que la carátula se completó sin limpiar el formato pedido. El campo DNI además está mal completado: figura `[37504260]`, que son 8 dígitos (el DNI completo), cuando se pedían solo los últimos 4. El nombre consignado en el README ("Ramiro Reynoso") tampoco coincide con el nombre completo real usado en `index.html` y en GitHub ("Ramiro Javier Reynoso Bascary").
- **`index.html`**: no contiene ningún comentario HTML (`<!-- ... -->`). El token único se puso en un `<h2>` visible en el body, lo cual no satisface el requisito de "comentario HTML con el token único" — el token debía quedar oculto en el marcado, no como contenido visible de la página.
- **Historial de commits**: el commit inicial (`2bb7050`) crea `index.html` vacío (0 bytes); el contenido real (estructura, `<h1>`, `<h2>` con token) se agrega recién en el commit `49110d6 Update index.html`. El mensaje de commit evaluado es correcto y el archivo está incluido, por lo que esto no penaliza el sub-ítem del mensaje de commit, pero indica que la consigna de "configurar el index con el token" en el commit inicial no se cumplió al pie de la letra en ese mismo commit.
- **`REFLEXION.md` — Pregunta 1**: la respuesta es `1-peylw-2026-practicos-reynoso-4260-07`, es decir el nombre completo del repositorio en vez del token aislado. El token coincide con el nombre del repo, pero no hay comentario HTML en `index.html` contra el cual contrastarlo (ver punto anterior), por lo que la verificación de coincidencia queda incompleta.
- **`REFLEXION.md` — Pregunta 2**: correcta, salida literal de `git status` pegada, coherente con el estado previo al commit inicial (`new file: index.html` en "Changes to be committed").
- **`REFLEXION.md` — Pregunta 3**: explicación correcta y en palabras propias de working directory vs. staging area.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 1 |
| Tarea 1 — captura presente | 10 | 10 |
| Tarea 1 — captura con contenido correcto | 10 | 10 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 10 |
| Tarea 2 — comentario con token | 5 | 0 |
| Tarea 2 — mensaje de commit exacto | 10 | 10 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 10 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 10 |
| Estructura de archivos | 10 | 10 |
| Reflexión | 10 | 9 |
| **TOTAL** | **100** | **90** |

Nota de corrección: la tabla original omitía el ítem "GitHub Pages
desplegado y respondiendo 200" (10 pts, distinto de "Tarea 3 — GitHub
Pages configurado y funcionando" según la tabla de pesos de
`AGENTS-Lab01.md`), ya verificado como cumplido. Se agrega aquí; no
cambia el total (ya estaba bien calculado en 90).
