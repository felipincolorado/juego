# Salverna · Sistemas de juego con números (v1)

**13 de octubre de 2026.** Propuesta de balance lista para programar: cada valor es un parámetro, con su nombre entre `comillas`. Hay que ajustarlo jugando. Lo que no está aquí no existe en la versión 1.

**Principio:** los resultados son **deterministas y legibles**.
- El pentágono enseña lo que se pide y lo que se lleva. El jugador debe poder prever el resultado.
- El resultado se calcula **una sola vez**, al resolver, y se guarda. La animación sólo lo muestra.
- El azar no existe salvo en un caso: elegir la variante de texto, con semilla fija por partida.

---

## 1. Tiempo

| Elemento | Regla |
|---|---|
| Temporada | 6 semanas |
| Semana | 7 días visibles en el calendario (lunes a domingo). Los eventos de la versión 1 caen de jueves a domingo; un evento largo puede ocupar varios días |
| Fases de la semana | **Planificación**: el tiempo está parado → **Ejecución**: los días corren solos → **Cierre**: Crónica y «Sólo para sus ojos» |
| Duración de la animación | `seg_por_dia` = 6 s; ▶▶ multiplica por `vel_rapida` = 3. La pausa detiene todo |
| Cambio de día | La ficha del día nuevo crece en el centro (1 s); después salen los viajes de ese día |

## 2. Eventos

### 2.1 Campos

Cada evento tiene:
- `id`, `tipo`, `lugar`, `dia_inicio`, `duracion` (en días, 1 por defecto).
- `plazas`: mínimo y máximo, de 1 a 4.
- `regla`: `cualquiera` · `dama_caballero` (una dama y un caballero) · `solo_damas` · `solo_caballeros`.
- `obligatorio`: sí o no.
- `requisito`: un valor de 0 a 5 por habilidad, con 2 o 3 habilidades distintas de 0.
- `reputacion`: lo que se gana o se pierde.
- `incidente`: opcional.
- `textos`.

### 2.2 Tipos de evento

| Tipo | Icono | Plazas habituales | Cercanía que genera | Para qué sirve |
|---|---|---|---|---|
| `baile` | Abanico | 2 (dama y caballero) o 4 | **+2** por par | Romance y reputación |
| `recepcion` | Taza | 2–4 | +1 | Reputación (Estatus y Presencia) |
| `cena` | Copa | 3–4 | +1 | Vínculos y conversación (Intelecto y Chisme) |
| `paseo` | Rosa | 2–4 | +1 | Confidencias (Presencia y Chisme) |
| `teatro` | Máscara | 2–3 | +1 | Cercanía discreta |
| `clase` | Libro | 1–3 | +0 | **+1 en una habilidad** |
| `visita` | Llave | 2 (cualquiera) | **+2** | Se desbloquea en el vínculo B. Escenas íntimas |
| `encargo_real` | Corona | Según el evento | Según el evento | Eventos obligatorios de historia |

### 2.3 Conflictos de agenda

- Una persona ocupa **todos los días** del evento, de la salida al regreso.
- No se la puede asignar a dos eventos que se solapen en algún día.
- Se pueden asignar eventos distintos en días distintos.
- **Límite:** `max_eventos_semana` = 2 por persona y semana. El límite no es el cansancio: es que hay pocos días.

## 3. Resolución de un evento

### 3.1 Valor del grupo en cada habilidad

```
grupo[h] = máximo(valor[h] de los asistentes)
         + 1 si algún OTRO asistente tiene valor[h] ≥ 3
         (tope 5)
```

### 3.2 Cobertura

```
cobertura = Σ_h mínimo(grupo[h], requisito[h]) / Σ_h requisito[h]     (de 0 a 1)
base = +1 si cobertura = 1
        0 si cobertura ≥ 0,8
       −1 si cobertura ≥ 0,6
       −2 si es menor
```

### 3.3 Ánimo

Por cada asistente:
- +1 si el tipo de evento le gusta.
- −1 si no le gusta.
- −1 si está **agitado** (ver §6).

Se suma y se divide entre el número de asistentes. Se redondea **hacia cero** a −1, 0 o +1.

### 3.4 Incidente (si el evento lo tiene)

- Aparece el día `dia_incidente` (por defecto, el día de inicio).
- Ofrece **3 opciones**. Cada opción usa una habilidad y tiene una dificultad `d` de 2 a 5:
  - **Éxito:** `grupo[h] ≥ d` → +1.
  - **A medias:** `grupo[h] = d − 1` → 0.
  - **Fallo:** `grupo[h] ≤ d − 2` → −1.
- Cada opción muestra su habilidad. La interfaz **no muestra la dificultad**, pero el pentágono permite intuirla.
- **Cada opción tiene además una consecuencia propia**, que se aplica con cualquier resultado: `cercania_asistentes`, `efectos` (marcas que vuelven más tarde), `reputacion_si_exito`. La consecuencia se insinúa con una línea breve (`pista_coste`) bajo la opción.
- Así **la decisión no es sólo «la habilidad más alta»**, sino qué precio se acepta.

