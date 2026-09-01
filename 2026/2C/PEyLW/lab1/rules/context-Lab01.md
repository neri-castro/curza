# Contexto y método de trabajo — Corrección Lab 1: Configuración de Entorno y Control de Versiones

Este documento describe **cómo ejecutar la corrección paso a paso** para el
Laboratorio 1. Las reglas de fondo (tono, escala, penalizaciones) están en
`AGENTS-Lab01.md` — leer ambos antes de empezar.

## Estructura de carpetas esperada

```
Laboratorios/
├── AGENTS.md                         # reglas generales
├── AGENTS-Lab01.md                   # reglas específicas Lab 1
├── context-Lab01.md                  # este archivo
├── Lab01/
│   ├── Lab01.md                      # enunciado oficial del laboratorio
│   ├── Alumnos/
│   │   └── <Nombre>_<id>_assignsubmission_file/
│   │       └── <archivo>.pdf | .docx    # carátula con link al repo
│   ├── repos-clonados/
│   │   └── <token-del-alumno>/       # clon local (solo lectura)
│   └── devoluciones/
│       ├── <token-del-alumno>.md             # devolución individual
│       └── Lab01-devoluciones-completas.md   # consolidado con tabla resumen
```

---

## Paso 1 — Leer el enunciado

Abrir `Lab01/Lab01.md` antes de corregir cualquier entrega. La rúbrica real,
el mensaje de commit exacto, los nombres de archivo y la estructura de
entregables salen de ahí. No corregir de memoria.

---

## Paso 2 — Extraer el enlace al repositorio de cada entrega

El archivo entregado por el alumno es un PDF o DOCX con la carátula. El
texto visible de un hipervínculo puede no coincidir con el `href` real.

**Para PDF** — extraer hrefs reales con `pymupdf`:

```python
import fitz
doc = fitz.open("Laboratorios/Lab01/Alumnos/<carpeta>/<archivo>.pdf")
for page in doc:
    for link in page.get_links():
        print(link.get("uri"))
```

**Para DOCX** — extraer texto plano y, si hace falta, los hrefs de relaciones:

```python
import zipfile, re

# Texto plano
z = zipfile.ZipFile("Laboratorios/Lab01/Alumnos/<carpeta>/<archivo>.docx")
xml = z.read("word/document.xml").decode("utf-8")
print(re.sub("<[^>]+>", "", xml))

# Hrefs reales de hipervínculos
rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
print(rels)
```

Registrar siempre los dos enlaces obtenidos (repositorio GitHub y GitHub
Pages). Si el alumno solo entregó uno de los dos, anotarlo como observación.

---

## Paso 3 — Clonar el repositorio

```bash
git clone <url-del-repo> "Laboratorios/Lab01/repos-clonados/<token-del-alumno>"
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
├── index.html
├── README.md
├── capturas/
│   └── config_git.png
└── REFLEXION.md
```

Anotar archivos faltantes, archivos fuera de lugar o carpetas que deberían
ser archivos. La carpeta `capturas/` debe existir como directorio, no como
archivo.

### 4.2 Historial de commits

```bash
git log --oneline --all --stat
```

Verificar:

- Que exista un commit con el mensaje exacto:
  `Commit inicial: Configurando el index con mi token unico`
- Que ese commit incluya al menos `index.html`.
- Si hay commits adicionales (subidas posteriores de README, REFLEXION, etc.),
  no penalizar por su existencia; el mensaje del commit de entrega es el
  que se evalúa.

### 4.3 Revisión de `index.html`

Leer el archivo y verificar ítem por ítem:

- Estructura HTML básica presente (no necesariamente HTML5 completo, el
  enunciado solo pide "básico").
- `<h1>` con el nombre completo del alumno visible.
- Comentario HTML con el token único en el formato indicado:
  `<!-- TOKEN-ALUMNO: <token> -->` o equivalente semántico.
- El archivo no puede estar vacío ni contener solo el esqueleto sin contenido.

### 4.4 Revisión de `capturas/config_git.png`

```bash
file capturas/config_git.png
```

Confirmar que:

- El archivo existe en la subcarpeta `capturas/`.
- Es un archivo de imagen válido (PNG, JPG u otro formato de imagen; el
  enunciado dice `.png` pero no penalizar si es JPG).
- Si el archivo está corrupto o tiene 0 bytes: ❌.
- El contenido de la captura debe mostrar la salida de `git config --list`
  con al menos `user.name` y `user.email` configurados. Si la imagen es
  ilegible por resolución, anotar como observación pero no penalizar si el
  archivo es válido.

### 4.5 Revisión de `README.md`

