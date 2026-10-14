# Brief para Figma (IA de Figma o Figma Make) · Plantilla v5 — 14 oct.

> **Sustituido por [`figma-make/`](<figma-make/PROMPTS.md>)** (14 oct.): `Guidelines.md` más los mensajes paso a paso, siguiendo la guía oficial de Figma Make. Este archivo queda como historial.

**Qué es:** las decisiones probadas en la maqueta HTML (`diseno/maqueta/`), convertidas en instrucciones para que Figma genere la plantilla con acabado profesional y de época.

**Cómo usarlo:**
1. Pega el **bloque 1** completo.
2. Después, una a una, las **pantallas del bloque 2**.
3. Si Figma pide imágenes, sube los 8 retratos recortados (`diseno/maqueta/*_carta.jpg`). Si no, deja los marcos de imagen vacíos y con su nombre: así se cambian en un clic.

---

## Bloque 1 · Sistema y reglas (pegar primero)

```text
Design a mobile game UI (portrait phone, 390 × 844 frame) for "Salverna", a narrative
matchmaking game set in an early-19th-century high-society season. The player is the
matchmaker of eight young adults. The look must feel like a beautiful period game
(Regency / light rococo stationery: ivory paper, fine gold filigree, wax seals, engraved
borders), NEVER like a dating app or a productivity app.

DESIGN TOKENS
- Colours: ivory #FBF7F0 (paper), ivory-shade #EFE7DA, ink navy #2B3350 (ALL text),
  soft ink #5D6480, silk blue #A9C6E0, deep silk #5E82A8, rose #C0627A (primary action and
  "has event"), wisteria #B9A6D3, gold #C9A45C, light gold #E6CF97, deep gold #8E6E2E,
  raspberry #B23A5B (alerts only, always with an icon or word). Text is never brown.
- Type: Cormorant Garamond (titles, names, numbers, small-caps labels),
  EB Garamond (body, dialogue, italic quotes), Allura (only letter greeting and signature).
  Use lining numerals everywhere.
- Shapes: paper sheets with 1 px gold border; confirm actions are round WAX SEALS (rose with a
  gold inner ring), never pill buttons. Calendar tiles look like antique almanac leaves:
  ivory, double fine ink border, small-caps weekday on top, big number below.
- Ornament lives on edges and corners (gold filigree, small autumn flowers: asters, ivy).
  The centre of every surface stays clean and readable.

COMPONENTS (make each one a reusable component with variants)
1. DayTile (34 × 42): weekday + number. Variants: normal; "has event" = border and number in
   rose (no dot); "event continues" = rose dashed inner border; "today" = gold halo; "past" = 45%.
2. PortraitCard (112 × 168): a RECTANGULAR painted portrait inside a carved gilded frame
   (ornate corners, simple sides). The character's NAME sits INSIDE the frame on a gold plate
   across the full width at the bottom. The image is a named image placeholder
   "portrait/<name>" so it can be swapped. Variants: available (full colour); selected (lifted
   10 px, rose outline glow); unavailable for this invitation (desaturated 70%, 70% opacity);
   busy elsewhere (black and white + small event emblem top-left); altered (raspberry ribbon
   across the top with one word: AGITADA / INDISPUESTO). Leave free space above the head for
   that ribbon. No rounded corners on the portrait.
3. Slot (72 × 108): same 2:3 proportion and same gold frame as PortraitCard, smaller.
   Variants: empty required ("+ Tap a card"), empty optional ("Optional"), filled (portrait).
4. WaxSeal button (56): rose seal, gold ring, ivory label. Variants: inactive 40%, ready (soft pulse).
5. Pentagon radar (150): five axes Dance, Standing, Gossip, Presence, Intellect;
   requirement = dashed soft-ink outline; guests = rose 25% fill with rose stroke.
6. MapMarker: round ivory seal (40) with event-type icon (fan = ball, teacup = reception,
   rose = stroll, wine glass = dinner, book = lesson, crown = royal), plus an almanac label
   [day | place]. Variants: optional (wisteria ring), required (rose ring + tiny crown),
   answered (filled rose), active (pulsing rose halo).
7. Envelope counter (42 × 31): an illustrated envelope with a red wax dot; the count "0/4"
   is written ON the envelope.

LAYOUT RULES
- The city map is the only screen; everything else is a layer over it.
- Top bar (one row, all elements 42 px tall): Envelope counter on the left; in the centre
  "SEMANA 1" in ivory small caps with a soft shadow, and below it SEVEN DayTiles (Mon–Sun);
  the round "start week" wax seal (play icon) on the right. Do not show the total of weeks.
- Bottom: the hand of PortraitCards in a horizontal row (about 3.5 visible, scrollable),
  over a soft dark gradient.
- Sheets (event, profile) rise from the BOTTOM EDGE OF THE PHONE: the ivory paper starts at
  the very bottom of the screen and continues up BEHIND the portrait cards; the cards stay
  on top of the paper, visible and tappable. Never a floating card above the hand.
```

