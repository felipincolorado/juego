# Salverna — Documento integral de entrega del proyecto

**Corte documental: 13 de octubre de 2026.** Documento para una persona, estudio o IA que recibe el proyecto por primera vez. Incluye contenido de autoría y secretos: no es material para mostrar al jugador.

**Estado:** consolidación documental; no introduce lore, aprobaciones, balance, imágenes ni implementación. La última instrucción explícita del usuario prevalece sobre una fuente anterior. Este archivo es una fotografía fechada: para continuar producción deben consultarse también las fuentes enlazadas.

## Índice

1. [Lectura ejecutiva y estado real](#1-lectura-ejecutiva-y-estado-real)
2. [Autoridades, versiones y reglas de continuidad](#2-autoridades-versiones-y-reglas-de-continuidad)
3. [Juego de temporada social: experiencia y mecánicas](#3-juego-de-temporada-social-experiencia-y-mecánicas)
4. [Interfaz, flujo y animación](#4-interfaz-flujo-y-animación)
5. [Lore y mundo vigente](#5-lore-y-mundo-vigente)
6. [Personajes, relaciones y casos existentes](#6-personajes-relaciones-y-casos-existentes)
7. [Dirección de arte y aprobaciones](#7-dirección-de-arte-y-aprobaciones)
8. [Vestuario, cabello, maquillaje y actuación](#8-vestuario-cabello-maquillaje-y-actuación)
9. [Referentes e investigación](#9-referentes-e-investigación)
10. [Producción de recursos y composición](#10-producción-de-recursos-y-composición)
11. [Implementación y herramientas](#11-implementación-y-herramientas)
12. [Pendientes y siguiente unidad de trabajo](#12-pendientes-y-siguiente-unidad-de-trabajo)
13. [Prompt de incorporación al proyecto](#13-prompt-de-incorporación-al-proyecto)
14. [Anexo A: prompts y sus autoridades](#anexo-a-prompts-y-sus-autoridades)
15. [Anexo B: reglas completas de autoría](#anexo-b-reglas-completas-de-autoría)
16. [Anexo C: mapa documental y procedencia](#anexo-c-mapa-documental-y-procedencia)

## 1. Lectura ejecutiva y estado real

Salverna es un mundo de fantasía adulta donde cortesía, dinero, apellido, deseo y registro público producen conflictos íntimos. La capital es Valcenda. La dirección artística busca ilustración artesanal, personajes adultos de identidad reconocible y vestuario estudiado, con una experiencia móvil vertical.

La dirección de juego más reciente es gestionar una temporada social como casamentera: leer invitaciones, reservar asistentes, seguir los compromisos en el mapa, intervenir ante novedades y conocer resultados públicos y privados. La estética social toma inspiración de Bridgerton, integrada en un mundo propio con condiciones y linajes fantásticos. El nombre comercial definitivo de esta nueva experiencia no está cerrado.

### Dos etapas que deben entenderse por separado

| Área | Qué existe | Qué no debe inferirse |
|---|---|---|
| Prototipo judicial «Las actas de Salverna» | Proyecto Godot, seis casos bilingües, lógica y guardado, interfaz C16 documentada | No es el juego social implementado ni una publicación comercial |
| Mundo v0.3 | Geografía, casas, economía, instituciones, calendario y reglas fantásticas | No aprueba todos los argumentos, escenarios o vestuarios posteriores |
| Temporada social | Decisiones del usuario, análisis de referentes, auditoría y recorrido de maqueta | Fórmulas, rutas y campaña completa siguen sin implementación |
| Arte | Bases concretas aprobadas y muchas tandas de candidatos | Cantidad de archivos no equivale a cantidad de recursos aprobados |
| Figma social | Página, fundamentos y controles; flujo local y plugin preparados | No quedaron guardadas las 54 pantallas sociales remotas |
| Android | APK judicial anterior exportado y verificado documentalmente | No refleja necesariamente C16; no demuestra prueba en teléfono |

El elenco judicial existente no pasa automáticamente a ser el reparto de ocho pretendientes. No borrar el prototipo anterior ni atribuirle funciones románticas que no contiene.

### Lo que debe preservar quien recibe el proyecto

- El mapa es parte central de la fantasía de gestión.
- La planificación de la semana ocurre antes de su ejecución por fechas.
- Las personas pueden estar ocupadas varios días y tener objetivos propios.
- Éxito social, afinidad, deseo y consentimiento son cosas diferentes.
- La ilustración debe conservar identidad, dibujo y pintura; no basta un filtro de textura.
- El resultado visual debe sentirse videojuego y mundo de época. El usuario rechaza la lectura de aplicación de citas.
- Los textos jugables nuevos se escriben en español e inglés con claves estables.

## 2. Autoridades, versiones y reglas de continuidad

### Cómo interpretar los estados

**Instrucción del usuario:** requisito solicitado. **Base de trabajo:** contexto vigente para desarrollar. **Propuesta:** alternativa editorial o mecánica todavía abierta. **Producido:** existe un archivo. **Integrado:** aparece en la aplicación. **Comprobado:** se verificó un aspecto concreto. **Aprobado:** aprobación explícita del usuario para ese elemento. Ninguno implica automáticamente el siguiente.

La verdad de autor se separa del conocimiento de cada personaje, la información pública y el estado de una partida. No asumir pareja, soborno, culpabilidad o resolución a partir de una posibilidad de diseño.

### Orden de consulta

1. `AGENTS.md`, `memoria-salverna/LEER-PRIMERO.md` y `memoria-salverna/decisiones.md`.
2. `REGLAS-CENTRALES-SALVERNA.md` y `ESTANDAR-CALIDAD-SALVERNA.md`.
3. Mundo: `BIBLIA-MUNDO-SALVERNA-v0.3.md` y `memoria-salverna/mundo-v0.3.json`.
4. Personajes: entidades, perfiles de autoría y fuentes de cada escena.
5. Arte: referencia ORIGINAL aprobada y `produccion-arte/mundo-v03/referencias-y-bloqueos.json`, contrastados con las decisiones posteriores.
6. Juego judicial real: `salverna-game/data/cases.json`, ambos catálogos y `scripts/game_state.gd`.
7. Diseño social: auditoría de definición, continuidad posterior y los requisitos consolidados aquí.

### Contradicciones conocidas que no deben fusionarse

- El diseño social v1 es histórico en habilidades y exclusión semanal. Rigen los cinco atributos del usuario y las reservas por fecha.
- La biblia mundial incluye reglas de ritmo judicial. No se importan como calendario de la temporada social.
- Las descripciones antiguas que exigían ocultar toda fantasía quedaron sustituidas: lo fantástico existe públicamente, aunque una identidad individual sea secreta.
- Leonora B, C2 y t36 conservan historia; **t48 es la base visual actual aprobada**. Algunos textos aún mencionan C2 y «sin velo». No aplicarlos sobre t48.
- El manifiesto original de t48 conserva `candidate_review_pending` y su encargo `approval: false`: describían la entrega previa. La aprobación posterior está en decisiones, entidades, referencias-y-bloqueos y manifiesto t49.
- Las variantes t49 siguen pendientes. Aprobar la base no aprueba las expresiones.
- Las instrucciones de adjuntar varios originales ilustrados sirven para un diseño inicial; para cambiar expresión se adjunta exclusivamente el original aprobado de esa misma persona.
- Los inventarios históricos de 68 o 73 recursos son encargos/registros de versiones, no pruebas de que todas esas imágenes existan o estén aprobadas.

## 3. Juego de temporada social: experiencia y mecánicas

### Fantasía y papel del jugador

Organizar la participación de un elenco adulto en la temporada de Valcenda. Las invitaciones ofrecen situaciones con relato, exigencias sociales y oportunidades de vínculo. El jugador conoce a las personas y toma decisiones sobre a quién enviar y cómo responder ante un incidente.

La reina como patrocinadora, autoridad y guía de apertura procede de la idea del usuario. Su encargo concreto, condiciones y frecuencia de intervención necesitan guion. Reservar sus intervenciones para momentos significativos y usar ayuda contextual cotidiana es una propuesta de interfaz, no una biografía aprobada.

### Bucle principal vigente

1. Recibir las invitaciones de la semana sobre las locaciones del mapa.
2. Abrir cada ficha: situación breve, fecha, duración, asistentes, requisitos, riesgos y oportunidades.
3. Consultar la carta completa si se desea una lectura inmersiva.
4. Elegir asistentes y responder; comprobar conflictos con otras reservas.
5. Revisar agenda y comenzar la semana con las asignaciones preparadas.
6. Seguir fechas, viajes y eventos simultáneos; abrir novedades y resultados.
7. Resolver incidentes y, cuando corresponda, reemplazos excepcionales.
8. Cerrar la semana: consecuencias conocidas, reputación y continuidad narrativa.

No volver a asignar libremente todo el elenco cada mañana durante la ejecución. Las modificaciones ante inconvenientes son excepciones del plan ya enviado.

### Atributos elegidos por el usuario

| Español | Inglés de trabajo | Función y distinción |
|---|---|---|
| Baile | Dance | Desenvolverse en situaciones de baile; sus pruebas concretas requieren autoría |
| Estatus | Standing | Movilizar respaldo y acceso social; no confundir con título biográfico ni reputación del jugador |
| Chisme | Gossip | Manejar información y maniobrar ante una situación; no inventa conocimiento ni convierte rumor en prueba |
| Presencia | Presence | Sostener atención, impresionar y conducir un intercambio mediante actitud y encanto |
| Intelecto | Intellect | Comprender, argumentar y resolver exigencias intelectuales |

Son cinco ejes: corresponde un **pentágono**. Escala 0–5 y valores iniciales son propuestas, no balance cerrado. Faltan agregación por equipo, normalización por asistentes, fórmula de probabilidad, límites, azar y relación entre prueba inicial e incidente.

El gráfico debe ayudar a comparar capacidad y requisitos. La animación de una esfera puede representar la resolución. Recomendación técnica: calcular una vez, guardar el resultado y animarlo después; no decidir el premio de nuevo por cada rebote ni al reabrir la pantalla.

### Agenda, simultaneidad y duración

- Dos actividades coincidentes impiden enviar a la misma persona; fechas suficientemente separadas pueden permitirlo.
- Existen actividades de varios días, con desplazamiento incluido cuando el diseño lo requiera.
- Dos eventos del mismo día avanzan simultáneamente en el mapa.
- Una actividad larga continúa mientras otra comienza o termina; puede atravesar el cierre semanal.
- La unidad exacta de conflicto —día completo o franjas— y la disponibilidad al regresar aún deben cerrarse. Reservar de salida a retorno es la recomendación de diseño, no una regla implementada.
- Una clase sólo sacrifica otra oportunidad si sus fechas realmente compiten.

### Incidentes, incapacidad y sustitución

La sorpresa puede ocurrir durante un evento o manifestarse cuando llega una reserva posterior. Ejemplo de funcionamiento, no escena canónica: alguien queda indispuesto y, al llegar su siguiente actividad, se ofrece enviar un reemplazo disponible.

La interfaz debe explicar la causa y ofrecer las salidas que permita ese evento: sustitución, asistencia reducida o retirada con consecuencia escrita. Los eventos centrales necesitan continuidad incluso si no existe sustituto. No hacer viajar al personaje y después afirmar que nunca pudo asistir.

Vergüenza e incapacidad son estados distintos. El retrato avergonzado es una intención visual; duración, penalización y acumulación están pendientes. La vergüenza no debería convertirse automáticamente en una prohibición de asistir.

### Clases y progresión individual

El usuario solicita clases como eventos programados por autoría: baile de salón, protocolo u otras actividades pertinentes. No un catálogo permanente donde elegir cualquier entrenamiento. La frecuencia semana por medio fue planteada como posibilidad. Atributo mejorado, coste, cupo, cantidad y límite requieren balance.

### Vínculos y rutas

El reparto social previsto es de ocho adultos: una mujer homosexual, un hombre homosexual, una mujer bisexual, un hombre bisexual y cuatro heterosexuales —dos mujeres y dos hombres—. Son requisitos de reparto, sin asignación aprobada a los personajes judiciales.

La orientación no se muestra como etiqueta de ficha. Se descubre mediante señales, confidencias y conductas escritas. La sorpresa necesita pistas legibles; no debe depender de ocultar toda información hasta castigar al jugador.

Separar cercanía, interés direccional, compromiso y resultado público. Hay posibilidades de amistad, atracción unilateral, romance, conveniencia, incompatibilidad e infelicidad. El matrimonio lavanda entre el hombre gay y la mujer lesbiana es una posibilidad solicitada: necesita acuerdo consciente y objetivos compatibles, no una conversión por puntuación.

Ocho personas producen 28 pares únicos, pero no implican 28 rutas románticas completas. No prometer escenas para cada combinación ni usar una tirada de habilidad para imponer deseo o contacto.

**Tensión de lore pendiente:** el mundo v0.3 permite uniones de cualquier género y no criminaliza automáticamente una orientación. Las rutas de armario y conveniencia deben justificar sus presiones concretas —familia, promesas, herencia o imagen— o registrar una revisión deliberada del mundo. No introducir una prohibición universal silenciosamente.

### Reputación, semanas y final

La evaluación semanal debe reflejar hechos que la sociedad puede conocer. Una relación secreta no genera reputación pública sin transmisión de información. Fórmula, escalones, recompensas y condiciones de éxito siguen pendientes.

Organizar un encuentro a medida gracias a reputación es una propuesta interesante, no una función aprobada o implementada. La reputación no fuerza voluntad.

La Temporada del Sello dura seis semanas en la biblia de mundo. La distribución jugable exacta, arco del encargo y final requieren guion. El gran baile se contempla como culminación; no está acordado que todos deban casarse ni que una tirada final anule toda la temporada.

### Contenido central, opcional y minijuego

El usuario quiere invitaciones obligatorias con continuidad de historia y otras opcionales. Participación obligatoria no significa victoria garantizada ni matrimonio forzoso.

Se propuso un memorice de cartas con una adivina, dificultad creciente y pistas de la semana siguiente. Falta definir intentos, progresión, fiabilidad y límites de conocimiento. Recomendación: opcional, sin reloj, sin bloquear información central ni revelar automáticamente orientaciones. Aún no implementado.

## 4. Interfaz, flujo y animación

### Dirección visual de interfaz

El usuario rechaza que la propuesta parezca una app de citas. La referencia de Dispatch demuestra composición por tarea, personajes expresivos, estados y contexto del mundo. La adaptación propuesta es un despacho de temporada: álbum, cartas, agenda, sellos y mapa, con controles reconocibles y tipografía legible.

Evitar construir toda pantalla con la misma tarjeta de perfil, repetir corazones de compatibilidad o usar gestos de aprobar/rechazar personas como centro de la experiencia. Tampoco copiar el terminal CRT o la estética militar de Dispatch.

### Pantallas y conexiones

| Pantalla | Contenido principal | Acción y retorno |
|---|---|---|
| Portada | Imagen que presenta el mundo y título | Nueva partida/continuar; ajustes accesibles |
| Apertura | Inicio de temporada, proclamación y encargo | Tutorial progresivo hacia el despacho |
| Despacho | Álbum, agenda, correspondencia y ciudad | Accesos directos; evitar pasos repetidos de ida y vuelta |
| Ciudad | Locaciones, invitaciones, fecha y actividad | Abrir evento; alternar planificación y ejecución |
| Ficha de invitación | Resumen, requisitos, duración y cupo | Carta completa o asignación |
| Carta | Documento inmersivo con relato completo | Volver a ficha conservando selección |
| Asignación | Pentágono, asistentes y retratos inferiores | Consultar persona, cambiar selección y confirmar respuesta |
| Agenda | Reservas y conflictos | Volver al evento afectado; comenzar semana |
| Incidente | Situación, participantes y respuestas | Resolver y reanudar progreso |
| Resultado | Desenlace, reacción y efectos causales | Reconocer resultado y volver al mapa |
| Elenco/ficha | Identidad, atributos y confidencias conocidas | Volver al contexto de origen |
| Cierre semanal | Balance público y privado distinguido | Recompensas y nueva semana |

Navegación Ciudad/Elenco/Calendario es una propuesta de estructura. Durante una decisión, los controles de esa tarea pueden reemplazar la barra inferior. No perpetuar navegación de aplicación por obligación visual.

### Lectura móvil

- Reducir simultaneidad de paneles, no encoger la composición de escritorio.
- Asignación: requisitos y comparación visibles; retratos horizontales compactos, sin deformar caras.
- Incidente: dos o tres opciones legibles y pulsables; no esconder respuestas bajo desplazamiento.
- Carta y biografía sí pueden tener desplazamiento para lectura extensa.
- Cursiva ornamental en títulos, firma y acentos; texto de decisión de lectura rápida.
- Iconos y texto acompañan colores de estado. Usar áreas táctiles cómodas y revisar el montaje en teléfono.

### Animaciones solicitadas y funcionamiento propuesto

| Elemento | Comportamiento |
|---|---|
| Retratos viajeros | Siguen rutas trazadas en el mapa; salidas simultáneas cuando coinciden fechas |
| Fecha | Cambia durante la ejecución; permite entender cuándo ocurre cada actividad |
| Aro amarillo | Progreso del evento alrededor del marcador de locación |
| Aro rojo y exclamación | Novedad que requiere atención; no equivale siempre a fracaso |
| Pausa | Se detiene el avance global mientras el jugador resuelve una decisión |
| Aro completo y resultado | Evento terminado; abrir y reconocer el desenlace |
| Evento largo | Mantiene participantes y progreso mientras continúan otras fechas |
| Retratos y cifras | Reacción pertinente y transición de cambios, sin otorgar otra vez los premios |

Duración narrativa y duración real de animación son distintas. No exigir esperas equivalentes a días. Velocidad, salto y movimiento reducido son recomendaciones a implementar. Día/noche del mapa es opcional; el calendario basta si la iluminación complica la lectura o la producción.

## 5. Lore y mundo vigente

Se reproduce a continuación la parte española de la biblia v0.3 como base de mundo. **Las menciones al juez y al ritmo de audiencias pertenecen al prototipo judicial**; no sustituyen el bucle social descrito arriba. Es base de trabajo, no aprobación de todas las escenas derivadas.

### world.identity — Identidad / Identity


Salverna es una monarquía mercantil de fantasía adulta: el título abre puertas, el crédito permite mantenerlas abiertas y el registro decide quién puede reclamar lo que hay detrás. Cortesía, deseo, necesidad y lealtad pueden enfrentar a personas que se quieren. El juez convierte una interpretación respaldada por pruebas en una versión oficial que tendrá beneficiarios y perjudicados.

Tomamos de nuestros referentes la función de las alianzas íntimas y del poder territorial, sin copiar sus familias, símbolos o acontecimientos. La identidad propia es la disputa por controlar el registro: conservar un nombre, ocultar un origen, reclamar una herencia o impedir que una injusticia desaparezca del archivo. No todos los conflictos desembocan en conspiración real.


### world.geography — País y agua / Land and water


Reino del hemisferio norte de unos 540 km de oeste a este y 610 de norte a sur. El mar de Nácar bordea oeste y suroeste. Greda forma el arco montañoso norte; Tiria, las mesetas orientales. La Vega es la cuenca central cultivada. Serel abarca el curso bajo y las marismas suroccidentales; Valcenda está al sureste de la Vega, sobre terrazas fluviales firmes.

El río Lumbre nace en Greda, pasa por Lumbrevía, alcanza Valcenda y gira al suroeste hacia el estuario de Serel. Afluentes orientales drenan Tiria. Los rápidos aguas arriba de Lumbrevía impiden navegar directamente hasta Greda: allí se transbordan cargas a carros y animales. Barcazas circulan por el tramo bajo.

El Canal de Serel es una derivación corta y regulada junto al barrio mercante de Valcenda. Su nombre procede del comercio, no del nacimiento del agua. Serel distingue marismas costeras salobres, vegas dulces y diques habitados. Las crecidas afectan parcelas y caminos determinados, no toda la capital automáticamente.

Distancias de camino para continuidad: Greda Alta–Lumbrevía 180 km; Puerto Nácar–Lumbrevía 220; Lumbrevía–Valcenda 200; Tiria–Valcenda 240; Serel–Valcenda 120. Una caravana ordinaria se planifica a 20–30 km diarios con buen tiempo; son convenciones internas aproximadas. Correos con relevos cuestan más; nieve, tormentas y crecidas retrasan. Las noticias distantes no llegan instantáneamente. El mapa es esquemático, no una carta de navegación.


### world.calendar — Clima y estaciones / Climate and seasons


La influencia marítima llega de oeste y suroeste. Las laderas expuestas de Greda reciben lluvia y nieve; valles interiores quedan más resguardados. Altitud, exposición y distancia al mar importan. Tiria tiene mayor contraste entre invierno y verano que la costa, sin ser un desierto. Serel es húmedo por relieve y agua, no tropical por estar al sur.

Calendario civil de doce meses, cuatro estaciones y semanas de siete días. Primavera: crecidas y siembra. Verano: cosechas tempranas y salinas. Otoño: principales cobros, cosecha tardía y temporada social. Invierno: pasos cerrados, almacenes y combustible. Comenzamos en el primer otoño: mañanas frescas, tardes templadas y lluvias intermitentes. Capas exteriores se retiran dentro salvo necesidad o costumbre individual.

Cada caso ocupa un día de juego. La Gaceta cierra tres o cuatro audiencias de la semana; no hay que simular cada día restante. La noche cambia luz, vidrio y sonido en la misma arquitectura. No se deforma la sala ni se tiñe toda piel de amarillo.


### world.cities — Ciudades y dependencias / Cities and dependencies


**Valcenda:** capital administrativa y cruce fluvial. Pozos de terraza y tomas controladas abastecen agua; Vega aporta alimentos, Greda madera y lana, Serel sal y productos de ribera, Nácar importaciones. Patios de servicio y recogida municipal retiran residuos de forma desigual. Palacio y Archivo dependen de proveedores, criados y crédito. Su debilidad es el abastecimiento y el control burocrático del acceso.

**Lumbrevía:** mercado de grano y transbordo bajo los rápidos. Molinos, talleres de lino y almacenes compiten por agua. Rovena controla molinos y propiedades concretas, no toda la Vega. Serravalle posee un conjunto distinto de villas y tierras. Los dos títulos no crean soberanías superpuestas sobre la misma región. Caudal, peajes y adelantos de cosecha sostienen sus conflictos.

**Greda Alta:** ciudad de almacenes, feria de lana y custodia de pasos, bajo las cumbres. Manantiales y cisternas, cereal parcialmente importado, cubiertas inclinadas y entradas protegidas. Hay arrieros, comerciantes y hogares civiles, no sólo un castillo. Lobreda cobra paso y debe mantener caminos y socorro. Crédito y comida limitan su independencia.

**Puerto Nácar:** puerto con calles altas residenciales, almacenes junto a muelles y patios resguardados. Manantiales y cisternas; pesca, huertas y comercio. Miravés domina crédito y parte de los fletes, no todos los barcos. Navegantes, aseguradores y trabajadores tienen intereses propios. Una tormenta puede arruinar una garantía sin fraude.

**Tiria:** ciudad de guarnición y mercado en la meseta, abastecida por cisternas y un afluente del Lumbre. Familias de servicio, pensiones y talleres tienen vida civil. Al este está la Liga de Orsena, confederación de villas con la que hay tregua. Un corredor de pastoreo y aduana al nordeste sigue disputado; Veyra busca derechos documentados, comerciantes de ambos lados necesitan paso. Orsena es contexto exterior, no otra campaña a producir ahora.

**Serel:** ciudad sobre diques y elevaciones naturales del curso bajo. Barcas, terraplenes y pasarelas conviven; no todo edificio es palafito. Salinas costeras evaporan en meses secos y almacenan para invierno. Huertas dulces quedan separadas de balsas salobres. Boticas, cestería, transporte y conservación de alimentos son oficios importantes, no exclusivos. Abrir compuertas beneficia unas parcelas y perjudica otras.


### world.valcenda — La capital y su sala / The capital and its court


Valcenda creció alrededor de un puente y depósitos reales sobre una terraza segura. Arcos Bajos ocupa las calles bajo los soportales de un antiguo mercado de grano: sus arcos sostienen viviendas y dependencias superiores. No son una cripta. Trabajo, alquileres y contratos atraen a población mezclada.

El juzgado ocupa una antigua sala de pesaje cedida al distrito. Identidad: sala longitudinal sobria, arco de carga bajo al fondo, cal clara, carpintería oscura reparable y ventanas altas laterales para leer sin mojar papeles. Reformas visibles, no ruina. El orden y los materiales expresan autoridad. El mobiliario permanece en capas independientes según el contrato vigente. Esta definición exige una nueva planta y cámara coherentes, no aprueba un fondo existente.

Calle de los Sellos reúne escribanos, archivo e imprenta; Canal de Serel, muelles y almacenes; Puerta de Greda, lana y alojamientos de arrieros; Patio de Tiria, cuarteles y oficios de servicio; Alto Laurel, residencias y palacio. Son concentraciones, no barrios étnicamente cerrados. Los niveles altos reducen exposición a crecidas, pero no toda pobreza vive en la cota más baja.


### world.material — Materiales y tecnología / Materials and technology


Sociedad preindustrial de imprenta, vela, vidrio, óptica artesanal y relojes mecánicos costosos. Hay pólvora en arsenales, sin armar a todo civil ni exigir combate jugable. No hay fotografía, telecomunicación ni confección industrial. Copiar necesita personas, tiempo y material; los errores de copia son posibles, no universales.

Greda produce lana y madera; Vega lino y alimentos; Serel sal y fibras de cestería. Nácar importa algodón y seda de mercados exteriores. Vega puede tejer algodón importado sin cultivarlo. Tinte, tejido, ajuste y conservación cuestan por separado. Color no equivale a riqueza; un negro profundo uniforme puede costar más que un negro rehecho o desteñido.


### world.dress — Vestuario y clase / Dress and class


Greda conserva lana y cierres tejidos; Nácar pañuelos y chaquetas adaptadas al viento; Vega mangas sustituibles y delantales; Tiria corte recto y señales de servicio; Serel chales lavables, bolsillos y prendas fáciles de secar. Son tradiciones, no uniformes. Cada vestuario responde a material, adquisición, ocasión, clima y elección personal. Herencia, segunda mano, reparación y préstamo explican diferencias. Las bases aprobadas no cambian sólo para obedecer una descripción regional nueva.

Título, cargo, patrimonio, ingreso, deuda y protección son variables distintas. Un noble sin dinero conserva acceso; una comerciante rica puede carecer de cargo; un criado conoce secretos sin poder faltar al trabajo. Gremios protegen aprendizaje y calidad, pero también excluyen. La vecindad se organiza y testifica; no es una masa pasiva.

La petición al mediador es gratuita. Copias certificadas, representación y apelaciones pueden costar, con exención registrada por falta de medios. Comparecer puede consumir un jornal o comprometer vivienda y empleo. La igualdad del testimonio en la ley no elimina desigualdad para obtener pruebas. Estos costes se escriben cuando importan al caso, no se cobran automáticamente en el prototipo.

Cualquier género hereda, trabaja y puede registrar unión, patrimonio y tutela. La adopción conserva derechos sucesorios. El escándalo nace de consentimiento, promesa, dependencia, clase y sucesión, no de criminalizar automáticamente una orientación. Artistas, acompañantes y cortesanas tienen propiedad, voz y vínculos propios.


### world.history — Historia y conflicto presente / History and present conflict


Año narrativo 80 después de la Noche del Censo. El incendio ocurrió hace ochenta años; la Carta de los Sellos se promulgó un año después para estabilizar títulos y sucesiones. La reforma reciente de la reina Maela Aurenza exige copias accesibles y revisión de sentencias distritales; comenzó a aplicarse en Arcos Bajos hace tres meses. No supone que Maela lleve ochenta años reinando: su edad y duración del reinado no se fijan aquí.

La justicia depende de quienes debe juzgar. Ordenar registros ofrece protección y amplía el control de la Corona. Casas y gremios apoyan o resisten según el asunto; no hay facción universalmente correcta. Tregua de Orsena, cobros de otoño y provisiones de invierno crean presión contemporánea sin una guerra nueva cada semana.

Verdad de autor: el archivo incendiado contenía el Pacto del Umbral, que protegía identidades y pactos sobrenaturales. Personas de varias casas aprovecharon pérdidas documentales para alterar parentescos y propiedades; no se fija aquí un culpable único del incendio. Conocimiento público: la versión oficial lo llama accidente, y hay rumores incompatibles. No todos los personajes conocen el Pacto ni sus beneficiarios.


### world.justice — Instituciones y competencias / Institutions and jurisdiction


El Archivo Real acredita nombramientos; tesorería paga al juez; cabildo mantiene sala y personal local; alguaciles ejecutan órdenes; visitaduría real investiga faltas. Escribano registra y Gaceta interpreta: ninguno sustituye el fallo. Una casa puede retirar crédito, presionar a un funcionario o denunciar; no reducir mágicamente el sueldo. Toda sanción salarial requiere procedimiento identificable.

Mediador: deuda, conciliación y restituciones menores, nunca muerte ni confiscación de títulos. Juez de Distrito: bienes, tutelas y delitos locales, con apelación. Magistrado Provincial: conflictos entre jurisdicciones y casas menores. Juez de la Corona: títulos y alta justicia por delegación real. Las condenas irreversibles requieren expediente de alta justicia y revisión, no una opción sorpresa en una deuda vecinal. Cinco grados por cargo; la competencia cambia al ascender de cargo, no por cada grado.

Aceptar soborno es falta incluso con un fallo defendible. Puede dejar testigo, carta, dinero o compromiso; no se descubre automáticamente ni genera conocimiento en toda la ciudad. Hechos, acta pública y exposición de corrupción son estados distintos. Estas reglas no sustituyen el balance ejecutable de seis casos.


### world.houses — Casas y dependencias / Houses and dependencies


Aurenza: Corona, Archivo, aduanas y rentas reales; necesita crédito, comida y cooperación militar. Centraliza tanto para gobernar como para proteger. Lobreda: lana, madera y pasos; debe mantenimiento y socorro, depende de cereal y crédito Miravés. Su disputa de paso con Veyra es interior, distinta del corredor exterior de Orsena.

Veyra: concesiones y administración militar, dependiente de pagos y suministro; defender territorio puede proteger hogares y rentas propias. Miravés: crédito y navíos, dependiente de confianza y cobros; la longevidad de su rama nocturna aporta continuidad y riesgo documental. Serravalle: villas y jardines, rentas y alianzas, más prestigio que liquidez; matrimonio con Rovena no fusiona patrimonios. Rovena: molinos y alquileres, dependiente de agua, mantenimiento y arrendatarios; edificios vacíos no garantizan ingresos.

Cada casa tiene desacuerdos internos. Un miembro no es portavoz automático. Calce no es casa titulada: necesita papel, encargos, lectores y credibilidad. Mara puede influir sin controlar la verdad. Los dos motivos de vestuario o heráldica compartidos por una casa no son genética ni aprobación de un escudo dibujado.


### world.fantasy — Pueblos y condiciones / Peoples and conditions


Lo fantástico existe públicamente. Su historia y alcance se discuten. El Pacto del Umbral protegía identidades, filiaciones y acuerdos concretos, no exigía incredulidad universal. Esta regla sustituye la ocultación absoluta anterior. Saber que existen nocturnos no revela qué persona lleva tres identidades ni de dónde obtiene sangre. Apariencia y condición nunca bastan para acreditar un delito.

Humanos: mayoría diversa en piel, origen, facciones y cultura. Velarios: linaje humanoide público y minoritario, asentado hace generaciones en varias regiones, especialmente Nácar y Valcenda. Cabello verde pizarra, franja perla frontal e iris cobre apagado son rasgos frecuentes; no imponen piel, mandíbula, edad, clase o belleza. Ascendencias mezcladas pueden heredar parte de ellos. Ciclo vital comparable al humano, sin poderes innatos exclusivos. Cierres laterales y cuello en V son una tradición portuaria que otros también usan. Ninguno de los ocho personajes existentes se convierte en velario.

Lunario: condición heredada o adquirida tras mordedura de una persona transformada; no toda mordedura la transmite. La transformación es involuntaria en la noche de plenilunio, incluso bajo techo, con forma de lobo grande pero físicamente vulnerable. Termina antes del amanecer, causa agotamiento y memoria fragmentaria. Fuera de esa noche no hay cambio a voluntad. Cada caso fija fecha lunar, transmisión y hechos en la verdad de autor; no se resuelven con azar después de oír al jugador. Un recuerdo incompleto no demuestra inocencia ni responsabilidad. Nilo conserva su secreto.

Nocturno: condición adquirida mediante intercambio deliberado de sangre y supervivencia a una crisis, no por mordedura aislada. Casi detiene el envejecimiento adulto; no resucita ni vuelve invulnerable. Necesita sangre al menos una vez por semana en condiciones ordinarias; privación causa debilidad y después pérdida de control, no absolución automática. Sol directo sostenido debilita y lesiona; vela no. No hay lectura mental ni consentimiento impuesto mágicamente. Colmillos y cambios individuales de palidez pueden ser reconocibles, sin exigir la misma piel o rostro a todos.

Donación adulta requiere consentimiento y condiciones pactadas; coacción, lesión y tráfico se juzgan como hechos. La longevidad no extingue deudas ni entrega títulos: supervivencia y continuidad de identidad deben probarse. La rama Miravés puede ocultar identidades y acuerdos aunque el fenómeno sea conocido. La campaña inicial no acumula condición lunar y nocturna en una persona; no produce híbridos ni reglas improvisadas.

Hilandera es una práctica aprendida, abierta a géneros y linajes distintos. Requiere contacto presencial, un objeto ligado al episodio y un recuerdo de los siete días anteriores. Sólo afecta a un episodio; no fabrica biografías ni modifica tinta, papel u otros testigos a distancia. Cambia experiencia, no hechos materiales. La persona que opera pierde un recuerdo propio de importancia comparable, fijado por autoría. Queda un nudo físico adicional en el objeto; como hay nudos ordinarios, eso sólo permite investigar intervención, no identificar autor o mentira. Todo caso mágico ofrece corroboración material independiente. Bruna no se convierte automáticamente en practicante.

Ninguna capacidad adicional se introduce para solucionar retrospectivamente un caso. Los personajes pueden desconocer estas reglas, equivocarse o mentir sobre ellas; el guion debe distinguirlo del conocimiento del autor.


### world.customs — Creencias y calendario social / Belief and social calendar


Las Casas de la Vigilia son asociaciones religiosas y de asistencia, distintas de casas nobles. Conservan nombres de difuntos y acompañan a familias; sus miembros discrepan sobre lo sobrenatural. No tienen monopolio judicial de matrimonio o tutela. Hay devociones domésticas y no creyentes. Recordar, prometer y decidir quién merece duelo atraviesa toda la sociedad.

La Temporada del Sello dura seis semanas del primer otoño: ferias, peticiones, visitas y alianzas antes de que empeoren los caminos. No todos participan en bailes nobles. Mesa de Invierno de Greda compromete provisiones ante testigos; Cierre de Cuentas de Nácar precede tormentas; Noche de los Faroles conmemora incendio y nombres perdidos, con duelo, fiesta y protesta.

Hilo de Luto: cinta oscura voluntaria con inicial o nombre; reutilizar vestido y cinta no disminuye dolor. Nudos de Recuerdo de Serel conservan memoria familiar, sin acreditar magia. Juramento de Puerta de Tiria entrega una llave ceremonial al dejar servicio, sin transferir propiedades. Primera Campanada registra orden de peticiones; el martillo del jugador abre la audiencia. No duplicar ambos como botones sin funciones diferentes.


### world.continuity — Límites de esta revisión / Revision boundaries


Conservar nombres, oficios, vínculos y referencias aprobadas de Leonora, Mireya, Mara, Nilo, Saúl, Bruna, Inés e Ivo. La viuda vampírica de siete maridos sigue como revisión individual pendiente: no mezclarla con Vera ni atribuir asesinatos sin verdad de autor. Este límite conserva continuidad sin restaurar el secreto universal anterior.

La descripción de sala fija función y materiales, no imágenes aprobadas. Patrones y emblemas necesitan diseño propio; técnica artesanal, contornos por material, variedad anatómica y ausencia de filtro amarillo siguen obligatorios. Antes de prompts, cada ficha recupera clima, recursos, ocasión e identidad individual.

Nada de aquí implementa calendario, poderes, tarifas, rutas, veinte grados o nuevas sanciones en Godot. Los seis casos conservan sus autoridades ejecutables. Una adaptación registra cambios y revisa pruebas EN/ES. El mapa nuevo es documento de continuidad, no arte final ni seis escenarios jugables. Fechas individuales, culpable del incendio y detalles ajenos al primer arco no se rellenan por obligación.


### world.references — Referencias y alcance / References and scope


La auditoría previa conserva fuentes reales: Porto/UNESCO para relación entre puerto, relieve y tejido urbano; Met Office para exposición, relieve y precipitación; V&A para recursos, tejidos y comercio. Son mecanismos de referencia, no pruebas de hechos ficticios ni permiso para copiar culturas. No se afirma que esta biblia alcance automáticamente la calidad literaria o el éxito de nuestros referentes. Debe demostrarse en escenas, personajes y montaje.


### world.atmosphere — Cómo se siente vivir aquí / What living here feels like


Valcenda: al amanecer, los proveedores del palacio y quienes esperan audiencia cruzan el mismo puente. Unos llevan el desayuno de los poderosos; otros, un papel del que depende conservar su habitación. Al anochecer, los salones repiten nombres que en el juzgado sólo se pronunciaron en voz baja.

Greda Alta: una mesa puede parecer generosa hasta saber que cada plato se descuenta de las provisiones del invierno. La hospitalidad es un orgullo real, y también una obligación que alguien tendrá que pagar.

Puerto Nácar: en los salones nadie pregunta cuánto vale una persona; preguntan quién responde por ella. Abajo, una tripulación espera el salario de un barco cuyo cargamento ya se vendió tres veces sobre el papel.

Lumbrevía: cuando un molino trabaja de noche, sus vecinos oyen prosperidad o abuso según de quién sea el agua que falta al amanecer. El apellido del dueño aparece en el contrato; las manos que reparan la rueda, casi nunca.

Tiria: al retirar el uniforme queda la marca del cuello en la piel. El servicio termina en una ceremonia; la deuda por botas, la pensión discutida y una promesa hecha al otro lado de la frontera no siempre terminan con él.

Serel: una compuerta se abre y la corriente cambia de dueño. La misma familia puede agradecer el drenaje del patio y perder la huerta; de noche, los nudos recuerdan nombres que ningún escribano llegó a registrar.

Estas viñetas fijan tono y tensiones colectivas. No afirman sucesos de una partida, culpabilidad de una casa o nuevas biografías del elenco.



## 6. Personajes, relaciones y casos existentes

Este es el elenco documentado del prototipo judicial. Las motivaciones siguientes conservan su condición de propuestas editoriales derivadas de la biblia. No les asignan orientación ni papel romántico. Las imágenes aprobadas prevalecen sobre descripciones físicas anteriores.

### Leonora Serravalle — `char_leonora`


- **Deseo:** Conservar margen sobre la casa familiar

- **Temor:** Quedar reducida a un apellido sin bienes

- **Contradicción:** Protege a Vera y decide por otras personas

- **Estrategia:** Redirige preguntas materiales hacia obligaciones afectivas

- **Voz:** Formal, relacional; escoge los términos de la conversación. Acorta las frases cuando ya no puede desviar la pregunta.

- **Competencia:** Negociar acceso social y detectar qué palabras alteran el crédito de una casa.

- **Límite:** No entrega la dirección de Vera. Puede sacrificar el pago ajeno por su imagen; no absolverla por proteger a su prima.

- **Evitar:** Convertir cada réplica en una ocurrencia o confundir orgullo con gritos.

- **Vida cotidiana fuera del caso:** Pendiente; no completar inventando.


Muestra existente (`c2.line.0`):

> Inés lleva años sentándose a mi mesa. Nunca se me ocurrió pasarle una cuenta.

> EN: Inés has eaten at my table for years. I never thought to send her a bill.


### Mireya Salceda — `char_mireya`


- **Deseo:** Cerrar cuentas y conservar su empleo

- **Temor:** Que le atribuyan un déficit ajeno

- **Contradicción:** Protege mediante reglas y causa daño aplicándolas sin verificar

- **Estrategia:** Acota responsabilidad y cita fechas

- **Voz:** Preciso, administrativo, frases medidas; distingue lo recibido por la oficina de lo que ella vio.

- **Competencia:** Llevar cuentas, contrastar entradas y reconocer el alcance de una firma.

- **Límite:** Propuesta: no firma una orden ajena como propia; puede cobrar antes de verificar por miedo al déficit.

- **Evitar:** Hacerla una recaudadora malvada o darle jerga jurídica en todas las frases.

- **Vida cotidiana fuera del caso:** Pendiente; no completar inventando.


Muestra existente (`c1.line.0`):

> Seis monedas: dos de material y cuatro de trabajo. El yesero ya cobró. Necesito saber a qué cuenta cargarlo.

> EN: Six coins: two for materials, four for labour. The plasterer has been paid. I need to know which account bears the cost.


### Mara Calce — `char_mara`


- **Deseo:** Publicar información útil fuera de los salones

- **Temor:** Ser impresora del poder

- **Contradicción:** Exige pruebas y tolera sus propias inferencias

- **Estrategia:** Pide que el otro sostenga sus palabras públicamente

- **Voz:** Ágil y orientado a atribución: quién dijo qué, con qué respaldo. Bajo presión defiende primero la inferencia.

- **Competencia:** Imprimir, reconocer materiales y separar fecha comprobada de conclusión editorial.

- **Límite:** Propuesta: puede corregir lo no probado sin retirar hechos verificados; no es omnisciente ni automáticamente honesta.

- **Evitar:** Periodista sarcástica que siempre tiene razón o conoce sobornos y secretos no transmitidos.

- **Vida cotidiana fuera del caso:** Guarda una copia sin cortar para compartirla; no implica una afición biográfica adicional.


Muestra existente (`c4.answer.0`):

> Yo imprimí los folios numerados; Ivo los encuadernó. Rovena anotó el dinero. El hilo azul dice qué tomo es. No dice si él pagó.

> EN: I printed the numbered sheets; Ivo bound them. Rovena entered the money. The blue thread tells you which volume it is. It cannot tell you whether he paid.


### Nilo Lobreda — `char_nilo`


- **Deseo:** Ayudar sin depender del apellido

- **Temor:** Que sus seres queridos descubran lo que oculta

- **Contradicción:** Generosidad pagada a veces por otras personas

- **Estrategia:** Resuelve primero y explica después

- **Voz:** Directo y cálido; ofrece soluciones antes de considerar condiciones. Vacila cuando debe admitir un coste personal.

- **Competencia:** Transportar suministros y resolver necesidades prácticas; aprende a preguntar antes de actuar.

- **Límite:** Propuesta: reconocer la deuda propia aunque no quiera empeñar el anillo. El secreto lunario no la cancela.

- **Evitar:** Héroe altruista infalible, rasgos de lobo visibles o frases misteriosas que revelen automáticamente su especie.

- **Vida cotidiana fuera del caso:** Pendiente; no completar inventando.


Muestra existente (`c3.answer.2`):

> Vi a Bruna cerrar la caja y la llevé al dispensario. Pregúnteme por ese trayecto. Por la oficina no puedo responder.

> EN: I saw Bruna seal it, then carried it to the dispensary. Ask me about that journey. I cannot answer for the office.


### Saúl Veyra — `char_saul`


- **Deseo:** Ser una autoridad confiable

- **Temor:** Corregirse ante subordinados

- **Contradicción:** Disciplina usada para aplazar una rectificación

- **Estrategia:** Defiende la primera decisión para no discutir la segunda

- **Voz:** Breve, procedural; nombra órdenes, horas y responsables. Bajo presión intenta volver a la decisión inicial.

- **Competencia:** Custodia, verificación de autorizaciones y organización del puesto.

- **Límite:** No atribuye al soldado la orden que él sostuvo.

- **Evitar:** Militar sádico genérico, amenazas constantes o volverlo simpático sólo por admitir un error.

- **Vida cotidiana fuera del caso:** Pendiente; no completar inventando.


Muestra existente (`c3.line.1`):

> El envío llegó a las siete de la tarde. No podía verificar el sello.

> EN: The delivery arrived at seven in the evening. I could not verify its seal.


### Bruna Narel — `char_bruna`


- **Deseo:** Atender preservando privacidad

- **Temor:** Convertir ayuda en selección moral

- **Contradicción:** Su discreción puede dificultar rendición de cuentas

- **Estrategia:** Pregunta por efectos materiales y horarios

- **Voz:** Concreto, sobrio; vuelve al gasto y al trabajo real cuando otros se desvían. Humor seco en confianza.

- **Competencia:** Preparar y documentar suministros y distinguir una compra de su entrega.

- **Límite:** No ofrece nombres de pacientes como espectáculo o prueba irrelevante.

- **Evitar:** Anciana oracular, diagnóstico mágico de mentiras o santidad sin intereses materiales.

- **Vida cotidiana fuera del caso:** Pendiente; no completar inventando.


Muestra existente (`c3.answer.1`):

> El carretero me cobró su tiempo. Aquí está el recibo. Fecha una entrega; no le da una lista de pacientes.

> EN: The carter charged me for his time. Here is the receipt. It dates a delivery; it does not give you a patient list.


### Inés Corvela — `char_ines`


- **Deseo:** Vivir de su oficio con autonomía

- **Temor:** Que la cercanía suponga consentimiento

- **Contradicción:** Pone límites tarde a quienes quiere

- **Estrategia:** Fija cantidades, plazos y condiciones

- **Voz:** Claro, rítmico; separa afecto, consentimiento y trabajo con palabras cotidianas.

- **Competencia:** Negociar actuaciones, pagar músicos y evaluar el coste de una concesión.

- **Límite:** No tratar una invitación, préstamo o convivencia como consentimiento ilimitado.

- **Evitar:** Coqueteo obligatorio o agradecer cualquier fallo favorable como interés romántico.

- **Vida cotidiana fuera del caso:** En días libres puede cantar por gusto y escoger ella la canción; no añadir hábitos nuevos como hechos.


Muestra existente (`c2.line.3`):

> Antes cantaba sola. Esta vez había músicos que pagar.

> EN: I used to sing alone. This time there were musicians to pay.


### Ivo Valcés — `char_ivo`


- **Deseo:** Trabajar y pagar únicamente lo que debe

- **Temor:** Perder taller y parecer ignorante

- **Contradicción:** Explica tanto que confunde una respuesta simple

- **Estrategia:** Usa objetos concretos y repite el punto central

- **Voz:** Concreto, cotidiano; empieza por un objeto y puede explicar más de lo necesario. Bajo presión se vuelve breve.

- **Competencia:** Encuadernar, proteger papel y preparar copias a partir de lo aprendido.

- **Límite:** Propuesta: insiste en que el pago documentado se reconozca; su torpeza verbal no implica incapacidad.

- **Evitar:** Acento caricaturesco, chistes de ignorancia o convertirlo en portavoz moral perfecto.

- **Vida cotidiana fuera del caso:** Pendiente; no completar inventando.


Muestra existente (`c1.line.2`):

> Llevé el aviso antes de la lluvia. Querían el original, así que pedí copia. Esta.

> EN: I took the notice in before the rain. They wanted the original, so I asked for a copy. This one.


### Relaciones y conocimiento

Vera Serravalle existe como entidad vinculada a Leonora; no llenar su ficha con una nueva historia por deducción. Las relaciones y secretos deben recuperarse de sus fuentes antes de ampliar escenas. El conjunto de seis relaciones registrado en memoria no representa una matriz social completa ni todas las parejas posibles.

Los perfiles completos y sus muestras bilingües están en `memoria-salverna/perfiles-autoria-v1.json`. Las fichas de producción visual antiguas describen diseños que pueden haber sido sustituidos; consultar la autoridad visual actual antes de usarlas.

### Seis casos judiciales conservados

| Caso | Título | Participantes documentados | Dependencias |
|---|---|---|---|

| C1 | El muro antes de la lluvia | Mireya Salceda, Ivo Valcés | Sin dependencia declarada |

| C2 | La canción que era un regalo | Leonora Serravalle, Inés Corvela, Mara Calce | Sin dependencia declarada |

| C3 | Tres frascos bajo un sello viejo | Bruna Narel, Saúl Veyra, Nilo Lobreda | Sin dependencia declarada |

| C4 | El libro de recibos equivocado | Mireya Salceda, Ivo Valcés, Mara Calce | C1 |

| C5 | Una deuda entre amigos | Nilo Lobreda, Inés Corvela, Bruna Narel | C3 |

| C6 | El hilo negro y la noticia | Leonora Serravalle, Mara Calce | C2 |


Para la historia y ramificación real de esos casos consultar `salverna-game/data/cases.json` y `locales/es.json` / `en.json`; para prosa previa, `arco-1-guiones-revisados.md`. No trasladar pruebas o culpabilidades judiciales a eventos románticos sin adaptación expresa.

Principios narrativos ya trabajados: recepción institucional no prueba lectura personal; incumplimiento no acredita fraude inicial; una retención inicialmente justificada no legitima la demora; identificar un tomo no demuestra pago; ayudar no extingue una deuda; una confesión posterior no justifica una publicación anterior sin pruebas.

## 7. Dirección de arte y aprobaciones

### Gramática compartida

Ilustración artesanal para novela visual: línea de presión variable, pequeñas irregularidades deliberadas y contornos más oscuros que cada material. En una unión de claro y oscuro manda el borde del material oscuro. Pintura mate con masas amplias, pigmento y textura localizados, zonas tranquilas y cambios selectivos de dureza.

Cabello por masas reconocibles, sin modelar cada mechón. Rostros con proporciones, asimetrías y personalidad individuales: ni una belleza idealizada idéntica en todos ni una caricatura tosca universal. El acabado de la cara, manos, pelo y ropa debe pertenecer a la misma ilustración.

El usuario rechaza dominante amarilla/naranja global, piel plástica, brillo 3D, vector excesivamente limpio y textura añadida como ruido. Corregir un baño cálido no significa enfriar toda imagen. Pintar materiales por color local independiente; conservar diferencias de piel.

Los nombres de técnicas —gouache, grafito coloreado— describen objetivos de ejecución. No prueban qué pincel o medio usó el artista de referencia. Los originales ilustrados enseñan comportamiento del dibujo y pintura; nunca autorizan copiar su rostro, traje o accesorios.

### Registro de bases visuales


| Persona | Estado registrado | Original de referencia | Condición de continuidad |
|---|---|---|---|

| Leonora Serravalle | `user_selected_original_visual_base` | [produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png>) | t48 aprobada; t49 molesta/alegre pendientes. No usar el texto C2 contra la imagen t48. |

| Mireya Salceda | `approved_identity_and_technique_attachment_correction_pending` | [produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png](<produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png>) | Identidad y técnica v2 aprobadas; unión visible de llaves pendiente. No rediseñar cara al corregirla. |

| Ivo Valcés | `approved_identity_and_technique` | [produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png](<produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png>) | El manifiesto registra identidad y técnica C3 aprobadas. Conservar original; no asumir aprobación de toda variante. |

| Inés Corvela | `candidate_review_required` | [produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png](<produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png>) | T50 es candidata posterior. No hay nueva base aprobada; no derivar expresiones. |

| Mara Calce | `candidate_review_required` | [produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png>) | Candidata; confirmar neutral antes de variantes. |

| Nilo Lobreda | `candidate_review_required` | [produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png>) | Candidato; no añadir rasgos de lobo a una pose. |

| Saúl Veyra | `candidate_review_required` | [produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png>) | Candidato; revisar diseño antes de variantes. |

| Bruna Narel | `candidate_review_required` | [produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png>) | Candidata; t30 requiere rediseño, no es base aprobada. |


**Leonora t48 — autoridad actual:** la palabra «candidato» en el nombre del PNG no invalida su aprobación posterior. Pelo rojo de silueta de corazón, vestuario negro, lino blanco y la construcción visible de esa base mandan sobre un prompt previo. No convertirla en vampiresa ni decidir con su expresión si es culpable.


![Leonora t48, base aprobada](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora-neutral-original-aprobado.png>)


### Regla absoluta de expresiones

Cada expresión parte del dibujo **ORIGINAL aprobado de esa misma persona**, como único adjunto visual. Base → molesta; base → alegre. Nunca neutral → molesta → alegre. Preservar rostro, cabello, cuerpo, vestuario, accesorios, paleta, trazado, pintura y encuadre. Cambiar sólo expresión, gesto y pliegues indispensables. Sin base aprobada no se generan expresiones desde texto.

La aprobación de una técnica no autoriza prestar el rostro de Mireya a los demás. Los accesorios necesitan sujeción o agarre plausible; las llaves no nacen del brazo ni del libro. Cada personaje debe actuar según su personalidad.

### Referencias técnicas identificadas


- [imgi_161_latest.webp](<imgi_161_latest.webp>) — referencia de técnica para diseño inicial; no adjuntar a cambios de expresión.

- [imgi_26_1000 (3).webp](<imgi_26_1000 (3).webp>) — referencia de técnica para diseño inicial; no adjuntar a cambios de expresión.

- [imgi_28_latest.webp](<imgi_28_latest.webp>) — referencia de técnica para diseño inicial; no adjuntar a cambios de expresión.


## 8. Vestuario, cabello, maquillaje y actuación

El vestuario necesita investigación concreta antes del prompt: prenda identificable, corte, construcción, materiales, ocasión y función para esa persona. «Vestido elegante», color de cabello o una lista de términos de época no sustituyen diseño.

Separar referencias fotográficas de moda y originales ilustrados de técnica. Las fotografías orientan silueta y coordinación; no trasladar su iluminación amarilla ni su realismo a los sprites. Una misma casa puede compartir códigos sin vestir a todos igual. Cultura, linaje, clase, profesión y gusto son variables distintas.

### Ficha mínima para un diseño nuevo

Persona y medios; ocasión y clima; intención social; referencia principal con procedencia; cuerpo/cintura/escote/mangas/cierre/falda; material; motivo dominante; accesorios y sujeción; estructura del peinado y tocado; maquillaje pertinente; simplificación para móvil; diferencias respecto al elenco. No acumular lazos, cordones, adornos o herramientas laborales para llenar huecos.

Para peinados y maquillaje consultar `produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md`. El gesto debe proceder de una intención y usar manos legibles. No resolver todas las emociones con la misma sonrisa, brazo cruzado o puño.

### Nueve originales de vestuario aportados por el usuario

Conservados sin modificación en `produccion-arte/referencias-vestuario-usuario-2026-10-11`. Son referentes, no vestuario final aprobado. Las observaciones describen apariencia; no certifican tejido ni temporada exacta de la serie.


| Referencia original | Qué estudiar |
|---|---|

| [Ref. 01](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-01.png>) | Imperio, escotes amplios, mangas cortas translúcidas, flores y guantes. Dos colores, una gramática social. |

| [Ref. 02](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-02.png>) | Conjunto azul floral abotonado frente a terciopelo burdeos de cuello alzado y bordado dorado concentrado. Dos autoridades maduras distintas. |

| [Ref. 03](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-03.png>) | Ceremonia del XVIII: cuerpo ajustado, falda amplia sostenida, manto; casaca, chaleco, calzón y medias masculinos. Diferente de imperio. |

| [Ref. 04](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-04.png>) | Cuerpo apuntado, sobrefalda abierta, mangas al codo con volantes, ribetes que siguen aberturas. |

| [Ref. 05](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-05.png>) | Diurno: parte superior azul floral con solapas y falda morada; contraste estructural, joya pequeña. |

| [Ref. 06](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-06.png>) | Imperio azul verdoso, bordado botánico vertical organizado, escote definido, un broche de cintura; guantes/abanico coordinados. |

| [Ref. 07](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-07.png>) | Misma familia de corte en cuerpos distintos; variación de escote, mangas, flores y joyería. |

| [Ref. 08](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-08.png>) | Calle: prendas largas de abrigo, solapas/cuello, puños, guantes y bolso. Distintas del baile. |

| [Ref. 09](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ref-09.png>) | Crema imperio, manga abullonada, franja enjoyada sobre el pecho; zonas lisas hacen legible el adorno. |


### Investigación de figurinismo ya registrada

El estudio de vestuario cita entrevistas a Ellen Mirojnick y John Glaser sobre Bridgerton; Lyn Elizabeth Paolo y Laura Frecon sobre Queen Charlotte; Michele Clapton sobre clima, comercio y materiales; y el archivo de bordados de Michele Carragher. Son fuentes investigadas anteriormente, no una nueva verificación web en esta entrega. Los enlaces y límites de lectura están en el estudio original.

Aprendizajes: diferenciar familias mediante silueta, forma y adorno además de color; vestir para la ocasión; motivos organizados, no arabescos improvisados; simplificar bordado conservando ubicación y escala; explicar las mezclas de época. En Bruna t30 la adaptación de cordones a grandes ochos blancos deformó la construcción y fue cuestionada. No repetirla como diseño aprobado.

## 9. Referentes e investigación

### Dispatch — gestión, incidentes y representación

Se estudió material JSON exportado localmente y capturas. Informa asignación por capacidades, especialistas, disponibilidad, incidentes, progresión y cierre. La ejecución completa de su fórmula de éxito no se recuperó; no presentar una fórmula propia como copia verificada de Dispatch.

Informes en `referencias-dispatch`: mecánicas, narrativa/tutoriales y episodios/plugins. Los exports originales están fuera del proyecto, en `C:/Users/carlo/OneDrive/Escritorio/Output/Exports/Dispatch`; no se necesita distribuirlos como recursos de nuestro juego. Este documento enlaza la evidencia propia, sin convertir material ajeno en contenido de producción.

Ocho capturas recibidas el 13 de octubre: siete únicas, porque 01 y 05 son idénticas. Conservadas con manifiesto y análisis.


- [01-incidente-tutorial.png](<referencias-dispatch/capturas-ui-2026-10-13/01-incidente-tutorial.png>): Contexto, situación, tres opciones, radar y estado del elenco.

- [02-evaluacion-recompensas.png](<referencias-dispatch/capturas-ui-2026-10-13/02-evaluacion-recompensas.png>): Evaluación, progreso, éxitos/fallos y recompensas.

- [03-mejoras-tutorial.png](<referencias-dispatch/capturas-ui-2026-10-13/03-mejoras-tutorial.png>): Mejora y comparación de atributos; no importa automáticamente una tienda de puntos.

- [04-ficha-personaje.png](<referencias-dispatch/capturas-ui-2026-10-13/04-ficha-personaje.png>): Personaje expresivo, biografía y capacidades.

- [05-incidente-repetido.png](<referencias-dispatch/capturas-ui-2026-10-13/05-incidente-repetido.png>): Duplicado exacto de la captura 01.

- [06-resultado-radar.png](<referencias-dispatch/capturas-ui-2026-10-13/06-resultado-radar.png>): Resolución visible y consecuencia textual.

- [07-mapa-marcador.png](<referencias-dispatch/capturas-ui-2026-10-13/07-mapa-marcador.png>): Mapa elevado, locación destacada y marcador; significado del número 2 no probado.

- [08-presentacion-encargo.png](<referencias-dispatch/capturas-ui-2026-10-13/08-presentacion-encargo.png>): Presentación enfocada de un encargo sobre mapa atenuado.


La adaptación móvil conserva tarea dominante y reduce paneles simultáneos. No hay medición de tiempos de animación ni usabilidad a partir de estas imágenes. Tampoco se recibió una captura del resultado actual de Figma AI para auditarlo directamente: la crítica a «app de citas» procede del usuario.

### Candy Crush — lectura del mapa móvil

Referencias preservadas en `referencias-candy-crush`: portada, modal de recursos y mapa. Aprendizajes: introducción visual inmediata, perspectiva elevada, marcadores claros, jerarquía superior/inferior y estado reconocible. Su mapa lineal de niveles no se importa como estructura obligatoria de ciudad. El modal de recursos es comercial, no ficha de nivel. No inferir motor o programación a partir de una captura ni importar vidas, tienda o esperas por este referente.

### Dressmaker y otros antecedentes

Las dos inspecciones de Dressmaker documentan scripts, localización, sprites y escenas como referencia de cuidado narrativo y composición. No se ejecutó ese referente ni se comprobó su uso en teléfono. ModuLore fue inspeccionado como antecedente, sin conexión ni modificaciones del proyecto. Los informes de investigación 2D son apoyo de producción, no identidad artística nueva aprobada.

## 10. Producción de recursos y composición

Primero componer una pantalla y su interacción; después derivar recursos. Es la prioridad del usuario antes de más APK. No generar un paquete masivo mientras la distribución siga sin revisión.

El mapa debe separar terreno, edificios que cambian, elementos de ambiente, retratos, caminos, aros, marcadores y UI. El suelo bajo un objeto móvil debe existir. Todos los elementos del mapa comparten cámara, perspectiva y escala. «Recortar y replicar un edificio» requiere comprobar bordes y correspondencia visual; no garantiza identidad por sí solo.

Texto, cifras, radar, caminos, progreso y controles simples deben ser dinámicos, no una imagen por estado. Marcos ilustrados escalables mediante nueve zonas o vectores. Retratos de viaje se recortan de la ilustración aprobada; no generar otra cara para cada tamaño.

Objetivos preliminares de la maqueta: marco lógico **432×768**, preparación candidata **864×1536**; ciudad visible aproximadamente 432×602 entre barras. No son tamaños finales aprobados ni garantía de salida del generador. Los sprites judiciales tienen encargos históricos 1024×1536; no confundir fuente de ilustración y espacio de interfaz.

Consultar `diseno-temporada-social/figma/INVENTARIO-VISUAL-PRELIMINAR.md` para cajas tentativas. La vertical móvil necesita contemplar otras proporciones, áreas seguras y textos ES/EN, no sólo una captura 9:16.

Escenarios judiciales previos: cámara y capas en `produccion-arte/mundo-v03/CONTRATO-ARTE-UI.md` y `produccion-arte/CONTRATO-CAPAS-TRIBUNAL.md`. Son antecedentes útiles; no convierten el tribunal en escenario social final.

## 11. Implementación y herramientas

### Godot y Android

Existe un proyecto Godot con render Compatibility y orientación vertical. La entrada documentada es `JUGAR-SALVERNA.cmd`, que abre `salverna-game/scenes/court.tscn`. F5 desde el proyecto también abre la escena integrada. El lanzador y las rutas del motor deben comprobarse en el equipo receptor.

La lógica judicial incluye casos, condiciones, preguntas, pruebas, acta, reputaciones, progresión, guardado versionado y cola persistente de presentación. Algunas funciones antiguas de casa/relaciones existen en otras escenas pero no están integradas en la entrada actual. Romance, temporada social, minijuego de adivina, audio y monetización no están implementados.

Archivos de entrada para desarrollo: `project.godot`, `scripts/court.gd`, `scripts/game_state.gd`, `data/cases.json`, `data/balance.json`, `data/people.json` y `locales/es.json` / `en.json`. Separar contenido, lógica y presentación. El arte candidato integrado no implica aprobación del usuario.

El APK judicial anterior sirve de antecedente técnico. Requiere exportación actualizada, instalación y revisión física de rendimiento, toque, suspensión y guardado. No afirmar publicación Google Play, calidad comercial o compatibilidad total por exportar un APK.

### Figma: estado documental exacto

Archivo: https://www.figma.com/design/kc12gfvIhjvUYkitBxFTsn

La página social `13:16` conserva fundamentos y tres controles reutilizables. La operación que creaba pantallas se revirtió por un enlace propio; el reintento corregido quedó bloqueado por cuota MCP. No quedaron las 54 pantallas sociales guardadas remotamente.

`diseno-temporada-social/figma/prototipo-flujo.html` contiene 27 estados ES y 27 EN, con 438 conexiones verificadas estructuralmente. Son fixtures A–H, ramas de demostración y gráficos estáticos; no simulación ni personajes canónicos. El plugin local está preparado y con sintaxis comprobada, todavía sin ejecutar en Figma. No hubo revisión visual interactiva automatizada: el navegador bloqueó `file://`.

`BRIEF-PARA-FIGMA-AI.md` y `PROMPTS-PARA-FIGMA-AI.md` conservan el encargo anterior. Deben revisarse frente al rechazo de aspecto de app. Figma es herramienta de composición y prototipo; su resultado automático no constituye criterio de aprobación ni proyecto Godot.

### Verificación que se debe repetir al modificar

Después de cambios de IDs, fichas, dependencias o fuentes: `python memoria-salverna/validar_memoria.py`. Para contenido judicial: validador en `salverna-game/tests/validate_content.py` y pruebas Godot documentadas en README. Pruebas estructurales, revisión editorial, inspección visual y observación con jugadores son controles diferentes.

No repetir pruebas de juego por una simple compilación documental. Este documento no certifica rendimiento, diversión ni aprobación estética.

## 12. Pendientes y siguiente unidad de trabajo

### Decisiones aún necesarias

| Bloque | Qué falta |
|---|---|
| Encargo | Papel exacto de la casamentera, patrocinio, presión central y condiciones de cierre |
| Reparto | Ocho fichas adultas, motivos, voces, recursos y matriz de rutas compatibles/incompatibles |
| Calendario | Día o franja, reservas, retorno, recuperación y cruce entre semanas |
| Éxito | Fórmula del equipo/radar, probabilidad, azar y alcance del incidente |
| Relaciones | Cercanía, interés direccional, hitos y compromisos con agencia |
| Reputación | Causas públicas, límites, rangos y desbloqueos |
| Estados | Vergüenza, incapacidad, duración y alternativas de reemplazo |
| Clases | Frecuencia, efecto y conflicto real con otras invitaciones |
| Narrativa | Arco semanal, eventos centrales y finales; señales previas a consecuencias graves |
| Arte | Bases pendientes, revisión de expresiones t49, identidad de candidatos nuevos y UI propia |
| Interfaz | Composición real de asignación/incidente, legibilidad y flujo en teléfono |
| Minijuego | Alcance y utilidad; no es requisito para probar el núcleo |

### Próxima unidad recomendada, no implementación ya realizada

Una pantalla de asignación y un incidente conectado a tamaño móvil, usando estados de prueba claramente señalados. Revisar composición antes de ampliar el Figma o producir imágenes. Después, un recorrido de dos semanas que pruebe simultaneidad, clase coincidente, evento largo, indisposición, sustitución y cierre causal.

Alguien que recibe este proyecto debería entregar una lectura de contradicciones y un bloque concreto terminado; no multiplicar personajes o pantallas sin resolver el núcleo. No hace falta pedir otra vez decisiones explícitas del usuario que ya están registradas.

## 13. Prompt de incorporación al proyecto

Texto para entregar junto con este documento y la carpeta del proyecto:

> Recibes Salverna, proyecto móvil vertical bilingüe con un prototipo judicial Godot y una nueva dirección de temporada social todavía en diseño. Lee este documento, AGENTS.md, la memoria y las fuentes pertinentes. Distingue requisitos del usuario, base de mundo, propuesta, implementación y aprobación. Conserva identidad visual y narrativa; no conviertas al elenco judicial automáticamente en pretendientes. El juego social se planifica por semana y se ejecuta por fechas, con actividades simultáneas, viajes, incidentes, resultados y reemplazos excepcionales. Los cinco atributos son Baile, Estatus, Chisme, Presencia e Intelecto. El mapa es central y la interfaz debe sentirse videojuego de época. No inventes fórmulas, biografías o aprobaciones. Para expresiones usa exclusivamente el ORIGINAL aprobado de la misma persona. Propón y completa una unidad revisable, registra sus límites, revisa el resultado real y conserva textos jugables ES/EN con claves estables.

**English handoff summary:** Salverna combines an existing bilingual Godot court prototype with a newly designed mobile social-season game. Weekly preplanning precedes date-based concurrent execution, incidents and exceptional replacements. The new mode is not implemented. Preserve author truth, individual knowledge, playthrough state and visual approvals separately. Current Leonora base is t48; t49 expressions remain unapproved. Never derive expressions from another expression or another character. The appended prompts retain their source status and may contain legacy conflicts; they are not blanket approval to generate. Read the linked sources before extending content.

# Anexo A: prompts y sus autoridades

## A.1. Qué significa «prompt aprobado» en este proyecto

El resultado t48 está aprobado. El texto exacto que lo produjo se conserva como procedencia; no garantiza idéntico resultado al repetirlo. Otros prompts son encargos, propuestas o historial. Ningún catálogo completo queda aprobado por figurar aquí.

Los siguientes extractos se conservan literalmente. **No ejecutar en lote.** Antes de usar uno, verificar base, adjuntos, estado de revisión y contradicciones señaladas. La referencia visible aprobada prevalece sobre instrucciones textuales antiguas.

## A.2. Leonora t48: prompt exacto de la imagen posteriormente aprobada

El encargo conserva su marca de candidatura previa. La aprobación posterior y la corrección del diagnóstico de halo están en t49/manifest.json y decisiones.md. No editarlo para aparentar que el prompt ya estaba aprobado al ejecutarse.


**Resumen español original del encargo:**

Regeneración desde cero del diseño t47, sin adjuntar Leonora previa. Carta de pigmentos: lino blanco puro #FFFFFF, sombras gris frío #DADDE7; piel pálida rosa-lila #E8DCE4 con rubor local, cabello rojo #A53649 y ropa carbón neutra. Aplicar colores por material sin filtro cálido global; originales solo técnica. Punta y uña del índice visibles sobre esquina del pañuelo, otros tres dedos distinguibles y pulgar anatómico. Mantener identidad, corazón, mini tocado, perlas y duelo ambiguo. Candidata pendiente de revisión.

**Adjuntos originales y sus roles en el texto:**


- [produccion-arte/mundo-v03/tanda-48-leonora-color-local/paleta.png](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/paleta.png>)

- [imgi_28_latest.webp](<imgi_28_latest.webp>)

- [imgi_26_1000 (3).webp](<imgi_26_1000 (3).webp>)

- [produccion-arte/mundo-v03/tanda-24-muestras-visuales/tela-original.png](<produccion-arte/mundo-v03/tanda-24-muestras-visuales/tela-original.png>)


**Prompt exacto ejecutado, inglés:**

```text
NEW ORIGINAL DRAWING FROM SCRATCH. Draw Leonora Serravalle, a mature aristocratic woman around46, in mourning whose sincerity is impossible to judge. She might be an unlucky bereaved woman, or concealing something; the picture must not settle that question. One game dialogue sprite, eye level, strictly frontal torso and face, head to UPPER THIGH only. Adult substantial torso, normal neck, real shoulders and waist, NOT a slender fashion model. Head INCLUDING styled hair near ONE QUARTER of visible figure, good-sized readable face, no full-body zoom-out. All hair, hands and elbows inside margins.

References: image1 local pigment COLOUR KEY only. Images2 and3 ORIGINAL illustrations for handmade drawing and simple painting ONLY; never copy their people, poses, clothes, hats or jewellery. Image4 is an ORIGINAL paint-detail sample: follow its sparse irregular coloured-pencil edge and broad quiet paint shapes throughout the sprite. No previous Leonora image is attached, not an edit or tracing.

COLOUR-SEPARATION PAINTING: apply opaque local pigments first, NOT a lit/rendered figure with a filter. Pale living rose-porcelain skin #E8DCE4 with local subdued rose shadow #BA9DAE, pale light #F4EBF2; subtle soft pink at nose/ears, NO grey corpse skin and no orange peach glaze. Jacket deep black #252331, skirt slightly lighter charcoal #34333A; PURE WHITE linen #FFFFFF occupying most of the blouse, collar, cuffs and handkerchief. Use only a few cool pale grey #DADDE7 shadow strokes. Treat WHITE as unprinted bright white paper left untouched. Never tint the white with the skin colour or warm brown outlines. HAIR clearly lively CHERRY RED #A53649, darker red-violet shadows, one matte red reflection, not auburn-brown, copper, neon pink or bright orange. Lips muted rose-mauve #815766. No environmental golden light, global warmth, global blue wash, paper tint or red aura.

JEWELLERY: exactly one small round WHITE PEARL stud attached directly to each earlobe. No gold setting, diamonds, geometric pendants, necklace or floating accessories.

CHARACTERFUL FACE: Distinctive mature face with a slightly BROADER angular jaw and a SHORT BLUNT CHIN, not an elongated tapered beauty face. Broad cheeks, subtly unequal SMALL grey-green eyes, viewer-left eye narrower and heavier-lidded, viewer-right eye more open; uneven eyebrows, a small mouth slightly off-centre with thin unequal lips. Face constructed with relaxed economical hand-drawn shapes, not symmetric glamour, not elegant almond-eyed beauty, no needle chin or plump cosmetic lips. Keep adult facial presence rather than adding wrinkles or realism. NO sculpted perfect pointed nose: suggest a modest individual nose with a soft muted rose SHADOW UNDER THE TIP and a tiny broken nostril mark. Leave the bridge largely unoutlined and softly merged with cheek. No sharp dark contour tracing the nose, no bright nose highlight, no cosmetic nose rendering. Living PALE NEUTRAL ROSE skin, soft diffused dusty pink blush on cheeks and nose, subtle mauve under-eye and jaw transitions. Several softly blended local hues, not a flat skin sticker, not peach copper or grey. Small tears at lower lids, real tired dignity, possible genuine grief, no knowing evil smirk.
HAIR IS THE PRIMARY SILHOUETTE: cherry-red hair arranged in a clearly readable symmetrical HEART outline, TWO rounded upright lobes of equal height, DEEP OPEN CENTRAL NOTCH above the forehead, tapered sides. Draw the complete uninterrupted heart BEFORE adding the little hat. No swept-over mound, no flattened lobe. Broad simple brushed locks forming the HEART ONLY. Smooth short tapered side locks ending behind ears. NO hanging curls, ringlets, coils or spirals. Hair stays distinct from hat.
HAT SECONDARY: a MINUSCULE BLACK MINI TOP HAT, small low cylindrical crown just slightly TALLER than WIDE, very narrow brim. Entire ornament only ONE QUARTER FACE WIDTH. Fixed snugly against VIEWER'S RIGHT OUTER hair lobe at temple level, below its summit; a tiny comb base enters the hair and a small contact shadow connects it firmly. Not floating and not a wide flat disk. Heart outline and notch entirely intact. A small sheer charcoal veil to upper ear only, showing red hair beneath. No feathers, floral decoration, ribbons or large brim.
TWO DISTINCT GARMENTS, simple repeatable construction:
1. BLACK SHORT BODICE-JACKET at natural waist. Two angular folded lapels, THREE small self-covered front buttons, tailored long sleeves, visible pointed structured shoulder caps. Its hem ends in EXACTLY TWO SHORT POINTS at UPPER HIP, one each side of centre. Each point is a complete clean triangular extension of the jacket hem, fully readable over skirt; NO long tails, scraps, thigh-length extensions, peplum ruffles or overlapping skirt panels. Adult fitted shape without pinched wasp waist.
2. SEPARATE PLAIN CHARCOAL FIVE-GORE FLARED SKIRT: smooth waist, concealed fastening, one continuous gentle bell silhouette. Three broad vertical shadow areas imply the panels; NO visible decorative seam grid, front opening, overskirt, tiers, frills, lace, embroidery, chains, gathering, bustle or train. It starts UNDER the short jacket and stays visually independent.
WHITE HIGH STANDING LINEN COLLAR with one restrained softly ruffled edge and matching narrow ruffled cuffs. No multiplied frill tiers or chest ornament. Matte old fine wool maintained carefully, no shiny silk or modern leather.

ACTING: strictly FRONTAL shoulders and head, looking at judge. Her right hand delicately pinches a white linen handkerchief at outer cheek, dabbing tears. Her OTHER hand rests lightly flat over lower abdomen just below jacket hem, fingers gently grouped, elbow slightly open. Not dangling, not sleeve adjusting or wrist holding. Readable compact adult gesture.
PAINT THE ENTIRE FIGURE with broad opaque GOUACHE strokes and sparse interrupted COLOURED GRAPHITE accents. Reference originals' economical quiet interior colour, very few large swept shadows and selected soft blended nose/cheek/lid transitions. Handcrafted pressure-varying edges darker than their own material; darker material owns light/dark joins. Some edges lost in paint, some firmer. Hair brush language also on face, hands and clothing. Not a uniform thick ink outline, polished vector, realistic portrait, faceted skin, intricate folds, engraved hair, uniform grain filter or glossy 3D. No extra detail to fill space.
TRUE TRANSPARENT BACKGROUND, no halo, vignette, mist, cast shadow blob or spotlight. No scene, podium, text or swatches.
Prioritise the lively imperfect DRAWING of the original game references. The face must share the hair's relaxed brushed edges: subtly uneven mouth painted with two simple strokes, soft nose colour transition, sparse eyebrow strokes. Garments are readable large opaque shapes, never polished digital airbrush. No warm light source.
Final priorities: HEART SILHOUETTE visible intact above tiny side ornament; adult distinctive face; ambiguous genuine grief; neutral pale pink skin and WHITE linen without creamy tint; relaxed original game brushwork. Transparent cutout with NO coloured haze outside the figure.
USER'S LATEST PRIORITY: jacket AND separate skirt both BLACK mourning garments, distinguished subtly by local charcoal value rather than violet costume. Simplify clothing to the SAME relaxed painted language as face and hair: quiet broad shapes, two or three soft swept shadows, few fold accents, no faceted crumpled panels. Material-colour irregular edges contained on figure, NO exterior black smoke, brown ghost edges, fuzzy drop shadow, maroon mist or aura. Absolutely transparent outside sprite. Heart-shaped hair stays the successful frontal silhouette but NO RINGLETS. Tiny mini top hat with sheer short veil only, NO feather ornament. Three covered buttons only.
HAND CLARITY: hand at cheek pinches the corner of the handkerchief between thumb and index finger. The middle, ring and little fingers follow alongside with THREE distinct softly separated fingertip contours. Anatomically five fingers, each digit traceable, never a three-finger cartoon mitten. Other hand relaxed over abdomen, five anatomically correct fingers. No extra digits.
Face is the main correction: visibly individual asymmetry and broad short jaw, softly implied nose with only underside shadow, preserve rose blush and tears. Avoid perfectly defined nasal bridge. Keep original game illustrative proportions and relaxed coloured-pencil/gouache edges.
CRITICAL COLOUR METHOD — SEPARATE LOCAL PAINT MASKS: match image1's pure white patch exactly for linen; image1's pale pink-lilac patch for skin; image1's red patch for hair. Paint each material independently in opaque gouache, with ZERO overall colour grading. No warm ambient lighting, sepia, tea-stained paper, cream or beige. Original illustrations supply linework and shape ONLY, NEVER their warm colour cast. Skin remains living porcelain with local soft rose cheek blush, not a global pink filter. White stays unmistakably WHITE beside pale skin. No yellow highlights anywhere. Black clothes stay neutral charcoal, not brown. Clear transparent space around the figure, not coloured haze.
HAND AT CHEEK: thumb grips behind the cloth. INDEX fingertip and its nail are clearly visible protruding just beyond the TOP folded corner of the handkerchief near the cheek. Middle, ring and little finger each show a separate contour along the cloth's outer edge: FOUR distinguishable fingers plus anatomically placed thumb. Do not hide the index completely behind cloth. Preserve compact graceful dabbing gesture.
```


## A.3. Expresiones t49: base aprobada, resultados pendientes

Cada llamada parte únicamente de t48 ORIGINAL. Textos exactos ES/EN conservados; no son aprobación de las variantes producidas.


### annoyed / ES

Fuente: [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.es.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.es.txt>)

```text
Adjuntar solo base ORIGINAL t48. Conservar identidad, paleta, ropa y técnica exactas. Ira contenida visible: pañuelo apretado en puño, mano contraria en cintura, cejas tensas desiguales y boca cerrada. Sin gritos ni sonrisa malvada. Solo expresión, gesto y pliegues necesarios.
```


### annoyed / EN

Fuente: [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt>)

```text
EXPRESSION AND GESTURE VARIANT OF THE ATTACHED ORIGINAL APPROVED CHARACTER. The attached Leonora is the SOLE visual authority and edit target. Preserve EXACT same woman, adult face proportions and asymmetry, eyes/nose/mouth construction, heart-shaped red hair silhouette without curls, tiny top hat and veil, pearl studs, black short jacket with three buttons and two short hem points, separate black skirt, white ruffled blouse/cuffs, pale rosy skin and cheek blush. Preserve original local colour with NO warm filter; whites remain white. Preserve handcrafted irregular material-colour outlines, broad gouache paint and simple shadows. Same head size, body proportions, eye level, frontal view, head-to-upper-thigh crop and canvas. Do not beautify, redesign costume, change light, add accessories or create a different person. Change ONLY expression, gesture and physically necessary folds. Correct five-finger anatomy. Transparent background. No scene, text or colour swatches. POSE: visibly FRUSTRATED, CONTAINED ANGER with aristocratic self-control. Lower the handkerchief from face. At upper abdomen she tightly compresses her SAME white handkerchief in her right fist, a small white corner visibly protruding; her left hand is held flat against her waist, elbow slightly outward, fingers gently braced. Hands distinct, not tangled. Shoulders held rigid, chin slightly raised, eyes fixed sternly on judge with one lid tighter, brows drawn down unequally, lips pressed into a small asymmetric line. No shouting, snarling, fangs, villain grin or raised fist. Residual moisture beneath eyes but no theatrical stream of tears. Clear change from the tear-dabbing base, still mysterious and socially superior.
```


### happy / ES

Fuente: [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.es.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.es.txt>)

```text
Adjuntar solo base ORIGINAL t48. Conservar identidad, paleta, ropa y técnica exactas. Gratitud reservada: mano abierta sobre pecho, otra con pañuelo en cintura, leve inclinación y sonrisa cerrada asimétrica. Misterio y dignidad, sin entusiasmo exagerado. Solo expresión, gesto y pliegues necesarios.
```


### happy / EN

Fuente: [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt>)

```text
EXPRESSION AND GESTURE VARIANT OF THE ATTACHED ORIGINAL APPROVED CHARACTER. The attached Leonora is the SOLE visual authority and edit target. Preserve EXACT same woman, adult face proportions and asymmetry, eyes/nose/mouth construction, heart-shaped red hair silhouette without curls, tiny top hat and veil, pearl studs, black short jacket with three buttons and two short hem points, separate black skirt, white ruffled blouse/cuffs, pale rosy skin and cheek blush. Preserve original local colour with NO warm filter; whites remain white. Preserve handcrafted irregular material-colour outlines, broad gouache paint and simple shadows. Same head size, body proportions, eye level, frontal view, head-to-upper-thigh crop and canvas. Do not beautify, redesign costume, change light, add accessories or create a different person. Change ONLY expression, gesture and physically necessary folds. Correct five-finger anatomy. Transparent background. No scene, text or colour swatches. POSE: gracious, visibly GRATEFUL but mysterious and aristocratically self-possessed. BOTH hands move away from the base pose: right open hand rests lightly over upper chest below collar, fingers relaxed and individually readable; left hand holds her SAME small white handkerchief loosely at waist, fingers naturally curved. Slight composed inclination of head, shoulders softened, small warm CLOSED-MOUTH asymmetric smile, eyes appreciatively softened but still watchful. A modest grateful nod rather than exaggerated excitement, no broad toothy grin, clasped prayer hands, waving or hearts. No crying expression; a tiny remaining trace of tear is allowed. Distinct warm gesture without abandoning her dignity or ambiguous intentions.
```


## A.4. Catálogo de 24 encargos de producción ES/EN

Estos encargos proceden de los archivos enlazados por el manifiesto de producción. Se incluyen completos para entrega y consulta, **no como 24 prompts aprobados**. Hay divergencias entre el manifiesto y algunos textos que aún describen diseños anteriores. En especial, el neutral de Leonora menciona C2 y no sustituye t48. Inés requiere rediseño/revisión posterior; las otras bases pendientes no habilitan expresiones. Los prompts de t49 sustituyen las expresiones antiguas de Leonora.


### `char_leonora_neutral`

Estado del manifiesto: `reuse_approved_original`. Base: [produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_leonora_neutral.es.txt](<produccion-arte/mundo-v03/char_leonora_neutral.es.txt>)**

```text
char_leonora_neutral

Leonora Serravalle

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Noble vizcondal de la Vega, residente entre Alto Laurel y Arcos Bajos. Conserva control y prestigio con poca liquidez; depende de crédito Miravés y vínculos Rovena. Su versión del luto y Vera siguen sus fuentes, no la nueva alternativa vampírica.

Vestido negro mate reformado, cuello y puños marfil de lino, costura reparada y mangas estructuradas. Paño fino antiguo sostenido por mantenimiento, no lujo recién comprado. Es una prenda de comparecencia en otoño; el corte noble envejecido expresa rango y deuda. No añadir velo o seda brillante ausentes de C2.

Piel y pelo cobrizo exactamente según C2; sombra local de párpados y nariz, sin palidez nueva ni velo naranja.

Un broche ovalado oscuro fijado al cuello; un pañuelo marfil sujeto por su esquina. No convertirlo en camafeo con retrato, añadir pendientes o cinta si no están visibles en C2.

C2 seleccionada para prueba: rostro ancho, nariz marcada, párpados desiguales y boca asimétrica; cabello cobrizo en masas. Conservar geometría visible, no imponer una vampiresa nueva sobre esta identidad.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Pañuelo junto al pecho, barbilla firme; escucha el término que le conviene discutir.

C2 es autoridad elegida para prueba; C3 fría y C11 no la sustituyen automáticamente. El rostro y borde aún requieren comparación artesanal, no embellecimiento.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_leonora_neutral.en.txt](<produccion-arte/mundo-v03/char_leonora_neutral.en.txt>)**

```text
char_leonora_neutral

Leonora Serravalle

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A Vega viscountal noblewoman living between Alto Laurel and Arcos Bajos. She preserves control and standing despite limited cash, depending on Miravés credit and Rovena ties. Mourning and Vera retain their existing sources, not the new vampiric alternative.

Remade matte black dress, ivory linen collar and cuffs, repaired seam and structured sleeves. Old fine cloth maintained rather than newly purchased luxury. An autumn court garment whose dated noble cut conveys rank and debt. Add no veil or glossy silk absent from C2.

Exact C2 skin and copper hair; local eyelid and nose shadows without newly imposed pallor or orange glaze.

One dark oval brooch attached to the collar; one ivory handkerchief gripped at a corner. Do not turn it into a portrait cameo or add earrings or ribbons absent from C2.

C2 selected for testing: broad face, prominent nose, unequal lids and asymmetric mouth; copper hair in masses. Preserve visible geometry, never impose a new vampire on this identity.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Handkerchief near chest, steady chin; she listens for the term she can challenge.

C2 is the selected test authority; cold C3 and C11 do not automatically supersede it. Face and contours still need handcrafted-style review, not beautification.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_leonora_annoyed`

Estado del manifiesto: `ready_from_approved_original_only`. Base: [produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png>).


**ES — [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.es.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.es.txt>)**

```text
Adjuntar solo base ORIGINAL t48. Conservar identidad, paleta, ropa y técnica exactas. Ira contenida visible: pañuelo apretado en puño, mano contraria en cintura, cejas tensas desiguales y boca cerrada. Sin gritos ni sonrisa malvada. Solo expresión, gesto y pliegues necesarios.
```


**EN — [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt>)**

```text
EXPRESSION AND GESTURE VARIANT OF THE ATTACHED ORIGINAL APPROVED CHARACTER. The attached Leonora is the SOLE visual authority and edit target. Preserve EXACT same woman, adult face proportions and asymmetry, eyes/nose/mouth construction, heart-shaped red hair silhouette without curls, tiny top hat and veil, pearl studs, black short jacket with three buttons and two short hem points, separate black skirt, white ruffled blouse/cuffs, pale rosy skin and cheek blush. Preserve original local colour with NO warm filter; whites remain white. Preserve handcrafted irregular material-colour outlines, broad gouache paint and simple shadows. Same head size, body proportions, eye level, frontal view, head-to-upper-thigh crop and canvas. Do not beautify, redesign costume, change light, add accessories or create a different person. Change ONLY expression, gesture and physically necessary folds. Correct five-finger anatomy. Transparent background. No scene, text or colour swatches. POSE: visibly FRUSTRATED, CONTAINED ANGER with aristocratic self-control. Lower the handkerchief from face. At upper abdomen she tightly compresses her SAME white handkerchief in her right fist, a small white corner visibly protruding; her left hand is held flat against her waist, elbow slightly outward, fingers gently braced. Hands distinct, not tangled. Shoulders held rigid, chin slightly raised, eyes fixed sternly on judge with one lid tighter, brows drawn down unequally, lips pressed into a small asymmetric line. No shouting, snarling, fangs, villain grin or raised fist. Residual moisture beneath eyes but no theatrical stream of tears. Clear change from the tear-dabbing base, still mysterious and socially superior.
```


### `char_leonora_happy`

Estado del manifiesto: `ready_from_approved_original_only`. Base: [produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/char_leonora-neutral-t48-candidato.png>).


**ES — [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.es.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.es.txt>)**

```text
Adjuntar solo base ORIGINAL t48. Conservar identidad, paleta, ropa y técnica exactas. Gratitud reservada: mano abierta sobre pecho, otra con pañuelo en cintura, leve inclinación y sonrisa cerrada asimétrica. Misterio y dignidad, sin entusiasmo exagerado. Solo expresión, gesto y pliegues necesarios.
```


**EN — [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt>)**

```text
EXPRESSION AND GESTURE VARIANT OF THE ATTACHED ORIGINAL APPROVED CHARACTER. The attached Leonora is the SOLE visual authority and edit target. Preserve EXACT same woman, adult face proportions and asymmetry, eyes/nose/mouth construction, heart-shaped red hair silhouette without curls, tiny top hat and veil, pearl studs, black short jacket with three buttons and two short hem points, separate black skirt, white ruffled blouse/cuffs, pale rosy skin and cheek blush. Preserve original local colour with NO warm filter; whites remain white. Preserve handcrafted irregular material-colour outlines, broad gouache paint and simple shadows. Same head size, body proportions, eye level, frontal view, head-to-upper-thigh crop and canvas. Do not beautify, redesign costume, change light, add accessories or create a different person. Change ONLY expression, gesture and physically necessary folds. Correct five-finger anatomy. Transparent background. No scene, text or colour swatches. POSE: gracious, visibly GRATEFUL but mysterious and aristocratically self-possessed. BOTH hands move away from the base pose: right open hand rests lightly over upper chest below collar, fingers relaxed and individually readable; left hand holds her SAME small white handkerchief loosely at waist, fingers naturally curved. Slight composed inclination of head, shoulders softened, small warm CLOSED-MOUTH asymmetric smile, eyes appreciatively softened but still watchful. A modest grateful nod rather than exaggerated excitement, no broad toothy grin, clasped prayer hands, waving or hearts. No crying expression; a tiny remaining trace of tear is allowed. Distinct warm gesture without abandoning her dignity or ambiguous intentions.
```


### `char_mireya_neutral`

Estado del manifiesto: `review_corrected_original_before_expressions`. Base: [produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png](<produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png>).


**ES — [produccion-arte/mundo-v03/char_mireya_neutral.es.txt](<produccion-arte/mundo-v03/char_mireya_neutral.es.txt>)**

```text
char_mireya_neutral

Mireya Salceda

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Administradora asalariada de Rovena, de familia de la Vega, vive en Arcos Bajos. Maneja rentas ajenas; teme responder por déficits que no controla. Su precisión puede proteger y perjudicar.

Vestido ciruela de lana ligera, delantal de lino lavable, mangas practicables y cuello sencillo de la base aprobada. Compra funcional y conservación; no uniforme de nobleza ni escudo Rovena. La ropa sirve en interiores frescos y trabajo entre edificios.

Conservar piel, canas, ciruela y marfil aprobados; no igualarla con el pigmento de Ivo.

Libro cerrado contra el torso. Anilla de latón y tres llaves unidas a correa de cuero y presilla cosida en cintura del delantal. Verificar geometría visible antes de aceptar; no nace del libro.

Base v2 seleccionada: preservar rostro no idealizado, relación entre nariz, párpados y labios, volumen de cabello y piel original. La corrección de llaves no autoriza corregir facciones.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Libro protegido contra el torso; mirada que verifica.

La corrección de llaves es un encargo técnico separado; C4 y C11 son candidatos, no nuevas aprobaciones. Una base corregida necesita revisión antes de nuevas poses.

Adjuntar SOLO la base v2 de Mireya. Conservar exactamente su identidad y técnica seleccionadas; corregir exclusivamente la conexión de las llaves al cinturón si la inspección confirma el fallo. No regenerar rostro, ropa o paleta. Revisar esta corrección antes de derivar expresiones.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_mireya_neutral.en.txt](<produccion-arte/mundo-v03/char_mireya_neutral.en.txt>)**

```text
char_mireya_neutral

Mireya Salceda

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A salaried Rovena administrator from a Vega family, living in Arcos Bajos. She manages rents she does not own and fears liability for deficits beyond her control. Her precision can protect and harm.

Approved plum lightweight-wool dress, washable linen apron, practical sleeves and simple collar. Functional purchase and upkeep rather than noble uniform or Rovena crest. Suitable for cool interiors and work between buildings.

Preserve approved skin, grey hair, plum and ivory; do not match her pigment to Ivo.

Closed ledger against the torso. Brass ring and three keys attached through a leather fob to a sewn apron-waist keeper. Check visible construction before accepting; it never sprouts from the book.

Selected v2 base: preserve the non-idealised face, nose/lid/lip relationships, hair volume and original skin. Repairing keys never authorises changing features.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Ledger protected against torso; a checking gaze.

Key attachment correction is a separate technical brief; C4 and C11 are candidates, not new approvals. A corrected base requires review before new poses.

Attach ONLY Mireya's v2 base. Preserve her exact selected identity and technique; repair only the keys' belt attachment if inspection confirms the fault. Never regenerate face, clothing or palette. Review this correction before deriving expressions.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_mireya_annoyed`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png](<produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png>).


**ES — [produccion-arte/mundo-v03/char_mireya_annoyed.es.txt](<produccion-arte/mundo-v03/char_mireya_annoyed.es.txt>)**

```text
char_mireya_annoyed

Mireya Salceda

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Administradora asalariada de Rovena, de familia de la Vega, vive en Arcos Bajos. Maneja rentas ajenas; teme responder por déficits que no controla. Su precisión puede proteger y perjudicar.

Vestido ciruela de lana ligera, delantal de lino lavable, mangas practicables y cuello sencillo de la base aprobada. Compra funcional y conservación; no uniforme de nobleza ni escudo Rovena. La ropa sirve en interiores frescos y trabajo entre edificios.

Conservar piel, canas, ciruela y marfil aprobados; no igualarla con el pigmento de Ivo.

Libro cerrado contra el torso. Anilla de latón y tres llaves unidas a correa de cuero y presilla cosida en cintura del delantal. Verificar geometría visible antes de aceptar; no nace del libro.

Base v2 seleccionada: preservar rostro no idealizado, relación entre nariz, párpados y labios, volumen de cabello y piel original. La corrección de llaves no autoriza corregir facciones.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Boca estrecha y presión de dedos sobre el mismo libro; nada de agitar llaves.

La corrección de llaves es un encargo técnico separado; C4 y C11 son candidatos, no nuevas aprobaciones. Una base corregida necesita revisión antes de nuevas poses.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_mireya_annoyed.en.txt](<produccion-arte/mundo-v03/char_mireya_annoyed.en.txt>)**

```text
char_mireya_annoyed

Mireya Salceda

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A salaried Rovena administrator from a Vega family, living in Arcos Bajos. She manages rents she does not own and fears liability for deficits beyond her control. Her precision can protect and harm.

Approved plum lightweight-wool dress, washable linen apron, practical sleeves and simple collar. Functional purchase and upkeep rather than noble uniform or Rovena crest. Suitable for cool interiors and work between buildings.

Preserve approved skin, grey hair, plum and ivory; do not match her pigment to Ivo.

Closed ledger against the torso. Brass ring and three keys attached through a leather fob to a sewn apron-waist keeper. Check visible construction before accepting; it never sprouts from the book.

Selected v2 base: preserve the non-idealised face, nose/lid/lip relationships, hair volume and original skin. Repairing keys never authorises changing features.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Narrower mouth and fingers pressing the same ledger; no key-waving.

Key attachment correction is a separate technical brief; C4 and C11 are candidates, not new approvals. A corrected base requires review before new poses.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_mireya_happy`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png](<produccion-arte/revision-estilo-v2/char_mireya_neutral-v2-prueba.png>).


**ES — [produccion-arte/mundo-v03/char_mireya_happy.es.txt](<produccion-arte/mundo-v03/char_mireya_happy.es.txt>)**

```text
char_mireya_happy

Mireya Salceda

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Administradora asalariada de Rovena, de familia de la Vega, vive en Arcos Bajos. Maneja rentas ajenas; teme responder por déficits que no controla. Su precisión puede proteger y perjudicar.

Vestido ciruela de lana ligera, delantal de lino lavable, mangas practicables y cuello sencillo de la base aprobada. Compra funcional y conservación; no uniforme de nobleza ni escudo Rovena. La ropa sirve en interiores frescos y trabajo entre edificios.

Conservar piel, canas, ciruela y marfil aprobados; no igualarla con el pigmento de Ivo.

Libro cerrado contra el torso. Anilla de latón y tres llaves unidas a correa de cuero y presilla cosida en cintura del delantal. Verificar geometría visible antes de aceptar; no nace del libro.

Base v2 seleccionada: preservar rostro no idealizado, relación entre nariz, párpados y labios, volumen de cabello y piel original. La corrección de llaves no autoriza corregir facciones.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Sonrisa ladeada pequeña; ofrece ver la cubierta del libro sin inventar páginas nuevas.

La corrección de llaves es un encargo técnico separado; C4 y C11 son candidatos, no nuevas aprobaciones. Una base corregida necesita revisión antes de nuevas poses.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_mireya_happy.en.txt](<produccion-arte/mundo-v03/char_mireya_happy.en.txt>)**

```text
char_mireya_happy

Mireya Salceda

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A salaried Rovena administrator from a Vega family, living in Arcos Bajos. She manages rents she does not own and fears liability for deficits beyond her control. Her precision can protect and harm.

Approved plum lightweight-wool dress, washable linen apron, practical sleeves and simple collar. Functional purchase and upkeep rather than noble uniform or Rovena crest. Suitable for cool interiors and work between buildings.

Preserve approved skin, grey hair, plum and ivory; do not match her pigment to Ivo.

Closed ledger against the torso. Brass ring and three keys attached through a leather fob to a sewn apron-waist keeper. Check visible construction before accepting; it never sprouts from the book.

Selected v2 base: preserve the non-idealised face, nose/lid/lip relationships, hair volume and original skin. Repairing keys never authorises changing features.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Small sideways smile; turns the ledger for inspection without inventing new pages.

Key attachment correction is a separate technical brief; C4 and C11 are candidates, not new approvals. A corrected base requires review before new poses.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_ivo_neutral`

Estado del manifiesto: `reuse_or_review_only`. Base: [produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png](<produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_ivo_neutral.es.txt](<produccion-arte/mundo-v03/char_ivo_neutral.es.txt>)**

```text
char_ivo_neutral

Ivo Valcés

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Encuadernador nacido en Valcenda, familia Tiria/Vega, arrendatario de Rovena y proveedor de Mara. Quiere conservar taller y pagar sólo lo debido; explica de más cuando teme no ser tomado en serio.

Camisa ladrillo de lino lavado, chaleco crema de lana ligera con remiendos y cierre heredado. Las mangas recogidas y restos de cola indican oficio, sin añadir delantal nuevo. Reparar sustituye comprar; abrigo exterior fuera del sprite.

Pigmento, pecas, nariz, mentón y cabello de C3 invariables. Su calidez local no es filtro para otros.

Mismo paquete de cuadernillos plegados en ambas manos y mismo corchete del chaleco. La alegría no lo sustituye por una cartera distinta ausente del original.

C3 seleccionada: preservar identidad morena, cabello en masas, nariz y boca particulares, proporción de mandíbula y gesto del original. No afinar, aclarar ni añadir cicatriz para fabricar carácter.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Protege cuadernillos y está a punto de explicar.

C3 aprobado: reutilizar antes de regenerar. No blanquear piel, suavizar rostro ni copiar la cicatriz a otras personas.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_ivo_neutral.en.txt](<produccion-arte/mundo-v03/char_ivo_neutral.en.txt>)**

```text
char_ivo_neutral

Ivo Valcés

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Valcenda-born bookbinder of Tiria/Vega family background, a Rovena tenant and Mara supplier. He wants to keep his workshop and pay only what he owes; he overexplains when afraid of being dismissed.

Washed brick-red linen shirt, light-wool cream waistcoat with patches and inherited fastening. Rolled sleeves and glue traces indicate work without a new apron. Repair substitutes for purchase; outer coat stays outside the sprite.

C3 pigment, freckles, nose, chin and hair remain unchanged. His local warmth is not a filter for others.

The same stack of folded signatures in both hands and the same waistcoat clasp. Happiness does not replace it with a different wallet absent from the original.

Selected C3: retain dark-skinned identity, broad hair masses, distinctive nose and mouth, jaw proportions and original manner. Never narrow, lighten or add a scar to manufacture character.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Protects signatures and is about to explain.

Approved C3: reuse before regeneration. Do not lighten skin, smooth the face or copy the scar to other people.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_ivo_annoyed`

Estado del manifiesto: `test_with_selected_original`. Base: [produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png](<produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_ivo_annoyed.es.txt](<produccion-arte/mundo-v03/char_ivo_annoyed.es.txt>)**

```text
char_ivo_annoyed

Ivo Valcés

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Encuadernador nacido en Valcenda, familia Tiria/Vega, arrendatario de Rovena y proveedor de Mara. Quiere conservar taller y pagar sólo lo debido; explica de más cuando teme no ser tomado en serio.

Camisa ladrillo de lino lavado, chaleco crema de lana ligera con remiendos y cierre heredado. Las mangas recogidas y restos de cola indican oficio, sin añadir delantal nuevo. Reparar sustituye comprar; abrigo exterior fuera del sprite.

Pigmento, pecas, nariz, mentón y cabello de C3 invariables. Su calidez local no es filtro para otros.

Mismo paquete de cuadernillos plegados en ambas manos y mismo corchete del chaleco. La alegría no lo sustituye por una cartera distinta ausente del original.

C3 seleccionada: preservar identidad morena, cabello en masas, nariz y boca particulares, proporción de mandíbula y gesto del original. No afinar, aclarar ni añadir cicatriz para fabricar carácter.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Aprieta el mismo paquete y adelanta poco el peso; boca firme, sin puños amenazantes.

C3 aprobado: reutilizar antes de regenerar. No blanquear piel, suavizar rostro ni copiar la cicatriz a otras personas.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_ivo_annoyed.en.txt](<produccion-arte/mundo-v03/char_ivo_annoyed.en.txt>)**

```text
char_ivo_annoyed

Ivo Valcés

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Valcenda-born bookbinder of Tiria/Vega family background, a Rovena tenant and Mara supplier. He wants to keep his workshop and pay only what he owes; he overexplains when afraid of being dismissed.

Washed brick-red linen shirt, light-wool cream waistcoat with patches and inherited fastening. Rolled sleeves and glue traces indicate work without a new apron. Repair substitutes for purchase; outer coat stays outside the sprite.

C3 pigment, freckles, nose, chin and hair remain unchanged. His local warmth is not a filter for others.

The same stack of folded signatures in both hands and the same waistcoat clasp. Happiness does not replace it with a different wallet absent from the original.

Selected C3: retain dark-skinned identity, broad hair masses, distinctive nose and mouth, jaw proportions and original manner. Never narrow, lighten or add a scar to manufacture character.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Grips the same stack and leans slightly forward; firm mouth, no threatening fists.

Approved C3: reuse before regeneration. Do not lighten skin, smooth the face or copy the scar to other people.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_ivo_happy`

Estado del manifiesto: `test_with_selected_original`. Base: [produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png](<produccion-arte/personajes-lore-C/char_ivo-neutral-C3-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_ivo_happy.es.txt](<produccion-arte/mundo-v03/char_ivo_happy.es.txt>)**

```text
char_ivo_happy

Ivo Valcés

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Encuadernador nacido en Valcenda, familia Tiria/Vega, arrendatario de Rovena y proveedor de Mara. Quiere conservar taller y pagar sólo lo debido; explica de más cuando teme no ser tomado en serio.

Camisa ladrillo de lino lavado, chaleco crema de lana ligera con remiendos y cierre heredado. Las mangas recogidas y restos de cola indican oficio, sin añadir delantal nuevo. Reparar sustituye comprar; abrigo exterior fuera del sprite.

Pigmento, pecas, nariz, mentón y cabello de C3 invariables. Su calidez local no es filtro para otros.

Mismo paquete de cuadernillos plegados en ambas manos y mismo corchete del chaleco. La alegría no lo sustituye por una cartera distinta ausente del original.

C3 seleccionada: preservar identidad morena, cabello en masas, nariz y boca particulares, proporción de mandíbula y gesto del original. No afinar, aclarar ni añadir cicatriz para fabricar carácter.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Sonrisa desigual; presenta el mismo paquete con orgullo de oficio, sin soltarlo en el aire.

C3 aprobado: reutilizar antes de regenerar. No blanquear piel, suavizar rostro ni copiar la cicatriz a otras personas.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_ivo_happy.en.txt](<produccion-arte/mundo-v03/char_ivo_happy.en.txt>)**

```text
char_ivo_happy

Ivo Valcés

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Valcenda-born bookbinder of Tiria/Vega family background, a Rovena tenant and Mara supplier. He wants to keep his workshop and pay only what he owes; he overexplains when afraid of being dismissed.

Washed brick-red linen shirt, light-wool cream waistcoat with patches and inherited fastening. Rolled sleeves and glue traces indicate work without a new apron. Repair substitutes for purchase; outer coat stays outside the sprite.

C3 pigment, freckles, nose, chin and hair remain unchanged. His local warmth is not a filter for others.

The same stack of folded signatures in both hands and the same waistcoat clasp. Happiness does not replace it with a different wallet absent from the original.

Selected C3: retain dark-skinned identity, broad hair masses, distinctive nose and mouth, jaw proportions and original manner. Never narrow, lighten or add a scar to manufacture character.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Uneven smile; presents the same supported stack with professional pride.

Approved C3: reuse before regeneration. Do not lighten skin, smooth the face or copy the scar to other people.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_ines_neutral`

Estado del manifiesto: `blocked_failed_colour_and_paint_test`. Base: [produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png](<produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_ines_neutral.es.txt](<produccion-arte/mundo-v03/char_ines_neutral.es.txt>)**

```text
char_ines_neutral

Inés Corvela

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Cantante y acompañante independiente de Nácar, vive en Arcos Bajos. Trabaja en salones, cobra para sostener a músicos y protege su autonomía. Cercanía afectiva no cancela una obligación.

Chaqueta azul salino de lana ligera bien cortada; pañuelo de seda marfil comprado mediante el comercio de Nácar, no lino de trabajo. Cuatro botones cobre y faldón oscuro. Inversión profesional cuidada, sin convertirla en noble.

Piel cálida individual y azul propio; no copiar la piel de Ivo, la nariz de Leonora o el peinado de Mireya.

Un pañuelo con nudo y dos puntas; cuatro botones cosidos y ojales correspondientes. Sin lentes, piercings, marca en barbilla o adornos nuevos.

Propuesta para neutral nuevo, no cambio de pose: cráneo más redondeado, mandíbula suave, nariz corta con base ancha, boca amplia con arco labial poco marcado; ojos separados de apertura media. Rizos anchos con recogido suelto lateral, distinto de los moños compactos de Leonora y Mara. Conservar tono propio de la candidata; belleza expresiva sin plantilla de modelo.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Enumera con dos dedos y sostiene la mirada; habla como profesional.

C3 aún candidata. En nuevo neutral diferenciar cráneo más redondeado, boca ancha, nariz corta y rizos amplios; evitar el mismo recogido que Leonora y Mara. No generar expresiones hasta elegir base.

Diseñar un neutral nuevo desde cero. Adjuntar los tres originales WebP SOLO como técnica. La candidata previa sirve para comparación editorial y NO se adjunta como autoridad. Resolver las diferencias indicadas en revisión antes de elegir esta base; no copiar accesorios ajenos. No añadir heráldica o patrones sin ficha aprobada.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_ines_neutral.en.txt](<produccion-arte/mundo-v03/char_ines_neutral.en.txt>)**

```text
char_ines_neutral

Inés Corvela

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Independent singer and companion from Nácar, living in Arcos Bajos. Salon work supports her and musicians; she protects her autonomy. Affection does not cancel an obligation.

Well-cut light-wool salt-blue jacket; ivory silk scarf acquired through Nácar trade rather than work linen. Four copper buttons and a dark skirt. Maintained professional investment without making her noble.

Individual warm skin and her own blue; do not copy Ivo skin, Leonora nose or Mireya hair.

One scarf with a knot and two ends; four sewn buttons with corresponding buttonholes. No glasses, piercings, chin mark or new ornaments.

New-neutral proposal, never a pose alteration: rounder skull, soft jaw, short broad-based nose, wide mouth with a shallow lip bow; moderately open, spaced eyes. Broad curls in a loose side gathering, distinct from Leonora and Mara compact updos. Retain the candidate’s own skin tone; expressive appeal without a fashion-model template.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Counts on two fingers while maintaining eye contact; speaks as a professional.

C3 remains a candidate. A new neutral needs a rounder skull, broad mouth, short nose and large curl masses; avoid the same updo as Leonora and Mara. Do not generate expressions before base selection.

Design a new neutral from scratch. Attach the three original WebPs for TECHNIQUE ONLY. The previous candidate is an editorial comparison, not an attached identity authority. Resolve the review notes before selecting this base; never copy others' accessories. No heraldry or patterns without an approved specification.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_ines_annoyed`

Estado del manifiesto: `blocked_failed_colour_and_paint_test`. Base: [produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png](<produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_ines_annoyed.es.txt](<produccion-arte/mundo-v03/char_ines_annoyed.es.txt>)**

```text
char_ines_annoyed

Inés Corvela

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Cantante y acompañante independiente de Nácar, vive en Arcos Bajos. Trabaja en salones, cobra para sostener a músicos y protege su autonomía. Cercanía afectiva no cancela una obligación.

Chaqueta azul salino de lana ligera bien cortada; pañuelo de seda marfil comprado mediante el comercio de Nácar, no lino de trabajo. Cuatro botones cobre y faldón oscuro. Inversión profesional cuidada, sin convertirla en noble.

Piel cálida individual y azul propio; no copiar la piel de Ivo, la nariz de Leonora o el peinado de Mireya.

Un pañuelo con nudo y dos puntas; cuatro botones cosidos y ojales correspondientes. Sin lentes, piercings, marca en barbilla o adornos nuevos.

Propuesta para neutral nuevo, no cambio de pose: cráneo más redondeado, mandíbula suave, nariz corta con base ancha, boca amplia con arco labial poco marcado; ojos separados de apertura media. Rizos anchos con recogido suelto lateral, distinto de los moños compactos de Leonora y Mara. Conservar tono propio de la candidata; belleza expresiva sin plantilla de modelo.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Detiene la enumeración, boca firme y mirada nivelada; las manos no cambian el pañuelo.

C3 aún candidata. En nuevo neutral diferenciar cráneo más redondeado, boca ancha, nariz corta y rizos amplios; evitar el mismo recogido que Leonora y Mara. No generar expresiones hasta elegir base.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_ines_annoyed.en.txt](<produccion-arte/mundo-v03/char_ines_annoyed.en.txt>)**

```text
char_ines_annoyed

Inés Corvela

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Independent singer and companion from Nácar, living in Arcos Bajos. Salon work supports her and musicians; she protects her autonomy. Affection does not cancel an obligation.

Well-cut light-wool salt-blue jacket; ivory silk scarf acquired through Nácar trade rather than work linen. Four copper buttons and a dark skirt. Maintained professional investment without making her noble.

Individual warm skin and her own blue; do not copy Ivo skin, Leonora nose or Mireya hair.

One scarf with a knot and two ends; four sewn buttons with corresponding buttonholes. No glasses, piercings, chin mark or new ornaments.

New-neutral proposal, never a pose alteration: rounder skull, soft jaw, short broad-based nose, wide mouth with a shallow lip bow; moderately open, spaced eyes. Broad curls in a loose side gathering, distinct from Leonora and Mara compact updos. Retain the candidate’s own skin tone; expressive appeal without a fashion-model template.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Stops counting, firm mouth and level gaze; hands do not alter the scarf.

C3 remains a candidate. A new neutral needs a rounder skull, broad mouth, short nose and large curl masses; avoid the same updo as Leonora and Mara. Do not generate expressions before base selection.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_ines_happy`

Estado del manifiesto: `blocked_failed_colour_and_paint_test`. Base: [produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png](<produccion-arte/personajes-lore-C/char_ines-neutral-C3-sin-marca-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_ines_happy.es.txt](<produccion-arte/mundo-v03/char_ines_happy.es.txt>)**

```text
char_ines_happy

Inés Corvela

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Cantante y acompañante independiente de Nácar, vive en Arcos Bajos. Trabaja en salones, cobra para sostener a músicos y protege su autonomía. Cercanía afectiva no cancela una obligación.

Chaqueta azul salino de lana ligera bien cortada; pañuelo de seda marfil comprado mediante el comercio de Nácar, no lino de trabajo. Cuatro botones cobre y faldón oscuro. Inversión profesional cuidada, sin convertirla en noble.

Piel cálida individual y azul propio; no copiar la piel de Ivo, la nariz de Leonora o el peinado de Mireya.

Un pañuelo con nudo y dos puntas; cuatro botones cosidos y ojales correspondientes. Sin lentes, piercings, marca en barbilla o adornos nuevos.

Propuesta para neutral nuevo, no cambio de pose: cráneo más redondeado, mandíbula suave, nariz corta con base ancha, boca amplia con arco labial poco marcado; ojos separados de apertura media. Rizos anchos con recogido suelto lateral, distinto de los moños compactos de Leonora y Mara. Conservar tono propio de la candidata; belleza expresiva sin plantilla de modelo.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Hombros relajados, sonrisa viva y mano libre con gesto musical breve.

C3 aún candidata. En nuevo neutral diferenciar cráneo más redondeado, boca ancha, nariz corta y rizos amplios; evitar el mismo recogido que Leonora y Mara. No generar expresiones hasta elegir base.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_ines_happy.en.txt](<produccion-arte/mundo-v03/char_ines_happy.en.txt>)**

```text
char_ines_happy

Inés Corvela

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Independent singer and companion from Nácar, living in Arcos Bajos. Salon work supports her and musicians; she protects her autonomy. Affection does not cancel an obligation.

Well-cut light-wool salt-blue jacket; ivory silk scarf acquired through Nácar trade rather than work linen. Four copper buttons and a dark skirt. Maintained professional investment without making her noble.

Individual warm skin and her own blue; do not copy Ivo skin, Leonora nose or Mireya hair.

One scarf with a knot and two ends; four sewn buttons with corresponding buttonholes. No glasses, piercings, chin mark or new ornaments.

New-neutral proposal, never a pose alteration: rounder skull, soft jaw, short broad-based nose, wide mouth with a shallow lip bow; moderately open, spaced eyes. Broad curls in a loose side gathering, distinct from Leonora and Mara compact updos. Retain the candidate’s own skin tone; expressive appeal without a fashion-model template.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Relaxed shoulders, lively smile and a brief musical gesture of the free hand.

C3 remains a candidate. A new neutral needs a rounder skull, broad mouth, short nose and large curl masses; avoid the same updo as Leonora and Mara. Do not generate expressions before base selection.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_mara_neutral`

Estado del manifiesto: `review_new_neutral_before_expressions`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_mara_neutral.es.txt](<produccion-arte/mundo-v03/char_mara_neutral.es.txt>)**

```text
char_mara_neutral

Mara Calce

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Impresora y editora nacida en Valcenda, familia mezclada. Encarga encuadernación a Ivo, publica avisos de Mireya y compra relatos a Inés. Quiere informar fuera de salones, pero le cuesta corregir su propia inferencia.

Camisa crema de lino, chaleco de lana azul tinta y delantal lavable con manchas localizadas. Tres botones visibles del chaleco en C4. Buena confección comprada para trabajar y reutilizada, no traje ceremonial.

Azul tinta distingue oficio, no uniforma su piel; luz y contornos locales.

Un lápiz de madera con punta de grafito; una prueba de imprenta sujeta por borde; delantal atado. Ningún broche de sello añadido si falta en base. Las letras finales las renderiza el juego.

Propuesta para neutral nuevo: rostro alargado, mentón estrecho sin punta extrema, nariz recta de puente bajo, labio superior más fino que inferior, ojos algo separados y cejas de distinto arco. Pelo oscuro recogido bajo, menos compacto. No repetir nariz redonda y boca de Inés. Mantener edad adulta y piel propia.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Lápiz preparado y atención adelantada a una respuesta atribuible.

C4 necesita limpiar píxeles del borde inferior antes de importar. Rostro y recogido se aproximan demasiado a otras mujeres: nuevo neutral con cara larga, mentón fino, ojos separados y recogido bajo menos compacto; no retocar poses para fingir otra identidad.

Diseñar un neutral nuevo desde cero. Adjuntar los tres originales WebP SOLO como técnica. La candidata previa sirve para comparación editorial y NO se adjunta como autoridad. Resolver las diferencias indicadas en revisión antes de elegir esta base; no copiar accesorios ajenos. No añadir heráldica o patrones sin ficha aprobada.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_mara_neutral.en.txt](<produccion-arte/mundo-v03/char_mara_neutral.en.txt>)**

```text
char_mara_neutral

Mara Calce

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Valcenda-born printer and editor with mixed family origins. She commissions Ivo, prints Mireya notices and buys Inés accounts. She wants information beyond salons but struggles to correct her own inference.

Cream linen shirt, ink-blue wool waistcoat and washable apron with local ink marks. Three visible C4 waistcoat buttons. Good tailoring bought for work and reused rather than ceremonial dress.

Ink blue distinguishes work rather than tinting her skin; local light and contours.

One wooden graphite pencil; one proof sheet gripped at its edge; tied apron. No seal brooch absent from the base. Final lettering is rendered by the game.

New-neutral proposal: long face, narrow chin without an extreme point, straight low-bridge nose, upper lip thinner than lower, slightly spaced eyes and uneven brow arches. Dark hair gathered low, less compact. Never repeat Inés rounded nose and mouth. Preserve adult age and individual skin colour.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Pencil ready, leaning attention towards an attributable answer.

C4 needs lower-edge stray pixels removed before import. Face and updo resemble other women too closely: a new neutral needs a long face, narrow chin, spaced eyes and a less compact low updo; do not disguise identity changes as pose edits.

Design a new neutral from scratch. Attach the three original WebPs for TECHNIQUE ONLY. The previous candidate is an editorial comparison, not an attached identity authority. Resolve the review notes before selecting this base; never copy others' accessories. No heraldry or patterns without an approved specification.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_mara_annoyed`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_mara_annoyed.es.txt](<produccion-arte/mundo-v03/char_mara_annoyed.es.txt>)**

```text
char_mara_annoyed

Mara Calce

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Impresora y editora nacida en Valcenda, familia mezclada. Encarga encuadernación a Ivo, publica avisos de Mireya y compra relatos a Inés. Quiere informar fuera de salones, pero le cuesta corregir su propia inferencia.

Camisa crema de lino, chaleco de lana azul tinta y delantal lavable con manchas localizadas. Tres botones visibles del chaleco en C4. Buena confección comprada para trabajar y reutilizada, no traje ceremonial.

Azul tinta distingue oficio, no uniforma su piel; luz y contornos locales.

Un lápiz de madera con punta de grafito; una prueba de imprenta sujeta por borde; delantal atado. Ningún broche de sello añadido si falta en base. Las letras finales las renderiza el juego.

Propuesta para neutral nuevo: rostro alargado, mentón estrecho sin punta extrema, nariz recta de puente bajo, labio superior más fino que inferior, ojos algo separados y cejas de distinto arco. Pelo oscuro recogido bajo, menos compacto. No repetir nariz redonda y boca de Inés. Mantener edad adulta y piel propia.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Inmoviliza el lápiz y asegura el pliego; resiste retirar su afirmación.

C4 necesita limpiar píxeles del borde inferior antes de importar. Rostro y recogido se aproximan demasiado a otras mujeres: nuevo neutral con cara larga, mentón fino, ojos separados y recogido bajo menos compacto; no retocar poses para fingir otra identidad.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_mara_annoyed.en.txt](<produccion-arte/mundo-v03/char_mara_annoyed.en.txt>)**

```text
char_mara_annoyed

Mara Calce

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Valcenda-born printer and editor with mixed family origins. She commissions Ivo, prints Mireya notices and buys Inés accounts. She wants information beyond salons but struggles to correct her own inference.

Cream linen shirt, ink-blue wool waistcoat and washable apron with local ink marks. Three visible C4 waistcoat buttons. Good tailoring bought for work and reused rather than ceremonial dress.

Ink blue distinguishes work rather than tinting her skin; local light and contours.

One wooden graphite pencil; one proof sheet gripped at its edge; tied apron. No seal brooch absent from the base. Final lettering is rendered by the game.

New-neutral proposal: long face, narrow chin without an extreme point, straight low-bridge nose, upper lip thinner than lower, slightly spaced eyes and uneven brow arches. Dark hair gathered low, less compact. Never repeat Inés rounded nose and mouth. Preserve adult age and individual skin colour.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Stills the pencil and secures the sheet; resists withdrawing her claim.

C4 needs lower-edge stray pixels removed before import. Face and updo resemble other women too closely: a new neutral needs a long face, narrow chin, spaced eyes and a less compact low updo; do not disguise identity changes as pose edits.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_mara_happy`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_mara-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_mara_happy.es.txt](<produccion-arte/mundo-v03/char_mara_happy.es.txt>)**

```text
char_mara_happy

Mara Calce

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Impresora y editora nacida en Valcenda, familia mezclada. Encarga encuadernación a Ivo, publica avisos de Mireya y compra relatos a Inés. Quiere informar fuera de salones, pero le cuesta corregir su propia inferencia.

Camisa crema de lino, chaleco de lana azul tinta y delantal lavable con manchas localizadas. Tres botones visibles del chaleco en C4. Buena confección comprada para trabajar y reutilizada, no traje ceremonial.

Azul tinta distingue oficio, no uniforma su piel; luz y contornos locales.

Un lápiz de madera con punta de grafito; una prueba de imprenta sujeta por borde; delantal atado. Ningún broche de sello añadido si falta en base. Las letras finales las renderiza el juego.

Propuesta para neutral nuevo: rostro alargado, mentón estrecho sin punta extrema, nariz recta de puente bajo, labio superior más fino que inferior, ojos algo separados y cejas de distinto arco. Pelo oscuro recogido bajo, menos compacto. No repetir nariz redonda y boca de Inés. Mantener edad adulta y piel propia.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Baja el lápiz y comparte el mismo pliego con sonrisa animada.

C4 necesita limpiar píxeles del borde inferior antes de importar. Rostro y recogido se aproximan demasiado a otras mujeres: nuevo neutral con cara larga, mentón fino, ojos separados y recogido bajo menos compacto; no retocar poses para fingir otra identidad.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_mara_happy.en.txt](<produccion-arte/mundo-v03/char_mara_happy.en.txt>)**

```text
char_mara_happy

Mara Calce

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Valcenda-born printer and editor with mixed family origins. She commissions Ivo, prints Mireya notices and buys Inés accounts. She wants information beyond salons but struggles to correct her own inference.

Cream linen shirt, ink-blue wool waistcoat and washable apron with local ink marks. Three visible C4 waistcoat buttons. Good tailoring bought for work and reused rather than ceremonial dress.

Ink blue distinguishes work rather than tinting her skin; local light and contours.

One wooden graphite pencil; one proof sheet gripped at its edge; tied apron. No seal brooch absent from the base. Final lettering is rendered by the game.

New-neutral proposal: long face, narrow chin without an extreme point, straight low-bridge nose, upper lip thinner than lower, slightly spaced eyes and uneven brow arches. Dark hair gathered low, less compact. Never repeat Inés rounded nose and mouth. Preserve adult age and individual skin colour.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Lowers the pencil and shares the same sheet with an animated smile.

C4 needs lower-edge stray pixels removed before import. Face and updo resemble other women too closely: a new neutral needs a long face, narrow chin, spaced eyes and a less compact low updo; do not disguise identity changes as pose edits.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_nilo_neutral`

Estado del manifiesto: `review_new_neutral_before_expressions`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_nilo_neutral.es.txt](<produccion-arte/mundo-v03/char_nilo_neutral.es.txt>)**

```text
char_nilo_neutral

Nilo Lobreda

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Hijo adulto de la duquesa Aldra, de Greda, alojado en Puerta de Greda. Quiere ayudar sin depender del apellido y evita costes propios. Su condición lunar es secreta; ayudar a Bruna no cancela deuda.

Chaqueta ocre de paño, chaleco oliva y camisa clara; alamares serranos expresan procedencia. Capa pizarra de viaje existente: en futuro neutral otoñal más ligera y abierta, no piel de invierno; si una pose usa C4 debe conservarla exactamente. Prefiere ropa resistente aun pudiendo acceder a mejor corte.

Ocre, oliva y pizarra conviven con piel propia; no luna azul sobre todo el rostro.

Broche de capa con dos placas cosidas y gancho, dos alamares del chaleco y anillo liso en el mismo dedo de la base. No añadir luna, colmillos, garras o amuletos.

Propuesta para neutral nuevo: rostro cuadrado blando, mandíbula ancha, nariz ancha de puente corto, cejas bajas bastante rectas, ojos pequeños de mirada atenta y labios de grosor medio. Pelo en mechones grandes, hombros redondeados. Diferenciarlo del rostro más anguloso de Ivo. Ningún rasgo prueba su condición lunar.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Palma abierta ofrece actuar antes de explicarse.

C4 candidata: preservar hombros y redondez sin repetir el cráneo de Ivo. No rediseñar una capa en una expresión.

Diseñar un neutral nuevo desde cero. Adjuntar los tres originales WebP SOLO como técnica. La candidata previa sirve para comparación editorial y NO se adjunta como autoridad. Resolver las diferencias indicadas en revisión antes de elegir esta base; no copiar accesorios ajenos. No añadir heráldica o patrones sin ficha aprobada.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_nilo_neutral.en.txt](<produccion-arte/mundo-v03/char_nilo_neutral.en.txt>)**

```text
char_nilo_neutral

Nilo Lobreda

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Adult son of Duchess Aldra from Greda, lodging at Puerta de Greda. He wants to help without his surname and avoids personal costs. His lunar condition is secret; helping Bruna does not cancel debt.

Ochre cloth jacket, olive waistcoat and pale shirt; mountain frog fastenings convey origin. Existing slate travel cloak: a future autumn neutral can make it lighter and open, not winter fur; any C4 pose must preserve it exactly. He prefers durable clothing despite access to better tailoring.

Ochre, olive and slate coexist with his own skin; no blue moonlight over the whole face.

Cloak clasp with two sewn plates and hook, two waistcoat frog fastenings and plain band on the same base finger. Add no moon, fangs, claws or charms.

New-neutral proposal: softly square face, broad jaw, broad short-bridge nose, low fairly straight brows, small attentive eyes and medium lips. Hair in large locks, rounded shoulders. Distinguish him from Ivo’s more angular face. No feature proves his lunar condition.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Open palm offers action before explanation.

C4 candidate: preserve shoulders and roundness without repeating Ivo skull. Never redesign a cloak in an expression.

Design a new neutral from scratch. Attach the three original WebPs for TECHNIQUE ONLY. The previous candidate is an editorial comparison, not an attached identity authority. Resolve the review notes before selecting this base; never copy others' accessories. No heraldry or patterns without an approved specification.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_nilo_annoyed`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_nilo_annoyed.es.txt](<produccion-arte/mundo-v03/char_nilo_annoyed.es.txt>)**

```text
char_nilo_annoyed

Nilo Lobreda

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Hijo adulto de la duquesa Aldra, de Greda, alojado en Puerta de Greda. Quiere ayudar sin depender del apellido y evita costes propios. Su condición lunar es secreta; ayudar a Bruna no cancela deuda.

Chaqueta ocre de paño, chaleco oliva y camisa clara; alamares serranos expresan procedencia. Capa pizarra de viaje existente: en futuro neutral otoñal más ligera y abierta, no piel de invierno; si una pose usa C4 debe conservarla exactamente. Prefiere ropa resistente aun pudiendo acceder a mejor corte.

Ocre, oliva y pizarra conviven con piel propia; no luna azul sobre todo el rostro.

Broche de capa con dos placas cosidas y gancho, dos alamares del chaleco y anillo liso en el mismo dedo de la base. No añadir luna, colmillos, garras o amuletos.

Propuesta para neutral nuevo: rostro cuadrado blando, mandíbula ancha, nariz ancha de puente corto, cejas bajas bastante rectas, ojos pequeños de mirada atenta y labios de grosor medio. Pelo en mechones grandes, hombros redondeados. Diferenciarlo del rostro más anguloso de Ivo. Ningún rasgo prueba su condición lunar.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Baja la mano ofrecida; tensa mandíbula sin mostrar dientes.

C4 candidata: preservar hombros y redondez sin repetir el cráneo de Ivo. No rediseñar una capa en una expresión.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_nilo_annoyed.en.txt](<produccion-arte/mundo-v03/char_nilo_annoyed.en.txt>)**

```text
char_nilo_annoyed

Nilo Lobreda

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Adult son of Duchess Aldra from Greda, lodging at Puerta de Greda. He wants to help without his surname and avoids personal costs. His lunar condition is secret; helping Bruna does not cancel debt.

Ochre cloth jacket, olive waistcoat and pale shirt; mountain frog fastenings convey origin. Existing slate travel cloak: a future autumn neutral can make it lighter and open, not winter fur; any C4 pose must preserve it exactly. He prefers durable clothing despite access to better tailoring.

Ochre, olive and slate coexist with his own skin; no blue moonlight over the whole face.

Cloak clasp with two sewn plates and hook, two waistcoat frog fastenings and plain band on the same base finger. Add no moon, fangs, claws or charms.

New-neutral proposal: softly square face, broad jaw, broad short-bridge nose, low fairly straight brows, small attentive eyes and medium lips. Hair in large locks, rounded shoulders. Distinguish him from Ivo’s more angular face. No feature proves his lunar condition.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Lowers the offered hand; tightens jaw without baring teeth.

C4 candidate: preserve shoulders and roundness without repeating Ivo skull. Never redesign a cloak in an expression.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_nilo_happy`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_nilo-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_nilo_happy.es.txt](<produccion-arte/mundo-v03/char_nilo_happy.es.txt>)**

```text
char_nilo_happy

Nilo Lobreda

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Hijo adulto de la duquesa Aldra, de Greda, alojado en Puerta de Greda. Quiere ayudar sin depender del apellido y evita costes propios. Su condición lunar es secreta; ayudar a Bruna no cancela deuda.

Chaqueta ocre de paño, chaleco oliva y camisa clara; alamares serranos expresan procedencia. Capa pizarra de viaje existente: en futuro neutral otoñal más ligera y abierta, no piel de invierno; si una pose usa C4 debe conservarla exactamente. Prefiere ropa resistente aun pudiendo acceder a mejor corte.

Ocre, oliva y pizarra conviven con piel propia; no luna azul sobre todo el rostro.

Broche de capa con dos placas cosidas y gancho, dos alamares del chaleco y anillo liso en el mismo dedo de la base. No añadir luna, colmillos, garras o amuletos.

Propuesta para neutral nuevo: rostro cuadrado blando, mandíbula ancha, nariz ancha de puente corto, cejas bajas bastante rectas, ojos pequeños de mirada atenta y labios de grosor medio. Pelo en mechones grandes, hombros redondeados. Diferenciarlo del rostro más anguloso de Ivo. Ningún rasgo prueba su condición lunar.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Abre la palma con calidez y espera respuesta, sin abrazo invasivo.

C4 candidata: preservar hombros y redondez sin repetir el cráneo de Ivo. No rediseñar una capa en una expresión.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_nilo_happy.en.txt](<produccion-arte/mundo-v03/char_nilo_happy.en.txt>)**

```text
char_nilo_happy

Nilo Lobreda

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Adult son of Duchess Aldra from Greda, lodging at Puerta de Greda. He wants to help without his surname and avoids personal costs. His lunar condition is secret; helping Bruna does not cancel debt.

Ochre cloth jacket, olive waistcoat and pale shirt; mountain frog fastenings convey origin. Existing slate travel cloak: a future autumn neutral can make it lighter and open, not winter fur; any C4 pose must preserve it exactly. He prefers durable clothing despite access to better tailoring.

Ochre, olive and slate coexist with his own skin; no blue moonlight over the whole face.

Cloak clasp with two sewn plates and hook, two waistcoat frog fastenings and plain band on the same base finger. Add no moon, fangs, claws or charms.

New-neutral proposal: softly square face, broad jaw, broad short-bridge nose, low fairly straight brows, small attentive eyes and medium lips. Hair in large locks, rounded shoulders. Distinguish him from Ivo’s more angular face. No feature proves his lunar condition.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Opens the palm warmly and waits for an answer rather than imposing an embrace.

C4 candidate: preserve shoulders and roundness without repeating Ivo skull. Never redesign a cloak in an expression.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_saul_neutral`

Estado del manifiesto: `review_new_neutral_before_expressions`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_saul_neutral.es.txt](<produccion-arte/mundo-v03/char_saul_neutral.es.txt>)**

```text
char_saul_neutral

Saúl Veyra

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Capitán de Tiria, miembro no titular de Veyra, vive en Patio de Tiria. Su autoridad depende de procedimientos y pagos, no sólo apellido. Le cuesta rectificarse ante subordinados.

Abrigo civil burdeos de lana, cuello interior carbón, cinturón funcional con hebilla. Corte bien mantenido por oficio y posición; no armadura de desfile ni joyería. Sin capa militar nueva ni espada.

Piel marrón profunda permanece marrón, con sombra local relacionada; burdeos separado de piel. No aclarar para ajustar contraste de UI.

Broche horizontal de metal observado en C4, cintura y presillas continuas; no reemplazarlo por escudo de puerta durante poses. Un portón heráldico sería otro diseño que requiere aprobación.

Propuesta para neutral nuevo: rostro largo y óseo, mandíbula estrecha, pómulos altos, puente nasal largo y punta plana, párpados pesados, boca ancha de labio superior fino. Piel oscura profunda sin aclarar. Pelo corto en pocas masas. Su firmeza viene de la quietud, no de un ceño de villano.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Ajusta un puño, postura medida y mirada reservada.

C4 candidata: rostro largo y huesudo, ojos y boca propios. Insignia descrita anteriormente como puerta no coincide con el dibujo; el prompt debe conservar lo visible.

Diseñar un neutral nuevo desde cero. Adjuntar los tres originales WebP SOLO como técnica. La candidata previa sirve para comparación editorial y NO se adjunta como autoridad. Resolver las diferencias indicadas en revisión antes de elegir esta base; no copiar accesorios ajenos. No añadir heráldica o patrones sin ficha aprobada.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_saul_neutral.en.txt](<produccion-arte/mundo-v03/char_saul_neutral.en.txt>)**

```text
char_saul_neutral

Saúl Veyra

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A Tiria captain and non-titular Veyra member living in Patio de Tiria. Authority depends on procedure and pay rather than surname alone. He struggles to correct himself before subordinates.

Burgundy civilian wool coat, charcoal inner collar and functional buckled belt. Well-maintained tailoring reflects work and standing, not parade armour or jewellery. No new military cloak or sword.

Deep brown skin remains brown with related local shadows; burgundy stays distinct from skin. Do not lighten him to match UI contrast.

The horizontal metal pin seen in C4, with continuous belt and keepers; do not replace it with a gate crest during poses. A heraldic gate would be a separate design requiring approval.

New-neutral proposal: long bony face, narrow jaw, high cheekbones, long nasal bridge and flat tip, heavy lids, broad mouth with a thin upper lip. Deep dark skin without lightening. Short hair in a few masses. Resolve authority through stillness, not a villain’s scowl.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Adjusts a cuff, measured stance and reserved gaze.

C4 candidate: a long bony face with individual eyes and mouth. The previously described gate badge does not match the drawing; prompts must preserve what is visible.

Design a new neutral from scratch. Attach the three original WebPs for TECHNIQUE ONLY. The previous candidate is an editorial comparison, not an attached identity authority. Resolve the review notes before selecting this base; never copy others' accessories. No heraldry or patterns without an approved specification.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_saul_annoyed`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_saul_annoyed.es.txt](<produccion-arte/mundo-v03/char_saul_annoyed.es.txt>)**

```text
char_saul_annoyed

Saúl Veyra

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Capitán de Tiria, miembro no titular de Veyra, vive en Patio de Tiria. Su autoridad depende de procedimientos y pagos, no sólo apellido. Le cuesta rectificarse ante subordinados.

Abrigo civil burdeos de lana, cuello interior carbón, cinturón funcional con hebilla. Corte bien mantenido por oficio y posición; no armadura de desfile ni joyería. Sin capa militar nueva ni espada.

Piel marrón profunda permanece marrón, con sombra local relacionada; burdeos separado de piel. No aclarar para ajustar contraste de UI.

Broche horizontal de metal observado en C4, cintura y presillas continuas; no reemplazarlo por escudo de puerta durante poses. Un portón heráldico sería otro diseño que requiere aprobación.

Propuesta para neutral nuevo: rostro largo y óseo, mandíbula estrecha, pómulos altos, puente nasal largo y punta plana, párpados pesados, boca ancha de labio superior fino. Piel oscura profunda sin aclarar. Pelo corto en pocas masas. Su firmeza viene de la quietud, no de un ceño de villano.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Deja quieta la mano, sostiene mirada y contiene hombros.

C4 candidata: rostro largo y huesudo, ojos y boca propios. Insignia descrita anteriormente como puerta no coincide con el dibujo; el prompt debe conservar lo visible.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_saul_annoyed.en.txt](<produccion-arte/mundo-v03/char_saul_annoyed.en.txt>)**

```text
char_saul_annoyed

Saúl Veyra

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A Tiria captain and non-titular Veyra member living in Patio de Tiria. Authority depends on procedure and pay rather than surname alone. He struggles to correct himself before subordinates.

Burgundy civilian wool coat, charcoal inner collar and functional buckled belt. Well-maintained tailoring reflects work and standing, not parade armour or jewellery. No new military cloak or sword.

Deep brown skin remains brown with related local shadows; burgundy stays distinct from skin. Do not lighten him to match UI contrast.

The horizontal metal pin seen in C4, with continuous belt and keepers; do not replace it with a gate crest during poses. A heraldic gate would be a separate design requiring approval.

New-neutral proposal: long bony face, narrow jaw, high cheekbones, long nasal bridge and flat tip, heavy lids, broad mouth with a thin upper lip. Deep dark skin without lightening. Short hair in a few masses. Resolve authority through stillness, not a villain’s scowl.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Stills the hand, holds the gaze and controls his shoulders.

C4 candidate: a long bony face with individual eyes and mouth. The previously described gate badge does not match the drawing; prompts must preserve what is visible.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_saul_happy`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_saul-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_saul_happy.es.txt](<produccion-arte/mundo-v03/char_saul_happy.es.txt>)**

```text
char_saul_happy

Saúl Veyra

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Capitán de Tiria, miembro no titular de Veyra, vive en Patio de Tiria. Su autoridad depende de procedimientos y pagos, no sólo apellido. Le cuesta rectificarse ante subordinados.

Abrigo civil burdeos de lana, cuello interior carbón, cinturón funcional con hebilla. Corte bien mantenido por oficio y posición; no armadura de desfile ni joyería. Sin capa militar nueva ni espada.

Piel marrón profunda permanece marrón, con sombra local relacionada; burdeos separado de piel. No aclarar para ajustar contraste de UI.

Broche horizontal de metal observado en C4, cintura y presillas continuas; no reemplazarlo por escudo de puerta durante poses. Un portón heráldico sería otro diseño que requiere aprobación.

Propuesta para neutral nuevo: rostro largo y óseo, mandíbula estrecha, pómulos altos, puente nasal largo y punta plana, párpados pesados, boca ancha de labio superior fino. Piel oscura profunda sin aclarar. Pelo corto en pocas masas. Su firmeza viene de la quietud, no de un ceño de villano.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Suelta el puño en gesto explicativo pequeño; boca se suaviza.

C4 candidata: rostro largo y huesudo, ojos y boca propios. Insignia descrita anteriormente como puerta no coincide con el dibujo; el prompt debe conservar lo visible.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_saul_happy.en.txt](<produccion-arte/mundo-v03/char_saul_happy.en.txt>)**

```text
char_saul_happy

Saúl Veyra

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

A Tiria captain and non-titular Veyra member living in Patio de Tiria. Authority depends on procedure and pay rather than surname alone. He struggles to correct himself before subordinates.

Burgundy civilian wool coat, charcoal inner collar and functional buckled belt. Well-maintained tailoring reflects work and standing, not parade armour or jewellery. No new military cloak or sword.

Deep brown skin remains brown with related local shadows; burgundy stays distinct from skin. Do not lighten him to match UI contrast.

The horizontal metal pin seen in C4, with continuous belt and keepers; do not replace it with a gate crest during poses. A heraldic gate would be a separate design requiring approval.

New-neutral proposal: long bony face, narrow jaw, high cheekbones, long nasal bridge and flat tip, heavy lids, broad mouth with a thin upper lip. Deep dark skin without lightening. Short hair in a few masses. Resolve authority through stillness, not a villain’s scowl.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Releases the cuff into a small explanatory gesture; mouth softens.

C4 candidate: a long bony face with individual eyes and mouth. The previously described gate badge does not match the drawing; prompts must preserve what is visible.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_bruna_neutral`

Estado del manifiesto: `review_new_neutral_before_expressions`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_bruna_neutral.es.txt](<produccion-arte/mundo-v03/char_bruna_neutral.es.txt>)**

```text
char_bruna_neutral

Bruna Narel

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Boticaria de Serel, instalada en el Canal. Documenta suministros, protege pacientes y reclama gastos; discreción puede dificultar rendir cuentas. Conoce a Nilo e Inés; saberes prácticos no confirman magia.

Chaqueta verde de lana ligera, camisa clara, chal salvia lavable de lino y delantal de cuero flexible con bolsillos. El chal no es junco áspero: las fibras de Serel para cestería no dictan su ropa. Capas compatibles con otoño fresco y trabajo de botica.

Conservar edad, piel y canas propias. Verde, salvia y ámbar del frasco no deben convertirse en filtro de piel.

Un frasco ámbar con corcho encajado, recibo doblado, alfiler de madera atravesando el chal y cordón familiar unido a presilla del bolsillo. El nudo cotidiano no diagnostica magia.

Propuesta para neutral nuevo: rostro ancho de mejillas llenas, barbilla corta, nariz convexa y redondeada al final, labios pequeños desiguales, ojos estrechos de distinta altura y cejas escasas. Canas agrupadas en mechones amplios. Mantener años y cuerpo; no una joven con pelo gris. Humor seco sin sonrisa caricaturesca permanente.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Sostiene frasco y separa recibo para mirar.

C4 candidata: no rejuvenecer, afinar nariz o convertirla en bruja con decoración. Mantener su volumen distinto de Mara y Saúl.

Diseñar un neutral nuevo desde cero. Adjuntar los tres originales WebP SOLO como técnica. La candidata previa sirve para comparación editorial y NO se adjunta como autoridad. Resolver las diferencias indicadas en revisión antes de elegir esta base; no copiar accesorios ajenos. No añadir heráldica o patrones sin ficha aprobada.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_bruna_neutral.en.txt](<produccion-arte/mundo-v03/char_bruna_neutral.en.txt>)**

```text
char_bruna_neutral

Bruna Narel

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Serel apothecary settled in the Canal district. She documents supplies, protects patients and claims expenses; discretion can hinder accountability. She knows Nilo and Inés; practical knowledge does not establish magic.

Light-wool green jacket, pale shirt, washable sage linen shawl and supple leather pocketed apron. The shawl is not rough reed: Serel basket fibres do not dictate clothing. Layers suit cool autumn and apothecary work.

Preserve her own age, skin and grey hair. Green, sage and vial amber must not become a skin filter.

One amber vial with fitted cork, folded receipt, wooden pin through the shawl and family cord attached to a pocket keeper. An ordinary knot does not diagnose magic.

New-neutral proposal: broad full-cheeked face, short chin, convex nose with rounded tip, small uneven lips, narrow eyes at slightly different heights and sparse brows. Grey hair grouped in broad locks. Preserve age and body; never a young woman with grey hair. Dry humour without a permanent caricature grin.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Supports the vial and separates the receipt for inspection.

C4 candidate: do not rejuvenate, narrow the nose or decorate her into a witch. Keep her volume distinct from Mara and Saúl.

Design a new neutral from scratch. Attach the three original WebPs for TECHNIQUE ONLY. The previous candidate is an editorial comparison, not an attached identity authority. Resolve the review notes before selecting this base; never copy others' accessories. No heraldry or patterns without an approved specification.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_bruna_annoyed`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_bruna_annoyed.es.txt](<produccion-arte/mundo-v03/char_bruna_annoyed.es.txt>)**

```text
char_bruna_annoyed

Bruna Narel

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Boticaria de Serel, instalada en el Canal. Documenta suministros, protege pacientes y reclama gastos; discreción puede dificultar rendir cuentas. Conoce a Nilo e Inés; saberes prácticos no confirman magia.

Chaqueta verde de lana ligera, camisa clara, chal salvia lavable de lino y delantal de cuero flexible con bolsillos. El chal no es junco áspero: las fibras de Serel para cestería no dictan su ropa. Capas compatibles con otoño fresco y trabajo de botica.

Conservar edad, piel y canas propias. Verde, salvia y ámbar del frasco no deben convertirse en filtro de piel.

Un frasco ámbar con corcho encajado, recibo doblado, alfiler de madera atravesando el chal y cordón familiar unido a presilla del bolsillo. El nudo cotidiano no diagnostica magia.

Propuesta para neutral nuevo: rostro ancho de mejillas llenas, barbilla corta, nariz convexa y redondeada al final, labios pequeños desiguales, ojos estrechos de distinta altura y cejas escasas. Canas agrupadas en mechones amplios. Mantener años y cuerpo; no una joven con pelo gris. Humor seco sin sonrisa caricaturesca permanente.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Objetos seguros, boca firme; insiste en el gasto sin gestos de hechizo.

C4 candidata: no rejuvenecer, afinar nariz o convertirla en bruja con decoración. Mantener su volumen distinto de Mara y Saúl.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_bruna_annoyed.en.txt](<produccion-arte/mundo-v03/char_bruna_annoyed.en.txt>)**

```text
char_bruna_annoyed

Bruna Narel

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Serel apothecary settled in the Canal district. She documents supplies, protects patients and claims expenses; discretion can hinder accountability. She knows Nilo and Inés; practical knowledge does not establish magic.

Light-wool green jacket, pale shirt, washable sage linen shawl and supple leather pocketed apron. The shawl is not rough reed: Serel basket fibres do not dictate clothing. Layers suit cool autumn and apothecary work.

Preserve her own age, skin and grey hair. Green, sage and vial amber must not become a skin filter.

One amber vial with fitted cork, folded receipt, wooden pin through the shawl and family cord attached to a pocket keeper. An ordinary knot does not diagnose magic.

New-neutral proposal: broad full-cheeked face, short chin, convex nose with rounded tip, small uneven lips, narrow eyes at slightly different heights and sparse brows. Grey hair grouped in broad locks. Preserve age and body; never a young woman with grey hair. Dry humour without a permanent caricature grin.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Objects remain secure, mouth firm; insists on the expense without spell gestures.

C4 candidate: do not rejuvenate, narrow the nose or decorate her into a witch. Keep her volume distinct from Mara and Saúl.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


### `char_bruna_happy`

Estado del manifiesto: `blocked_until_original_confirmed`. Base: [produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png](<produccion-arte/personajes-lore-C/tanda-C4/char_bruna-neutral-C4-candidato.png>).


**ES — [produccion-arte/mundo-v03/char_bruna_happy.es.txt](<produccion-arte/mundo-v03/char_bruna_happy.es.txt>)**

```text
char_bruna_happy

Bruna Narel

Ilustración artesanal para novela visual. Contornos con variación de presión y pequeñas irregularidades deliberadas; cada borde es más oscuro que su material y en un contacto claro/oscuro domina el borde del material oscuro. Pintura interior sencilla: pocas manchas suaves y sombras localizadas en mejillas, nariz y párpados; ropa con pocos pliegues estructurales, pelo en masas y un brillo sencillo. Sin filtro amarillo, iluminación naranja global, piel plástica, detalle fotográfico, ruido añadido por toda la imagen ni contorno negro uniforme. La piel conserva su color propio. Los referentes enseñan técnica, no prestan rostros, patrones o accesorios.

Boticaria de Serel, instalada en el Canal. Documenta suministros, protege pacientes y reclama gastos; discreción puede dificultar rendir cuentas. Conoce a Nilo e Inés; saberes prácticos no confirman magia.

Chaqueta verde de lana ligera, camisa clara, chal salvia lavable de lino y delantal de cuero flexible con bolsillos. El chal no es junco áspero: las fibras de Serel para cestería no dictan su ropa. Capas compatibles con otoño fresco y trabajo de botica.

Conservar edad, piel y canas propias. Verde, salvia y ámbar del frasco no deben convertirse en filtro de piel.

Un frasco ámbar con corcho encajado, recibo doblado, alfiler de madera atravesando el chal y cordón familiar unido a presilla del bolsillo. El nudo cotidiano no diagnostica magia.

Propuesta para neutral nuevo: rostro ancho de mejillas llenas, barbilla corta, nariz convexa y redondeada al final, labios pequeños desiguales, ojos estrechos de distinta altura y cejas escasas. Canas agrupadas en mechones amplios. Mantener años y cuerpo; no una joven con pelo gris. Humor seco sin sonrisa caricaturesca permanente.

Base seleccionada manda en poses; rasgos propuestos solo para neutral nuevo sin aprobar. Región y linaje no fijan una nariz o belleza universal.

Ofrece el mismo frasco apoyado en palma, sonrisa pequeña de humor seco.

C4 candidata: no rejuvenecer, afinar nariz o convertirla en bruja con decoración. Mantener su volumen distinto de Mara y Saúl.

Adjuntar SOLO el dibujo original de este personaje indicado en el manifiesto. La imagen manda sobre las descripciones cuando hay conflicto: conservar rostro, cabello, anatomía, vestuario, accesorios, colores, técnica y encuadre. Cambiar únicamente expresión y gesto, con pliegues indispensables. No encadenar variantes ni rediseñar. Si la base sigue pendiente de selección, NO ejecutar este encargo.

Sprite individual sin fondo, sin estrado, sin mesa, sin texto ni sombra proyectada sobre un suelo. Objetivo de preparación 1024×1536, no garantía del generador. Mantener manos y objetos íntegros; comprobar alfa real y márgenes al preparar. Para expresiones conservar el encuadre original. No desplazar ni redimensionar la sala para acomodar al personaje.
```


**EN — [produccion-arte/mundo-v03/char_bruna_happy.en.txt](<produccion-arte/mundo-v03/char_bruna_happy.en.txt>)**

```text
char_bruna_happy

Bruna Narel

Handcrafted visual-novel illustration. Pressure-varied contours with small deliberate irregularities; each edge is darker than its own material, and the darker material owns a shared light/dark boundary. Simple interior paint: a few soft washes and local cheek, nose and eyelid shadows; a few structural clothing folds, hair in broad masses with a simple highlight. No yellow filter, global orange lighting, plastic skin, photographic detail, all-over noise or uniform black outline. Preserve individual skin colour. References teach technique, never lend faces, patterns or accessories.

Serel apothecary settled in the Canal district. She documents supplies, protects patients and claims expenses; discretion can hinder accountability. She knows Nilo and Inés; practical knowledge does not establish magic.

Light-wool green jacket, pale shirt, washable sage linen shawl and supple leather pocketed apron. The shawl is not rough reed: Serel basket fibres do not dictate clothing. Layers suit cool autumn and apothecary work.

Preserve her own age, skin and grey hair. Green, sage and vial amber must not become a skin filter.

One amber vial with fitted cork, folded receipt, wooden pin through the shawl and family cord attached to a pocket keeper. An ordinary knot does not diagnose magic.

New-neutral proposal: broad full-cheeked face, short chin, convex nose with rounded tip, small uneven lips, narrow eyes at slightly different heights and sparse brows. Grey hair grouped in broad locks. Preserve age and body; never a young woman with grey hair. Dry humour without a permanent caricature grin.

Selected base governs poses; proposed features apply only to an unapproved new neutral. Region and ancestry never determine a universal nose or beauty standard.

Offers the same palm-supported vial with a small dry smile.

C4 candidate: do not rejuvenate, narrow the nose or decorate her into a witch. Keep her volume distinct from Mara and Saúl.

Attach ONLY this character's original drawing named in the manifest. Where prose conflicts with the image, the image governs: preserve face, hair, anatomy, costume, accessories, colours, technique and framing. Change expression and gesture only, plus indispensable folds. Never chain variants or redesign. If base selection remains pending, DO NOT execute this brief.

Single transparent character sprite, no background, stand, desk, text or cast shadow on a ground plane. Preparation target 1024×1536, not a generator guarantee. Keep hands and props intact; verify real alpha and margins during preparation. Expressions retain original framing. Never shift or resize the room to accommodate a character.
```


## A.5. Otros encargos y prompts de interfaz

- `produccion-arte/prompts/personajes/`: catálogo inglés histórico/activo en documentación anterior; contrastar con las rutas y bloqueos anteriores antes de usar.
- `produccion-arte/mundo-v03/prompts-personajes.json`: catálogo contextual de producción, no aprobación automática de sus diseños.
- `produccion-arte/mundo-v03/elementos.json`: encargos de fondos, objetos, interfaz, casa y evidencias; no afirma que todos estén producidos.
- `produccion-arte/mundo-v03/tanda-51-tribunal-montaje/prompts-props-en.json`: procedencia de candidatos judiciales.
- `diseno-temporada-social/figma/PROMPTS-PARA-FIGMA-AI.md`: encargo para herramienta de diseño; necesita revisión de dirección visual tras el comentario del usuario.
- Las carpetas `historial-prompts`, `prompts-anteriores` y `tanda-*` conservan experimentación. No elegir un archivo sólo por su número o fecha sin leer la decisión que le corresponde.

# Anexo B: reglas completas de autoría

Se incluye la fuente íntegra para no perder requisitos al transferir el proyecto. Sus resúmenes ingleses se conservan. El documento original enlazado sigue siendo la fuente editable.


## Fuente: [REGLAS-CENTRALES-SALVERNA.md](<REGLAS-CENTRALES-SALVERNA.md>)


### Reglas centrales de personajes, escritura y mundo — Salverna

Versión 1, 2026-10-10. Contrato de trabajo para fichas, casos, diálogos y prompts. Consolidación solicitada por el usuario; no aprueba detalles nuevos de lore, rostros ni secretos. Las instrucciones explícitas del usuario y las identidades visuales aprobadas prevalecen.

#### 1. Una persona quiere algo y elige cómo conseguirlo

Todo personaje recurrente debe tener:

- Deseo duradero: qué intenta conservar, alcanzar o evitar perder.
- Petición actual: qué quiere de esta audiencia, de forma concreta.
- Interés material: dinero, trabajo, propiedad, seguridad, acceso o tiempo.
- Interés afectivo/social: dignidad, autonomía, reconocimiento, deseo, lealtad o pertenencia.
- Temor: qué coste personal trata de evitar; no exige un trauma.
- Contradicción: dos valores o deseos que entran en tensión; no una incoherencia arbitraria.
- Límite moral: qué se niega a hacer y qué presión podría acercarlo a ese límite.
- Capacidad de actuar: una iniciativa propia y al menos una habilidad o competencia.
- Vida fuera del conflicto: un gusto, rutina o compromiso que no exista sólo para resolver el caso.

Los adjetivos se traducen en conductas. «Orgullosa» debe explicar, por ejemplo, qué ayuda rechaza, qué pregunta evade o cómo admite un error. Ninguna persona se reduce a profesión, especie, orientación, clase o papel de culpable/víctima.

EN: Give recurring characters enduring wants, a concrete immediate request, material and emotional stakes, fears, conflicting values, boundaries, agency, competence and an ordinary life. Express traits through observable choices.

#### 2. La personalidad organiza la voz

La ficha define:

- Registro habitual, ritmo y longitud de frase.
- Vocabulario ligado a experiencias y oficio, usado con naturalidad.
- Cómo trata a superiores, iguales y personas dependientes de ella.
- Qué hace bajo presión: precisar, atacar, callar, negociar, bromear, repetir o corregirse.
- Qué palabra o asunto evita y por qué.
- Tres muestras breves bilingües: trato habitual, presión y confianza.

La voz puede cambiar con la intimidad y el peligro. No fijar una muletilla en cada frase ni hacer que todos hablen con ingenio aristocrático. Inglés y español conservan intención, subtexto y alcance probatorio; los nombres y hechos no cambian al traducir.

Prueba editorial: ocultar los nombres en una escena importante. Las estrategias y el registro deben aportar pistas sobre quién habla; no exigir que cada frase aislada sea identificable.

EN: Specify register, rhythm, social address, pressure response and bilingual voice samples. Preserve intent and evidential meaning across languages; avoid repetitive catchphrases and a uniform witty voice.

#### 3. El diálogo es una acción

Cada intervención relevante debe hacer al menos una cosa: pedir, resistir, aclarar, ocultar, negociar, provocar, proteger o cambiar una relación. El contexto puede justificar frases cotidianas y silencios; no todas las líneas tienen que entregar una pista.

Antes de escribir una respuesta, definir quién habla, a quién, qué sabe, qué pretende conseguir y qué acaba de escuchar. La respuesta debe reaccionar a la pregunta real. Una confrontación modifica una defensa que el personaje ya sostenía.

Las preguntas disponibles deben distinguir propósitos. No ofrecer tres paráfrasis ni opciones que anuncien siempre la solución correcta. La información decisiva debe poder obtenerse antes del sello; el epílogo no inventa la prueba que faltaba.

EN: Dialogue performs an action and responds to the actual exchange. Choices differ in purpose. Decisive evidence must be available before judgment.

#### 4. Separar verdad, conocimiento y versión oficial

Cada caso distingue:

1. Lo que ocurrió, fijado por autoría.
2. Qué sabe cada participante y cómo lo supo.
3. Qué cree, sospecha, omite o declara cada participante.
4. Qué pruebas puede conocer el jugador y qué demuestra cada una.
5. Qué versión queda en el acta.
6. Qué se publica, qué se rumorea y qué sigue siendo privado.

Una persona no conoce automáticamente el soborno, una prueba ni una conversación privada. Toda transmisión de información necesita una causa. Vestuario, nerviosismo, atractivo o especie no prueban culpabilidad.

No todos necesitan un secreto espectacular. Puede haber una vergüenza, compromiso privado, error o diferencia entre imagen pública y necesidad. No forzar una revelación sobrenatural o traumática en cada arco. Si hay mentira, definir qué protege y qué arriesga si se descubre.

EN: Track author truth, individual knowledge, claims, player evidence, official findings and public information separately. Every transfer of knowledge needs a cause; secrets need not be sensational.

#### 5. Las relaciones tienen historia, intereses y límites

Para cada relación relevante: origen, qué aporta cada parte, qué reclama, dependencia o desigualdad, tensión actual y conducta que puede cambiarla. No basta decir «se odian» o «son amigas».

Personajes recurrentes nuevos: prever al menos dos vínculos causales y tres apariciones útiles como objetivo de campaña. Un papel breve justificado puede tener menos; no inflar el reparto para cumplir una cuota. Las relaciones pueden ser asimétricas y variar sin invertir toda la personalidad.

Un favor no compra afecto automáticamente. Una pareja mantiene intereses y límites propios. Perder un juicio puede generar vergüenza, distancia o cautela; no siempre odio. Ganarlo puede producir alivio, arrogancia o deuda moral; no siempre gratitud.

EN: Relationships have history, reciprocal interests, asymmetry and boundaries. Recurring cast members need purposeful connections and returns; justified cameos are exempt. Favour, affection and obedience are distinct.

#### 6. Los hechos dejan conductas y costes

Toda resolución define quién obtiene algo, quién paga el coste, qué se registra y qué puede reaparecer. Una consecuencia debe poder mostrarse mediante una conducta: pedir copia, retirar crédito, cambiar de intermediario, evitar una visita o traer un testigo.

Usar cambios numéricos con causa identificable. XP, reputación judicial, reputación de casas/personas, dinero y vínculo personal conservan funciones distintas. Una misma decisión puede aumentar unos y reducir otros. No cambiar puntos sólo porque una opción fue cortés.

Las consecuencias graves deben tener causas y señales previas. El alcance se limita a ramas escritas y efectos definidos; no prometer simulación social infinita.

EN: Decisions produce attributable costs, state changes and observable behaviour. Keep progression, public standing, house power, money and personal bonds distinct. Major consequences need prior causes and signals.

#### 7. Identidad visual al servicio del personaje

La ficha fija referencia aprobada, proporciones faciales, silueta, edad aparente adulta, piel, cabello, paleta, ropa y objetos. Describir diferencias en forma y volumen, además del color. Ni belleza uniforme ni rasgos toscos para todo el elenco.

Oficio, recursos, procedencia y gusto personal influyen en el vestuario sin convertirlo en uniforme obligatorio. Cada accesorio debe tener nombre, función y agarre o sujeción plausible. No añadir objetos para llenar espacio.

Tres poses de la misma persona:

- Neutral: forma habitual de ocupar espacio y relacionarse con la autoridad.
- Molesta: defensa corporal propia, acorde con el conflicto.
- Alegre: forma propia de relajarse, celebrar o permitir cercanía.

Cada pose modifica gesto y postura, preservando rostro, vestuario y accesorios. Para generarlas usar siempre la base ORIGINAL aprobada del mismo personaje, no una variante anterior.

Técnica compartida: trazado artesanal, pintura mate y simplificada, textura localizada; contorno más oscuro del color de cada material. En la unión de claro y oscuro domina el borde del material oscuro. Cabello por masas y brillos simples; sin dominante cálida global ni detalle uniforme.

EN: Preserve approved identity while differentiating face construction, silhouette, wardrobe and gesture. Accessories need a purpose and physical attachment. Derive every pose from the original approved base. Share the local-colour outline and handcrafted matte technique without sharing one face.

#### 8. El mundo sostiene los conflictos

Una familia relevante necesita fuente de ingresos/poder, dependencia, obligación, diferencia interna y relación con la justicia. Una ciudad o barrio necesita actividad material, quién vive allí y un conflicto cotidiano que pueda llegar al juzgado.

Cada costumbre nueva debe afectar una conducta, derecho, reputación o intercambio. No ampliar genealogías, razas o mapas sólo para sumar nombres. La capital permite procedencias diversas; evitar asociar una especie a una sola clase, moralidad o profesión.

Lo sobrenatural tiene capacidades, límites, costes y reglas de conocimiento establecidas antes de usarse. No introducir poderes que resuelvan retrospectivamente el caso ni equiparar sospecha de especie con culpa.

EN: Families, places and customs need material and social functions. Capital diversity should be credible. Supernatural rules, limits and knowledge must precede their use in a case.

#### 9. Qué permanece y qué cambia

Identidad estable: nombre/ID, historia fijada, referencia aprobada y rasgos estructurales. Revisión explícita si hay contradicción con una instrucción posterior.

Evolución escrita: intereses inmediatos, estrategias, hábitos, recursos y relaciones pueden cambiar por acontecimientos identificados.

Estado de partida: reputaciones, pruebas conocidas, soborno, sentencia, pareja y escenas vistas pertenecen al guardado. Nunca presentarlos como biografía única ni incrustarlos en la ficha de autor.

Una propuesta nueva se marca como propuesta; un vacío como pendiente. No completar huecos automáticamente para aparentar una ficha terminada. Las reglas se aplican al trabajo nuevo; las fichas existentes se auditan sin borrar sus decisiones válidas.

EN: Separate stable identity, authored development and playthrough state. Mark proposals and unknowns explicitly. Audit existing material without discarding approved decisions.

#### 10. Ficha y revisión antes de producir

Plantilla: memoria-salverna/plantilla-personaje-central.json. Es un instrumento de autoría; no añade una entidad ni significa que su contenido exista.

Orden de trabajo:

1. Recuperar fuentes y decisiones aprobadas.
2. Completar motivación, voz, vínculos y contexto del caso.
3. Comprobar verdad, conocimiento, evidencia y consecuencias.
4. Traducir personalidad a postura, vestuario y accesorios.
5. Redactar inglés y español; mantener IDs estables.
6. Revisar el elenco junto para detectar voces, caras y gestos repetidos.
7. Validar estructura/contenido y registrar cambios de fuentes.
8. Revisar una escena y un montaje real antes de multiplicar casos o poses.

Preguntas de control:

- ¿Qué quiere hoy y qué le cuesta perder?
- ¿Qué hace por decisión propia?
- ¿Qué sabe y qué no puede saber todavía?
- ¿Su respuesta nace de su interés y de la pregunta recibida?
- ¿El jugador puede comprender la prueba antes de decidir?
- ¿Su reacción conserva carácter, incluso si cambia de estrategia?
- ¿Se reconoce la misma persona entre poses y traducciones?
- ¿El regreso demuestra algo que el juicio cambió?

Los validadores comprueban estructura, claves y reglas. La profundidad psicológica, naturalidad del diálogo y coherencia visual requieren lectura y comparación editorial; no se certifican contando campos completos.

EN: Recover sources, write motives and knowledge first, derive visual behaviour, author bilingually, compare the ensemble and review an actual scene. Automated validation does not certify literary or artistic quality.


#### Vestuario: requisito del usuario — 2026-10-11 / User costume requirement
Antes de otro diseño de vestuario consultar produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md (ruta desde raíz). Investigar prendas concretas de época y diseño, nombres de cortes, construcción y simplificación; no resolver identidad añadiendo color, lazos o pliegues arbitrarios. Separar referencia de moda y técnica ilustrada. / Before another costume design, read the linked rule from the workspace root. Research specific period/designer garments, named cuts, construction and simplification; do not substitute colour, bows or arbitrary folds for identity. Separate fashion construction from illustration technique.


#### Peinado, maquillaje y poses: requisito del usuario — 2026-10-11
Antes de nuevos diseños consultar produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md (ruta desde raíz). Investigar referencias identificables de estructura capilar, maquillaje y actuación de videojuegos; registrar función, adaptación y legibilidad móvil. No resolver identidad con pelo de color o gestos genéricos. Conservar la regla de base original exclusiva para expresiones. / Before new designs, consult the linked hair/makeup/acting rule. Research identifiable references, their function, adaptation and mobile readability; no substitute colour/stock gestures for identity. Preserve original-only expression authority.

## Fuente: [produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md](<produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md>)


### Vestuario con referentes identificables / Costume with identifiable references

2026-10-11. Instrucción de método del usuario, vigente / Current user-directed method. No aprueba diseños ni altera biografía / No design approval or biography change.

#### Regla obligatoria antes de otro vestuario / Required before another costume

ES — Investigar prendas de época concretas, diseñadores y vestidos identificables. Usar nombres de cortes y piezas correctos, con fuente y fecha. Un nombre de diseñador solo no es un diseño. No sustituir esta investigación por «vestido elegante», por color de pelo o por acumular términos históricos incompatibles. Primero definir construcción, silueta y sentido para la persona; luego formular el prompt y generar.
EN — Research specific period garments, designers and identifiable dresses. Use correct cut/component names with source and date. A designer's name alone is not a design. Do not replace research with “elegant gown”, hair colour or incompatible historical terms. Establish construction, silhouette and character purpose before prompting or generating.

#### Ficha mínima de vestuario / Minimum costume brief

1. ES — Persona, oficio, medios, ocasión, clima y objetivo social de vestir así. EN — Character, occupation, means, occasion, climate and social purpose.
2. ES — Una prenda principal con nombre, fecha, museo/archivo y enlace. Qué se toma exactamente de ella. EN — One primary garment, name, date, museum/archive and link. Specify exactly what is borrowed.
3. ES — Altura de cintura, forma del cuerpo/corsage, escote, hombro, manga y volumen de falda. EN — Waist height, bodice shape, neckline, shoulder, sleeve and skirt volume.
4. ES — Material y cómo sostiene el corte: rigidez, peso, caída. No pedir brillo fotográfico. EN — Material and structural effect: stiffness, weight, drape. No photographic shine request.
5. ES — Costuras, cierre y soporte del volumen. Explicar dónde se origina cada pliegue necesario. EN — Seams, fastening and volume support. Explain necessary fold origins.
6. ES — Un rasgo dominante legible en móvil; simplificar el resto sin borrar la construcción. EN — One dominant phone-readable feature; simplify the rest without erasing construction.
7. ES — Adaptación a Salverna explícita: no presentar una pieza del siglo XX como histórica del reino. EN — Explicit Salverna adaptation: do not present twentieth-century couture as historical kingdom clothing.
8. ES — Pose ligada a una intención concreta; no saludo/signo V por defecto. Sin lazos, nudos ni cintas colgantes en los próximos encargos, según corrección del usuario. EN — Pose linked to concrete intent, not a default greeting/V sign. No bows, knots or hanging ribbons in subsequent briefs, following user correction.

#### Investigación inicial: prendas y construcción / Initial research: garments and construction

##### HIST-01 — Robe à l'anglaise, ca. 1770

[The Met — C.I.37.66a, b](https://www.metmuseum.org/art/collection/search/82288)

ES — La ficha describe cuerpo ajustado y sobrefalda abierta sobre una falda interior, sin los pliegues dorsales de la robe à la française. Es una familia de construcción concreta: no añadir cintura imperio manteniendo el mismo nombre sin declarar la adaptación.
EN — The record describes a fitted bodice and open overskirt over a petticoat, without the robe à la française's back pleats. A specific construction family: adding an Empire waist requires declaring the adaptation.

Aplicación propuesta / Proposed application: para una profesional de salones, explorar cuerpo definido y contraste entre sobrefalda/falda interior, simplificando ornamento; todavía no seleccionada ni generada / for a salon professional, explore defined bodice and overskirt/petticoat contrast with reduced ornament; not yet selected or generated.

##### DESIGN-01 — Jeanne Lanvin, Robe de Style, ca. 1922

[LACMA — Woman’s Dress (Robe de Style)](https://collections.lacma.org/object/113433)

ES — Prenda de diseñadora identificada, útil como estudio separado de silueta de fiesta. No es vestuario de la época preindustrial ni se incorpora automáticamente al mundo. Requiere análisis visual de la pieza antes de elegir rasgos para un prompt.
EN — Identified designer garment, useful as a separate evening-silhouette study. Not preindustrial dress or automatically part of the world. Requires visual examination before selecting prompt features.

##### DESIGN-02 — Charles James, Clover Leaf, 1953

[The Met — Clover Leaf](https://www.metmuseum.org/art/collection/search/159353)

ES — La ficha explica cuatro capas y un contorno de cuatro lóbulos. Enseña que una silueta reconocible nace de estructura, no de añadir pliegues decorativos. No equivale a recomendar su compleja construcción o lujo para Inés.
EN — The record explains four layers and a four-lobed outline. Shows identifiable silhouette arising from structure rather than decorative folds. Not a recommendation of its complex construction or luxury for Inés.

##### METHOD-01 — Cristóbal Balenciaga, estudio de construcción

[V&A — Learning from The Master](https://www.vam.ac.uk/articles/learning-from-the-master)

ES — El museo estudia prendas originales y señala pocas costuras, mangas kimono y cuellos separados del cuerpo entre sus recursos. Es una lección de patronaje: sencillez aparente puede depender de construcción precisa. No usar «Balenciaga» como palabra mágica ni atribuir todos esos recursos a cualquier vestido.
EN — The museum studies original garments, noting few seams, kimono sleeves and stand-away collars among his techniques. A pattern-cutting lesson: apparent simplicity may depend on precise construction. Do not use “Balenciaga” as a magic word or attribute every feature to every dress.

#### Diagnóstico del trabajo anterior / Previous-work diagnosis

ES — Se mezclaron cintura imperio, cuello retrato y sucesivos accesorios sin escoger y estudiar una prenda rectora. El generador resolvió volumen con fruncidos, envolturas y sombras triangulares. Esto describe nuestros resultados; no demuestra una causa interna del modelo. Cambiar a rosa tampoco construyó personalidad. T16 está rechazada por identidad y t17 sigue candidata, no base aprobada.
EN — Empire waist, portrait neckline and successive accessories were combined without choosing and studying a governing garment. Outputs resolved volume through gathers, wraps and triangular shadows. This describes our results, not a proven internal model mechanism. Pink hair did not establish personality. T16 identity rejected; t17 remains a candidate, not an approved base.

#### Puerta de calidad / Quality gate

ES — Antes de generar: poder señalar la fuente concreta y explicar cuerpo, cierre, volumen y simplificación. Después: comparar con esa estructura, técnica original, proporciones y legibilidad móvil. Si el traje solo se distingue por color, o sus pliegues no tienen origen claro, revisar el diseño. No copiar rostro, pose, accesorios o acabado fotográfico del referente de moda: separar autoridad de construcción y autoridad de ilustración. No nueva generación en esta investigación.
EN — Before generation: identify the source and explain bodice, fastening, volume and simplification. Afterwards: compare structure, original art technique, proportions and mobile readability. Revise if colour is the only distinction or folds lack clear origins. Do not copy a fashion reference's face, pose, accessories or photographic finish: separate construction authority from illustration authority. No generation in this research.

## Fuente: [produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md](<produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md>)


### Peinado, maquillaje y actuación con referentes / Referenced hair, makeup and acting

2026-10-11. Regla de método solicitada por usuario / User-directed method. Complementa REGLA-VESTUARIO-CON-REFERENTES.md y reglas centrales; no aprueba imágenes ni cambia identidades por sí sola / Complements costume and central rules; no automatic image approval or identity changes.

#### 1. Peinado: estructura antes de color / Hair: structure before colour

ES — Antes de un diseño nuevo, escoger un peinado identificable y una fuente visual concreta con nombre, contexto y fecha cuando se conozcan. Definir raya, textura natural, largo, dirección, volumen, recogido, soporte/fijación y silueta frontal/lateral. Indicar qué se adapta al personaje y cómo se simplifica en masas pintadas. Un color llamativo no sustituye esta ficha. No cambiar pelo entre poses; no inventar horquillas o rizos para tapar problemas.
EN — Before a new design, choose an identifiable hairstyle and concrete visual source with name, context and date when known. Specify parting, natural texture, length, direction, volume, arrangement, support/fastening and front/side silhouette. Explain character adaptation and painted-mass simplification. Striking colour does not replace the brief. No hair changes between poses or invented pins/curls to conceal problems.

ES — Nombres para investigar, no sinónimos intercambiables ni propuestas aprobadas: chignon bajo, recogido trenzado, ondas al agua/finger waves, corte à la Titus, rollos laterales. Confirmar ejemplo y época antes de usar el nombre. No llamar finger waves a cualquier cabello ondulado ni à la Titus a cualquier corte corto.
EN — Research terms, not interchangeable synonyms or approved proposals: low chignon, braided updo, finger waves, coiffure à la Titus, side rolls. Verify the example and period before naming it. Wavy hair is not automatically finger waves; a short cut is not automatically à la Titus.

Fuentes iniciales / Initial sources:
- [Versailles — Guess the era: hairstyles](https://en.chateauversailles.fr/sites/default/files/resources/pdf/guess_the_era_hairstyles_-_solutions.pdf): material educativo comparativo de épocas / educational period comparison.
- [V&A — Style and Satire](https://www.vam.ac.uk/blog/shop/style-and-satire): documenta grandes peinados del XVIII y su construcción con postizos, rellenos, pomada y polvo / documents eighteenth-century high coiffures and construction with added hair, pads, pomade and powder.

ES — Estas fuentes no certifican todos los términos de la lista; cada elección requiere su propia comprobación. No adoptar decoración extrema por haberla encontrado en una fuente.
EN — These sources do not verify every listed term; each choice needs its own check. Finding elaborate decoration is not a reason to adopt it.

#### 2. Maquillaje: intención y mapa facial / Makeup: intent and face chart

ES — Definir ocasión y finalidad: actuación escénica, presentación social, protocolo, gusto personal o ausencia de maquillaje. Buscar una referencia identificable y separar convención histórica, adaptación fantástica y técnica de ilustración. Fijar forma de cejas, borde de párpado, posición e intensidad del rubor, forma/color/acabado de labios. Registrar también qué no lleva. No imponer el mismo eyeliner, labios brillantes y sombreado de belleza a todo el elenco.
EN — Define occasion and purpose: stage performance, social presentation, protocol, personal preference or no makeup. Find an identifiable reference and separate historical convention, fantasy adaptation and illustration technique. Specify eyebrow shape, eyelid accents, blush placement/intensity and lip shape/colour/finish, including what is absent. No universal eyeliner, glossy lips or beauty shading.

ES — No confundir pigmento natural de piel, sombra pintada y cosmético. El maquillaje no altera silenciosamente anatomía, profundidad de piel o edad, ni se justifica por origen étnico. Conservar variaciones locales sin filtro global. La paleta y el mapa se mantienen entre expresiones; la pose no cambia un maquillaje completo.
EN — Distinguish natural skin pigment, painted shadow and cosmetics. Makeup must not silently alter anatomy, skin depth or age, or be justified by ethnicity. Preserve local variation without global filters. Keep the palette and face chart across expressions; a pose change does not replace makeup.

Fuente inicial / Initial source:
[V&A — The story of Mary Quant make-up](https://www.vam.ac.uk/articles/the-story-of-mary-quant-make-up). Caso documentado de relación entre diseño de vestuario y cosmética; siglo XX, no autoridad para atribuir ese maquillaje a Salverna ni plantilla que aplicar a Inés / documented relationship between clothing design and cosmetics; twentieth century, not authority for Salverna history or a preset for Inés.

#### 3. Poses de videojuegos: estudiar actuación, no copiar un gesto / Game poses: study acting, not a gesture

ES — Antes de proponer una pose, recuperar una captura, sprite o secuencia concreta del juego elegido. Registrar título, personaje, estado/situación, fuente y fotograma o momento si está disponible. No afirmar análisis de una animación por conocer el nombre del juego. Biblioteca prioritaria de estudio propuesta: Ace Attorney y The Great Ace Attorney para declaración, escucha, presión y recuperación; pendiente de fichas de secuencias verificadas, no afirmar inspección completa.
EN — Before proposing a pose, retrieve a specific screenshot, sprite or sequence from the chosen game. Record title, character, state/situation, source and frame or timestamp when available. Knowing the game title does not establish animation analysis. Proposed priority study library: Ace Attorney and The Great Ace Attorney for testimony, listening, pressure and recovery; verified sequence sheets remain pending, not a completed inspection.

ES — Analizar: verbo/intención, línea de acción, peso, orientación de torso/cabeza, hombros, mirada, manos, silueta, escala del gesto y transición desde/hacia reposo. Distinguir ilustración promocional, retrato de menú, pose de diálogo y reacción breve. Una pose de portada o de combate puede no servir para escuchar detrás de un estrado. Elegir el principio expresivo; construir la actuación del personaje propio.
EN — Analyse verb/intent, line of action, weight, torso/head orientation, shoulders, gaze, hands, silhouette, gesture scale and transitions to/from rest. Distinguish promotional art, menu portrait, dialogue pose and brief reaction. A cover or combat pose may not work while listening behind a stand. Extract the expressive principle and build this character's own acting.

ES — En Salverna comprobar la pose en el bloque real de pantalla 9:16: cara legible, espacio para diálogo, manos dentro de encuadre y sin intersecciones con cuello/ropa. La intención principal debe sobrevivir si el estrado oculta manos. Evitar signos V, saludos, dedos contadores y mano al pecho como automatismos. No prohibir todos los gestos amplios: requieren personalidad y momento que los justifiquen. No usar nerviosismo como prueba automática de mentira.
EN — Check against Salverna's actual 9:16 screen block: readable face, dialogue space, hands in frame and no collar/clothing intersections. Main intent should survive hands hidden by the stand. Avoid default V signs, greetings, counting fingers and chest-touching. Broad gestures are allowed when character and moment justify them. Nervousness does not automatically prove lying.

#### 4. Ficha conjunta antes de generar / Joint pre-generation brief

- ES: identidad y momento narrativo recuperados de ficha; cambios propuestos separados de canon / EN: character and moment recovered from profile; proposals separated from canon.
- ES: referente de vestuario + construcción y adaptación / EN: costume source + construction and adaptation.
- ES: referente de peinado + estructura y simplificación / EN: hair source + structure and simplification.
- ES: referente de maquillaje o ausencia justificada + mapa facial / EN: makeup reference or justified absence + face chart.
- ES: pose concreta estudiada + intención propia + verificación del encuadre / EN: studied concrete pose + own intent + frame check.
- ES: autoridad de técnica ilustrada separada de estas fuentes / EN: illustration-technique authority separate from these sources.
- ES: versiones ES/EN y IDs estables; aprobar base antes de expresiones / EN: ES/EN versions and stable IDs; approve base before expressions.

#### 5. Continuidad de poses / Expression continuity

ES — La regla del original aprobado sigue intacta: para molesta/alegre adjuntar exclusivamente la base original de esa persona, no otras personas ni variantes encadenadas. Los referentes de investigación se usan para decidir y describir la actuación, no se adjuntan como autoridades rivales al cambiar expresión. Si no hay base aprobada, se diseña una candidata nueva con autorización; no se finge continuidad.
EN — Approved-original rule unchanged: annoyed/happy variants attach solely that character's original base, never other characters or chained variants. Research references inform acting choices and wording, not competing visual authorities during expression changes. Without an approved base, an authorised new candidate is designed rather than pretending continuity.

No generación nueva en esta actualización / No new generation in this update.


# Anexo C: mapa documental y procedencia

## C.1. Fuentes de entrada prioritarias

| Área | Fuente |
|---|---|
| Continuidad | `memoria-salverna/LEER-PRIMERO.md`, `decisiones.md`, `entidades.json` |
| Mundo | `BIBLIA-MUNDO-SALVERNA-v0.3.md`, `memoria-salverna/mundo-v0.3.json` |
| Autoría | `REGLAS-CENTRALES-SALVERNA.md`, `perfiles-autoria-v1.json`, `plantilla-personaje-central.json` |
| Calidad | `ESTANDAR-CALIDAD-SALVERNA.md` |
| Diseño social | `diseno-temporada-social/AUDITORIA-DEFINICION-2026-10-13.md` y continuidad del 13 de octubre |
| Diseño anterior | `DISENO-NARRATIVO-Y-MECANICO-v1.md`, histórico donde difiere de decisiones recientes |
| Arte | `produccion-arte/mundo-v03/referencias-y-bloqueos.json` y aprobaciones posteriores |
| Vestuario | `produccion-arte/referencias-vestuario-usuario-2026-10-11/ESTUDIO-VESTUARIO.md` |
| Dispatch visual | `referencias-dispatch/capturas-ui-2026-10-13/ANALISIS-Y-ADAPTACION-MOVIL.md` |
| Runtime | `salverna-game/README.md`, `data/cases.json`, `scripts/game_state.gd`, catálogos |
| UI judicial | `MEJORA-EXPERIENCIA-C16.md` |
| Figma social | `diseno-temporada-social/figma/LEER-PRIMERO.md` y `state.json` |

## C.2. Catálogo de documentación Markdown existente

Catálogo para localizar antecedentes. La presencia aquí **no significa vigencia ni aprobación**. Los documentos pueden contener estados históricos dentro de sus propias páginas. Los títulos son los de cada archivo, no una certificación editorial.


- [Adaptación de ModuLore para la memoria de Salverna](<adaptacion-modulore-salverna.md>) — `adaptacion-modulore-salverna.md`

- [Instrucciones de continuidad — Salverna](<AGENTS.md>) — `AGENTS.md`

- [Análisis de identidad visual de las referencias](<analisis-identidad-visual.md>) — `analisis-identidad-visual.md`

- [Dressmaker: primera inspección de mecánicas y presentación](<analisis-referente-dressmaker-primera-inspeccion.md>) — `analisis-referente-dressmaker-primera-inspeccion.md`

- [Dressmaker → Salverna: segunda inspección](<analisis-referente-dressmaker-segunda-inspeccion.md>) — `analisis-referente-dressmaker-segunda-inspeccion.md`

- [Arco 1 — Lo que una ayuda permite cobrar](<arco-1-guiones-revisados.md>) — `arco-1-guiones-revisados.md`

- [Auditoría crítica C15 — botones, composición y experiencia](<AUDITORIA-CRITICA-C15-BOTONES-Y-EXPERIENCIA.md>) — `AUDITORIA-CRITICA-C15-BOTONES-Y-EXPERIENCIA.md`

- [Auditoría del mundo — geografía, sociedad y diseño visual](<AUDITORIA-MUNDO-GEOGRAFIA-SOCIEDAD-v1.md>) — `AUDITORIA-MUNDO-GEOGRAFIA-SOCIEDAD-v1.md`

- [Auditoría de sistemas y progresión / Systems and progression audit](<AUDITORIA-SISTEMAS-Y-PROGRESION-2026-10-12.md>) — `AUDITORIA-SISTEMAS-Y-PROGRESION-2026-10-12.md`

- [Auditoría UX y de referentes — Las actas de Salverna](<auditoria-ux-referentes-salverna.md>) — `auditoria-ux-referentes-salverna.md`

- [Auditoría del montaje rechazado: composición, construcción y recompensas](<AUDITORIA-VISUAL-C8-RECHAZADO.md>) — `AUDITORIA-VISUAL-C8-RECHAZADO.md`

- [Salverna — biblia de mundo v0.3 / World Bible v0.3](<BIBLIA-MUNDO-SALVERNA-v0.3.md>) — `BIBLIA-MUNDO-SALVERNA-v0.3.md`

- [Biblia narrativa de Salverna — revisión editorial v0.3](<biblia-narrativa-salverna.md>) — `biblia-narrativa-salverna.md`

- [Visual context](<DESIGN.md>) — `DESIGN.md`

- [Dirección dramática v2 — cortesía, deseo y peligro](<DIRECCION-DRAMATICA-v2.md>) — `DIRECCION-DRAMATICA-v2.md`

- [Dirección integral de identidad — Salverna v1](<DIRECCION-INTEGRAL-IDENTIDAD-v1.md>) — `DIRECCION-INTEGRAL-IDENTIDAD-v1.md`

- [Apertura y primer juicio — propuesta v1](<DISENO-APERTURA-Y-PRIMER-JUICIO-v1.md>) — `DISENO-APERTURA-Y-PRIMER-JUICIO-v1.md`

- [Las actas de Salverna — diseño base (título provisional)](<diseno-base-juego-juzgado.md>) — `diseno-base-juego-juzgado.md`

- [Auditoría de definición — temporada social / Definition audit — social season](<diseno-temporada-social/AUDITORIA-DEFINICION-2026-10-13.md>) — `diseno-temporada-social/AUDITORIA-DEFINICION-2026-10-13.md`

- [Temporada social de Salverna — diseño narrativo y mecánico v1 / Social-season narrative and mechanics v1](<diseno-temporada-social/DISENO-NARRATIVO-Y-MECANICO-v1.md>) — `diseno-temporada-social/DISENO-NARRATIVO-Y-MECANICO-v1.md`

- [Salverna — Figma AI design brief](<diseno-temporada-social/figma/BRIEF-PARA-FIGMA-AI.md>) — `diseno-temporada-social/figma/BRIEF-PARA-FIGMA-AI.md`

- [Inventario visual preliminar / Preliminary visual inventory](<diseno-temporada-social/figma/INVENTARIO-VISUAL-PRELIMINAR.md>) — `diseno-temporada-social/figma/INVENTARIO-VISUAL-PRELIMINAR.md`

- [Maqueta de temporada social — estado real](<diseno-temporada-social/figma/LEER-PRIMERO.md>) — `diseno-temporada-social/figma/LEER-PRIMERO.md`

- [Prompts para Figma / Figma prompts](<diseno-temporada-social/figma/PROMPTS-PARA-FIGMA-AI.md>) — `diseno-temporada-social/figma/PROMPTS-PARA-FIGMA-AI.md`

- [Elenco de Valcenda — reparto cerrado del primer prototipo](<elenco-valcenda-prototipo.md>) — `elenco-valcenda-prototipo.md`

- [Estándar de calidad y consistencia — Salverna](<ESTANDAR-CALIDAD-SALVERNA.md>) — `ESTANDAR-CALIDAD-SALVERNA.md`

- [Flujo de audiencia y evidencias — decisión de interfaz v0.2](<flujo-audiencia-y-evidencias.md>) — `flujo-audiencia-y-evidencias.md`

- [Salverna: flujo propuesto y auditoría C14](<FLUJO-Y-AUDITORIA-SALVERNA-2026-10-12.md>) — `FLUJO-Y-AUDITORIA-SALVERNA-2026-10-12.md`

- [Técnica base para personajes de la serie](<guia-tecnica-personajes.md>) — `guia-tecnica-personajes.md`

- [Guion jugable — C1 «El muro antes de la lluvia»](<guion-jugable-caso-01.md>) — `guion-jugable-caso-01.md`

- [Tribunal integrado C14 / Integrated court C14](<INTEGRACION-TRIBUNAL-C14.md>) — `INTEGRACION-TRIBUNAL-C14.md`

- [Tribunal vertical 9:16 — propuesta de interfaz](<interfaz-tribunal-9x16.md>) — `interfaz-tribunal-9x16.md`

- [Intervenciones jugables por caso — propuesta v0.2](<intervenciones-jugables-por-caso.md>) — `intervenciones-jugables-por-caso.md`

- [Auditoría: causas y evidencia](<investigacion-juego-2d/2026-10-11/01-AUDITORIA.md>) — `investigacion-juego-2d/2026-10-11/01-AUDITORIA.md`

- [Cámara y preparación de imágenes](<investigacion-juego-2d/2026-10-11/02-ASSETS.md>) — `investigacion-juego-2d/2026-10-11/02-ASSETS.md`

- [Godot, Android y puesta en escena narrativa](<investigacion-juego-2d/2026-10-11/03-GODOT-Y-NARRATIVA.md>) — `investigacion-juego-2d/2026-10-11/03-GODOT-Y-NARRATIVA.md`

- [Reconstrucción y comprobaciones](<investigacion-juego-2d/2026-10-11/04-PLAN-Y-PRUEBAS.md>) — `investigacion-juego-2d/2026-10-11/04-PLAN-Y-PRUEBAS.md`

- [Fuentes primarias y alcance](<investigacion-juego-2d/2026-10-11/FUENTES.md>) — `investigacion-juego-2d/2026-10-11/FUENTES.md`

- [Salverna: investigación de producción 2D y experiencia narrativa móvil](<investigacion-juego-2d/2026-10-11/LEER-PRIMERO.md>) — `investigacion-juego-2d/2026-10-11/LEER-PRIMERO.md`

- [Las actas de Salverna — biblia de mundo, versión 0.2](<lore-salverna.md>) — `lore-salverna.md`

- [Matriz de diálogo y confrontación — expedientes C2 a C6](<matriz-dialogos-c2-c6.md>) — `matriz-dialogos-c2-c6.md`

- [Salverna — mejora de experiencia C15](<MEJORA-EXPERIENCIA-C15.md>) — `MEJORA-EXPERIENCIA-C15.md`

- [C16 — Experiencia judicial integrada](<MEJORA-EXPERIENCIA-C16.md>) — `MEJORA-EXPERIENCIA-C16.md`

- [Decisiones y estado editorial](<memoria-salverna/decisiones.md>) — `memoria-salverna/decisiones.md`

- [Vestuario y producción gráfica v0.3 — 2026-10-11](<memoria-salverna/LEER-PRIMERO.md>) — `memoria-salverna/LEER-PRIMERO.md`

- [Ficha de personaje](<memoria-salverna/plantilla-personaje.md>) — `memoria-salverna/plantilla-personaje.md`

- [Encargo reutilizable de escritura — Salverna](<memoria-salverna/PROMPT-AUTORIA-BILINGUE.md>) — `memoria-salverna/PROMPT-AUTORIA-BILINGUE.md`

- [Propuesta anterior, sustituida](<minijuegos-inspeccion-judicial.md>) — `minijuegos-inspeccion-judicial.md`

- [Plan C16 — experiencia judicial e identidad de interfaz](<PLAN-C16-EXPERIENCIA-JUDICIAL.md>) — `PLAN-C16-EXPERIENCIA-JUDICIAL.md`

- [Campaña bilingüe y producción escalable — decisión de trabajo](<plan-campana-bilingue-36-personajes.md>) — `plan-campana-bilingue-36-personajes.md`

- [Actualización C12 · 11 de octubre de 2026](<PLAN-MEJORA-SALVERNA.md>) — `PLAN-MEJORA-SALVERNA.md`

- [Plan de producción — prototipo de Las actas de Salverna](<plan-produccion-prototipo.md>) — `plan-produccion-prototipo.md`

- [Textura ilustrada / Illustration texture — GPT Image 2.5](<produccion-arte/auditoria-historial-estilo/GUIA-TEXTURA-IMAGE25-v1.md>) — `produccion-arte/auditoria-historial-estilo/GUIA-TEXTURA-IMAGE25-v1.md`

- [Auditoría del historial de estilo / Style history audit](<produccion-arte/auditoria-historial-estilo/REVISION.md>) — `produccion-arte/auditoria-historial-estilo/REVISION.md`

- [Base artística del tribunal — corrección vigente](<produccion-arte/BASE-ARTISTICA-TRIBUNAL.md>) — `produccion-arte/BASE-ARTISTICA-TRIBUNAL.md`

- [Casa C7 para montaje](<produccion-arte/casa-C7/README.md>) — `produccion-arte/casa-C7/README.md`

- [Comparación de composición — diálogo y elecciones](<produccion-arte/COMPARACION-COMPOSICION-DIALOGOS.md>) — `produccion-arte/COMPARACION-COMPOSICION-DIALOGOS.md`

- [Contrato vigente de capas — tribunal](<produccion-arte/CONTRATO-CAPAS-TRIBUNAL.md>) — `produccion-arte/CONTRATO-CAPAS-TRIBUNAL.md`

- [Corrección vigente de capas](<produccion-arte/direccion-y-montaje.md>) — `produccion-arte/direccion-y-montaje.md`

- [Tanda C6 · tribunal](<produccion-arte/escena-C6/README.md>) — `produccion-arte/escena-C6/README.md`

- [Estados que no necesitan otra generación](<produccion-arte/estados-y-derivados.md>) — `produccion-arte/estados-y-derivados.md`

- [Producción vigente vinculada al mundo v0.3 — 2026-10-11](<produccion-arte/LEER-PRIMERO.md>) — `produccion-arte/LEER-PRIMERO.md`

- [Contrato de arte e interfaz / Art and interface contract](<produccion-arte/mundo-v03/CONTRATO-ARTE-UI.md>) — `produccion-arte/mundo-v03/CONTRATO-ARTE-UI.md`

- [Control de dominante cálida — investigación v0.4](<produccion-arte/mundo-v03/CONTROL-DOMINANTE-CALIDA-v04.md>) — `produccion-arte/mundo-v03/CONTROL-DOMINANTE-CALIDA-v04.md`

- [Estilo de los referentes / Reference style — v0.6](<produccion-arte/mundo-v03/ESTILO-REFERENTES-v06.md>) — `produccion-arte/mundo-v03/ESTILO-REFERENTES-v06.md`

- [Inés Corvela — revisión conceptual v0.4](<produccion-arte/mundo-v03/INES-IDENTIDAD-VISUAL-v04.md>) — `produccion-arte/mundo-v03/INES-IDENTIDAD-VISUAL-v04.md`

- [Producción vigente — mundo v0.3 / Current production — world v0.3](<produccion-arte/mundo-v03/LEER-PRIMERO.md>) — `produccion-arte/mundo-v03/LEER-PRIMERO.md`

- [Personajes y vestuario — mundo v0.3](<produccion-arte/mundo-v03/PERSONAJES-Y-VESTUARIO.md>) — `produccion-arte/mundo-v03/PERSONAJES-Y-VESTUARIO.md`

- [Inés — dirección previa a t17 / Pre-t17 direction](<produccion-arte/mundo-v03/PLAN-INES-POSE-VESTUARIO-t17.md>) — `produccion-arte/mundo-v03/PLAN-INES-POSE-VESTUARIO-t17.md`

- [Reinicio de prueba de técnica y color / Colour and technique test reset](<produccion-arte/mundo-v03/REINICIO-PRUEBA-COLOR-Y-PINTURA-v05.md>) — `produccion-arte/mundo-v03/REINICIO-PRUEBA-COLOR-Y-PINTURA-v05.md`

- [Propuesta visual Inés t15](<produccion-arte/mundo-v03/tanda-15-vestuario-identidad/propuesta.es.md>) — `produccion-arte/mundo-v03/tanda-15-vestuario-identidad/propuesta.es.md`

- [Inés — propuesta visual t16](<produccion-arte/mundo-v03/tanda-16-fiesta-rosa/propuesta.es.md>) — `produccion-arte/mundo-v03/tanda-16-fiesta-rosa/propuesta.es.md`

- [Inés — propuesta t17](<produccion-arte/mundo-v03/tanda-17-ines-profesional/direccion.es.md>) — `produccion-arte/mundo-v03/tanda-17-ines-profesional/direccion.es.md`

- [Inés t18 — ficha de diseño / Design brief](<produccion-arte/mundo-v03/tanda-18-referentes-investigados/FICHA-DISENO-BILINGUE.md>) — `produccion-arte/mundo-v03/tanda-18-referentes-investigados/FICHA-DISENO-BILINGUE.md`

- [Técnica propuesta t19](<produccion-arte/mundo-v03/tanda-19-lapiz-gouache/tecnica.es.md>) — `produccion-arte/mundo-v03/tanda-19-lapiz-gouache/tecnica.es.md`

- [Prueba t21: formas recortadas pintadas](<produccion-arte/mundo-v03/tanda-21-formas-recortadas/tecnica.es.md>) — `produccion-arte/mundo-v03/tanda-21-formas-recortadas/tecnica.es.md`

- [Color t22 — aprobación de alcance limitado / Scoped colour approval](<produccion-arte/mundo-v03/tanda-22-tintas-sin-luz/COLOR-APROBADO.md>) — `produccion-arte/mundo-v03/tanda-22-tintas-sin-luz/COLOR-APROBADO.md`

- [t22: tintas de color local sin luz ambiental](<produccion-arte/mundo-v03/tanda-22-tintas-sin-luz/tecnica.es.md>) — `produccion-arte/mundo-v03/tanda-22-tintas-sin-luz/tecnica.es.md`

- [t23: trazado con canto de pincel](<produccion-arte/mundo-v03/tanda-23-trazo-pincel-canto/tecnica.es.md>) — `produccion-arte/mundo-v03/tanda-23-trazo-pincel-canto/tecnica.es.md`

- [t24: muestras visuales reales de técnica](<produccion-arte/mundo-v03/tanda-24-muestras-visuales/tecnica.es.md>) — `produccion-arte/mundo-v03/tanda-24-muestras-visuales/tecnica.es.md`

- [t25: muestras de dibujo aisladas](<produccion-arte/mundo-v03/tanda-25-muestras-aisladas/tecnica.es.md>) — `produccion-arte/mundo-v03/tanda-25-muestras-aisladas/tecnica.es.md`

- [Leonora — nueva candidata con dirección t25](<produccion-arte/mundo-v03/tanda-26-leonora/ficha-propuesta.es.md>) — `produccion-arte/mundo-v03/tanda-26-leonora/ficha-propuesta.es.md`

- [Leonora t27 — rediseño autorizado](<produccion-arte/mundo-v03/tanda-27-leonora-redisenada/ficha-propuesta.es.md>) — `produccion-arte/mundo-v03/tanda-27-leonora-redisenada/ficha-propuesta.es.md`

- [Leonora t28 — coherencia del elenco y construcción de época](<produccion-arte/mundo-v03/tanda-28-leonora-coherencia/ficha-propuesta.es.md>) — `produccion-arte/mundo-v03/tanda-28-leonora-coherencia/ficha-propuesta.es.md`

- [Corrección: ropa para comparecer / Correction: clothing for a hearing](<produccion-arte/mundo-v03/tanda-29-elenco-beta/COMPARECENCIA-Y-REDISENO.md>) — `produccion-arte/mundo-v03/tanda-29-elenco-beta/COMPARECENCIA-Y-REDISENO.md`

- [Control obligatorio de continuidad cromática / Required colour continuity control](<produccion-arte/mundo-v03/tanda-29-elenco-beta/CONTROL-COLOR.md>) — `produccion-arte/mundo-v03/tanda-29-elenco-beta/CONTROL-COLOR.md`

- [Leonora — reconstrucción controlada / Controlled reconstruction](<produccion-arte/mundo-v03/tanda-42-leonora-diseno-controlado/ESTUDIO-Y-DISENO.md>) — `produccion-arte/mundo-v03/tanda-42-leonora-diseno-controlado/ESTUDIO-Y-DISENO.md`

- [Corrección C2, 2026-10-11](<produccion-arte/personajes-lore-C/REVISION-C2.md>) — `produccion-arte/personajes-lore-C/REVISION-C2.md`

- [Rechazo C2 y prueba individual C3](<produccion-arte/personajes-lore-C/REVISION-C3.md>) — `produccion-arte/personajes-lore-C/REVISION-C3.md`

- [Tanda C2: personajes para prueba](<produccion-arte/personajes-lore-C/TANDA-C2.md>) — `produccion-arte/personajes-lore-C/TANDA-C2.md`

- [Tanda C3: calidad elegida de Ivo y nuevas identidades](<produccion-arte/personajes-lore-C/TANDA-C3.md>) — `produccion-arte/personajes-lore-C/TANDA-C3.md`

- [Tanda C4: cinco bases restantes](<produccion-arte/personajes-lore-C/tanda-C4/LEER-PRIMERO.md>) — `produccion-arte/personajes-lore-C/tanda-C4/LEER-PRIMERO.md`

- [Identidad visual y referencias — versión vigente v3](<produccion-arte/personajes-y-referencias.md>) — `produccion-arte/personajes-y-referencias.md`

- [Plantilla C: espacios antes de ilustrar](<produccion-arte/plantilla-bloques-C/LEER-PRIMERO.md>) — `produccion-arte/plantilla-bloques-C/LEER-PRIMERO.md`

- [Elenco C5 — 24 poses](<produccion-arte/poses-elenco-C5/LEER-PRIMERO.md>) — `produccion-arte/poses-elenco-C5/LEER-PRIMERO.md`

- [Estudio de vestuario / Costume study](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ESTUDIO-VESTUARIO.md>) — `produccion-arte/referencias-vestuario-usuario-2026-10-11/ESTUDIO-VESTUARIO.md`

- [Peinado, maquillaje y actuación con referentes / Referenced hair, makeup and acting](<produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md>) — `produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md`

- [Vestuario con referentes identificables / Costume with identifiable references](<produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md>) — `produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md`

- [Control de color y calidad de assets — C11](<produccion-arte/revision-color-C11/ESTUDIO-Y-PROTOCOLO.md>) — `produccion-arte/revision-color-C11/ESTUDIO-Y-PROTOCOLO.md`

- [Revisión de color C11 — cinco candidatos](<produccion-arte/revision-color-C11/LEER-PRIMERO.md>) — `produccion-arte/revision-color-C11/LEER-PRIMERO.md`

- [Revisión artística v2 — 2026-10-10](<produccion-arte/revision-estilo-v2/REVISION.md>) — `produccion-arte/revision-estilo-v2/REVISION.md`

- [Recursos jugables generados](<produccion-arte/revision-estilo-v3/ASSETS-JUGABLES-GENERADOS.md>) — `produccion-arte/revision-estilo-v3/ASSETS-JUGABLES-GENERADOS.md`

- [Dirección de sala vigente — corrección del usuario](<produccion-arte/revision-estilo-v3/CORRECCION-DIRECCION-JUDICIAL.md>) — `produccion-arte/revision-estilo-v3/CORRECCION-DIRECCION-JUDICIAL.md`

- [Generación de neutrales — candidatos v3](<produccion-arte/revision-estilo-v3/GENERACION-NEUTRALES.md>) — `produccion-arte/revision-estilo-v3/GENERACION-NEUTRALES.md`

- [Identidad, atractivo y accesorios — revisión v3](<produccion-arte/revision-estilo-v3/IDENTIDAD-Y-ACCESORIOS.md>) — `produccion-arte/revision-estilo-v3/IDENTIDAD-Y-ACCESORIOS.md`

- [Estudio de UI móvil aplicado a Salverna — C12](<produccion-arte/revision-ui-C12/ESTUDIO-UI-Y-APLICACION.md>) — `produccion-arte/revision-ui-C12/ESTUDIO-UI-Y-APLICACION.md`

- [Revisión UI C12](<produccion-arte/revision-ui-C12/LEER-PRIMERO.md>) — `produccion-arte/revision-ui-C12/LEER-PRIMERO.md`

- [Fantasía más visible — propuesta visual, no canon aprobado](<produccion-arte/revision-ui-C12/PROPUESTA-LINAJES-VISUALES.md>) — `produccion-arte/revision-ui-C12/PROPUESTA-LINAJES-VISUALES.md`

- [Sala de Arcos Bajos — dirección corregida por el usuario](<produccion-arte/SALA-ARCOS-BAJOS-DIRECCION-V4.md>) — `produccion-arte/SALA-ARCOS-BAJOS-DIRECCION-V4.md`

- [Corrección de autoridad visual v2 — 2026-10-10](<produccion-arte/TANDA-1.md>) — `produccion-arte/TANDA-1.md`

- [Prioridad vigente: arquitectura por capas](<produccion-arte/tanda-prueba-visual/LEER-PRIMERO.md>) — `produccion-arte/tanda-prueba-visual/LEER-PRIMERO.md`

- [Tanda v6 — cámara común y recursos generados](<produccion-arte/tanda-prueba-visual/TANDA-V6-CAMARA.md>) — `produccion-arte/tanda-prueba-visual/TANDA-V6-CAMARA.md`

- [Product context](<PRODUCT.md>) — `PRODUCT.md`

- [Propuesta narrativa R1 — La moneda de la muerta / The Dead Woman's Coin](<PROPUESTA-CASOS-CON-IDENTIDAD-R1.md>) — `PROPUESTA-CASOS-CON-IDENTIDAD-R1.md`

- [Candy Crush: referencias de diagramación / Layout references](<referencias-candy-crush/ANALISIS-DIAGRAMACION.md>) — `referencias-candy-crush/ANALISIS-DIAGRAMACION.md`

- [Inspección de Plugins y misiones — 2026-10-12](<referencias-dispatch/ANALISIS-EPISODIOS-PLUGINS.md>) — `referencias-dispatch/ANALISIS-EPISODIOS-PLUGINS.md`

- [Inspección de Dispatch — 2026-10-12](<referencias-dispatch/ANALISIS-MECANICAS-2026-10-12.md>) — `referencias-dispatch/ANALISIS-MECANICAS-2026-10-12.md`

- [Narrativa y tutoriales del referente — inspección 2026-10-12](<referencias-dispatch/ANALISIS-NARRATIVA-TUTORIALES-SHARED.md>) — `referencias-dispatch/ANALISIS-NARRATIVA-TUTORIALES-SHARED.md`

- [Dispatch — análisis de ocho capturas y adaptación móvil](<referencias-dispatch/capturas-ui-2026-10-13/ANALISIS-Y-ADAPTACION-MOVIL.md>) — `referencias-dispatch/capturas-ui-2026-10-13/ANALISIS-Y-ADAPTACION-MOVIL.md`

- [Reglas centrales de personajes, escritura y mundo — Salverna](<REGLAS-CENTRALES-SALVERNA.md>) — `REGLAS-CENTRALES-SALVERNA.md`

- [Aplicación de reglas centrales — revisión editorial v1](<revision-autoria-dialogos-prompts-v1.md>) — `revision-autoria-dialogos-prompts-v1.md`

- [Salverna: revisión del plan y programación v2](<revision-plan-programacion-v2.md>) — `revision-plan-programacion-v2.md`

- [Revisión independiente con Sol 6.1: interés y monetización móvil](<revision-sol61-interes-y-monetizacion.md>) — `revision-sol61-interes-y-monetizacion.md`

- [Maqueta Figma — Salverna](<salverna-game/design/LEER-PRIMERO.md>) — `salverna-game/design/LEER-PRIMERO.md`

- [Prueba jugable C7](<salverna-game/PRUEBA-EXPERIENCIA-C7.md>) — `salverna-game/PRUEBA-EXPERIENCIA-C7.md`

- [Prueba visual B — propuesta aplicada](<salverna-game/PRUEBA-VISUAL.md>) — `salverna-game/PRUEBA-VISUAL.md`

- [Current revision / Revisión actual v2 — 2026-10-10](<salverna-game/qa/verification.md>) — `salverna-game/qa/verification.md`

- [Current playable entry / Entrada jugable vigente — 2026-10-12](<salverna-game/README.md>) — `salverna-game/README.md`

- [C10 — primera entrega del plan: composición](<salverna-game/studies/c10/LEER-PRIMERO.md>) — `salverna-game/studies/c10/LEER-PRIMERO.md`

- [Prueba de arte y composición C11](<salverna-game/studies/c11/LEER-PRIMERO.md>) — `salverna-game/studies/c11/LEER-PRIMERO.md`

- [C12 — jerarquía y escala del tribunal](<salverna-game/studies/c12/LEER-PRIMERO.md>) — `salverna-game/studies/c12/LEER-PRIMERO.md`

- [C13 — Arte y audiencia / Art and hearing](<salverna-game/studies/c13/LEER-PRIMERO.md>) — `salverna-game/studies/c13/LEER-PRIMERO.md`

- [Ajuste de lectura solicitado después de C9](<salverna-game/studies/c9/LEER-PRIMERO.md>) — `salverna-game/studies/c9/LEER-PRIMERO.md`

- [Las actas de Salverna — mecánicas y balance del prototipo v0.1](<sistema-jugable-y-balance.md>) — `sistema-jugable-y-balance.md`

- [Sistema de puntos, reputación y acceso a casos — versión 0.1](<sistema-puntos-y-rangos.md>) — `sistema-puntos-y-rangos.md`

- [Temporada 1 — seis expedientes de Valcenda, guion de prototipo v0.1](<temporada-1-seis-casos.md>) — `temporada-1-seis-casos.md`

- [Valcenda: atlas social y visual — versión 0.1](<valcenda-atlas-social-visual.md>) — `valcenda-atlas-social-visual.md`


## C.3. Fuentes incorporadas literalmente o por campos

SHA-256 al compilar esta entrega. Permiten detectar si una fuente cambió después de esta fotografía documental. No sustituyen una nueva lectura ni certifican coherencia editorial.

| Fuente | SHA-256 |
|---|---|

| [BIBLIA-MUNDO-SALVERNA-v0.3.md](<BIBLIA-MUNDO-SALVERNA-v0.3.md>) | `3b6958309558d66735cf4ef33ba99c9831ffe2c45326bf5e591d67241f7ec68c` |

| [REGLAS-CENTRALES-SALVERNA.md](<REGLAS-CENTRALES-SALVERNA.md>) | `2a51b8d80dfbbec93f496025e08d25e420a484bb4b8a94b5aced29893fa6c504` |

| [memoria-salverna/casos.json](<memoria-salverna/casos.json>) | `aecec0077ba2d8086c389ec6e9c24cbf9219aff124da0d5125ef4c2f850fbfc7` |

| [memoria-salverna/entidades.json](<memoria-salverna/entidades.json>) | `c4bb6c1dded470d4961e9cb97b1ba11455894f06036069b576a0392532c8e599` |

| [memoria-salverna/perfiles-autoria-v1.json](<memoria-salverna/perfiles-autoria-v1.json>) | `fbf745a3ac453da8c31a0a09dedb2bcc21c8aa087978ffb205ae659fcc682e97` |

| [produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md](<produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md>) | `f86b067f2b8d29c44435d9cf4d0b8f1f019de79862902f2a8395832908864ee2` |

| [produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md](<produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md>) | `ab68beada090043df100a51291da7a4e70651cb1ce09b8136a77477c0324af2f` |

| [produccion-arte/mundo-v03/char_bruna_annoyed.en.txt](<produccion-arte/mundo-v03/char_bruna_annoyed.en.txt>) | `79bba5a885fba02cd523dd2408fff245ebb148521482e03be7cb23f8cd204303` |

| [produccion-arte/mundo-v03/char_bruna_annoyed.es.txt](<produccion-arte/mundo-v03/char_bruna_annoyed.es.txt>) | `f2be11b2e4ae7e0307001f44ac0e12ea64a46220500d9d3de5f867b9bb6f9946` |

| [produccion-arte/mundo-v03/char_bruna_happy.en.txt](<produccion-arte/mundo-v03/char_bruna_happy.en.txt>) | `4a6656537eca8a769e37963eeb138e7af605c52e9747413d4ee74bb2f7052c20` |

| [produccion-arte/mundo-v03/char_bruna_happy.es.txt](<produccion-arte/mundo-v03/char_bruna_happy.es.txt>) | `c859ee565cfa8d639e22f8da332f3a0e339187c1c3795dfa48589882366e60b0` |

| [produccion-arte/mundo-v03/char_bruna_neutral.en.txt](<produccion-arte/mundo-v03/char_bruna_neutral.en.txt>) | `5a29b79dd963e22786994bfdac56f686148cdec5c23e76c7c2daebbd3bffd77e` |

| [produccion-arte/mundo-v03/char_bruna_neutral.es.txt](<produccion-arte/mundo-v03/char_bruna_neutral.es.txt>) | `d3273f05e9d64474e790db3106f6e62f3317a028122a3c9dbba6af859314b60f` |

| [produccion-arte/mundo-v03/char_ines_annoyed.en.txt](<produccion-arte/mundo-v03/char_ines_annoyed.en.txt>) | `c115764d377a56eccf59eed7ddc0578445a1efd64f70540a5bf5a00aaea60933` |

| [produccion-arte/mundo-v03/char_ines_annoyed.es.txt](<produccion-arte/mundo-v03/char_ines_annoyed.es.txt>) | `54c61d04428275f0869d111cfe00851b631a6b8b92db3ac46600acb706609312` |

| [produccion-arte/mundo-v03/char_ines_happy.en.txt](<produccion-arte/mundo-v03/char_ines_happy.en.txt>) | `4d5e691da01fb0a5724b2783a38bd0072b5585b5ae8fababb42d9bd7ebbc0825` |

| [produccion-arte/mundo-v03/char_ines_happy.es.txt](<produccion-arte/mundo-v03/char_ines_happy.es.txt>) | `0eb5c27d1c78cb400e5763f24b15c919190be1163a88647ad6d0572c6c6e72ff` |

| [produccion-arte/mundo-v03/char_ines_neutral.en.txt](<produccion-arte/mundo-v03/char_ines_neutral.en.txt>) | `6446d3fed2832767f54457d69df85f2b41dd0d781a0baf92859953cf88c95c07` |

| [produccion-arte/mundo-v03/char_ines_neutral.es.txt](<produccion-arte/mundo-v03/char_ines_neutral.es.txt>) | `cb0728143bd19a6c610f8c449febf16c984a199f8df0c2d593637aa930ce3ab6` |

| [produccion-arte/mundo-v03/char_ivo_annoyed.en.txt](<produccion-arte/mundo-v03/char_ivo_annoyed.en.txt>) | `a1c6599f2a49877ce9d2c3009087c243b9db097c2bcbe7c4b7067b3ca566dfb2` |

| [produccion-arte/mundo-v03/char_ivo_annoyed.es.txt](<produccion-arte/mundo-v03/char_ivo_annoyed.es.txt>) | `c3debe2b9f9ca51516154d4cc731e74d556a677f94182e980f33ddf4f36f30c0` |

| [produccion-arte/mundo-v03/char_ivo_happy.en.txt](<produccion-arte/mundo-v03/char_ivo_happy.en.txt>) | `829b9a9c123fe2463c6de3b3b86cf6f3b0e55e9c3590291b1325c31f2583db9a` |

| [produccion-arte/mundo-v03/char_ivo_happy.es.txt](<produccion-arte/mundo-v03/char_ivo_happy.es.txt>) | `795dd3c7cbf7edd18025fe1893addc248e1e0ad2896ede79f6c61e9b19040c9e` |

| [produccion-arte/mundo-v03/char_ivo_neutral.en.txt](<produccion-arte/mundo-v03/char_ivo_neutral.en.txt>) | `ab86e227cf8cf68da9d0edb36295eb468bee48ddf8509b9fb0bb1479bba2f4ae` |

| [produccion-arte/mundo-v03/char_ivo_neutral.es.txt](<produccion-arte/mundo-v03/char_ivo_neutral.es.txt>) | `058e26894ddeca42cc5f0744f88f596c0187834c22885898b182fe2f5175f65c` |

| [produccion-arte/mundo-v03/char_leonora_neutral.en.txt](<produccion-arte/mundo-v03/char_leonora_neutral.en.txt>) | `873ccb09caaa0e0b0b7a10491db18611e709fbcd4e6459b31adeea9c8a79cb92` |

| [produccion-arte/mundo-v03/char_leonora_neutral.es.txt](<produccion-arte/mundo-v03/char_leonora_neutral.es.txt>) | `96757270ffa3c812ee59826d5afa83c3ac85148730333212a4f013231812140d` |

| [produccion-arte/mundo-v03/char_mara_annoyed.en.txt](<produccion-arte/mundo-v03/char_mara_annoyed.en.txt>) | `70acaed573ca5073206bc9622c28b40dbf6fcaa7a82c579f156c42981963a0bd` |

| [produccion-arte/mundo-v03/char_mara_annoyed.es.txt](<produccion-arte/mundo-v03/char_mara_annoyed.es.txt>) | `14c6afec0459620e820837c9e73775558c023cce4ffa1d0fa5780698d5560d5a` |

| [produccion-arte/mundo-v03/char_mara_happy.en.txt](<produccion-arte/mundo-v03/char_mara_happy.en.txt>) | `3d741540c723be34282545b0313569d480bda6a732273ad4be69b90ebc2a95b2` |

| [produccion-arte/mundo-v03/char_mara_happy.es.txt](<produccion-arte/mundo-v03/char_mara_happy.es.txt>) | `1c2b941d915bbf3b9212dd252de3138f1cb3f938640aac62847745097957007e` |

| [produccion-arte/mundo-v03/char_mara_neutral.en.txt](<produccion-arte/mundo-v03/char_mara_neutral.en.txt>) | `06675a2b706d25a0918176e3d22f8f5d2323efd4b20a88ba5e242a607794dc0f` |

| [produccion-arte/mundo-v03/char_mara_neutral.es.txt](<produccion-arte/mundo-v03/char_mara_neutral.es.txt>) | `e727803150226d51245720dce6b8b930f81a4a80c5207f1448a27c572bd4f49f` |

| [produccion-arte/mundo-v03/char_mireya_annoyed.en.txt](<produccion-arte/mundo-v03/char_mireya_annoyed.en.txt>) | `e348a737dd065e4422559031903be5fe6c802430f9212dcb0d2fe6f9baabcf65` |

| [produccion-arte/mundo-v03/char_mireya_annoyed.es.txt](<produccion-arte/mundo-v03/char_mireya_annoyed.es.txt>) | `a5d0623b07c5408ebf53c43f046c087c21162113bae0f834a8a2b943fd050aca` |

| [produccion-arte/mundo-v03/char_mireya_happy.en.txt](<produccion-arte/mundo-v03/char_mireya_happy.en.txt>) | `91cdcb685bc7badb4c01bb16db0fbf5c7821ce4b2e63f14d8cb4a05de09094ef` |

| [produccion-arte/mundo-v03/char_mireya_happy.es.txt](<produccion-arte/mundo-v03/char_mireya_happy.es.txt>) | `cc0c84054751cd008c9917c37fc4f94ec7ace0e179a70d0589181cbba166a80c` |

| [produccion-arte/mundo-v03/char_mireya_neutral.en.txt](<produccion-arte/mundo-v03/char_mireya_neutral.en.txt>) | `cb08e5445c332f9d596b137315ac3c44b35cef8fbcdc72e8e9cfec1e251f3110` |

| [produccion-arte/mundo-v03/char_mireya_neutral.es.txt](<produccion-arte/mundo-v03/char_mireya_neutral.es.txt>) | `dedebb1868372b325567c2a0662cc32653546b9263f8db8d7244b63af070b036` |

| [produccion-arte/mundo-v03/char_nilo_annoyed.en.txt](<produccion-arte/mundo-v03/char_nilo_annoyed.en.txt>) | `0c73b380c64e66ffa5f486427e4b49012b1c795f2ab83c613e8487cdafae1ee0` |

| [produccion-arte/mundo-v03/char_nilo_annoyed.es.txt](<produccion-arte/mundo-v03/char_nilo_annoyed.es.txt>) | `35ead1006e0bb2df9cb22f9830ddf2e6f5f4502b3841bbd18a8f8c4dabc09abc` |

| [produccion-arte/mundo-v03/char_nilo_happy.en.txt](<produccion-arte/mundo-v03/char_nilo_happy.en.txt>) | `f6068567fcb4b6eb12d67b72aac68dff45b8ab98a71940e80905b418d030942c` |

| [produccion-arte/mundo-v03/char_nilo_happy.es.txt](<produccion-arte/mundo-v03/char_nilo_happy.es.txt>) | `61c852048fcaaa585a83af64923a6f8b29c95effbe639fbb06601d378b2122e2` |

| [produccion-arte/mundo-v03/char_nilo_neutral.en.txt](<produccion-arte/mundo-v03/char_nilo_neutral.en.txt>) | `6e1a35707740d3291a94a73a3b389be35e9c69537973ae3abfeff364252f02fc` |

| [produccion-arte/mundo-v03/char_nilo_neutral.es.txt](<produccion-arte/mundo-v03/char_nilo_neutral.es.txt>) | `63637c17c310a3bd2a198d7003fcf1bc5d131c47818abb282023c6457cce7c20` |

| [produccion-arte/mundo-v03/char_saul_annoyed.en.txt](<produccion-arte/mundo-v03/char_saul_annoyed.en.txt>) | `f0dd7ad096da3ea96158d3b5de20d8d0ec36c50af8cfac562e2013b71361d243` |

| [produccion-arte/mundo-v03/char_saul_annoyed.es.txt](<produccion-arte/mundo-v03/char_saul_annoyed.es.txt>) | `69479de7da8d63e9203cc2124096dcb91282017d6dcdeae59d5e45dae18ba3e6` |

| [produccion-arte/mundo-v03/char_saul_happy.en.txt](<produccion-arte/mundo-v03/char_saul_happy.en.txt>) | `70b113141a1f4707928e3df729c8ebc20c45d846127e9ffbac869aef8796aba3` |

| [produccion-arte/mundo-v03/char_saul_happy.es.txt](<produccion-arte/mundo-v03/char_saul_happy.es.txt>) | `6075bf0e1c754fe04bbc24d00d0ab0db44d3d5a9aa5d4be59baae12a15673ca4` |

| [produccion-arte/mundo-v03/char_saul_neutral.en.txt](<produccion-arte/mundo-v03/char_saul_neutral.en.txt>) | `e051a1359335ee4d7385220c67b88b7b9759e4ad063488e7974754192232e9e0` |

| [produccion-arte/mundo-v03/char_saul_neutral.es.txt](<produccion-arte/mundo-v03/char_saul_neutral.es.txt>) | `4b6ca84fe73d743ecd67af8dfa08036e852dbd706bea6a1bd7a502a86fff3498` |

| [produccion-arte/mundo-v03/referencias-y-bloqueos.json](<produccion-arte/mundo-v03/referencias-y-bloqueos.json>) | `91ebbc0519ad817b23b565432f743b71740d5c5be93b2dc12880ceacecddbad6` |

| [produccion-arte/mundo-v03/tanda-48-leonora-color-local/encargo-bilingue.json](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/encargo-bilingue.json>) | `00d3a7dc749faf070fee44da39ef58c61b1f2fd3abb8967a4ea7f79daceb22ac` |

| [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt>) | `17130c7253139f051b2002823e67992f7ece405279095c9c667d86bd80fae51d` |

| [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.es.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.es.txt>) | `c655042981a0732b154f39cb9b1fe8ab0e8f4b2ae03a4ce65c3c3c3448a6e590` |

| [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt>) | `d234cffb003005f636e69847ab35e88030b4b28dcbd176ef8f366177f2e19cd6` |

| [produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.es.txt](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.es.txt>) | `6a1e03ebab8b091551893d0416d6e2f98188efef9de5403927cc0c8d77d3caa0` |

| [produccion-arte/referencias-vestuario-usuario-2026-10-11/ESTUDIO-VESTUARIO.md](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ESTUDIO-VESTUARIO.md>) | `63428e15c09e0ebf785624b937ffdad2ce6edd9cefe4f8eed5988d66db15e0ff` |

| [produccion-arte/revision-estilo-v2/reference-sets.json](<produccion-arte/revision-estilo-v2/reference-sets.json>) | `ebb5fb2ea33ec905f72972b7824f9e647b4e7ec4e598560e634082c50ef72b25` |


## C.4. Alcance de esta entrega

Se consolidaron decisiones, mundo, perfiles, casos, dirección artística, aprobaciones, vestuario, referentes, flujo social, límites técnicos, prompts y enlaces a antecedentes. Se conservaron los textos fuente de los anexos sin presentarlos como aprobaciones nuevas. No se generaron recursos, cambiaron historias, corrigieron catálogos antiguos, alteró el juego ni se probó Android durante esta compilación.

El documento puede enviarse como contexto textual. Para inspeccionar imágenes y ejecutar herramientas, entregar también la carpeta del proyecto o los adjuntos enlazados: un Markdown no contiene los bytes de las imágenes. Los enlaces relativos están preparados para acompañar esa carpeta.
