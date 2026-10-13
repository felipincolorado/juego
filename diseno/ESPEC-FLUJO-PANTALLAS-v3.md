# Salverna · Temporada social — Especificación de flujo, pantallas y tamaños (v3)

**14 de octubre de 2026 · Propuesta de dirección de interfaz para revisión del usuario.**
Complementa la entrega integral, la investigación de referentes y la guía de prompts. No aprueba arte ni implementa nada en Godot. Cuando esta especificación contradiga la sección 4 de la entrega integral (agenda separada, barra Ciudad/Elenco/Calendario), prevalece esta, porque recoge las instrucciones posteriores del usuario.

---

## 0. Principios (en orden de prioridad)

1. **La ciudad es la pantalla.** Todo lo demás son capas sobre el mapa: hoja de evento, carta, ficha, incidente, resultado. No hay pestañas ni pantalla de calendario.
2. **El elenco siempre está a la vista.** La tira inferior de retratos es a la vez el elenco, el selector de asistentes y el tablero de estados.
3. **Cada elemento comunica una cosa.** Si un texto, adorno o número no ayuda a decidir, se quita. La belleza vive en el material (papel, seda, lacre, flores), no en texto decorativo.
4. **Delicadeza, no misión.** Nada de carteles de «ÉXITO», sellos rojos de caucho ni lenguaje de operación. Los desenlaces se cuentan como se contarían en un salón: con tono, reacción y consecuencia.
5. **Un mismo componente sirve en varios sitios.** La ficha de fecha, la hoja inferior y la tarjeta de retrato se reutilizan. Menos piezas significa más coherencia y menos arte que producir.

---

## 1. Lienzo, rejilla y áreas seguras

| Concepto | Valor | Nota |
|---|---|---|
| Lienzo de diseño | **390 × 844 dp** | Teléfono actual medio. Se valida también a 360 × 780 (Android estrecho) y 430 × 932 (alto). |
| Área segura | 47 dp arriba, 34 dp abajo | Nada interactivo dentro de esas franjas. |
| Rejilla | Base 8 dp; margen lateral 16 dp | Separaciones de 4 dp sólo dentro de componentes. |
| Toque mínimo | 48 × 48 dp | Aunque el dibujo sea menor, el área táctil no. |
| Preparación de arte | **@3×** sobre el tamaño en dp | 104 dp → 312 px. |
| Texto mínimo | 12 dp | Nunca reducir para que algo quepa; se reescribe. |

El marco 432 × 768 de documentos anteriores queda como histórico. La composición no es una caja rígida: el mapa se desplaza y absorbe las diferencias de alto.

---

## 2. Sistema visual

### 2.1 Paleta de temporada

La paleta anterior (verde terciopelo, granate, marrón, sepia) se leía como estrategia histórica. Se sustituye por la gramática Bridgerton: pasteles de seda, glicinia, marfil y dorado fino.

| Token | Hex | Uso | No usar para |
|---|---|---|---|
| `marfil` | `#FBF7F0` | Papel de hojas, cartas, fichas | Fondos de pantalla completa sin textura |
| `marfil-sombra` | `#EFE7DA` | Filas, casillas libres, separadores | Texto |
| `tinta` | `#2B3350` | **Todo el texto** principal | — |
| `tinta-suave` | `#5D6480` | Texto secundario, etiquetas | Texto menor de 13 dp |
| `azul-seda` | `#A9C6E0` | Fondo de la tira, identidad de temporada | Botones de acción |
| `azul-profundo` | `#5E82A8` | Bordes activos, día actual | Alertas |
| `rosa-polvo` | `#EBC3C8` | Fondos suaves, flores | — |
| `rosa-acción` | `#C0627A` | **Acción principal** (sellos de confirmar, botón principal) | Estados de error |
| `glicinia` | `#B9A6D3` | Acento secundario, eventos opcionales, desenlace a medias | — |
| `menta` | `#BFD8C6` | Disponible / libre, desenlace favorable suave | — |
| `oro` | `#C9A45C` | Filetes de 1 dp, selección, progreso | Superficies grandes |
| `frambuesa` | `#B23A5B` | Atención (aro con «!», estado alterado) | Siempre acompañado de icono o palabra |

