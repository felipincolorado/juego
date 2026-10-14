# Semana 5 · Cierre de Cuentas

**Tormentas de Nácar.** Llegan las tormentas de Nácar y, con ellas, los convoyes del sur. Antes del Gran Baile, las casas saldan sus deudas: las que se pagan y las que no se pueden pagar.

## Apertura

- **nota**: Señora: el capitán Veyra ha abierto por fin el correo de Tiria. Es una orden: debe volver al ejército después del Gran Baile.
- **nota**: Salvo que antes selle un compromiso en el Archivo. Entonces podrá quedarse a servir aquí, «para la alianza de su casa».
- **nota**: Y Mara Calce pide una entrevista. Por escrito, esta vez, y con sello. Dice que es la última vez que lo pide.
- si `marca(nilo_cubierto) o marca(nilo_confia)`: Nilo ha venido a desayunar dos veces esta semana. No ha contado nada. Pero se queda más rato, como quien está a punto de decir algo.
- si `marca(nilo_visto) y no marca(nilo_cubierto)`: En los salones se habla de Nilo Lobreda «y sus huidas». Él sonríe como siempre. Ya no duerme como siempre.
- si `marca(dario_sospechoso)`: Han apedreado el carruaje de los Miravés en el puente. Dario dice que no fue nada. Llevaba las cortinas abiertas.
- si `marca(teo_bufon)`: Teo es el invitado más solicitado de la semana. Lo llaman para que haga reír. Nadie lo llama para otra cosa.
- si `marca(isolda_hablo_primero)`: Isolda le ha dado los buenos días en voz alta, desde la puerta, sin que usted la viera llegar. Bruna casi deja caer la bandeja.
- Opción **Conceder la entrevista a Mara** → Mara no pregunta por parejas. Pregunta si usted escribe la Hoja. Usted se ríe. Ella no. «Alguien que lo sabe todo de su elenco… Si no es usted, es alguien muy cerca de usted.» Se va satisfecha, sin una línea apuntada.
- Opción **Negarse con firmeza** → Mara devuelve el sello roto con una nota: «Entonces escribiré lo que pienso, que es peor que lo que usted habría dicho.»

## Peticiones

- **nilo** pide no ir a nada el día 25: Nilo: «Mi casa quiere que esté en la lectura de capitulaciones del jueves. Y le prometí a Camila ayudarla ese mismo día con las cuentas del barco. No me mande. Por favor. Esta vez quiero cumplir la promesa que importa.»
  - Si se cumple: Nilo pasa el jueves entre los libros de cuentas de los Ferrán. Su padre le escribe una carta furiosa. Nilo la lee, la dobla y sigue sumando.
  - Si no: Nilo va a la lectura, como pide su casa. Camila hace las cuentas sola. Cuando él llega, por la noche, ya están hechas.
- **camila** pide `s5_cena_deudas`: Camila: «A la cena de las deudas quiero ir yo. Si los Miravés van a leer mi nombre en voz alta, que lo hagan mirándome.»
  - Si se cumple: Camila vuelve de la villa Serravalle y se quita los guantes en la puerta, como quien deja un peso. «Hecho», dice. Nada más.
  - Si no: Camila se entera por otros de lo que se dijo de ella en la cena. No se lo reprocha a usted. Eso es peor.

## Lección de voz · día 23 · academia
*clase · plazas 1–3 · cualquiera*

> Inés enseña a hablar en un salón lleno sin levantar la voz. En el Gran Baile, dice, la reina sólo oirá a quien sepa hacerse oír.

- \+ +1 en Presencia a cada asistente (hasta 4)
- − Inés hace cantar a todo el mundo. A todo el mundo

**Carta**

*Señora casamentera:*

El martes doy la última lección de la temporada. No es de baile: es de voz. Quien no sepa hacerse oír en el Gran Baile, bailará muy bien y nadie sabrá su nombre. Mándeme a los que hablan bajito. Y a los que hablan demasiado, para que aprendan a callar a tiempo.

*Inés*

