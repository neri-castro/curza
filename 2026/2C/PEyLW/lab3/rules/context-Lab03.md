# Contexto y método de trabajo — Corrección Lab 3: Captura de Datos y Validación Semántica con Formularios HTML5

Este documento describe **cómo ejecutar la corrección paso a paso** para el
Laboratorio 3. Las reglas de fondo (tono, escala, penalizaciones) están en
`AGENTS-Lab03.md` — leer ambos antes de empezar.

Enunciado oficial: `Trabajo Práctico 3: Captura de Datos y Validación
Semántica con Formularios HTML5`. Apertura 06/09/2026 00:00, cierre
28/09/2026 23:55.

## Estructura de carpetas esperada

```
lab3/
├── rules/
│   ├── AGENTS-Lab03.md               # reglas específicas Lab 3
│   └── context-Lab03.md              # este archivo
├── <archivo-de-entrega-del-alumno>.pdf | .docx   # carátula con link al repo
├── entregas.md                       # enlaces extraídos de cada entrega
├── repos-clonados/
│   └── <token-del-alumno>/           # clon local (solo lectura)
└── devoluciones/
    ├── <token-del-alumno>.md                 # devolución individual
    └── Lab03-devoluciones-completas.md       # consolidado con tabla resumen
```

Si el alumno ya tiene un clon de Lab 1/Lab 2 en
`lab2/repos-clonados/<token>/`, para Lab 3 se puede reutilizar haciendo
`git pull` dentro de un clon nuevo en `lab3/repos-clonados/<token>/`, ya que
normalmente es el mismo repositorio `peylw-2026-practicos-<token>` extendido
con `contacto.html`.

---

## Paso 1 — Leer el enunciado

Releer la consigna del Laboratorio 3 antes de corregir cualquier entrega. La
rúbrica real, el mensaje de commit exacto, los nombres de campos y la
estructura de entregables salen de ahí, no de memoria. Puntos clave a tener
frescos:

- Página nueva: `contacto.html`, con la misma cabecera/nav/footer que
  `index.html` y `acercade.html`.
- Token único en comentario HTML en el encabezado de `contacto.html`.
- Botón de envío con `id="btn-cargar-[tu-token-unico]"`.
- `<nav>` actualizado en las **tres** páginas con el enlace "Contacto".
- Formulario con 11 controles y validación nativa estricta (sin JavaScript):
  Nombre, Apellido, Email, Teléfono, Edad, Dirección, Provincia (con
  `<datalist>`), Código Postal (con `pattern` + `title`), Método de Contacto
  (radios), Suscripción de Interés (checkboxes), botón "Cargar".
- Código Postal: `pattern="^[A-Z]\d{4}[A-Z]{3}$"`, debe rechazar `"8500"` y
  `"R8500"`, aceptar `"R8500AAF"`.
- Tabla de resumen vacía debajo del formulario, con 10 `<td>` de IDs
  específicos (ver lista completa en `AGENTS-Lab03.md`).
- `styles.css` vinculado en `contacto.html`.
- Commit final con mensaje exacto:
  `TP3: Implementacion de formulario contacto con validacion`.

---

## Paso 2 — Extraer el enlace al repositorio de cada entrega

El archivo entregado por el alumno es un PDF o DOCX con la carátula. El
texto visible de un hipervínculo puede no coincidir con el `href` real.

**Para PDF** — extraer hrefs reales con `pymupdf`:

```python
import fitz
doc = fitz.open("lab3/<carpeta-o-archivo>.pdf")
for page in doc:
    for link in page.get_links():
        print(link.get("uri"))
```

**Para DOCX** — extraer texto plano y, si hace falta, los hrefs de relaciones:

```python
import zipfile, re

# Texto plano
z = zipfile.ZipFile("lab3/<carpeta-o-archivo>.docx")
xml = z.read("word/document.xml").decode("utf-8")
print(re.sub("<[^>]+>", "", xml))

# Hrefs reales de hipervínculos
rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
print(rels)
```

Registrar siempre los dos enlaces obtenidos (repositorio GitHub y GitHub
Pages) en `lab3/entregas.md`. Si el alumno solo entregó uno de los dos,
anotarlo como observación.

---

## Paso 3 — Clonar (o actualizar) el repositorio

```bash
git clone <url-del-repo> "lab3/repos-clonados/<token-del-alumno>"
# o, si ya existe el clon de Lab 1/Lab 2 y se reutiliza el mismo repo:
git -C "lab3/repos-clonados/<token-del-alumno>" pull
```

**Si el clone falla con "Repository not found":**

1. Visitar `https://github.com/<usuario>?tab=repositories` para ver el
   nombre real del repo.
2. El nombre esperado según enunciado es `peylw-2026-practicos-<token>`.
   Si difiere, clonar con el nombre real y anotar la discrepancia.
3. Si el repo es privado, registrar como incumplimiento de publicación.

---

## Paso 4 — Revisar el clon local

Ejecutar sobre el clon (nunca modificar nada):

### 4.1 Estructura de archivos

```bash
find . -not -path "./.git*" | sort
```

