# Devoluciones — Laboratorio 1: Configuración de Entorno y Control de Versiones

Corrección realizada sobre 10 entregas, siguiendo la rúbrica y el método
descriptos en `rules/AGENTS-Lab01.md` y `rules/context-Lab01.md`. Cada
entrega fue verificada clonando el repositorio real del alumno y
comprobando en vivo la publicación en GitHub y GitHub Pages.

## Tabla resumen — Lab 1

| Token | Nombre | Nota | Observación principal |
|---|---|---|---|
| chavarria-7037-55 | Javier Chavarria | 100 | Entrega completa, sin observaciones que descuenten. |
| cobis-5580-89 | Rolando Cobis | 100 | Entrega completa; carátula en captura de pantalla en vez de PDF/DOCX, sin impacto en la nota. |
| ditrich-0827-98 | Carla Yamila Ditrich | 100 | Entrega técnica completa; carátula PDF incompleta pero compensada por el README del repo. |
| boisselier-8339-91 | Sara Celeste Boisselier | 97 | REFLEXION.md, Pregunta 2, sin salida de `git status` pegada. |
| duarte-6881-34 | Elizabeth Priscila Duarte Nuñez | 93 | REFLEXION.md con Pregunta 1 mal respondida, Pregunta 2 del momento equivocado y Pregunta 3 sin responder. |
| cambarieri-8763-78 | Matías Cambarieri Gentile | 92 | Carátula PDF sin datos identificatorios, `index.html` sin `<html>/<head>/<body>`, commit inicial con tilde. |
| reynoso-4260-07 | Ramiro Javier Reynoso Bascary | 90 | README con placeholders `[ ]` sin remover y DNI mal completado; token en `<h2>` visible, no en comentario HTML. |
| camandulle-5746-93 | Fernanda Camandulle | 87 | Ningún commit usa el mensaje exacto exigido; `.DS_Store` commiteado en la raíz. |
| garciadiaz-9325-19 | Luciano García Díaz | 63 | Todos los archivos del TP anidados en una subcarpeta, no en la raíz del repo; GitHub Pages responde 404; README vacío. |
| airala-2016-08 | Gabriel Airala | 15 | Repositorio de GitHub completamente vacío: sin commits, sin `index.html`, sin capturas, sin REFLEXION.md. |

---

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

---

# Devolución Lab 1 — Rolando Cobis

## Datos identificatorios

- **Nombre:** Rolando Cobis
- **Legajo:** CURZA-9389
- **Token:** cobis-5580-89
- **Repositorio:** https://github.com/cRolandoJr/peylw-2026-practicos-cobis-5580-89
- **GitHub Pages:** https://crolandojr.github.io/peylw-2026-practicos-cobis-5580-89/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | `README.md` trae los 5 campos completos (nombre, legajo, DNI, token, fecha) más los enlaces a repo y Pages. Sin `[Completar]` pendientes. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido de 153.707 bytes (779x418), no corrupto. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | La captura muestra la salida completa de `git config --list`, con `user.email=cobiscalleja@gmail.com` y `user.name=Rolando Cobis` visibles. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-cobis-5580-89`, respeta el formato exigido. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Rolando Cobis</h1>` presente; comentario `<!-- Token único de verificación: cobis-5580-89 -->` — variante semántica aceptable del formato `TOKEN-ALUMNO`. |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `8ac6554`: `Commit inicial: Configurando el index con mi token unico`, incluye `index.html`. Coincide carácter por carácter con lo exigido. |
| Tarea 2 — Repositorio público | ✅ | Confirmado en vivo: etiqueta "Public" visible en GitHub. |
| Tarea 3 — GitHub Pages configurado y funcionando | ✅ | Deployment `github-pages` activo en el repo y contenido servido corresponde al `index.html` del repo. |
| Estructura de archivos correcta | ✅ | `find . -not -path "./.git*"` da exactamente `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png` — sin archivos de más ni de menos. |
| GitHub Pages respondiendo 200 | ✅ | `curl -o /dev/null -w "%{http_code}"` sobre `https://crolandojr.github.io/peylw-2026-practicos-cobis-5580-89/` devuelve `200`. |
| Reflexión — 3 preguntas respondidas | ✅ | Token coincide con nombre de repo y comentario en `index.html`; `git status` pegado literal y corresponde al estado previo al primer commit; pregunta 3 explica correctamente las tres zonas (working directory, staging area, repositorio) y menciona `git add`. |

