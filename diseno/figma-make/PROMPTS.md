# Cómo construir la maqueta en Figma Make (14 oct.)

## Lo que dice Figma sobre cómo darle instrucciones a su IA

Según la documentación oficial de Figma y sus guías:

1. **El archivo `Guidelines.md` se lee siempre primero.** Cada archivo de Figma Make tiene una carpeta `guidelines/` que la IA consulta antes de generar. Es el lugar para el sistema de diseño: colores, tipografía, componentes y reglas. → Por eso el sistema completo va en `Guidelines.md` y no en el chat.
2. **El primer mensaje es el encargo.** Debe incluir objetivo, contexto, elementos clave, comportamientos, restricciones y cómo se ve terminado. Los mensajes siguientes son cambios pequeños.
3. **Primero la composición, después la funcionalidad.** Conviene construir la pantalla estática y añadir las interacciones en mensajes posteriores.
4. **Hay que ser claro y concreto.** Cuanto más preciso, menos inventa.
5. **Las imágenes adjuntas sirven de ejemplo, pero no transmiten colores exactos.** Por eso los colores van en hexadecimal y en cada adjunto hay que decir si es para copiar uno a uno o sólo como referencia.
6. **El móvil todavía es su punto débil.** Hay que insistir en «mobile-sized 390 × 844» y en un solo marco principal.
7. **Los retoques pequeños se hacen a mano.** Para cambios visuales menores conviene editar directamente en lugar de gastar créditos con otro mensaje.
8. **First Draft**, la otra IA de Figma, no usa tu propio sistema de diseño y funciona mejor con diseños comunes. Para este juego, **Figma Make es la herramienta adecuada.**

