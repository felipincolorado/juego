# Semana 2 · Primeras impresiones

**Cobros de otoño.** Vencen los cobros de otoño. Las casas con deudas sonríen más de lo normal y gastan menos de lo que aparentan.

## Apertura

- **nota**: Señora: el sobre sin firma sigue en su escritorio. Folio 80, legajo de la Noche del Censo.
- **nota**: Podría preguntar en el Archivo, con discreción. O guardarlo y esperar a que quien lo escribió vuelva a hacerlo.
- Opción **Preguntar con discreción en el Archivo** → Un escribiente le dice que ese legajo «no se presta». Después baja la voz: «Aunque alguien lo pidió hace un mes. Alguien de la casa.»
- Opción **Guardarlo y esperar** → Lo guarda con las demás cartas. Si quien lo escribió quiere algo de usted, volverá a escribir.

## Peticiones

- **teo** pide `s2_molinos`: Teo: «Mi padre abre los molinos esta semana. Si va alguien de su elenco, la ribera entera hablará de los Rovena. Si no va nadie, también.»
  - Si se cumple: Teo le manda una nota con un solo verso: «Gracias, y que no se entere mi orgullo.»
  - Si no: Teo no dice nada. Es la primera vez que no hace un chiste sobre algo.
- **isolda** pide `s2_cena_salvat`: Isolda, muy bajito: «Si… si hubiera un sitio libre en la cena de la Calle de los Sellos, a mí me gustaría ir. Sólo si sobra.»
  - Si se cumple: Isolda le da las gracias tres veces y se pone una pluma nueva en el pelo. No explica por qué esa cena.
  - Si no: Isolda dice que lo entiende perfectamente. Lo dice demasiado deprisa.

## Jornada en los molinos · día 4 · muelles
*paseo · plazas 2–4 · cualquiera*

> Dos días río arriba, entre ruedas de agua y almuerzos al sol. Los Rovena quieren que se hable de ellos, y bien.

Requisito: presencia 5, estatus 4, intelecto 5
- \+ Dos días juntos acercan mucho a quienes van
- − El cielo amenaza lluvia, y la ribera se embarra
- − Quien vaya no podrá asistir a nada más el jueves ni el viernes

**Carta**

*Distinguida casamentera:*

Los molinos Rovena llevan tres generaciones moliendo el grano que come Valcenda. Este otoño abrimos sus puertas durante dos días: barcas, almuerzo junto a las ruedas y una cena sencilla en la casa del río. Mi hijo insiste en que sus jóvenes lo pasarán bien. Yo insisto en que lo cuenten después.

*Aurelio Rovena*

**Incidente (día 5)** · Llueve. Bajo el alero, un grupo de arrendatarios espera al señor Rovena: les deben los jornales de dos meses. Los invitados lo están viendo.

- **Acercarse a los arrendatarios y escucharlos** (presencia, d 5)
  - Éxito: {mejor} los escucha bajo la lluvia sin apurarlos. Cuando llega Rovena, ya no hay gritos: hay una fecha de pago.
  - A medias: Los arrendatarios se calman a medias. Uno de ellos se queda mirando a los invitados con rencor.
  - Fallo: {mejor} no encuentra las palabras. Los gritos llegan hasta el comedor.
- **Revisar con el administrador las cuentas del molino** (intelecto, d 5)
  - Éxito: Las cuentas cuadran a medias: los molinos ganan, pero los adelantos de cosecha se los come una deuda con los Miravés. Hay dinero para los jornales si se retrasa otra cosa.
  - A medias: El administrador enseña unas cuentas y esconde otras. Algo no cuadra, y {mejor} lo nota.
  - Fallo: El administrador se ofende. Rovena se entera de que alguien ha mirado sus libros.
- **Distraer a los invitados con un buen cuento junto al fuego** (chisme, d 4)
  - Éxito: Junto al fuego, {mejor} cuenta una historia tan buena que nadie mira por la ventana.
  - A medias: La historia funciona hasta que alguien pregunta por los gritos de fuera.
  - Fallo: La historia se cae a la mitad. Todos miran por la ventana a la vez.

**Indisposición (días [6, 7])** · asistente de s2_molinos que también esté en s2_baile_casas, el de Presencia más baja: {a} volvió de los molinos con fiebre. Bruna dice que no se levantará hasta el lunes.

