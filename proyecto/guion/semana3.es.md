# Semana 3 · Noche de los Faroles

**Ochenta años del incendio.** Hace ochenta años ardió el Archivo Real la Noche del Censo. Esta semana Valcenda enciende faroles sobre el río por todo lo que se perdió. La reina bajará a los muelles el sábado.

## Apertura

- **nota**: Señora: la Hoja sin Firma está en todas las mesas del desayuno. Nadie admite haberla leído. Todos la citan.
- **nota**: Y Mara Calce ha vuelto. Espera en el recibidor con el sombrero puesto, que es su manera de decir que no piensa irse.
- si `marca(hoja_retirada)`: En los salones se comenta que usted mandó recoger los pliegos del baile. Unos lo llaman prudencia. Otros, miedo.
- si `marca(pista_archivo_interno)`: El escribiente del Archivo le hizo una seña al pasar: el legajo 80 ha vuelto a salir. Esta vez nadie lo ha apuntado.
- si `marca(irene_recelosa)`: Irene no vino al té del lunes. Mandó decir que tenía trabajo. Es la primera vez que se excusa.
- si `marca(irene_agradecida)`: Irene le manda saludos por medio de Bruna. Bruna dice que es la primera vez que Irene manda saludos a alguien.
- si `marca(rumor_compromiso_paso)`: Las casas Lobreda y Veyra ya no piden mesas contiguas: piden la misma. El rumor del compromiso del paso tiene fecha, aunque nadie la ha dicho.
- Opción **Recibir a Mara Calce** → Mara deja la Hoja sobre su mesa. «Esta semana he vendido el doble de Crónicas. No me mire así: yo no la escribí. Ojalá. Pero está mal impresa: ninguna prensa mía deja esas manchas.» Antes de irse, pregunta qué sabe usted. Usted no contesta. Ella sonríe, como si eso fuera una respuesta.
- Opción **Despedirla con una nota cortés** → Mara le devuelve la nota con una línea debajo de la suya: «Entonces lo averiguaré sola.» La letra es grande y rápida.

## Peticiones

- **camila** pide `s3_subasta`: Camila: «Subastan el catalejo de mi marido entre los objetos del Archivo. No quiero comprarlo. Quiero saber quién lo compra.»
  - Si se cumple: Le cuenta a Camila quién se llevó el catalejo: la casa Marén. Camila se ríe sin ganas. «Los aseguradores. Claro. Compran todo lo que se hunde.»
  - Si no: Camila no vuelve a preguntar. Pero esa semana la ve dos veces mirando el río desde el puente.
- **celia** pide `s3_clase`: Celia: «Quiero ir a la lección de protocolo. Si la reina me habla en el río, quiero saber contestar. Y quiero ir sin Nilo.»
  - Si se cumple: Celia vuelve de palacio con la espalda aún más recta, si es posible. Le dice a Nilo que no necesitó a nadie. Nilo aplaude demasiado fuerte.
  - Si no: Celia ensaya reverencias sola, frente al espejo del pasillo. Las cuenta en voz baja.

## Subasta por el Archivo · día 9 · jardines
*recepcion · plazas 2–4 · cualquiera*

> En los Jardines Serravalle se subastan objetos que se salvaron del incendio, o que dicen haberse salvado. Lo recaudado irá a la restauración del Archivo.

Requisito: estatus 5, presencia 4, chisme 4
- \+ Las casas pujan por caridad y, sobre todo, por ser vistas
- \+ Hay lotes que interesan a más de uno de su elenco
- − Una puja mal hecha se recuerda más que un baile

**Carta**

*Querida casamentera:*

Ochenta años después, todavía aparecen en los desvanes cosas que se salvaron del incendio: un tintero, un mapa, un catalejo que nadie sabe cómo llegó allí. El martes los subastamos en mis jardines, por el Archivo. Traiga a sus jóvenes. Que pujen, que se dejen ver y, si es posible, que no paguen de más por un tintero.

*Leonora Serravalle*

**Incidente (día 9)** · Sale el lote 12: un cofre de papeles chamuscados, sin catalogar. Un hombre de guantes grises puja enseguida, y alto. Nadie sabe para quién puja.

