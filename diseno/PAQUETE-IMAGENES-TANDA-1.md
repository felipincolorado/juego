# Salverna · Paquete de imágenes — Tanda 1 (entorno e interfaz)

**14 de octubre de 2026 · Encargos listos para generar en ChatGPT (modelo de imagen) y devolver para montaje en Figma.**
Sigue la [guía de prompts](<../GUIA-PROMPTS-Y-GENERACION-PERSONAJES-SALVERNA.md>) (técnica, color local, sin veladura amarilla) y la [especificación v3](<ESPEC-FLUJO-PANTALLAS-v3.md>). Ninguna imagen queda aprobada por existir: cada una se revisa montada en la pantalla, a tamaño de teléfono.

---

## 1. Decisiones de la carta de personaje (cerradas para producir)

| Pregunta | Decisión | Por qué |
|---|---|---|
| ¿Redondeada o cuadrada? | **Arco arriba, esquinas casi rectas abajo** (radio superior = mitad del ancho; inferior 6 dp) | El arco es miniatura de época y ventana georgiana (el mismo motivo de la colección de libros de referencia). Un rectángulo redondeado parece botón de app; uno recto parece carta de estrategia. El arco es identidad propia y sigue leyéndose como carta. |
| Proporción | Vertical **2:3**, 112 × 168 dp | El busto es vertical; la cabeza y los hombros caben sin recortar. |
| Nombre | **Franja completa abajo, sobre los hombros**, 26 dp de alto, texto centrado | Decidido por el usuario: no corta el retrato y se lee como placa. |
| Color de la franja | **Color de la casa** del personaje, con filete de oro fino arriba y texto marfil | Identidad por color, como los lomos de los libros; evita que las ocho cartas sean iguales. |
| Fondo dentro del arco | **Lavado pintado suave del color de la casa**, más claro arriba | El busto viene transparente; el fondo da identidad sin estampados. |
| Marco | Filete de oro de 3 dp + filete interior claro de 1 dp | Lámina dorada fina, no relleno. |
| Estado ocupado | **Velo marfil translúcido** + emblema del lugar (no blanco y negro) | Sobre ilustración el blanco y negro parece foto antigua; el velo conserva al personaje. Se valida con el arte real. |
| Estado seleccionado | La carta **se levanta** sobre la mano y gana un halo cálido | Gesto de sacar una carta de la mano. |
| Estado alterado | Banda superior frambuesa con una palabra | Único estado con texto. |

Estas cartas usan los recortes de la ilustración maestra (regla de encuadre: ojos al 20 % del alto). Los personajes se generan en la **tanda 2**, cuando existan sus fichas.

---

## 2. Inventario completo de imágenes (todas las tandas)

| Tanda | Grupo | Imágenes | Estado |
|---|---|---|---|
| **1** | Mapa: completo de día, plancha limpia sin edificios de lugar, 6 edificios aislados | 8 | **Este documento** |
| **1** | Guirnalda floral superior (marco del mapa) | 1 | **Este documento** |
| **1** | Ramillete de esquina para cartas y hojas | 1 | **Este documento** |
| **1** | Papel marfil (textura) | 1 | **Este documento** |
| **1** | Portada (ilustración sin texto) | 1 | **Este documento** |
| 2 | Elenco social: 8 personas × 4 expresiones (neutral, alegre, molesta, ruborizada) | 32 | Bloqueado: faltan fichas de los ocho |
| 2 | Reina (base + 2) y guía/secretaria (base + 3) | 7 | Bloqueado: faltan fichas |
| 3 | Grabados de cabecera de carta (6 casas + Corona) | 7 | Tras tanda 1 |
| 3 | Fondo de carta por casa (lavado pintado) | 6 | Puede hacerse en motor; generar sólo si no convence |
| 3 | Cabecera de la Crónica | 1 | Tras tanda 1 |
| 3 | Pétalos sueltos (partículas, 4 formas) | 1 hoja | Tras tanda 1 |
| Opcional | Balaustrada inferior | 1 | Sólo si se elige la opción B |

**No se generan:** iconos, sellos, radar, rutas, aros, textos, fichas de almanaque, marcos simples. Son vectores o motor.

---

## 3. Cómo trabajar con ChatGPT (método de capas)

### 3.1 Tamaños reales del generador