**Al completarse**
- publico: {grupo} tomaron lección de voz con Inés. En la Academia se oyó cantar hasta el portero.
- privado: Inés le escribe: «Ya se hacen oír. Ahora falta que tengan algo que decir. Eso ya no lo enseño yo.»
  - si `asiste(isolda)`: Isolda cantó sola una estrofa entera. Cuando terminó, nadie aplaudió durante un momento, y después todos a la vez.
  - si `asiste(irene)`: Irene se negó a cantar y leyó un poema en voz alta. Inés dijo que también contaba. Irene leyó demasiado bien para ser la primera vez.
  - si `asiste(saul)`: Saúl cantó una marcha del ejército, sin desafinar y sin sonreír. Inés le pidió otra, más lenta. Esa sí la cantó sonriendo.

## Llegada de los convoyes · día 24 · muelles
*recepcion · plazas 2–4 · cualquiera*

> Los Marén y los Veyra reciben en los muelles a los convoyes del sur, entre tormenta y tormenta. Quieren que Valcenda vea su alianza.

Requisito: estatus 5, presencia 5, intelecto 4
- \+ Las dos casas están de muy buen humor
- − El cielo de Nácar no respeta recepciones
- − Los aseguradores miran cada barco como si fuera a hundirse

**Carta**

*Distinguida señora:*

El miércoles llegan a Valcenda los primeros convoyes que la casa Veyra escolta por tierra y la casa Marén asegura por mar. Celebraremos su llegada en los muelles, si la tormenta lo permite, y aunque no lo permita. Nos honraría ver a sus jóvenes. Sobre todo, a los que ya conocen a nuestros hijos.

*Tobías Marén y Ernesto Veyra*

**Incidente (día 24)** · Un golpe de viento tumba el toldo de la recepción. Entre el desorden, los dos padres anuncian en voz alta que «la alianza merece un lazo más fuerte que un contrato». Todos miran a {a}.

- **Poner orden bajo la lluvia y salvar la recepción** (presencia, d 5)
  - Éxito: {mejor} organiza a los criados, a los invitados y a la lluvia. Cuando vuelve a salir el sol, los padres brindan por la alianza y todo el muelle aplaude.
  - A medias: La recepción se salva a medias. El brindis se hace bajo un toldo torcido.
  - Fallo: La lluvia gana. Los invitados se dispersan y el anuncio queda en el aire, empapado.
- **Desviar la atención de los padres antes de que digan nombres** (estatus, d 5)
  - Éxito: {mejor} propone un brindis por los barqueros antes de que nadie diga un nombre. Los padres se miran, contrariados. Saúl e Isolda, aliviados.
  - A medias: El brindis llega a tiempo, pero uno de los padres se las arregla para decir «nuestros hijos» antes de beber.
  - Fallo: El brindis llega tarde: los dos apellidos ya están dichos, juntos, delante de todo el muelle.
- **Fijarse en qué barco revisan los aseguradores con más cuidado** (intelecto, d 4)
  - Éxito: Los aseguradores Marén revisan un barco gemelo del Clara de Nácar. Uno murmura: «Éste no se hundirá. Aquél tampoco tenía por qué.» {mejor} lo oye.
  - A medias: Los aseguradores revisan todos los barcos igual. Pero uno de ellos se santigua al ver el último.
  - Fallo: {mejor} se acerca demasiado al barco y un marinero le pide, con malos modos, que se aparte.

**Desenlace · favorable** — Barcos y brindis
- publico: Los convoyes de Nácar llegaron entre tormentas y aplausos. {grupo} estuvieron en el muelle y fueron lo único seco de la tarde.
  - si `asiste(saul) y asiste(isolda)`: El capitán Veyra y la señorita Marén recibieron juntos al primer barco. Sus padres lloraron. Ellos dos se dieron la mano como socios.
  - si `asiste(camila)`: La señora Ferrán miró pasar el barco gemelo del Clara de Nácar sin apartar la vista. Después pidió una copa y brindó por los que no llegaron.
- privado: Tobías Marén le escribe: «Mi hija nunca había hablado tanto en una recepción. No sé qué le ha hecho usted, pero siga.»
  - si `asiste(isolda) y marca(isolda_hablo_primero)`: Isolda le pidió a su padre, delante de todos, que la dejara elegir sola. Su padre dijo que sí antes de pensarlo. Ahora lo está pensando.

**Desenlace · medias** — Mojados pero aliados
- publico: La recepción de los convoyes terminó bajo la lluvia. La alianza Marén–Veyra, en cambio, parece más sólida que nunca.
- privado: Saúl se va del muelle sin despedirse, a paso militar. Isolda lo mira irse y no dice nada.

