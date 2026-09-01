# Contexto y método de trabajo — Corrección Lab 2: Estructura y Semántica Web con HTML5

Este documento describe **cómo ejecutar la corrección paso a paso** para el
Laboratorio 2. Las reglas de fondo (tono, escala, penalizaciones) están en
`AGENTS-Lab02.md` — leer ambos antes de empezar.

Enunciado oficial: `Laboratorio 2: Estructura y Semántica Web con HTML5`
(PDF fuente: `curza-2026-web-estatica_ Laboratorio 2 - HTML.pdf`). Apertura
31/08/2026 00:00, cierre 07/09/2026 23:55.

## Estructura de carpetas esperada

```
lab2/
├── rules/
│   ├── AGENTS-Lab02.md               # reglas específicas Lab 2
│   └── context-Lab02.md              # este archivo
├── <archivo-de-entrega-del-alumno>.pdf | .docx   # carátula con link al repo
├── repos-clonados/
│   └── <token-del-alumno>/           # clon local (solo lectura)
└── devoluciones/
    ├── <token-del-alumno>.md                 # devolución individual
    └── Lab02-devoluciones-completas.md       # consolidado con tabla resumen
```

Si el alumno ya tiene un clon de Lab 1 en `lab1/repos-clonados/<token>/`,
para Lab 2 se puede reutilizar haciendo `git pull` dentro de un clon nuevo
en `lab2/repos-clonados/<token>/`, ya que normalmente es el mismo
repositorio `peylw-2026-practicos-<token>` extendido con los archivos
nuevos de este TP.

---

## Paso 1 — Leer el enunciado

Releer el PDF del Laboratorio 2 antes de corregir cualquier entrega. La
rúbrica real, el mensaje de commit exacto, los nombres de archivo y la
estructura de entregables salen de ahí, no de memoria. Puntos clave a tener
frescos:

- Dos páginas: `index.html` (Inicio) y `acercade.html` (Acerca de).
- Token en comentario HTML al inicio del `<body>` en **ambos** archivos.
- `<h1>` exacto en ambas páginas: `Portal de [Nombre Completo] - [Token]`.
- Biografía real (mínimo dos párrafos) en `acercade.html`, no relleno.
- `styles.css` vinculado con `<link>` en ambas páginas.
- Commit final con mensaje exacto:
  `TP2: Estructuras HTML y vinculacion de estilos`.

---

## Paso 2 — Extraer el enlace al repositorio de cada entrega

El archivo entregado por el alumno es un PDF o DOCX con la carátula. El
texto visible de un hipervínculo puede no coincidir con el `href` real.

**Para PDF** — extraer hrefs reales con `pymupdf`:

```python
import fitz
doc = fitz.open("lab2/<carpeta-o-archivo>.pdf")
for page in doc:
    for link in page.get_links():
        print(link.get("uri"))
```

**Para DOCX** — extraer texto plano y, si hace falta, los hrefs de relaciones:

```python
import zipfile, re

# Texto plano
z = zipfile.ZipFile("lab2/<carpeta-o-archivo>.docx")
xml = z.read("word/document.xml").decode("utf-8")
print(re.sub("<[^>]+>", "", xml))

# Hrefs reales de hipervínculos
rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
print(rels)
```

Registrar siempre los dos enlaces obtenidos (repositorio GitHub y GitHub
Pages). Si el alumno solo entregó uno de los dos, anotarlo como observación.

---

## Paso 3 — Clonar (o actualizar) el repositorio

```bash
git clone <url-del-repo> "lab2/repos-clonados/<token-del-alumno>"
# o, si ya existe el clon de Lab 1 y se reutiliza el mismo repo:
git -C "lab2/repos-clonados/<token-del-alumno>" pull
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
├── index.html (página de bienvenida)
├── acercade.html (página de biografía e imagen)
├── styles.css (hoja de estilos básica vinculada)
├── img/
│   └── [su_imagen_de_perfil.png/.jpg]
├── README.md (carátula del TP2)
└── REFLEXION.md (análisis)
```

Anotar archivos faltantes, archivos fuera de lugar, o la imagen guardada
fuera de `img/`.

### 4.2 Historial de commits

```bash
git log --oneline --all --stat
```

Verificar:

- Que exista un commit con el mensaje exacto:
  `TP2: Estructuras HTML y vinculacion de estilos`
- Que ese commit incluya `index.html`, `acercade.html`, `styles.css` y la
  imagen de `img/` (o que estos archivos ya estén en el historial previo al
  commit final).
- Si hay commits adicionales, no penalizar por su existencia; el mensaje
  del commit de entrega del TP2 es el que se evalúa.

### 4.3 Revisión de `index.html`

Leer el archivo y verificar ítem por ítem contra el enunciado:

- `<!DOCTYPE html>` y `<html lang="es">`.
- `<head>` con `<meta charset="utf-8">` y `<title>` descriptivo.
- `<link>` a `styles.css`.
- Comentario `<!-- TOKEN-ALUMNO: <token> -->` al inicio del `<body>`.
- `<header>` con `<h1>` exactamente `Portal de [Nombre Completo] - [Token]`.
- `<nav>` con `<ul>` y dos enlaces relativos: "Inicio" (`index.html`) y
  "Acerca de" (`acercade.html`).
