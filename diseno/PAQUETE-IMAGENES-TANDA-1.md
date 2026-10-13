# Salverna · Paquete de imágenes — Tanda 1 (entorno e interfaz)

**14 de octubre de 2026 · Encargos listos para generar en ChatGPT (modelo de imagen) y devolver para montaje en Figma.**
Sigue la [guía de prompts](<../GUIA-PROMPTS-Y-GENERACION-PERSONAJES-SALVERNA.md>) (técnica, color local, sin veladura amarilla) y la [especificación v3](<ESPEC-FLUJO-PANTALLAS-v3.md>). Ninguna imagen queda aprobada por existir: cada una se revisa montada en la pantalla, a tamaño de teléfono.

---

## 1. Propuesta de carta de personaje (pendiente de aprobación)

| Pregunta | Propuesta | Por qué |
|---|---|---|
| ¿Redondeada o cuadrada? | **Arco arriba, esquinas casi rectas abajo** (radio superior = mitad del ancho; inferior 6 dp) | El arco es miniatura de época y ventana georgiana (el mismo motivo de la colección de libros de referencia). Un rectángulo redondeado parece botón de app; uno recto parece carta de estrategia. El arco es identidad propia y sigue leyéndose como carta. |
| Proporción | Vertical **2:3**, 112 × 168 dp | El busto es vertical; la cabeza y los hombros caben sin recortar. |
| Nombre | **Franja completa abajo, sobre los hombros**, 26 dp de alto, texto centrado | Indicación del usuario sobre la maqueta: no corta el retrato y se lee como placa. Falta verla con arte real. |
| Color de la franja | **Color de la casa** del personaje, con filete de oro fino arriba y texto marfil | Identidad por color, como los lomos de los libros; evita que las ocho cartas sean iguales. |
| Fondo dentro del arco | **Lavado pintado suave del color de la casa**, más claro arriba | El busto viene transparente; el fondo da identidad sin estampados. |
| Marco | Filete de oro de 3 dp + filete interior claro de 1 dp | Lámina dorada fina, no relleno. |
| Estado ocupado | **Velo marfil translúcido** + emblema del lugar (no blanco y negro) | Sobre ilustración el blanco y negro parece foto antigua; el velo conserva al personaje. Se valida con el arte real. |
| Estado seleccionado | La carta **se levanta** sobre la mano y gana un halo cálido | Gesto de sacar una carta de la mano. |
| Estado alterado | Banda superior frambuesa con una palabra | Único estado con texto. |

**Estado:** ninguna de estas propuestas está aprobada. Se contrastan con las decisiones registradas del proyecto y se validan montadas en Figma a tamaño de teléfono.

Estas cartas usan los recortes de la ilustración maestra (regla de encuadre propuesta: ojos al 20 % del alto). Los personajes se generan en la **tanda 2**, cuando existan sus fichas.

**Prueba de formato con Leonora t48:** puede usarse para comprobar encuadre, recorte y lectura de la carta, **identificada en Figma como «personaje de prueba»**. Eso no la convierte en candidata del elenco social ni le asigna papel romántico.

---

## 2. Inventario completo de imágenes (todas las tandas)

| Tanda | Grupo | Imágenes | Estado |
|---|---|---|---|
| **1** | Mapa: completo de día, plancha limpia sin edificios de lugar, 6 edificios aislados | 8 | **Este documento** |
| **1** | Guirnalda floral superior (marco del mapa) | 1 | **Este documento** |
| **1** | Ramillete de esquina para cartas y hojas | 1 | **Este documento** |
| **1** | Papel marfil (textura) | 1 | **Este documento** |
| **1** | Portada (ilustración sin texto) | 1 | **Este documento** |
| 2 | Elenco social: 8 personas × 5 (original formal amplio del que se recorta la carta · pose de ficha editada desde ese original · 3 expresiones desde el original) | 40 | Propuesta de reparto en [ELENCO-TEMPORADA-PROPUESTA.md](<ELENCO-TEMPORADA-PROPUESTA.md>); pendiente de aprobación |
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

Los formatos habituales del modelo son **1024 × 1024, 1024 × 1536 (vertical) o 1536 × 1024 (horizontal)**; comprobar siempre las dimensiones reales del archivo recibido. Los tamaños de la especificación (por ejemplo, mapa ~2304 × 3456) son **objetivos**, no capacidades garantizadas: se intentan alcanzar después con un escalador que conserve el trazo (Krita, Real-ESRGAN, Topaz u otro) y se aceptan sólo tras revisión visual a tamaño de uso. **Escalar no cambia la proporción:** si el destino tiene otra proporción, hay que recortar o ampliar el lienzo (ver KEY-01). Transparencia, tamaño y escalado se registran como «objetivo» hasta comprobarlos.

