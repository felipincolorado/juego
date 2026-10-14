# Semana 4 · Luna llena

**Plenilunio.** La noche del sábado 20 hay luna llena. El Teatro del Puente abre su techo de cristal para la función de gala, como cada otoño, y Valcenda entera querrá estar debajo.

## Apertura

- **nota**: Señora: la segunda Hoja ha asustado a más gente que la primera. Tres casas han pedido ver sus legajos en el Archivo. El Archivo dice que están en restauración.
- **nota**: Y ha llegado una invitación que no esperaba: Amalia Miravés la recibe a tomar el té. Al atardecer.
- si `marca(reina_interes) o marca(reina_conmovida)`: Mireya dice que la reina ha preguntado por usted dos veces esta semana. Una, por su nombre.
- si `marca(vistos_en_arcos)`: Alguien dejó una nota sin firma bajo su puerta: «Las barcas no deberían acercarse a Arcos Bajos de noche. Por su bien y por el de otros.» La letra es pequeña y muy ordenada.
- si `marca(mara_investiga)`: Mara Calce ha pegado carteles en la Calle de los Sellos: diez coronas por el impresor de la Hoja. Ya hay seis personas que dicen saberlo. Ninguna coincide.
- si `marca(lavanda_hablada)`: Los Veyra y los Marén han cenado juntos. Saúl e Isolda se sentaron uno al lado del otro y hablaron de libros toda la noche. Sus padres parecían encantados. Ellos, tranquilos.
- Opción **Ir al té de Amalia Miravés** → La casa Miravés tiene todas las cortinas echadas. Amalia es pálida, amable y muy precisa. «Los papeles viejos hacen daño a gente que no lo merece», le dice. «Yo sólo quiero que nadie los lea antes de tiempo. Ni siquiera mi sobrino.» Al irse, ve que no ha tocado su taza.
- Opción **Excusarse con una nota** → Amalia responde a vuelta de correo: «Lo comprendo. A mí tampoco me gusta salir de día.» No sabe si es una broma.

## Peticiones

- **nilo** pide no ir a nada el día 20: Nilo: «¿Me haría un favor? El sábado no me mande a ninguna parte. No me pregunte por qué. Te… Le debo una.»
  - Si se cumple: El domingo, Nilo le trae flores del camino de Greda. Tiene ojeras y una sonrisa enorme. «Gracias por no preguntar.»
  - Si no: Nilo no protesta. Es lo peor que podría haber hecho.
- **isolda** pide `s4_teatro`: Isolda, mirando al suelo: «Si Irene va al teatro… ¿podría ir yo también? Es que nunca he visto la luna desde allí.»
  - Si se cumple: Isolda vuelve del teatro sin decir nada. Pero esa noche, en la residencia, se la oye cantar en voz baja.
  - Si no: Isolda dice que la luna se ve igual desde la ventana. Y es verdad, casi.

## Cena entre prensas · día 16 · imprenta
*cena · plazas 2–3 · cualquiera*

> Mara Calce invita a cenar en la imprenta, entre pliegos recién salidos. Promete un juego de sobremesa: adivinar quién escribe la Hoja.

Requisito: chisme 5, intelecto 5, presencia 5
- \+ Mara sabe más chismes que nadie y los cuenta gratis
- − Todo lo que se diga puede salir impreso el lunes

**Carta**

*Querida rival:*

Usted junta parejas y yo junto noticias: nos parecemos más de lo que a usted le gustaría. El martes ceno en la imprenta, entre las prensas, que es donde mejor se piensa. Después de los postres, jugaremos a adivinar quién escribe esa Hoja que me roba lectores. El que acierte, cena gratis todo el otoño.

*Mara Calce*

**Incidente (día 16)** · Mara reparte papeletas: cada invitado debe escribir un nombre. Ella lee la suya en voz alta: «Dario Miravés. Nadie lo ve de día, su carruaje nunca abre las cortinas y su tía compra papeles quemados.» La mesa se vuelve hacia {a}.

- **Seguir el juego y escuchar todas las sospechas** (chisme, d 5)
  - Éxito: {mejor} juega con gracia y escucha. Salen seis nombres. Dos veces el de Dario, una el de Mara y una, en voz muy baja, «alguien del Archivo».
  - A medias: El juego divierte, pero todos repiten el nombre de Dario, como si fuera un estribillo.
  - Fallo: {mejor} escribe un nombre por compromiso y Mara lo lee en voz alta. No era el que debía.
