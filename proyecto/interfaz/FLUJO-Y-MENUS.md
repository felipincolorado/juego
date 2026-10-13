# Salverna · Flujo, menús y capas (v1)

**Fuentes:**
- `diseno/ESPEC-FLUJO-PANTALLAS-v3.md`: tamaños, componentes y estados.
- Figma «JUEGO», marcos v4: carta del elenco `83:509`, introducción `83:515` y mano de cartas `83:536`.

Los textos se piden con `ui("…")` a `datos/textos/ui.yaml`. **Si este documento contradice la especificación v3, manda este**, porque recoge las decisiones posteriores:
- El elenco es una **mano de cartas en arco**, no una tira.
- La ficha **sube desde abajo, por detrás de las cartas**.
- Las habilidades se muestran en un **pentágono**, no con puntos.

---

## 1. Principio

**El mapa de Valcenda es la única pantalla.** Todo lo demás son capas encima de él:
- **Hojas** que suben desde abajo.
- **Lectura a pantalla completa:** carta, Crónica y diálogo.
- **Avisos pequeños.**

No hay pestañas, ni barra de navegación, ni pantalla de calendario.

## 2. Árbol completo

```
PORTADA  (ui.portada.*)
├─ Nueva temporada ─► [¿sobrescribir la partida?] ─► APERTURA
├─ Continuar (sólo si hay partida) ─► MAPA en la fase guardada
├─ ⚙ Ajustes ─► AJUSTES
└─ ES · EN (cambio inmediato)

APERTURA (diálogo con la reina) ─► notas de la asistente ─► REPARTO DE CARTAS ─► MAPA · PLANIFICACIÓN (tutorial)

MAPA · PLANIFICACIÓN
├─ Barra superior: ⚙ · S1/6 · cuatro fichas de día (tocar = filtrar el mapa) · ✉ n/total · sello ▶
├─ Marcador ─► HOJA DE EVENTO
│     ├─ ✉ ─► CARTA (pantalla completa; ✕ vuelve a la hoja con la selección intacta)
│     ├─ tocar carta de la mano ─► se asigna al primer hueco libre
│     ├─ tocar cara en un hueco ─► se retira
│     ├─ sello ─► respondida (se puede cambiar hasta comenzar)
│     └─ «Declinar con cortesía» (sólo opcionales)
├─ Marcador con varias invitaciones ─► MINI AGENDA ─► HOJA DE EVENTO
├─ Carta de la mano (sin hoja abierta) o mantener pulsado ─► FICHA (sube por detrás de las cartas)
├─ Residencia ─► CARTAS GUARDADAS (proclamación, sobre sin firma, Hojas…)
└─ Sello ▶ ─► [AVISO si quedan opcionales sin responder] ─► MAPA · EJECUCIÓN

MAPA · EJECUCIÓN
├─ Barra: ❚❚ pausa · ▶▶ rápido
├─ Cambio de día ─► salen los viajes ─► aros de progreso
├─ Aro «!» ─► INCIDENTE (obliga a decidir) ─► RESULTADO MAYOR
├─ Aro «!» por indisposición ─► REEMPLAZO
└─ Aro completo ─► sobre con lazo en el mapa ─► RESULTADO MENOR (opcional)

CIERRE
├─ CRÓNICA DE SALONES (lo público y la reputación)
├─ SÓLO PARA SUS OJOS (vínculos, confidencias, ánimo)
├─ ESCENAS DE VÍNCULO (desde la semana 2, 2 como máximo)
├─ GANCHO de la semana (escena o carta)
└─ NUEVA SEMANA: llegan los sobres ─► MAPA · PLANIFICACIÓN

SEMANA 6 ─► GRAN BAILE ─► CARNET DE BAILE ─► propuestas ─► sellos de la reina ─► CRÓNICA FINAL ─► EPÍLOGOS ─► CRÉDITOS ─► PORTADA
```

## 3. Capas y su comportamiento