## Observaciones puntuales

- El alumno no entregó una carátula en PDF/DOCX como especifica el formato de entrega esperado — en su lugar se recibió una captura de pantalla del propio repositorio de GitHub. No hay ítem de rúbrica específico para el formato del archivo entregable, y como el `README.md` del repositorio sí trae la carátula completa con todos los campos, esto no afecta la nota, pero se deja constancia porque es un desvío del canal de entrega solicitado.
- En `README.md`, sección "Configuración local de Git", el alumno explica que usa NixOS con configuración declarativa de Git vía `home-manager`, por lo que no ejecutó `git config --global user.name "..."` de forma interactiva sino que declaró los valores en su configuración de sistema. La captura `capturas/config_git.png` igual muestra `git config --list` con `user.name` y `user.email` resueltos correctamente, que es lo que exige la consigna verificar; no corresponde penalización porque el resultado exigido (valores configurados y visibles) está cumplido.
- En `index.html` el comentario con el token no usa literalmente `<!-- TOKEN-ALUMNO: cobis-5580-89 -->` sino `<!-- Token único de verificación: cobis-5580-89 -->`. La consigna admite "formato equivalente", por lo que no se descuenta, pero se señala la diferencia de literalidad por si en futuras entregas se pide el formato exacto.
- `REFLEXION.md`, pregunta 2: la salida de `git status` está en español (`En la rama main`, `Archivos sin seguimiento`) por tener el entorno de terminal localizado, no en inglés como los ejemplos de la consigna (`On branch main`, `Untracked files:`). Es salida literal real de terminal (no parafraseada) y corresponde al estado previo al primer commit, por lo que cumple igual el ítem.

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
| Estructura de archivos | 10 | 10 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 10 |
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 1 — Carla Yamila Ditrich

## Datos identificatorios

- **Nombre:** Carla Yamila Ditrich
- **Legajo:** 10498
- **Últimos 4 dígitos DNI:** 0827
- **Token:** ditrich-0827-98
- **Repositorio:** https://github.com/Carla-Ditrich/peylw-2026-practicos-ditrich-0827-98
- **GitHub Pages:** https://carla-ditrich.github.io/peylw-2026-practicos-ditrich-0827-98/

**Nota sobre la fuente de estos datos:** la carátula en PDF entregada
(`Practico.1.CarlaDitrich.pdf`) solo contiene dos líneas — el nombre de
la alumna y el enlace al repositorio — sin legajo, DNI, fecha de entrega
ni enlace a GitHub Pages. Legajo, DNI y fecha se tomaron de `README.md`
dentro del repositorio, que sí está completo.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | `README.md` en el repo tiene los 5 campos completos (nombre, legajo, DNI, fecha, enlace). La carátula PDF entregada al margen del repo está incompleta (ver observaciones). |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido (1598x854). |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | Se ve `git config --global user.name/email` y la salida completa de `git config --list` con `user.name=Carla Ditrich` y `user.email=ditrichcarla70@hotmail.com`. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-ditrich-0827-98` respeta el patrón `peylw-2026-practicos-<token>`. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Carla Yamila Ditrich</h1>` presente. Comentario `<!-- ditrich-0827-98 -->` presente, aunque sin la etiqueta `TOKEN-ALUMNO:` sugerida en el enunciado. |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `cf7287b` con mensaje exacto `Commit inicial: Configurando el index con mi token unico`, incluye `index.html`. |
| Tarea 2 — Repositorio público | ✅ | Confirmado vía API de GitHub (`private: false`). |
| Tarea 3 — GitHub Pages configurado y funcionando | ✅ | `has_pages: true`, estado `built`, `public: true` en la API de Pages. |
| GitHub Pages desplegado y respondiendo 200 | ✅ | `curl` a la URL inferida devuelve `200`. Contenido renderizado coincide con `index.html` del repo. |
| Estructura de archivos correcta | ✅ | `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png` — exactamente lo esperado, sin archivos de más ni de menos. |
| Reflexión — 3 preguntas respondidas | ✅ | Las tres respuestas están completas y cumplen lo pedido (ver detalle en observaciones). |

