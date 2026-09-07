# Contexto y método de trabajo — Corrección Lab 5: JavaScript

Este documento describe **cómo ejecutar la corrección paso a paso** para el
Laboratorio 5. Las reglas de fondo (tono, escala, penalizaciones) están en
`AGENTS-Lab05.md` — leer ambos antes de empezar.

Enunciado oficial: `Trabajo Práctico: JavaScript`. Apertura 21/09/2026
00:00, cierre 06/11/2026 23:00. **Formato avanzado**: la entrega es la URL
de GitHub Pages ya finalizada (no carátula ni reflexión — ver nota en
`AGENTS-Lab05.md`).

## Estructura de carpetas esperada

```
lab5/
├── rules/
│   ├── AGENTS-Lab05.md               # reglas específicas Lab 5
│   └── context-Lab05.md              # este archivo
├── entregas.md                       # URLs de GitHub Pages entregadas
├── repos-clonados/
│   └── <token-del-alumno>/           # clon local (solo lectura)
└── devoluciones/
    ├── <token-del-alumno>.md                 # devolución individual
    └── Lab05-devoluciones-completas.md       # consolidado con tabla resumen
```

Reutilizar el clon de labs anteriores en `lab4/repos-clonados/<token>/`
haciendo `git pull` dentro de un clon nuevo en
`lab5/repos-clonados/<token>/`, ya que es el mismo repositorio
`peylw-2026-practicos-<token>` extendido con `script.js`.

---

## Paso 1 — Leer el enunciado

Releer la consigna del Laboratorio 5 antes de corregir cualquier entrega.
Puntos clave a tener frescos:

- Crear `script.js` y vincularlo al HTML del formulario (`contacto.html`).
- Todo lo cargado en el formulario debe reflejarse en la tabla inferior al
  terminar de rellenar cada campo, **sin botones**.
- En `acercade.html`, botón "Leer más": CV abreviado por defecto, CV
  completo al hacer clic (Lorem Ipsum aceptable como relleno).

---

## Paso 2 — Obtener la URL de la entrega

Igual que en Lab 4: puede llegar como texto plano con la URL, o como
PDF/DOCX si el alumno reutilizó el formato de carátula.

**Para PDF**:

```python
import fitz
doc = fitz.open("lab5/<carpeta-o-archivo>.pdf")
for page in doc:
    for link in page.get_links():
        print(link.get("uri"))
```

**Para DOCX**:

```python
import zipfile, re

z = zipfile.ZipFile("lab5/<carpeta-o-archivo>.docx")
xml = z.read("word/document.xml").decode("utf-8")
print(re.sub("<[^>]+>", "", xml))

rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
print(rels)
```

Registrar la URL en `lab5/entregas.md`. A partir de la URL de Pages se
infiere el repositorio: `https://<usuario>.github.io/<repo>/` →
`https://github.com/<usuario>/<repo>`.

---

## Paso 3 — Clonar (o actualizar) el repositorio

