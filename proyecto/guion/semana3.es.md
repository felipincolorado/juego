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

*(Cierre pendiente: se escribe en la parte 2.)*
