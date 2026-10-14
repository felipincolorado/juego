# Semana 6 · Gran Baile del Sello

**La primera escarcha.** Cae la primera escarcha sobre Valcenda. El domingo, en el Salón de las Columnas, la reina sellará las uniones de la temporada en el libro del Archivo.

## Apertura

- **nota**: Señora: es la última semana. El carnet de baile está sobre su mesa y la nota del Archivo, debajo.
- **nota**: La nota dice «antes del baile». El Archivo abre el viernes por la noche, para preparar el libro de los sellos.
- si `marca(acuerdo_lavanda)`: Saúl e Isolda han enviado juntos una carta a sus padres. Esta vez sí la han enviado.
- si `marca(deuda_saldada)`: Camila ha venido a darle las gracias en persona. Ha traído un catalejo viejo: «Me lo devolvió Isolda Marén. Ninguna de las dos lloró. Casi.»
- si `marca(celia_rechaza_paso)`: Celia ha devuelto la última página de las capitulaciones sin firmar. Su padre no le habla. Ella baila sola cada mañana, sin contar.
- Opción **Ir al Archivo el viernes por la noche** → Lo apunta en su agenda con una sola palabra: «Archivo». Después la tacha, y la vuelve a escribir.
- Opción **No ir: hay cosas que es mejor no saber** → Guarda la nota con el sobre de la primera semana. Si la temporada termina sin saberlo, que termine así.

## Peticiones

- **nilo** pide no ir a nada el día 4: Nilo: «El sábado no me mande a nada. Tengo que contarle a alguien lo que me pasa las noches de luna. Si no lo hago ahora, no lo haré nunca.»
  - Si se cumple: El domingo, Nilo llega al baile con la cara de quien ha dormido por primera vez en años. No dice a quién se lo contó. Se le nota.
  - Si no: Nilo no se lo cuenta a nadie. Sonríe toda la semana, como siempre. Como siempre, demasiado.

## La primera escarcha · día 1 · jardines
*paseo · plazas 2–4 · cualquiera*

> Los jardines amanecen blancos. El último paseo de la temporada, para decir en voz baja lo que no se dirá en el baile.

Requisito: presencia 4, chisme 4, baile 3
- \+ Lo que se dice con frío se recuerda mucho tiempo
- − Leonora ha invitado también a los padres

**Carta**

*Querida casamentera:*

Mis ásteres se han helado esta noche. Es lo que tiene el otoño: cuando por fin está bonito, se termina. El miércoles paseamos entre la escarcha por última vez. Traiga a quien aún tenga algo que decir.

*Leonora Serravalle*

**Desenlace · favorable** — Huellas en la escarcha
- publico: {grupo} pasearon por los jardines helados de los Serravalle. Dejaron huellas en la escarcha, y algunas iban en pareja.
- privado: Leonora le dice al despedirse: «Ha sido una buena temporada. La echaré de menos, y no lo diré en público.»

**Desenlace · medias** — Frío
- publico: El paseo de la primera escarcha fue breve: hacía demasiado frío para decir nada.
- privado: Algunos padres vigilaron cada paso. Nadie se atrevió a dar ninguno.

**Desenlace · desaire** — Hielo
- publico: En el paseo de la escarcha hubo resbalones, y no todos fueron por el hielo.
- privado: Leonora le manda un frasco de linimento. Sin nota. Con mucha intención.

## Gran Baile del Sello · día 5 · salon
*baile · plazas 8–8 · cualquiera · OBLIGATORIO*

> Doce valses, ocho jóvenes y un libro abierto sobre un atril. Al final de la noche, la reina sellará lo que la temporada haya unido.


**Carta**

*A la casamentera de la Temporada,*

Su Majestad la espera el domingo en el Salón de las Columnas con sus ocho jóvenes. Habrá doce valses y un solo libro. Rellene el carnet con cuidado: lo que se baila esta noche se sella al amanecer. Su Majestad desea añadir, de su puño y letra, que ha disfrutado de esta temporada más que de ninguna.