- **Pujar por el cofre en nombre del Archivo** (estatus, d 5)
  - Éxito: {mejor} sube la puja con calma hasta que el hombre de los guantes grises se rinde. El cofre volverá al Archivo, y la sala aplaude.
  - A medias: {mejor} se retira a tiempo. El cofre se lo lleva el hombre de los guantes grises, pero ha pagado el triple.
  - Fallo: La puja se dispara y {mejor} se queda con un precio que no puede pagar. Leonora lo arregla con una sonrisa. Nadie lo olvidará.
- **Averiguar para quién puja el hombre de los guantes grises** (chisme, d 4)
  - Éxito: Un criado de los Serravalle lo reconoce: es el administrador de Amalia Miravés. La tía de Dario quiere esos papeles, y los quiere sin que se sepa.
  - A medias: Nadie lo conoce, pero su carruaje espera con las cortinas echadas, a pleno sol.
  - Fallo: La pregunta llega a oídos del hombre de los guantes grises. Mira a {mejor} durante el resto de la subasta.
- **Pedir, antes de pujar, examinar los papeles** (intelecto, d 5)
  - Éxito: Entre los papeles, medio quemado, hay un sello que {mejor} no reconoce: una puerta abierta dentro de un círculo. Leonora cierra el cofre un poco deprisa.
  - A medias: Les dejan mirar un momento. Hay fechas de hace ochenta años y una palabra repetida: «Umbral».
  - Fallo: Leonora se niega con amabilidad: «Los lotes se compran, querida, no se leen.» La sala se ríe.

**Desenlace · favorable** — Martillo y caridad
- publico: La subasta de los Serravalle recaudó más que ninguna en diez años. {grupo} pujaron con elegancia y se fueron con la sala a su favor.
  - si `asiste(saul)`: El capitán Veyra compró un mapa antiguo del paso de Greda por una suma discreta, y lo regaló al Archivo en el acto. Nadie le había visto regalar nada.
  - si `asiste(teo)`: Teo Rovena hizo de subastador durante tres lotes cuando el titular se quedó sin voz. Vendió un tintero por el precio de un caballo.
- privado: Leonora le escribe para darle las gracias, y añade al final: «El lote 12 no estaba en mi lista. No sé quién lo trajo.»
  - si `asiste(irene)`: Irene no pujó por nada. Pero no apartó los ojos del lote 12 hasta que se lo llevaron, y se fue sin despedirse.
  - si `asiste(dario) y marca(pujador_miraves)`: Cuando se supo para quién pujaba el hombre de los guantes grises, Dario se puso muy serio. Después se rió demasiado alto de algo que no tenía gracia.

**Desenlace · medias** — Pujas tibias
- publico: La subasta por el Archivo fue correcta. {grupo} pujaron poco y bien, que en estos tiempos de cobros ya es mucho.
- privado: El cofre del lote 12 salió de los jardines en un carruaje sin escudo. Nadie de su elenco sabe adónde fue.
  - si `asiste(irene)`: Irene siguió el carruaje con la mirada hasta el final de la calle. Luego le preguntó la hora a {mejor}, aunque llevaba reloj.

**Desenlace · desaire** — Una puja de más
- publico: En la subasta de los Serravalle se pujó más de lo que se podía pagar. La Crónica no dirá quién; ya lo sabe todo el mundo.
- privado: Leonora no la ha invitado al té del jueves. Es la primera vez en tres temporadas.

## Lección de protocolo · día 10 · palacio
*clase · plazas 1–3 · cualquiera*

> Mireya enseña cómo se habla a la reina: cuándo, cuánto y, sobre todo, cuándo no.

- \+ +1 en Estatus a cada asistente (hasta 4)
- \+ La reina estará en el río el sábado
- − Mireya no perdona una reverencia torcida

**Carta**

*Señora casamentera:*

Su Majestad bajará al río el sábado y, por primera vez en años, hablará con quien se le acerque. Eso me preocupa. El miércoles enseño en palacio lo que hay que saber: cómo se saluda, cuánto se habla y qué no se pregunta nunca. Mande a quien quiera que la reina recuerde su nombre por buenos motivos.

