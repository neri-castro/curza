# Lab 5 — Devoluciones completas

## Tabla resumen — Lab 5

| Token | Nombre | Nota |
|---|---|---|
| bastias-1018-59 | Marité Bastías | 100 |
| boisselier-8339-91 | Sara Celeste Boisselier | 100 |
| camandulle-5746-93 | Fernanda Camandulle | 100 |
| chavarria-7037-55 | Javier Chavarria | 100 |
| klug-3903-68 | Robertino Klug | 81 |
| pereyra-1554-84 | Sofia Pereyra | 100 |
| quintulen-3932-92 | Carlos Quintulen | 82 |
| reyes-6775-42 | Isaías Reyes Arzamendia | 100 |
| reynoso-4260-07 | Ramiro Reynoso | 100 |
| tiradomoreira-5676-19 | Carla Tirado Moreira | 100 |
| vela-9972-35 | Sandra Vela | 100 |

---

# Devolución Lab 5 — Marité Bastías

## Datos identificatorios

- **Token:** bastias-1018-59
- **GitHub Pages:** https://marite28.github.io/peylw-2026-practicos-bastias-1018-59/
- **Repositorio:** https://github.com/Marite28/peylw-2026-practicos-bastias-1018-59 (rama `master` (merge de `laboratorio_5`))

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-bastias-1018-59` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- Entrega con fecha 03/11/2026, dentro del plazo (cierre 06/11).
- Sin observaciones sobre el comportamiento. `script.js` usa `innerText` (preferible `textContent`, no se penaliza).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Sara Celeste Boisselier

## Datos identificatorios

- **Token:** boisselier-8339-91
- **GitHub Pages:** https://saraboisselier.github.io/peylw-2026-practicos-boisselier-8339-91/
- **Repositorio:** https://github.com/SaraBoisselier/peylw-2026-practicos-boisselier-8339-91 (rama `lab5`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-boisselier-8339-91` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- El bloque oculto usa la clase `.biografia` (no `.cv-completo`); es coherente entre HTML, CSS y JS, no se penaliza.
- Sin observaciones sobre el comportamiento.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Fernanda Camandulle

## Datos identificatorios

- **Token:** camandulle-5746-93
- **GitHub Pages:** https://camandulle.github.io/peylw-2026-practicos-camandulle-5746-93/
- **Repositorio:** https://github.com/Camandulle/peylw-2026-practicos-camandulle-5746-93 (rama `main`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-camandulle-5746-93` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- `provincia` se refleja con `change` (al elegir/salir del campo), compatible con la consigna.
- La versión "abreviada" visible por defecto es larga (dos secciones); el bloque oculto agrega "Mi recorrido completo". Cumple.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Javier Chavarria

## Datos identificatorios

- **Token:** chavarria-7037-55
- **GitHub Pages:** https://javi-jav.github.io/peylw-2026-practicos-chavarria-7037-55/
- **Repositorio:** https://github.com/javi-jav/peylw-2026-practicos-chavarria-7037-55 (rama `main`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-chavarria-7037-55` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- Sin observaciones. Agrega `aria-expanded` al botón, no exigido.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Robertino Klug

## Datos identificatorios

- **Token:** klug-3903-68
- **GitHub Pages:** https://robertino512.github.io/peylw-2026-practicos-klug-3903-68/ (no informada por el alumno; inferida del usuario de GitHub)
- **Repositorio:** https://github.com/Robertino512/peylw-2026-practicos-klug-3903-68 (rama `lab5`, la informada)

## Criterio de esta corrección

