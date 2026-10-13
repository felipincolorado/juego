# Salverna — Investigación de referentes, diseño móvil y producción

**Complemento del documento integral · 13 de octubre de 2026.**

Reúne los aprendizajes y fuentes ya registrados en el proyecto sobre King/Candy Crush, Apple/Overboard!, otros juegos narrativos, accesibilidad y producción 2D. No se hizo una nueva consulta web en esta entrega: se recuperó la investigación local fechada. Los enlaces externos son los registrados entonces; verificar documentación y APIs al implementar.

Documento principal: [Entrega integral](<ENTREGA-INTEGRAL-SALVERNA-2026-10-13.md>).

## 1. Alcance: qué se estudió realmente

| Investigación | Evidencia disponible | Límite |
|---|---|---|
| King / Candy Crush | Tres capturas, caso de colaboración publicado por Figma y portafolio de diseño | No se inspeccionó su código ni se ejecutó el juego |
| Apple / Overboard! | Fuente editorial Apple Developer registrada en la auditoría y descripción oficial de inkle | No es un estudio exhaustivo de las Human Interface Guidelines de Apple |
| Dispatch | JSON exportados, análisis de estructuras y ocho capturas —siete únicas— | Fórmula ejecutable completa no recuperada; capturas no demuestran tiempos ni usabilidad |
| Dressmaker | Scripts recuperados, sprites, metadatos y escenas inspeccionados | No se ejecutó el original ni se comprobó en teléfono |
| Otros juegos | Páginas oficiales y diario de adaptación móvil de Papers, Please | No se analizaron todos cuadro por cuadro |
| GDC | Resúmenes oficiales de tres ponencias | Ponencias completas pendientes; no atribuirles detalles no vistos |
| Android, Godot y Krita | Documentación técnica registrada en informes locales | Una recomendación documentada no demuestra su cumplimiento en Salverna |

Las conclusiones de adaptación siguientes son criterio del proyecto. Ninguna fuente demuestra ventas, retención o calidad comercial futura de Salverna.

## 2. King y Candy Crush

### Proceso de diseño

La investigación registrada identifica uso de Figma para prototipos, bibliotecas de componentes y colaboración en King. Esto respalda diseñar y probar flujos antes de programar toda la experiencia. No demuestra que una propuesta automática de Figma tenga la dirección artística adecuada ni obliga a utilizar el motor de King.