**Balance medido** con `herramientas/simular_eventos.py`: probando todas las combinaciones de asistentes, con la mejor opción el desenlace favorable debe quedar entre el 50 y el 85 %.
- Las parejas deben tenerlo más difícil que los grupos de 3 o 4, porque los grupos gastan más gente de la semana.
- Los eventos sin incidente sólo pueden salir favorables si el grupo cubre todo lo que se pide.

### 3.5 Desenlace

```
total = base + ánimo + incidente
favorable  si total ≥ 1        → sello oro, «Velada lograda»
a medias   si total = 0 o −1  → sello glicinia, «A medias»
desaire    si total ≤ −2       → sello tinta, «Un desaire»
```

| Desenlace | Reputación (evento obligatorio) | Reputación (evento opcional) | Cercanía | Ánimo |
|---|---|---|---|---|
| Favorable | +2 | +1 | +1 extra a cada par | Asistentes **alegres** |
| A medias | 0 | 0 | — | Neutral |
| Desaire | −2 | −1 | −1 a cada par (mínimo 0) | Asistentes **molestos**; quien falló la opción, **agitado** |
| Obligatorio sin asistentes | −3 | — | — | Texto de disculpas |
| Opcional declinado | 0 | 0 | — | — |

## 4. Cercanía, interés y vínculos

### 4.1 Cercanía

- Se mide por pareja, sin dirección, con valores de 0 a 20.
- Cada evento al que asisten juntas suma lo que indica su tipo, más:

```
afinidad = |eje1 A − eje1 B| + |eje2 A − eje2 B|      (de 0 a 8)
+1 si afinidad ≤ 2   (piensan parecido)
```

### 4.2 Atracción posible

Matriz de autoría y dirección (A puede sentir atracción por B), sacada de las orientaciones del canon §3.1:
- Hetero: personas del otro género.
- Gay y lesbiana: del mismo género.
- Bi: ambos géneros.
- Primos: según `ruta_primos`.

### 4.3 Niveles de vínculo

| Nivel | Cercanía | Escena | Efecto |
|---|---|---|---|
| — | 0–2 | — | Se tratan de usted |
| C · Curiosidad | ≥ 3 | Escena C | — |
| B · Confianza | ≥ 6 | Escena B | **Pasan al tú.** Se desbloquea la **visita privada** de esa pareja. Entrada 4 de la ficha |
| A · Umbral romántico | ≥ 10 **y** atracción mutua posible | Escena A | Interés romántico declarado en privado. Entrada 5 de la ficha |
| ★ Beso | Escena A vista **y** una visita privada después | Escena del beso | Marca `beso[A][B]` |
| Confesión no correspondida | A siente por B, cercanía ≥ 10 y B no puede corresponder | Escena de confesión | Marca `no_correspondido[A] = B` |

**Reglas:**
- Las escenas se reproducen **en el cierre de la semana**, desde la **semana 2**: como máximo `max_escenas_cierre` = 2 por cierre, por orden de nivel más alto.
- Las pendientes pasan a la semana siguiente.
- En la semana 1 sólo se acumula cercanía.

## 5. Reputación de la casamentera

- Empieza en 0. Suma lo que indica la tabla de §3.5, más los hechos de historia.
- **Niveles del final:**
  - ≥ 12: favorita de la Corona.
  - De 4 a 11: respetada.
  - < 4: olvidada.
- La Crónica muestra el cambio de la semana y sus motivos, sólo los públicos.
- **La reputación nunca obliga a nadie a nada.**

### 5 bis. Fama de cada joven

- **Fama** = número de desenlaces favorables en eventos públicos a los que asistió (las clases no cuentan). Suma también +1 quien abrió el baile de la recepción.
- La *Hoja sin Firma* elige al joven con más fama. En caso de empate, al primero en el orden del elenco (Nilo, Saúl, Dario, Teo, Celia, Irene, Isolda, Camila).
- La fama no se muestra con números: la Crónica la insinúa («el nombre que más se repite en los salones»).

### 5 ter. Peticiones

- Desde la semana 2, de 1 a 2 por semana. Aparecen como nota en el mapa al empezar la planificación.
- **Se cumplen** si alguien del elenco asiste al evento pedido (el propio solicitante cuenta). Efecto: ánimo alegre del solicitante en su próximo evento y +1 de cercanía con la casamentera (entrada «Lo que le gusta» de su ficha).
- **No cumplir** sólo produce el texto `si_no` en el cierre. No hay castigo de reputación: pedir es un favor, no una orden.

## 6. Estados de una persona