El modelo entrega **1024 × 1024, 1024 × 1536 (vertical) o 1536 × 1024 (horizontal)**. Los objetivos de la especificación (por ejemplo, mapa 2340 × 3000) se alcanzan **después**: escalado ×2–3 con un escalador que conserve el trazo (Krita, Real-ESRGAN, Topaz u otro) y revisión visual. No pedir tamaños imposibles en el prompt.

### 3.2 El truco de las capas (imagen completa → piezas idénticas)

1. **Generar la escena completa** (mapa con todo).
2. **Plancha limpia:** editar *esa misma imagen* pidiendo quitar los edificios de lugar y pintar el suelo, la vegetación y las calles que había debajo. Sin esto, al mover o iluminar un edificio aparecería un hueco o un duplicado.
3. **Piezas aisladas:** editar *esa misma imagen completa* (no la plancha) pidiendo reproducir **sólo un edificio**, idéntico en posición relativa, perspectiva, escala, luz y pintura, sobre **fondo realmente transparente**.
4. **Comprobar en Figma:** superponer el PNG sobre la imagen completa con 50 % de opacidad. Si no coincide, se corrige la pieza; no se acepta «parecido».

**Límite honesto:** el generador no garantiza identidad de píxel. Las piezas pueden desplazarse o variar detalles. Por eso la comprobación del paso 4 es obligatoria, y a veces conviene recortar el edificio a mano de la imagen completa (Krita/Photoshop) y usar el generador sólo para la plancha limpia.

### 3.3 Transparencia

- Pedir siempre «true transparent background (alpha channel), PNG».
- Comprobar el canal alfa sobre fondo claro **y** oscuro: a veces entrega un damero dibujado o un halo blanco.
- Si falla: quitar fondo después (rembg, Krita, Photoshop, eliminar fondo de Figma) y revisar bordes.

### 3.4 Adjuntos

Para entorno e interfaz, adjuntar sólo los **originales ilustrados de técnica** (`imgi_28_latest.webp`, `imgi_26_1000 (3).webp`, `imgi_161_latest.webp`) con su rol declarado: enseñan línea y pintura, no contenido. No adjuntar los pósters de Bridgerton: son referencia de principios, no de imagen (y su arco de glicinia es muy reconocible).

### 3.5 Registro de cada entrega (guía §11)

ID del recurso · prompt exacto · adjuntos y rol · tamaño real recibido · estado (candidato / revisado / aprobado / rechazado + causa) · prueba de alfa · captura del montaje.

---

## 4. Bloque de estilo común de entorno

Este bloque se pega dentro de cada prompt de la tanda 1. Extiende la técnica de la guía de personajes al entorno.

**EN (pegar):**
```text
STYLE — SALVERNA ENVIRONMENT:
Handcrafted illustration for a narrative mobile game. Pressure-varied ink lines,
slightly irregular, always darker than the material they outline (brown-grey on stone,
deep green on foliage, slate on roofs). Broad matte gouache-like paint shapes with
few structural shadows and quiet surfaces; texture only in small local areas.
Local colour painted independently per material. Morning light, soft and cool-neutral.
NO yellow, orange or sepia glaze over the image. NO photographic detail, NO 3D render,
NO glossy plastic surfaces, NO uniform vector look, NO global grain or noise.
Palette: natural greens and blues of a living city, warm-ivory and pale pastel
façades (powder blue, blush, pale sage, cream), slate-lilac roofs, flowering trees,
small accents of wisteria lilac and rose. Pastel is air and light, not a wash over everything:
keep real darks (ink, deep foliage, window openings) for contrast.
Fictional world: no real landmarks, no text, no signs, no heraldry from real families.
```

**ES (equivalente):**
Ilustración artesanal para juego narrativo móvil. Línea de tinta con presión variable, algo irregular, siempre más oscura que su material. Manchas mate amplias tipo gouache, pocas sombras estructurales, superficies tranquilas; textura sólo localizada. Color local por material. Luz de mañana suave, neutra-fría. Sin veladura amarilla, naranja ni sepia; sin detalle fotográfico, render 3D, plástico, vector uniforme ni grano general. Verdes y azules naturales, fachadas marfil y pasteles pálidos, tejados pizarra lila, árboles en flor, pequeños acentos glicinia y rosa. El pastel es aire y luz, no un velo sobre todo: conservar oscuros reales. Mundo ficticio: sin monumentos reales, textos, letreros ni heráldica real.