Fuentes registradas: [Figma — How King brings game design together](https://www.figma.com/customers/how-king-brings-game-design-together/) y [Anna Brandberg — Candy Crush Saga](https://www.annabrandberg.com/candy-crush-saga). El portafolio sirve para estudiar proceso; no se le atribuyen todas las capturas del usuario.

### Observación de las capturas

- La portada introduce el mundo con ilustración, título dominante y una acción principal distinguible.
- El mapa usa perspectiva elevada oblicua, caminos legibles y marcadores grandes. La escala de nodos y personajes prioriza interacción sobre realismo geográfico.
- El modal oscurece el fondo y separa cabecera, contenido y cierre.
- Las barras superior e inferior agrupan funciones persistentes y destinos reconocibles.
- La captura del modal corresponde a una oferta de vidas/recursos; no es una ficha de nivel ni evidencia de que ese contenido comercial sirva para nuestras invitaciones.

### Aplicación propuesta a Salverna

Mapa teatral 2D de Valcenda, con unas cinco locaciones distinguibles y rutas ramificadas. Fecha y semana visibles; Ciudad, Elenco y Calendario como hipótesis de navegación. Marcadores y retratos legibles, sin edificios diminutos ni botones que oculten caminos.

Conservar la posibilidad de eventos simultáneos y multidiarios: nuestro calendario no es una escalera lineal de niveles. No importar vidas, tienda, esperas, distintivos acumulados ni acabado plástico por asociación con el referente. La gramática de documentos y materiales debe pertenecer a Salverna.

Informe completo y originales: [Análisis de diagramación](<referencias-candy-crush/ANALISIS-DIAGRAMACION.md>), [portada](<referencias-candy-crush/01-portada.png>), [modal](<referencias-candy-crush/02-modal-recursos.png>) y [mapa](<referencias-candy-crush/03-mapa.png>).

## 3. Apple Developer e inkle: Overboard!

La auditoría del 12 de octubre registra [Apple Developer — Behind the Design: Overboard!](https://developer.apple.com/news/?id=fkelkwzq) como fuente sobre prototipado narrativo, conocimiento de personajes y pruebas tempranas. También registra [la descripción oficial de Overboard!](https://www.inklestudios.com/overboard/), centrada en acciones sociales y consecuencias.

**No se documentó una investigación general de toda la interfaz de Apple ni una auditoría completa de sus HIG.** La referencia concreta es un caso de diseño de videojuego publicado por Apple.

### Qué aporta al proyecto

El interés de esta investigación es la relación entre narrativa y sistema: las personas saben cosas distintas; las acciones cambian lo que puede ocurrir después; una historia interactiva necesita probarse como recorrido.

### Adaptación propuesta

- Escribir para cada incidente quién conoce qué, qué pretende y qué cambia al responder.
- Mantener separados verdad de autor, información del jugador, conocimiento individual y rumor público.
- Probar pronto un evento y su retorno, antes de producir una temporada entera.
- Mostrar consecuencias mediante conductas y oportunidades posteriores, además de cifras.
- Evitar que el cierre semanal revele una confidencia que nadie transmitió a la sociedad.

Estas son aplicaciones editoriales de Salverna, no citas ni reglas universales atribuidas a Apple. La apertura judicial, los casos y las propuestas económicas de la auditoría conservan su fecha; no son implementación del modo social.

Informe de origen: [Auditoría de sistemas y progresión](<AUDITORIA-SISTEMAS-Y-PROGRESION-2026-10-12.md>), especialmente sus fuentes y propuestas de bucle.

## 4. Dispatch: gestión y presentación de decisiones

| Función estudiada | Aplicación a Salverna | Precaución |
|---|---|---|
| Encargo con requisitos | Invitación resumida y carta completa aparte | No esconder condiciones esenciales en la carta larga |
| Asignación de especialistas | Comparar cinco atributos y asistentes | Falta nuestra fórmula; no afirmar que ya conocemos la suya |
| Estados del elenco | Disponible, reservado, en viaje, en actividad o afectado | Vergüenza e incapacidad requieren reglas diferentes |
| Incidente | Situación, participantes y opciones significativas | Pausar mientras se decide; no volver a tirar al abrir |
| Resultado | Desenlace, reacción y cambios explicados | Animación representa estado confirmado; no duplica premios |
| Evaluación | Cierre semanal con causas | La reputación pública no conoce secretos automáticamente |
| Composición por tarea | Distintas pantallas para asignar, decidir y revisar | No encoger tres columnas de escritorio en un móvil |

La identidad proviene de personajes, estados, mundo y causalidad, además de los marcos. No copiar terminal CRT, símbolos o material narrativo del referente.

Informes: [Mecánicas](<referencias-dispatch/ANALISIS-MECANICAS-2026-10-12.md>), [narrativa y tutoriales](<referencias-dispatch/ANALISIS-NARRATIVA-TUTORIALES-SHARED.md>), [episodios/plugins](<referencias-dispatch/ANALISIS-EPISODIOS-PLUGINS.md>) y [capturas y adaptación móvil](<referencias-dispatch/capturas-ui-2026-10-13/ANALISIS-Y-ADAPTACION-MOVIL.md>).

## 5. Otros referentes narrativos y de progresión

| Referente | Aprendizaje registrado | Adaptación y límite |
|---|---|---|
| Dressmaker | Lugar de trabajo persistente, personajes recurrentes, recompensa y presentación | Despacho reconocible y retratos con actuación; no importar sus proporciones horizontales sin revisar móvil |
| Papers, Please móvil | Reorganización de la mesa, documentos grandes y continuidad de comparación | Abrir carta/perfil sin perder selección o reserva; no trasladar toda la mesa de escritorio reducida |
| The Case of the Golden Idol | Deducción a partir de pistas | En Salverna judicial, comprender verdad y publicar versión interesada son posibilidades distintas; no convertir toda elección en examen |
| Yes, Your Grace | Peticionarios recurrentes, recursos limitados y presión familiar | Invitaciones con retorno y costes personales; la continuidad debe cambiar decisiones |
| Coin Master | Construcción visible conectada con su propio sistema de eventos y riesgos | Un despacho puede mejorar visualmente; grandes árboles de construcción necesitan utilidad y contenido propios |
| 80 Days | Narrativa combinada con recursos, según descripción oficial | Referencia de estructura, no auditoría de sus pantallas |
| Ren’Py e ink | Separación de autoría, diálogo, opciones e historial | Contenido y estado separados de presentación; no exige migrar desde Godot |

Fuentes registradas: [Dressmaker](https://freelives.net/dressmaker-presskit/), [Papers, Please: adaptación móvil](https://dukope.com/devlogs/papers-please/mobile/), [Golden Idol](https://www.playstack.com/games/goldenidol/), [Yes, Your Grace](https://noodlecake.com/games/yes-your-grace/), [Coin Master](https://support.coinmastergame.com/hc/en-us/articles/29805992231058-How-can-I-strategically-best-build-my-Village), [80 Days](https://www.inklestudios.com/80days/), [ink](https://www.inklestudios.com/ink/) y [pantallas Ren’Py](https://www.renpy.org/doc/html/screen_special.html).

Informes locales: [Auditoría UX del 10 de octubre](<auditoria-ux-referentes-salverna.md>), [primera inspección Dressmaker](<analisis-referente-dressmaker-primera-inspeccion.md>) y [segunda inspección](<analisis-referente-dressmaker-segunda-inspeccion.md>).

**Advertencia de versión:** el informe del 10 de octubre describe una etapa anterior al prototipo integrado. Sus afirmaciones sobre funciones todavía inexistentes deben contrastarse con C16 y el README actual; no restablecer ese estado antiguo.

## 6. Android, accesibilidad y jerarquía visual

La investigación registrada usa las guías de Android para áreas táctiles de al menos 48×48 dp, texto adaptable, contraste y áreas seguras. El mínimo de referencia no equivale a 48 píxeles del PNG ni a 48 unidades de cualquier lienzo.

También recoge las recomendaciones de Game Accessibility Guidelines sobre texto claro y fondos sin distracciones; Material sobre jerarquía funcional de botones; y W3C sobre no depender exclusivamente del color.

### Contrato de aplicación propuesto

- Una acción principal reconocible por estado; opciones de igual importancia con énfasis equivalente.
- Seleccionado no significa correcto: marca, borde y texto comunican selección.
- Rojo y exclamación indican atención; no anuncian por sí solos fracaso o culpa.
- Texto importante sobre una superficie legible, sin reducir fuente automáticamente hasta que quepa.
- Carta y biografía pueden desplazarse; las opciones de un incidente deben verse y tocarse cómodamente.
- Abrir un documento y regresar conserva contexto y selección.
- Revisar español e inglés, pantalla estrecha y alta, interrupción y reanudación.
- La composición 9:16 es referencia artística, no una caja rígida para todo Android.

Fuentes registradas: [Android: accesibilidad](https://developer.android.com/design/ui/mobile/guides/foundations/accessibility), [objetivos táctiles](https://support.google.com/accessibility/android/answer/7101858?hl=en), [áreas de contenido](https://developer.android.com/design/ui/mobile/guides/layout-and-content/content-structure), [texto en juegos](https://gameaccessibilityguidelines.com/use-simple-clear-text-formatting/), [Material: botones](https://github.com/material-components/material-web/blob/main/docs/components/button.md), [W3C: uso del color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) y [contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

Aplicación histórica y límites: [Estudio UI C12](<produccion-arte/revision-ui-C12/ESTUDIO-UI-Y-APLICACION.md>). Sus medidas y contrastes sólidos no certifican toda textura, toda pantalla ni accesibilidad Android real.

## 7. Producción 2D, animación y lectura

La investigación técnica registrada cubre proporción y recorte de TextureRect; NinePatchRect/StyleBoxTexture para paneles; atlas y contaminación de bordes; contenedores; fuentes y RichTextLabel; capas; Tween/AnimationPlayer; animación por recortes; área segura; recursos y audio.

### Aplicación al nuevo mapa

Separar terreno, edificios, ambiente, retratos, caminos, marcadores y controles. Cámara y escala comunes; fondo completo bajo objetos móviles. Rutas y aros dinámicos. Texto y valores vivos. Reutilizar el rostro aprobado mediante recortes, sin generar una cara diferente por tamaño.

Las transiciones deben comunicar viaje, progreso, alerta y consecuencia. Guardar el estado antes de presentar recompensas; permitir movimiento reducido. No usar una captura estática como prueba de que una animación o una interacción ya funciona.

Fuentes técnicas registradas: [Godot: resoluciones múltiples](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html), [NinePatchRect](https://docs.godotengine.org/en/stable/classes/class_ninepatchrect.html), [Tween](https://docs.godotengine.org/en/stable/classes/class_tween.html) y [Krita: imágenes](https://docs.krita.org/en/user_manual/working_with_images.html). Comprobar versión del motor al implementar.

Paquete local completo:

- [Entrada de investigación 2D](<investigacion-juego-2d/2026-10-11/LEER-PRIMERO.md>).
- [Auditoría](<investigacion-juego-2d/2026-10-11/01-AUDITORIA.md>).
- [Recursos y composición](<investigacion-juego-2d/2026-10-11/02-ASSETS.md>).
- [Godot y narrativa](<investigacion-juego-2d/2026-10-11/03-GODOT-Y-NARRATIVA.md>).
- [Plan y pruebas](<investigacion-juego-2d/2026-10-11/04-PLAN-Y-PRUEBAS.md>).
- [Catálogo completo de fuentes](<investigacion-juego-2d/2026-10-11/FUENTES.md>).

## 8. GDC: alcance de la investigación

Sólo se consultaron resúmenes oficiales de:

- [Designing Text UX for Effortless Reading](https://gdcvault.com/play/1025104/Designing-Text-UX-for-Effortless), Joseph Humfrey, 2018: lectura, ritmo, tipografía, movimiento y atención.
- [Art Direction for AAA](https://www.gdcvault.com/play/1025498/Art-Direction-for-AAA), Omer Younas, 2018: coherencia de dirección artística en producción.
- [Juice It or Lose It](https://www.gdcvault.com/play/1016487/Juice-It-or-Lose), Martin Jonasson y Petri Purho, 2012: feedback.

No atribuirles duraciones concretas, recetas o conclusiones de una ponencia completa no vista. El PDF de Big Visuals y la página de cámaras de Blender no pudieron leerse en aquella consulta y no cuentan como material estudiado.

## 9. Qué debe demostrar la próxima maqueta

1. Se entiende dónde ocurre el evento, cuándo y quién está reservado.
2. Se puede comparar requisitos y asistentes sin perder legibilidad.
3. Dos actividades simultáneas y una multidiaria se distinguen en el mapa.
4. La alerta abre una decisión comprensible y pausa el avance.
5. El reemplazo ofrece sólo opciones válidas y explica su causa.
6. El resultado comunica qué ocurrió, por qué cambió algo y qué continúa.
7. La escena conserva carácter de videojuego y de Salverna a tamaño de teléfono.

Estos puntos son criterios propuestos de revisión, no resultados ya obtenidos. Una prueba estructural, una inspección visual y una sesión con un jugador miden cosas distintas.

## English summary

This supplement consolidates previously recorded research, not a new web review. King/Figma informs collaborative prototyping and reusable components; Candy Crush screenshots inform mobile map hierarchy, not monetisation or a linear season structure. Apple Developer's Overboard! article informs narrative prototyping and character knowledge; no comprehensive Apple HIG audit is claimed. Dispatch, Dressmaker, Papers, Please and other references retain explicit evidence limits. Android/accessibility and Godot/2D findings are linked to their original reports. Proposed Salverna applications are separate from source claims, implementation and user approval.