## Observaciones puntuales

1. **Carátula PDF entregada incompleta (`Practico.1.CarlaDitrich.pdf`).** El documento entregado como carátula del trabajo práctico contiene únicamente dos líneas: el nombre de la alumna y el enlace al repositorio. No incluye legajo, últimos 4 dígitos del DNI, fecha de entrega ni el enlace a GitHub Pages, pese a que el enunciado pide todos esos campos en la carátula. El `README.md` del repositorio sí contiene la información completa, y por eso el ítem de rúbrica "README completo" no se penaliza — pero la carátula formalmente entregada para corrección no cumple por sí sola con lo pedido. Se deja constancia como incumplimiento de forma, sin impacto en la nota porque la fuente alternativa (README.md) está completa.
2. **`index.html` — formato del comentario con el token.** El comentario `<!-- ditrich-0827-98 -->` contiene el token pero no usa el formato sugerido en el enunciado (`<!-- TOKEN-ALUMNO: ditrich-0827-98 -->`). Se acepta como equivalente porque el token está presente y es inequívoco.
3. **`REFLEXION.md`, pregunta 3.** La explicación de staging area es correcta en lo esencial pero imprecisa en un punto: dice que en el staging area se preparan cambios "para ser enviados al repositorio local", lo cual mezcla el rol del staging (preparar el próximo commit) con el del commit en sí. No se descuenta porque la distinción entre working directory y staging area queda clara, pero es un matiz a corregir. No menciona `git add` explícitamente.
4. **Commits posteriores al commit inicial.** Hay tres commits adicionales que agregan y corrigen README, REFLEXION y la captura. No se penalizan, conforme a la consigna de corrección.

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
| Reflexión | 10 | 10 |
| **TOTAL** | **100** | **100** |

Cumple todos los ítems de la rúbrica técnica del clon y de la
verificación en vivo. El único incumplimiento real detectado es de
forma y externo al repositorio: la carátula PDF entregada para la
corrección no trae los datos completos que pide el enunciado; no se
tradujo en descuento porque el propio repositorio (README.md) contiene
esa información, pero debe quedar registrado como observación para la
alumna.

---

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
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | `<h1>Sara Celeste Boisselier</h1>` presente; comentario `<!--Token: boisselier-8339-91 -->` presente. El formato del comentario difiere del sugerido pero es equivalente semántico, no se penaliza. |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `cd9f359` con mensaje exacto `Commit inicial: Configurando el index con mi token unico`, contiene únicamente `index.html`. |
| Tarea 2 — Repositorio público | ✅ | Verificado en vivo: el repositorio muestra "Public" en GitHub. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ | `https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/` responde HTTP 200 y muestra el `<h1>` con el nombre de la alumna. |
| Estructura de archivos correcta | ✅ | `find . -not -path "./.git*"` devuelve exactamente `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png` — coincide con lo esperado. |
| Reflexión — 3 preguntas respondidas | ⚠️ | Pregunta 1 y 3 correctas; pregunta 2 no cumple (ver observaciones). |

## Observaciones puntuales

