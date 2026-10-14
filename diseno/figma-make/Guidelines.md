# Salverna — Guidelines for Figma Make

You are building a **mobile game UI prototype** (portrait, 390 × 844) for *Salverna*, a narrative matchmaking game set in an early-19th-century high-society season. The player is the **matchmaker** of eight young adults. Keep everything **mobile-sized**: one 390 × 844 phone frame, and no desktop layout.

## Product rules (never break)

1. **The city map is the only screen.** Every other view is a layer over the map: event sheet, full letter, character profile.
2. **It is a period game, never a dating app or a productivity app.** Do not use swipe cards, hearts, compatibility percentages, pill buttons, tab bars or app-style navigation.
3. **All visible text is in Spanish** (the game is bilingual, but this prototype uses Spanish). Use the exact strings given in the prompts. The player is addressed as «usted».
4. **All text uses ink navy `#2B3350`.** Never brown, never black.
5. **Ornament goes on edges and corners only.** The centre of every surface stays clean and readable.

## Visual language

Light rococo / Regency stationery: thick ivory paper, fine gold filigree, carved gilded frames, red wax seals, engraved vignettes, early-autumn flowers (asters, ivy, late roses).

### Colour tokens

| Token | Hex | Use |
|---|---|---|
| ivory | #FBF7F0 | Paper surfaces |
| ivory-shade | #EFE7DA | Empty slots, dividers |
| ink | #2B3350 | All text |
| ink-soft | #5D6480 | Secondary text, labels |
| silk | #A9C6E0 | Season accent |
| silk-deep | #5E82A8 | Links, focus |
| rose | #C0627A | Primary action, "has event", selection |
| wisteria | #B9A6D3 | Optional events |
| gold | #C9A45C | Frames, borders |
| gold-light | #E6CF97 | Frame highlights |
| gold-deep | #8E6E2E | Frame shadows |
| raspberry | #B23A5B | Alerts only, always with an icon or a word |

### Type

- **Cormorant Garamond** (600/700): titles, names, small-caps labels, numbers.
- **EB Garamond** (400, italic): body, quotes, dialogue.
- **Allura**: only the greeting and the signature of letters.
- Always use lining numerals. Minimum text size 12 px. Body 16/22. Titles 24.

## Components

Build these as reusable components with variants.

| Component | Size | Variants and rules |
|---|---|---|
| **DayTile** | 34 × 42 | Antique almanac leaf: ivory, double fine ink border, weekday in small caps on top, big number below. `has-event`: the border and number turn rose (**no dot**). `continues`: rose dashed inner border. `today`: gold halo. `past`: 45 % opacity |
| **PortraitCard** | 112 × 168 | **Rectangular** painted portrait inside a carved gilded frame (ornate corners, simple sides). The **name sits inside the frame**, on a gold plate across the full width at the bottom. Image slot named `portrait/<id>`. `available`; `selected` (lifted 10 px, rose glow); `not-eligible` (desaturated, 70 % opacity); `busy` (black and white + event emblem); `altered` (raspberry ribbon across the top with one word: AGITADA, INDISPUESTO). Leave free space above the head for that ribbon. No rounded portraits |
| **Slot** | 72 × 108 | Same 2:3 ratio and gold frame as PortraitCard. `empty-required` («+ Toque una carta»), `empty-optional` («Opcional»), `filled` |
| **WaxSeal** | 56 (42 in the top bar) | Round rose seal with a gold inner ring and an ivory label or icon. `inactive` (40 %), `ready` (soft pulse) |
| **Pentagon** | 150 | Axes: BAILE, ESTATUS, CHISME, PRESENCIA, INTELECTO. Requirement: dashed ink-soft outline. Guests: rose fill at 25 % with a rose stroke. Labels never clipped |
| **MapMarker** | 40 + label | Round ivory seal with an event icon (fan = ball, teacup = reception, rose = stroll, wine glass = dinner, book = lesson, crown = royal) plus an almanac label `[day │ place]`. `optional` (wisteria ring), `required` (rose ring + tiny crown), `answered` (filled rose), `active` (pulsing rose halo) |
| **EnvelopeCounter** | 42 × 31 | An illustrated envelope with a red wax dot. The count «0/4» is written **on** the envelope |