- `<main>` con `<section>` de bienvenida: `<h2>` "Bienvenidos a mi espacio"
  y al menos dos párrafos explicativos del sitio.
- `<footer>` con copyright (© 2026 [Nombre]), dirección del nodo (CURZAS -
  UNCo, Viedma, Río Negro) y el token en texto simple.

### 4.4 Revisión de `acercade.html`

- `<header>`, `<nav>` y `<footer>` deben ser idénticos (o equivalentes) a
  los de `index.html`, incluyendo el mismo comentario de token y el mismo
  `<h1>`.
- `<main>` con:
  - `<article>` con biografía real (no texto de relleno), dividida en dos
    `<section>`, sobre el interés del alumno por la Tecnicatura en
    Desarrollo Web.
  - `<figure>` + `<figcaption>` con una imagen cargada desde `img/` con
    ruta relativa (ej. `img/mi_foto.jpg`) y `<img alt="...">` con texto
    alternativo específico (no genérico).
  - `<ul>` con lenguajes de programación o tecnologías de interés.

### 4.5 Revisión de `styles.css`

- Confirmar que existe en la raíz y contiene al menos la regla de `body`
  (no hace falta que sea idéntica al ejemplo del enunciado, pero debe
  tener contenido real, no vacío).
- Confirmar que `<link rel="stylesheet" href="styles.css">` (o ruta
  equivalente) está presente en el `<head>` de **ambos** archivos HTML.

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

**Pregunta 1 — Nombre de la imagen y `alt`:**
- El nombre de archivo declarado debe coincidir con el que realmente está
  en `img/`, y el valor de `alt` declarado debe coincidir con el que
  realmente está en `acercade.html`.
- Si no coincide alguno de los dos: ⚠️ parcial.

**Pregunta 2 — Semántica vs `<div>`:**
- Debe explicar con sus palabras por qué usar `<main>`/`<nav>`/etc. en vez
  de `<div>` genéricos (accesibilidad, lectores de pantalla, SEO,
  mantenibilidad del código).
- Respuesta de una línea sin justificación real, o copiada textual de
  internet sin adaptación: ⚠️ parcial.

**Pregunta 3 — Verificación de rutas de navegación:**
- Debe describir cómo comprobó que los enlaces del `<nav>` funcionan tanto
  abriendo el HTML localmente como en el sitio ya desplegado en GitHub
  Pages (ej. abrir el archivo en el navegador, o cliquear los enlaces
  desde la URL de Pages).
- Respuesta vaga ("lo probé y andaba") sin mencionar cómo: ⚠️ parcial.

---

## Paso 5 — Verificar en vivo lo publicado

### 5.1 Repositorio GitHub

Visitar `https://github.com/<usuario>/peylw-2026-practicos-<token>` y
confirmar que el repo es público y la rama principal tiene los archivos
nuevos del TP2.

### 5.2 GitHub Pages

Probar con `WebFetch` la URL:
`https://<usuario>.github.io/peylw-2026-practicos-<token>/`

- Respuesta **200**: Pages desplegado correctamente.
- Respuesta **404**: incumplimiento total del ítem Pages. No asumir que
  "estará bien después". Registrar como incumplimiento.
- Navegar desde la home a `acercade.html` y viceversa usando los enlaces
  reales del sitio desplegado para confirmar que las rutas relativas
  funcionan también en producción (no solo en local).

Si el nombre del repo difiere del esperado, ajustar la URL de Pages en
consecuencia y anotar la discrepancia.

---

## Paso 6 — Redactar la devolución individual

Guardar en `lab2/devoluciones/<token-del-alumno>.md` con el siguiente
formato:

```markdown
# Devolución Lab 2 — [Nombre Completo]

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
| Personalización — Token en comentario (ambos archivos) | ✅ / ⚠️ / ❌ | ... |
| Personalización — `<h1>` exacto (ambos archivos) | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — `index.html`: plantilla HTML5 + head | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — `index.html`: `<header>` | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — `index.html`: `<nav>` con enlaces relativos | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — `index.html`: `<main>` bienvenida | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — `index.html`: `<footer>` | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — `acercade.html`: header/nav/footer consistentes | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — `acercade.html`: biografía real en `<article>`/`<section>` | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — `acercade.html`: `<figure>`/`<figcaption>`/`alt` | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — `acercade.html`: lista de tecnologías | ✅ / ⚠️ / ❌ | ... |
| Tarea 3 — `styles.css` presente y vinculado en ambas páginas | ✅ / ⚠️ / ❌ | ... |
| Tarea 3 — Commit con mensaje exacto | ✅ / ⚠️ / ❌ | ... |
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
| Personalización (token + `<h1>`) | 10 | ... |
| Tarea 1 — `index.html` | 25 | ... |
| Tarea 2 — `acercade.html` | 30 | ... |
| Tarea 3 — `styles.css` y commit | 10 | ... |
| Estructura de archivos | 5 | ... |
| GitHub Pages | 5 | ... |
| Reflexión | 10 | ... |
| **TOTAL** | **100** | **...** |
```

---

## Paso 7 — Consolidado final

Al terminar todas las entregas del laboratorio, generar
`lab2/devoluciones/Lab02-devoluciones-completas.md` con:

1. Tabla resumen al inicio:

```markdown
## Tabla resumen — Lab 2

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