- **Desmontar la sospecha: quien escribe sabe de archivos, no de carruajes** (intelecto, d 5)
  - Éxito: {mejor} razona en voz alta: la Hoja cita folios exactos, usa papel de descarte y sale al día siguiente de las visitas al Archivo. «Es una archivera, o un escribiente.» Mara apunta algo. La mesa se queda pensando.
  - A medias: El razonamiento es bueno, pero Mara lo interrumpe con un brindis. Nadie sabe si lo ha oído.
  - Fallo: {mejor} se embarulla con los folios y Mara se ríe: «Eso es lo que diría el autor.»
- **Negarse con elegancia: no se juega con nombres ajenos** (presencia, d 5)
  - Éxito: {mejor} rompe su papeleta sin escribir nada. «Esta mesa ya tiene bastantes nombres impresos.» Dos invitados hacen lo mismo. Mara, para sorpresa de todos, también.
  - A medias: Nadie más se niega, pero tampoco insisten.
  - Fallo: La negativa suena a que {mejor} tiene algo que ocultar. Mara la apunta en su cuaderno.

**Desenlace · favorable** — Sobremesa larga
- publico: {grupo} cenaron entre las prensas de la imprenta Calce. Fue la cena más comentada de la semana, y Mara no publicará ni la mitad.
- privado: Mara le envía las papeletas del juego en un sobre. «Para que vea lo que piensa Valcenda. A mí ya no me interesa: yo sé que no fui.»
  - si `asiste(irene)`: Irene llegó tarde y con los dedos manchados de una tinta espesa, de imprenta. Dijo que había estado restaurando un legajo. Nadie en la imprenta Calce restaura legajos con esa tinta.
  - si `asiste(dario)`: Dario oyó su nombre en el juego y se rió con todos. En el carruaje, de vuelta, abrió las cortinas por primera vez.

**Desenlace · medias** — Tinta y vino
- publico: {grupo} cenaron con Mara Calce. Se bebió bien y se habló de más.
- privado: Por la mañana, en la Crónica no sale nada de la cena. Mara se lo guarda. Eso le preocupa más que si lo hubiera publicado.
  - si `asiste(irene)`: Irene escondía las manos bajo la mesa. Cuando las sacó para brindar, tenía los dedos negros de tinta.

**Desenlace · desaire** — Nombres en voz alta
- publico: En la cena de la imprenta Calce se leyeron en voz alta nombres que no debían. Varias casas han dejado de saludar a {grupo}.
- privado: Dario no le escribe esta semana. Es la primera vez que su encanto le falla a usted.

## Tiro con arco · día 18 · jardines
*paseo · plazas 2–4 · cualquiera*

> Leonora organiza un concurso de tiro con arco entre los ásteres. Se apunta mal y se conversa bien.

Requisito: presencia 5, estatus 4, baile 4
- \+ Un buen tiro se recuerda más que un buen vals
- − Han venido acreedores de varias casas: los cobros no han terminado

**Carta**

*Querida casamentera:*

El jueves, arcos y dianas entre los ásteres. No le prometo puntería, pero sí buena compañía y un premio de plata para quien acierte en el centro. He perdonado la subasta: venga, y traiga a quien sepa perder con gracia.

*Leonora Serravalle*

**Incidente (día 18)** · Entre tiro y tiro, un escribiente de prestamista se acerca a Teo y le recuerda, en voz alta, una deuda. Teo suelta un chiste y nadie se ríe. Lo mira {a}.

- **Llevarse a Teo aparte y hablar con él de verdad** (presencia, d 5)
  - Éxito: Bajo los castaños, Teo deja de bromear. «Mi padre quiere casarme con dinero. Y yo quiero que alguien se ría conmigo, no de mí.» Lo dice una vez y no lo repite.
  - A medias: Teo empieza a hablar en serio y, a mitad de la frase, hace un chiste. Se le ha escapado otra vez.
  - Fallo: Teo se ríe de la oferta antes de oírla. «¿Hablar? Si quisiera hablar, me habría hecho cura.»
- **Despachar al escribiente con autoridad** (estatus, d 5)
  - Éxito: {mejor} le recuerda al escribiente que está en una casa ajena. Se marcha con una reverencia. Teo da las gracias con los ojos.
  - A medias: El escribiente se aparta, pero se queda esperando junto a la verja.
  - Fallo: El escribiente responde que la deuda es pública. Ahora lo es.