Verificar que la carátula incluya todos los campos del enunciado:

- Nombre y apellido
- Legajo / Matrícula
- Últimos 4 dígitos del DNI
- Fecha de entrega
- Enlace al repositorio de GitHub

Si algún campo tiene `[Completar]` sin reemplazar: ⚠️ parcial, descontar
proporcionalmente dentro del ítem de README.

### 4.6 Revisión de `REFLEXION.md`

Leer las tres respuestas y evaluar:

**Pregunta 1 — Token único:**
- Verificar que el token declarado coincide con el nombre del repositorio
  y con el comentario HTML en `index.html`.
- Si el token declarado no coincide con ninguno de los dos: ❌.
- Si coincide con uno pero no con el otro: ⚠️ parcial.

**Pregunta 2 — Salida de `git status`:**
- Debe ser texto literal copiado de la terminal, no una descripción.
- Salidas esperadas típicas incluyen líneas como `Untracked files:`,
  `Changes to be committed:` o `On branch main/master`.
- Si el alumno describe con palabras lo que vio en lugar de pegar la
  salida literal: ⚠️ parcial (máximo 1 punto de 3).
- Si la salida pegada no corresponde a un estado previo al primer commit
  (por ejemplo, muestra `nothing to commit`): ⚠️ parcial, anotar.

**Pregunta 3 — Staging area vs working directory:**
- Debe explicar con sus palabras que el working directory es donde se
  editan los archivos localmente, y la staging area es la zona intermedia
  donde se preparan los cambios antes de hacer commit.
- Mención de `git add` como la operación que mueve cambios al staging: positivo.
- Respuesta de una línea sin distinción clara: ⚠️ parcial.
- Respuesta copiada textualmente de internet sin adaptación: ⚠️ parcial.

---

## Paso 5 — Verificar en vivo lo publicado

### 5.1 Repositorio GitHub

Visitar `https://github.com/<usuario>/peylw-2026-practicos-<token>` y
confirmar que el repo es público y la rama principal tiene los archivos
esperados.

### 5.2 GitHub Pages

Probar con `WebFetch` la URL:
`https://<usuario>.github.io/peylw-2026-practicos-<token>/`

- Respuesta **200**: Pages desplegado correctamente.
- Respuesta **404**: incumplimiento total del ítem Pages. No asumir que
  "estará bien después". Registrar como incumplimiento.

Si el nombre del repo difiere del esperado, ajustar la URL de Pages en
consecuencia y anotar la discrepancia.

---

## Paso 6 — Redactar la devolución individual

Guardar en `Laboratorios/Lab01/devoluciones/<token-del-alumno>.md` con el
siguiente formato:

```markdown
# Devolución Lab 1 — [Nombre Completo]

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
| Tarea 1 — Captura `config_git.png` presente | ✅ / ⚠️ / ❌ | ... |
| Tarea 1 — Captura muestra `user.name` y `user.email` | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Nombre del repo con formato correcto | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — `index.html` con `<h1>` y token en comentario | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Commit con mensaje exacto | ✅ / ⚠️ / ❌ | ... |
| Tarea 2 — Repositorio público | ✅ / ⚠️ / ❌ | ... |
| Tarea 3 — GitHub Pages configurado y respondiendo 200 | ✅ / ⚠️ / ❌ | ... |
| Estructura de archivos correcta | ✅ / ⚠️ / ❌ | ... |
| Reflexión — 3 preguntas respondidas | ✅ / ⚠️ / ❌ | ... |

## Observaciones puntuales

[Lista concreta de errores, archivos faltantes o desvíos del enunciado,
citando archivo y sección cuando corresponda.]

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| README / carátula | 5 | ... |
| Tarea 1 — captura presente | 10 | ... |
| Tarea 1 — captura con contenido correcto | 10 | ... |
| Tarea 2 — nombre del repo | 5 | ... |
| Tarea 2 — `index.html` correcto | 10 | ... |
| Tarea 2 — comentario con token | 5 | ... |
| Tarea 2 — mensaje de commit exacto | 10 | ... |
| Tarea 2 — repo público | 5 | ... |
| Tarea 3 — GitHub Pages | 10 | ... |
| Estructura de archivos | 10 | ... |
| Reflexión | 10 | ... |
| **TOTAL** | **100** | **...** |
```

---

## Paso 7 — Consolidado final

Al terminar todas las entregas del laboratorio, generar
`Laboratorios/Lab01/devoluciones/Lab01-devoluciones-completas.md` con:

1. Tabla resumen al inicio:

```markdown
## Tabla resumen — Lab 1

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