Fuentes:
- [Figma Help: Make](https://help.figma.com/hc/en-us/articles/31304485164695-Create-a-Figma-Make-file)
- [Figma: How to write great prompts](https://developers.figma.com/docs/code/how-to-write-great-prompts/)
- [Figma: Write design system guidelines](https://developers.figma.com/docs/code/write-design-system-guidelines/)
- [Figma Help: Attach designs and images](https://help.figma.com/hc/en-us/articles/31304529835671)
- [Figma Blog: 7 tips for credits](https://www.figma.com/blog/7-tips-for-using-figma-make-credits-more-efficiently/)
- [Figma Help: First Draft](https://help.figma.com/hc/en-us/articles/23955143044247)
- [UX Collective: 5 ways to improve Figma Make prompts](https://uxdesign.cc/how-to-prompt-figma-makes-ai-better-for-product-design-627daf3f4036)

---

## Pasos

### Paso 0 · Preparar

1. Crea un archivo de **Figma Make**.
2. Abre **Code → guidelines → Guidelines.md** y reemplaza su contenido por el de [`Guidelines.md`](<Guidelines.md>) de esta carpeta.
3. Ten a mano para adjuntar:
   - los 8 retratos (`diseno/maqueta/*_carta.jpg`);
   - `ref_mapa.png` y `ref_hoja.png`, que son capturas de la maqueta HTML y sirven **sólo** para la disposición.

### Paso 1 · El encargo (primer mensaje)

Adjunta los 8 retratos y `ref_mapa.png`, y pega:

```text
Build the main screen of the Salverna mobile game prototype, following Guidelines.md exactly.
Keep it mobile-sized: a single 390 × 844 phone frame.

GOAL: the "Map – planning" screen where the matchmaker reads the week's invitations on a city map.
CONTEXT: period matchmaking game; this is the screen the player sees most.
KEY ELEMENTS:
- Full-screen illustrated city map placeholder (soft painted streets, a river, two parks, early autumn),
  with a soft dark gradient at the top and bottom.
- Top bar exactly as in Guidelines.md: EnvelopeCounter «0/4» (left), «SEMANA 1» + seven DayTiles
  24–30 (Mon–Sun, 27 today; 27, 29 and 30 have events), start-week WaxSeal (right, inactive).
- Four MapMarkers: Palacio (29, required, teacup), Imprenta Calce (27, wine glass),
  Jardines Serravalle (27, rose), Academia (30, book).
- Assistant note card above the hand: small caps «NOTA», italic «Ya llegaron sus ocho jóvenes.
  Toque una carta para conocer a cada uno.»
- Hand of eight PortraitCards using the attached portraits, in this order: Nilo, Saúl, Dario, Teo,
  Celia, Irene, Isolda, Camila.
CONSTRAINTS: layout and visuals only in this step, no interactions yet. The attached screenshot is a
LAYOUT reference only: match positions and proportions, but make the visual finish richer and more
period (gilded carved frames, filigree, almanac paper), as described in Guidelines.md.
DONE WHEN: the screen looks like a polished period game screen, every element sits in the positions
described, the portraits are rectangular with the name inside the frame, and nothing looks like a dating app.
```

### Paso 2 · La hoja de evento (composición)

Adjunta `ref_hoja.png` y pega:

```text
Add the event sheet for «Recepción de apertura», as a static state (no interactions yet).
- Shift the map so the Palacio marker (active, pulsing) sits in the upper visible area; dim the rest slightly.
- The ivory paper sheet starts at the BOTTOM EDGE OF THE PHONE and rises BEHIND the hand of portraits;
  the portraits stay in front, on top of the paper. Small drag handle and ✕ at the top; rococo gold
  filigree on the top corners only.
- Always-visible content (there is NO "see details" toggle):
  large DayTile «OBLIG. 29», title «Recepción de apertura», line «La Corona · Una dama y un caballero»;
  italic quote «Los ocho serán presentados ante la reina. Una pareja abrirá el primer baile.»;
  two Slots (Saúl filled, the other «+ Toque una carta») and the Pentagon on the right
  (requirement estatus 4, presencia 4, baile 4; guests = Saúl);
  «+ Toda la temporada mira esta noche» and «− El maestro de ceremonias es nuevo y está nervioso»;
  help line «Falta una dama.»; bottom row: text button with an envelope icon «Leer la invitación»
  (left) and the WaxSeal «Sellar» (right, inactive).
- In the hand: Saúl selected; Nilo, Dario and Teo not-eligible; the ladies available.
The screenshot is a layout reference only; the sheet itself must start at the phone's bottom edge.
```

### Paso 3 · Las interacciones

```text
Now make the event sheet work, following the Interaction rules in Guidelines.md:
tapping a marker focuses the map and raises the sheet from the bottom edge (behind the hand);
tapping a portrait flies it into the first free slot; ineligible portraits shake and the help line
shows the reason; tapping a placed face removes it; the Pentagon updates live; «Sellar» is ready
only when the minimum seats are filled; sealing closes the sheet, fills the marker and adds one to the
envelope count; the start-week seal becomes ready when the required invitation is answered.
Dragging the handle down or tapping the map closes the sheet. Use the week 1 data in Guidelines.md
for all four invitations.
```

### Paso 4 · La invitación completa (experiencia rococó)

```text
Add the full invitation view, opened from «Leer la invitación».
Full-screen letter on thick ivory paper with a 10 px margin where the map peeks through:
an engraved header vignette of the host's building, a gold filigree frame, early-autumn flower
sprigs in two corners, a broken red wax seal at the top.
Greeting in Allura «A la casamentera de la Temporada,»; body in EB Garamond 16:
«Su Majestad recibirá a sus ocho jóvenes el sábado, a la hora de las lámparas, en el Palacio de Alto
Laurel. Le ruega que elija una dama y un caballero para abrir el primer baile ante la corte. Se valorará
el apellido, la soltura y que nadie pise a nadie.»
Signature in Allura «Mireya, secretaria de listas». Only an ✕, which returns to the sheet keeping the selection.
```

### Paso 5 · La ficha de personaje

```text
Add the character profile: tapping a portrait while no sheet is open raises a tall ivory sheet from the
bottom edge, behind the hand; that portrait stays lifted in front.
Content for Nilo: framed rectangular portrait 160 × 240, «Nilo Lobreda», «Casa Lobreda · Greda Alta»
with a small forest-green swatch, italic «Te trata como a un amigo antes de saber tu nombre.»;
the Pentagon of his skills next to a short technical sheet (Edad 26); «Biografía»: «De la casa Lobreda
de Greda Alta, cuyas caravanas cruzan el paso hacia Valcenda. Primo de Celia. Llega con fama de
resolver cualquier cosa antes de que se la pidan.»; «Lo que usted sabe»: one unlocked entry
«Promete antes de que una termine de pedir. Lo raro es que casi siempre cumple.» and five locked
titles in ink-soft. Same pattern for all eight characters.
```

---

## Después de cada paso

1. **Pásame el enlace del archivo de Make** (figma.com/make/…). Lo reviso con las herramientas de Figma y te devuelvo correcciones concretas para el siguiente mensaje.
2. Si sólo falla un detalle visual (un color, un tamaño), corrígelo a mano en Figma: no gasta créditos.
3. **Revisión en cada paso:**
   - El papel nace en el borde inferior, detrás de los retratos.
   - Los retratos son rectangulares, con el nombre dentro del marco.
   - Los días con evento tienen el borde rosa, sin punto.
   - No aparece «ver detalles».
   - No hay pastillas ni corazones.
   - El texto está en azul marino.
   - Hay un solo marco de 390 × 844.
