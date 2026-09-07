# Contexto y método de trabajo — Corrección Lab 4: CSS, Fuentes Web y Posicionamiento

Este documento describe **cómo ejecutar la corrección paso a paso** para el
Laboratorio 4. Las reglas de fondo (tono, escala, penalizaciones) están en
`AGENTS-Lab04.md` — leer ambos antes de empezar.

Enunciado oficial: `Trabajo Práctico: CSS, Fuentes Web y Posicionamiento`.
Apertura 21/09/2026 00:00, cierre 23/10/2026 23:00. **Formato avanzado**:
la entrega es la URL de GitHub Pages ya finalizada (no carátula ni
reflexión — ver nota en `AGENTS-Lab04.md`).

## Estructura de carpetas esperada

```
lab4/
├── rules/
│   ├── AGENTS-Lab04.md               # reglas específicas Lab 4
│   └── context-Lab04.md              # este archivo
├── entregas.md                       # URLs de GitHub Pages entregadas
├── repos-clonados/
│   └── <token-del-alumno>/           # clon local (solo lectura)
└── devoluciones/
    ├── <token-del-alumno>.md                 # devolución individual
    └── Lab04-devoluciones-completas.md       # consolidado con tabla resumen
```

Reutilizar el clon de labs anteriores en
`lab3/repos-clonados/<token>/` (o `lab2/.../<token>/`) haciendo `git pull`
dentro de un clon nuevo en `lab4/repos-clonados/<token>/`, ya que es el
mismo repositorio `peylw-2026-practicos-<token>` extendido con los cambios
de CSS de este TP.

---

## Paso 1 — Leer el enunciado

Releer la consigna del Laboratorio 4 antes de corregir cualquier entrega.
Puntos clave a tener frescos:

- Formatear correctamente tabla y formulario de `contacto.html`.
- Incluir al menos una fuente web.
- Animar el título principal con el logo del CURZA a la derecha: giro
  completo (360°) sobre el eje vertical, terminando en orientación
  correcta.
- Header fijo en la parte superior en **todas** las páginas, visible al
  hacer scroll.
- `acercade.html`: primera línea del texto sticky; `<article>` con
  `max-height: 300px` y barra de desplazamiento si el contenido excede ese
  alto.
- Flecha hacia arriba dentro de un círculo, al final de cada página y
  alineada a la derecha, que vuelve al inicio al hacer clic.

---

## Paso 2 — Obtener la URL de la entrega

El enunciado pide directamente la URL de GitHub Pages ya finalizada. Según
el medio de entrega (campus/formulario/mail), puede llegar como:

- **Texto plano con la URL**: usar directamente.
- **PDF o DOCX** (si el alumno reutilizó el formato de carátula de labs
  anteriores): extraer el href real con las mismas herramientas que en
  labs previos.

**Para PDF** — extraer hrefs reales con `pymupdf`:

```python
import fitz
doc = fitz.open("lab4/<carpeta-o-archivo>.pdf")
for page in doc:
    for link in page.get_links():
        print(link.get("uri"))
```

**Para DOCX**:

```python
import zipfile, re

z = zipfile.ZipFile("lab4/<carpeta-o-archivo>.docx")
xml = z.read("word/document.xml").decode("utf-8")
print(re.sub("<[^>]+>", "", xml))

rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
print(rels)
```

Registrar la URL en `lab4/entregas.md`. A partir de la URL de Pages se
infiere el repositorio: `https://<usuario>.github.io/<repo>/` →
`https://github.com/<usuario>/<repo>`.

---

## Paso 3 — Clonar (o actualizar) el repositorio

