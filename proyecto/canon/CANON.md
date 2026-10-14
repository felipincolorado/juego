# Salverna · Canon de la Temporada del Sello (v1)

**13 de octubre de 2026 · Base de trabajo para producir textos y programar.**

- Resume y cierra lo que estaba abierto en `diseno/` y en la entrega integral v0.3 (`produccion/fuentes/`).
- Las decisiones tomadas por defecto están en [`produccion/DECISIONES.md`](<../../produccion/DECISIONES.md>) y llevan la marca **(D#)**.
- Los nombres o hechos inventados aquí se marcan como **(nuevo)**.
- Si algo de este archivo contradice a `diseno/`, manda este archivo.

> **Verdad de autor.** Este documento contiene secretos (orientaciones, la autoría de la *Hoja*, condiciones). Nada de esto se muestra en la interfaz salvo cuando el juego lo revela.

---

## 1. Premisa

- La reina **Maela Aurenza** abre la **Temporada del Sello**: seis semanas del primer otoño en **Valcenda**, la capital.
- Novedad de este año, ligada a su reforma de los registros: **las uniones que se acuerden en la temporada se sellarán en el Archivo renovado durante el Gran Baile final**.
- Encarga a **la casamentera** (la jugadora) guiar a ocho jóvenes adultos de casas y orígenes distintos.
- La casamentera no tiene nombre, retrato ni rasgos. El texto la trata en femenino y de «usted».
- Desde la semana 2 circula ***La Hoja sin Firma***, un pliego anónimo que revela secretos de los salones. A mitad de temporada insinúa que **sobrevivieron páginas del Pacto del Umbral**, el documento perdido en el incendio del Archivo (la «Noche del Censo», hace 80 años) que protegía identidades sobrenaturales.

**Las tres preguntas de la temporada:**
1. ¿Con quién y cómo acaba cada uno de los ocho?
2. ¿Quién escribe *La Hoja sin Firma* y qué quiere?
3. ¿Qué queda sellado en el Archivo y qué secretos sobreviven?

**Tono.** Ingenio de salón, ternura y presión social, como Bridgerton, pero en un mundo propio.
- Lo fantástico existe y es público. Lo secreto son identidades concretas.
- **El romance llega como máximo a un beso.**

---

## 2. Registro y estilo (obligatorio en todos los textos)

| Regla | Español | English |
|---|---|---|
| Trato en sociedad | «usted» / «ustedes». **Nunca «vos» ni «vosotros»**. | Formal, sin arcaísmos: *Miss Lobreda*, *Mr. Veyra*, *Your Majesty* |
| Trato en confianza | «tú», cuando el vínculo llega al nivel B | El nombre de pila |
| El elenco a la casamentera | Siempre «usted». **Excepción: Nilo** se le escapa el «tú» y a veces se corrige | *you*. Nilo es más familiar |
| La reina a la casamentera | «usted» | *you* |
| Tratamientos | «Su Majestad», «señorita», «señor», «señora» (Camila es viuda) | *Your Majesty*, *Miss*, *Mr.*, *Mrs. Ferrán* |
| Largo de las frases | Comentarios del mapa: menos de 14 palabras. Desenlaces: hasta 22. Diálogo: un máximo de 3 líneas por toque | Igual |
| Idiomas | El español es la versión maestra. El inglés **adapta la intención**: no traduce palabra por palabra y conserva el humor | — |

**Prohibido en cualquier imagen:** que la orientación se lea en el aspecto. No se usan estereotipos de «marimacho» o de «afeminado»: las damas son igual de refinadas entre sí y los caballeros, igual de elegantes. La personalidad se muestra en la expresión y en la ropa, nunca en códigos de orientación.

**Prohibido en cualquier texto:**
- Afirmar una orientación o una condición antes de que el juego la revele.
- Colmillos o rasgos de lobo.
- Contar como ocurrido algo que la persona que habla no pudo saber.
- Carteles de «éxito» o «fracaso».
- Lenguaje de misión militar («objetivo cumplido»).

---

## 3. El elenco

### 3.1 Datos de juego

Las habilidades van de 0 a 5. Los ejes de carácter van de −2 a +2:
- **Eje 1:** −2 = deber, +2 = libertad.
- **Eje 2:** −2 = ingenio, +2 = sinceridad.

| ID | Nombre | Edad | Casa (color) | Baile | Estatus | Chisme | Presencia | Intelecto | Eje 1 | Eje 2 | Le gusta | No le gusta | Orientación (oculta) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `nilo` | Nilo Lobreda | 26 | Lobreda · verde bosque | 2 | 3 | 2 | 4 | 3 | +1 | +2 | paseo | cena | hetero |
| `saul` | Saúl Veyra | 30 | Veyra · azul acero | 3 | 4 | 1 | 3 | 3 | −2 | +1 | recepcion | teatro | gay |
| `dario` | Dario Miravés | 27 | Miravés · ciruela | 5 | 2 | 3 | 3 | 1 | 0 | −2 | baile | paseo | bi |
| `teo` | Teo Rovena | 24 | Rovena · rosa malva | 2 | 2 | 5 | 2 | 3 | +1 | −2 | teatro | baile | hetero |
| `celia` | Celia Lobreda | 21 | Lobreda · verde salvia | 5 | 3 | 1 | 2 | 3 | −2 | +1 | clase | paseo | hetero |
| `irene` | Irene Salvat | 25 | Archiveros · gris carbón | 1 | 2 | 3 | 3 | 5 | −1 | +2 | cena | baile | bi |
| `isolda` | Isolda Marén | 23 | Marén · amarillo prímula | 3 | 2 | 3 | 2 | 4 | −1 | +2 | paseo | recepcion | lesbiana |
| `camila` | Camila Ferrán | 29 | Ferrán · lavanda y gris perla | 2 | 4 | 4 | 2 | 2 | +1 | −1 | cena | clase | hetero |

**Damas y caballeros** (para la regla de los bailes de cortejo):
- Caballeros: Nilo, Saúl, Dario, Teo.
- Damas: Celia, Irene, Isolda, Camila.

### 3.2 Fichas resumidas

| Persona | Atractivo | Deseo de la temporada | Contradicción | Secreto o carga | Arco: si crece / si se tuerce |
|---|---|---|---|---|---|
| **Nilo** | Calidez sin cálculo | Ser útil en Valcenda por sí mismo, no como «el Lobreda de los pasos» | Promete antes de medir el coste | **Lunario** (condición heredada): se transforma, sin poder evitarlo, la noche de plenilunio | Aprende a medir lo que promete y confía su secreto a alguien / Sus promesas lo arruinan y su secreto sale a la luz |
| **Saúl** | Aplomo; lo poco que deja ver vale mucho | Cerrar un acuerdo que proteja su posición sin traicionarse | Cumple deberes; le cuesta reconocer lo que desea | Gay, sin decirlo; se refugia en el deber | Reconoce lo que desea / Se refugia en el deber y se marcha |
| **Dario** | Misterio cortés | Retrasar la herencia sin enfrentarse a su tía **Amalia Miravés** | Domina la cortesía y evita la intimidad | **Humano (D4).** Conoce los secretos de la rama nocturna de su familia: Amalia es nocturna. Llevó la reclamación de la deuda contra los Ferrán | Deja que alguien lo conozca / Se cierra del todo y acepta la herencia sin quererla |
| **Teo** | Humor, y de pronto una mirada seria | Que la casa Rovena vuelva a ser invitada a todas partes (los molinos pasan una mala racha) | Divierte a todos para evitar una conversación sincera | Debe dinero a Nilo y a medio Lumbrevía | Tiene una conversación sincera / Se convierte en el bufón de los salones |
| **Celia** | Disciplina convertida en gracia | Destacar por mérito propio, no ser «la prima de Nilo» | Depende de la aprobación ajena | Guarda una lista de quienes la miraron mal en un salón | Baila por gusto / Se quiebra ante un error público |
| **Irene** | Atención total | Acceder a los archivos privados de las casas | Entiende los argumentos mejor que las insinuaciones | **Es la autora de *La Hoja sin Firma* (D5)**, ver §6 | Se arriesga a ser vista y publica sólo los abusos / Usa lo que sabe contra otros |
| **Isolda** | Dulzura tímida; cuando habla, todos se callan para oírla | Atreverse a hablar primero, una sola vez, de algo que quiere | Calcula todos los riesgos y nunca corre el suyo | Hija de aseguradores de Puerto Nácar; su familia pagó el seguro del barco Ferrán. Está enamorada en silencio y no se lo ha dicho a nadie | Dice en voz alta lo que quiere / Se casa por conveniencia y calla |
| **Camila** | Experiencia y humor seco | Decidir sola su siguiente paso tras el luto | Dice no necesitar a nadie y echa de menos que la sorprendan | Su fortuna viene del seguro Marén por el barco hundido de su marido; la casa Miravés le reclama la deuda de ese barco, que **vence en la semana 5** | Se deja sorprender / Se queda observando, sola |

**Datos fijos nuevos:**
- **Celia es rubia miel** (corrección del usuario del 13 de octubre: la pelirroja recordaba demasiado a un personaje conocido y repetía el pelo de Teo). Se mantiene su recogido alto con ramitas.
- **Irene es de origen asiático oriental** (petición del usuario). Viste **gris carbón**, no azul, para no recordar a un personaje conocido.
- El difunto marido de Camila es **Julián Ferrán** (nuevo). Su barco, el *Clara de Nácar* (nuevo), se hundió hace dos otoños.
- **Camila es la carabina de Celia** esta temporada. Es **sólo narrativo**: aparece en las escenas y en los comentarios, pero no obliga a enviarlas juntas.

### 3.3 Uniones y vínculos previos

La matriz de las 28 parejas está en `diseno/RELACIONES-Y-UNIONES-PROPUESTA.md` §2.

**Tipos de unión:**
- **A. Mutua:** los dos pueden sentirse atraídos.
- **B. Lavanda:** Saúl con Isolda.
- **C. Desigual:** sólo uno siente.
- **D. Compañía:** ninguno siente.

**Excepciones:**
- Nilo y Celia son primos. Su ruta es secundaria y se puede desactivar con `ajustes.ruta_primos` (D6).
- El motivo de la unión lavanda es la **alianza de convoyes (D3)**: la concesión Veyra en Tiria necesita que una aseguradora de Nácar respalde sus convoyes, y los Marén piden un vínculo formal.

**Cercanía de partida** (puntos, ver sistemas §4):

| Pareja | Puntos | Por qué |
|---|---|---|
| Celia–Camila | 2 | Carabina |
| Dario–Isolda | 2 | Amigos de infancia en el puerto; él la defendía cuando ella no se atrevía a hablar |
| Nilo–Celia | 2 | Primos |
| Nilo–Teo | 1 | Taberna y deuda |
| Nilo–Saúl | 1 | La tormenta en el paso |
| Saúl–Dario | 1 | Negociaron el préstamo Veyra |
| Teo–Camila | 1 | Teo fue protegido de su difunto marido |
| Irene–Isolda | 1 | Los registros portuarios de su abuela, que Irene buscó tres semanas más de lo necesario |
| Resto | 0 | — |

---

## 4. Personajes recurrentes (no se emparejan)

| ID | Persona | Papel en la temporada |
|---|---|---|
| `reina` | **Maela Aurenza**, reina | Abre la temporada, interviene en la semana 3 y en el Gran Baile, y sella las uniones. Habla poco y con peso |
| `nota` | **La asistente** de la casamentera | Nunca se ve. Habla con notas manuscritas en el tutorial y en momentos clave |
| `mara` | **Mara Calce**, editora | Imprime la ***Crónica de salones*** (el pliego de sociedad legal y de cada semana). **Pista falsa** de la *Hoja*: todos la sospechan |
| `leonora` | **Leonora Serravalle** | Anfitriona de los Jardines Serravalle y de la cena de las deudas (semana 5) |
| `ines` | **Inés**, cantante de los salones | Da la lección de baile y de música de las semanas 1, 3 y 5 |
| `mireya` | **Mireya** | Organiza las listas de invitados de palacio. Sabe quién faltó y quién llegó tarde |
| `bruna` | **Bruna** | Cuidados. Atiende a quien queda indispuesto |
| `amalia` | **Amalia Miravés** | Tía de Dario y cabeza de la casa. Nocturna en secreto. Aparece desde la semana 3 |

---

## 5. Lugares de Valcenda (marcadores del mapa)

| ID | Lugar | Barrio | Tipo de edificio | Arte |
|---|---|---|---|---|
| `palacio` | Palacio de Alto Laurel | Alto Laurel | Palacio | Edificio propio |
| `salon` | Salón de las Columnas (nuevo) | Alto Laurel | Salón de baile | Edificio propio |
| `jardines` | Jardines Serravalle | Alto Laurel, junto al río | Jardines | Edificio propio |
| `teatro` | Teatro del Puente (nuevo) | Junto al puente del Lumbre | Teatro | Edificio propio |
| `academia` | Academia de la Puerta de Greda (nuevo) | Puerta de Greda | Academia | Edificio propio |
| `residencia` | La residencia de la casamentera | Alto Laurel, cota baja | Residencia | Edificio propio |
| `imprenta` | Imprenta Calce | Calle de los Sellos | Lugar menor | Sólo marcador |
| `archivo` | Archivo Real | Calle de los Sellos | Lugar menor | Sólo marcador |
| `muelles` | Muelles del Canal de Serel | Canal de Serel | Lugar menor | Sólo marcador |

---

## 6. Calendario y verdad del misterio

**Días:**
- Cada semana de juego son **4 días de salón, de jueves a domingo**. De lunes a miércoles no se juega.
- Meses de otoño (nuevo): **Vendimias** (30 días) y **Nieblas**.

| Semana | Días | Hecho del reino | Evento obligatorio | Gancho de cierre |
|---|---|---|---|---|
| 1 · Apertura | Vendimias 27–30 | Proclamación real | Recepción de apertura (palacio, día 29) | Sobre sin firma en la residencia |
| 2 · Primeras impresiones | Nieblas 4–7 | Cobros de otoño | Baile de las casas (salón) | Primera *Hoja*: un secreto menor de quien tenga más fama pública |
| 3 · Noche de los Faroles | Nieblas 11–14 | Conmemoración del incendio | Velada de los Faroles (muelles) | La *Hoja* insinúa que hay páginas del Pacto |
| 4 · Luna llena | Nieblas 18–21 | **Plenilunio la noche del 20 (D13)** | Teatro de gala (teatro, día 20) | «Alguien de los salones no es lo que aparenta» |
| 5 · Cierre de Cuentas | Nieblas 25–28 | Tormentas de Nácar; vence la deuda Miravés–Ferrán; orden de Tiria para Saúl | Cena de las deudas (jardines) | Saúl podría tener que irse |
| 6 · Gran Baile del Sello | Escarchas 2–5 (mes siguiente, nuevo) | La reina sella las uniones | Gran Baile del Sello (salón, día 5) | Se revela la autoría; propuestas; epílogo |

**Verdad de *La Hoja sin Firma* (D5):**
- **Autora: Irene Salvat.**
- En el Archivo encontró pruebas de que varias casas **alteraron parentescos y propiedades** aprovechando el incendio. La reforma de la reina exige copias accesibles, pero sus superiores entierran esos folios.
- Publica de forma anónima para forzar que salgan a la luz. Imprime de noche en un taller de Arcos Bajos.
- **El riesgo:** entre esos folios hay **fragmentos del Pacto del Umbral** con nombres de condiciones protegidas, entre ellas la línea lunaria de los Lobreda.
- Su arco decide si publica sólo los abusos o también las identidades.

**Pistas que debe poder leer el jugador**, siempre legibles y nunca castigadas:
1. La *Hoja* cita números de folio con exactitud de archivera.
2. Aparece al día siguiente de las visitas de Irene al Archivo.
3. Usa su construcción favorita («Interesante. ¿Por qué…?»).
4. El papel es de los cuadernillos de descarte del Archivo.
5. **Pista falsa:** Mara gana lectores con cada *Hoja*.

**El sobre de la semana 1** lo deja Irene. Es una advertencia a la casamentera, sin firma y con un número de folio. Ver `datos/semanas/semana1.yaml`.

---

## 7. Lo que no cambia de la entrega integral

- El mapa es la única pantalla y el elenco se ve siempre.
- Primero se planifica la semana y después se ejecuta por fechas.
- Éxito social, afinidad, deseo y consentimiento son cosas distintas: **una tirada nunca impone deseo**.
- La reputación de la casamentera sólo recoge lo que la sociedad pudo saber.
- Las uniones se deciden en el Gran Baile, con el carnet de baile.


---

## 8. Cambio de personaje: Isolda (14 oct.)

Decisión del usuario, a partir del original nuevo:
- **Aspecto:** pelo castaño ondulado medio recogido, pluma amarilla en el peinado, ojos ámbar, vestido amarillo pálido con florecitas azules.
- **Carácter:** **tímida y dulce**.
- **Deja de ser velaria.**

Su función en la historia se mantiene: es la dama lesbiana, el romance prioritario con Irene y el posible acuerdo lavanda con Saúl. Ahora es más fuerte, porque los dos esconden lo que sienten. Su color de casa pasa a **amarillo prímula** (`#D9C46A`).

## 9. Calendario corregido (semanas de 7 días)

| Cap. | Días |
|---|---|
| 1 | Vendimias 24–30 |
| 2 | Nieblas 1–7 |
| 3 | Nieblas 8–14 |
| 4 | Nieblas 15–21 (plenilunio el 20) |
| 5 | Nieblas 22–28 |
| 6 | Nieblas 29 – Escarchas 5 (Gran Baile el 5) |

Esta tabla **reemplaza** las fechas del §6. Los meses tienen 30 días.
