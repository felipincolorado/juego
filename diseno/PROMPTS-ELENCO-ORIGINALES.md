# Salverna · Prompts de los 8 originales formales (ChatGPT) — Propuesta v1

**13 de octubre de 2026 · PROPUESTA.** Prompts completos y listos para pegar, sin marcadores. Se generan **desde cero**, sin editar imágenes anteriores. Las poses vienen del [estudio de poses](<ESTUDIO-POSES-PERSONAJES.md>) y la identidad de [encargos del elenco](<ENCARGOS-ELENCO-TANDA-2.md>) §3, con los ajustes de abajo. Ningún personaje queda aprobado por generarse.

## Cómo usarlos

1. **Un chat nuevo por personaje**, para que no se mezclen rasgos entre ellos.
2. **Adjuntar sólo las dos referencias neutras de Dressmaker:** la chica del vestido blanco y la chica del vestido verde agua con abanico. Nunca adjuntar a otro personaje del elenco.
3. Pegar el prompt entero.
4. **Si el resultado no sirve, regenerar desde cero con el mismo prompt.** No pedir arreglos sobre la imagen: cada edición pierde la mano del dibujo.
5. **Revisar:** cara visible, pose legible en la mitad superior, manos simples, fondo transparente y blancos sin crema. Si los blancos salen crema: `python herramientas/corregir_tono.py imagen.png --solo-blancos 0.85`.
6. **Prueba final:** la carta (mitad superior y centro de la imagen) a tamaño de teléfono y las 8 siluetas juntas.

## Ajustes respecto a los prompts anteriores (autocrítica)

| Problema detectado | Cambio |
|---|---|
| Dario: el chaleco con damasco salía demasiado detallado | Chaleco negro **liso, sin dibujo** |
| Teo: chaleco estampado (el mismo riesgo) y «camisa blanco crema», que choca con el control de color | Chaleco **gris claro liso**, camisa blanca pura |
| Camila: la inicial bordada en la cinta es texto diminuto y difícil; el abanico iba «en las dos manos», en contradicción con la pose | Cinta **lisa**; abanico en **una** mano, en vertical contra el pecho |
| Isolda: la palabra «velaria» no significa nada para el generador | Se describen sólo los rasgos visibles |
| «Playable character»: el elenco no se juega, se gestiona | «One of eight cast members» |
| Los porcentajes exactos el generador no los mide | Se dice «busto hasta la cadera, margen pequeño sobre el pelo» y los porcentajes van como «aproximadamente» |
| «Review priorities» era una nota para nosotros | Pasa a «MUST READ AT A GLANCE»: lo que debe leerse de un vistazo |
| Brillos en «jewels»: invitaba a añadir joyas | Brillos sólo en el pelo y los ojos |

---

## 1. Dario Miravés · Mística

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Dario Miravés, a 27-year-old man.
FRAMING: Three-quarter view: body turned about 40° to his left, face towards the viewer.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Slender build, long neck, long face, heavy-lidded grey eyes, fine straight nose.
Pale olive skin with a cool undertone. Long straight black hair tied low at the nape with
a dark ribbon. Nothing supernatural: no fangs, no red eyes, no vampire costume.
COSTUME: Deep plum velvet tailcoat with a high collar; plain black waistcoat with no
pattern; crisp white cravat with one small garnet pin. Clean, precise tailoring with
natural, fairly narrow early-19th-century shoulders: no padded or puffed shoulders.
No rings, nothing in his hands.
ACTING AND POSE: Perfect courtesy hiding a closed door. Chin slightly lowered, heavy-lidded gaze
arriving at the viewer a moment late, a faint half-smile that does not reach the eyes.
His long tied hair falls forward over the near shoulder onto his chest. Arms relaxed at
his sides; hands low and simple.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Plum, black, pure white linen, pale olive skin, grey eyes.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Long tied hair over the shoulder; long neck; mystery without vampire clichés.
```

## 2. Nilo Lobreda · Cálido-franco

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Nilo Lobreda, a 26-year-old man.
FRAMING: Front view.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Broad shoulders, strong neck, broad jaw, thick dark brows, slightly broad straight
nose, open warm face. Light olive skin tanned by mountain roads, flushed cheeks. Unruly
dark brown loose curls to the ears.
COSTUME: Forest-green wool tailcoat, slightly rumpled; oatmeal wool waistcoat with a few
simple wooden buttons; white linen shirt; loosely tied white cravat.
ACTING AND POSE: Warm and frank, trying to look formal for the occasion: leaning slightly towards
the viewer, a held-back smile escaping, one flat hand resting on his chest as if
beginning a bow.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Forest green, oatmeal, pure white linen, tanned skin, dark brown curls.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Broad, open silhouette; unruly curls; sincerity.
```