## Bloque 2 · Pantallas (una por mensaje)

### 2.1 Mapa en planificación

```text
SCREEN 1 · "Map – planning". Full-screen illustrated city map of Valcenda (placeholder image
"map/valcenda"), top bar as specified, four MapMarkers: Palace (29, required, reception),
Calce Printing House (27, dinner), Serravalle Gardens (27, stroll), Academy (30, lesson).
Days 27, 29 and 30 use the "has event" DayTile; 27 is today. Envelope shows 0/4.
A small handwritten-style note card from the assistant above the hand: label "NOTA",
italic text "Ya llegaron sus ocho jóvenes. Toque una carta para conocer a cada uno."
Hand of 8 PortraitCards: Nilo, Saúl, Dario, Teo, Celia, Irene, Isolda, Camila.
```

### 2.2 Hoja de evento (asignar)

```text
SCREEN 2 · "Event sheet – assigning". Same map, shifted so the Palace marker (active, pulsing)
sits in the visible upper area; the rest of the map slightly dimmed.
An ivory paper sheet rises from the bottom edge of the phone, behind the hand of portraits,
with a small drag handle and an ✕ at the top. Rococo gold filigree on its top corners only.
CONTENT, ALWAYS VISIBLE (no "see details" toggle):
- Almanac DayTile large (48 × 56) "OBLIG. 29", title "Recepción de apertura" (Cormorant 24),
  line "La Corona · Una dama y un caballero".
- One italic quote: "Los ocho serán presentados ante la reina. Una pareja abrirá el primer baile."
- Two Slots (one filled with Saúl, one empty "+ Toque una carta") on the left, the Pentagon
  radar on the right.
- Two short lines: "+ Toda la temporada mira esta noche" and "− El maestro de ceremonias es nuevo y está nervioso".
- A help line in soft ink: "Falta una dama."
- Bottom row: a text button with an envelope icon "Leer la invitación" on the left and the
  WaxSeal "Sellar" on the right (inactive until both slots are filled).
In the hand: Saúl selected (lifted), the other gentlemen desaturated (not eligible), the
ladies available.
```

### 2.3 La invitación completa (experiencia rococó)

```text
SCREEN 3 · "Full invitation". Opened from "Leer la invitación". A full-screen letter on thick
ivory paper with a 10 px margin where the map peeks through. Rococo ornament: an engraved
header vignette of the host's palace (placeholder "letter/crown"), gold filigree frame,
autumn flower sprigs in two corners, a red wax seal broken at the top.
Greeting in Allura: "A la casamentera de la Temporada,". Body in EB Garamond 16:
"Su Majestad recibirá a sus ocho jóvenes el sábado, a la hora de las lámparas, en el Palacio
de Alto Laurel. Le ruega que elija una dama y un caballero para abrir el primer baile ante la
corte. Se valorará el apellido, la soltura y que nadie pise a nadie."
Signature in Allura: "Mireya, secretaria de listas". Only an ✕ to close (returns to the sheet,
keeping the selection).
```

### 2.4 Ficha de personaje

```text
SCREEN 4 · "Character profile". Tapping a portrait (no invitation open) raises a tall ivory
sheet from the bottom edge, behind the hand; the chosen PortraitCard stays lifted in front.
Content: large framed portrait (160 × 240, rectangular, gold frame) at top-left, name
"Nilo Lobreda" (Cormorant 26), house "Casa Lobreda · Greda Alta" with a small forest-green
house swatch, italic line "Te trata como a un amigo antes de saber tu nombre."
Pentagon radar of his five skills next to a small "technical sheet" (Age 26, likes: walks).
Section "Biografía" (3 lines). Section "Lo que usted sabe": one unlocked entry and five
locked ones shown only by their titles in soft ink ("Lo que le gusta", "Lo que teme",
"Una confidencia", "Lo que esconde", "Cómo terminó la temporada").
Section "Compromisos de la semana" with almanac tiles. No orientation, no compatibility hearts.
```

---

**Comprobar en lo que entregue Figma:**
- El papel marfil nace en el borde inferior del teléfono, detrás de los retratos.
- Los retratos son rectangulares y llevan el nombre dentro.
- Los días con evento tienen el borde rosa, sin punto.
- No aparece «ver detalles».
- No hay pastillas ni corazones.
- Todo el texto va en tinta azul marino.
