# Prompts: marco de retrato y fondo pintado (14 oct.)

Cada retrato del elenco se monta en tres capas, de abajo arriba:
1. **Fondo pintado común:** la misma imagen para los 8.
2. **Personaje recortado**, sin fondo.
3. **Marco**: PNG con el centro transparente, el mismo para los 8.

**La placa del nombre** la hace el motor, del ancho del marco, para que el texto cambie con el idioma.

**Medidas:** el retrato en pantalla es de 2:3. El marco se genera grande (1024 × 1536) y el motor lo reduce a 104 × 156 dp (312 × 468 px), así que **el adorno debe leerse en pequeño**: las molduras van en el borde y el grosor no pasa de 1/14 del ancho.

---

## 1. Marco (pegar en ChatGPT)

```text
Create a single ornate picture frame for character portraits in a narrative game set in an
early-19th-century high-society season (Regency style).
FORMAT: vertical 2:3 (1024 × 1536). The INSIDE of the frame must be fully TRANSPARENT
(an empty rectangular window), and the outside of the frame also transparent. PNG with alpha.
SHAPE: a strict rectangle, straight edges, square outer corners. No arches, no ovals, no rounded window.
STYLE: carved and gilded wood, hand-painted look matching flat-colour gouache illustrations:
soft gold with cool shadows, a thin inner bead moulding, small acanthus leaves or late-autumn
flowers (asters, ivy) carved only at the FOUR CORNERS and at the centre of the top edge.
The sides stay simple so the frame reads clearly at very small size.
PROPORTIONS: frame border thickness about 7% of the image width, identical on all four sides;
the window is centred.
COLOUR: warm-neutral gold (not orange, not yellow-brown), highlights cool ivory, shadows
grey-violet. No text, no nameplate, no picture inside, no background, no shadow outside the frame.
```

## 2. Fondo pintado común (pegar en ChatGPT)

```text
Create a painted backdrop for character portraits, in the same hand-made style as the attached
character illustrations (ink line, flat gouache colour, soft patchy shadows).
FORMAT: vertical 2:3 (1024 × 1536), opaque.
SUBJECT: an empty studio backdrop like an early-19th-century portrait painter's: a soft
pale silk-blue (light celeste) wall with a gentle lighter glow behind where a head would be, a
hint of a draped curtain fold on one side, painted loosely with visible brushwork.
No people, no furniture, no text, no strong pattern. Calm, airy, slightly lighter in the upper
third and slightly deeper blue at the bottom so the figure stands out.
COLOUR: neutral daylight, cool pale blue (#C9DAEA at the top to #96B3CF at the bottom),
no yellow or cream tint.
```

**Por qué es un fondo común:** todos los retratos comparten luz y color, la mano de cartas se ve como una colección y cada personaje destaca por su ropa y su paleta, no por el fondo. Más adelante podría haber variantes por casa (un tono por casa), pero la versión 1 usa uno solo.