## 3. Saúl Veyra · Segura

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Saúl Veyra, a 30-year-old man.
FRAMING: Front view, perfectly symmetrical: the only symmetrical pose of the cast.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Tall, long neck, square shoulders, high cheekbones, defined jaw, calm dark eyes.
Deep brown skin. Very short cropped black hair with a crisp hairline.
COSTUME: Steel-blue dress tailcoat with a high collar and silver buttons (not gold),
impeccable white cravat, white gloves.
ACTING AND POSE: Composed and reliable: chin level, calm direct gaze, square relaxed shoulders,
hands clasped behind his back (not visible). The stillness of someone who keeps his word,
with contained warmth in the eyes.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Steel blue, silver, pure white, deep brown skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Upright, symmetrical column; crisp hairline; discipline with warmth.
```

## 4. Teo Rovena · Bromista

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Teo Rovena, a 24-year-old man.
FRAMING: Three-quarter view: body turned about 40° to his right, face towards the viewer.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Slim and restless, narrow face, very mobile arched brows, wide mouth. Fair skin
with freckles and rosy cheeks. Messy copper hair going in every direction.
COSTUME: His only good tailcoat, in dusty mauve-rose, slightly worn at the cuffs; plain
pale grey waistcoat; white shirt; loosely knotted white cravat.
ACTING AND POSE: Trying very hard to look serious and almost managing it: head tilted the opposite
way to his body, shoulders slightly raised, one eyebrow up, one corner of the mouth
escaping into a grin. One fist gripping his own lapel; the other arm relaxed.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Dusty mauve-rose, pale grey, pure white shirt, copper hair, freckled fair skin. The copper hair must not turn the image orange.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Messy copper hair readable at small size; humour about to break.
```

## 5. Celia Lobreda · Ensayada

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Celia Lobreda, a 21-year-old woman.
FRAMING: Slight three-quarter view: body turned about 20°, face towards the viewer.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Petite, long neck, dancer's posture, round face, large eyes, small chin, thick
dark brows. Fair rosy skin. Light brown hair in a high elaborate updo with a braided
coronet and a few tiny green sprigs.
COSTUME: Sage-green high-waisted gown with vertical botanical embroidery in a deeper green
(suggested with a few strokes), short puffed sleeves, long white gloves.
ACTING AND POSE: Perfectly rehearsed: chin slightly high, long neck, practised smile with a hint of
nerves in the eyes, gloved hands folded at the waist.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Sage green, deeper green, pure white gloves, rosy fair skin, light brown hair.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Tall updo and long neck; rehearsed perfection with a hint of nerves.
```

## 6. Irene Salvat · Analítica

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Irene Salvat, a 25-year-old woman.
FRAMING: Front view (a slight turn is fine).
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Tall, narrow shoulders, angular face, straight brows, attentive analytical eyes.
Light-medium beige skin with a neutral undertone. Straight black hair in a plain low knot,
no ornament. No glasses.
COSTUME: Slate-blue day dress of fine wool, long sleeves, small white collar, no jewellery.
ACTING AND POSE: Studying the viewer as if reading a document: head tilted, attentive gaze, the
ghost of a smile when she finds something interesting. Arms crossed at chest height with
the hands tucked away (not visible).
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Slate blue, pure white collar, black hair, beige skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Plain low knot and angular face; total attention.
```

