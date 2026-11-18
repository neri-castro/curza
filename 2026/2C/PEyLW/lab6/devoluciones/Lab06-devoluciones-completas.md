# Lab 6 — Devoluciones completas

## Tabla resumen — Lab 6

| Token | Nombre | Juego | Nota |
|---|---|---|---|
| apelahnz-2743-10 | Santiago Valentín Apelahnz | Piedra, Papel o Tijera | 100 |
| chavarria-7037-55 | Javier Chavarria | Memoria con Cartas | 100 |
| klug-3903-68 | Robertino Klug | Adivinanza de Números | 85 |
| reyes-6775-42 | Isaías Reyes Arzamendia | Memoria con Cartas | 100 |

---

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

---

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

---

# Devolución Lab 6 — Robertino Klug

## Datos identificatorios

- **Token:** klug-3903-68
- **GitHub Pages:** https://robertino512.github.io/peylw-2026-practicos-klug-3903-68/
- **Repositorio:** https://github.com/Robertino512/peylw-2026-practicos-klug-3903-68 (Pages sirve la rama `publicacion`, que incluye el TP6, merge del 17/11/2026; `main` solo tiene el commit inicial)
- **Juego elegido:** Adivinanza de Números

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Continuidad — página personal completa y refinada | ❌ | `contacto.html`: el formulario ya no actualiza la tabla (ver observaciones). Además, `script.js` lanza un error de consola en `acercade.html`. El resto de las páginas, la navegación y "Leer más" siguen presentes. |
| Subpágina/sección del juego — presente | ✅ | `juego.html`. |
| Subpágina/sección del juego — diseño consistente con el portal | ✅ | Usa `styles.css`, misma nav y mismo footer. El header no lleva la clase `header` del resto de páginas y falta el botón volver arriba. |
| Navegación — enlace al juego en todas las páginas | ✅ | Enlace "Juego" en el `<nav>` de las 4 páginas (el archivo del formulario se llama `Contacto.html`, con mayúscula, y el enlace coincide). |
| Juego — reglas básicas correctas | ✅ | `Math.random()` en 1–100, intentos por botón, pista "Muy alto"/"Muy bajo" y mensaje al acertar. |
| Juego — casos borde manejados | ⚠️ | No valida el campo: vacío cuenta como intento y responde "Muy bajo"; 500 se acepta como "Muy alto"; tras acertar se puede seguir comprobando y cada intento suma. Sí limpia el campo tras cada intento. |
| Juego — interactividad y manejo de estado | ✅ | Contador de intentos y récord (menor cantidad de intentos) en `localStorage`; el estado del juego funciona. |
| Juego — feedback claro al usuario | ✅ | Mensaje por intento, contador de intentos y récord visibles. |
| Juego — reinicio sin recargar la página | ✅ | "Reiniciar" limpia el campo, pone intentos en 0 y genera otro número secreto. |

## Observaciones puntuales

- Verificación: Pages responde 200 en las 4 páginas y `script.js`. Eventos y partida simulados con jsdom (sin navegador real).
- `script.js` (bloque de suscripciones): `document.querySelectorAll('input[name="suscripcion"]').forEach(cb => cb.addEventListener("change", actualizarSuscripciones))` referencia una función `actualizarSuscripciones` que no existe. En `contacto.html` lanza `ReferenceError` al cargar y aborta el script entero: ningún campo vuelca su valor a la tabla de resumen. Es una regresión del Lab 5.
- `script.js` (suscripciones): `suscripcionInteres` queda con el resultado de `forEach` (`undefined`), por lo que aunque se definiera la función, el segundo `if (suscripcionInteres && ...)` nunca se ejecutaría.
- `script.js` (método de contacto): `metodosContacto` es un `NodeList` y se le llama `.addEventListener` directamente, lo que fallaría igual. Además, en `Contacto.html` solo el primer radio tiene `value`; los otros dos devolverían "on".
- `script.js` en `acercade.html`: el bloque del juego se ejecuta en todas las páginas y `get_reiniciar.addEventListener(...)` lanza `TypeError` al no existir el botón. "Leer más" se registra antes y sigue funcionando, pero queda un error en la consola.
- `Contacto.html`: `<datalist id="provincia">` repite el id del input de provincia y el campo usa `list="provincias"`, que no existe; el autocompletado de provincias no funciona. El input tiene `id="codigo postal"` con espacio.
- Los `if (x && xTD)` agregados para separar páginas no alcanzan: el guardado correcto es envolver cada bloque por página o verificar la existencia del elemento antes de cada `addEventListener`.
- Entrega dentro del plazo (último commit 16/11, merge 17/11, cierre 21/11).