- **`REFLEXION.md`, pregunta 2:** la alumna responde textualmente "No ejecuté el comando `git status` antes de realizar el primer commit, por lo tanto no cuento con la salida correspondiente para responder esta pregunta." No hay salida de terminal pegada. El enunciado pide la salida literal de `git status`; al no existir ninguna salida (ni siquiera parafraseada), el ítem se considera incumplido, no parcial. 0/3.
- **`index.html`:** el comentario con el token usa el formato `<!--Token: boisselier-8339-91 -->` en lugar de `<!-- TOKEN-ALUMNO: boisselier-8339-91 -->`. Se acepta como equivalente semántico, sin descuento, pero se señala como desvío menor del formato sugerido.
- **Consistencia del token:** el token declarado en `REFLEXION.md` (pregunta 1) coincide tanto con el nombre del repositorio como con el comentario en `index.html`. Sin observaciones.
- **Historial de commits:** además del commit inicial exigido, hay tres commits posteriores que agregan README, REFLEXION y la captura, y corrigen un error de nombre de archivo de la captura. No se penaliza por su existencia, conforme a la consigna.

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
| Reflexión (P1: 3, P2: 0, P3: 4) | 10 | 7 |
| **TOTAL** | **100** | **97** |

---

# Devolución Lab 1 — Elizabeth Priscila Duarte Nuñez

## Datos identificatorios