Regla: el texto nunca es marrón. La tinta azul marino sobre marfil es el cambio que más aleja el aspecto de «Age of Empires».

Los personajes conservan su **carta de color individual** (guía de prompts §3.C). La paleta de temporada gobierna la interfaz y el ambiente, no la piel ni el pelo de nadie.

### 2.2 Tipografía

| Estilo | Fuente | Tamaño / interlínea | Uso |
|---|---|---|---|
| Display | Cormorant Garamond Bold | 32 / 36 | Título de portada, título de carta |
| Título | Cormorant Garamond SemiBold | 24 / 28 | Nombre del evento, nombre del personaje |
| Encabezado | Cormorant Garamond SemiBold | 18 / 22 | Secciones |
| Cuerpo | EB Garamond Regular | 16 / 22 | Situaciones, cartas, opciones |
| Cita | EB Garamond Italic | 16 / 22 | Voz de personaje |
| Etiqueta | Cormorant Garamond SemiBold, versalitas +8 % | 12 / 16 | Habilidad, día de la semana |
| Número de fecha | Cormorant Garamond Bold | 20–26 | Fichas de fecha |
| Firma | Allura | 28 | **Sólo** saludo y firma de cartas |

### 2.3 Formas

| Elemento | Forma | Por qué |
|---|---|---|
| Hojas (paneles) | Esquina 6 dp, borde oro 1 dp, sombra suave | Papelería de época: tarjeta de visita, no caja de app |
| Tarjeta de retrato | **Vertical 2:3**, esquina 10 dp, borde 1,5 dp | El busto es vertical; horizontal recortaría hombros o cabeza |
| Ficha de fecha | Esquina 4 dp, cabecera de color | Se lee como hoja de calendario |
| Filas de opción | Esquina 6 dp, alto mínimo 56 dp | Toque cómodo, lectura de una o dos líneas |
| Acciones de confirmar | **Sello de lacre** circular 56 dp | Objeto del mundo; nunca un botón pastilla |
| Cerrar | ✕ de 20 dp con área de 48 dp | Universal |

### 2.4 Dónde van las flores (y dónde no)

Lo floral es ceremonial: aparece cuando la pantalla es un momento, no cuando es una herramienta.

| Sí | No |
|---|---|
| Esquinas de cartas (ramillete de flores de primer otoño: ásteres, rosa tardía, hiedra) | Filas de opciones del incidente |
| Portada (guirnalda alrededor del título) | Marcadores del mapa |
| Cabecera de la «Crónica de salones» (cierre de semana) | Huecos de asistentes |
| Fondo de la tira: **damasco floral tono sobre tono** al 8 % de opacidad | Encima de un texto |
| Sello de desenlace (pétalos al estamparse) | Fichas de fecha |

### 2.5 Iconografía

Iconos de línea de 1,75 dp, en tinta o marfil, dentro de sellos o en filas. Generados como vectores, no como imágenes.

| Grupo | Iconos |
|---|---|
| Tipo de evento | Abanico = baile · Máscara = teatro · Taza = recepción/visita · Rosa = paseo/jardín · Libro = clase · Corona = encargo real |
| Estado de marcador | Sobre cerrado = por responder · Sello con icono = respondida · Aro oro = en curso · Aro frambuesa + «!» = atención · Sobre abierto con lazo = resultado por leer |
| Habilidades | Abanico (Baile) · Blasón (Estatus) · Labios que susurran (Chisme) · Espejo (Presencia) · Libro abierto (Intelecto) |
| Controles | ✕ cerrar · ▶ comenzar · ❚❚ pausa · ▶▶ rápido · ✉ carta · ⚙ ajustes |
| Estado de persona | Vela (cansancio, sólo si la mecánica existe) · Termómetro (indispuesto) |

El ánimo **no** usa icono: lo cuenta la expresión del retrato (neutral, alegre, molesta, ruborizada).

---

## 3. Componentes reutilizables

### 3.1 Ficha de fecha (`ficha-fecha`) — hoja de almanaque