- **Ayudar a Teo a convertirlo en un chiste** (chisme, d 4)
  - Éxito: Entre {mejor} y Teo convierten la deuda en la mejor historia de la tarde. Leonora llora de risa. Teo, al terminar, se queda muy callado.
  - A medias: El chiste funciona a medias. Algunos se ríen; otros miran al escribiente.
  - Fallo: El chiste cae en un silencio que se oye desde la casa.

**Desenlace · favorable** — En el centro
- publico: {grupo} brillaron en el tiro con arco de los Serravalle. El premio de plata se quedó en casa de la casamentera, y Leonora no se lo reprocha.
  - si `asiste(celia) y asiste(dario)`: Celia Lobreda acertó en el centro a la primera. Dario Miravés falló a propósito los tres tiros siguientes para que nadie lo pudiera comparar.
  - si `asiste(saul)`: El capitán Veyra tiró como en el ejército: sin gracia y sin fallar. Se quitó los guantes para el último tiro. Hubo quien lo comentó.
- privado: Leonora le dice al despedirse: «Ese chico Rovena es mejor de lo que finge.» No dice cuál de los dos lados la sorprendió.
  - si `asiste(teo) y opcion(s4_arco) == hablar`: Teo le escribe esa noche, sin chistes: «Gracias por la conversación. No sé si la repetiré, pero ya no puedo decir que no la tuve.»

**Desenlace · medias** — Flechas al césped
- publico: El tiro con arco de los Serravalle fue agradable. Las flechas fueron a parar sobre todo al césped.
- privado: El escribiente del prestamista se fue con un recado para la casa Rovena. Teo lo sabe y no dice nada.

**Desenlace · desaire** — Deudas en público
- publico: En los Jardines Serravalle se habló más de deudas que de flechas. {grupo} se fueron antes del premio.
- privado: Teo no aparece en ningún salón hasta el domingo. Nilo dice que está bien. Nilo siempre dice que todo está bien.

## Una visita privada · día 19 · residencia
*visita · plazas 2–2 · cualquiera*

> Una tarde sin salones ni Crónica. Dos personas que ya se tutean, una sala con chimenea y nadie mirando.

- \+ +2 de cercanía. Prepara la escena del umbral (A)
- − No da reputación: nadie se entera

**Al completarse**
- publico: Una tarde privada. Nadie en Valcenda lo sabrá.
- privado: {a} y {b} pasaron la tarde en la residencia. Bruna llevó té dos veces y, la segunda, no se atrevió a interrumpir.
  - si `asiste(saul) y asiste(dario)`: Saúl y Dario jugaron al ajedrez sin terminar la partida. Saúl dejó los guantes en la mesa de la entrada y se fue sin ellos.
  - si `asiste(irene) y asiste(isolda)`: Irene leyó en voz alta e Isolda escuchó con los ojos cerrados. Luego fue Isolda quien leyó, y no se equivocó ni una vez.
  - si `asiste(nilo) y asiste(camila)`: Camila le enseñó a Nilo a jugar a las cartas como juegan las viudas: sin piedad. Nilo perdió todo y se rió todo el rato.
  - si `asiste(teo) y asiste(celia)`: Teo intentó enseñarle a Celia a contar un chiste. Celia ensayó la entonación nueve veces. Al décimo, Teo se rió de verdad.
  - si `asiste(dario) y asiste(celia)`: Dario y Celia bailaron sin música en la sala pequeña. Ella no contó. Él no fingió. Bruna dice que no los vio.
  - si `asiste(teo) y asiste(irene)`: Teo leyó por fin uno de sus versos. Irene no dijo si se lo creía, pero le pidió otro.
  - si `asiste(saul) y asiste(isolda)`: Saúl e Isolda redactaron juntos una carta a sus padres sobre los convoyes. Tardaron tres horas y se rieron mucho. No la enviaron.

## Teatro de gala · día 20 · teatro
*teatro · plazas 4–4 · parejas · OBLIGATORIO*

> Función de gala con el techo de cristal abierto a la luna llena. Le corresponde un palco: dos parejas, a la vista de toda la sala.

Requisito: intelecto 5, estatus 5, presencia 5
- \+ Toda Valcenda estará mirando los palcos, no el escenario
- − La función termina tarde, con la luna en lo alto
- − La tía de Dario tiene el palco de al lado

**Carta**

*A la casamentera de la Temporada,*