| Estado | Cuándo | Efecto | Duración |
|---|---|---|---|
| **Alegre / molesta / ruborizada** | Según el desenlace o la escena | Sólo la expresión del retrato | Hasta el siguiente evento |
| **Agitada** | Falló la opción de un incidente en un desaire | −1 de ánimo en su próximo evento | Hasta el cierre de la semana siguiente |
| **Indispuesta** | Sólo por guion (`indisposicion` de un evento; p. ej., la fiebre de los molinos en la semana 2) | No puede asistir; se ofrece un **reemplazo** | Los días que indique el guion |
| **Ausente por luna** | Nilo, la noche de plenilunio (Nieblas 20) | Si se le asigna algo nocturno ese día, salta el `incidente_riesgo` del evento en lugar del normal, y Nilo se va: el valor del grupo y el ánimo se calculan **sin él**. Con `celia_cubre_nilo` y Celia en el evento, la opción «cubrir» baja a d 2 (`facil_si`) | 1 noche |

No hay mecánica de cansancio en la versión 1.

## 7. Clases

- Son de tipo `clase`, de 1 a 3 plazas, en las semanas 1, 3 y 5.
- Cada asistente gana **+1 en la habilidad de la clase**, con un tope de `tope_clase` = 4 (el 5 sólo es de nacimiento).
- No tienen incidente ni desenlace.

## 8. Reemplazo

Cuando una persona asignada pasa a estar indispuesta antes de su evento, se abre la hoja de reemplazo con hasta tres salidas:
1. **Sustituir** por una persona disponible que cumpla la regla.
2. **Asistencia reducida:** se va con menos gente, si hay más que el mínimo. En un evento de regla `parejas` se permite bajar una pareja por debajo del mínimo (la pareja de quien falta se queda en casa); la cobertura se calcula con quienes van.
3. **Retirarse con disculpas:**
   - En un evento opcional: reputación 0.
   - En un evento obligatorio: −1, y la historia sigue con un texto propio.

### 8.1 Regla «parejas»

Eventos con baile de varias parejas (el Baile de las casas, el Gran Baile): igual número de damas que de caballeros. En el Baile de las casas son 4 plazas obligatorias, dos parejas. La cobertura se calcula con los cuatro, como siempre.

## 9. Gran Baile (semana 6)

1. **Intereses:** para cada persona, hasta 2 personas del elenco con cercanía ≥ 6 y atracción posible de su parte, ordenadas por cercanía.
2. **Carnet de baile:**
   - Con dos intereses, el jugador elige o marca «ninguno».
   - Con uno, se confirma.
   - Con ninguno, va a un final en solitario.
   - **Exclusividad:** quien ya tiene pareja desaparece de las demás opciones.
3. **Uniones sin amor** (lavanda, desigual o de compañía): sólo se ofrecen si la partida activó su motivo:
   - Lavanda: `motivo.lavanda` (alianza de convoyes, que se activa con la escena del acuerdo).
   - Lobreda–Veyra: `motivo.compromiso_paso`.
   - Rovena–Ferrán (Teo y Camila): `motivo.deuda`, con la escena `acuerdo_teo_camila` (cambio del 14 de octubre: antes era Miravés–Ferrán).
   - Las marcas reales son `acuerdo_lavanda`, `acuerdo_paso` y `acuerdo_deuda` (`escenas/capitulo5.yaml`).
4. **Calidad de la unión mutua:**
   - Cercanía ≥ 14: feliz.
   - De 10 a 13: cordial.
   - Menos de 10: fría.
5. **Doble beso:** si una persona besó a dos, la descartada reacciona con una escena breve antes de las propuestas.
6. Después: propuestas → sellos de la reina → Crónica final → epílogos.
   - Cada epílogo combina el **destino de cada persona** (unión o final en solitario), la **reputación** y el **hilo de la *Hoja***: autora descubierta o no, y secretos protegidos o expuestos.

## 10. Guardado

- Guardado automático **al empezar cada fase**. No se guarda a mitad de la ejecución: si se cierra la aplicación, la ejecución vuelve a empezar desde la planificación confirmada.
- 3 ranuras manuales en ajustes.
- El estado guarda:
  - semana, fase, reputación;
  - asignaciones;
  - resultados ya calculados;
  - cercanías, estados y habilidades;
  - escenas vistas, entradas de ficha desbloqueadas;
  - marcas (`beso`, `motivo.*`, `hoja.*`);
  - la semilla.

## 11. Parámetros (resumen para ajustar)

| Nombre | Valor |
|---|---|
| `seg_por_dia` | 6 |
| `vel_rapida` | 3 |
| `max_eventos_semana` | 2 |
| `umbral_C`, `umbral_B`, `umbral_A` | 3, 6, 10 |
| `union_feliz`, `union_cordial` | 14, 10 |
| `max_escenas_cierre` | 2 |
| `tope_clase` | 4 |
| `rep_favorita`, `rep_respetada` | 12, 4 |
| `ruta_primos` | sí |