*Mireya, secretaria de listas*

## Crónica de salones · Número extraordinario · El Gran Baile del Sello

*Doce valses, un libro y una Hoja. Esta Crónica no recuerda una noche igual, y lleva treinta años recordando noches.*

- **Lo que la reina selló**: Su Majestad selló al amanecer las uniones de la temporada. La lista completa, en la página dos. Las lágrimas, en todas.
- **La archivera**: La autora de la Hoja sin Firma es Irene Salvat, del Archivo Real. Esta Crónica, que la sospechó de todo el mundo menos de ella, se quita el sombrero. Y le ofrece trabajo.
- **El último pliego**: La Hoja sin Firma se despidió en el Gran Baile. Sigue sin firma. Esta Crónica sigue buscando, aunque ya sin recompensa.
- **Una nota de la editora**: Esta Crónica firma todo lo que publica. Esta temporada ha aprendido que firmar no basta: también hay que tener razón.

*Fin de la temporada. Mara Calce, editora.*

## La Hoja sin Firma · Último número · nº 5

*Ochenta años después, lo que no ardió.*

Esta Hoja publica hoy los folios 80 a 84 del Archivo Real: las casas que, la Noche del Censo, quemaron sus linajes para quedarse con lo que no era suyo. Sus nombres están abajo. Que la reina haga justicia; nosotros sólo hemos hecho memoria.
- si `marca(nombres_protegidos_final) o nivel(irene, isolda) >= A o nivel(irene, teo) >= A`: Las páginas del Pacto del Umbral se quedan donde estaban. Quien sólo quería esconderse tiene derecho a seguir escondido.
- si `marca(hoja_completa) o no (marca(nombres_protegidos_final) o nivel(irene, isolda) >= A o nivel(irene, teo) >= A)`: Publicamos también las páginas del Pacto del Umbral, con todos sus nombres. Entre ellos, el de una casa de Greda Alta cuyos hijos no salen las noches de luna.

*— Firmado: I. S., archivera. Ya no hace falta esconderse.*

## Sólo para sus ojos


## Gancho


## Epílogos

### nilo
- si `marca(nilo_confiesa) y union(nilo, camila)`: Nilo se casó con Camila en primavera. Las noches de luna, ella cierra los postigos del invernadero y riega las plantas hasta el amanecer. Nunca le ha pedido que prometa nada.
- si `marca(nilo_confiesa) o marca(nilo_elige_promesa)`: Nilo aprendió a medir lo que promete. Alguien en Valcenda conoce su secreto y lo guarda. Las noches de luna ya no las pasa solo.
- si `marca(hoja_completa) o marca(nilo_visto)`: La Hoja final puso a la casa Lobreda en boca de todos. Nilo volvió a Greda Alta antes del invierno. Sigue ayudando a todo el mundo, pero ahora desde lejos.
- si no: Nilo siguió prometiendo antes de que nadie terminara de pedir. Casi siempre cumplió. Casi.

### saul
- si `union(saul, dario)`: Saúl se quedó en Valcenda. El ejército recibió una carta muy correcta y muy breve. En el despacho de los Veyra hay ahora dos pares de guantes sobre la mesa, y ninguno se usa.
- si `union(saul, isolda)`: Saúl e Isolda se casaron por los convoyes y se quieren como socios. Su casa tiene una puerta que siempre se puede cerrar, y la usan los dos.
- si `union(saul, celia)`: Saúl cumplió con el paso de Greda y con su casa. Es un marido correcto, puntual y leal. Algunas mañanas, en el picadero, se queda mucho rato mirando a ninguna parte.
- si no: Saúl volvió a Tiria después del Gran Baile, como mandaba la orden. Escribe cartas a Valcenda que nunca dicen nada y que alguien guarda en un cajón.

