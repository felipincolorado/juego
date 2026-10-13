# Salverna · Estudio de poses de personaje — Propuesta (v1)

**13 de octubre de 2026 · PROPUESTA.** Complementa [encargos del elenco](<ENCARGOS-ELENCO-TANDA-2.md>) (§5 y §6) y el [elenco](<ELENCO-TEMPORADA-PROPUESTA.md>). Nada queda aprobado por estar escrito.

**Pedido del usuario:** que cada pose cuente la personalidad sin depender de detalles difíciles de dibujar (como el anillo que Dario gira entre los dedos). Los modelos son los juegos japoneses que mejor lo hacen.

---

## 1. Qué hacen bien los juegos japoneses

| Referente | Qué aprender | Qué no copiar |
|---|---|---|
| **Ace Attorney** (Capcom) | Pocas poses, pero cada una es la personalidad entera. Cada diseño se distingue por silueta, gestos y forma de hablar. Las poses cambian con la escena: de suficiente, a nervioso, a desesperado. | La exageración cómica, que no encaja con el tono de Salverna. |
| **Persona 5** (Soejima) | La ropa ya actúa: quien es relajado lleva la camisa desabrochada. La primera impresión es el aspecto, y el diseño parte de lo que escribe el guionista. | El estilo gráfico duro y el rojo. |
| **Otome de Otomate** (*Hakuoki*, *Code: Realize*, *Amnesia*) y **Ikemen** (Cybird) | Retrato de pie en vista de tres cuartos. Cada pretendiente tiene **un gesto de brazo propio**. La personalidad está en la línea de los hombros, la inclinación de la cabeza y la dirección de la mirada. Se cambian partes del rostro, no todo el cuerpo. | Los ojos enormes. La ropa recargada de cadenas y hebillas. |
| **Fire Emblem: Three Houses** | Retratos de busto: los hombros girados o de frente y la altura de la barbilla definen al personaje antes que la cara. | El nivel de detalle de la armadura. |
| **Danganronpa** | Inseguridad sin palabras: encogido de hombros, manos juntas delante o en los bolsillos, la sombra del pelo sobre los ojos. | El estilo de colores saturados. |

**Conclusión práctica.** En estos juegos la personalidad no está en un objeto pequeño. Está en **cinco palancas grandes** que se leen incluso en miniatura:

1. **Cabeza:** inclinación lateral y altura de la barbilla.
2. **Hombros:** de frente o girados, altos o caídos, simétricos o desiguales.
3. **Mirada:** al jugador, apartada, que llega tarde, desde arriba o desde abajo.
4. **Forma de los brazos:** abiertos, cerrados, una mano cerca del pecho o de la cara.
5. **Peso del cuerpo:** recto, apoyado en una cadera, inclinado hacia delante o hacia atrás.

---

## 2. Regla de Salverna: la pose tiene que leerse en la carta

La carta muestra sólo **el 50 % central del ancho y el 50 % superior del alto** del original (cabeza, cuello, hombros y parte del pecho). Las manos a la altura de la cintura **quedan fuera de la carta**.

- **El 80 % de la personalidad va arriba:** cabeza, mirada, línea de los hombros, cuello, y un brazo o una mano a la altura del pecho si el gesto lo pide.
- **Lo de la cintura para abajo** sólo se ve en el original completo y en la ficha. Es un complemento, nunca lo único que cuenta.

### 2.1 Manos baratas y manos caras

| ✅ Usar (fáciles y legibles) | ❌ Evitar (caras y con errores frecuentes) |
|---|---|
| Manos ocultas: a la espalda, metida en el chaleco (gesto de época), brazos cruzados | Objetos pequeños entre los dedos: anillo, alfiler, lápiz, taza, carta abierta, flor |
| Puño cerrado: en la cadera, agarrando la solapa | Dedos que señalan, se cruzan o tocan algo con precisión |
| Mano plana apoyada: en el pecho, sobre el antebrazo | Dos manos entrelazadas con los dedos visibles |
| Guantes: convierten la mano en una forma simple | Manos delante de la cara que tapen rasgos |
| Como máximo **un** objeto grande, sujeto con la mano entera (un abanico cerrado como una vara) | Accesorios que haya que repetir igual en cada pose y expresión |