```bash
git clone <url-del-repo> "lab5/repos-clonados/<token-del-alumno>"
# o, si ya existe el clon de un lab anterior y se reutiliza el mismo repo:
git -C "lab5/repos-clonados/<token-del-alumno>" pull
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

### 4.1 Revisión de `script.js`

- Confirmar que el archivo existe en la raíz del repositorio.
- Confirmar que `contacto.html` lo vincula con
  `<script src="script.js"></script>` (idealmente con `defer`, o ubicado
  al final del `<body>` para asegurar que el DOM ya está cargado).
- Identificar los `id` reales de los campos del formulario en
  `contacto.html` y compararlos contra lo que `script.js` selecciona
  (`document.getElementById`, `querySelector`, etc.). Si el alumno cambió
  algún `id` respecto al de Lab 3, usar el `id` real presente en el HTML,
  no el del enunciado de Lab 3.
- Verificar que los listeners están en eventos que no dependen de un botón
  ni del `submit` del formulario: `input`, `change`, `blur`, `keyup`, etc.
  sobre cada campo individual (no un único listener en el botón "Cargar").
- Confirmar que existe un listener específico para los radios de "Método
  de Contacto" (evento `change` sobre el grupo, o sobre cada radio) y para
  los checkboxes de "Suscripción de Interés" (que recalcula la lista
  completa de marcados en cada cambio, no solo agrega sin quitar).
- Confirmar que las celdas `resumen-*` (ver lista en `AGENTS-Lab05.md`) se
  actualizan con `textContent` o `innerText` (no hace falta que sea
  `innerHTML`, y de hecho `textContent` es preferible).

### 4.2 Revisión de `acercade.html` — "Leer más"

- Confirmar que existe un botón con texto "Leer más" (o equivalente
  cercano) y un bloque de contenido con el CV/currículum.
- Confirmar que por defecto solo se ve una versión abreviada (ej. mediante
  `display: none` sobre el bloque extendido, o mediante un `max-height`
  chico + `overflow: hidden`, o el contenido extendido directamente
  ausente del DOM hasta el clic).
- Confirmar en `script.js` el listener de clic sobre el botón que revela el
  contenido completo (cambio de clase, `style.display`, `classList.toggle`,
  etc.).
- Si el contenido extendido es Lorem Ipsum, no penalizar — el enunciado lo
  habilita explícitamente como relleno aceptable.

### 4.3 Historial de commits (referencia, no obligatorio)

```bash
git log --oneline --all --stat
```

No hay un mensaje de commit exacto que verificar en este TP. Revisar el
historial solo como referencia para confirmar que `script.js` y sus
cambios asociados llegaron efectivamente al repositorio.

---

## Paso 5 — Verificar en vivo lo publicado

Probar con `WebFetch` la URL de GitHub Pages entregada:

- Respuesta **200**: Pages desplegado correctamente.
- Respuesta **404**: incumplimiento total. No asumir que "estará bien
  después". Registrar como incumplimiento.

Sobre el sitio ya desplegado (no alcanza con leer el código):

- Completar cada campo de `contacto.html` uno por uno y confirmar que la
  tabla de resumen se actualiza sola, sin hacer clic en "Cargar".
- Cambiar la opción seleccionada de "Método de Contacto" más de una vez y
  confirmar que la celda `resumen-metodo` sigue el último cambio.
- Marcar y desmarcar varios checkboxes de "Suscripción de Interés" y
  confirmar que `resumen-suscripciones` refleja exactamente el conjunto
  marcado en cada momento (no acumula valores desmarcados).
- Abrir la consola del navegador y revisar si aparecen errores de
  JavaScript al cargar la página o al interactuar con el formulario.
- En `acercade.html`, hacer clic en "Leer más" y confirmar que aparece
  contenido adicional del currículum que no estaba visible antes.

---

## Paso 6 — Redactar la devolución individual

Guardar en `lab5/devoluciones/<token-del-alumno>.md` con el siguiente
formato:

```markdown
# Devolución Lab 5 — [Nombre Completo, si se conoce de labs anteriores]

## Datos identificatorios

- **Token:** [token]
- **GitHub Pages:** [URL]
- **Repositorio:** [URL, inferido de la URL de Pages]

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ / ⚠️ / ❌ | ... |
| `script.js` — vinculado en `contacto.html` | ✅ / ⚠️ / ❌ | ... |
| `script.js` — sin errores de consola | ✅ / ⚠️ / ❌ | ... |
| Interactividad — actualización sin botón | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Nombre → `resumen-nombre` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Apellido → `resumen-apellido` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Email → `resumen-email` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Teléfono → `resumen-telefono` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Edad → `resumen-edad` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Dirección → `resumen-direccion` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Provincia → `resumen-provincia` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — CP → `resumen-cp` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Método de Contacto → `resumen-metodo` | ✅ / ⚠️ / ❌ | ... |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ / ⚠️ / ❌ | ... |
| "Leer más" — botón presente | ✅ / ⚠️ / ❌ | ... |
| "Leer más" — CV abreviado por defecto | ✅ / ⚠️ / ❌ | ... |
| "Leer más" — revela CV completo al clic | ✅ / ⚠️ / ❌ | ... |

## Observaciones puntuales

[Lista concreta de errores o desvíos del enunciado, citando archivo y
sección afectada.]

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | ... |
| Interactividad formulario → tabla | 65 | ... |
| "Acerca de" — botón "Leer más" | 20 | ... |
| **TOTAL** | **100** | **...** |
```

---

## Paso 7 — Consolidado final

Al terminar todas las entregas del laboratorio, generar
`lab5/devoluciones/Lab05-devoluciones-completas.md` con:

1. Tabla resumen al inicio:

```markdown
## Tabla resumen — Lab 5

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