```bash
git clone <url-del-repo> "lab4/repos-clonados/<token-del-alumno>"
# o, si ya existe el clon de un lab anterior y se reutiliza el mismo repo:
git -C "lab4/repos-clonados/<token-del-alumno>" pull
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

### 4.1 Revisión de `styles.css` (o CSS adicional)

- Confirmar la existencia de reglas de estilo para `table`, `th`, `td` y
  para los controles del formulario (`input`, `label`, `fieldset`, etc.)
  en `contacto.html`.
- Buscar la importación de la fuente web: `<link>` a Google Fonts (u otro
  servicio) en el `<head>`, o `@font-face` dentro del CSS. Confirmar que el
  `font-family` importado se usa realmente en algún selector aplicado al
  HTML (no solo declarado y sin uso).
- Buscar la animación del logo/título: selector del logo con
  `animation: nombre duración ...` y su `@keyframes` correspondiente
  usando `rotateY(...)`. Verificar que el `@keyframes` termina en `0deg` o
  `360deg` (giro completo, no en `180deg`).
- Buscar las reglas de header fijo: `position: fixed` o `position: sticky`
  con `top: 0` sobre el selector del `<header>`, aplicadas de forma que
  cubran las tres páginas (revisar si `styles.css` es compartido, o si
  cada página tiene su propio bloque de estilos).
- Buscar en `acercade.html`/`styles.css` la regla `position: sticky` sobre
  el elemento que envuelve la primera línea del artículo, y
  `max-height: 300px` + `overflow-y` sobre el `<article>` (o contenedor
  equivalente).
- Buscar el botón "volver arriba": selector con `border-radius: 50%` (o
  equivalente circular), ícono o carácter de flecha hacia arriba,
  posicionado con `position: fixed`/`sticky` + `right`/`bottom`, y su
  mecanismo de scroll-to-top (`href="#top"` con ancla, `onclick`, JS
  `scrollTo`, o `scroll-behavior: smooth` en combinación con un ancla).

### 4.2 Revisión de los tres archivos HTML

- Confirmar que el logo del CURZA está incluido como `<img>` (u otro
  elemento) a la derecha del `<h1>` en el encabezado de cada página.
- Confirmar que el botón/flecha de volver arriba está presente al final
  del `<body>` (o del `<main>`) en las tres páginas.
- Confirmar que la estructura semántica de labs anteriores (`header`,
  `nav`, `main`, `footer`) sigue intacta; este TP es de estilos, no debería
  haber roto la semántica previa.

### 4.3 Historial de commits (referencia, no obligatorio)

```bash
git log --oneline --all --stat
```

No hay un mensaje de commit exacto que verificar en este TP. Revisar el
historial solo como referencia para confirmar que los cambios de CSS
llegaron efectivamente al repositorio y no quedaron solo en local.

---

## Paso 5 — Verificar en vivo lo publicado

Probar con `WebFetch` la URL de GitHub Pages entregada:

- Respuesta **200**: Pages desplegado correctamente.
- Respuesta **404**: incumplimiento total. No asumir que "estará bien
  después". Registrar como incumplimiento.

Sobre el sitio ya desplegado (no alcanza con leer el código):

- Confirmar visualmente que el header queda fijo arriba al scrollear en
  cada una de las tres páginas.
- Confirmar que la animación de giro del logo se ejecuta y termina en
  orientación correcta.
- Confirmar que en `acercade.html` la primera línea del texto queda fija
  mientras se scrollea dentro del artículo, y que aparece la barra de
  desplazamiento al superar los 300px de alto.
- Hacer clic en el botón "volver arriba" en cada página y confirmar que
  vuelve efectivamente al inicio.
- Revisar que la tabla y el formulario de `contacto.html` se vean
  formateados (no con el estilo por defecto del navegador).

---

## Paso 6 — Redactar la devolución individual

Guardar en `lab4/devoluciones/<token-del-alumno>.md` con el siguiente
formato:

```markdown
# Devolución Lab 4 — [Nombre Completo, si se conoce de labs anteriores]

## Datos identificatorios

- **Token:** [token]
- **GitHub Pages:** [URL]
- **Repositorio:** [URL, inferido de la URL de Pages]

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Tabla de `contacto.html` formateada | ✅ / ⚠️ / ❌ | ... |
| Formulario de `contacto.html` formateado | ✅ / ⚠️ / ❌ | ... |
| Fuente web importada y aplicada | ✅ / ⚠️ / ❌ | ... |
| Logo CURZA a la derecha del título | ✅ / ⚠️ / ❌ | ... |
| Animación de giro completo (360°) del logo | ✅ / ⚠️ / ❌ | ... |
| Header fijo en todas las páginas | ✅ / ⚠️ / ❌ | ... |
| "Acerca de" — primera línea sticky | ✅ / ⚠️ / ❌ | ... |
| "Acerca de" — `max-height: 300px` + scroll | ✅ / ⚠️ / ❌ | ... |
| Botón volver arriba — presente en todas las páginas | ✅ / ⚠️ / ❌ | ... |
| Botón volver arriba — estilo círculo + flecha, alineado a la derecha | ✅ / ⚠️ / ❌ | ... |
| Botón volver arriba — funcional | ✅ / ⚠️ / ❌ | ... |

## Observaciones puntuales

[Lista concreta de errores o desvíos del enunciado, citando archivo y
sección cuando corresponda.]

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Tabla `contacto.html` | 15 | ... |
| Formulario `contacto.html` | 15 | ... |
| Fuente web | 10 | ... |
| Animación título + logo | 15 | ... |
| Header fijo | 15 | ... |
| "Acerca de" sticky + scroll | 15 | ... |
| Botón volver arriba | 15 | ... |
| **TOTAL** | **100** | **...** |
```

---

## Paso 7 — Consolidado final

Al terminar todas las entregas del laboratorio, generar
`lab4/devoluciones/Lab04-devoluciones-completas.md` con:

1. Tabla resumen al inicio:

```markdown
## Tabla resumen — Lab 4

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