Se usa en cuatro lugares y siempre tiene el mismo aspecto: **hoja de almanaque antiguo**, no calendario moderno. Papel marfil `#FCF8EF`, esquina casi recta (1 dp), filete exterior en tinta de 1 dp y filete interior de 0,5 dp a 2,5 dp de distancia, número grande en Cormorant Bold y sombra mínima. **Sin franja ni cabecera de color.**

**Regla de fechas:** una ficha muestra siempre **un solo día, el de inicio**. Nunca rangos como «28–30». La duración se dice dentro de la hoja del evento («3 días · del 28 al 30»).

| Variante | Tamaño | Dónde |
|---|---|---|
| Día de semana | 40 × 48 dp | Barra superior (los días de la semana en curso) |
| Marcador | 36 × 36 dp | Junto al nombre del lugar en el mapa (día de inicio) |
| Encabezado de hoja | 48 × 56 dp, con etiqueta en versalitas arriba («OBLIG.», «AHORA») | Hoja de evento, incidente, resultado |
| Compromiso | Relleno flexible × 52 dp | Ficha de personaje (día ocupado: filete `rosa-acción` e icono del evento) |

Estados: **hoy** (filetes en `oro`, el exterior de 1,8 dp), **pasado** (45 % de opacidad), **con evento** (punto `rosa-acción` bajo el número), **ocupado** (filete `rosa-acción` + icono), **incidente** (filete y etiqueta `frambuesa`).

### 3.2 Barra superior (`barra-semana`) — sustituye a la cartela «Día 27 / Otoño temprano»

```
┌──────────────────────────────────────────────────────┐
│ ⚙   S1/6   [27][28][29][30]          ✉ 2/4   (▶)    │   alto 64 dp + área segura
└──────────────────────────────────────────────────────┘
```

| Pieza | Comunica | Sustituye |
|---|---|---|
| `S1/6` | En qué semana de la temporada estás (de seis) | «Semana 1», «Otoño temprano» |
| Cuatro fichas de fecha | Qué días abarca la semana y cuál es hoy | «27 – 30» |
| Punto bajo cada día | Qué días tienen eventos | — |
| `✉ 2/4` | Invitaciones respondidas de las de la semana | Nada (faltaba) |
| Sello `▶` | **Comenzar semana.** Gris hasta responder todas las obligatorias; luego `rosa-acción` y late suavemente | El reloj de arena |
| Durante la ejecución | `▶` se convierte en `❚❚` y `▶▶` | — |

Tocar un día del calendario **filtra el mapa**: sólo se ven los eventos de ese día. Tocar de nuevo lo quita. Es la función de «agenda» sin pantalla de agenda.

«Otoño temprano» desaparece de la interfaz permanente: la estación no cambia durante la temporada y ya se presenta en la portada y en la apertura.

### 3.3 Marcador de lugar (`marcador`)

```
        ( 🪭 )        ← sello 40 dp: icono del tipo de evento + estado
  ┌────┬───────────┐
  │ 29 │ Recepción │   ← ficha-fecha 36 dp (sólo día de inicio) + nombre 16 dp
  └────┴───────────┘
```

- Si el lugar tiene dos o más invitaciones, el sello lleva un número pequeño y tocarlo abre una **mini agenda** (lista de 2–3 filas) en vez de apilar marcadores.
- **Obligatoria**: corona pequeña sobre el sello y borde `rosa-acción`. **Opcional**: borde `glicinia`.
- El edificio del lugar se ilumina (contorno oro suave) cuando su hoja está abierta.

### 3.4 Tarjeta de retrato (`retrato`) y tira (`tira-elenco`)

| Pieza | Valor |
|---|---|
| Tira | Alto **200 dp** (12 de margen + 156 de tarjeta + 32 hasta el área segura); fondo `azul-seda` con damasco al 8 %; filete oro arriba |
| Tarjeta | **104 × 156 dp**, vertical 2:3, esquina 10 dp, separación 10 dp → se ven 3,5 tarjetas (la media indica que se puede deslizar) |
| Retrato | Busto pintado a sangre, de borde a borde |
| Nombre | Dentro de la tarjeta, abajo, sobre degradado de tinta al 60 %: 15 dp SemiBold marfil |
| Emblema de estado | Círculo 24 dp arriba a la izquierda (icono del evento donde está) |
| Expresión | El busto cambia según el ánimo (no hay icono de ánimo) |

