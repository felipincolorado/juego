# Escenas del capítulo 5: besos, confesiones y acuerdos

## saul y dario · La sala pequeña de la residencia, con la chimenea apagándose
*beso_saul_dario · beso* · si `nivel(saul, dario) >= A`

- **dario**: Mañana te vas a Tiria, o te quedas. Y yo sigo sin saber cuál de las dos me da más miedo.
- **saul**: A mí me da miedo esto.
- **narración**: Saúl se quita los guantes, despacio, uno y luego el otro. Esta vez no los deja en la mesa: los deja caer.
- **narración**: Dario es el que se acerca. Saúl es el que no se aparta.
- **narración**: Cuando Bruna entra a avivar el fuego, ya no hace falta.

> 

## irene y isolda · La sala de lectura del Archivo, de noche
*beso_irene_isolda · beso* · si `nivel(irene, isolda) >= A`

- **irene**: Antes de que pase nada, tengo que contarte algo. Sobre lo que hago de noche.
- **isolda**: ¿Es peligroso?
- **irene**: Para otros. Para gente que no lo merece, quizá.
- **isolda** (ruborizada): Entonces cuéntamelo después. Ahora es mi turno de hablar primero.
- **narración**: Isolda no dice nada más. No hace falta: esta vez, es ella quien se acerca.

> 

## nilo y camila · El invernadero de los Ferrán, al anochecer
*beso_nilo_camila · beso* · si `nivel(nilo, camila) >= A`

- **camila**: He tirado las plantas de Julián. Todas menos una.
- **nilo**: ¿Por qué ésa?
- **camila** (alegre): Porque es la que regaste tú.
- **narración**: Nilo abre la boca para prometer algo. Camila se la cierra antes de que pueda.
- **narración**: Por una vez, Nilo Lobreda no ofrece nada. Sólo se queda.

> 

## teo y celia · El salón vacío, con un solo violinista
*beso_teo_celia · beso* · si `nivel(teo, celia) >= A`

- **teo**: El violinista me ha cobrado el doble por quedarse. Dice que esta vez no tiene que tocar mal.
- **celia**: ¿Y tú vas a bailar bien?
- **teo**: No. Pero voy a dejar de contar los chistes.
- **narración**: Bailan. Teo no la pisa. Celia no cuenta. En el tercer giro, ninguno de los dos sigue bailando.
- **narración**: El violinista sigue tocando, de espaldas, con mucha discreción y bastante orgullo.

> 

## dario y celia · La Academia, junto al piano
*beso_dario_celia · beso* · si `nivel(dario, celia) >= A`

- **celia**: Toca algo. Pero de verdad.
- **narración**: Dario toca. Sin una sola nota falsa, y tan despacio que parece otra persona.
- **dario**: Es la primera vez que toco sin que nadie me aplauda.
- **celia** (alegre): No pienso aplaudir. Tengo otra idea.
- **narración**: La última nota se queda sonando sola. Ninguno de los dos la termina.

> 

## teo y irene · La biblioteca de los Salvat, entre estanterías
*beso_teo_irene · beso* · si `nivel(teo, irene) >= A`

- **irene**: He leído todos tus versos. Los del cuaderno y los que tachaste.
- **teo** (ruborizada): ¿Y?
- **irene**: Me los creo.
- **narración**: Teo empieza un chiste por costumbre y se le olvida a la mitad. Irene no le deja recordarlo.

> 

## dario y isolda · El despacho de los Marén, junto a la maqueta del puerto
*conf_dario_isolda · confesion* · si `cercania(dario, isolda) >= 10`

- **dario**: Isolda. Desde que teníamos ocho años, te he defendido de todo el mundo. Creo que también me estaba defendiendo de esto.
- **isolda**: Dario…
- **dario**: No digas nada. Lo veo en tu cara. No es «todavía no». Es «no».
- **isolda** (ruborizada): No es por ti. Es que yo… no puedo querer así a ningún caballero. Eres el primero al que se lo digo.
- **narración**: Dario se queda callado mucho rato. Después le tiende la mano, como cuando eran niños, para salir del escondite.
- **dario** (alegre): Entonces seguiré defendiéndote. Ahora sé de qué.

> 

