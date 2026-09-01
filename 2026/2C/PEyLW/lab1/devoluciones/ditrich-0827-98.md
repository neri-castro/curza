# Devolución Lab 1 — Carla Yamila Ditrich

## Datos identificatorios

- **Nombre:** Carla Yamila Ditrich
- **Legajo:** 10498
- **Últimos 4 dígitos DNI:** 0827
- **Token:** ditrich-0827-98
- **Repositorio:** https://github.com/Carla-Ditrich/peylw-2026-practicos-ditrich-0827-98
- **GitHub Pages:** https://carla-ditrich.github.io/peylw-2026-practicos-ditrich-0827-98/

**Nota sobre la fuente de estos datos:** la carátula en PDF entregada
(`Practico.1.CarlaDitrich.pdf`) solo contiene dos líneas — el nombre de la
alumna y el enlace al repositorio — sin legajo, DNI, fecha de entrega ni
enlace a GitHub Pages. Legajo, DNI y fecha se tomaron de `README.md` dentro
del repositorio, que sí está completo. Ver observación correspondiente más
abajo.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | `README.md` en el repo tiene los 5 campos completos (nombre, legajo, DNI, fecha, enlace). La carátula PDF entregada al margen del repo está incompleta (ver observaciones). |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido (1598x854). |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | Se ve `git config --global user.name/email` y la salida completa de `git config --list` con `user.name=Carla Ditrich` y `user.email=ditrichcarla70@hotmail.com`. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-ditrich-0827-98` respeta el patrón `peylw-2026-practicos-<token>`. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Carla Yamila Ditrich</h1>` presente. Comentario `<!-- ditrich-0827-98 -->` presente, aunque sin la etiqueta `TOKEN-ALUMNO:` sugerida en el enunciado (ver observaciones). |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `cf7287b` con mensaje exacto `Commit inicial: Configurando el index con mi token unico`, incluye `index.html`. |
| Tarea 2 — Repositorio público | ✅ | Confirmado vía API de GitHub (`private: false`). |
| Tarea 3 — GitHub Pages configurado y funcionando | ✅ | `has_pages: true`, estado `built`, `public: true` en la API de Pages. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `curl` a la URL inferida devuelve `200`. Contenido renderizado coincide con `index.html` del repo. |
| Estructura de archivos correcta | ✅ | `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png` — exactamente lo esperado, sin archivos de más ni de menos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas están completas y cumplen lo pedido (ver detalle en observaciones). |

## Observaciones puntuales

1. **Carátula PDF entregada incompleta (`Practico.1.CarlaDitrich.pdf`).** El
   documento entregado como carátula del trabajo práctico contiene
   únicamente dos líneas: el nombre de la alumna y el enlace al
   repositorio. No incluye legajo, últimos 4 dígitos del DNI, fecha de
   entrega ni el enlace a GitHub Pages, pese a que el enunciado pide todos
   esos campos en la carátula. El `README.md` del repositorio sí contiene
   la información completa, y por eso el ítem de rúbrica "README completo"
   no se penaliza — pero la carátula formalmente entregada para
   corrección no cumple por sí sola con lo pedido. Se deja constancia
   como incumplimiento de forma, sin impacto en la nota porque la fuente
   alternativa (README.md) está completa.

2. **`index.html` — formato del comentario con el token.** El comentario
   `<!-- ditrich-0827-98 -->` contiene el token pero no usa el formato
   sugerido en el enunciado (`<!-- TOKEN-ALUMNO: ditrich-0827-98 -->`).
   Se acepta como equivalente porque el token está presente y es
   inequívoco, pero se señala porque un comentario sin etiqueta es menos
   legible para quien revisa el archivo sin contexto.

3. **`REFLEXION.md`, pregunta 3.** La explicación de staging area es
   correcta en lo esencial pero imprecisa en un punto: dice que en el
   staging area se preparan cambios "para ser enviados al repositorio
   local", lo cual mezcla el rol del staging (preparar el próximo commit)
   con el del commit en sí (que es el que efectivamente pasa al
   repositorio). No se descuenta porque la distinción entre working
   directory y staging area queda clara, pero es un matiz a corregir. No
   menciona `git add` explícitamente (el enunciado lo marca como
   "positivo", no como requisito).

4. **Commits posteriores al commit inicial.** Hay tres commits adicionales
   (`5387f17`, `b4db14a`, `90b40bc`) que agregan y corrigen README,
   REFLEXION y la captura. No se penalizan, conforme a la consigna de
   corrección (el commit evaluado es el inicial).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula completa | 5 | 5 |
| Tarea 1 — captura presente | 10 | 10 |
| Tarea 1 — captura con contenido correcto | 10 | 10 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 10 |
| Tarea 2 — comentario con token | 5 | 5 |
| Tarea 2 — mensaje de commit exacto | 10 | 10 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 10 |
| Estructura de archivos | 10 | 10 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 10 |
| Reflexión (P1: 3, P2: 3, P3: 4) | 10 | 10 |
| **TOTAL** | **100** | **100** |

Cumple todos los ítems de la rúbrica técnica del clon y de la verificación
en vivo. El único incumplimiento real detectado es de forma y externo al
repositorio: la carátula PDF entregada para la corrección no trae los
datos completos que pide el enunciado; no se tradujo en descuento porque
el propio repositorio (README.md) contiene esa información, pero debe
quedar registrado como observación para la alumna.