Estados de la tarjeta:

| Estado | Tratamiento | Texto |
|---|---|---|
| Disponible | Color completo | — |
| Seleccionado | Elevado 8 dp, borde oro 2,5 dp, halo suave | — |
| Asignado / fuera / en viaje | **Blanco y negro** + emblema del lugar | — |
| Alterado (agitada, indispuesto) | Color, banda superior `frambuesa` | Una palabra: «AGITADA», «INDISPUESTO» |
| No elegible para el hueco actual | Blanco y negro al 70 %; al tocarlo se sacude y muestra «Paseo 28–30» un segundo | Sólo como respuesta al toque |

Interacción, una sola regla:

- **Con una hoja de evento abierta**: tocar retrato = poner en el primer hueco libre. Tocar una cara ya puesta en un hueco = quitarla.
- **Sin hoja abierta**: tocar retrato = abrir su ficha.
- Mantener pulsado (en cualquier caso) = abrir la ficha. Atajo, no requisito.
- Deslizar sólo desplaza la tira; nunca asigna.

### 3.5 Hoja inferior (`hoja`)

Todas las capas que no son lectura a pantalla completa usan la misma hoja: ancho 358 dp (16 de margen), esquina 6 dp, marfil, filete oro, sombra 24 dp al 25 %. Se apoya sobre la tira y deja visibles la barra superior y la tira. Alto según contenido, máximo hasta 16 dp bajo la barra superior; si no cabe, desplaza su cuerpo y **nunca** las opciones de decisión. Se cierra con ✕, tocando fuera o deslizando hacia abajo, salvo en incidentes (obligan a decidir).

### 3.6 Sello de lacre (`sello`)

56 dp, círculo `rosa-acción`, anillo interior oro, icono marfil. Estados: inactivo (40 % de opacidad, sin animación), listo (latido de escala 1 → 1,04 cada 2 s), pulsado (se hunde 2 dp y suelta pétalos). En la barra superior mide 44 dp.

### 3.7 Busto de diálogo (`dialogo`)

Busto transparente de 220 × 330 dp que asoma a la izquierda por encima de una caja de papel de 358 × 150 dp, con pestaña de nombre. Texto 17 dp, máximo tres líneas por toque. Indicador de «continuar» = pluma pequeña que parpadea. Se usa para la reina, el guía y cualquier personaje que hable en un incidente o resultado.

---

## 4. Flujo completo

```
PORTADA ──Nueva temporada──► APERTURA (diálogo: reina → guía)
   │                                   │
   └──Continuar──────────────┐         ▼
                             ▼    TUTORIAL GUIADO (primera invitación)
                ┌──────────► MAPA · PLANIFICACIÓN ◄───────────────────┐
                │             │   ├─ toque marcador ─► HOJA DE EVENTO  │
                │             │   │      ├─ ✉ ─► CARTA (✕ vuelve)      │
                │             │   │      ├─ retrato ─► asigna          │
                │             │   │      └─ sello ─► respondida ───────┤
                │             │   ├─ toque retrato ─► FICHA (✕ vuelve) │
                │             │   └─ toque día ─► filtra el mapa        │
                │             ▼                                        │
                │      ▶ COMENZAR SEMANA (si quedan opcionales: aviso) │
                │             ▼                                        │
                │      MAPA · SEMANA EN MARCHA                          │
                │        transición de día ─► viajes ─► aros            │
                │        ├─ aro «!» ─► INCIDENTE ─► RESULTADO MAYOR     │
                │        ├─ aro «!» ─► REEMPLAZO ─► (sigue)             │
                │        └─ aro completo ─► sobre con lazo (menor)      │
                │             ▼                                        │
                │      CIERRE: CRÓNICA DE SALONES (público)             │
                │             ▼                                        │
                │      CIERRE: SÓLO PARA TUS OJOS (privado)             │
                │             ▼                                        │
                └────── LLEGAN LAS CARTAS DE LA SEMANA SIGUIENTE ───────┘
                              (semana 6 ─► GRAN BAILE · fuera de alcance)
```