- **Nombre:** Elizabeth Priscila Duarte Nuñez
- **Legajo:** CURZA-9986
- **Token:** duarte-6881-34
- **Repositorio:** https://github.com/Elzzzzo-oss/peylw-2026-practicos-duarte-6881-34
- **GitHub Pages:** https://elzzzzo-oss.github.io/peylw-2026-practicos-duarte-6881-34/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | Todos los campos exigidos presentes en `README.md` (nombre, legajo, últimos 4 dígitos DNI, fecha de entrega, enlace al repo), sin `[Completar]` pendientes. |
| Tarea 1 — Captura `config_git.png` presente | ✅ | Existe en `capturas/config_git.png`, PNG válido (1366x768). |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ | La imagen muestra la salida completa de `git config --list`, incluyendo `user.name=Elizabeth Priscila Duarte Nuñez` y `user.email=priciladuarte2001@gmail.com`. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-duarte-6881-34` respeta el formato `peylw-2026-practicos-<token>`. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ | Estructura HTML básica correcta. `<h1>` con el nombre completo. Comentario `<!-- Token único: duarte-6881-34 -->` presente. |
| Tarea 2 — Commit con mensaje exacto | ✅ | Commit `b553f9d` con el mensaje exacto `Commit inicial: Configurando el index con mi token unico`, incluye `index.html` y la captura. |
| Tarea 2 — Repositorio público | ✅ | Verificado en vivo: repositorio accesible sin restricciones. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ | Verificado en vivo: la URL sirve el contenido real de `index.html`, no un 404. |
| Estructura de archivos correcta | ✅ | `find` sobre el clon devuelve exactamente `index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png`, sin archivos ni carpetas fuera de lugar. |
| Reflexión — 3 preguntas respondidas | ❌ | Pregunta 1 sin respuesta en su lugar (respuesta suelta y errónea al final del archivo). Pregunta 2 con salida literal pero del momento equivocado. Pregunta 3 directamente sin responder. |

## Observaciones puntuales

- **`REFLEXION.md`, Pregunta 1 (Token único):** no hay respuesta debajo de la pregunta. Al final del archivo aparece una línea suelta, desconectada de la pregunta: `Token: peylw-2026-practico-duarte-6881-34`. Esa cadena no es el token solicitado (que es `duarte-6881-34`), sino una construcción tipo nombre-de-repo con error de tipeo: dice `practico` (singular) mientras el repositorio real es `peylw-2026-practicos-duarte-6881-34` (plural). Coincide solo parcialmente y no responde lo que se pidió.
- **`REFLEXION.md`, Pregunta 2 (salida de `git status`):** el texto pegado es literal, pero corresponde al estado previo a un commit posterior ("realice el readmi y reflexion"), no al estado previo al commit inicial exigido. No corresponde al momento pedido por el enunciado.
- **`REFLEXION.md`, Pregunta 3 (staging area vs working directory):** sin respuesta. No hay ningún texto debajo de la pregunta.
- **Historial de commits (menor, no penalizado):** existe un commit `primer commit` anterior al commit inicial exigido, con `index.html` vacío. No afecta la evaluación porque el commit exigido existe con el mensaje exacto y el contenido correcto.
- El resto de los ítems (README, captura, `index.html`, nombre del repo, commit inicial, publicación del repo y de Pages, estructura de archivos) cumple sin observaciones.

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
| Estructura de archivos | 10 | 10 |
| GitHub Pages respondiendo 200 | 10 | 10 |
| Reflexión (P1: 1/3, P2: 2/3, P3: 0/4) | 10 | 3 |
| **TOTAL** | **100** | **93** |

---

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

1. **Carátula PDF entregada (`Laboratorio 1 - Matías Cambarieri Gentile.pdf`):** el archivo tiene una sola página y su único contenido son dos hipervínculos (Repositorio y Página de GitHub Pages). No incluye nombre completo, legajo, últimos 4 dígitos de DNI ni fecha de entrega, campos que el enunciado pide en la carátula. Verificado con extracción de texto completa del PDF, sin más contenido en ninguna otra parte del documento. Los datos identificatorios sí están completos en `README.md` dentro del repositorio, pero la entrega formal (el documento subido) está incompleta.
2. **`index.html` — estructura básica incompleta:** el archivo es únicamente `<!DOCTYPE html>` seguido de un `<h1>` con el nombre y el comentario del token anidado adentro. Falta `<html>`, `<head>` y `<body>`. El enunciado no exige HTML5 completo, pero un `<h1>` colgando directamente del `DOCTYPE` sin las etiquetas contenedoras básicas no llega al piso de "estructura HTML básica" que pide la Tarea 2.
3. **Mensaje del primer commit (`git log`):** el commit `4d2974c` dice "Commit inicial: Configurando el index con mi token **único**" (con tilde en la ú). El enunciado pide el mensaje exacto sin tilde. La diferencia es mínima pero el string no es idéntico, así que no se otorga el puntaje completo.
4. **Inconsistencia de nombre entre archivos:** el PDF entregado usa "Matías Cambarieri Gentile" (también en `README.md`), pero `index.html` usa "Matías **Andrés** Cambarieri Gentile". No se penaliza aparte porque igual constituye un nombre completo válido en el `<h1>`, pero es una inconsistencia entre los documentos de la misma entrega.
5. **Detalle positivo:** el token declarado en `REFLEXION.md` coincide exactamente con el nombre del repositorio y con el comentario de `index.html`. La salida de `git status` en la pregunta 2 es literal y corresponde efectivamente a un estado previo al primer commit, cumpliendo lo pedido.

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

---

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
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ⚠️ parcial | `<h1>` con nombre completo presente y correcto. El token se muestra en un `<h2>reynoso-4260-07</h2>` visible en la página, **no** como comentario HTML. No cumple el formato pedido para el token. |
| Tarea 2 — Commit con mensaje exacto | ✅ cumple | Commit `2bb7050` con mensaje exacto `Commit inicial: Configurando el index con mi token unico`, incluye `index.html` (vacío en ese commit, el contenido se agrega en un commit posterior, lo cual el enunciado no penaliza). |
| Tarea 2 — Repositorio público | ✅ cumple | Confirmado en vivo: repo público. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ cumple | La URL responde y renderiza el `<h1>` con el nombre del alumno. |
| Estructura de archivos correcta | ✅ cumple | `find` sobre el clon coincide exactamente con la estructura esperada (`index.html`, `README.md`, `REFLEXION.md`, `capturas/config_git.png`). |
| Reflexión — 3 preguntas respondidas | ⚠️ parcial | Ver detalle en observaciones. |

## Observaciones puntuales

- **`README.md`**: los campos "Nombre y Apellido", "Legajo/Matrícula", "Últimos 4 dígitos del DNI" y "Enlace al Repositorio de GitHub" quedaron con los corchetes de plantilla sin remover. El campo DNI además está mal completado: figura el DNI completo (8 dígitos) en vez de solo los últimos 4. El nombre consignado en el README ("Ramiro Reynoso") tampoco coincide con el nombre completo real usado en `index.html` y en GitHub ("Ramiro Javier Reynoso Bascary").
- **`index.html`**: no contiene ningún comentario HTML. El token único se puso en un `<h2>` visible en el body, lo cual no satisface el requisito de "comentario HTML con el token único" — el token debía quedar oculto en el marcado, no como contenido visible de la página.
- **Historial de commits**: el commit inicial crea `index.html` vacío; el contenido real se agrega recién en un commit posterior ("Update index.html"). El mensaje de commit evaluado es correcto y el archivo está incluido, por lo que esto no penaliza el sub-ítem del mensaje de commit, pero indica que "configurar el index con el token" en el commit inicial no se cumplió al pie de la letra en ese mismo commit.
- **`REFLEXION.md` — Pregunta 1**: la respuesta es el nombre completo del repositorio en vez del token aislado. El token coincide con el nombre del repo, pero no hay comentario HTML en `index.html` contra el cual contrastarlo, por lo que la verificación de coincidencia queda incompleta.
- **`REFLEXION.md` — Pregunta 2**: correcta, salida literal de `git status` pegada, coherente con el estado previo al commit inicial.
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

---

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

- **`git log` (historial de commits):** el commit inicial real es `eef74dc "first commit"`, y el commit que agrega `index.html` con el token es `63f2425 "Agregar caratula en README e index.html con token unico"`. Ninguno de los cuatro commits usa el mensaje exacto exigido por la consigna. Esto es un incumplimiento directo de la Tarea 2, no una diferencia de redacción menor: el enunciado pide ese mensaje literal y no aparece en ningún punto del historial.
- **Estructura de archivos (raíz del repo):** además de `index.html`, `README.md`, `REFLEXION.md` y `capturas/config_git.png` (correctos), se commiteó `.DS_Store`, un archivo de sistema de macOS que debería estar en `.gitignore` y no en el repositorio.
- **`REFLEXION.md`, Pregunta 2:** la salida de `git status` pegada corresponde al estado previo a un commit posterior que agrega README actualizado, captura y reflexión — no al estado previo al primer commit del `index.html` que la consigna pide documentar. La salida es literal (cumple ese requisito), pero corresponde al momento equivocado del flujo de trabajo.
- **`remote.origin.url` en la captura de `capturas/config_git.png`:** apunta a un usuario distinto (`fercamandulle`) del repositorio real y publicado (`Camandulle`). No afecta la corrección porque el repositorio efectivamente accesible es el declarado en la carátula, pero es una inconsistencia a tener en cuenta.

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

---

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
2. **Estructura de archivos fuera de la raíz del repo.** El repositorio `Lucho-GD/peylw-2026-practicos-garciadiaz-9325-19` tiene, en su raíz, únicamente la carpeta `garciadiaz-9325-19/`; dentro de ella están `index.html`, `readme.md`, `reflexion.md` y `capturas/config_git.png`. El enunciado pide esos archivos directamente en la raíz del repositorio. El enlace que el alumno puso en la carátula (`.../tree/main/garciadiaz-9325-19`) ya delataba este desvío. Se calificó como incumplimiento total del ítem "Estructura de archivos exacta (raíz del repo)": la raíz del repo no contiene ninguno de los archivos pedidos, están todos un nivel más abajo.
3. **GitHub Pages responde 404, consecuencia directa del punto anterior.** GitHub Pages sirve el contenido de la raíz de la rama `main` (salvo configuración explícita de subcarpeta, que no está activada aquí), por lo que al no existir `index.html` en la raíz, la URL devuelve un 404 real de GitHub Pages, verificado con `curl` (código `404`). Por regla, esto es incumplimiento total, sin excepciones, tanto para "Tarea 3" como para el ítem específico de despliegue respondiendo 200.
4. **`garciadiaz-9325-19/reflexion.md`, Pregunta 3.** El bloque contiene texto de plantilla/instrucción pegado sin depurar (la cita textual del enunciado, la instrucción "Podés explicarlo de manera sencilla:" y un bloque de código Markdown sin cerrar). El contenido conceptual de la respuesta es correcto, pero la falta de depuración del texto pegado se penaliza parcialmente conforme a la regla de "respuesta sin adaptación".
5. **Punto positivo:** el token declarado en `reflexion.md` coincide exactamente con el nombre del repositorio y con el comentario HTML en `index.html`. La salida de `git status` pegada en la Pregunta 2 es literal y corresponde a un estado previo al primer commit.
6. El mensaje del primer commit es exacto y correcto, e incluye `index.html`, aunque este viva en la subcarpeta y no en la raíz — el contenido de la Tarea 2 en sí está completo y bien resuelto.

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

---

# Devolución Lab 1 — Gabriel Airala

## Datos identificatorios

- **Nombre:** Gabriel Airala
- **Legajo:** 4508
- **Token:** airala-2016-08
- **Repositorio:** https://github.com/gairala/peylw-2026-practicos-airala-2016-08
- **GitHub Pages:** https://gairala.github.io/peylw-2026-practicos-airala-2016-08/

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ | `REDAME.docx` incluye los 5 campos pedidos (nombre, legajo, últimos 4 dígitos de DNI, fecha de entrega, enlace al repositorio). No incluye enlace a GitHub Pages, pero ese campo no es exigido en la carátula. |
| Tarea 1 — Captura `config_git.png` presente | ❌ | El repositorio está completamente vacío: no existe la carpeta `capturas/` ni ningún otro archivo. |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ❌ | No hay captura para evaluar. |
| Tarea 2 — Nombre del repo con formato correcto | ✅ | `peylw-2026-practicos-airala-2016-08` respeta el formato `peylw-2026-practicos-<token>`. |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ❌ | No existe `index.html`; el repositorio no tiene contenido. |
| Tarea 2 — Commit con mensaje exacto | ❌ | `git log --oneline --all --stat` no devuelve ningún commit. `git status` sobre el clon confirma "No hay commits todavía". |
| Tarea 2 — Repositorio público | ✅ | Confirmado en GitHub: visibilidad pública. |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ❌ | `https://gairala.github.io/peylw-2026-practicos-airala-2016-08/` responde **404 Not Found**. No puede estar configurado porque la rama principal no tiene contenido para publicar. |
| Estructura de archivos correcta | ❌ | `find . -not -path "./.git*"` no devuelve nada: no hay `index.html`, `README.md`, `capturas/` ni `REFLEXION.md`. |
| Reflexión — 3 preguntas respondidas | ❌ | No existe `REFLEXION.md` en el repositorio. |

