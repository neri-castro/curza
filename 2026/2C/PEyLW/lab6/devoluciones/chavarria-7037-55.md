# Devolución Lab 6 — Javier Chavarria

## Datos identificatorios

- **Token:** chavarria-7037-55
- **GitHub Pages:** https://javi-jav.github.io/peylw-2026-practicos-chavarria-7037-55/
- **Repositorio:** https://github.com/javi-jav/peylw-2026-practicos-chavarria-7037-55 (rama `main`, commit `2943259` del 16/11/2026)
- **Juego elegido:** Memoria con Cartas

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Continuidad — página personal completa y refinada | ✅ | Las 4 páginas responden 200; header, nav, footer, fuente web y botón volver arriba presentes. El formulario de `contacto.html` vuelca los 10 campos a la tabla (incluidos radios y checkboxes con recálculo) y "Leer más" alterna el CV. |
| Subpágina/sección del juego — presente | ✅ | `juego.html`. |
| Subpágina/sección del juego — diseño consistente con el portal | ✅ | Mismo header con logo, nav, footer y `styles.css`. |
| Navegación — enlace al juego en todas las páginas | ✅ | Enlace "Juego" en el `<nav>` de las 4 páginas. |
| Juego — reglas básicas correctas | ✅ | Grid de 16 cartas boca abajo, volteo por clic, comparación de pares y detección de los 8 pares (partida completa simulada). |
| Juego — casos borde manejados | ✅ | Bloqueo del tablero mientras se comparan dos cartas, la misma carta no cuenta dos veces, las parejas encontradas se deshabilitan y el reinicio cancela el `setTimeout` pendiente. |
| Juego — interactividad y manejo de estado | ✅ | Estado encapsulado en una IIFE, intentos y puntos, récord en `localStorage` con `try/catch`. |
| Juego — feedback claro al usuario | ✅ | Mensaje por cada acción (par encontrado, no coinciden, ganaste con N intentos) y contadores visibles. |
| Juego — reinicio sin recargar la página | ✅ | "Nueva partida" remezcla el tablero y pone a cero los contadores. |

## Observaciones puntuales

- Verificación: Pages responde 200 en las 4 páginas y `script.js`. Partida completa, reinicio, doble clic sobre la misma carta y los eventos de `contacto.html`/`acercade.html` simulados con jsdom (sin navegador real); sin errores de JavaScript.
- La celda del método de contacto es `resumen-metodo-contacto` (id real del HTML) y el script la usa correctamente.
- Sin observaciones adicionales. Entrega dentro del plazo (último commit 16/11, cierre 21/11).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Página personal completa y refinada | 20 | 20 |
| Subpágina/sección del juego | 15 | 15 |
| Navegación al juego | 10 | 10 |
| Juego — reglas correctas | 20 | 20 |
| Juego — interactividad y estado | 15 | 15 |
| Juego — feedback al usuario | 10 | 10 |
| Juego — reinicio sin recargar | 10 | 10 |
| **TOTAL** | **100** | **100** |