---

## 5. Encargos de la tanda 1

### MAP-01 · Mapa de Valcenda completo, de día

- **Uso:** fondo principal del juego; se desplaza en vertical y algo en horizontal.
- **Generar:** 1024 × 1536 (vertical). **Objetivo tras escalar:** 2340 × 3000 aprox. (recorte final a definir al montar).
- **Fondo:** opaco.
- **Adjuntos:** 3 originales de técnica.

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL ENVIRONMENT ILLUSTRATION FROM SCRATCH.
Create the city of Valcenda for a portrait mobile game map: the main screen where the
player sees events on buildings and small character tokens travelling along streets.

ATTACHMENTS: the attached illustrations teach line and paint behaviour only.
Do not copy their subjects, composition or colours.

VIEW: elevated oblique bird's-eye view (about 45°), one consistent camera and scale
for every building. Portrait composition. Readable streets wide enough for small
portrait tokens. Leave calm areas (plazas, lawns, river surface) where UI markers can sit.
Keep the top 12% and bottom 22% of the image visually quiet (rooftops, gardens, water),
because interface elements will cover them.

CITY: a Regency-era-inspired fictional capital on firm river terraces. A wide calm river
(the Lumbre) crosses the upper third with an elegant stone bridge. Terraced townhouses
in pale pastel façades, crescents and squares, cobbled streets, small carriages.
SIX distinct venue buildings, clearly separated from neighbours by streets or gardens,
each with a recognisable silhouette:
1. Assembly ballroom: long neoclassical hall with tall arched windows and a portico.
2. Garden villa with formal gardens, hedges, a fountain and a glasshouse (Serravalle gardens).
3. Theatre: round domed building with a colonnade.
4. Residence: an elegant corner townhouse with a small private garden (the matchmaker's home).
5. Academy: a modest classical building with a courtyard and a small cupola.
6. Royal palace (Alto Laurel): larger, on the highest terrace, partly visible at an edge.
Flowering trees (pink and white), climbing wisteria on a few walls, autumn hints
(a few amber trees) because the season is early autumn.

{STYLE — SALVERNA ENVIRONMENT block}

OUTPUT: single opaque illustration, no text, no labels, no UI, no frame, no people larger
than tiny distant figures.

REVIEW PRIORITIES: six venue buildings instantly distinguishable at phone size;
consistent perspective; no yellow cast.
```

**ES (resumen equivalente):** dibujo original desde cero de Valcenda en vista oblicua elevada (~45°), cámara y escala únicas, composición vertical. Río ancho con puente de piedra en el tercio superior; casas adosadas pastel, plazas, calles empedradas. Seis edificios de lugar bien separados y reconocibles: salón de baile neoclásico, villa con jardines formales (Serravalle), teatro redondo con cúpula, residencia de esquina con jardín, academia con patio y cúpula pequeña, palacio en la terraza más alta. Árboles en flor y toques de otoño. Zonas tranquilas para marcadores; franja superior (12 %) e inferior (22 %) calmas. Sin texto ni interfaz. Prioridades: edificios distinguibles, perspectiva coherente, sin tono amarillo.

### MAP-02 · Plancha limpia (sin los seis edificios)

- **Uso:** capa base bajo los edificios, para poder iluminarlos, animarlos o cambiarlos.
- **Generar:** editar MAP-01 aprobado, mismo tamaño. **Fondo:** opaco.
- **Adjuntos:** únicamente MAP-01.

**EN (pegar):**
```text
EDIT OF THE ATTACHED IMAGE. The attached illustration is the sole visual authority.
Remove ONLY these six buildings: the ballroom, the garden villa with its glasshouse,
the domed theatre, the corner residence, the academy and the palace.
In their place paint plausible continuous ground: paving, lawns, garden paths and
low hedges that match the surroundings, as if the plots were empty courtyards.
Keep EVERYTHING else pixel-faithful: camera, scale, every other building, river,
bridge, trees, colours, line and paint. Same canvas size and framing. No text.
```

**ES:** edición de MAP-01: quitar sólo los seis edificios de lugar y pintar en su sitio suelo continuo creíble (pavimento, césped, caminos, setos bajos). Conservar todo lo demás idéntico: cámara, escala, edificios, río, puente, árboles, color, línea y pintura. Mismo lienzo.

### MAP-03 a MAP-08 · Edificios aislados (uno por encargo)

- **Uso:** capa superior de cada lugar (se ilumina al seleccionar, puede tener animación sutil: banderolas, ventanas encendidas al atardecer).
- **Generar:** editar MAP-01 aprobado, mismo tamaño de lienzo; luego recortar el área útil. **Fondo:** transparente.
- **Adjuntos:** únicamente MAP-01.
- IDs: `MAP-03 salón de baile` · `MAP-04 villa y jardines` · `MAP-05 teatro` · `MAP-06 residencia` · `MAP-07 academia` · `MAP-08 palacio`.

**EN (pegar, cambiando {building}):**
```text
EDIT OF THE ATTACHED IMAGE. The attached illustration is the sole visual authority.
Keep ONLY {building} — the {short description and location, e.g. "domed round theatre
with a colonnade, lower right"} — exactly as it appears: same position on the canvas,
same perspective, scale, lighting, colours, ink line and paint. Include its own steps,
railings and the small garden or forecourt that belongs to it, nothing else.
Remove everything else and make it TRUE TRANSPARENT background (alpha), PNG.
Do not redraw, restyle, clean up or improve the building. No shadow plate, no ground
beyond its own plot, no text.
```

**ES:** edición de MAP-01: conservar sólo {edificio} exactamente igual (misma posición en el lienzo, perspectiva, escala, luz, color, línea y pintura), con su escalinata, rejas y su pequeño patio; eliminar el resto con fondo realmente transparente. No redibujar ni mejorar.

**Comprobación obligatoria:** superponer en Figma sobre MAP-01 al 50 %; si no coincide, recortar a mano de MAP-01.

### UI-01 · Guirnalda floral superior

- **Uso:** cuelga del borde superior del mapa; enmarca la ciudad y da fondo legible a las fichas de almanaque (sustituye a la franja superior). Se mece levemente.
- **Generar:** 1536 × 1024 (horizontal). Se usará la franja superior ~1536 × 420. **Fondo:** transparente.
- **Adjuntos:** 3 originales de técnica.

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL DECORATIVE ELEMENT FROM SCRATCH.
A horizontal hanging garland to frame the TOP EDGE of a mobile game screen.
Clusters of lilac wisteria mixed with small climbing roses (blush and ivory) and
fresh green leaves, hanging from a thin unseen line along the top edge.
Asymmetric and organic: denser and longer at the left and right corners (hanging down
to about 40% of the image height), very sparse and short across the centre
(only small leaves and a few blossoms, under 12% of the height) so the centre stays clear.
Must not look like a copy of any film or series poster: no arch, no symmetry.
Seen from slightly below, soft morning light.

{STYLE — SALVERNA ENVIRONMENT block}

OUTPUT: isolated element on TRUE TRANSPARENT background (alpha), PNG. No sky, no wall,
no text, no frame. Edges of petals clean, no white halo.
REVIEW PRIORITIES: clear centre; painted (not photographic) flowers; real transparency.
```

**ES:** guirnalda horizontal para el borde superior: glicinia lila con rosas trepadoras pequeñas (rosa pálido y marfil) y hojas verdes; asimétrica, densa y larga en las esquinas (hasta 40 % del alto), muy escasa en el centro (menos del 12 %). Sin arco ni simetría, sin parecer póster de serie. Fondo transparente real, sin halo.

### UI-02 · Ramillete de esquina

- **Uso:** esquinas de cartas, hojas de invitación y Crónica (se refleja para las otras esquinas).
- **Generar:** 1024 × 1024. **Fondo:** transparente.

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL DECORATIVE ELEMENT FROM SCRATCH.
A small corner spray for stationery: a sprig of wisteria and one small rose with
three leaves, growing diagonally from the TOP-LEFT corner towards the centre,
occupying only the top-left 45% of the canvas; the rest empty.
Delicate and light, like a painted motif on fine writing paper.

{STYLE — SALVERNA ENVIRONMENT block}
Simplified for small display: fewer, clearer shapes than a botanical study.

OUTPUT: TRUE TRANSPARENT background (alpha), PNG, no paper, no text, no frame.
```

**ES:** ramillete de esquina: una rama de glicinia y una rosa pequeña con tres hojas, en diagonal desde la esquina superior izquierda, ocupando sólo el 45 % superior izquierdo. Delicado, simplificado para tamaño pequeño. Transparente.

### UI-03 · Papel marfil

- **Uso:** superficie de hojas, cartas y Crónica (9 zonas en motor).
- **Generar:** 1024 × 1024. **Fondo:** opaco (es la propia textura).

**EN (pegar):**
```text
A seamless, tileable texture of fine ivory writing paper (#FBF7F0 average), very subtle:
faint cotton fibres and gentle tonal variation only. Flat and evenly lit, no shadows,
no folds, no stains, no vignette, no yellowing, no visible pattern repetition.
Must stay quiet behind 16 px text. OUTPUT: opaque PNG, edges tile seamlessly.
```

**ES:** textura continua de papel marfil fino (media #FBF7F0), muy sutil: fibras y leve variación tonal; sin sombras, pliegues, manchas, viñeta ni amarilleo. Debe quedar tranquila detrás de texto de 16 px. Bordes repetibles.

### KEY-01 · Portada

- **Uso:** pantalla de inicio. El título y los botones se ponen en Figma encima.
- **Generar:** 1024 × 1536. **Objetivo tras escalar:** 1290 × 2796 con zona segura central. **Fondo:** opaco.
- **Adjuntos:** 3 originales de técnica (y MAP-01 aprobado como referencia de lugar, si existe).

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL KEY ART FROM SCRATCH.
Title-screen illustration for a portrait mobile game about a matchmaker during the
social season of Valcenda, a fictional Regency-inspired capital.
COMPOSITION (three depth planes): foreground — hanging wisteria and roses at the top
corners and a stone balustrade at the bottom edge; middle — an empty terrace with an
open folding fan and a sealed letter with a rose wax seal resting on the balustrade;
background — the city of Valcenda at early-morning light with the river and stone
bridge, softly lit. NO people (characters are added later as separate art).
Keep the centre band (from 35% to 60% of the height) calm and low in detail for the
game title; keep the bottom 25% darker and simple for buttons.
Strong value contrast near the letter and fan (deep ink shadows, clean whites);
pastel only in sky and blossoms.

{STYLE — SALVERNA ENVIRONMENT block}

OUTPUT: single opaque illustration, no text, no logo, no frame.
REVIEW PRIORITIES: calm title band; letter and fan as focal point; no yellow cast.
```

**ES:** ilustración de portada sin personas: delante, glicinias y rosas colgando en las esquinas superiores y una balaustrada de piedra abajo; en medio, una terraza con un abanico abierto y una carta lacrada (sello rosa) sobre la balaustrada; al fondo, Valcenda con río y puente a primera hora. Franja central (35–60 % del alto) tranquila para el título; 25 % inferior más oscuro y simple para botones. Contraste fuerte en carta y abanico; pastel sólo en cielo y flores. Sin texto.

---

## 6. Orden de trabajo recomendado

1. **MAP-01** → lo monto en Figma y revisamos juntos a tamaño teléfono con marcadores y cartas.
2. Si se aprueba: **MAP-02** y **MAP-03…08** (capas).
3. En paralelo: **UI-01, UI-02, UI-03** (independientes del mapa).
4. **KEY-01** cuando el mapa esté aprobado (comparten lugar y luz).
5. Mientras tanto, se escriben las **fichas del elenco social** para desbloquear la tanda 2. Para probar el formato de la carta antes, puede usarse una base ya aprobada (Leonora t48).

Subir cada resultado aquí o al repositorio con su ID en el nombre del archivo (por ejemplo `MAP-01_v1.png`).

---

## English summary

Batch 1 covers environment and UI only, because the eight social-season characters have no design sheets yet (the project guide forbids generating characters without them). Card decisions are fixed: arched top with near-square bottom corners, 2:3, full-width name bar over the shoulders in the character's house colour, painted house-colour wash behind a transparent bust, ivory veil for busy, lift for selected. The image model outputs 1024×1024, 1024×1536 or 1536×1024; targets are reached by trait-preserving upscaling. Layer method: generate the full map, edit it into a clean plate without the six venue buildings, then edit the full map into one transparent PNG per building, and verify each by 50 % overlay in Figma (hand-cut from the full map if it does not align). Prompts (EN to paste, ES equivalent) are provided for the full map, clean plate, six building cut-outs, top floral garland, corner spray, ivory paper texture and title key art, each with a shared environment style block (handcrafted line, matte gouache, local colour, no yellow glaze, pastel as air not as wash).