## Observaciones puntuales

- **Repositorio sin ningún commit.** `git clone` advierte "Pareces haber clonado un repositorio sin contenido" y `git status` muestra la rama `main` sin historial. No se subió `index.html`, `README.md`, `capturas/config_git.png` ni `REFLEXION.md`. Esto incumple de manera total la Tarea 1, la Tarea 2 y la Reflexión.
- **Mensaje de commit inicial ausente por completo.** No se puede verificar el mensaje exigido porque no hay ningún commit en el repositorio.
- **GitHub Pages no funcional.** La URL esperada devuelve 404, consistente con la ausencia total de contenido en el repo.
- **Existe un segundo repositorio público en la cuenta**, `https://github.com/gairala/peylw-2026`, también completamente vacío. No contiene ninguno de los entregables del laboratorio; se deja constancia por si el alumno intentó usarlo por error, pero no aporta puntaje porque tampoco tiene contenido.
- Lo único entregado con contenido real es la carátula `REDAME.docx`, que cumple con los campos requeridos.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | 5 |
| Tarea 1 — captura presente | 10 | 0 |
| Tarea 1 — captura con contenido correcto | 10 | 0 |
| Tarea 2 — nombre del repo | 5 | 5 |
| Tarea 2 — `index.html` correcto | 10 | 0 |
| Tarea 2 — comentario con token | 5 | 0 |
| Tarea 2 — mensaje de commit exacto | 10 | 0 |
| Tarea 2 — repo público | 5 | 5 |
| Tarea 3 — GitHub Pages configurado y funcionando | 10 | 0 |
| Estructura de archivos | 10 | 0 |
| GitHub Pages desplegado y respondiendo 200 | 10 | 0 |
| Reflexión | 10 | 0 |
| **TOTAL** | **100** | **15** |