### 3.2 Método de capas (de la imagen aprobada a piezas alineadas)

Generar cada edificio con una edición independiente puede cambiar perspectiva, tamaño, contorno y detalles. Por eso el orden preferente es:

1. **Conservar el mapa aprobado como original** (MAP-01). Nunca se sobrescribe.
2. **Extraer los edificios directamente de ese original** cuando sea posible: máscara y recorte manual en Krita/Photoshop, con su escalinata, rejas y patio. Así la pieza es, por construcción, idéntica y está en su sitio.
3. **Reconstruir el terreno que queda debajo** (MAP-02): edición con el generador o retoque manual, pintando suelo, setos y caminos donde estaban los edificios.
4. **Verificar cada pieza** en Figma sobre MAP-01: posición, escala, contorno y **orden de profundidad** (qué árboles, farolas o edificios vecinos quedan delante de la pieza y deben ir en una capa superior). La superposición al 50 % ayuda a detectar diferencias, pero no sustituye esta revisión.
5. **Sólo como alternativa**, si el recorte manual no es viable: pedir la pieza aislada al generador editando MAP-01 (prompt MAP-03…08) y aplicarle la misma verificación. Si no coincide, se descarta.

### 3.2 bis Medidas de pantalla que deben respetar las imágenes

Para que este paquete se entienda sin abrir la especificación (`diseno/ESPEC-FLUJO-PANTALLAS-v3.md`, rama `claude/gifted-knuth-4g09c2` del repositorio):

| Concepto | Valor |
|---|---|
| Pantalla de referencia | 390 × 844 dp (se valida también 360 × 780 y 430 × 932) |
| Área segura | 47 dp arriba, 34 dp abajo |
| Capa fija superior (calendario, contador, comenzar) | ~56 dp bajo el área segura → ocupa hasta ~105 dp desde arriba |
| Capa fija inferior (mano de cartas) | ~182 dp desde abajo |
| Zona útil del mapa entre ambas capas | ~557 dp de alto |

**El mapa se desplaza y la interfaz no.** El calendario, los controles y la mano son capas fijas superpuestas; el mapa se mueve por debajo. Por eso no sirve reservar franjas «tranquilas» en la imagen: lo que garantiza que un edificio se vea es que **la cámara pueda centrarlo en la zona útil**. Regla: cada edificio de lugar debe quedar al menos a ~15 % del ancho y ~12 % del alto de los bordes del mapa, para que al desplazarse pueda situarse entre la capa superior y la mano.

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

