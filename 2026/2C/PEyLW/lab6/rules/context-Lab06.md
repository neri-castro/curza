# Contexto y método de trabajo — Corrección Lab 6: Juego con JavaScript

Este documento describe **cómo ejecutar la corrección paso a paso** para el
Laboratorio 6. Las reglas de fondo (tono, escala, penalizaciones) están en
`AGENTS-Lab06.md` — leer ambos antes de empezar.

Enunciado oficial: `Trabajo Práctico: Juego con JavaScript`. Apertura
21/09/2026 00:00, cierre 21/11/2026 23:00. **Formato avanzado**: la entrega
es la URL de GitHub Pages ya finalizada (no carátula ni reflexión — ver
nota en `AGENTS-Lab06.md`). El enunciado permite usar IA para el desarrollo
completo del juego: no penalizar por eso.

## Estructura de carpetas esperada

```
lab6/
├── rules/
│   ├── AGENTS-Lab06.md               # reglas específicas Lab 6
│   └── context-Lab06.md              # este archivo
├── entregas.md                       # URLs de GitHub Pages entregadas
├── repos-clonados/
│   └── <token-del-alumno>/           # clon local (solo lectura)
└── devoluciones/
    ├── <token-del-alumno>.md                 # devolución individual
    └── Lab06-devoluciones-completas.md       # consolidado con tabla resumen
```

Reutilizar el clon de labs anteriores en `lab5/repos-clonados/<token>/`
haciendo `git pull` dentro de un clon nuevo en
`lab6/repos-clonados/<token>/`, ya que es el mismo repositorio
`peylw-2026-practicos-<token>` extendido con la subpágina/sección del
juego.

---

## Paso 1 — Leer el enunciado

Releer la consigna del Laboratorio 6 antes de corregir cualquier entrega.
Puntos clave a tener frescos:

- Completar y refinar la página personal con todos los elementos
  anteriores (Labs 1-5).
- Crear una subpágina o sección para el juego.
- Desarrollar **uno** de 4 juegos posibles: Adivinanza de Números, Preguntas
  y Respuestas, Memoria con Cartas, o Piedra/Papel/Tijera.
- El juego debe funcionar correctamente y estar bien integrado a la página
  personal.
- Uso de IA para el desarrollo del juego está explícitamente permitido.

---

## Paso 2 — Obtener la URL de la entrega

Igual que en Labs 4 y 5: puede llegar como texto plano con la URL, o como
PDF/DOCX si el alumno reutilizó el formato de carátula.

**Para PDF**:

```python
import fitz
doc = fitz.open("lab6/<carpeta-o-archivo>.pdf")
for page in doc:
    for link in page.get_links():
        print(link.get("uri"))
```

**Para DOCX**:

```python
import zipfile, re

z = zipfile.ZipFile("lab6/<carpeta-o-archivo>.docx")
xml = z.read("word/document.xml").decode("utf-8")
print(re.sub("<[^>]+>", "", xml))

rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
print(rels)
```

Registrar la URL en `lab6/entregas.md`. A partir de la URL de Pages se
infiere el repositorio: `https://<usuario>.github.io/<repo>/` →
`https://github.com/<usuario>/<repo>`.

---

## Paso 3 — Clonar (o actualizar) el repositorio

