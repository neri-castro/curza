# Devolución Lab 5 — Santiago Valentín Apelahnz

## Datos identificatorios

- **Token:** apelahnz-2743-10
- **GitHub Pages:** https://officialsantos.github.io/peylw-2026-practicos-apelahnz-2743-10/
- **Repositorio:** https://github.com/officialsantos/peylw-2026-practicos-apelahnz-2743-10 (rama `main`, commit del TP5: `b2fa833`)
- **Entrega:** commit del 10/11/2026 04:33 — **tardía** (cierre: 06/11/2026 23:00, ~3 días y 5 horas después).

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| `script.js` — creado en la raíz | ✅ | Presente en la raíz del repo. |
| `script.js` — vinculado en `contacto.html` | ✅ | `<script src="script.js"></script>` al final del `<body>` (también en `acercade.html`). |
| `script.js` — sin errores de consola | ✅ | Los bloques están protegidos por `window.location.pathname.includes(...)`; todos los `id` seleccionados existen en el HTML. Sin excepciones al cargar. |
| Interactividad — actualización sin botón | ✅ | Listeners `input`/`change` por campo; no depende de "Cargar" ni de `submit`. |
| Interactividad — Nombre → `resumen-nombre` | ✅ | `input` → `innerText`. |
| Interactividad — Apellido → `resumen-apellido` | ✅ | `input` → `innerText`. |
| Interactividad — Email → `resumen-email` | ✅ | `input` → `innerText`. |
| Interactividad — Teléfono → `resumen-telefono` | ✅ | `input` → `innerText`. |
| Interactividad — Edad → `resumen-edad` | ✅ | `input` → `innerText`. Agrega " (Menor de edad)" y fondo rojo si es < 18: extra no pedido, no afecta la rúbrica. |
| Interactividad — Dirección → `resumen-direccion` | ✅ | `input` → `innerText`. |
| Interactividad — Provincia → `resumen-provincia` | ✅ | `change` sobre el input con `datalist`; se actualiza al elegir opción o perder foco. Compatible con la consigna. |
| Interactividad — CP → `resumen-cp` | ✅ | `input` → `innerText`. |
| Interactividad — Método de Contacto → celda de método | ✅ | La celda real es `resumen-metodo-contacto` (el script usa el id real del HTML). `change` en cada radio; sigue el último cambio. |
| Interactividad — Suscripciones → `resumen-suscripciones` | ✅ | En cada `change` recorre todos los checkboxes y reconstruye la lista; al desmarcar se quita. |
| "Leer más" — botón presente | ✅ | `btn-leer-mas-apelahnz-2743-10` en `acercade.html`. |
| "Leer más" — CV abreviado por defecto | ✅ | `.cv-completo { display: none; }` en `styles.css`; solo se ve la sección "Sobre mí". |
| "Leer más" — revela CV completo al clic | ✅ | El clic muestra `.cv-completo` (Lorem Ipsum) y el botón pasa a "Leer menos"; otro clic lo oculta. |

## Observaciones puntuales

- Verificación en línea: Pages responde 200 en `index`, `contacto.html`, `acercade.html` y `script.js`. El `script.js` publicado es el del HEAD (incluye además el código del TP6); la lógica del TP5 es idéntica a la del commit `b2fa833`. No se probó en navegador real: la verificación de eventos se hizo por lectura de código contra los `id` reales de `contacto.html`.
- `script.js`: los valores de `value` de los radios se vuelcan crudos (`email`, `postal`, `telefono`) en vez de la etiqueta visible ("Correo electrónico", etc.). No es incumplimiento, pero la tabla queda menos legible.
- Los estados iniciales (radio "Correo electrónico" y checkbox "Alertas" marcados por defecto) no se vuelcan a la tabla al cargar; las celdas aparecen vacías hasta que el usuario toca esos controles. Con `checked` en el HTML, la tabla queda inconsistente con el formulario al inicio.
- Entrega fuera de término (10/11 contra cierre 06/11). El reglamento del lab no define penalización por atraso; se registra como tardía sin descuento en el puntaje.
- `<!-- No supe exactamente qué poner -->` en `acercade.html` sobre el CV completo: el relleno Lorem Ipsum es válido según la consigna.

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| `script.js` — creación y vinculación | 15 | 15 |
| Interactividad formulario → tabla | 65 | 65 |
| "Acerca de" — botón "Leer más" | 20 | 20 |
| **TOTAL** | **100** | **100** (entrega tardía) |