Este bloque ya está incluido completo dentro de cada prompt de la tanda 1 (no hay marcadores que sustituir). Extiende la técnica de la guía de personajes al entorno.

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
façades (powder blue, blush, pale sage, cream), slate-lilac roofs.
SEASON: the first weeks of autumn. Trees mostly green with some amber, russet and soft gold;
no spring blossom, no trees covered in flowers. Flowers only as small late-season accents:
blue-lilac hydrangeas, lilac asters, late blush roses, ivy starting to turn red.
Pastel is air and light, not a wash over everything:
keep real darks (ink, deep foliage, window openings) for contrast.
Fictional world: no real landmarks, no text, no signs, no heraldry from real families.
```

**ES (equivalente):**
Ilustración artesanal para juego narrativo móvil. Línea de tinta con presión variable, algo irregular, siempre más oscura que su material. Manchas mate amplias tipo gouache, pocas sombras estructurales, superficies tranquilas; textura sólo localizada. Color local por material. Luz de mañana suave, neutra-fría. Sin veladura amarilla, naranja ni sepia; sin detalle fotográfico, render 3D, plástico, vector uniforme ni grano general. Verdes y azules naturales, fachadas marfil y pasteles pálidos, tejados pizarra lila. Estación: primeras semanas de otoño; árboles sobre todo verdes con algo de ámbar, rojizo y oro suave; nada de floración primaveral ni árboles cubiertos de flores. Flores sólo como acentos tardíos: hortensias azul-lila, ásteres lila, rosas tardías y hiedra que empieza a enrojecer. El pastel es aire y luz, no un velo sobre todo: conservar oscuros reales. Mundo ficticio: sin monumentos reales, textos, letreros ni heráldica real.

---

## 5. Encargos de la tanda 1

### MAP-01 · Mapa de Valcenda completo, de día

- **Uso:** fondo principal del juego; se desplaza en vertical y algo en horizontal.
- **Generar:** 1024 × 1536 (vertical, 2:3). **Objetivo tras escalar:** ~2304 × 3456 px (768 × 1152 dp, misma proporción 2:3; sujeto a comprobación). El mapa es mayor que la pantalla y se desplaza bajo capas fijas (§3.2 bis).
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
portrait tokens. Leave calm areas (plazas, lawns, river surface) next to each venue
where a small marker can sit without hiding the building.
SCROLLING MAP: the image is larger than the phone screen and will scroll under fixed
interface layers. Place every venue building well inside the image, at least 15% of the
width and 12% of the height away from the edges, so the camera can centre each one.
The edges can hold ordinary houses, gardens and the river.

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
Early autumn: street trees mostly green with some amber and russet crowns, ivy on a few
walls starting to redden, hydrangeas and late roses in the garden villa and residence.
No blossoming trees.

STYLE — SALVERNA ENVIRONMENT:
Handcrafted illustration for a narrative mobile game. Pressure-varied ink lines,
slightly irregular, always darker than the material they outline (brown-grey on stone,
deep green on foliage, slate on roofs). Broad matte gouache-like paint shapes with
few structural shadows and quiet surfaces; texture only in small local areas.
Local colour painted independently per material. Morning light, soft and cool-neutral.
NO yellow, orange or sepia glaze over the image. NO photographic detail, NO 3D render,
NO glossy plastic surfaces, NO uniform vector look, NO global grain or noise.
Palette: natural greens and blues of a living city, warm-ivory and pale pastel
façades (powder blue, blush, pale sage, cream), slate-lilac roofs.
SEASON: the first weeks of autumn. Trees mostly green with some amber, russet and soft gold;
no spring blossom, no trees covered in flowers. Flowers only as small late-season accents:
blue-lilac hydrangeas, lilac asters, late blush roses, ivy starting to turn red.
Pastel is air and light, not a wash over everything:
keep real darks (ink, deep foliage, window openings) for contrast.
Fictional world: no real landmarks, no text, no signs, no heraldry from real families.

OUTPUT: single opaque illustration, no text, no labels, no UI, no frame, no people larger
than tiny distant figures.

REVIEW PRIORITIES: six venue buildings instantly distinguishable at phone size;
consistent perspective; no yellow cast.
```

**ES (resumen equivalente):** dibujo original desde cero de Valcenda en vista oblicua elevada (~45°), cámara y escala únicas, composición vertical. Río ancho con puente de piedra en el tercio superior; casas adosadas pastel, plazas, calles empedradas. Seis edificios de lugar bien separados y reconocibles: salón de baile neoclásico, villa con jardines formales (Serravalle), teatro redondo con cúpula, residencia de esquina con jardín, academia con patio y cúpula pequeña, palacio en la terraza más alta. Primer otoño: árboles verdes con copas ámbar y rojizas, hiedra que enrojece, hortensias y rosas tardías; sin árboles en flor. Espacio tranquilo junto a cada edificio para su marcador. Mapa desplazable: cada edificio de lugar al menos a 15 % del ancho y 12 % del alto de los bordes, para que la cámara pueda centrarlo bajo las capas fijas. Sin texto ni interfaz. Prioridades: edificios distinguibles, perspectiva coherente, sin tono amarillo.

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
- **Método preferente:** recorte manual desde MAP-01 (§3.2). **Alternativa:** edición con el generador usando el prompt siguiente, mismo lienzo, fondo transparente como objetivo.
- **Adjuntos (alternativa):** únicamente MAP-01.
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

**Verificación obligatoria (§3.2 paso 4):** posición, escala, contorno y orden de profundidad sobre MAP-01. Si no coincide, se descarta y se recorta a mano.

### UI-01 · Guirnalda floral superior