*Mireya, secretaria de listas*

**Al completarse**
- publico: {grupo} tomaron lección de protocolo con Mireya, en palacio. Se dice que salieron saludando a las columnas.
- privado: Mireya le escribe una línea: «Aprobados.» Viniendo de ella, es casi un abrazo.
  - si `asiste(isolda)`: Isolda casi no habló en toda la lección. Mireya dice que es justo lo que la reina prefiere: alguien que habla poco y, cuando habla, dice algo.
  - si `asiste(nilo)`: Nilo tuteó a Mireya dos veces y se corrigió tres. Mireya le hizo repetir el saludo hasta que dejó de sonreír.
  - si `asiste(teo)`: Teo preguntó qué no se le pregunta nunca a la reina. Mireya le contestó que eso, precisamente.
  - si `asiste(celia)`: Celia hizo la reverencia perfecta a la primera. Mireya no dijo nada, y Celia supo que eso era un elogio.
  - si `asiste(dario)`: Dario sabía ya todo el protocolo. Mireya le preguntó dónde lo había aprendido. «En casa de mi tía», dijo, «se practica mucho de noche.»

## Barcas al atardecer · día 12 · muelles
*paseo · plazas 2–2 · cualquiera*

> La víspera de los Faroles, los barqueros alquilan barcas para dos. Se rema poco y se habla mucho.

Requisito: presencia 4, chisme 5, intelecto 4
- \+ Dos personas solas en una barca se conocen deprisa
- − La corriente del Serel lleva hacia Arcos Bajos al caer la noche

**Carta**

*Señora:*

El viernes, víspera de los Faroles, el gremio alquila barcas para dos desde el muelle de las Lonjas. Se reman hasta el puente y se vuelve antes de que oscurezca. Si no se vuelve antes de que oscurezca, la culpa es de la corriente, que lleva hacia Arcos Bajos y no entiende de modales.

*Por el gremio, el maestre barquero*

**Incidente (día 12)** · Anochece antes de lo previsto y la corriente lleva la barca hacia Arcos Bajos. En la orilla, en un taller que debería estar cerrado, hay luz y se oye una prensa.

- **Remar con decisión de vuelta al muelle** (presencia, d 4)
  - Éxito: {mejor} rema contra la corriente sin perder el buen humor. Llegan al muelle con las manos rojas y riéndose.
  - A medias: Llegan, pero tarde y empapados. El barquero no cobra el retraso, por lástima.
  - Fallo: Los remos se cruzan, la barca gira dos veces y tiene que rescatarlos el gremio. Lo ve medio muelle.
- **Dejarse llevar y mirar quién trabaja en el taller** (chisme, d 4)
  - Éxito: Por la ventana se ve una silueta delgada, con manguitos de escribiente, colgando pliegos a secar. Al oír los remos, apaga la lámpara.
  - A medias: Sólo ven pliegos colgados, como ropa tendida. Luego la lámpara se apaga.
  - Fallo: La barca golpea el muelle del taller. La lámpara se apaga al instante y alguien cierra los postigos de un golpe.
- **Orientarse por los faroles ya colgados y buscar un remanso** (intelecto, d 4)
  - Éxito: {mejor} encuentra un remanso bajo el puente. Esperan a que la corriente afloje, y en la espera hablan más que en todo el otoño.
  - A medias: Encuentran el remanso, pero hace frío. Hablan poco, muy juntos.
  - Fallo: El remanso resulta ser un banco de barro. Esperan a los barqueros con el agua por los tobillos.

**Desenlace · favorable** — Bajo el puente
- publico: {grupo} pasearon en barca la víspera de los Faroles. Volvieron tarde, y nadie en el muelle se atrevió a preguntar de qué hablaban.
- privado: El barquero dice que es la barca que más tarde ha vuelto este otoño, y la única que volvió sin discutir.
  - si `chispa(a, b)`: Al bajar de la barca, {a} le tendió la mano a {b}, y tardaron un poco más de la cuenta en soltarse.
  - si `asiste(irene)`: Cuando pasaron cerca de Arcos Bajos, Irene se puso a hablar muy deprisa de otra cosa.

