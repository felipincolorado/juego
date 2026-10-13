# Salverna · Elenco: revisión crítica, control del tono amarillo y encargos de imagen (tanda 2)

**14 de octubre de 2026 · PROPUESTA para generar en ChatGPT con la referencia de técnica de Dressmaker.**
Depende de [elenco](<ELENCO-TEMPORADA-PROPUESTA.md>), [relaciones](<RELACIONES-Y-UNIONES-PROPUESTA.md>), la [guía de prompts](<../GUIA-PROMPTS-Y-GENERACION-PERSONAJES-SALVERNA.md>) y el [paquete de la tanda 1](<PAQUETE-IMAGENES-TANDA-1.md>). Ninguna identidad queda aprobada por existir: cada original se revisa antes de derivar poses y expresiones.

---

## 1. Revisión crítica del conjunto (personajes y propuestas)

| # | Hallazgo | Riesgo | Propuesta |
|---|---|---|---|
| 1 | **No había diversidad de piel definida** en el elenco | Ocho caras parecidas; además, Bridgerton es conocido justamente por su reparto diverso | Se asigna un tono de piel individual a cada persona (§3) según el mundo v0.3 («humanos diversos en piel, origen y facciones») |
| 2 | **Faltaban colores de casa** para cartas y vestuario | Cartas indistinguibles | Un color por casa, evitando amarillos y naranjas (el generador ya empuja hacia ahí) (§3) |
| 3 | **Vestuario sin referente concreto** | La guía exige referencia identificable antes del prompt | Mujeres: se apoyan en los 9 originales del usuario. **Hombres: no hay referentes propios del periodo** (sólo la casaca del XVIII de la ref. 03): falta investigar levitas, chalecos y corbatines de 1800–1820 en museos (V&A, Met) antes de aprobar |
| 4 | **Dato de Dario sin fuente** («sobrino de Amalia, reacio a heredar») | Inventar sobre canon | Confirmar en el registro del proyecto antes de escribir su ruta |
| 5 | **Decisiones abiertas que afectan a las imágenes** | Ninguna (lo visual no depende de ellas) | Dario se diseña sin colmillos ni rasgos sobrenaturales; sirve para las opciones A y B |
| 6 | **Edades sin fijar** | Rostros incoherentes con la ficha | Se proponen edades (§3) para revisión |
| 7 | **Dos Lobreda (Nilo y Celia)** | Que parezcan iguales | Comparten verde de casa en tonos distintos y algún rasgo familiar (cejas), con siluetas opuestas |
| 8 | **Orientación y aspecto** | Que el diseño «delate» la orientación | Ningún rasgo visual sugiere orientación; los estereotipos están prohibidos |
| 9 | **Fondo transparente para personajes** | No permite medir ni corregir el tono amarillo | **Decisión del usuario (13 oct.):** ChatGPT entrega el personaje ya sin fondo; no se genera sobre gris ni se recorta. El tono se controla en los blancos (§2) |

Lo que funciona bien: arquetipos con contradicción, atractivo concreto, vínculos previos que generan drama, habilidades justificadas y el sistema de uniones con consecuencias. El elenco está listo para diseñarse.

---

## 2. Cómo vencer el tono amarillo de ChatGPT

### 2.1 Qué se sabe (investigación del 14 oct.)

- No existe un interruptor oficial: la dominante cálida es un comportamiento por defecto del modelo y OpenAI no ha publicado su causa.
- Las palabras de color en el prompt («balance de blancos neutro», «luz de día») **ayudan, pero no son fiables**: a veces la imagen sale lavada y el tono vuelve.
- Pedirle a ChatGPT «menos amarillo» sobre una imagen **la regenera entera** y cambia el dibujo.
- **Lo único fiable es corregir después**: balance de blancos sobre una zona que debería ser neutra, curvas o el canal b* en LAB.