### 2.2 Prueba de silueta

Las 8 cartas deben distinguirse **en negro, a 112 px de ancho** (el tamaño de la carta en la mano del elenco). Si dos siluetas coinciden, se cambia una de las dos poses.

---

## 3. Catálogo de poses por arquetipo

Cada arquetipo trae su frase en inglés, lista para pegar en el bloque POSE del prompt.

| Arquetipo | Cabeza y mirada | Hombros y peso | Brazos y manos | Silueta clave | Frase para el prompt |
|---|---|---|---|---|---|
| **Tímida** | Barbilla baja, mirada que sube hacia el jugador por debajo de las cejas o se aparta | Hombros algo levantados y hacia dentro, cuerpo ligeramente de lado | Brazos pegados al cuerpo; una mano sujeta el otro brazo | Estrecha, recogida | *chin slightly lowered, eyes lifting shyly towards the viewer, shoulders drawn slightly up and inward, one hand holding the opposite forearm close to the body* |
| **Galán** | Cabeza un poco ladeada, media sonrisa, mirada directa y sostenida | Tres cuartos, un hombro adelantado hacia el jugador | Una mano plana en el pecho, como al empezar una reverencia | Diagonal abierta hacia el jugador | *three-quarter view, near shoulder turned towards the viewer, head tilted slightly, steady warm gaze, one flat hand resting on his chest as if beginning a bow* |
| **Segura** | Barbilla nivelada, mirada frontal tranquila, sin sonrisa forzada | Frontal, hombros rectos y relajados, simétrica | Manos a la espalda (no se ven) | Vertical, columna | *front view, chin level, calm direct gaze, square relaxed shoulders, hands clasped behind the back (not visible)* |
| **Empoderada** | Barbilla algo alta, mirada desde arriba, sonrisa de desafío | Peso en una cadera, hombros abiertos y anchos | Un puño en la cadera, codo hacia fuera | Triángulo ancho | *chin slightly raised, looking down at the viewer with a challenging smile, weight on one hip, shoulders open, one fist on the hip with the elbow out* |
| **Mística o enigmática** | Cuerpo de espaldas a tres cuartos; la cabeza gira y mira por encima del hombro; párpados pesados | El hombro hace de barrera entre él y el jugador | Una mano metida en el chaleco o fuera del cuadro | Diagonal cerrada, de espaldas | *body turned three-quarters away, head turning back over the shoulder towards the viewer, heavy-lidded gaze, one hand tucked inside the front of the waistcoat* |
| **Bromista** | Una ceja arriba, la comisura se escapa, cabeza ladeada | Hombros algo altos, inclinado como si fuera a contar un secreto | Los dos puños agarran las solapas: «seriedad» de orador | Asimétrica, inquieta | *shoulders slightly raised, head tilted, one eyebrow up, mouth corner escaping into a grin, both fists gripping his own lapels in mock solemnity* |
| **Ensayada o perfecta** | Barbilla alta, cuello largo, sonrisa practicada | Postura de bailarina, totalmente simétrica | Manos enguantadas juntas a la cintura (fuera de la carta) | Vertical y estrecha | *dancer's posture, long neck, chin slightly high, practised smile, gloved hands folded at the waist* |
| **Analítica** | Cabeza ladeada, mirada que estudia, cejas rectas | Peso recto, ligeramente hacia atrás | Un brazo cruzado a la cintura; los nudillos de la otra mano rozan la barbilla, dedos recogidos | Asimétrica con el codo a media altura | *head tilted, studying gaze, one arm folded across the waist supporting the other elbow, the knuckles of that hand lightly at the chin, fingers curled* |
| **Matriarca irónica** | Cabeza algo atrás, mira «por encima de la nariz», una ceja arriba | Peso atrás, figura amplia y quieta | Abanico cerrado sujeto con la mano entera, apoyado en el hombro | Ancha y horizontal | *head tilted slightly back, looking down her nose with one eyebrow raised, slow knowing smile, a closed fan held in her whole hand and resting on her shoulder like a baton* |
| **Cálido y franco** | Mirada abierta, sonrisa que se le escapa | Frontal, inclinado un poco hacia el jugador | Brazos abiertos o una mano en el pecho | Ancha y abierta | *front view, leaning slightly towards the viewer, open honest face, a held-back smile escaping* |