**Desenlace · medias** — Agua fría
- publico: {grupo} pasearon en barca y volvieron empapados. El Serel no respeta apellidos.
- privado: Bruna pone a secar dos pares de guantes junto a la chimenea y no hace preguntas.

**Desenlace · desaire** — Rescate en el muelle
- publico: El gremio de barqueros tuvo que rescatar a {grupo} la víspera de los Faroles. Valcenda se ha reído toda la mañana.
- privado: Los dos se culpan mutuamente. Con mucha educación, eso sí.

## Velada de los Faroles · día 13 · muelles
*encargo_real · plazas 3–3 · cualquiera · OBLIGATORIO*

> Valcenda suelta faroles sobre el Serel por lo que ardió hace ochenta años. Este año, la reina baja a los muelles y hablará con sus jóvenes.

Requisito: presencia 5, estatus 5, intelecto 5
- \+ La reina recordará a quien le hable bien
- \+ Una noche de recuerdo: se habla con el corazón
- − Es una conmemoración: un chiste a destiempo pesa el doble
- − Medio Valcenda lleva una Hoja en el bolsillo

**Carta**

*A la casamentera de la Temporada,*

Su Majestad bajará a los muelles del Serel el sábado, al caer la tarde, para soltar el primer farol por el Archivo. Desea que la acompañen tres jóvenes de la temporada, a su elección. La reina hablará con ellos. Le ruego que elija a quien sepa recordar sin entristecer, y escuchar sin mirar el reloj.

*Mireya, secretaria de listas*

**Incidente (día 13)** · La reina suelta su farol y se vuelve hacia sus jóvenes. «Dígame, ¿qué cree que perdió Valcenda aquella noche?» Mira a {a}. Detrás, en el agua, un farol hecho con un pliego impreso arde despacio.

- **Contestar con sinceridad: los nombres y las pruebas** (intelecto, d 5)
  - Éxito: {mejor} habla de los registros que nadie pudo rehacer: quién era hijo de quién, quién era dueño de qué. La reina escucha sin interrumpir. «Exacto», dice. «Y alguien se aprovechó.»
  - A medias: La respuesta es buena, pero larga. La reina asiente con educación y mira el agua.
  - Fallo: {mejor} se enreda en fechas y apellidos. Varias casas carraspean a la vez.
- **Contestar como enseñó Mireya: breve, digno y sin nombres** (estatus, d 5)
  - Éxito: «La memoria, Majestad. Por eso estamos aquí.» La reina sonríe por primera vez en la noche. Mireya respira.
  - A medias: La respuesta es correcta. La reina la ha oído cien veces y lo agradece, pero no la recordará.
  - Fallo: La reverencia sale torcida y la frase, a medias. Mireya cierra los ojos.
- **No contestar: ofrecerle un farol para que lo suelte por quien ella quiera** (presencia, d 5)
  - Éxito: La reina toma el farol y se queda callada mucho tiempo. Lo suelta sin decir por quién. Al volverse, tiene los ojos brillantes y no lo disimula.
  - A medias: La reina acepta el farol con una cortesía distante. Lo suelta y sigue su camino.
  - Fallo: El farol se apaga antes de tocar el agua. Alguien se ríe y se calla de golpe.

**Desenlace · favorable** — Mil faroles
- publico: La reina soltó el primer farol y habló largo con {grupo}. Nadie recuerda una Noche de los Faroles tan hermosa, ni tan comentada.
  - si `asiste(celia) y asistio(s3_clase, celia)`: Celia Lobreda contestó a la reina sin una sola duda. La reina le preguntó dónde había aprendido. «Sola, Majestad», dijo Celia.
  - si `asiste(saul) y asiste(isolda) y marca(semilla_lavanda)`: El capitán Veyra y la señorita Marén soltaron un farol juntos. La reina comentó que hacían buena pareja. Ninguno de los dos supo qué contestar.
  - si `asiste(nilo)`: Nilo Lobreda ayudó a los barqueros a soltar los faroles de los que no tenían a nadie que los soltara. La reina lo vio, y no dijo nada.
