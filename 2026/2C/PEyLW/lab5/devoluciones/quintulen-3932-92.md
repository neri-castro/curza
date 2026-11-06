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