---

## 5. Pantallas y estados

Para cada una: propósito, contenido, acción principal, salida, y qué se optimizó respecto a v2.

### 5.1 Portada
- **Propósito:** presentar el mundo en un segundo.
- **Contenido:** ilustración de portada a pantalla completa; título «Salverna» (provisional) con *La Temporada del Sello* en cursiva; guirnalda floral; una frase de tono.
- **Acción:** botón principal (si hay partida: «Continuar»; si no: «Nueva temporada»). Secundario en texto: la otra opción. ⚙ y ES · EN abajo.
- **Optimizado:** sin partida no aparece «Continuar».

### 5.2 Apertura (diálogo)
- **Propósito:** dar el encargo y presentar a quien guía.
- **Contenido:** mapa atenuado; busto de la reina Maela Aurenza; tres intervenciones cortas (una por toque). Después entra el **guía** (persona por definir: secretaria, dama de compañía o mayordomo de la casamentera) y presenta la tira: los retratos se iluminan uno a uno.
- **Salida:** el guía señala el primer sobre.
- **Optimizado:** el muro de texto de la proclamación v2 se convierte en diálogo; la carta formal de la Corona puede guardarse como objeto releíble.

### 5.3 Tutorial guiado
- Sólo la primera semana. El guía oscurece todo menos lo que hay que tocar: sobre → hoja → retrato → sello → ▶. Cada paso con una frase. Se aprende haciendo (lección de Candy Crush), no leyendo.

### 5.4 Mapa · planificación (centro del juego)
- **Contenido:** barra superior; ciudad desplazable; marcadores; tira.
- **Acción principal:** responder invitaciones; luego ▶.
- **Optimizado:** fechas como fichas de calendario; contador de respondidas; comenzar semana integrado en la barra; filtro por día.

### 5.5 Mini agenda de lugar
- Hoja pequeña con 2–3 filas: ficha de fecha + nombre + estado. Tocar una fila abre su hoja de evento.

### 5.6 Hoja de evento (asignación)

```
┌──────────────────────────────────────────────┐
│ [29]  Recepción                          ✕   │  ficha 48×56 + título 24 dp
│ JUE   Casa Serravalle · 🪭 Baile               │  anfitrión + tipo
│ «Que sepan sostener un vals y una conversación»│  una línea de la carta (cita)
│ ┌────┐ ┌────┐        ⬠ radar 140 dp            │
│ │ C  │ │ +  │        ── requisito ── invitados  │  huecos 72×108 dp (2:3)
│ └────┘ └────┘                                  │
│ + Asistirá el heredero Miravés                 │
│ − También invitaron a la prima de C            │
│ ✉                                     (sello)  │
└──────────────────────────────────────────────┘
```

- **Huecos** con la misma proporción que la tarjeta de retrato (2:3), para que la cara «salte» de la tira al hueco sin cambiar de forma.
- **Radar** 140 dp: requisito en línea discontinua `tinta-suave`, invitados en relleno `rosa-acción` al 25 % con borde 2 dp. La leyenda sólo aparece las dos primeras veces.
- **Sello** inactivo hasta completar el cupo; listo late.
- **Optimizado:** se eliminó el adorno «◦◇◦»; lo que está en juego queda junto a la acción; la carta se abre desde ✉.

### 5.7 Carta
- Papel a pantalla completa con margen de 10 dp por el que asoma el mapa; ramillete en dos esquinas; grabado de la casa anfitriona 326 × 180 dp; saludo y firma en Allura; cuerpo 16 dp; desplazable si es larga. Sólo ✕. Volver conserva la hoja y la selección.