- privado: Mireya le hace llegar una nota: «Su Majestad pregunta si usted cree, como ella, que algunas cosas no ardieron.»
  - si `asiste(irene)`: Irene soltó un farol sin nombre. Cuando le preguntaron por quién era, dijo: «Por los que nadie apuntó.»

**Desenlace · medias** — Una noche correcta
- publico: La Velada de los Faroles fue solemne y correcta. La reina saludó a {grupo} con cortesía, y volvió pronto a palacio.
- privado: En el agua flotaban, entre los faroles, restos de pliegos impresos. Alguien los había usado de papel.

**Desenlace · desaire** — Un farol apagado
- publico: En la Noche de los Faroles, la reina se retiró antes de tiempo. Se dice que algo la incomodó entre los jóvenes de la casamentera.
- privado: Mireya no le ha escrito. Usted sabe ya lo que significa que Mireya no escriba.

**Desenlace · sin_asistentes**
- publico: La casamentera no acompañó a la reina en la Noche de los Faroles. La reina soltó su farol sola.

## Crónica de salones · Número 3 · Impreso por Calce, Calle de los Sellos

*Mil faroles en el río y un solo tema en los salones. Esta Crónica no se lo dirá, porque ya lo sabe usted.*

- **La reina en el río** (texto del desenlace)
- **Martillo en los jardines** (texto del desenlace)
- **Dos en una barca** (texto del desenlace)
- **Reverencias** (texto del desenlace)
- **Se busca impresor**: Esta Crónica ofrece diez coronas a quien diga dónde se imprime la Hoja sin Firma. No por celos: por oficio.
- **Faroles de más**: Los cereros de la Calle de los Sellos se quedaron sin velas el viernes. Dicen que alguien compró cuarenta de golpe, y que pagó en monedas de cobre.

*La Crónica firma todo lo que publica. Incluso esto.*

## La Hoja sin Firma · nº 2

*Hace ochenta años ardió el Archivo. No ardió todo.*

Sobrevivieron páginas del Pacto del Umbral, el documento que se dio por perdido aquella noche. Algunas casas lo saben, porque las han comprado. Otras lo temen, porque aparecen en ellas.
- si `marca(cofre_para_archivo)`: Esta semana un cofre de papeles quemados volvió al Archivo, y Valcenda aplaudió. Interesante. ¿Por qué nadie preguntó qué faltaba dentro?
- si `no marca(cofre_para_archivo)`: Esta semana alguien pagó el triple por un cofre de papeles quemados. Interesante. ¿Por qué se paga tanto por ceniza?

*— Folio 81, que sigue a donde lo dejamos.*

## Sólo para sus ojos

- si `marca(pista_sello_umbral)`: Dibuja de memoria el sello del cofre: una puerta abierta dentro de un círculo. Lo guarda entre las páginas de la Hoja nº 2. Encaja demasiado bien.
- si `marca(pujador_miraves)`: Amalia Miravés quería esos papeles. La tía de Dario no compra nada que no necesite.
- si `marca(pista_taller_arcos)`: Un taller de Arcos Bajos con la prensa en marcha a medianoche y pliegos colgados a secar. Y una silueta con manguitos de escribiente.
- si `marca(pista_mala_impresion) y marca(pista_taller_arcos)`: Mara tenía razón: la Hoja no sale de sus prensas, que imprimen limpio. Sale de una prensa vieja, manejada por alguien que no es impresor.
- si `marca(catalejo_maren)`: Los Marén pagaron el seguro del Clara de Nácar sin discutir, y ahora compran el catalejo de su capitán. Isolda no sabe nada. O eso parece.
- si `marca(reina_interes) o marca(reina_conmovida)`: La reina también cree que algo no ardió. Si es así, la temporada no termina en un baile: termina en el Archivo.
- si `semana == 3`: Mitad de temporada. Sus jóvenes empiezan a tutearse en los rincones. Usted empieza a no tutear a nadie.

## Gancho

- **nota**: Señora: la reina ha dejado caer en palacio que alguien de su elenco sabe del Archivo más de lo que dice.
- **nota**: Y otra cosa. El teatro de gala es el día 20, con luna llena. Nilo ha preguntado dos veces a qué hora termina la función.