**Reemplazo en `s2_baile_casas`** · {a} no podrá bailar el domingo. El baile es obligatorio: alguien tiene que ocupar su lugar.
- Enviar a otra persona en su lugar
- Ir con una pareja menos
- Enviar disculpas a los anfitriones
- resultado_reducir: Una sola pareja abrirá el baile de su casa. Se notará el hueco, pero no tanto como una silla vacía.
- resultado_retirar: Las casas reciben sus disculpas. Las aceptan en voz alta y las comentan en voz baja.

**Desenlace · favorable** — Dos días río arriba
- publico: Los invitados de los Rovena volvieron de los molinos encantados, embarrados y con historias. La ribera habla bien de la casa, por una vez.
  - si `asiste(teo)`: Teo Rovena enseñó los molinos de su familia con un orgullo que nadie le conocía. Hubo quien olvidó que alguna vez bromeó sobre ellos.
- privado: Aurelio Rovena le escribió una carta de agradecimiento demasiado larga para un hombre que dice no tener tiempo.
  - si `opcion(s2_molinos) == cuentas`: Ahora sabe que los molinos Rovena deben dinero a la casa Miravés. Teo no lo sabe. O finge muy bien.

**Desenlace · medias** — Barro y buena voluntad
- publico: La jornada en los molinos Rovena fue agradable cuando no llovía. Llovió bastante.
- privado: Teo le pregunta, como quien no quiere la cosa, si alguien comentó algo de los jornales. Usted no contesta. Él tampoco insiste.

**Desenlace · desaire** — Gritos bajo la lluvia
- publico: En los molinos Rovena, los arrendatarios reclamaron sus jornales delante de los invitados. La Crónica lamenta no haber estado allí; ya tiene tres versiones.
- privado: Teo no le ha escrito desde entonces. Su padre, sí: para decir que nunca más.

## Cena en la Calle de los Sellos · día 6 · archivo
*cena · plazas 2–3 · cualquiera*

> La familia Salvat recibe en su casa, encima de los depósitos del Archivo. Se habla en voz baja, por costumbre.

Requisito: intelecto 5, chisme 5, estatus 3
- \+ Aquí se sabe de verdad quién debe qué a quién
- − Las conversaciones son largas y nadie baila

**Carta**

*Estimada señora:*

Mi hija Irene me asegura que usted es persona de confianza, y mi hija no se equivoca casi nunca. El sábado cenaremos en casa, sobre los depósitos. No hay música ni espejos: hay buen vino y mejores papeles. Traiga a quien sepa escuchar. En esta calle, quien escucha, aprende.

*Tomás Salvat*

**Incidente (día 6)** · Un viejo escribiente, algo bebido, comenta que alguien pidió el legajo de la Noche del Censo hace un mes «y lo devolvió más ligero». Irene deja la copa en la mesa.

- **Sonsacarle al escribiente quién lo pidió** (chisme, d 5)
  - Éxito: El escribiente no recuerda el nombre, pero sí la letra del registro: «Pequeña, muy ordenada. De alguien de aquí.»
  - A medias: El escribiente empieza a contarlo y Tomás Salvat le sirve más vino para que olvide.
  - Fallo: La pregunta suena a interrogatorio. La mesa se queda en silencio.
- **Pedir, con interés de erudito, ver el libro de préstamos** (intelecto, d 5)
  - Éxito: Tomás Salvat enseña el libro con orgullo de archivero. En la línea del legajo, la firma está tachada; la letra de la fecha es pequeña y muy ordenada.
  - A medias: Les enseñan el libro, pero la página del legajo está doblada. Nadie se atreve a desdoblarla en la mesa.
  - Fallo: Tomás Salvat sonríe y dice que los libros no salen de la mesa de trabajo. La conversación cambia.
- **Cambiar de tema con gracia, por cortesía con los anfitriones** (presencia, d 4)
  - Éxito: Un brindis por las hijas que aprenden el oficio de sus padres. Irene levanta la copa y, por un momento, mira a {mejor} con alivio.
  - A medias: El tema cambia, pero el escribiente sigue murmurando en su rincón.
  - Fallo: El brindis llega tarde y suena a que todos ocultan algo.

**Desenlace · favorable** — Vino y buenos papeles
- publico: {grupo} cenaron en casa de los Salvat, en la Calle de los Sellos. Dicen que hablaron de historia hasta la medianoche, y que nadie se aburrió.
  - si `asiste(isolda)`: La señorita Marén, tan callada, hizo una pregunta sobre los registros del puerto que dejó en silencio a la mesa entera. Irene Salvat la contestó durante media hora.