### 5.8 Ficha de personaje
- Hoja alta. Busto grande 160 × 240 dp que sobresale por arriba; nombre 24 dp; **una línea de carácter** y la **casa** con su color; cinco habilidades (icono, nombre, cinco puntos); **compromisos de la semana** con fichas de fecha; sección «Lo que sabes» (confidencias, desplazable).
- No muestra orientación, compatibilidad ni secretos.

### 5.9 Aviso al comenzar
- Sólo si quedan invitaciones opcionales sin responder: hoja pequeña «Quedan 2 invitaciones sin responder. Se declinarán con cortesía.» · [Revisar] [▶ Comenzar].

### 5.10 Mapa · semana en marcha
- **Transición de día** (1 s): la ficha del nuevo día crece al centro y vuelve a su sitio en la barra.
- Las cabezas de viaje, **a color** porque están activas, recorren rutas punteadas desde su residencia. En la tira esas mismas personas aparecen en blanco y negro con el emblema del destino: la tira dice «no disponible», el mapa dice «aquí está».
- Aros de progreso oro alrededor del sello del lugar.
- ❚❚ y ▶▶ en la barra. Movimiento reducido en ajustes.

### 5.11 Incidente
- El mapa se pausa y se atenúa. Hoja con ficha de fecha, lugar, **bustos de los implicados con su expresión** (molesta, ruborizada…), situación en 2 líneas, una cita, **tres opciones** de 56 dp mínimo con palabra clave en `oro` y la habilidad en versalitas a la derecha. No se cierra sin decidir.

### 5.12 Reemplazo
- Causa (busto del indispuesto en blanco y negro + termómetro), hueco libre con borde oro discontinuo, tira desplazada para mostrar a los disponibles (a color y con halo), y las dos alternativas válidas: **asistencia reducida** y **retirada con disculpas**. Sólo se ofrecen opciones posibles.

### 5.13 Resultado (sólo eventos mayores)

Se muestra a pantalla completa sólo para **incidentes y obligatorias**. El resto deja un sobre con lazo en el mapa y se repasa en el cierre (evita cuatro ventanas seguidas por semana).

**Sustituye el cartel rojo «ÉXITO».** El desenlace se comunica con tres cosas delicadas:

1. **Un sello de cera pequeño** (40 dp) que se estampa con pétalos, en un color que resume el tono:
   - `oro` + «Velada lograda» (favorable)
   - `glicinia` + «A medias» (mixto)
   - `tinta-suave` + «Un desaire» (desfavorable)
2. **Un título narrativo** («La velada se salva»), no una palabra de misión.
3. **La reacción** del personaje con su busto y su expresión, en el componente de diálogo.

Debajo, dos bloques: **«Lo que se comenta»** (hechos públicos) y **«Sólo tú lo sabes»** (privado). Una acción: sello ✓.

### 5.14 Sobre de resultado menor
- Al tocar el sobre con lazo en el mapa: hoja pequeña con el título, una línea y los cambios. Es opcional leerlo antes del cierre.

### 5.15 Cierre · Crónica de salones (público)
- Pliego impreso de sociedad (guiño al papel de chismes de Bridgerton, con identidad propia): cabecera tipográfica con guirnalda, fecha, tres noticias breves de la semana escritas con malicia, y al pie **la reputación de la casamentera** con sus motivos («+1 · La casa Serravalle habla bien de su recepción»). Sólo hechos que la sociedad pudo conocer.

### 5.16 Cierre · Sólo para tus ojos (privado)
- Sobre lacrado que se abre: vínculos que avanzaron, confidencias nuevas, ánimo de cada persona (con su busto). Lo privado no suma reputación.

### 5.17 Nueva semana
- Animación: llegan los sobres volando a sus lugares; la barra pasa a `S2/6` con los nuevos días. Vuelta a 5.4.

### 5.18 Pausa y ajustes
- Hoja desde ⚙: idioma ES/EN, tamaño de texto, velocidad, movimiento reducido, música/efectos, guardar y salir.

---

## 6. Revisión crítica: qué se optimiza respecto a v2