Comparar contra la estructura pedida en el enunciado:

```
peylw-2026-practicos-<token>/
├── index.html (actualizado con enlace a Contacto)
├── acercade.html (actualizado con enlace a Contacto)
├── contacto.html (formulario nuevo de este TP)
├── styles.css
├── img/
├── README.md (carátula del TP3)
└── REFLEXION.md (análisis)
```

Anotar archivos faltantes o fuera de lugar.

### 4.2 Historial de commits

```bash
git log --oneline --all --stat
```

Verificar:

- Que exista un commit con el mensaje exacto:
  `TP3: Implementacion de formulario contacto con validacion`
- Que ese commit incluya `contacto.html` (y, si corresponde, los cambios de
  `<nav>` en `index.html`/`acercade.html`).
- Si hay commits adicionales, no penalizar por su existencia; el mensaje
  del commit de entrega del TP3 es el que se evalúa.

### 4.3 Revisión de la navegación en `index.html` y `acercade.html`

- Confirmar que el `<nav>` de ambas páginas ahora incluye un tercer enlace
  "Contacto" apuntando a `contacto.html`, sin haber roto la estructura de
  `<header>`, `<h1>` ni `<footer>` heredada de Lab 2.

### 4.4 Revisión de `contacto.html`

Leer el archivo y verificar ítem por ítem contra el enunciado:

- `<!DOCTYPE html>`, `<html lang="es">`, `<meta charset="utf-8">`, `<title>`
  descriptivo.
- `<link>` a `styles.css`.
- Comentario de Token Único en el encabezado.
- `<header>`, `<nav>` (con los 3 enlaces) y `<footer>` consistentes con las
  otras páginas.
- `<main>` con sección de formulario y `<h2>` descriptivo.
- Formulario (`<form>`) con los 11 controles pedidos. Verificar campo por
  campo contra la tabla de la Tarea 2 del enunciado:
  - Nombre: `type="text"`, `required`, `maxlength="20"`.
  - Apellido: `type="text"`, `maxlength="20"`.
  - Email: `type="email"`, `required`.
  - Teléfono: placeholder exacto `Ej: +54 2920 123456`.
  - Edad: `type="number"`, `min="16"`, `max="120"`.
  - Dirección: campo de texto libre.
  - Provincia: `<input>` + `<datalist>` con Río Negro, Neuquén, Chubut,
    Santa Cruz, Tierra del Fuego, La Pampa.
  - Código Postal: `pattern="^[A-Z]\d{4}[A-Z]{3}$"` (o equivalente
    funcional) + `title` con advertencia de formato.
  - Método de Contacto: 3 `type="radio"` con el **mismo** `name`,
    "Correo electrónico" con `checked`.
  - Suscripción de Interés: 4 `type="checkbox"`, "Alertas" con `checked`.
  - Botón `type="submit"` con etiqueta "Cargar" e
    `id="btn-cargar-[token]"`.
- Verificar asociación `<label for="...">` ↔ `id` del control en cada campo
  (no descuenta puntaje de validación por sí solo, pero se registra como
  observación).
- Tabla de resumen vacía debajo del formulario con los 10 `<td>` de IDs
  exactos (`resumen-nombre`, `resumen-apellido`, `resumen-email`,
  `resumen-telefono`, `resumen-edad`, `resumen-direccion`,
  `resumen-provincia`, `resumen-cp`, `resumen-metodo`,
  `resumen-suscripciones`), completamente vacíos.

### 4.5 Revisión de `styles.css`

- Confirmar que `<link rel="stylesheet" href="styles.css">` (o ruta
  equivalente) está presente en el `<head>` de `contacto.html`.

### 4.6 Revisión de `README.md`

Verificar que la carátula incluya todos los campos del enunciado:

- Nombre y apellido
- Legajo / Matrícula
- Últimos 4 dígitos del DNI
- Fecha de entrega
- Enlace al repositorio de GitHub
- Enlace a la página en GitHub Pages

Si algún campo tiene `[Completar]` sin reemplazar: ⚠️ parcial, descontar
proporcionalmente dentro del ítem de README.

### 4.7 Revisión de `REFLEXION.md`

Leer las tres respuestas y evaluar:

**Pregunta 1 — Código del campo Código Postal:**
- Debe transcribir el `<input>` con `pattern` y `title` tal cual está en
  `contacto.html`. Confirmar que coincide con el HTML real del repo.
- Si el `pattern`/`title` transcripto no coincide con el usado realmente:
  ⚠️ parcial.

**Pregunta 2 — `<label>` y `for`:**
- Debe explicar con sus palabras para qué sirve `<label>` (accesibilidad,
  clic ampliado sobre el control, lectores de pantalla) y cómo el atributo
  `for` lo asocia al `id` del campo correspondiente.
- Respuesta de una línea sin justificación real, o copiada textual de
  internet sin adaptación: ⚠️ parcial.

**Pregunta 3 — Radios con `name` distinto vs. mismo `name`:**
- Debe explicar que con `name` distinto los radios actúan de forma
  independiente (se pueden marcar varios a la vez, perdiendo la exclusión
  mutua), y que con el mismo `name` forman un grupo donde solo uno puede
  estar seleccionado.