El Teatro del Puente tiene el honor de reservarle el palco cuarto para la función de gala del sábado: «La dama del faro», en tres actos, con el techo abierto a la luna llena. Le rogamos que lo ocupen dos parejas. Un palco vacío en una noche así se comenta más que cualquier escena.

*La dirección del Teatro del Puente*

**Incidente (día 20)** · En el entreacto, Amalia Miravés ocupa el palco de al lado con las cortinas echadas. Media sala mira hacia allí, y después hacia {a}. Alguien susurra «La Hoja tenía razón».

- **Saludar a Amalia en público, con toda cortesía** (estatus, d 5)
  - Éxito: {mejor} cruza al palco vecino y saluda. Amalia descorre una cortina, un palmo, y sonríe. La sala decide que no hay nada que ver.
  - A medias: Amalia responde al saludo sin descorrer las cortinas. La sala sigue mirando, aunque menos.
  - Fallo: El saludo llega tarde y parece una disculpa. Ahora la sala mira a los dos palcos.
- **Hacer que el palco brille más que el chisme** (presencia, d 5)
  - Éxito: El palco cuarto ríe, conversa y aplaude a destiempo con tanta gracia que la sala deja de mirar las cortinas.
  - A medias: Funciona hasta el tercer acto, cuando alguien vuelve a señalar el palco de Amalia.
  - Fallo: Las risas del palco suenan forzadas bajo la luna. Alguien pide silencio.
- **Observar quién no está en su sitio esta noche** (intelecto, d 5)
  - Éxito: {mejor} cuenta los palcos: Amalia está, Dario está, Mara está. Faltan dos personas: un caballero que siempre llega primero e Irene Salvat, que dijo que vendría.
  - A medias: {mejor} nota que alguien falta, pero no sabe quién hasta que se apagan las luces.
  - Fallo: {mejor} mira tanto a los palcos que se pierde el final de la obra. Lo comenta medio teatro.

**Incidente de riesgo (si `asiste(nilo)`, sustituye al anterior)** · Al abrirse el techo de cristal, la luz de la luna llena entra en la sala. Nilo se pone muy pálido, se excusa y sale del palco sin mirar a nadie. {a} lo ve alejarse hacia el río.

- **Cubrirlo: inventar una excusa para el palco** (chisme, d 5)
  - Éxito: «Una cita», dice {mejor}, «con una dama que no quiere que la vean.» El palco se ríe, la sala también, y nadie vuelve a preguntar.
  - A medias: La excusa convence a medias. Alguien del palco de enfrente apunta la hora.
  - Fallo: La excusa se contradice sola. Para el tercer acto, media sala sabe que Nilo Lobreda se fue corriendo.
- **Seguirlo, por si necesita ayuda** (presencia, d 5)
  - Éxito: {mejor} lo alcanza junto al río. Nilo tiembla, de espaldas, y le pide sin volverse que se vaya. «Por favor. Mañana se lo cuento todo. Hoy no.» {mejor} se va. Lo cumple.
  - A medias: {mejor} lo pierde entre los faroles del puente. Sólo encuentra su chaqueta, doblada con cuidado sobre la barandilla.
  - Fallo: {mejor} lo sigue hasta el río y alguien más los sigue a los dos. Por la mañana, ya circula que Nilo Lobreda «huyó del teatro como un animal asustado».
- **Dejarlo ir y disculparlo como indispuesto** (estatus, d 4)
  - Éxito: {mejor} manda una nota a la dirección: el señor Lobreda está indispuesto. El palco queda incompleto, pero digno.
  - A medias: La nota llega, pero el asiento vacío se ve desde toda la sala.
  - Fallo: La nota se pierde. Durante dos actos, el asiento de Nilo es lo más mirado del teatro.

**Desenlace · favorable** — Bajo el techo de cristal
- publico: El palco cuarto fue el más admirado de la gala. {grupo} vieron «La dama del faro» bajo la luna, y la sala los vio a ellos.
  - si `asiste(irene) y asiste(isolda)`: Isolda Marén e Irene Salvat compartieron un programa durante toda la función. En el tercer acto, Isolda dejó de leerlo y miró a Irene.
  - si `asiste(saul) y asiste(dario)`: El capitán Veyra y el señor Miravés compartieron palco y no se dirigieron la palabra en público. En privado, dicen, no pararon.
  - si `asiste(celia) y marca(celia_error_tapado)`: Celia Lobreda tropezó en la escalera del palco, se levantó sola y saludó a la sala. La ovación fue para ella.