| v2 | v3 | Por qué |
|---|---|---|
| Cartela «Día 27 / 27 – 30 · Otoño temprano» | Barra con `S1/6`, cuatro fichas de día y contador ✉ | Tres textos que no ayudaban a decidir pasan a ser información accionable |
| Número suelto bajo el nombre del lugar; rangos «28–30» | Hoja de almanaque con el día de inicio a la izquierda del nombre; duración dentro de la hoja | Se lee como calendario antiguo y nunca se deforma con rangos |
| Todos los sellos con la misma flor | Icono por tipo de evento + estado | El icono ahora dice algo |
| Retratos 62 × 78 dp con cinta de texto | Tarjetas 104 × 156 dp, B/N cuando no están disponibles, emblema | Se valora el arte y el estado se ve sin leer |
| Medallas de batería y caritas | Expresión del retrato | Se aprovechan las expresiones que ya se producen |
| Reloj de arena aparte | ▶ en la barra superior | Una sola ubicación para el tiempo |
| Cartel «ÉXITO» rojo | Sello de cera pequeño + título narrativo + reacción | Delicadeza de salón, no misión |
| Cuatro resultados seguidos | Sólo mayores a pantalla completa; menores como sobre | Menos interrupción |
| Proclamación como muro de texto | Diálogo con busto, tres frases | Alguien habla; el jugador escucha |
| Verde, granate, marrón, sepia | Marfil, tinta azul, azul seda, rosa, glicinia, oro fino | Bridgerton en vez de estrategia histórica |
| Adornos sin función (◦◇◦) | Flores sólo en momentos ceremoniales | Cada adorno en su lugar |

---

## 7. Lista de imágenes a producir (con tamaños)

Todo lo que es texto, número, radar, ruta, aro, icono, sello o marco simple se construye en el motor o en vector. **Sólo se genera arte pintado.**

### 7.1 Personajes

Una **ilustración maestra por persona y expresión**, con encuadre fijo para poder recortar todos los tamaños desde la misma imagen.

| Recurso | Tamaño | Fondo | Cantidad |
|---|---|---|---|
| Original formal (busto hasta la cadera, encuadre amplio) | **1536 × 2304 px** (2:3, objetivo) | Transparente | 8 |
| Pose de ficha (editada desde el original aprobado) | 1536 × 2304 px (objetivo) | Transparente | 8 |
| Expresiones (alegre, molesta, ruborizada; cada una desde el original) | 1536 × 2304 px (objetivo) | Transparente | 24 |

Regla de encuadre de la maestra (para que la tira quede alineada):

- Coronilla al 6 % del alto (incluido peinado y tocado).
- Línea de ojos al **20 %** del alto.
- Barbilla al 31 %; cadera en el borde inferior.
- Cara centrada en horizontal (±3 %).
- Manos dentro del lienzo si actúan.

Recortes derivados (no se generan aparte):

| Uso | Tamaño en dp | Recorte desde la maestra | Exportación @3× |
|---|---|---|---|
| Tarjeta de la tira | 104 × 156 | Centro, ancho 50 %, alto 0–50 % | 312 × 468 |
| Hueco de hoja | 72 × 108 | Igual que la tarjeta | 216 × 324 |
| Ficha / diálogo | 160 × 240 / 220 × 330 | Centro, ancho 62,5 %, alto 0–62,5 % | 480 × 720 / 660 × 990 |
| Cabeza de viaje en el mapa | 44 × 56 | Centro, ancho 30 %, alto 2–29 % | 132 × 168 |

La tarjeta de la tira necesita fondo: se le añade en el motor un fondo pintado común (seda azul con luz), no se genera uno por personaje.

| Recurso | Tamaño | Fondo | Cantidad |
|---|---|---|---|
| Reina Maela Aurenza | 1536 × 2304 | Transparente | 1 base + 2 expresiones = 3 |
| Guía | 1536 × 2304 | Transparente | 1 base + 3 expresiones = 4 |
| Fondo de tarjeta (seda pintada) | 312 × 468 | Opaco | 1 |

### 7.2 Mapa de Valcenda