---

## 4. Propuesta por personaje (original formal)

| Persona | Arquetipo | Pose propuesta | En la carta se lee… | Silueta |
|---|---|---|---|---|
| **Nilo** | Cálido-franco con toque de galán | Frontal, inclinado hacia el jugador, mano plana en el pecho como al empezar una reverencia | Sonrisa escapada, hombros anchos, la mano en el pecho | Ancha y abierta |
| **Saúl** | Segura | Frontal, manos a la espalda, barbilla nivelada | Columna recta, cuello largo, mirada serena | Vertical, simétrica |
| **Dario** | Mística | De espaldas a tres cuartos, mira por encima del hombro, una mano metida en el chaleco. **Sin anillo** | Hombro barrera, mirada que llega tarde, pelo atado | Diagonal cerrada |
| **Teo** | Bromista | Hombros altos, puños en las solapas, una ceja arriba | Asimetría, sonrisa escapada, pelo revuelto | Inquieta, en zigzag |
| **Celia** | Ensayada | Postura de bailarina, barbilla alta, manos juntas a la cintura | Cuello largo, recogido alto, sonrisa practicada | Vertical y estrecha |
| **Irene** | Analítica | Cabeza ladeada, brazo cruzado, nudillos en la barbilla | Inclinación de la cabeza, codo a la altura del pecho | Asimétrica |
| **Isolda** | Empoderada | Puño en la cadera, peso en una pierna, barbilla alta, chaquetilla abierta | Barbilla, mirada desafiante, franja perla, hombros abiertos | Triángulo ancho |
| **Camila** | Matriarca irónica | Cabeza atrás, ceja arriba, abanico cerrado apoyado en el hombro | Mirada por encima de la nariz, abanico como diagonal | Ancha y horizontal |

**Tímida:** ningún original formal la usa, porque nadie se presenta así en sociedad. Se usa en las **expresiones ruborizadas** y en la **pose de ficha de Celia**, cuando se le cae la máscara.

**Contrastes:**
- Saúl y Celia comparten verticalidad. Los distinguen la simetría quieta de él y la barbilla alta de ella; en la carta, el recogido alto de Celia rompe la columna.
- Dario y Camila: los dos son reservados. Él es una diagonal cerrada; ella, una forma ancha.

---

## 5. Bloque común para los prompts

Se añade a cada prompt, después de ACTING:

```text
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
```

---

## 6. Pendiente de decisión

1. ¿Te sirven los arquetipos asignados, sobre todo **Dario místico de espaldas** y **Teo con los puños en las solapas**?
2. ¿Camila **conserva el abanico** (como vara apoyada en el hombro) o se queda sin objeto?
3. Para Dario: ¿**rehacer el original** con la nueva pose o **editar el v1** (el de mejor calidad)? Recomiendo editar el v1, para no perder la mano del dibujo.

---

## Fuentes consultadas

- [Mechanics of Magic: Ace Attorney review](https://mechanicsofmagic.com/2024/05/03/rwp-2024-phoenix-wright-ace-attorney-jasmine-steele/) and [RWP 2024 – Ace Attorney](https://mechanicsofmagic.com/?p=29204)
- [Fandom: entrevista con Shigenori Soejima](https://www.fandom.com/articles/atlus-booth-hosts-interview-persona-5-character-designer-shigenori-soejima) · [RPG Site: P5 Q&A](https://www.rpgsite.net/interview/4887-persona-5-qa-with-character-designer-shigenori-soejima)
- [Lycoris: devlog de sprites otome](https://itch.io/devlog/89901/update-1-finished-sprites-and-profiles.amp)
- [Wikipedia: List of Ace Attorney characters](https://en.wikipedia.org/wiki/List_of_Ace_Attorney_characters)
- Las observaciones sobre Otomate, Ikemen, Fire Emblem y Danganronpa vienen del análisis de sus retratos publicados. No hay entrevistas citables sobre sus poses.