- **Uso:** capa fija colgada del borde superior de la pantalla (no se desplaza con el mapa); enmarca la ciudad y da fondo legible a las fichas de almanaque. Se mece levemente.
- **Generar:** 1536 × 1024 (horizontal). Se usará la franja superior ~1536 × 420. **Fondo:** transparente.
- **Adjuntos:** 3 originales de técnica.

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL DECORATIVE ELEMENT FROM SCRATCH.
A horizontal hanging garland to frame the TOP EDGE of a mobile game screen.
Early-autumn garden flowers: blue-lilac hydrangea heads, lilac asters, a few late climbing
roses (blush and ivory) and trailing ivy with some leaves turning red and gold,
hanging from a thin unseen line along the top edge. No wisteria, no spring blossom.
Asymmetric and organic: denser and longer at the left and right corners (hanging down
to about 40% of the image height), very sparse and short across the centre
(only small leaves and a few blossoms, under 12% of the height) so the centre stays clear.
Must not look like a copy of any film or series poster: no arch, no symmetry.
Seen from slightly below, soft morning light.

STYLE — SALVERNA ENVIRONMENT:
Handcrafted illustration for a narrative mobile game. Pressure-varied ink lines,
slightly irregular, always darker than the material they outline (brown-grey on stone,
deep green on foliage, slate on roofs). Broad matte gouache-like paint shapes with
few structural shadows and quiet surfaces; texture only in small local areas.
Local colour painted independently per material. Morning light, soft and cool-neutral.
NO yellow, orange or sepia glaze over the image. NO photographic detail, NO 3D render,
NO glossy plastic surfaces, NO uniform vector look, NO global grain or noise.
Palette: natural greens and blues of a living city, warm-ivory and pale pastel
façades (powder blue, blush, pale sage, cream), slate-lilac roofs.
SEASON: the first weeks of autumn. Trees mostly green with some amber, russet and soft gold;
no spring blossom, no trees covered in flowers. Flowers only as small late-season accents:
blue-lilac hydrangeas, lilac asters, late blush roses, ivy starting to turn red.
Pastel is air and light, not a wash over everything:
keep real darks (ink, deep foliage, window openings) for contrast.
Fictional world: no real landmarks, no text, no signs, no heraldry from real families.

OUTPUT: isolated element on TRUE TRANSPARENT background (alpha), PNG. No sky, no wall,
no text, no frame. Edges of petals clean, no white halo.
REVIEW PRIORITIES: clear centre; painted (not photographic) flowers; real transparency.
```

**ES:** guirnalda horizontal para el borde superior con flores de primer otoño: hortensias azul-lila, ásteres lila, algunas rosas trepadoras tardías (rosa pálido y marfil) e hiedra con hojas que empiezan a enrojecer; sin glicinia ni floración primaveral; asimétrica, densa y larga en las esquinas (hasta 40 % del alto), muy escasa en el centro (menos del 12 %). Sin arco ni simetría, sin parecer póster de serie. Fondo transparente real, sin halo.

### UI-02 · Ramillete de esquina

- **Uso:** esquinas de cartas, hojas de invitación y Crónica (se refleja para las otras esquinas).
- **Generar:** 1024 × 1024. **Fondo:** transparente.

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL DECORATIVE ELEMENT FROM SCRATCH.
A small corner spray for stationery: a sprig of lilac asters, one small late rose and
two ivy leaves (one turning red), growing diagonally from the TOP-LEFT corner towards the centre,
occupying only the top-left 45% of the canvas; the rest empty.
Delicate and light, like a painted motif on fine writing paper.

STYLE — SALVERNA ENVIRONMENT:
Handcrafted illustration for a narrative mobile game. Pressure-varied ink lines,
slightly irregular, always darker than the material they outline (brown-grey on stone,
deep green on foliage, slate on roofs). Broad matte gouache-like paint shapes with
few structural shadows and quiet surfaces; texture only in small local areas.
Local colour painted independently per material. Morning light, soft and cool-neutral.
NO yellow, orange or sepia glaze over the image. NO photographic detail, NO 3D render,
NO glossy plastic surfaces, NO uniform vector look, NO global grain or noise.
Palette: natural greens and blues of a living city, warm-ivory and pale pastel
façades (powder blue, blush, pale sage, cream), slate-lilac roofs.
SEASON: the first weeks of autumn. Trees mostly green with some amber, russet and soft gold;
no spring blossom, no trees covered in flowers. Flowers only as small late-season accents:
blue-lilac hydrangeas, lilac asters, late blush roses, ivy starting to turn red.
Pastel is air and light, not a wash over everything:
keep real darks (ink, deep foliage, window openings) for contrast.
Fictional world: no real landmarks, no text, no signs, no heraldry from real families.
Simplified for small display: fewer, clearer shapes than a botanical study.

OUTPUT: TRUE TRANSPARENT background (alpha), PNG, no paper, no text, no frame.
```