- privado: Al despedirse, Irene le escribe una nota de dos líneas: «Vuelva. En esta calle se escucha mejor que en los salones.» La letra es pequeña y muy ordenada.
  - si `asiste(isolda) y asiste(irene)`: Isolda e Irene se quedaron hablando en la escalera cuando todos ya se habían ido. Isolda volvió sin la pluma del pelo. No parecía importarle.

**Desenlace · medias** — Una cena callada
- publico: {grupo} cenaron con los Salvat. Fue una cena seria, en una calle seria.
- privado: Tomás Salvat les acompañó hasta la puerta y miró la calle antes de cerrar. A un lado y al otro.

**Desenlace · desaire** — Preguntas de más
- publico: Se comenta que en casa de los Salvat alguien preguntó lo que no debía. Los archiveros no lo olvidarán pronto.
- privado: Irene no le ha devuelto el saludo esta mañana. Lo ha visto. Ha decidido no verlo.

## Baile de las casas · día 7 · salon
*baile · plazas 4–4 · parejas · OBLIGATORIO*

> Cada casa presenta a sus jóvenes en el Salón de las Columnas. Usted presenta dos parejas, y Valcenda decide quién brilla.

Requisito: baile 5, estatus 4, presencia 5
- \+ Bailar juntos acerca el doble que una cena
- − Las casas con deudas vigilarán quién baila con quién

**Carta**

*A la casamentera de la Temporada,*

Como cada otoño, las casas abrirán el Salón de las Columnas para el primer gran baile. Le corresponden dos parejas en el segundo vals. Le recuerdo, con todo el respeto, que la reina leerá la Crónica del lunes. Las casas Lobreda y Veyra han pedido mesas contiguas. No pregunte por qué; ya lo sabe.

*Mireya, secretaria de listas*

**Incidente (día 7)** · Al empezar el segundo vals, aparecen sobre las mesas unos pliegos impresos, sin firma. Todo el salón lee a la vez. Algunos miran hacia {a} y {b}.

- **Seguir bailando como si nada** (baile, d 5)
  - Éxito: Las dos parejas siguen el vals sin perder el compás. Al tercer giro, el salón vuelve a mirar el baile y no los pliegos.
  - A medias: Una de las parejas pierde el paso un instante. Lo justo para que alguien lo apunte.
  - Fallo: El vals se rompe. Las parejas se quedan quietas en mitad del salón, leyendo como todos.
- **Pedir a los anfitriones que recojan los pliegos** (estatus, d 5)
  - Éxito: Los criados recogen los pliegos antes del tercer vals. Los que quedan circulan escondidos en los guantes, que es peor para la reputación de quien los lee.
  - A medias: Se recogen la mitad. La otra mitad ya está en los bolsillos.
  - Fallo: La petición llega tarde y se interpreta como miedo. ¿Qué tiene que esconder la casamentera?
- **Averiguar quién dejó los pliegos** (chisme, d 4)
  - Éxito: Nadie vio quién los dejó, pero {mejor} se fija en el papel: es de cuadernillo cosido, con el borde cortado. Papel de descarte, del que usan los escribientes.
  - A medias: Un criado jura que los pliegos llegaron en una cesta de flores. Las flores eran de la floristería de la Calle de los Sellos.
  - Fallo: La pregunta circula más deprisa que los pliegos. Ahora todos sospechan de todos.

**Desenlace · favorable** — El segundo vals, el mejor
- publico: Ni los pliegos sin firma pudieron con el segundo vals: {grupo} bailaron como si el salón fuera suyo. La Crónica no recuerda un primer baile tan comentado.
  - si `asiste(saul) y asiste(celia)`: Saúl Veyra y Celia Lobreda volvieron a bailar juntos. Las mesas Lobreda y Veyra brindaron a la vez. Ya nadie dice «rumor»: dicen «cuándo».
  - si `asiste(dario) y asiste(celia)`: Dario Miravés y Celia Lobreda, otra vez. Valcenda empieza a hablar de ellos como de una pieza de música: en pareja.
  - si `asiste(teo) y asiste(irene)`: Teo Rovena bailó con Irene Salvat y, por una vez, no hizo ni un chiste. Ella le corrigió el paso dos veces. Él le dio las gracias las dos.
- privado: Mireya le hace llegar una nota: «Su Majestad pidió la Crónica antes que el desayuno.»