**Desenlace · desaire** — La tormenta ganó
- publico: La tormenta arruinó la recepción de los convoyes. Las casas Marén y Veyra culpan al cielo. Algunos culpan a otros.
- privado: Los dos padres le escriben el mismo día, por separado, la misma queja. Se copian las cartas, decididamente.

## Lectura de capitulaciones · día 25 · archivo
*recepcion · plazas 2–3 · cualquiera*

> Los Lobreda y los Veyra leen en el Archivo los acuerdos del paso de Greda. Dicen que sólo hablarán de caravanas. Nadie lo cree.

Requisito: estatus 5, intelecto 5, chisme 4
- \+ Quien entienda los papeles, entiende la temporada
- − Los Veyra ya tienen otra alianza sobre la mesa

**Carta**

*Señora:*

El jueves, en la sala de actas del Archivo, nuestras casas renovarán los acuerdos del paso de Greda. Se agradecerá la presencia de testigos de confianza. La señorita Celia Lobreda y el capitán Saúl Veyra están invitados de forma especial, aunque no se ha dicho por qué.

*Las casas Lobreda y Veyra*

**Incidente (día 25)** · En la última página de las capitulaciones aparece una cláusula nueva: «El paso quedará unido por matrimonio.» No lleva nombres, pero hay dos sillas vacías junto a la mesa. {a} la lee primero.

- **Leerla en voz alta, tal como está** (intelecto, d 5)
  - Éxito: {mejor} lee la cláusula con calma. Los padres asienten. Celia se queda muy quieta. Saúl mira la ventana.
  - A medias: La cláusula se lee, pero nadie dice nada después. El silencio dura un minuto entero.
  - Fallo: {mejor} se trabuca en los nombres de las casas. Alguien se ríe, nervioso, y la reunión se agria.
- **Proponer una enmienda: «si ambas partes lo desean»** (estatus, d 5)
  - Éxito: {mejor} propone la enmienda con tal cortesía que nadie se atreve a negarla. «Si ambas partes lo desean» queda escrito con tinta fresca.
  - A medias: La enmienda se acepta «para estudiarla». Nadie sabe qué significa eso.
  - Fallo: Los padres rechazan la enmienda a la vez, como si lo hubieran ensayado.
- **Preguntar a la archivera de guardia quién redactó la cláusula** (chisme, d 4)
  - Éxito: La archivera de guardia es Irene Salvat. Dice que la cláusula la trajeron ya escrita. Tiene un pliego doblado en el bolsillo del delantal, y lo tapa con la mano.
  - A medias: La archivera de guardia dice que no puede hablar de documentos privados. Es Irene Salvat. No le mira a los ojos.
  - Fallo: La pregunta se oye en toda la sala. Los padres miran a {mejor} como a un intruso.

**Desenlace · favorable** — Tinta fresca
- publico: Las casas Lobreda y Veyra renovaron los acuerdos del paso. {grupo} firmaron como testigos con una caligrafía impecable.
  - si `asiste(celia) y asiste(saul)`: Celia Lobreda y Saúl Veyra se sentaron en las dos sillas vacías. No se miraron. Valcenda ya les ha puesto fecha.
- privado: Al salir del Archivo, el padre de Celia le estrecha la mano: «Usted entiende de casas.» No sabe si es un elogio o una amenaza.
  - si `asiste(celia) y opcion(s5_capitulaciones) == enmendar`: Celia la alcanza en la escalera y le dice, muy rápido: «Gracias por lo de “si ambas partes lo desean”. Todavía no sé lo que deseo. Pero ahora puedo saberlo.»

**Desenlace · medias** — Una silla vacía
- publico: La lectura de capitulaciones del paso fue larga y discreta. Se firmó todo menos la última página.
- privado: La última página se queda en el Archivo, sin firmar. Alguien la ha guardado en un legajo con el número 84.

**Desenlace · desaire** — Papeles rotos
- publico: La lectura de capitulaciones Lobreda–Veyra terminó con voces. Las caravanas del paso seguirán pasando. Las casas, por ahora, no.
- privado: Celia no ha salido de su cuarto en todo el día. Camila dice que está bien. Camila tampoco ha salido del suyo.

## Cena de las deudas · día 26 · jardines
*cena · plazas 3–3 · cualquiera · OBLIGATORIO*

> La víspera del cierre de cuentas, las grandes casas cenan en la villa Serravalle y saldan en voz alta lo que se deben. Es una tradición. Es una crueldad.

