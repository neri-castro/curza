# Devolución Lab 1 — Javier Chavarria

## Datos identificatorios

- **Nombre:** Javier Chavarria (carátula: Chavarria, Javier Andres)
- **Legajo:** CURZA-6755
- **Token:** chavarria-7037-55
- **Repositorio:** https://github.com/javi-jav/peylw-2026-practicos-chavarria-7037-55
- **GitHub Pages:** https://javi-jav.github.io/peylw-2026-practicos-chavarria-7037-55/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Todos los campos presentes y completos en `README.md`: nombre, legajo, DNI, fecha, enlace al repo. Coincide con la carátula del PDF. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido de 652x397. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | Muestra la salida completa de `git config --list`, con `user.name=Javier Chavarria` y `user.email=chavarriajavierandres@gmail.com` legibles. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-chavarria-7037-55`, respeta el formato exigido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Javier Chavarria</h1>` presente. Comentario `<!-- chavarria-7037-55 -->` presente; no usa el formato literal `TOKEN-ALUMNO: <token>` pero es equivalente semántico aceptado por la consigna. |
| Tarea 2 — Commit con mensaje exacto | ✅ | `f70e459 Commit inicial: Configurando el index con mi token unico`, mensaje textual exacto, incluye `index.html`. |
| Tarea 2 — Repositorio público | ✅ | Verificado en vivo: la página del repo carga sin restricción de acceso. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ | Verificado en vivo: la URL de Pages sirve contenido (título "Laboratorio 1", nombre del alumno), no devuelve 404. |
| Estructura de archivos correcta | ✅ | `find` sobre el clon devuelve exactamente `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png`, sin archivos de más ni de menos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres preguntas de `REFLEXION.md` están completas y correctas (detalle abajo). |

## Observaciones puntuales

- `index.html`, `README.md` y `REFLEXION.md` tienen dos líneas en blanco antes del contenido real (antes de `<!DOCTYPE html>` y antes del primer encabezado). No afecta la validez ni el contenido evaluado, se menciona solo como detalle de prolijidad.
- El comentario de token en `index.html` (línea 12) es `<!-- chavarria-7037-55 -->` en lugar del formato sugerido `<!-- TOKEN-ALUMNO: chavarria-7037-55 -->`. Se acepta como equivalente semántico según lo indicado en la consigna de corrección, no se descuenta.
- `REFLEXION.md`, pregunta 2: la salida de `git status` pegada corresponde al momento posterior a `git add` y anterior al commit (`Changes to be committed: new file: index.html`), estado válido de "antes del primer commit" — no es el estado `nothing to commit` que se penalizaría.
- Token declarado en `REFLEXION.md` (chavarria-7037-55) coincide exactamente con el nombre del repositorio y con el comentario en `index.html`. Sin inconsistencias.
- No hay commits adicionales fuera de lo esperado: el segundo commit (`Agrego entregables del Laboratorio 1`) solo agrega README, REFLEXION y la captura, consistente con lo permitido por la consigna.

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
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **100** |

Nota de corrección: la tabla original omitía el ítem "GitHub Pages
desplegado y respondiendo 200" (10 pts, distinto de "Tarea 3 — GitHub
Pages configurado y funcionando" según la tabla de pesos de
`AGENTS-Lab01.md`), ya verificado como cumplido. Se agrega aquí; no
cambia el total (ya estaba bien calculado en 100).