La nota se calcula sobre el código de la rama `lab5`, sin tener en cuenta GitHub Pages. Dato informativo, no computado: Pages sirve la rama `lab2-lab3` (sin `script.js`, 404), por lo que el trabajo de este TP no es visible en el link publicado. Conviene apuntar Settings → Pages → Source a `lab5`.

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz de `lab5`. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `Contacto.html` y `acercade.html`. |
| `script.js` — sin errores de consola | ❌ | `Uncaught TypeError: suscripcionInteres.addEventListener is not a function` al cargar `Contacto.html`: `querySelectorAll` devuelve una NodeList. |
| Interactividad — actualización sin botón | ✅ | Eventos `input`/`change` por campo, sin depender de "Cargar". |
| Interactividad — Nombre → `resumen-nombre` | ✅ | `input`. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | `input`. |
| Interactividad — Email → celda de email | ✅ | Usa el id real del HTML (`resumen-correo electronico`, con espacio; no coincide con el nombre esperado `resumen-email`, pero script y HTML son coherentes). |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | `input`. |
| Interactividad — Edad → `resumen-edad` | ✅ | `input`; marca menores de 18. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | `input`. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | `change`. |
| Interactividad — CP → celda de CP | ✅ | Ids reales con espacios (`codigo postal` / `resumen-codigo Postal`); coherentes. |
| Interactividad — Método de Contacto → celda de método | ❌ | `addEventListener` sobre una NodeList (los radios no se enganchan) y el id de la celda tiene una comilla de más (`'resumen-metodo de contacto preferido"'`), por lo que el elemento es `null`. Además el `TypeError` anterior corta el script antes de llegar acá. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ❌ | Mismo `TypeError` de NodeList; además usa `.value` sobre la colección y no recalcula los marcados. La celda nunca se actualiza. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-klug-3903-68` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | `.cv-completo` con `display: none`. |
| "Leer más" — revela CV completo al clic | ⚠️ | El primer clic no hace nada: el `if` compara `style.display === "none"` y el valor inline inicial es `""`, entra por la rama de ocultar y deja el botón en "Leer más". Recién el segundo clic revela el CV. |

## Observaciones puntuales

- `script.js`: para radios y checkboxes usar `querySelectorAll(...).forEach(el => el.addEventListener("change", ...))`; para suscripciones recalcular la lista con `:checked` en cada cambio.
- `script.js`: corregir el id de la celda de método (comilla final de más) y preferir nombres sin espacios (`resumen-metodo`).
- `script.js`: para el botón, preguntar por `=== "block"` para ocultar o usar `getComputedStyle`, así el primer clic revela el CV.
- Verificación: se simularon (jsdom) los eventos de cada campo sobre la rama `lab5`; los 8 campos de texto se reflejan, radios y suscripciones no, y se reproduce el `TypeError`. "Leer más" se evaluó por lectura del código.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 10 |
| Interactividad formulario → tabla | 65 | 55 |
| "Acerca de" — botón "Leer más" | 20 | 16 |
| **TOTAL** | **100** | **81** |

Desglose: interactividad = mecanismo 15 + 8 campos × 5 (40) + método 0 + suscripciones 0; "Leer más" = 5 + 5 + 6/10.

---

# Devolución Lab 5 — Sofia Pereyra

## Datos identificatorios

- **Token:** pereyra-1554-84
- **GitHub Pages:** https://sofiaquino567-bot.github.io/peylw-2026-practicos-pereyra-1554-84/
- **Repositorio:** https://github.com/sofiaquino567-bot/peylw-2026-practicos-pereyra-1554-84 (rama `Laboratorio5`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-pereyra-1554-84` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- `acercade.html`: hay un `</p>` sobrante tras el párrafo de biografía (HTML inválido, sin efecto visible).
- IDs de los campos con mayúscula/acento (`Nombre`, `Dirección`) y sin `id` en radios/checkboxes; `script.js` los resuelve igual y funciona.
- El último commit ("Agrego los enlaces solicitados") no modifica la funcionalidad.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Carlos Quintulen

## Datos identificatorios