**ES:** ramillete de esquina: una rama de ásteres lila, una rosa tardía pequeña y dos hojas de hiedra (una enrojeciendo), en diagonal desde la esquina superior izquierda, ocupando sólo el 45 % superior izquierdo. Delicado, simplificado para tamaño pequeño. Transparente.

### UI-03 · Papel marfil

- **Uso:** superficie de hojas, cartas y Crónica (9 zonas en motor).
- **Generar:** 1024 × 1024. **Fondo:** opaco (es la propia textura).

**EN (pegar):**
```text
A seamless, tileable texture of fine ivory writing paper (#FBF7F0 average), very subtle:
faint cotton fibres and gentle tonal variation only. Flat and evenly lit, no shadows,
no folds, no stains, no vignette, no yellowing, no visible pattern repetition.
Must stay quiet behind body text on a phone screen. OUTPUT: opaque PNG; edges intended to tile seamlessly.
```

**ES:** textura continua de papel marfil fino (media #FBF7F0), muy sutil: fibras y leve variación tonal; sin sombras, pliegues, manchas, viñeta ni amarilleo. Debe quedar tranquila detrás del texto de lectura en el teléfono. Bordes pensados para repetirse.

**Comprobación:** pedir textura repetible no asegura que lo sea. Montar una repetición 3 × 3 y buscar costuras o motivos que se repiten; probar lectura del cuerpo de texto real sobre la textura en Figma a tamaño de teléfono.

### KEY-01 · Portada

- **Uso:** pantalla de inicio. El título y los botones se ponen en Figma encima.
- **Problema de proporción:** el generador entrega 1024 × 1536 (2:3) y la pantalla de destino ronda 9:19,5 (por ejemplo, 1290 × 2796). Escalar no lo resuelve: al llenar la altura se pierde ~31 % del ancho (unos 160 px por lado en el original).
- **Vía elegida: recortar el ancho, conservar el alto.** Todo lo importante se compone dentro de la **columna central del 68 % del ancho**; al llenar la pantalla se recortan los laterales (sólo follaje y fondo prescindibles) y **la altura no cambia, así que los porcentajes de las zonas siguen siendo válidos**.
- **Ampliar el lienzo sólo para pantallas más altas** que 9:19,5. Si se amplía, los porcentajes se desplazan (la imagen original pasa a ocupar una franja central): **hay que volver a medir** título, carta, abanico y botones sobre el encuadre final. Nunca estirar.
- El título, los botones y el foco se comprueban **sobre el encuadre final** en Figma (9:19,5 y también 9:16 y 9:20).
- **Zonas (porcentajes de la altura de la imagen generada, válidos con la vía de recorte):** título en el 18–36 %; carta y abanico en el **48–70 %**, por encima de los botones y con espacio para distinguir ambos objetos; botones en el 74–94 %.
- **Generar:** 1024 × 1536 como primer paso. **Objetivo tras ampliar y escalar:** ~1290 × 2796 (objetivo sujeto a comprobación). **Fondo:** opaco.
- **Adjuntos:** 3 originales de técnica (y MAP-01 aprobado como referencia de lugar, si existe).

**EN (pegar):**
```text
OPERATION: NEW ORIGINAL KEY ART FROM SCRATCH.
Title-screen illustration for a portrait mobile game about a matchmaker during the
social season of Valcenda, a fictional Regency-inspired capital.
CROP SAFETY: the image will be cropped to a narrow phone screen. Keep EVERY important
element inside the central 68% of the width. The outer 16% on each side may contain
only expendable foliage, blossoms and background.
COMPOSITION (three depth planes):
- foreground: early-autumn flowers (hydrangeas, asters, late roses, reddening ivy)
  entering from the top corners; no wisteria, no spring blossom;
  a stone balustrade crossing the lower part of the image;
- middle: on the balustrade rail, between 48% and 70% of the image height, an open
  folding fan and a sealed letter with a rose wax seal, clearly separated from each other
  and both inside the central column;
- background: the city of Valcenda in early-morning light, river and stone bridge, soft.
NO people (characters are added later as separate art).
ZONES: keep 18%–36% of the height calm and low in detail (sky and distant roofs) for the
game title. Keep the bottom 26% simple and darker (lower balustrade and stone paving)
for buttons; nothing important there.
Strong value contrast at the letter and fan (deep ink shadows, clean whites);
pastel only in sky and blossoms.

STYLE — SALVERNA ENVIRONMENT:
Handcrafted illustration for a narrative mobile game. Pressure-varied ink lines,
slightly irregular, always darker than the material they outline (brown-grey on stone,
deep green on foliage, slate on roofs). Broad matte gouache-like paint shapes with
few structural shadows and quiet surfaces; texture only in small local areas.
Local colour painted independently per material. Morning light, soft and cool-neutral.
NO yellow, orange or sepia glaze over the image. NO photographic detail, NO 3D render,
NO glossy plastic surfaces, NO uniform vector look, NO global grain or noise.
Palette: natural greens and blues of a living city, warm-ivory and pale pastel
façades (powder blue, blush, pale sage, cream), slate-lilac roofs.
SEASON: the first weeks of autumn. Trees mostly green with some amber, russet and soft gold;
no spring blossom, no trees covered in flowers. Flowers only as small late-season accents:
blue-lilac hydrangeas, lilac asters, late blush roses, ivy starting to turn red.
Pastel is air and light, not a wash over everything:
keep real darks (ink, deep foliage, window openings) for contrast.
Fictional world: no real landmarks, no text, no signs, no heraldry from real families.

OUTPUT: single opaque illustration, no text, no logo, no frame.
REVIEW PRIORITIES: all key elements inside the central 68% column; calm title band;
letter and fan readable above the button zone; no yellow cast.
```

**ES (resumen equivalente):** ilustración de portada sin personas. Todo lo importante dentro de la columna central del 68 % del ancho; los laterales, sólo follaje prescindible. Delante: flores de primer otoño (hortensias, ásteres, rosas tardías, hiedra que enrojece) desde las esquinas superiores y una balaustrada de piedra en la parte baja. En medio, sobre la baranda y entre el 48 % y el 70 % del alto: abanico abierto y carta lacrada (sello rosa), separados y legibles. Al fondo: Valcenda con río y puente de mañana. Franja 18–36 % tranquila para el título; 26 % inferior simple y más oscuro para botones. Contraste fuerte en carta y abanico; pastel sólo en cielo y flores. Sin texto.

**Ampliación posterior (sólo para pantallas más altas; después, volver a medir las zonas):**
```text
EDIT OF THE ATTACHED IMAGE: extend the canvas vertically only. Continue the sky and
distant city upward and the stone balustrade and paving downward, matching camera,
light, line and paint exactly. Do not move, resize or redraw anything already present.
No text.
```

## 6. Orden de trabajo recomendado

1. **MAP-01** → lo monto en Figma y revisamos juntos a tamaño teléfono con marcadores y cartas.
2. Si se aprueba: extracción manual de edificios y **MAP-02** (terreno reconstruido); generador para piezas sólo como alternativa.
3. En paralelo: **UI-01, UI-02, UI-03** (independientes del mapa).
4. **KEY-01** cuando el mapa esté aprobado (comparten lugar y luz).
5. Mientras tanto, se escriben las **fichas del elenco social** para desbloquear la tanda 2. Para probar el formato de la carta antes, puede usarse una base ya aprobada (Leonora t48).

Subir cada resultado aquí o al repositorio con su ID en el nombre del archivo (por ejemplo `MAP-01_v1.png`).

---

## English summary

Batch 1 covers environment and UI only, because the eight social-season characters have no design sheets yet (the project guide forbids generating characters without them). Card proposals (not yet approved; to be validated mounted in Figma): arched top with near-square bottom corners, 2:3, full-width name bar over the shoulders in the character's house colour, painted house-colour wash behind a transparent bust, ivory veil for busy, lift for selected. The image model usually outputs 1024×1024, 1024×1536 or 1536×1024. Layer method: keep the approved full map as the original, cut buildings directly from it where possible, rebuild the ground underneath, and verify each piece for position, scale, outline and depth order; generator cut-outs are only a fallback. The title art is composed for a central 68 % safe column and extended vertically, since 2:3 output cannot become ~9:19.5 by scaling. Sizes, transparency and upscaling are targets subject to checking. Prompts (EN to paste, ES equivalent) are provided for the full map, clean plate, six building cut-outs, top floral garland, corner spray, ivory paper texture and title key art, each with a shared environment style block (handcrafted line, matte gouache, local colour, no yellow glaze, pastel as air not as wash).