| Capa | Tipo | Cómo se cierra | ¿Pausa el tiempo? | Claves de interfaz |
|---|---|---|---|---|
| Hoja de evento | Hoja inferior; deja ver la barra y la mano | ✕, tocar fuera o deslizar hacia abajo | Sólo existe en la planificación | `hoja.*` |
| Carta | Pantalla completa, papel con margen de 10 dp | ✕ | — | `carta.*` |
| Ficha | Sube **por detrás de la mano de cartas**. La carta de esa persona queda delante, elevada | ✕ o deslizar hacia abajo | Sí, en la ejecución | `ficha.*` |
| Mini agenda | Hoja pequeña | ✕ o tocar fuera | — | `mapa.mini_agenda.*` |
| Aviso al comenzar | Hoja pequeña | Revisar / Comenzar | — | `aviso_comenzar.*` |
| Incidente | Hoja; el mapa se atenúa | **No se cierra** sin elegir | Sí | `incidente.*` |
| Reemplazo | Hoja | No se cierra sin elegir | Sí | `reemplazo.*` |
| Resultado mayor | Pantalla completa | Sello ✓ | Sí | `resultado.*` |
| Resultado menor | Hoja pequeña | ✕ | No | `resultado.menor.*` |
| Diálogo | Busto y caja de papel | Tocar para avanzar; «Saltar» en las escenas ya vistas | Sí | `dialogo.*` |
| Crónica y «Sólo para sus ojos» | Pantalla completa | Botón «Seguir» | — | `cierre.*` |
| Ajustes | Hoja alta | ✕ | Sí | `ajustes.*` |

## 4. La mano de cartas

- Como en el marco v4 de Figma (`83:536`), las cartas van **en fila horizontal con un leve arco**.
  - Se ven unas 3,5 cartas de 104 × 156 dp y la mano **se desliza** para ver al resto.
  - La media carta del borde indica que hay más.
  - Con ocho cartas a la vez en 390 dp, las caras quedarían demasiado pequeñas: se descartó.
- Cada carta mide 2:3. El nombre va abajo, en una **placa a todo lo ancho**, del color de su casa.
- Los estados y las reglas de toque son los de la especificación v3 §3.4:
  - **Blanco y negro:** ocupada o de viaje.
  - **Banda frambuesa con una palabra:** alterada.
  - **Sacudida:** no puede ir a ese evento.
- Con una hoja de evento abierta, tocar una carta la hace **volar al hueco** (tiene la misma proporción 2:3) y en la mano queda su silueta en blanco y negro.

## 5. La ficha

Sube desde abajo, por detrás de las cartas. **El busto de la pose de ficha** asoma por arriba. Secciones, de arriba abajo:
1. Nombre, casa (con su color) y la `linea` de la persona (`personajes.yaml`).
2. **Pentágono** de habilidades. Al tocarlo, sale el valor de cada eje.
3. **Ficha técnica:** edad, casa, gustos y disgustos, ambos **sólo cuando el jugador ya los ha descubierto**.
4. **Biografía** (`fichas.yaml → biografia`).
5. **Compromisos de la semana**, con fichas de fecha.
6. **Lo que usted sabe:** las 6 entradas. Las bloqueadas muestran sólo su título.
7. **Diario de la temporada**, plegado por defecto.

**Nunca muestra** orientación, compatibilidad, cercanías numéricas ni secretos.

## 6. Accesibilidad

- Todo control que sólo tiene icono lleva su etiqueta para lectores de pantalla (`ui.accesibilidad.*`).
- Ningún estado se comunica sólo con color: siempre hay un icono o una palabra.
- **Tamaño de texto** (100, 115 y 130 %), **movimiento reducido** (sin vuelo de cartas ni pétalos; fundidos simples) y **velocidad**.
- Área táctil mínima de 48 × 48 dp.

## 7. Repaso del flujo (pendiente)

Cuando estén definidas las semanas, se revisará el flujo completo:
- **En Figma**, si hay capacidad; si no, en una **maqueta HTML navegable** a tamaño de teléfono.
- **Se medirá:** toques por semana, ventanas que interrumpen y tiempo hasta la primera decisión.
