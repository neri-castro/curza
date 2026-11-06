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