### dario
- si `union(saul, dario) o union(dario, celia)`: Dario dejó que alguien lo conociera, y no se murió de miedo. Sigue tropezando con talento, pero ya sólo cuando quiere.
- si `marca(dario_sin_mascara) o marca(dario_guarda_secreto_isolda)`: Dario no se casó esta temporada. Se plantó ante su tía y aplazó la herencia un año más. Dice que es lo más valiente que ha hecho, y que le temblaban las rodillas.
- si no: Dario heredó la casa Miravés sin quererla. Su carruaje sigue con las cortinas echadas. Ahora es él quien no las abre.

### teo
- si `union(teo, celia) o union(teo, irene)`: Teo se casó con alguien que se ríe con él y no de él. Los molinos siguen en apuros. El cuaderno de versos ya va por el tercer tomo.
- si `union(teo, camila)`: Teo y Camila se casaron por las cuentas y se hacen reír cada mañana. Los molinos Rovena pagan los jornales a tiempo. Teo dice que es el matrimonio más divertido de Valcenda, y nadie le lleva la contraria.
- si `marca(teo_conversacion_seria) o marca(teo_sin_chiste)`: Teo no se casó esta temporada. Pero dijo algo sincero una vez, delante de alguien, y desde entonces no ha podido volver a ser sólo un bufón.
- si no: Teo es el invitado más solicitado de Valcenda. Lo llaman para que haga reír. Nadie lo llama para otra cosa.

### celia
- si `union(teo, celia) o union(dario, celia)`: Celia baila por gusto. A veces se equivoca en el tercer giro y se ríe antes que nadie. Ha quemado la lista.
- si `union(saul, celia)`: Celia se casó por el paso de Greda. Es la dama más admirada de Valcenda. Sigue contando los pasos, en voz muy baja.
- si `marca(celia_rechaza_paso)`: Celia no se casó. Rechazó un compromiso que todo el mundo daba por hecho y abrió una academia de baile en la Puerta de Greda. Sus alumnas no cuentan los pasos.
- si no: Celia sigue siendo perfecta. Un error en público, una tarde de invierno, estuvo a punto de romperla. Se levantó sola, pero no ha vuelto a bailar.

### irene
- si `union(irene, isolda) o union(teo, irene)`: Irene se arriesgó a ser vista, y alguien la vio entera. Trabaja de día en el Archivo y de noche, ahora, sólo duerme.
- si `marca(irene_descubierta) y marca(nombres_protegidos_final)`: Irene publicó los abusos y calló a quien sólo se escondía. La reina la nombró guardiana de los folios recuperados. Mara Calce le ofrece trabajo cada semana. Ella dice que no, cada semana, con mucha educación.
- si `marca(irene_descubierta)`: Irene firmó la última Hoja con sus iniciales. Lo publicó todo. Ganó la verdad y perdió a dos amigos. No sabe todavía si el trato fue justo.
- si no: Nadie sabe quién escribió la Hoja sin Firma. En el Archivo, una archivera de letra pequeña y muy ordenada sigue trabajando de noche.

### isolda
- si `union(irene, isolda)`: Isolda dijo en voz alta lo que quería, delante de toda la corte. Ahora habla primero casi siempre. Cuando no, Irene espera.
- si `union(saul, isolda) y marca(isolda_hablo_primero)`: Isolda se casó con Saúl por los convoyes y con los ojos abiertos. Detrás de su puerta hay alguien a quien quiere, y ese alguien lo sabe.
- si `union(saul, isolda)`: Isolda se casó con Saúl por los convoyes. Es una buena alianza y un buen marido. Lo que quería de verdad no se lo dijo nunca a nadie.
- si no: Isolda volvió a Puerto Nácar sin casarse. Habla poco, y cuando habla, todos se callan para oírla. Aún no ha dicho lo que más quería decir.