| Recurso | Tamaño | Fondo | Cantidad |
|---|---|---|---|
| Terreno base (calles, río, puente, parques, sin edificios principales) | **~2304 × 3456 px** (768 × 1152 dp, proporción 2:3 como el generador; mayor que la pantalla para desplazarse) | Opaco | 1 |
| Edificio de lugar (salón de baile, jardines, teatro, residencia, academia, palacio) | ~600 × 540 px | Transparente | 6 |
| Capa de ambiente (copas otoñales, hiedra, barcas) | 2304 × 3456 | Transparente | 1 (opcional) |
| Variante de noche | Tinte en motor sobre las mismas capas | — | 0 imágenes nuevas |

Dirección del mapa: vista oblicua elevada, fachadas pastel tipo Bath, **primer otoño** (árboles verdes con copas ámbar y rojizas, sin floración primaveral), luz de mañana, sin dominante amarilla. El mapa se desplaza bajo capas fijas de interfaz; cada edificio de lugar debe poder centrarse en la zona útil. Cámara y escala comunes para todas las capas.

### 7.3 Ilustraciones de cartas y portada

| Recurso | Tamaño | Fondo | Cantidad |
|---|---|---|---|
| Grabado de casa anfitriona (cabecera de carta) | 978 × 540 px (326 × 180 dp) | Opaco | 6 casas + Corona = 7 |
| Portada | **1290 × 2796 px**, zona segura central 1080 × 2160 | Opaco | 1 |
| Cabecera de la Crónica (grabado pequeño) | 978 × 300 px | Opaco | 1 |

### 7.4 Ornamento (pintado o vector)

| Recurso | Tamaño | Cantidad |
|---|---|---|
| Ramillete de esquina (flores de primer otoño) | 360 × 360 px, transparente | 1 (se refleja) |
| Damasco floral para la tira | 512 × 512 px, mosaico continuo | 1 |
| Textura de papel marfil (9 zonas) | 288 × 288 px | 1 |
| Guirnalda de portada | 1080 × 400 px, transparente | 1 |

### 7.5 Recuento

| Grupo | Imágenes |
|---|---|
| Elenco (8 × 5: original, pose de ficha, 3 expresiones) | 40 |
| Reina y guía | 7 |
| Mapa (terreno, 6 edificios, ambiente) | 8 |
| Cartas, portada, Crónica | 9 |
| Ornamento | 4 |
| Fondo de tarjeta | 1 |
| **Total** | **69** |

Escalabilidad: cada **personaje nuevo** cuesta 5 imágenes; cada **casa anfitriona nueva**, 1; cada **lugar nuevo**, 1 edificio. Iconos, sellos, radar, rutas y textos no generan imágenes.

---

## 8. Pendiente de decidir por el usuario

1. Quién es el **guía** (persona, oficio, relación con la casamentera).
2. Si existen **trajes de ocasión** (propuesta: un traje de temporada por persona; traje de baile sólo para el gran baile).
3. Nombre de la **Crónica de salones** y quién la escribe dentro del mundo.
4. Si la **vela de cansancio** existe como mecánica (si no, se omite).
5. Nombres de los **lugares** según los barrios de Valcenda (Alto Laurel, Canal de Serel…).

---

## English summary

The city map is the only screen; every task is an overlay. The cast strip (200 dp tall, 104 × 156 dp portrait cards, colour = available, black-and-white + venue emblem = busy, single word only for altered states) doubles as roster, guest picker and status board. A top week bar (week 1/6, four calendar day tiles, replies counter and the start-week seal) replaces the decorative date cartouche and any calendar screen. Calendar-style date tiles are reused in the bar, map labels, event sheets and character sheets. The palette moves from dark green/burgundy/brown to Bridgerton silks: ivory, navy ink text, silk blue, rose, wisteria, mint, fine gold. Florals are reserved for ceremonial moments. Outcomes are told with a small wax seal, a narrative title and a character reaction, never a red "SUCCESS" stamp. Only major results interrupt; minor ones wait as envelopes for the weekly close (public "Salon Chronicle", then private "For your eyes only"). Painted assets: 61 images (8 characters × 4 expressions from a fixed-framing 1536 × 2304 master, queen, guide, layered map, house letterheads, title art, ornaments); everything else is built in-engine or as vectors.