## celia y saul · La sala de actas del Archivo, vacía
*conf_celia_saul · confesion* · si `cercania(celia, saul) >= 10 y marca(compromiso_paso_propuesto)`

- **celia**: Capitán. Firmé la primera página pensando que era un negocio. Ya no lo es. Para mí, no.
- **saul**: Señorita Lobreda. Celia. Usted merece a alguien que la mire como usted me mira ahora.
- **celia** (molesta): ¿Y usted no puede?
- **saul**: No. Y no es por usted. Le pido que no me pregunte más, y le prometo que nunca le mentiré sobre esto.
- **narración**: Celia cuenta en voz baja hasta tres. Luego deja de contar.
- **celia**: Entonces no firmaré la última página. No por orgullo. Porque quiero bailar con alguien que no cuente los pasos para huir.

> 

## a y b · Un rincón del salón, al final de la velada
*conf_generica · confesion* · si `cercania(a, b) >= 10`

- **a**: Tengo que decírtelo una vez, aunque ya sepa la respuesta. Te quiero más de lo que debería.
- **b**: Lo sé. Y lo siento. No puedo darte lo mismo.
- **narración**: {a} asiente. Duele menos de lo que esperaba, y más de lo que dice.

> 

## saul y isolda · El despacho de los Veyra, con dos copas y un contrato
*acuerdo_saul_isolda · acuerdo* · si `marca(lavanda_hablada)`

- **saul**: Mi padre quiere un vínculo formal con los Marén. El ejército quiere que vuelva a Tiria si no me caso. Y yo quiero quedarme en Valcenda.
- **isolda**: Mi padre quiere un yerno que proteja los convoyes. Y yo quiero que nadie me pregunte nunca por qué no estoy enamorada de mi marido.
- **saul**: Te ofrezco mi nombre, mi respeto y una puerta que siempre podrás cerrar.
- **isolda**: Y yo a ti lo mismo. Y una casa donde nadie mire tus guantes.
- **narración**: Brindan sin sonreír. Luego sonríen sin brindar. Es el contrato más sincero que se ha firmado en esa mesa.
- **isolda** [si `nivel(irene, isolda) >= A`]: Saúl. Hay alguien. No quiero dejar de verla.
- **saul** [si `nivel(irene, isolda) >= A`]: Lo sé. Para eso es la puerta.
- **saul** [si `nivel(irene, isolda) >= A y nivel(saul, dario) >= A`]: Yo también tengo a alguien detrás de la mía.

> 

## saul y celia · Una galería del palacio, a media tarde
*acuerdo_saul_celia · acuerdo* · si `marca(compromiso_paso_propuesto) y no marca(celia_rechaza_paso) y no marca(acuerdo_lavanda)`

- **celia**: Nuestras casas ya lo han decidido. Sólo falta que lo decidamos nosotros.
- **saul**: Seré un marido correcto. Puntual. Leal a su casa. No le pediré nada que no quiera darme.
- **celia**: Es la proposición menos romántica que me han hecho.
- **saul**: Es la más honrada que sé hacer.
- **narración**: Celia cuenta los pasos hasta el final de la galería. Doce. Los cuenta dos veces.
- **celia**: Lo pensaré hasta el Gran Baile. Si digo que sí, no será por mi casa.

> 

## teo y camila · La salita de los Ferrán, con las cuentas sobre la mesa
*acuerdo_teo_camila · acuerdo* · si `cercania(teo, camila) >= 6 y no marca(deuda_saldada)`

- **camila**: Tu padre quiere casarte con dinero. Yo tengo dinero y una deuda que me quieren cobrar dos veces.
- **teo**: ¿Me está proponiendo matrimonio, señora Ferrán?
- **camila**: Te estoy proponiendo un negocio. Tu apellido me protege de los Miravés; mi fortuna salva tus molinos. Julián te quería como a un hermano pequeño.
- **teo**: ¿Y el amor?
- **camila** (alegre): Ya lo tuve una vez. Ahora quiero a alguien que me haga reír por las mañanas. Tú eres muy bueno en eso.
- **teo**: Es el chiste más serio que me han contado.
- **narración**: No dicen que sí. Tampoco que no. Teo se lleva las cuentas a casa para leerlas, y no hace ni un chiste en el camino.

> 