**Desenlace · medias** — Un baile interrumpido
- publico: El Baile de las casas tuvo dos protagonistas: el segundo vals, que fue correcto, y unos pliegos sin firma, que fueron otra cosa.
- privado: Al salir, encuentra un pliego en el asiento de su carruaje. Alguien quería asegurarse de que lo leyera.

**Desenlace · desaire** — El baile de los pliegos
- publico: Del Baile de las casas sólo se recordará el escándalo y que {grupo} se quedaron quietos en mitad del salón.
- privado: La reina no pidió la Crónica. Mireya dice que eso es peor.

**Desenlace · sin_asistentes**
- publico: La casamentera no presentó parejas en el Baile de las casas. Las demás casas bailaron más tiempo, y hablaron de ella entre vals y vals.

## Crónica de salones · Número 2 · Impreso por Calce, Calle de los Sellos

*Semana de cobros, semana de sonrisas. Nunca se baila tan bien como cuando se debe dinero.*

- **El segundo vals** (texto del desenlace)
- **Un pliego sin modales**: Esta Crónica no sabe quién imprimió la hoja que circuló el domingo, y lo lamenta: nos habría gustado contratarlo. Lamentamos aún más su falta de firma.
- **Ruedas y lluvia** (texto del desenlace)
- **Calle de los Sellos** (texto del desenlace)
- **Lo que se dijo en la imprenta**: Un invitado a nuestra velada de lectura nos confió el nombre de la pareja de la temporada. Lo publicamos con gusto. Si no es cierto, lo será.
- **Cobros**: Tres casas han vendido caballos esta semana y ninguna lo admite. Las cuadras de Alto Laurel están más vacías que sus promesas.

*La Crónica firma todo lo que publica. Que conste.*

## La Hoja sin Firma · nº 1

*Valcenda guarda sus secretos en cajones. Nosotros guardamos las llaves.*

Secreto según quién tenga más fama:
- **nilo**: El joven Lobreda ayuda a todo el mundo. Pregunten en el paso de Greda quién paga el socorro de invierno que su casa debe desde hace dos años.
- **saul**: El capitán Veyra rechazó dos compromisos antes de esta temporada. Su familia dice que por deber. ¿Por qué nadie pregunta por qué?
- **dario**: El heredero Miravés ha asistido a once fiestas al aire libre en tres años. Ha llegado a todas cuando ya se ponía el sol.
- **teo**: Los molinos Rovena llevan dos meses sin pagar a sus arrendatarios. El ingenio de la casa no alcanza para los jornales.
- **celia**: La señorita Lobreda ensaya cada noche con un maestro de baile que su rama de la familia no puede pagar. ¿Quién paga?
- **irene**: Una archivera fue vista en los depósitos del Archivo pasada la medianoche. El Archivo dice que es imposible. El Archivo dice muchas cosas.
- **isolda**: Hace dos otoños, la casa Marén pagó sin discutir el seguro de un barco hundido. Las aseguradoras de Nácar nunca pagan sin discutir. ¿Por qué la señorita Marén palidece cuando alguien nombra el «Clara de Nácar»?
- **camila**: La viuda Ferrán sonríe mucho para alguien con una deuda que vence este otoño. Pregunten a la casa Miravés por el «Clara de Nácar».

*¿Por qué todos lo leen y nadie pregunta si es cierto? — Legajo 80.*

## Sólo para sus ojos

- si `marca(pista_letra_registro) y marca(sobre_guardado)`: Compara la letra del sobre sin firma con lo que le contaron del registro: pequeña, muy ordenada. No es una prueba. Es una coincidencia que no la deja dormir.
- si `marca(pista_papel_descarte)`: Guarda un pliego de la Hoja junto al sobre de la semana pasada. El papel es del mismo cuadernillo cosido.
- si `marca(deuda_rovena_vista)`: Los molinos Rovena deben dinero a los Miravés. Teo no lo ha dicho. Dario, tampoco.
- si `marca(irene_agradecida)`: Irene le envía un libro sin nota. Es una historia del Archivo anterior al incendio. Hay una página doblada: la del folio 80.
- si `semana == 2`: Primera semana de cobros, primera Hoja. Alguien en Valcenda ha decidido que la temporada no será sólo de bailes.

## Gancho

- **nota**: Señora: Mara Calce ha venido dos veces. Quiere saber si usted sabe quién imprimió la Hoja. Le dije que no. ¿Hice bien?
- **nota**: La reina baja al río la semana que viene, para los Faroles. Dicen que no lo hacía desde que era niña.