## 7. Isolda Marén · Empoderada

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Isolda Marén, a 26-year-old woman.
FRAMING: Three-quarter view: body turned about 40° to her left, face towards the viewer.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Strong neck and shoulders, straight brows, a ready smile. Medium brown skin.
Slate-green hair in loose half-up waves with a pearl-white streak at the front; muted
copper irises. The hair and eye colour are natural to her and do not change her skin,
jaw or age.
COSTUME: Sea-green gown with a side fastening and a V neckline (a port tradition), a short
open jacket she has not buttoned.
ACTING AND POSE: Relaxed and challenging: head tilted, direct gaze, a smile that dares the viewer
to object; near shoulder dropped, shoulders open, weight on one hip, one fist on the hip.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Sea green, slate-green hair, pearl-white streak, muted copper eyes, medium brown skin.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Slate-green hair with pearl streak instantly readable; freedom.
```

## 8. Camila Ferrán · Matriarca irónica

```text
ROLE: You are a senior character designer for a hand-illustrated narrative mobile game.
TASK: NEW ORIGINAL CHARACTER, DRAWN FROM SCRATCH. Do not edit or reuse any previous image.
WORLD: Valcenda, a fictional capital with early-19th-century fashion (high-waisted gowns,
tailcoats, cravats). The character is one of eight cast members of a matchmaking season.
ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
They do not supply face, clothes, pose or colour.
CHARACTER: Camila Ferrán, a 29-year-old widow.
FRAMING: Three-quarter view: body turned about 40° to her right, face towards the viewer.
Head-to-hip portrait, centred, cut at the hips. Leave a small margin above the hair:
top of head at about 6% of the image height, eyes at about 20%, chin at about 31%.
The face is always fully visible and turned towards the viewer; never seen from behind.
IMAGE FORMAT: vertical portrait 2:3 (1024 × 1536), not square.
IDENTITY: Full figure, short elegant neck, heavy-lidded eyes, a slow knowing smile. Deep
brown skin. Dark coily hair arranged low at the nape.
COSTUME: Lavender-grey half-mourning silk gown with black lace trim (suggested with a few
strokes), a narrow plain black mourning ribbon tied at the wrist, a closed fan.
ACTING AND POSE: She has seen all this before: head level, heavy-lidded eyes, one eyebrow raised,
a slow knowing smile. The closed fan is held upright against her chest in her whole hand,
like a simple bar.
POSE RULES: the personality must read in the upper half of the image (head, neck,
shoulders, chest), because the game card shows only that part. Use big, clear body
language: head tilt, shoulder line, gaze direction, arm shape.
Hands are simple shapes: hidden, fists, or flat on the body. No small objects held
between the fingers, no rings, no pointing fingers, no interlaced visible fingers.
At most one large prop, held in the whole hand.
COLOUR KEY: Lavender-grey, black lace, deep brown skin, dark hair. The lavender must stay cool and never drift to beige.
TECHNIQUE (hand-made look of the attached references):
Hand-drawn ink line with a slight wobble, heavier on the outer silhouette, thinner and
sometimes broken inside; line colour dark grey-brown, softer than pure black.
Flat local colour fills with ONE simple shadow shape per material; shadow edges soft and
slightly patchy, like gouache or marker on paper. Almost no gradients: no airbrush,
no smooth rendering, no glossy velvet or satin effects.
Highlights only as a few graphic shapes (hair, eyes). Fabric patterns, lace and
embroidery suggested with a few strokes, never rendered in detail.
Face built from simple, characterful shapes: simple nose, small blush patches, expressive
brows, individual features. Slightly stylised proportions (head and hair a little large),
neither realistic nor anime. Hands simplified but readable.
Whites have cool lilac-grey shadows.
No 3D render, no photographic detail, no uniform vector look, no global grain.
COLOUR CONTROL (critical):
Neutral daylight white balance (D65, 6500 K). This is a contemporary illustration,
not an old painting or an old photograph.
Whites are pure neutral white (linen, cravats, collars and gloves are bright cool white
like fresh snow, never cream or ivory); greys are neutral; shadows are cool grey-violet
or deep blue-grey, never brown or amber. Paint each material in its own local colour;
do not unify the image with any overall tone.
NO yellow, orange, amber, sepia, golden or brown overall tint. NO aged paper,
varnish or vintage grading.
BACKGROUND: fully transparent PNG. No background, no floor, no cast shadow,
no white halo around the silhouette.
OUTPUT: exactly one character, no text, no lettering, no frame, no other people.
MUST READ AT A GLANCE: Low coiled hair and full silhouette; experienced irony.
```