```bash
git clone <url-del-repo> "lab6/repos-clonados/<token-del-alumno>"
# o, si ya existe el clon de un lab anterior y se reutiliza el mismo repo:
git -C "lab6/repos-clonados/<token-del-alumno>" pull
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

### 4.1 Verificación abreviada de continuidad (Labs 1-5)

No repetir la rúbrica completa de cada lab; alcanza con confirmar
rápidamente:

- `index.html`/`acercade.html`/`contacto.html` siguen con su estructura
  semántica y el `<nav>` funcionando (Lab 2/3).
- El header se ve fijo y hay animación de logo+título en al menos una
  página (Lab 4).
- `script.js` sigue reflejando el formulario en la tabla, y "Leer más"
  sigue funcionando en "Acerca de" (Lab 5).

Si algo dejó de funcionar, anotarlo puntualmente con el archivo y la causa
probable (ej. un `id` cambiado sin actualizar el JS).

### 4.2 Localizar la subpágina/sección del juego

```bash
find . -not -path "./.git*" | sort
```

Buscar un archivo nuevo tipo `juego.html` (o nombre similar), o una nueva
`<section>` dentro de una página existente. Confirmar que usa
`styles.css` y mantiene `<header>`/`<nav>`/`<footer>` consistentes con el
resto del portal.

### 4.3 Identificar el juego elegido y revisar su lógica

Leer el HTML y JS del juego y determinar a cuál de los 4 tipos del
enunciado corresponde. Verificar contra la lista de reglas mínimas de cada
tipo (ver `AGENTS-Lab06.md`, detalle "Juego — reglas según el tipo
elegido"):

- **Adivinanza de Números**: buscar `Math.random()` generando el número
  secreto, un `<input type="number">` o similar para los intentos, y lógica
  de comparación (`if (intento > secreto) ... else if (intento < secreto)`).
- **Preguntas y Respuestas**: buscar un array/objeto con preguntas y
  opciones, lógica de verificación de respuesta correcta, y un contador de
  puntaje.
- **Memoria con Cartas**: buscar un grid de elementos con estado
  oculto/revelado, lógica de comparación de a pares al voltear dos cartas,
  y detección de juego completo.
- **Piedra, Papel o Tijera**: buscar botones/controles para la elección del
  usuario, `Math.random()` para la elección de la computadora, y la lógica
  de las 3 reglas de victoria (piedra > tijera, tijera > papel, papel >
  piedra).

### 4.4 Historial de commits (referencia, no obligatorio)

```bash
git log --oneline --all --stat
```

No hay un mensaje de commit exacto que verificar en este TP. Revisar el
historial solo como referencia para confirmar que el juego llegó
efectivamente al repositorio.

---

## Paso 5 — Verificar en vivo lo publicado

Probar con `WebFetch` la URL de GitHub Pages entregada:

- Respuesta **200**: Pages desplegado correctamente.
- Respuesta **404**: incumplimiento total. No asumir que "estará bien
  después". Registrar como incumplimiento.

Sobre el sitio ya desplegado (no alcanza con leer el código):

- Navegar hasta la subpágina/sección del juego usando el `<nav>` real del
  sitio.
- Jugar una partida completa de principio a fin, según el tipo de juego:
  - Adivinanza: ingresar varios intentos hasta acertar, confirmar las
    pistas mayor/menor.
  - Trivia: responder todas las preguntas, confirmar el puntaje final.
  - Memoria: voltear cartas hasta encontrar todas las parejas.
  - Piedra/Papel/Tijera: jugar varias rondas, incluyendo una que termine en
    empate si es posible.
- Confirmar que existe un botón o mecanismo de "jugar de nuevo" / reinicio
  que no requiere recargar la página manualmente.
- Abrir la consola del navegador y jugar una partida completa observando
  si aparecen errores de JavaScript.

---

## Paso 6 — Redactar la devolución individual

Guardar en `lab6/devoluciones/<token-del-alumno>.md` con el siguiente
formato:

```markdown
# Devolución Lab 6 — [Nombre Completo, si se conoce de labs anteriores]

## Datos identificatorios

- **Token:** [token]
- **GitHub Pages:** [URL]
- **Repositorio:** [URL, inferido de la URL de Pages]
- **Juego elegido:** [Adivinanza de Números / Preguntas y Respuestas / Memoria con Cartas / Piedra, Papel o Tijera]

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Continuidad — página personal completa y refinada | ✅ / ⚠️ / ❌ | ... |
| Subpágina/sección del juego — presente | ✅ / ⚠️ / ❌ | ... |
| Subpágina/sección del juego — diseño consistente con el portal | ✅ / ⚠️ / ❌ | ... |
| Navegación — enlace al juego en todas las páginas | ✅ / ⚠️ / ❌ | ... |
| Juego — reglas básicas correctas | ✅ / ⚠️ / ❌ | ... |
| Juego — casos borde manejados | ✅ / ⚠️ / ❌ | ... |
| Juego — interactividad y manejo de estado | ✅ / ⚠️ / ❌ | ... |
| Juego — feedback claro al usuario | ✅ / ⚠️ / ❌ | ... |
| Juego — reinicio sin recargar la página | ✅ / ⚠️ / ❌ | ... |

## Observaciones puntuales

[Lista concreta de errores o desvíos del enunciado, citando archivo y
sección afectada.]

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Página personal completa y refinada | 20 | ... |
| Subpágina/sección del juego | 15 | ... |
| Navegación al juego | 10 | ... |
| Juego — reglas correctas | 20 | ... |
| Juego — interactividad y estado | 15 | ... |
| Juego — feedback al usuario | 10 | ... |
| Juego — reinicio sin recargar | 10 | ... |
| **TOTAL** | **100** | **...** |
```

---

## Paso 7 — Consolidado final

Al terminar todas las entregas del laboratorio, generar
`lab6/devoluciones/Lab06-devoluciones-completas.md` con:

1. Tabla resumen al inicio (incluir columna de juego elegido):

```markdown
## Tabla resumen — Lab 6

| Token | Nombre | Juego | Nota |
|---|---|---|---|
| perez-4567-89 | Juan Pérez | Piedra, Papel o Tijera | 87 |
| ... | ... | ... | ... |
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