Requisito: intelecto 5, chisme 5, estatus 5
- \+ Lo que se arregla esta noche no llega al Gran Baile
- − Esta noche vence la reclamación Miravés contra la señora Ferrán
- − Las casas con deudas no perdonan a quien las ve pagar

**Carta**

*Querida casamentera:*

Como cada otoño, la víspera del cierre de cuentas reúno en la villa a las casas que se deben algo. Se cena bien, se habla claro y se sale con las cuentas saldadas o con los enemigos declarados. Esta vez, me temo, habrá de todo. Traiga a tres de sus jóvenes, y que sepan contar.

*Leonora Serravalle*

**Incidente (día 26)** · Amalia Miravés se levanta y le tiende un papel a su sobrino: «Léelo tú, Dario. Es tu reclamación.» Es la deuda del Clara de Nácar contra la viuda Ferrán. La mesa entera mira a {a}.

- **Demostrar con los papeles que el seguro Marén ya pagó ese barco** (intelecto, d 5)
  - Éxito: {mejor} recuerda las fechas: el seguro Marén pagó el Clara de Nácar entero, sin discutir. Reclamarlo dos veces es cobrarlo dos veces. Amalia se sienta despacio. La deuda cae.
  - A medias: El argumento es bueno, pero faltan papeles. La deuda se aplaza hasta la primavera.
  - Fallo: {mejor} se equivoca de año. Amalia sonríe, educada. La deuda queda en pie.
- **Negociar en nombre de la casamentera: aplazar la deuda** (estatus, d 5)
  - Éxito: {mejor} propone aplazar la deuda hasta después de la primavera, con la garantía de la casamentera. Amalia acepta con una mirada que dice: «Me debe una.»
  - A medias: Se aplaza un mes. Lo justo para pasar el Gran Baile.
  - Fallo: La propuesta suena a caridad. Camila la rechaza en voz alta, por orgullo.
- **Contraatacar: preguntar por el cofre de papeles quemados** (chisme, d 5)
  - Éxito: «¿Y los papeles del lote 12, señora Miravés?» La mesa se vuelve hacia Amalia. Amalia guarda la reclamación sin leerla. Dario no levanta la vista del plato.
  - A medias: La pregunta incomoda, pero Amalia la esquiva con elegancia. La reclamación se lee igual.
  - Fallo: La pregunta suena a calumnia. Leonora pide orden, y la mesa se pone de parte de los Miravés.

**Desenlace · favorable** — Cuentas claras
- publico: La cena de las deudas terminó con más cuentas saldadas que enemigos. {grupo} salieron de la villa Serravalle con la frente alta.
  - si `asiste(dario) y marca(dario_sin_mascara)`: Dario Miravés se negó a leer la reclamación de su tía. «No la redacté yo», dijo, «y no la voy a firmar.» Es la primera vez que alguien le lleva la contraria a Amalia en público.
  - si `asiste(camila)`: La señora Ferrán escuchó su nombre sin pestañear y contestó con una sola frase: «El mar ya cobró ese barco.» Leonora pidió que se lo grabaran en un plato.
  - si `asiste(teo)`: Aurelio Rovena anunció que su hijo buscará «una unión ventajosa» antes del Gran Baile. Teo brindó por ello sin un solo chiste.
- privado: Leonora le escribe a medianoche: «Hacía veinte años que nadie salía contento de esta cena. Ha sido usted. No vuelva a hacerlo: me arruina la tradición.»
  - si `marca(deuda_saldada) y asiste(isolda)`: Isolda supo esa noche por qué su familia pagó sin discutir: un asegurador de los Marén firmó el barco sabiendo que estaba podrido. Su padre pagó para callarlo. Isolda no lloró en la cena. Lloró después, sola, y luego fue a ver a Camila.

**Desenlace · medias** — Cuentas pendientes
- publico: En la cena de las deudas se saldó la mitad y se aplazó el resto. Es lo normal. {grupo} no empeoraron nada, que esta noche ya es mucho.
- privado: Camila vuelve a casa sola, a pie, bajo la lluvia. No quiso carruaje.

**Desenlace · desaire** — Enemigos declarados
- publico: La cena de las deudas de este otoño se recordará por las voces. La señora Ferrán sale de ella con la deuda en pie y la mitad de las casas, en contra.
- privado: Amalia Miravés le manda un ramo de flores blancas. Sin nota. Bruna las tira sin preguntar.

