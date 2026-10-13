# Revisión crítica tras escribir la semana 1

**13 de octubre de 2026.** Contrasta lo escrito con:
- lo previsto en Figma (marcos v3 y v4);
- las mecánicas de la entrega integral;
- lo que se sabe de juegos móviles del género.

Cada hallazgo indica qué se corrigió ya (✅) y qué queda propuesto (◻).

---

## 1. Desajustes con Figma

| # | Hallazgo | Gravedad | Estado |
|---|---|---|---|
| F1 | El marco v4 (`83:536`) tiene una nota «TU SECRETARIA» con **«Estas son vuestras ocho jóvenes. Tocad a una…»**. Hay tres errores: el «vosotros» está prohibido, «ocho jóvenes» en femenino no vale porque son cuatro y cuatro, y la guía ya no tiene etiqueta de personaje (D9). El texto correcto está en `tutorial.yaml` | Alta | ◻ Corregir en Figma (`ui.tutorial` y `t09`) |
| F2 | Mi documento de flujo decía «las 8 cartas en arco, todas visibles». **Figma enseña 3,5 cartas y la mano se desliza**, y eso es más legible: con ocho cartas en 390 dp, las caras serían diminutas | Media | ✅ Corregido en `FLUJO-Y-MENUS.md` |
| F3 | En Figma v3, la recepción era «Casa Serravalle · Baile». En los datos es «Palacio · recepción», de la Corona | Baja | ◻ Actualizar el marco; mandan los datos |
| F4 | Las cartas de Figma muestran «A, B, C» y retratos realistas de relleno | Baja | ◻ Se sustituyen cuando estén los originales |
| F5 | **Faltan en Figma:** la ficha (biografía, pentágono, ficha técnica), el incidente con la línea de coste, el resultado, la Crónica, «Sólo para sus ojos» y el carnet de baile | Media | ◻ Repaso del flujo (E8) |

## 2. Mecánicas prometidas que la semana 1 no cumplía

| # | Hallazgo | Estado |
|---|---|---|
| M1 | **No había simultaneidad.** Las 4 invitaciones caían en días distintos, así que el mapa nunca mostraba dos eventos a la vez. Es el corazón de lo tomado de Dispatch y lo pide la entrega integral | ✅ El paseo y la lectura caen ahora **el mismo jueves 27**: se ven en paralelo y nadie puede ir a los dos |
| M2 | **El incidente se resolvía eligiendo siempre la habilidad más alta.** No había decisión real | ✅ Cada opción tiene un **precio propio** (`consecuencia` y `pista_coste`). Por ejemplo, el rumor sale bien pero Mara lo publicará; el debate une a quienes discuten; corregir al maestro de ceremonias da reputación, pero lo humilla |
| M3 | **Estaba demasiado fácil.** La simulación de todas las combinaciones daba un 100 % de veladas logradas en la lectura y un 96 % en el paseo | ✅ Fórmula y requisitos rebalanceados: ahora la mejor opción logra entre el 68 y el 72 % y la peor, entre el 12 y el 15 %. Herramienta nueva: `herramientas/simular_eventos.py` |
| M4 | **No había romance en la primera sesión.** Las escenas de vínculo empiezan en la semana 2, así que la primera partida terminaba sin ningún roce. En móvil, la primera sesión decide si se vuelve | ✅ Se añadieron las **«chispas»** (`observaciones.yaml`): una observación privada por semana sobre la pareja con posible atracción que asistió junta. Nunca es una etiqueta |
| M5 | **El primer toque útil llegaba tarde:** la reina y luego el reparto de las 8 cartas una a una tardaban unos 2,5 minutos | ✅ Las cartas caen juntas y «Continuar» se ve desde el principio. Objetivo: la primera decisión antes de 90 s |
| M6 | **Las personas no tienen objetivos propios** («Nilo quiere ir al paseo»). Lo pedía la entrega integral | ◻ Propuesta: **peticiones semanales** (1 o 2 por semana). Si se atienden, el personaje queda alegre y se desbloquea una entrada de su ficha. Desde la semana 2 |
| M7 | Faltan dos ideas del usuario recogidas en la entrega integral: el **memorice de cartas con una adivina**, que da pistas de la semana siguiente, y el **encuentro a medida que se paga con reputación** | ◻ Propuesta: la adivina en la Noche de los Faroles (semana 3), opcional y sin reloj. El encuentro a medida, desde la semana 4, a cambio de 3 de reputación |
| M8 | «Camila acompaña a Celia a todas partes» no tenía mecánica | ✅ Queda como algo **sólo narrativo** (canon §3.2) |
| M9 | Los viajes de varios días y el reemplazo no aparecen en la semana 1 | ◻ Se estrenan en la semana 2: una excursión de 2 días y la primera indisposición escrita |
| M10 | La pista del carruaje Miravés con las cortinas echadas apunta a Dario como nocturno, pero es humano (D4) | Aceptable como pista falsa, porque la nocturna es su tía. ◻ Confirmarlo con el usuario |

## 3. Calidad de juego en móvil

**Lo que está bien:**
- **Sesiones cortas con un cierre natural.** Una semana dura entre 8 y 10 minutos (planificar, ver correr los días, leer la Crónica). El gancho final da ganas de volver.
- **Se entiende de un vistazo:** el pentágono compara lo que se pide con lo que se lleva y los resultados se cuentan con sellos y frases, no con números.
- **Hay mucho que coleccionar:** 48 entradas de ficha, 83 cierres y 28 parejas posibles. Da para varias partidas.
- **El texto es breve:** como máximo 3 líneas por toque y comentarios de menos de 14 palabras.

**Riesgos:**
1. **Una partida completa dura unas 1,5–2 horas.** Para un juego de pago está bien; para uno gratuito con compras, es corto.
2. **Si el pentágono se puede leer y el resultado es fijo, puede volverse un puzle resuelto.** Lo compensan los precios de cada opción, las chispas y que optimizar la reputación compite con juntar a quien se quiere unir. **Esa tensión hay que enseñarla en el tutorial.** Propuesta: una nota en la semana 2, «La mejor pareja para un salón no siempre es la mejor pareja».
3. **El balance está medido en una tabla, no jugando.** Hay que probarlo con 5–10 personas antes de producir las semanas 2 a 6.
4. **Queda texto sin voz.** Buena parte del encanto depende del arte de los retratos y de sus 4 expresiones: si el arte falla, el juego se vuelve una hoja de cálculo.

**Referencias de retención:** en 2025, la mediana de los juegos móviles retuvo un 22 % el día 1, menos del 4 % el día 7 y menos del 1 % el día 30. El 10 % mejor llega al 40 % el día 1 y a cerca del 12 % el día 7 ([GameAnalytics 2026](https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game)). Un juego narrativo de pago no se mide igual: importa más que se termine y que se vuelva a jugar.

## 4. Lo que sigue pendiente de decidir

1. Peticiones semanales (M6).
2. La adivina y el encuentro a medida (M7).
3. La pista falsa del carruaje (M10).
4. El modelo de venta (ver [COMERCIALIZACION.md](<COMERCIALIZACION.md>)).