- privado: La reina no estaba, pero envió a Mireya. Mireya le dice: «Su Majestad querrá saber quién faltó esta noche. Yo ya lo sé.»
  - si `asiste(nilo) y marca(nilo_cubierto)`: Al amanecer, Nilo deja una nota en la residencia: «Gracias. Algún día se lo explicaré. Te lo prometo.» Esta vez no se ha corregido.

**Desenlace · medias** — Un palco a medias
- publico: La gala fue hermosa y el palco cuarto, correcto. La sala pasó más tiempo mirando las cortinas de los Miravés.
- privado: En la salida, alguien ha dejado un pliego doblado en cada carruaje. Es la tercera Hoja, un día antes de lo previsto.

**Desenlace · desaire** — La noche de la luna
- publico: En la gala del Teatro del Puente, el palco de la casamentera dio más que hablar que la obra. Ninguna de las cosas que se dicen es buena.
- privado: Mireya le escribe una sola línea: «La reina leerá la Hoja antes que la Crónica.»

**Desenlace · sin_asistentes**
- publico: El palco cuarto se quedó vacío la noche de la gala. Bajo la luna llena, se veía desde toda la sala.

## Crónica de salones · Número 4 · Impreso por Calce, Calle de los Sellos

*Luna llena, techo abierto y un pliego en cada carruaje. Valcenda no dormirá tranquila hasta el próximo cuarto menguante.*

- **La dama del faro** (texto del desenlace)
- **Entre prensas** (texto del desenlace)
- **Flechas y ásteres** (texto del desenlace)
- **Una salida apresurada**: El joven Lobreda abandonó la gala en mitad del segundo acto. Esta Crónica no especula. Sólo informa de que corría.
- **Cortinas**: Los tapiceros de Alto Laurel han vendido más cortinas gruesas esta semana que en todo el año. Nadie quiere que lo miren por la ventana.

*La Crónica firma todo lo que publica. Esta semana, con más orgullo que nunca.*

## La Hoja sin Firma · nº 3

*Alguien de los salones no es lo que aparenta.*

Llega cuando se pone el sol. Su carruaje nunca abre las cortinas. Su familia compra papeles quemados. Interesante. ¿Por qué nadie le ha visto nunca a mediodía?
- si `marca(nilo_visto) y no marca(nilo_cubierto)`: Y no es el único. Otro caballero abandona los teatros cuando sale la luna. El Pacto del Umbral tenía una página para cada uno.
- si `marca(amalia_saludada)`: Algunos ya la saludan en público. Valcenda siempre ha preferido la cortesía a las preguntas.

*— Folios 82 y 83. El 84 lo guardamos para el final.*

## Sólo para sus ojos

- si `asistio(s4_cena_calce, irene)`: Irene llevaba tinta de imprenta en los dedos el martes. No de registro: de imprenta. Usted conoce la diferencia; Mara se la enseñó.
- si `marca(pista_ausencias)`: La noche del teatro faltaron dos personas: Nilo, que siempre llega primero, e Irene, que había dicho que vendría. La Hoja apareció en los carruajes antes de terminar la función.
- si `marca(pista_archivera)`: Lo dijo en voz alta en casa de Mara: quien escribe es una archivera, o un escribiente. Desde entonces no ha podido dejar de pensarlo.
- si `marca(dario_sospechoso)`: Media Valcenda sospecha de Dario. Usted no. Dario no sabe escribir una carta sin faltas de ortografía, y la Hoja no tiene ni una.
- si `marca(nilo_visto)`: Nilo temblaba junto al río y no quiso volverse. Le prometió contarlo todo. Usted decide no preguntar hasta que él quiera.
- si `marca(amalia_conocida)`: Amalia Miravés quiere que nadie lea esos papeles «antes de tiempo». Usted empieza a entender que no los quiere para hacer daño, sino para que no se lo hagan a alguien.
- si `marca(teo_conversacion_seria)`: Teo quiere a alguien que se ría con él, no de él. Lo dijo una vez. A usted le basta.
- si `semana == 4`: Quedan dos semanas. Las parejas ya no son posibilidades: son personas que se esperan en los rincones.

## Gancho

- **nota**: Señora: tres noticias. La primera, que llegan tormentas de Nácar. La segunda, que la deuda Miravés contra la señora Ferrán vence la semana que viene.
- **nota**: La tercera, que ha llegado un correo de Tiria para el capitán Veyra. Lleva el sello del ejército. No lo ha abierto delante de nadie.
