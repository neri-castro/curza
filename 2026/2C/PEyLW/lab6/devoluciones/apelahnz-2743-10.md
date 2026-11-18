# Devolución Lab 6 — Santiago Valentín Apelahnz

## Datos identificatorios

- **Token:** apelahnz-2743-10
- **GitHub Pages:** https://officialsantos.github.io/peylw-2026-practicos-apelahnz-2743-10/
- **Repositorio:** https://github.com/officialsantos/peylw-2026-practicos-apelahnz-2743-10 (rama `main`, commit `4b91612` del 16/11/2026)
- **Juego elegido:** Piedra, Papel o Tijera

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Continuidad — página personal completa y refinada | ✅ | `index`, `acercade`, `contacto` y `juego` responden 200 y conservan header, nav, footer y botón volver arriba. `script.js` sigue volcando el formulario a la tabla y "Leer más" alterna el CV. |
| Subpágina/sección del juego — presente | ✅ | `juego.html`. |
| Subpágina/sección del juego — diseño consistente con el portal | ✅ | Usa `styles.css`, mismo header, footer y fuente. |
| Navegación — enlace al juego en todas las páginas | ✅ | Enlace "Juegos" en el `<nav>` de las 4 páginas. |
| Juego — reglas básicas correctas | ✅ | Elección del usuario por botones, `Math.random()` para la computadora y las 3 reglas de victoria correctas (probado con elecciones forzadas). |
| Juego — casos borde manejados | ✅ | El empate se detecta y se cuenta aparte. |
| Juego — interactividad y manejo de estado | ✅ | Contadores de ganadas/empatadas/perdidas, racha y récord de racha en `localStorage`. |
| Juego — feedback claro al usuario | ⚠️ | Informa ¡Ganaste!/¡Perdiste!/¡Empate! en cada ronda, pero no muestra qué jugada eligió la computadora. Descuento nulo en la nota; queda como mejora. |
| Juego — reinicio sin recargar la página | ✅ | "Reiniciar" pone a cero contadores y mensaje; conserva el récord guardado. |

## Observaciones puntuales

- Verificación: Pages responde 200 en las 4 páginas y `script.js`. Se simularon con jsdom (sin navegador real) las rondas contra elecciones forzadas de la computadora, el reinicio y los eventos de `contacto.html`/`acercade.html`; sin errores de JavaScript.
- `script.js` — `juego.html`: la pantalla no muestra la jugada de la computadora, solo el resultado; el usuario no puede verificar por qué ganó o perdió.
- `script.js` — `juego.html`: un empate no corta la racha. Es una decisión válida, pero conviene aclararla en la interfaz.
- Heredado del Lab 5, sin descuento: `contacto.html` no vuelca a la tabla el radio y el checkbox marcados por defecto hasta que el usuario los toca.
- Entrega dentro del plazo (último commit 16/11, cierre 21/11).

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