- **Token:** quintulen-3932-92
- **GitHub Pages:** https://caarlosq.github.io/peylw-2026-practicos-quintulen-3932-92/
- **Repositorio:** https://github.com/CaarlosQ/peylw-2026-practicos-quintulen-3932-92 (rama `laboratorio_5`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` y `acercade.html`. |
| `script.js` — sin errores de consola | ✅ | Sin excepciones al cargar ni al interactuar. |
| Interactividad — actualización sin botón | ❌ | Las suscripciones solo se actualizan al hacer clic en "Cargar" (`script.js`, último listener, sobre `#btn-cargar-quintulen-3932-92`). Rige el criterio: un campo que actualiza solo con el botón anula este sub-ítem. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Con `change` (al salir del campo); admitido. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | `input`. |
| Interactividad — Email → `resumen-email` | ✅ | `input`. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | `input`. |
| Interactividad — Edad → `resumen-edad` | ✅ | `input`. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | `input`. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | `input`. |
| Interactividad — CP → `resumen-cp` | ✅ | `input`. |
| Interactividad — Método de Contacto → `resumen-metodo` | ✅ | Listener `change` en cada radio; se actualiza en cambios sucesivos. La opción marcada por defecto (Email) no se vuelca al cargar: la celda queda vacía hasta que se cambie de opción. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ⚠️ | La celda (`id="celdaSuscripciones"`, no sigue el nombre `resumen-suscripciones`) muestra la lista correcta, pero solo después de pulsar "Cargar", no al marcar/desmarcar. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-quintulen-3932-92` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | `.cv-completo` con `display: none`; se ve la biografía corta. |
| "Leer más" — revela CV completo al clic | ✅ | Alterna con `getComputedStyle`; funciona desde el primer clic. |

## Observaciones puntuales

- `script.js`: el listener de suscripciones debe colgarse de `change` en los checkboxes (`input[name="suscripcion[]"]`) y no del botón. Es la causa de la pérdida de los 15 puntos del mecanismo y de parte del ítem de suscripciones.
- `contacto.html`: el id de la tabla de resumen es `setDatos` y el de la celda de suscripciones `celdaSuscripciones`; el resto de los ids `resumen-*` son los esperados.
- Verificación: Pages responde 200 y el contenido servido es idéntico a la rama `laboratorio_5`. Se simularon (jsdom) los eventos de campos, radios y checkboxes; el botón "Cargar" es el único disparador de las suscripciones.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 47 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **82** |

Desglose de interactividad: mecanismo 0/15; nombre a CP 8 × 5 = 40; método 5; suscripciones 2/5.

---

# Devolución Lab 5 — Isaías Reyes Arzamendia

## Datos identificatorios

- **Token:** reyes-6775-42
- **GitHub Pages:** https://isaiasreyesbjj16-ux.github.io/peylw-2026-practicos-reyes-6775-42/
- **Repositorio:** https://github.com/isaiasreyesbjj16-ux/peylw-2026-practicos-reyes-6775-42 (rama `main`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-reyes-6775-42` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- Sin observaciones sobre el comportamiento. `provincia` con `change`, compatible con la consigna.
- El repo conserva archivos sueltos heredados (`images (2).jfif`, `config_git.png`, `laboratorio1/`); no son parte de la rúbrica.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Ramiro Reynoso

## Datos identificatorios

- **Token:** reynoso-4260-07
- **GitHub Pages:** https://ramireybas.github.io/peylw-2026-practicos-reynoso-4260-07/
- **Repositorio:** https://github.com/Ramireybas/peylw-2026-practicos-reynoso-4260-07 (rama `main`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-reynoso-4260-07` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- Entrega con fecha 30/10/2026, dentro del plazo.
- Sin observaciones sobre el comportamiento. Todo envuelto en `DOMContentLoaded`.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Carla Tirado Moreira

## Datos identificatorios

- **Token:** tiradomoreira-5676-19
- **GitHub Pages:** https://carlatmoreira98.github.io/peylw-2026-practicos-tiradomoreira-5676-19/
- **Repositorio:** https://github.com/carlatmoreira98/peylw-2026-practicos-tiradomoreira-5676-19 (rama `main`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-tiradomoreira-5676-19` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- Sin observaciones sobre el comportamiento.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |

---

# Devolución Lab 5 — Sandra Vela

## Datos identificatorios

- **Token:** vela-9972-35
- **GitHub Pages:** https://shalom198424.github.io/peylw-2026-practicos-vela-9972-35/
- **Repositorio:** https://github.com/Shalom198424/peylw-2026-practicos-vela-9972-35 (rama `laboratorio5`)

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js">` en `contacto.html` (y en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Carga sin excepciones en `contacto.html` ni `acercade.html`. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Email → `resumen-email` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Edad → `resumen-edad` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — CP → `resumen-cp` | ✅ | Se refleja en la celda al completar el campo. |
| Interactividad — Método de Contacto → celda de método | ✅ | Cambia al seleccionar cada radio, también en cambios sucesivos. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | Recalcula la lista completa de marcados en cada `change`; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-vela-9972-35` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | Bloque extendido oculto por CSS (`display: none`); se ve solo la versión corta. |
| "Leer más" — revela CV completo al clic | ✅ | El primer clic muestra el bloque y el botón pasa a "Leer menos"; el segundo lo oculta. |

## Observaciones puntuales

- Verificación: Pages responde 200 en `index`, `contacto`, `acercade`, `script.js` y `styles.css`, y el contenido servido es idéntico al de la rama revisada. Se simularon (jsdom, sin navegador real) los eventos de cada campo, los radios y los checkboxes y se contrastó la celda de resumen; sin errores de JavaScript.
- `provincia` con `change` y valores iniciales (Correo electrónico / Alertas) volcados al cargar: correcto.
- Sin observaciones adicionales.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** |
