# Reglas de Corrección — Laboratorio 5: JavaScript

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 5. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

Fechas oficiales: apertura lunes 21/09/2026 00:00 — cierre viernes 06/11/2026
23:00. Entregas posteriores al cierre: marcar como tardías según criterio
general del curso (este documento no define penalización por atraso).

## Formato de entrega — igual a Lab 4

Este TP usa **formato avanzado**, igual que Lab 4: el enunciado solo pide
colocar la URL de la página en GitHub (GitHub Pages) una vez finalizada, ya
desplegada.

- **No** se exige carátula README.md con tabla de datos del alumno.
- **No** se exige `REFLEXION.md`.
- **No** hay un mensaje de commit exacto a verificar.
- **No** se exige comentario de token único adicional.

Si el alumno igual entrega un README/REFLEXION heredado de labs anteriores,
no se penaliza ni se exige actualizarlo; simplemente no forma parte de la
rúbrica de este TP. Si la entrega llega como PDF/DOCX con un enlace (en vez
de URL directa), extraer el enlace igual que en labs anteriores (ver
`context-Lab05.md`).

## Tono y estilo de la corrección

- Sin adulación. Sin emojis de aprobación ni frases de relleno motivacional.
- Señalar errores y omisiones citando el archivo y la tarea del enunciado.
- No inflar la nota por esfuerzo percibido. Si falta algo, se descuenta.
- Lo que está bien: una línea. El foco es lo que falta o está mal.

## Continuidad con Lab 3

La tabla de resumen y los campos del formulario que este TP debe conectar
con JavaScript son los definidos en el Lab 3 (`contacto.html`). IDs de
celda esperados: `resumen-nombre`, `resumen-apellido`, `resumen-email`,
`resumen-telefono`, `resumen-edad`, `resumen-direccion`,
`resumen-provincia`, `resumen-cp`, `resumen-metodo`,
`resumen-suscripciones`. Si el alumno cambió esos IDs en algún momento
entre Lab 3 y este TP, verificar que el `script.js` los referencia
correctamente contra los IDs **reales** actuales del HTML, no contra los
del enunciado de Lab 3.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 5

| Ítem | Puntos |
|---|---|
| `script.js` — creación y vinculación (ver detalle) | 15 |
| Interactividad formulario → tabla, en tiempo real (ver detalle) | 65 |
| "Acerca de" — botón "Leer más" (ver detalle) | 20 |
| **TOTAL** | **100** |

#### Detalle `script.js` (15 pts)

| Sub-ítem | Puntos |
|---|---|
| Archivo `script.js` creado en la raíz del repositorio | 5 |
| Vinculado en `contacto.html` mediante `<script src="script.js">` | 5 |
| Sin errores de JavaScript en la consola del navegador al cargar la página | 5 |

#### Detalle Interactividad formulario → tabla (65 pts)

| Sub-ítem | Puntos |
|---|---|
| Mecanismo de actualización sin botón (eventos `input`/`change`/`blur`, no requiere `submit` ni click en "Cargar") | 15 |
| Nombre se refleja en `resumen-nombre` | 5 |
| Apellido se refleja en `resumen-apellido` | 5 |
| Email se refleja en `resumen-email` | 5 |
| Teléfono se refleja en `resumen-telefono` | 5 |
| Edad se refleja en `resumen-edad` | 5 |
| Dirección se refleja en `resumen-direccion` | 5 |
| Provincia se refleja en `resumen-provincia` | 5 |
| Código Postal se refleja en `resumen-cp` | 5 |
| Método de Contacto (radio seleccionado) se refleja en `resumen-metodo` y se actualiza al cambiar de opción | 5 |
| Suscripciones (checkboxes marcados) se reflejan en `resumen-suscripciones`, lista actualizada al marcar/desmarcar cualquiera | 5 |

Si algún campo actualiza la tabla solo al enviar el formulario (con el
botón "Cargar") en vez de "al terminar de rellenar cada campo": ❌ en el
sub-ítem general de mecanismo (15 pts), aunque los valores individuales
lleguen a mostrarse.

Si un campo de texto se refleja solo con `onblur` (al perder foco) en vez
de en cada tecleo: no se penaliza — "al terminar de rellenar cada campo" es
compatible con eventos `change`/`blur`, no exige `keyup`/`input` en cada
carácter, aunque tampoco se descuenta si el alumno lo implementó así.

#### Detalle "Acerca de" — botón "Leer más" (20 pts)

| Sub-ítem | Puntos |
|---|---|
| Botón "Leer más" presente y visible en `acercade.html` | 5 |
| Currículum abreviado visible por defecto (versión corta, no el CV completo) | 5 |
| Al hacer clic, se revela el CV completo (contenido adicional; Lorem Ipsum aceptable) | 10 |

Si el botón existe pero el contenido "completo" ya estaba visible desde el
inicio (el clic no cambia nada perceptible): ❌ en el tercer sub-ítem.

## Verificación en internet

- Acceder a la URL de GitHub Pages entregada y confirmar que responde 200.
- Sobre el sitio ya desplegado (no alcanza con leer el código):
  - Completar cada campo del formulario de `contacto.html` y confirmar que
    la tabla de resumen se actualiza sin necesidad de hacer clic en
    "Cargar".
  - Probar especialmente los radios y checkboxes: cambiar de opción y
    verificar que la celda correspondiente se actualiza también, no solo
    la primera vez.
  - Abrir la consola del navegador (F12) mientras se interactúa con el
    formulario para detectar errores de JavaScript.
  - En `acercade.html`, hacer clic en "Leer más" y confirmar que se revela
    contenido adicional del currículum.
- Si Pages devuelve 404 o algún efecto no se puede reproducir en el sitio
  desplegado (aunque el código lo sugiera): registrar como incumplimiento
  del ítem correspondiente, no asumir que "andará".

## Clonado y revisión local

- Clonar (o reutilizar el clon de labs anteriores) en
  `lab5/repos-clonados/<token-del-alumno>/` y hacer `git pull` si ya existía.
- Revisar `script.js` y `contacto.html`/`acercade.html` sobre el clon local.
- No modificar ni commitear nada en el clon.
- No hay mensaje de commit exacto que verificar en este TP; alcanza con
  confirmar que `script.js` y sus vinculaciones están presentes en el repo.

## Archivo de devolución por alumno

- Guardar en `lab5/devoluciones/<token-del-alumno>.md`.
- Al terminar todas las entregas del lab, generar el consolidado
  `lab5/devoluciones/Lab05-devoluciones-completas.md` con tabla resumen al
  inicio y la devolución completa de cada alumno a continuación.

## Formato del informe de corrección

Por cada alumno entregar:

1. **Datos identificatorios**: nombre (si se conoce por labs anteriores),
   token, enlace a GitHub Pages.
2. **Checklist por ítem** con estado: ✅ cumple / ❌ no cumple / ⚠️ parcial
   y motivo concreto.
3. **Observaciones puntuales**: errores específicos con archivo y sección afectada.
4. **Nota final (0–100)** con desglose ítem por ítem que la justifica.