- Respuesta vaga o incorrecta sobre el comportamiento real: ⚠️ parcial.

---

## Paso 5 — Verificar en vivo lo publicado

### 5.1 Repositorio GitHub

Visitar `https://github.com/<usuario>/peylw-2026-practicos-<token>` y
confirmar que el repo es público y la rama principal tiene los archivos
nuevos del TP3.

### 5.2 GitHub Pages

Probar con `WebFetch` la URL:
`https://<usuario>.github.io/peylw-2026-practicos-<token>/contacto.html`

- Respuesta **200**: Pages desplegado correctamente.
- Respuesta **404**: incumplimiento total del ítem Pages. No asumir que
  "estará bien después". Registrar como incumplimiento.
- Navegar entre las tres páginas (Inicio, Acerca de, Contacto) usando los
  enlaces reales del sitio desplegado para confirmar que las rutas
  relativas funcionan también en producción (no solo en local).
- Si es posible interactuar con el formulario desplegado, intentar enviar
  con un Código Postal inválido (ej. `"8500"`) y confirmar que el navegador
  bloquea el envío mostrando el mensaje de validación del `pattern`.

Si el nombre del repo difiere del esperado, ajustar la URL de Pages en
consecuencia y anotar la discrepancia.

---

## Paso 6 — Redactar la devolución individual

Guardar en `lab3/devoluciones/<token-del-alumno>.md` con el siguiente
formato:

```markdown
# Devolución Lab 3 — [Nombre Completo]

## Datos identificatorios

- **Nombre:** [Nombre Completo]
- **Legajo:** [Legajo]
- **Token:** [token]
- **Repositorio:** [URL]
- **GitHub Pages:** [URL]

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| README / carátula completa | ✅ / ⚠️ / ❌ | ... |
| Personalización — Token en comentario | ✅ / ⚠️ / ❌ | ... |
| Personalización — `id` del botón de envío | ✅ / ⚠️ / ❌ | ... |
| Navegación — enlace "Contacto" en `index.html` | ✅ / ⚠️ / ❌ | ... |
| Navegación — enlace "Contacto" en `acercade.html` | ✅ / ⚠️ / ❌ | ... |
| Navegación — `<nav>` de `contacto.html` con 3 enlaces | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — estructura base `contacto.html` | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — campos de texto (Nombre/Apellido/Email/Teléfono/Dirección) | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Edad (`number`, `min`/`max`) | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Provincia (`datalist`) | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Código Postal (`pattern` + `title`) | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Método de Contacto (radios) | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Suscripción de Interés (checkboxes) | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — botón "Cargar" | ✅ / ⚠️ / ❌ | ... |
| Tarea 3 — tabla de resumen vacía con IDs exactos | ✅ / ⚠️ / ❌ | ... |
| Tarea 4 — `styles.css` vinculado | ✅ / ⚠️ / ❌ | ... |
| Tarea 4 — commit con mensaje exacto | ✅ / ⚠️ / ❌ | ... |
| Estructura de archivos correcta | ✅ / ⚠️ / ❌ | ... |
| GitHub Pages desplegado y respondiendo 200 | ✅ / ⚠️ / ❌ | ... |
| Reflexión — 3 preguntas respondidas | ✅ / ⚠️ / ❌ | ... |

## Observaciones puntuales

[Lista concreta de errores, archivos faltantes o desvíos del enunciado,
citando archivo y sección cuando corresponda.]

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | ... |
| Personalización | 8 | ... |
| Vinculación de navegación | 7 | ... |
| Tarea 1 — estructura base `contacto.html` | 8 | ... |
| Tarea 2 — formulario y validaciones | 35 | ... |
| Tarea 3 — tabla de resumen vacía | 10 | ... |
| Tarea 4 — `styles.css` y commit | 7 | ... |
| Estructura de archivos | 5 | ... |
| GitHub Pages | 5 | ... |
| Reflexión | 10 | ... |
| **TOTAL** | **100** | **...** |
```

---

## Paso 7 — Consolidado final

Al terminar todas las entregas del laboratorio, generar
`lab3/devoluciones/Lab03-devoluciones-completas.md` con:

1. Tabla resumen al inicio:

```markdown
## Tabla resumen — Lab 3

| Token | Nombre | Nota |
|---|---|---|
| perez-4567-89 | Juan Pérez | 87 |
| ... | ... | ... |
```

2. Devolución completa de cada alumno a continuación (mismo contenido que
   los archivos individuales), separadas por `---`.

---

## Reentregas

Si aparece una entrega nueva para un alumno ya corregido:

1. Repetir Pasos 2 a 5 sobre la entrega nueva.
2. Actualizar el archivo de devolución individual sin borrar la nota anterior:
   agregar sección `## Historial de correcciones` con tabla
   (entrega → nota → motivo principal) y señalar explícitamente qué se
   corrigió, qué no se corrigió y si algo empeoró.
3. Actualizar la fila correspondiente en la tabla resumen del consolidado
   indicando la nota nueva y la nota anterior entre paréntesis.