**Desenlace · sin_asistentes**
- publico: La casamentera no envió a nadie a la cena de las deudas. Las casas cenaron sin testigos, y eso nunca termina bien.

## La última visita antes del baile · día 27 · residencia
*visita · plazas 2–2 · cualquiera*

> Una tarde a solas antes del Gran Baile. Si ya se dijeron lo que sienten, ésta es la tarde en que algo puede pasar.

- \+ +2 de cercanía. Tras una escena A, desbloquea el beso
- − No da reputación: nadie se entera

**Al completarse**
- publico: Una tarde privada. Nadie en Valcenda lo sabrá.
- privado: {a} y {b} pasaron la tarde en la residencia. Bruna no llevó té. Dice que no hizo falta.
  - si `nivel(a, b) >= A`: Cuando {a} y {b} se fueron, la sala olía a chimenea apagada y a algo que Bruna no quiso nombrar. Sonreía.

## Crónica de salones · Número 5 · Impreso por Calce, Calle de los Sellos

*Semana de cuentas. Se pagó lo que se pudo, se aplazó lo que no y se prometió todo lo demás para el Gran Baile.*

- **La cena de las deudas** (texto del desenlace)
- **Barcos del sur** (texto del desenlace)
- **El paso de Greda** (texto del desenlace)
- **La casamentera habla**: Esta Crónica entrevistó a la casamentera. No dijo nada. Lo dijo muy bien. Esta Crónica cree que sabe quién escribe la Hoja, y que no es ella.
- **Preguntas sin respuesta**: La casamentera se negó a hablar con esta Crónica. Lo respetamos. También nos preguntamos por qué alguien que no esconde nada necesita tanta discreción.
- **Tormentas**: Las tormentas de Nácar han tumbado tres toldos, dos chimeneas y un compromiso. Esta Crónica no dirá cuál.

*La Crónica firma todo lo que publica. La semana que viene, también el Gran Baile.*

## La Hoja sin Firma · nº 4

*El próximo número será el último. Llevará nombres.*

El Archivo empezó a arder a la hora tercera de la noche del 14 de nieblas, hace ochenta años, por la sala de linajes. No por la de impuestos, como dice la historia oficial. Alguien eligió qué debía arder. El Gran Baile sabrá quién.
- si `nivel(irene, isolda) >= A o nivel(irene, teo) >= A o marca(nombres_protegidos)`: Publicaremos lo que se robó y a quién se le robó. Los nombres de quienes sólo intentaban esconderse… todavía no lo hemos decidido.

*— Folio 84. El último.*

## Sólo para sus ojos

- si `marca(pista_irene_actas)`: Irene estaba de guardia en el Archivo el jueves, con un pliego doblado en el delantal. La Hoja nº 4 salió el viernes.
- si `marca(hoja_4_publicada)`: La Hoja dice a qué hora y en qué sala empezó el incendio. Eso no está en ningún libro: sólo en el registro interno del Archivo. Quien la escribe ha leído ese registro.
- si `marca(deuda_saldada)`: La deuda del Clara de Nácar ha caído. Camila es libre. Los Marén, no tanto: ahora todos saben por qué pagaron sin discutir.
- si `marca(favor_amalia)`: Le debe un favor a Amalia Miravés. Sospecha que se lo cobrará en el Gran Baile, y que tendrá que ver con papeles.
- si `marca(nilo_elige_promesa)`: Nilo eligió la promesa que importaba, no la que le exigía su casa. Es la primera vez que mide lo que promete.
- si `marca(alianza_anunciada) o marca(compromiso_paso_propuesto)`: Saúl tiene dos alianzas sobre la mesa, la de los convoyes y la del paso, y una orden de Tiria. Sólo puede sellar una cosa en el Gran Baile, o marcharse.
- si `semana == 5`: Una semana. Repasa sus notas: hay pistas suficientes para saber quién escribe la Hoja, si se atreve a juntarlas.

## Gancho

- **nota**: Señora: ha llegado el carnet de baile del Gran Baile del Sello. Ocho nombres, doce valses y una sola noche.
- **nota**: Y otra nota, sin firma, con letra pequeña y muy ordenada: «Si quiere saber quién soy, venga al Archivo antes del baile. Si no quiere saberlo, no venga.»