## Screen structure

- **Top bar**: one row; every element is 42 px tall.
  - EnvelopeCounter on the left.
  - In the centre, «SEMANA 1» in ivory small caps with a soft shadow, and below it **seven DayTiles, Monday to Sunday**.
  - The start-week WaxSeal (play icon) on the right.
  - Never show the total number of weeks.
- **Bottom**: the hand of eight PortraitCards in one horizontal row, with about 3.5 visible, scrollable, over a soft dark gradient.
- **Sheets** (event, profile) rise from the **bottom edge of the phone**. The ivory paper begins at the very bottom of the screen and continues upwards **behind** the portrait cards. The cards stay in front of the paper, visible and tappable. A sheet is never a floating card above the hand.

## Data (use exactly)

**Cast** (id · name · house · Baile/Estatus/Chisme/Presencia/Intelecto · gender):

| id | Name | House | Baile | Estatus | Chisme | Presencia | Intelecto | Gender |
|---|---|---|---|---|---|---|---|---|
| nilo | Nilo Lobreda | Casa Lobreda · Greda Alta | 2 | 3 | 2 | 4 | 3 | m |
| saul | Saúl Veyra | Casa Veyra · Tiria | 3 | 4 | 1 | 3 | 3 | m |
| dario | Dario Miravés | Casa Miravés · Puerto Nácar | 5 | 2 | 3 | 3 | 1 | m |
| teo | Teo Rovena | Casa Rovena · Lumbrevía | 2 | 2 | 5 | 2 | 3 | m |
| celia | Celia Lobreda | Casa Lobreda · Greda Alta | 5 | 3 | 1 | 2 | 3 | f |
| irene | Irene Salvat | Familia Salvat · Calle de los Sellos | 1 | 2 | 3 | 3 | 5 | f |
| isolda | Isolda Marén | Aseguradores Marén · Puerto Nácar | 3 | 1 | 2 | 5 | 3 | f |
| camila | Camila Ferrán | Viuda de Ferrán | 2 | 4 | 4 | 2 | 2 | f |

**Week 1 invitations** (Vendimias, Monday 24 to Sunday 30; today is Thursday 27):

| Invitation | Place | Day | Seats | Rule | Requirement | Required? |
|---|---|---|---|---|---|---|
| Velada de lectura | Imprenta Calce | 27 | 2–3 | Abierta a cualquiera | intelecto 5 · chisme 4 · presencia 4 | No |
| Paseo de primer otoño | Jardines Serravalle | 27 | 2–4 | Abierta a cualquiera | presencia 4 · chisme 3 · estatus 3 | No |
| Recepción de apertura | Palacio | 29 | 2 | Una dama y un caballero | estatus 4 · presencia 4 · baile 4 | **Yes** |
| Lección de baile | Academia | 30 | 1–3 | Abierta a cualquiera | +1 Baile for each attendee | No |

**Group value of a skill** = the highest value among the guests, +1 if any other guest has 3 or more (maximum 5). The Pentagon draws these values.

## Interaction rules

- Tapping a marker focuses the map so that place sits in the visible upper area, then raises the event sheet.
- With an event sheet open, tapping a portrait sends it to the first free slot; tapping a placed face removes it.
- When a portrait **cannot** go, it is shown `not-eligible`. If tapped, it shakes and the help line explains why:
  - «Ya tiene compromiso el 29.»
  - «Ya tiene dos compromisos esta semana.»
  - «Falta una dama, no otro caballero.»
  - «No quedan huecos.»
- The WaxSeal «Sellar» becomes ready only when the minimum seats are filled. Sealing marks the marker as answered and adds one to the envelope count.
- The start-week seal becomes ready when every **required** invitation is answered.
- Tapping a portrait with no sheet open raises the character profile.
