# Reglas de Corrección — Laboratorio 1: Configuración de Entorno y Control de Versiones

Este documento extiende las reglas generales de `AGENTS.md` con las
particularidades del Lab 1. Leer ambos antes de corregir; en caso de
conflicto, este archivo tiene prioridad para este laboratorio.

## Tono y estilo de la corrección

- Sin adulación. Sin emojis de aprobación ni frases de relleno motivacional.
- Señalar errores y omisiones citando el archivo y la tarea del enunciado.
- No inflar la nota por esfuerzo percibido. Si falta algo, se descuenta.
- Lo que está bien: una línea. El foco es lo que falta o está mal.

## Escala de calificación

Nota numérica de **0 a 100**, construida sumando el cumplimiento de cada
ítem. Antes de la nota final, desglosar cada ítem con su puntaje parcial.

### Pesos por ítem — Lab 1

| Ítem | Puntos |
|---|---|
| Carátula / README completo con todos los campos | 5 |
| **Tarea 1** — Instalación y configuración de Git (ver detalle) | 20 |
| **Tarea 2** — Repositorio creado y vinculado correctamente (ver detalle) | 35 |
| **Tarea 3** — GitHub Pages configurado y funcionando | 10 |
| Estructura de archivos exacta (raíz del repo) | 10 |
| GitHub Pages desplegado y respondiendo 200 | 10 |
| **Reflexión** — `REFLEXION.md` con las 3 preguntas respondidas (ver detalle) | 10 |
| **TOTAL** | **100** |

#### Detalle Tarea 1 — Configuración de Git (20 pts)

| Sub-ítem | Puntos |
|---|---|
| Captura `capturas/config_git.png` presente en el repositorio | 10 |
| La captura muestra la salida de `git config --list` con `user.name` y `user.email` visibles | 10 |

#### Detalle Tarea 2 — Repositorio y commits (35 pts)

| Sub-ítem | Puntos |
|---|---|
| Nombre del repositorio respeta el formato `peylw-2026-practicos-<token>` | 5 |
| `index.html` presente con estructura básica y `<h1>` con nombre completo | 10 |
| Comentario HTML con token único presente en `index.html` | 5 |
| Primer commit con mensaje `Commit inicial: Configurando el index con mi token unico` | 10 |
| Repositorio público en GitHub | 5 |

#### Detalle Reflexión — `REFLEXION.md` (10 pts)

| Sub-ítem | Puntos |
|---|---|
| Pregunta 1: Token único indicado y coincide con el del repositorio | 3 |
| Pregunta 2: Salida literal de `git status` pegada (no parafraseda) | 3 |
| Pregunta 3: Explicación correcta de staging area vs working directory | 4 |

## Verificación en internet

- Acceder al repositorio de GitHub del alumno para confirmar que es público.
- Acceder a la URL de GitHub Pages para confirmar que responde 200 (no 404).
  URL esperada: `https://<usuario>.github.io/peylw-2026-practicos-<token>/`
- Si Pages devuelve 404 o el repo es privado: incumplimiento total del ítem
  correspondiente, sin excepciones.

## Clonado y revisión local

- Clonar en `Laboratorios/Lab01/repos-clonados/<token-del-alumno>/`.
- Revisar estructura real con `find . -not -path "./.git*"`.
- Verificar historial con `git log --oneline --all --stat`:
  - El mensaje del primer commit debe ser exactamente
    `Commit inicial: Configurando el index con mi token unico`.
  - Si hay commits adicionales posteriores, no penalizar por existir.
- Leer `index.html`, `README.md` y `REFLEXION.md` sobre el clon local.
- Cruzar el token declarado en `REFLEXION.md` con el nombre real del repo y
  el comentario HTML en `index.html`. Inconsistencias se penalizan en el ítem
  de reflexión (pregunta 1).
- No modificar ni commitear nada en el clon.
- Diferencias de casing en nombres de archivo (`reflexion.md` vs
  `REFLEXION.md`) no se penalizan.

## Verificaciones específicas de `index.html`

Al leer el archivo sobre el clon, confirmar:

- Que exista estructura HTML básica válida.
- Que haya un `<h1>` con el nombre completo del alumno.
- Que exista un comentario HTML con el token único en formato
  `<!-- TOKEN-ALUMNO: <token> -->` o similar equivalente.
- Que el archivo no esté vacío ni sea un placeholder.

## Verificación de la captura

- Confirmar que `capturas/config_git.png` existe como archivo de imagen.
- Si el archivo existe pero no es una imagen válida, o está vacío: parcial.
- La captura debe mostrar al menos `user.name` y `user.email` configurados.
  Si muestra la salida completa de `git config --list`, mejor, pero no es
  requisito estricto.

## Archivo de devolución por alumno

- Guardar en `Laboratorios/Lab01/devoluciones/<token-del-alumno>.md`.
- Al terminar todas las entregas del lab, generar el consolidado
  `Laboratorios/Lab01/devoluciones/Lab01-devoluciones-completas.md` con
  tabla resumen al inicio y la devolución completa de cada alumno a continuación.

## Formato del informe de corrección

Por cada alumno entregar:

1. **Datos identificatorios**: nombre, legajo, token, enlace al repo,
   enlace a GitHub Pages.
2. **Checklist por ítem** con estado: ✅ cumple / ❌ no cumple / ⚠️ parcial
   y motivo concreto.
3. **Observaciones puntuales**: errores específicos con archivo y sección afectada.
4. **Nota final (0–100)** con desglose ítem por ítem que la justifica.
