# Salverna · Minijuego «La mesa de la cartomante» (v1)

**13 de octubre de 2026 · Propuesta.**

**Origen:**
- La idea del usuario recogida en la entrega integral §3: un memorice de cartas con una adivina, dificultad creciente y pistas de la semana siguiente.
- Su petición del 13 de octubre: algo que **saque del ritmo del juego**, con **cartas bonitas** y una **predicción**.

**Recomendación de la entrega integral:** debe ser opcional, sin reloj, sin bloquear información central y sin revelar orientaciones. Este diseño la respeta.

---

## 1. Qué es

**La cartomante Oriana Vell** (nuevo) pone su mesa en los Muelles del Canal de Serel durante la temporada.
- La casamentera la visita **una vez por semana**, durante la planificación.
- La visita **no ocupa a nadie del elenco**: es un momento sólo de la jugadora.
- Oriana reparte sus cartas boca abajo. Según cuántas parejas encuentre la jugadora, le lee **un presagio de la semana**.

**Por qué funciona como pausa:**
- Cambia de verbo: de asignar personas a recordar imágenes.
- Cambia de ritmo: no hay fechas ni consecuencias sociales.
- Cambia de escenario: una mesa con terciopelo azul noche y una vela, en lugar del mapa.
- Dura entre 1 y 2 minutos.

## 2. Reglas

| Elemento | Regla |
|---|---|
| Disponible | Desde la **semana 2**, en la fase de planificación. Marcador en `muelles` con un icono de carta |
| Frecuencia | 1 visita por semana. Si no se usa, se pierde (no se acumula) |
| Mesa | Cartas 2:3 boca abajo. Se tocan dos: si son iguales, quedan descubiertas; si no, se vuelven a tapar |
| Velas | La mesa empieza con un número de **velas**. Cada pareja fallida apaga una. Cuando se apagan todas, termina la lectura con las parejas encontradas. **No hay reloj** |
| Dificultad creciente | Semana 2: 6 parejas (rejilla de 3 × 4) y 8 velas · Semanas 3–4: 8 parejas (4 × 4) y 9 velas · Semanas 5–6: 10 parejas (4 × 5) y 10 velas |
| Resultado | **Todas** las parejas → presagio claro y **don de la vela**. **La mitad o más** → presagio velado. **Menos de la mitad** → presagio oscuro |
| Don de la vela | Esa semana, en un incidente al azar, la opción con mejor resultado lleva **una pequeña llama dorada**. Se marca y se recuerda en la hoja del incidente |
| Movimiento reducido | Las cartas se dan la vuelta con un fundido en lugar de un giro |
| Accesibilidad | Cada carta tiene nombre para el lector de pantalla al descubrirse. Con el lector activo, se puede elegir **«Mesa sencilla»**: 4 parejas sin velas |

**Distribución:**
- Las cartas se mezclan con la semilla de la partida y la semana, así que repetir la visita no cambia la mesa.
- El presagio está **escrito por autoría para cada semana**, con tres niveles, y siempre es **verdad**:
  - **Claro:** nombra un lugar y lo que está en juego.
  - **Velado:** sólo da imágenes.
  - **Oscuro:** casi no se entiende hasta después.
- **Nunca revela** orientaciones, la autoría de la *Hoja* ni condiciones.

## 3. Las cartas (12 símbolos del mundo)

Cada símbolo pertenece a Valcenda. El nombre y el significado aparecen al descubrir la pareja y dan color a la lectura.

| ID | Carta | Significado en la lectura |
|---|---|---|
| `sello` | El Sello | Un compromiso que no se puede deshacer |
| `abanico` | El Abanico | Lo que se dice tapándose la boca |
| `mascara` | La Máscara | Alguien que no es lo que aparenta |
| `rosa` | La Rosa tardía | Un afecto que llega fuera de tiempo |
| `llave` | La Llave | Una puerta que sólo se abre en confianza |
| `farol` | El Farol | Recordar a quien se perdió |
| `luna` | La Luna llena | Una noche en que alguien no puede estar |
| `pluma` | La Pluma | Algo escrito que nadie firmó |
| `corona` | La Corona | La mirada de la reina |
| `barco` | El Barco | Una deuda que viene del mar |
| `nudo` | El Nudo de Serel | Un recuerdo que alguien quiere conservar |
| `copa` | La Copa | Un brindis que es también un pacto |

**Arte necesario:**
- 1 reverso de carta.
- 12 caras.
- 1 tapete de fondo.
- La cartomante: busto base y 2 expresiones.
- **Total: 17 imágenes.** Están añadidas al inventario como tanda 3.

## 4. Datos

Todo está en `datos/minijuego_adivina.yaml`: las cartas, las frases de Oriana y los presagios de las semanas 2 a 6 en tres niveles, en ES y EN.