### camila
- si `union(nilo, camila)`: Camila se dejó sorprender. Por un caballero de sombrero horrible, dos veces en el mismo camino. Dice que a la tercera ya no cuenta como casualidad.
- si `union(teo, camila)`: Camila se casó con Teo por las cuentas y descubrió que reírse por las mañanas también es una forma de querer.
- si `marca(deuda_saldada)`: Camila no se casó. Pagó sus deudas, devolvió el catalejo al mar y se fue a vivir sola a la costa. Dice que nunca ha estado mejor. Esta vez es verdad.
- si no: Camila sigue en Valcenda, observándolo todo con su copa en la mano. Es la mejor carabina de la ciudad. Por las noches, echa de menos que la sorprendan.

## Epílogo del misterio

- si `marca(irene_descubierta) y marca(nombres_protegidos_final)`: La verdad del incendio salió a la luz, y quienes sólo se escondían siguieron a salvo. Valcenda aprendió que se puede decir la verdad sin hacer daño. Le costó ochenta años.
- si `marca(irene_descubierta)`: La verdad del incendio salió a la luz entera, con todos sus nombres. Hubo justicia y hubo daño. En Greda Alta, una casa cerró sus postigos para siempre.
- si `nivel(irene, isolda) >= A o nivel(irene, teo) >= A`: Nadie supo quién escribía la Hoja. Pero la última no nombró a quien se escondía: alguien había convencido a su autora de que el silencio, a veces, también es justicia.
- si no: Nadie supo quién escribía la Hoja. La última lo publicó todo. Valcenda leyó, se escandalizó y, como siempre, nadie preguntó si era cierto.

## Epílogo de la casamentera

- si `rep >= 12`: La reina la nombró casamentera de la Corona. Le han dado un despacho en palacio, con vistas al río. Usted prefiere su residencia, y Bruna también.
- si `rep >= 4`: Su nombre se pronuncia con respeto en los salones. La temporada que viene, ya hay seis casas que le han escrito. Bruna dice que esta vez no le dejará aceptar más de ocho.
- si no: Valcenda la olvidará pronto. Ocho personas, no. Algunas le escriben todavía, en invierno, para contarle cómo les va.

## Confrontación en el Archivo

**Si `pistas >= 3 o nivel_max(irene) >= B`**
- **narración**: El Archivo está a oscuras salvo una lámpara. Irene espera junto al atril del libro de los sellos, con los manguitos de escribiente puestos.
- **irene**: Ha venido. Entonces ya lo sabe.
- **irene**: Sí. Soy yo. El sobre, las Hojas, la prensa de Arcos Bajos. Encontré los folios que las casas quemaron para cambiar quién era hijo de quién, y nadie quería leerlos.
- **irene**: Pero entre esos folios hay otros. Páginas del Pacto, con nombres de gente que sólo intentaba esconderse. Gente que aprecio. Mañana imprimo el último número, y todavía no sé qué nombres poner.
- **irene**: Alguien me dijo que publicara lo que se robó y callara a quien se escondía. Creo que tenía razón. Pero quería oírselo a usted.
- Opción **«Publique los abusos. Proteja los nombres.»** → Irene tacha una lista entera, despacio. Deja sólo los nombres de quienes robaron. «Gracias», dice. «Llevaba ochenta años esperando a que alguien me lo dijera.» Luego se ríe de sí misma: «Ochenta años no. Tres semanas.»
- Opción **«Publíquelo todo. La verdad no se elige.»** → Irene asiente sin mirarla. «Eso pensaba yo. Ojalá me hubiera dicho otra cosa.» Apaga la lámpara.
- Opción **«Entrégueme los folios. Se los daré a la reina.»** → Irene duda mucho tiempo. Luego le da la caja. «Si la reina hace con esto lo que yo no me atreví, habrá valido la pena. Si no, nunca se lo perdonaré.»

**Si `no (pistas >= 3 o nivel_max(irene) >= B)`**
- **narración**: El Archivo está a oscuras. Sobre el atril del libro de los sellos hay un papel doblado, con letra pequeña y muy ordenada.
- **narración**: «Todavía no me ha encontrado. Quizá sea mejor así. Mañana sabrá lo que decidí.»