## Nota final

| Ítem | Pts posibles | Pts obtenidos |
|---|---|---|
| Página personal completa y refinada | 20 | 10 |
| Subpágina/sección del juego | 15 | 15 |
| Navegación al juego | 10 | 10 |
| Juego — reglas correctas | 20 | 15 |
| Juego — interactividad y estado | 15 | 15 |
| Juego — feedback al usuario | 10 | 10 |
| Juego — reinicio sin recargar | 10 | 10 |
| **TOTAL** | **100** | **85** |

---

# Devolución Lab 6 — Isaías Reyes Arzamendia

## Datos identificatorios

- **Token:** reyes-6775-42
- **GitHub Pages:** https://isaiasreyesbjj16-ux.github.io/peylw-2026-practicos-reyes-6775-42/
- **Repositorio:** https://github.com/isaiasreyesbjj16-ux/peylw-2026-practicos-reyes-6775-42 (rama `main`, commit `7a85f25` del 18/11/2026)
- **Juego elegido:** Memoria con Cartas

## Checklist por ítem

| Ítem | Estado | Observación |
|---|---|---|
| Continuidad — página personal completa y refinada | ✅ | Las 4 páginas responden 200; header, nav, footer, fuente web y botón volver arriba presentes. El formulario de `contacto.html` vuelca los 10 campos a la tabla y "Leer más" alterna el CV. |
| Subpágina/sección del juego — presente | ✅ | `juego.html`. |
| Subpágina/sección del juego — diseño consistente con el portal | ✅ | Usa `styles.css`, mismo header, nav y footer. |
| Navegación — enlace al juego en todas las páginas | ✅ | Enlace "Juego" en el `<nav>` de las 4 páginas. |
| Juego — reglas básicas correctas | ✅ | Grid de 16 cartas boca abajo, volteo por clic, comparación de pares y detección de los 8 pares (partida completa simulada). |
| Juego — casos borde manejados | ✅ | Tablero bloqueado durante la comparación, no se puede voltear la misma carta ni una ya encontrada, y un contador de generación invalida los temporizadores de una partida anterior al reiniciar. |
| Juego — interactividad y manejo de estado | ✅ | Estado dentro de una IIFE, intentos, puntos, cronómetro y récord (intentos y tiempo) en `localStorage` con `try/catch`. |
| Juego — feedback claro al usuario | ✅ | Panel de feedback por acción y al ganar, más estadísticas visibles. |
| Juego — reinicio sin recargar la página | ✅ | "Reiniciar" remezcla, detiene el cronómetro y pone a cero los contadores. |

## Observaciones puntuales

- Verificación: Pages responde 200 en las 4 páginas y `script.js`. Partida completa, reinicio, par erróneo con re-ocultado y los eventos de `contacto.html`/`acercade.html` simulados con jsdom (sin navegador real); sin errores de JavaScript.
- La celda del método de contacto es `resumen-metodo` y el script la usa correctamente.
- El repositorio tiene archivos sueltos en la raíz (`config_git.png`, `images (2).jfif`, `laboratorio1`). No entran en la rúbrica.
- Entrega dentro del plazo (último commit 18/11, cierre 21/11).

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