Fuentes: [PopularAI](https://www.popularai.org/p/chatgpts-piss-filter-why-ai-images), [TechRadar](https://www.techradar.com/ai-platforms-assistants/chatgpt/tired-of-that-yellow-tint-in-chatgpt-images-heres-how-to-fix-it-with-simple-color-correction), [CO/AI](https://getcoai.com/news/why-chatgpt-images-look-yellow-and-3-ways-to-fix-it/), [Korben](https://korben.info/en/fix-ai-color-balance-practical-solutions.html).

### 2.2 Método propuesto en cuatro capas

1. **Evitar palabras que llaman al tono cálido** en todos los prompts: *Regency painting, vintage, antique, aged, parchment, candlelight, golden hour, warm, cozy, cinematic, sepia, oil painting, old master, varnish*. Hablar de «moda de principios del siglo XIX» en lugar de «pintura de época». Tampoco *warm-ivory*: usar *cool off-white*.
2. **Bloque de control de color** dentro de cada prompt (§2.3), con blancos y sombras definidos.
3. **Personajes sin fondo** (decisión del usuario, 13 oct.): ChatGPT los entrega ya en PNG transparente, así que no se genera sobre gris ni se recorta. Los fondos y escenarios sí conservan el método del gris o una zona neutra de referencia.
4. **Corrección automática** con [`herramientas/corregir_tono.py`](<../herramientas/corregir_tono.py>). En personajes sin fondo: `--solo-blancos 0.85` (sólo neutraliza linos y camisas pintados en crema; no toca piel ni colores). En fondos: `--borde` o `--zona` como antes.

```
pip install pillow numpy
python herramientas/corregir_tono.py dario_formal_v1.png --borde 4
python herramientas/corregir_tono.py carpeta_tanda2/ --borde 4          (lote)
python herramientas/corregir_tono.py mapa.png --zona 120,80,60,60       (zona neutra concreta)
```

El script informa del índice de amarillo antes y después (ejemplo de prueba: +24,5 → 0,0) y conserva la transparencia si la imagen ya la tiene. Para imágenes sin fondo neutro (como el mapa), se indica con `--zona` un rectángulo que deba ser neutro (una fachada blanca, una nube).

**La carta de colores que ya usan** sigue siendo útil como guía de pigmentos, pero ya no tiene que cargar sola con el control: la corrección final la asegura la herramienta.

### 2.3 Bloque de control de color (incluido en cada prompt)

```text
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
```

---

## 3. Identidad visual del elenco

Edades, pieles y rasgos son **propuestas**. Ningún rasgo sugiere orientación.

| Persona | Edad | Piel | Pelo (silueta en carta) | Rostro y cuerpo | Color de casa | Vestuario (referente) |
|---|---|---|---|---|---|---|
| **Nilo Lobreda** | 26 | Clara-oliva tostada por los caminos, mejillas encendidas | Rizos castaño oscuro sueltos, hasta las orejas, imposibles de peinar | Mandíbula ancha, cejas gruesas, nariz recta algo ancha; hombros anchos, cuello fuerte | **Verde bosque** (Lobreda) | Levita de lana verde bosque algo arrugada, chaleco de lana avena con botones de madera (lana y madera de Greda), corbatín flojo. Referente masculino por investigar |
| **Saúl Veyra** | 30 | Marrón profundo | Muy corto, línea nítida | Pómulos altos, mandíbula marcada, mirada serena; alto, cuello largo, hombros rectos | **Azul acero** (Veyra) | Casaca de gala azul acero de cuello alto, botones plateados (no dorados), corbatín blanco impecable, guantes blancos. Referente masculino por investigar |
| **Dario Miravés** | 27 | Oliva pálida, subtono frío | Largo, negro y liso, atado bajo con cinta oscura | Rostro alargado, párpados pesados, ojos grises, nariz fina; esbelto, cuello largo | **Ciruela** (Miravés) | Levita de terciopelo ciruela, chaleco de seda negra con dibujo ciruela sutil, un solo alfiler granate, un anillo. Referente masculino por investigar |
| **Teo Rovena** | 24 | Clara con pecas, mejillas rosadas | Cobrizo revuelto en todas direcciones | Rostro estrecho, cejas arqueadas muy móviles, boca ancha; delgado, nervioso | **Rosa malva** (Rovena) | Su única levita buena, malva empolvado, gastada en los puños; chaleco estampado discreto. Referente masculino por investigar |
| **Celia Lobreda** | 21 | Clara, rosada | **Recogido alto elaborado** con trenza en corona y ramitas | Rostro redondo, ojos grandes, barbilla pequeña, cejas Lobreda; menuda, cuello largo, postura de bailarina | **Verde salvia** (Lobreda, más claro) | Vestido imperio verde salvia con **bordado botánico vertical** (ref. 06), mangas abullonadas cortas, guantes largos blancos |
| **Irene Salvat** | 25 | Beige claro-medio, subtono neutro | Negro y liso, **moño bajo sin adorno** | Rostro anguloso, cejas rectas, mirada analítica; alta, hombros estrechos | **Azul pizarra** (archiveros) | Vestido de día de lana fina azul pizarra, manga larga, cuello blanco pequeño; prendas largas de calle para exteriores (ref. 08) |
| **Isolda Marén** | 26 | Marrón medio | **Verde pizarra, ondas medio sueltas, franja perla frontal**; iris cobre apagado (rasgos velarios) | Cejas rectas, sonrisa pronta; cuello y hombros fuertes | **Verde mar** (aseguradores Marén) | Vestido verde mar con **cierre lateral y escote en V** (tradición portuaria, mundo v0.3), chaquetilla corta abierta sin abrochar (contraste estructural de la ref. 05) |
| **Camila Ferrán** | 29 | Marrón profundo | **Rizos oscuros recogidos bajos** en la nuca | Párpados caídos, sonrisa lenta; figura plena, cuello corto y elegante | **Lavanda y gris perla** (medio luto) | Seda lavanda grisácea con encaje negro (medio luto), cinta de luto en la muñeca con una inicial (costumbre del mundo), abanico cerrado; autoridad madura de la ref. 02 sin su burdeos |

---

## 4. Imágenes por persona y orden de producción

1. **Original formal** (las 8 primero): busto hasta la cadera, encuadre fijo (coronilla al 6 %, **ojos al 20 %**, barbilla al 31 %), manos visibles si actúan. Sin fondo (PNG transparente). De aquí se recorta la carta.
2. Revisión y **aprobación de identidad** de cada original.
3. **Pose de ficha**: edición desde el original aprobado (§6).
4. **Expresiones** (alegre, molesta, ruborizada): cada una desde el original (§6).

Generar: 1024 × 1536. Objetivo tras escalar: 1536 × 2304 (sujeto a comprobación). Después: `corregir_tono.py --borde 4` → quitar fondo → revisar alfa sobre claro y oscuro → montar en la carta en Figma.

**Adjuntos del original formal:** los originales ilustrados de técnica (Dressmaker y los del proyecto), declarados como **técnica, no identidad ni color**; la carta de color individual si se prepara. Nunca adjuntar otro personaje del elenco.

**Qué referencias de Dressmaker adjuntar (medido el 14 oct.):**

| Referencia | Blancos (índice de amarillo) | Uso recomendado |
|---|---|---|
| Chica del vestido blanco y pelo rubio | +6 (casi neutra) | **Adjuntar**: línea, pintura y blancos con sombra lila fría |
| Chica de vestido verde agua y abanico | −5 (fría) | **Adjuntar**: color local limpio, guantes blancos fríos |
| Chica de gafas y chaleco verde | +22 (crema) | No adjuntar: enseña el blanco crema |
| Dama de rosa con sombrero de pájaro | +23 (crema) | No adjuntar por color (sí sirve para estudiar actuación y personalidad del diseño) |
| Dama de negro | +15 (cálida) | No adjuntar |

La línea de las tres cálidas es marrón (≈ RGB 78·63·44); la de las dos frías es gris oscuro. El bloque de técnica pide gris-marrón oscuro, intermedio.

**Aviso sobre Dressmaker:** si sus imágenes tienen una paleta cálida, adjuntarlas empuja hacia el amarillo. Declararlas explícitamente como referencia de **línea y pintura** y confiar el color al bloque de §2.3 y a la corrección posterior.

---

## 5. Prompts del original formal (listos para pegar)

Bloque de técnica común (ya incluido abajo en cada prompt):

```text
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
```

### 5.1 Dario Miravés (primero)

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Dario Miravés, a 27-year-old man, as the formal portrait of a playable
character in a narrative mobile game set in Valcenda, a fictional capital with
early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front three-quarter view, head to hip, centred. Top of head at 6% of the
image height, eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: slender build, long neck, long face, heavy-lidded grey eyes, fine straight
nose, a faint half-smile that does not reach the eyes. Pale olive skin with a cool
undertone. Long straight black hair tied low at the nape with a dark ribbon.
Nothing supernatural: no fangs, no red eyes, no vampire costume.
COSTUME: deep plum velvet tailcoat with a high collar, black silk waistcoat with a
subtle plum pattern, crisp white cravat with a single small garnet pin, one plain ring
on the left hand. Clean, precise tailoring with natural, fairly narrow early-19th-century
shoulders: no padded or puffed shoulders.
ACTING: perfect courtesy hiding a closed door. He is turning the ring with his thumb;
his gaze arrives at the viewer a moment late.
COLOUR KEY: plum, black, pure white linen, pale olive skin, grey eyes.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: unmistakable silhouette (long tied hair, long neck); mysterious
courtesy without vampire clichés; neutral colour.
```

### 5.2–5.8 Resto del elenco

Mismo prompt que 5.1 cambiando sólo los bloques **Create**, **FRAMING** (si cambia la vista), **IDENTITY**, **COSTUME**, **ACTING** y **COLOUR KEY**. Los bloques TECHNIQUE, COLOUR CONTROL y OUTPUT se pegan idénticos.

| Persona | IDENTITY | COSTUME | ACTING | COLOUR KEY |
|---|---|---|---|---|
| **Nilo Lobreda**, 26 | Broad shoulders, strong neck, broad jaw, thick dark brows, slightly broad straight nose, open warm face. Light olive skin tanned by mountain roads, flushed cheeks. Unruly dark brown loose curls to the ears. | Forest-green wool tailcoat slightly rumpled, oatmeal wool waistcoat with wooden buttons, linen shirt, loosely tied cravat. | Trying to look formal for the occasion; a held-back smile escapes; one hand on his chest as if about to bow. Front view. | Forest green, oatmeal, white linen, tanned skin. |
| **Saúl Veyra**, 30 | Tall, long neck, square shoulders, high cheekbones, defined jaw, calm dark eyes. Deep brown skin. Very short cropped black hair with a crisp hairline. | Steel-blue dress tailcoat with a high collar and silver buttons, impeccable white cravat, white gloves. | Composed and reliable: hands behind his back, chin level, direct steady gaze; the stillness of someone who keeps his word. | Steel blue, silver, pure white, deep brown skin. |
| **Teo Rovena**, 24 | Slim and restless, narrow face, very mobile arched brows, wide mouth. Fair skin with freckles and rosy cheeks. Messy copper hair going in every direction. | His only good tailcoat in dusty mauve-rose, slightly worn at the cuffs; discreet patterned waistcoat; loosely knotted cravat. | Trying very hard to look serious and almost managing it: one corner of the mouth already rising, one eyebrow ahead of the joke. Front view. | Dusty mauve-rose, cream-white shirt, copper hair, freckled fair skin. |
| **Celia Lobreda**, 21 | Petite, long neck, dancer's posture, round face, large eyes, small chin, the same thick Lobreda brows as her cousin. Fair rosy skin. Light brown hair in a high elaborate updo with a braided coronet and tiny green sprigs. | Sage-green high-waisted gown with vertical botanical embroidery, short puffed sleeves, long white gloves. | Perfectly rehearsed: practised smile, chin slightly high, gloved hands folded at the waist. | Sage green, white gloves, embroidery in deeper green, rosy fair skin. |
| **Irene Salvat**, 25 | Tall, narrow shoulders, angular face, straight brows, attentive analytical eyes. Light-medium beige skin with a neutral undertone. Straight black hair in a plain low knot, no ornament. No glasses. | Slate-blue day dress of fine wool, long sleeves, small white collar, no jewellery. | Studying the viewer as if reading a document: head slightly tilted, hands loosely together. Front view. | Slate blue, white collar, black hair, beige skin. |
| **Isolda Marén**, 26 | Strong neck and shoulders, straight brows, a ready smile. Medium brown skin. Velaria traits: slate-green hair in loose half-up waves with a pearl-white streak at the front, muted copper irises. | Sea-green gown with a side fastening and a V neckline (port tradition), a short open jacket she has not buttoned. | Relaxed and amused, weight on one hip, looking straight at the viewer as if daring them to object. | Sea green, slate-green hair, pearl streak, copper eyes, medium brown skin. |
| **Camila Ferrán**, 29 | Full figure, short elegant neck, heavy-lidded eyes, a slow knowing smile. Deep brown skin. Dark coily hair arranged low at the nape. | Lavender-grey half-mourning silk gown with black lace trim, a narrow black mourning ribbon at the wrist embroidered with a single initial, a closed fan. | She has seen this before: one eyebrow slightly raised, fan closed in both hands. | Lavender-grey, black lace, deep brown skin, dark hair. |

---

## 6. Pose de ficha y expresiones (desde el original aprobado)

Plantilla (de la guía de prompts §7), con fondo gris neutro y el bloque COLOUR CONTROL añadido al final:

```text
EDIT OF THE ATTACHED APPROVED ORIGINAL. The attached image is the sole visual authority.
Preserve exactly the same person: identity, proportions, face, hair, skin, costume,
accessories, palette, handcrafted line and paint. Do not beautify or redesign.
NEW {POSE or EXPRESSION}: {intent and precise description from the table below}.
Change only pose/expression, gesture and physically necessary folds.
Keep readable anatomy, complete hands and attached accessories.
(+ COLOUR CONTROL block from §2.3)
```

| Persona | Pose de ficha (cómo es cuando baja la guardia) | Alegre | Molesta | Ruborizada |
|---|---|---|---|---|
| Nilo | Sentado del revés en una silla, cuerpo adelantado, atención franca a alguien fuera de cuadro | Carcajada abierta, cabeza atrás | Mandíbula apretada, mirada al suelo, culpa | Se rasca la nuca y aparta la vista sonriendo |
| Saúl | Sentado, guantes retirados sobre la rodilla, hombros menos rígidos | Sonrisa pequeña que intenta contener | Mandíbula firme, mirada al frente, manos a la espalda | Aparta la mirada y se ajusta el corbatín |
| Dario | Junto a una ventana, torso de tres cuartos, la mirada vuelve al interlocutor | Sonrisa auténtica, sorprendido de sí mismo | Cortesía helada, párpados aún más pesados | Pierde la compostura un instante, mano en el anillo |
| Teo | Acaba de soltar una observación: gesto abierto, un instante de incertidumbre | Ríe con todo el cuerpo | Cejas caídas, broma que no le sale | Se tapa media cara con la mano, ríe nervioso |
| Celia | Preparándose antes de entrar al salón: concentración, postura ensayada | Sonrisa no ensayada, ojos brillantes | Labios apretados, se recoloca un guante | Mira hacia abajo, mejillas encendidas, sonrisa pequeña |
| Irene | Deja un momento un documento para atender con curiosidad | Sonrisa de descubrimiento | Cejas rectas más juntas, mirada fija | Pierde el hilo, se toca el cuello del vestido |
| Isolda | Postura cómoda y poco ceremonial, codo apoyado, atención cómplice | Ríe la primera, cabeza ladeada | Barbilla alta, sonrisa desafiante | Mira a un lado sin perder la sonrisa, se toca la franja perla |
| Camila | Recostada en un diván, abanico cerrado, observa la sala con ironía | Sonrisa lenta que por fin llega | Abanico golpeando la palma, mirada de párpado caído | Abre el abanico para ocultar la sonrisa |

---

## 7. Recuento y orden

| Paso | Imágenes |
|---|---|
| Originales formales (empezar por Dario) | 8 |
| Poses de ficha | 8 |
| Expresiones | 24 |
| **Total tanda 2 (elenco)** | **40** |

---

## 8. Primera prueba: Dario v1 (14 oct.)

**Color (medido):**
- Fondo: índice de amarillo **+0,7** → el bloque de control de color funcionó; **no hubo filtro global**.
- Blancos (corbatín, puños): **+15 a +18** → ChatGPT pinta el «blanco» como crema. El fondo gris no lo detecta.
- La corrección de ChatGPT con el código de Python dio el mismo resultado que el script (diferencia media 0,95 sobre 255): **ChatGPT ejecutó bien el filtro sin redibujar**.
- Nuevo modo `--blancos` en la herramienta: neutraliza sólo píxeles claros y poco saturados. Dario: blancos **+15,3 → +6,7**; piel, terciopelo y pelo sin cambios (±3). Resultado y comparación en `diseno/pruebas/`.
- Prompts actualizados: los blancos se piden «blanco frío como nieve recién caída, nunca crema ni marfil».

**Dirección de arte:**

| Aspecto | Valoración |
|---|---|
| Silueta (pelo largo atado, cinta, cuello largo, ciruela) | ✅ Se reconoce; funcionará en carta |
| Actuación (cortesía, mirada que llega tarde, gira el anillo) | ✅ Conseguida |
| Sin clichés de vampiro | ✅ |
| Rostro individual y atractivo | ✅ Alargado, párpados pesados |
| Formato | ❌ Salió **cuadrado** (1254 × 1254), no 2:3: se cortan cadera y manos bajas. Añadido «IMAGE FORMAT: vertical 2:3» a los 8 prompts |
| Hombros | ❌ Hombreras exageradas, más de los años 80 que de 1810. Corregido en el prompt de Dario |
| Técnica | ⚠️ Línea limpia y sombreado suave de ilustración digital: está más cerca del cómic occidental que de lo «hecho a mano». Hay que compararlo con las imágenes de Dressmaker que usan como referencia (no las he visto) y, si hace falta, pedir textura de pincel visible y bordes de pincel seco |
| Anillo | Menor: lo gira con la mano derecha; el prompt decía izquierda |

**Estado:** candidato. No aprobar la identidad hasta generar la versión 2:3 con los hombros corregidos.

### Análisis de técnica: Dressmaker frente a Dario v1

| Rasgo | Dressmaker | Dario v1 | Ajuste en el prompt |
|---|---|---|---|
| Línea | Hecha a mano, temblorosa, más gruesa en el contorno, a veces abierta o con trazos de construcción | Limpia, uniforme, casi negra | Línea temblorosa, contorno más grueso, gris-marrón |
| Pintura | Relleno plano + **una** sombra por material, bordes de pincel irregulares (gouache o rotulador) | Degradados suaves, terciopelo renderizado | Sin degradados ni brillos; una sombra por material |
| Rostro | Formas simples y con carácter: nariz simple, rubor en manchas, cejas expresivas | Semirrealista, «guapo de ilustración» | Formas simples, proporciones algo estilizadas |
| Proporción | Cabeza y pelo algo grandes, manos simplificadas | Realista, alargada | Estilización leve |
| Detalle | Estampados y encajes sugeridos con pocos trazos | Damasco del chaleco detallado | Sugerir, no renderizar |
| Personalidad | Objetos y gestos que cuentan (lápiz en el pelo, pájaro en el sombrero, abanico) | Gesto del anillo: bien | Mantener |

**Atractivo:** Dressmaker es más simpático que seductor. El atractivo de nuestro elenco debe venir del **diseño y la actuación** (silueta, mirada, gesto), no de un renderizado más realista.




## 9. Segunda prueba: Dario v2 (14 oct.)

**Color: resuelto desde el prompt.**
- Fondo (esquinas superiores): RGB 121,2 · 121,2 · 121,2, variación 0,5 → **perfectamente neutro y plano**. No es #808080 exacto, pero **lo que importa es que sea neutro y uniforme, no el valor**: así sirve para medir y se recorta o amplía sin costuras.
- Blancos: amarillo **+1,8** (v1: +15). El corbatín tiene sombras lila frías, como las referencias neutras de Dressmaker.
- La corrección casi no actúa (ganancias 1,000). Herramienta mejorada: el modo `--borde` descarta ahora el pelo y la ropa que tocan el borde (antes el abrigo contaminaba la medición: 111 en lugar de 121).

**Dirección de arte:**

| Aspecto | v2 | Acción |
|---|---|---|
| Formato | ✅ 1024 × 1536 (2:3) | — |
| Técnica | ⚠️ Mejor: terciopelo con sombras planas y manchadas. Siguen el rostro semirrealista, la línea casi negra y el damasco del chaleco muy detallado | Aceptable como candidata; afinar en v3 si se quiere más Dressmaker |
| Hombros | ❌ Siguen anchos: el contorno ocupa ~80 % del ancho | **Edición local** en ChatGPT (seleccionar hombros y mangas): «estrechar los hombros a una caída natural, sin hombreras», sin regenerar el resto |
| Encuadre | ❌ El pelo toca el borde superior (1,3 % en lugar de 6 %); ojos hacia el 10 % en lugar del 20 % | **Se corrige en posproducción**: como el fondo es neutro y plano, basta ampliar el lienzo por arriba con el mismo gris. No hace falta regenerar |
| Actuación y silueta | ✅ Mirada lateral, media sonrisa, gira el anillo (ahora en la mano izquierda), pelo largo atado | — |

**Estado:** candidata fuerte. Siguiente paso propuesto: edición local de hombros (y, opcionalmente, simplificar el damasco), ampliar lienzo superior y probarla montada en la carta.


---

## Anexo · Prompts completos del original formal (5.2–5.8)

Cada bloque está completo y se pega tal cual (no hay marcadores que sustituir).

### 5.2 Nilo Lobreda

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Nilo Lobreda, a 26-year-old man, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Broad shoulders, strong neck, broad jaw, thick dark brows, slightly broad straight nose, open warm face. Light olive skin tanned by mountain roads, flushed cheeks. Unruly dark brown loose curls to the ears.
COSTUME: Forest-green wool tailcoat slightly rumpled, oatmeal wool waistcoat with wooden buttons, linen shirt, loosely tied cravat.
ACTING: Trying to look formal for the occasion; a held-back smile escapes; one hand on his chest as if about to bow.
COLOUR KEY: forest green, oatmeal, white linen, tanned skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: warm, open silhouette (broad shoulders, unruly curls); sincerity; neutral colour.
```

### 5.3 Saúl Veyra

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Saúl Veyra, a 30-year-old man, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front three-quarter view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Tall, long neck, square shoulders, high cheekbones, defined jaw, calm dark eyes. Deep brown skin. Very short cropped black hair with a crisp hairline.
COSTUME: Steel-blue dress tailcoat with a high collar and silver buttons, impeccable white cravat, white gloves.
ACTING: Composed and reliable: hands behind his back, chin level, direct steady gaze; the stillness of someone who keeps his word.
COLOUR KEY: steel blue, silver, pure white, deep brown skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: upright silhouette and crisp hairline; contained warmth under discipline; neutral colour.
```

### 5.4 Teo Rovena

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Teo Rovena, a 24-year-old man, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Slim and restless, narrow face, very mobile arched brows, wide mouth. Fair skin with freckles and rosy cheeks. Messy copper hair going in every direction.
COSTUME: His only good tailcoat in dusty mauve-rose, slightly worn at the cuffs; discreet patterned waistcoat; loosely knotted cravat.
ACTING: Trying very hard to look serious and almost managing it: one corner of the mouth already rising, one eyebrow ahead of the joke.
COLOUR KEY: dusty mauve-rose, white shirt, copper hair, freckled fair skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: messy copper hair readable at small size; humour about to break; copper hair must not turn the image orange.
```

### 5.5 Celia Lobreda

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Celia Lobreda, a 21-year-old woman, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Petite, long neck, dancer's posture, round face, large eyes, small chin, thick dark brows. Fair rosy skin. Light brown hair in a high elaborate updo with a braided coronet and tiny green sprigs.
COSTUME: Sage-green high-waisted gown with vertical botanical embroidery in a deeper green, short puffed sleeves, long white gloves.
ACTING: Perfectly rehearsed: practised smile, chin slightly high, gloved hands folded at the waist.
COLOUR KEY: sage green, deeper green embroidery, white gloves, rosy fair skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: high updo silhouette; rehearsed perfection with a hint of nerves; neutral colour.
```

### 5.6 Irene Salvat

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Irene Salvat, a 25-year-old woman, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Tall, narrow shoulders, angular face, straight brows, attentive analytical eyes. Light-medium beige skin with a neutral undertone. Straight black hair in a plain low knot, no ornament. No glasses.
COSTUME: Slate-blue day dress of fine wool, long sleeves, small white collar, no jewellery.
ACTING: Studying the viewer as if reading a document: head slightly tilted, hands loosely together.
COLOUR KEY: slate blue, white collar, black hair, beige skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: plain low knot and angular face; total attention; neutral colour.
```

### 5.7 Isolda Marén

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Isolda Marén, a 26-year-old woman of the velario lineage, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front three-quarter view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Strong neck and shoulders, straight brows, a ready smile. Medium brown skin. Velaria traits: slate-green hair in loose half-up waves with a pearl-white streak at the front, muted copper irises. These traits do not change her skin, jaw or age.
COSTUME: Sea-green gown with a side fastening and a V neckline (a port tradition), a short open jacket she has not buttoned.
ACTING: Relaxed and amused, weight on one hip, looking straight at the viewer as if daring them to object.
COLOUR KEY: sea green, slate-green hair, pearl-white streak, muted copper eyes, medium brown skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: slate-green hair with pearl streak instantly readable; freedom; neutral colour.
```

### 5.8 Camila Ferrán

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create Camila Ferrán, a 29-year-old widow, as the formal portrait of a playable character in a narrative
mobile game set in Valcenda, a fictional capital with early-19th-century fashion.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
FRAMING: front three-quarter view, head to hip, centred. Top of head at 6% of the image height,
eyes at 20%, chin at 31%. Keep both hands inside the frame.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Full figure, short elegant neck, heavy-lidded eyes, a slow knowing smile. Deep brown skin. Dark coily hair arranged low at the nape.
COSTUME: Lavender-grey half-mourning silk gown with black lace trim, a narrow black mourning ribbon at the wrist embroidered with a single initial, a closed fan held in both hands.
ACTING: She has seen all this before: one eyebrow slightly raised, fan closed in both hands.
COLOUR KEY: lavender-grey, black lace, deep brown skin, dark hair.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes, jewels). Patterns, lace and
embroidery suggested with a few strokes, not rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats and gloves are bright cool white like
fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet or
deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: one character, no text, no frame, no other people.
REVIEW PRIORITIES: low coiled hair and full silhouette; experienced irony; neutral colour (lavender must not drift to beige).
```

---

## English summary

Critical review: the cast lacked defined skin diversity, house colours, period references for men's costume and confirmed sources for Dario's family detail; ages and per-character colours are now proposed and no visual trait hints at orientation. Yellow-cast research: there is no official switch, prompt colour words help inconsistently, re-prompting regenerates the image, and post-correction is the only reliable fix. Proposed four layers: avoid warm-trigger words, include a colour-control block, generate on flat neutral grey #808080, then run `herramientas/corregir_tono.py`, which measures the cast on the grey border and removes it from the whole image (test: yellow index +24.5 → 0.0), before removing the background. Ready-to-paste formal-portrait prompt for Dario and per-character blocks for the other seven, plus profile-pose and expression intents for all eight: 40 images.
