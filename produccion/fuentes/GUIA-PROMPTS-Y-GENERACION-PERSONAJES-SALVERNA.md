# Salverna — Guía de estilo, prompts y generación de personajes

**13 de octubre de 2026 · Guía de entrega para artistas y herramientas de generación.**

Este documento explica el método que estamos utilizando para diseñar personajes, redactar sus prompts, generar una base y producir expresiones coherentes. No es el diseño visual definitivo de todo el juego ni convierte pruebas pendientes en recursos aprobados.

Documentos relacionados: [entrega integral](<ENTREGA-INTEGRAL-SALVERNA-2026-10-13.md>) e [investigación de referentes](<INVESTIGACION-REFERENTES-Y-UX-SALVERNA-2026-10-13.md>).

## 1. Resumen para quien recibe el encargo

Salverna busca personajes adultos expresivos, ilustrados con trazado artesanal y pintura mate de ejecución económica. El contexto combina sociedad de época, intereses familiares y fantasía propia. La nueva dirección del juego es una temporada social de invitaciones, encuentros e incidentes, con inspiración de ambiente en Bridgerton. Esa inspiración no sustituye el diseño individual ni el estudio de vestuario.

El objetivo visual es que cada personaje se reconozca por rostro, cuerpo, silueta, cabello, ropa y forma de actuar. No basta cambiar colores sobre una misma plantilla de belleza.

**La imagen ORIGINAL aprobada manda al crear expresiones.** Un prompt sirve para orientar la generación; el resultado debe revisarse. Un archivo generado, una buena descripción y una aprobación son estados distintos.

## 2. Qué se conserva del estilo

| Elemento | Dirección vigente | Fallo que debemos evitar |
|---|---|---|
| Dibujo | Presión variable, irregularidades deliberadas, extremos selectivos y gesto vivo | Contornos vectoriales uniformes o textura superpuesta a un dibujo demasiado pulido |
| Contornos | Más oscuros que el material y de su familia cromática | Línea negra idéntica alrededor de todo |
| Contactos | En encuentros claro/oscuro domina el borde del material oscuro | Bordes claros que separan artificialmente piezas oscuras |
| Pintura | Masas amplias, mate, pocas sombras estructurales y transiciones locales | Modelado fotográfico, plástico, brillo 3D o detalle uniforme |
| Textura | Pigmento y bordes de pincel localizados, con superficies tranquilas | Ruido, grano o rayado general para aparentar artesanía |
| Rostros | Proporciones distintas, asimetrías e intención; modelado selectivo | Mismos ojos, mandíbula, labios y nariz idealizados para todos |
| Pelo | Silueta propia, masas claras, pocas divisiones y reflejos | Modelar cada mechón/rizo con sombra, borde y brillo |
| Piel | Color individual, matices localizados y transiciones pertinentes | Aclarar piel por defecto, baño naranja o corrección fría global |
| Ropa | Corte identificable, construcción legible y simplificación pictórica | Pliegues facetados por todas partes, adornos aleatorios o prendas incompatibles |
| Objetos | Función concreta, escala y sujeción plausible | Llaves naciendo del brazo/libro; joyas o tocados flotantes |

«Gouache» y «grafito coloreado» describen el comportamiento de pintura y línea buscado. No certifican qué materiales usó el artista de nuestros originales ni obligan a aplicar grano a toda la figura.

La sencillez de ejecución no significa ropa pobre o cara sin personalidad. Un bordado puede conservar su función con menos marcas, y una piel puede tener matices sin volverse un retrato realista.

## 3. Separar las referencias por su función

### A. Técnica de ilustración

Los originales ilustrados se adjuntan para un **diseño inicial nuevo**, indicando expresamente que enseñan línea, proporción ilustrada, economía de pintura y tratamiento de bordes. No prestan rostro, peinado, vestido, pose o accesorios.

Ejemplos presentes en el proyecto:

- [Original ilustrado 1](<imgi_28_latest.webp>).
- [Original ilustrado 2](<imgi_26_1000 (3).webp>).
- [Original ilustrado 3](<imgi_161_latest.webp>).
- [Muestra original de pintura de tela usada en t48](<produccion-arte/mundo-v03/tanda-24-muestras-visuales/tela-original.png>).

El conjunto concreto depende del encargo registrado. No afirmar que todos esos archivos participaron en cada generación.

### B. Vestuario y coordinación

Fotografías, prendas museísticas y diseños identificables sirven para estructura, corte, ocasión, materiales y coordinación. No se usan como autoridad de pintura, anatomía fotográfica o luz amarilla.

Los nueve originales del usuario y sus observaciones están en [el estudio de vestuario](<produccion-arte/referencias-vestuario-usuario-2026-10-11/ESTUDIO-VESTUARIO.md>). No mezclar los nueve trajes en una persona ni copiarlos literalmente.

### C. Carta de color individual

Define pigmentos por material: piel, pelo, ropa, blanco, sombra y acentos. No es una paleta universal para todo el elenco. Las referencias técnicas no deben imponer su dominante cálida.

Ejemplo: [carta de color de Leonora t48](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/paleta.png>). Sus blancos y tonos de piel pertenecen a ese encargo, no a todos los personajes.

### D. Identidad aprobada

Para una expresión, el **único adjunto visual** es el dibujo ORIGINAL aprobado de la misma persona. Las referencias técnicas y de vestuario se utilizan al investigar y describir la intención, pero no se añaden a la edición de la pose.

Si falta la base aprobada, no crear una expresión sólo desde texto ni usar a otro personaje para compensarla.

## 4. Antes del prompt: ficha de diseño

Antes de generar un personaje nuevo, recuperar las fuentes de autoría y documentar:

1. **Identidad:** ID, nombre, edad adulta y qué datos están definidos o pendientes.
2. **Motivación:** qué quiere en este momento, qué protege y cómo trata a su interlocutor.
3. **Contexto:** procedencia, recursos, ocasión, clima y trayecto; profesión no obliga a portar herramientas.
4. **Construcción física:** proporciones del cuerpo y de la cara; forma de mandíbula, nariz, párpados y boca; diferencias respecto al elenco.
5. **Pelo:** textura, raya, dirección, volumen, recogido, soporte y silueta. Un color llamativo no reemplaza la estructura.
6. **Vestuario:** referencia concreta, cintura, escote, mangas, cierres, falda/pantalón, materiales y motivo dominante.
7. **Maquillaje:** intención o ausencia; cejas, párpados, rubor y labios. No confundir cosmético con pigmento natural o sombra pintada.
8. **Objetos:** inventario breve, mano que los sostiene o punto donde se sujetan.
9. **Actuación:** verbo principal —resistir, escuchar, negociar, agradecer— y traducción a mirada, hombros, manos y peso.
10. **Encuadre:** función del sprite, zona visible, escala, margen y relación con la interfaz.

No rellenar vacíos biográficos para que una ficha parezca terminada. La plantilla de autoría está en [plantilla-personaje-central.json](<memoria-salverna/plantilla-personaje-central.json>).

Las condiciones fantásticas requieren ficha propia. No volver nocturna, velaria o hilandera a una persona existente para hacerla visualmente más interesante.

## 5. Cómo estructuramos un prompt de diseño inicial

Un encargo inicial se organiza por bloques de instrucciones observables:

1. **Operación:** dibujo nuevo desde cero; personaje y función.
2. **Referencias:** archivo/orden y función de cada adjunto.
3. **Encuadre y proporciones:** vista, corte, anatomía visible y márgenes.
4. **Identidad:** construcción facial, corporal y capilar.
5. **Vestuario:** piezas separadas y construcción, no sólo calificativos.
6. **Color local:** materiales independientes, sin iluminación ambiental global.
7. **Actuación:** gesto preciso que conserva el carácter.
8. **Dibujo y pintura:** comportamiento de línea, manchas, sombras y textura.
9. **Salida:** transparencia, ausencia de escena/texto y contenido íntegro.
10. **Prioridades:** qué dos o tres aspectos deben revisarse primero.

No existe un texto universal que garantice la técnica. Los prompts largos de las tandas son historial de correcciones concretas; acumular todas sus prohibiciones en cada persona puede introducir contradicciones.

### Plantilla ES — diseño inicial

**Plantilla para completar antes de ejecutar. Los campos entre llaves no son un encargo listo.** La versión de trabajo inglesa debe tener los mismos hechos, límites y prioridades.

```text
OPERACIÓN: NUEVO DISEÑO ORIGINAL DESDE CERO.
Crear {nombre, ID}, personaje adulto de {edad definida}, como {función del recurso}.
Momento: {situación e intención}; no revelar mediante la imagen {secreto o interpretación que deba quedar abierta}.

ADJUNTOS:
{lista ordenada de imágenes y función exacta}.
Los originales ilustrados enseñan técnica, no prestan rostro, ropa, objetos o pose.
Las referencias de vestuario enseñan construcción, no luz o acabado fotográfico.

ENCUADRE:
{vista, orientación, corte y perspectiva definidos por la composición}.
{proporciones relativas y márgenes}. Conservar cabello, manos y objetos esenciales completos.

IDENTIDAD:
{proporciones corporales y construcción facial diferenciada}.
{pelo: silueta, textura, dirección, recogido y fijación}.
{maquillaje definido o ausencia}. No imponer una cara de belleza genérica.

VESTUARIO Y OBJETOS:
{piezas, corte, cierres y materiales; referencia investigada y adaptación propia}.
{inventario breve y sujeción/agarre de cada objeto}.
{motivo dominante y zonas sin adorno}.

COLOR:
{carta individual y colores por material}. Pintar pigmentos locales independientes.
Sin veladura amarilla/naranja, sepia ni corrección fría global. Mantener el color individual de piel.

ACTUACIÓN:
{verbo e intención}, mediante {mirada, párpados, boca, cabeza, hombros, manos y peso}.
La pose debe leerse al tamaño de teléfono y responder a esta persona.

TÉCNICA:
Línea artesanal de presión variable, más oscura que su material.
En un contacto claro/oscuro domina el borde del material oscuro.
Pintura mate de masas amplias, pocas sombras estructurales y transiciones locales.
Textura localizada y superficies tranquilas. Cabello por masas, reflejos escasos.
Sin modelado plástico, vector uniforme, detalle fotográfico ni grano general.

SALIDA:
Sprite aislado con fondo realmente transparente; sin escena, texto, muestras de color o suelo.
{objetivo de preparación y margen; no presentarlo como tamaño garantizado}.

PRIORIDADES DE REVISIÓN:
{identidad principal}; {control de color}; {construcción o gesto crítico}.
```

### Template EN — initial design

```text
OPERATION: NEW ORIGINAL CHARACTER DESIGN FROM SCRATCH.
Create {name, ID}, an adult aged {defined age}, as {asset purpose}.
Moment: {situation and intent}; the image must not settle {unresolved secret or interpretation}.

ATTACHMENTS:
{ordered images with an explicit role for each}.
Original illustrations teach technique, never supply faces, clothes, props or poses.
Costume references teach construction, never photographic lighting or rendering.

FRAMING:
{view, orientation, crop and perspective established by the layout}.
{relative proportions and margins}. Keep essential hair, hands and props fully visible.

IDENTITY:
{distinct body and facial construction}.
{hair silhouette, texture, direction, arrangement and fastening}.
{defined makeup or its absence}. Never impose a generic beauty face.

COSTUME AND PROPS:
{garments, cuts, fastenings and materials; researched reference and original adaptation}.
{short inventory and a plausible attachment or grip for every prop}.
{dominant motif and quiet undecorated areas}.

COLOUR:
{individual colour key and pigments by material}. Paint local pigments independently.
No yellow/orange glaze, sepia or overall cool correction. Preserve individual skin colour.

ACTING:
{verb and intent}, through {gaze, lids, mouth, head, shoulders, hands and weight}.
The pose must read at phone size and belong to this character.

TECHNIQUE:
Handcrafted pressure-varied lines darker than their own material.
The darker material owns shared light/dark boundaries.
Broad matte paint shapes, few structural shadows and local soft transitions.
Localised texture and quiet surfaces. Hair in masses, sparse highlights.
No plastic modelling, uniform vector finish, photographic detail or global grain.

OUTPUT:
Isolated sprite with true transparency; no scene, text, colour swatches or ground plane.
{preparation target and margins; never promise guaranteed generated dimensions}.

REVIEW PRIORITIES:
{main identity cue}; {colour control}; {critical construction or gesture}.
```

## 6. El método de color que funcionó en Leonora t48

El encargo t48 separó visualmente los pigmentos y declaró los roles de sus referencias:

- Carta de color como autoridad cromática.
- Dos originales ilustrados como técnica, no identidad ni iluminación.
- Muestra de tela como comportamiento de línea/pintura.
- Ninguna Leonora anterior adjunta: fue una nueva generación desde cero.

La instrucción pedía blanco puro para lino, sombras gris frío puntuales, piel pálida rosa-lila con rubor local, pelo rojo y ropa carbón neutro. La prioridad era evitar que un filtro cálido recoloreara toda la figura. **Esa paleta pertenece a Leonora**, no es una norma de piel o cabello para todo el elenco.

La imagen t48 fue aprobada posteriormente por el usuario. El encargo original todavía conserva la marca de candidatura de su fecha; no debe reescribirse para fingir una aprobación previa.

El diagnóstico de nube/halo se corrigió al componer el alfa sobre fondo claro: no justificar regeneración de la base aprobada por una apariencia de previsualización.

Fuente exacta: [encargo t48 y adjuntos](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/encargo-bilingue.json>). El prompt completo también figura en el Anexo A.2 de la entrega integral.

## 7. Expresiones: una operación diferente

**Base ORIGINAL aprobada → expresión solicitada.** Cada llamada vuelve a la misma base.

| Operación | Adjuntos | Qué se permite |
|---|---|---|
| Diseño inicial | Referencias con roles definidos para técnica, construcción y color | Proponer identidad nueva sujeta a revisión |
| Cambio de expresión | Sólo el ORIGINAL aprobado de esa persona | Expresión, gesto y pliegues necesarios |
| Cambio de vestuario/identidad | Encargo específico y revisión propia | No se oculta dentro de un cambio de pose |
| Corrección técnica puntual | Base correspondiente y objetivo acotado | No autoriza embellecer rostro o cambiar personalidad |

Para expresiones se conserva: persona, edad, geometría facial, piel, pelo, cuerpo, ropa, maquillaje, accesorios, paleta, pintura, trazo, encuadre y escala. No encadenar variantes. No agregar otros personajes como referencia de estilo.

### Plantilla ES — expresión

```text
VARIANTE DE EXPRESIÓN Y GESTO DEL ORIGINAL APROBADO ADJUNTO.
La imagen adjunta es la única autoridad visual y el objetivo de edición.
Conservar exactamente la misma persona, identidad, proporciones, rostro, cabello,
piel, vestuario, accesorios, maquillaje, paleta, trazado artesanal y pintura.
Mismo encuadre, escala y tamaño de cabeza. No embellecer ni rediseñar.

INTENCIÓN: {emoción y objetivo propios del personaje en este momento}.
CAMBIO: {mirada, párpados, cejas, boca, cabeza, hombros y manos descritos con precisión}.
OBJETOS: {cómo se conservan y sujetan los mismos objetos durante el gesto}.
Modificar sólo expresión, gesto y pliegues físicamente necesarios.
Mantener anatomía legible, manos completas y accesorios unidos.
Fondo realmente transparente; sin escena, texto ni elementos nuevos.
```

### Template EN — expression

```text
EXPRESSION AND GESTURE VARIANT OF THE ATTACHED ORIGINAL APPROVED CHARACTER.
The attached image is the sole visual authority and edit target.
Preserve the exact same person, identity, proportions, face, hair, skin,
costume, accessories, makeup, palette, handcrafted linework and paint.
Same framing, scale and head size. Do not beautify or redesign.

INTENT: {this character's emotion and purpose in this moment}.
CHANGE: {precise gaze, lids, brows, mouth, head, shoulders and hand instructions}.
PROPS: {how the same objects remain present and physically held or attached}.
Change only expression, gesture and physically necessary folds.
Keep readable anatomy, complete hands and attached accessories.
True transparent background; no scene, text or new elements.
```

## 8. Ejemplo real: Leonora y sus expresiones

### Base actual aprobada

[Original t48, conservado sin cambios en t49](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora-neutral-original-aprobado.png>).

![Leonora: original aprobado](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora-neutral-original-aprobado.png>)

La imagen manda: silueta de pelo, cara, mini tocado, velo, perlas, prendas negras, lino blanco y gesto de duelo no se sustituyen con un texto antiguo. No hacer que una sonrisa o el luto decidan su sinceridad moral.

### Ira contenida — prompt ES registrado

```text
Adjuntar solo base ORIGINAL t48. Conservar identidad, paleta, ropa y técnica exactas.
Ira contenida visible: pañuelo apretado en puño, mano contraria en cintura,
cejas tensas desiguales y boca cerrada. Sin gritos ni sonrisa malvada.
Solo expresión, gesto y pliegues necesarios.
```

### Gratitud reservada — prompt ES registrado

```text
Adjuntar solo base ORIGINAL t48. Conservar identidad, paleta, ropa y técnica exactas.
Gratitud reservada: mano abierta sobre pecho, otra con pañuelo en cintura,
leve inclinación y sonrisa cerrada asimétrica. Misterio y dignidad,
sin entusiasmo exagerado. Solo expresión, gesto y pliegues necesarios.
```

Las versiones inglesas son más detalladas; ambos registros se conservan como se escribieron, no se presentan como traducciones literales de la misma extensión. Consultar los archivos completos antes de ejecutar.

- [Ira contenida EN](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_annoyed.en.txt>).
- [Gratitud EN](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/char_leonora_happy.en.txt>).
- [Manifiesto de aprobación de base y estado de variantes](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/manifest.json>).

**Estado:** t48 aprobada; ambas variantes t49 producidas, pendientes de aprobación. Son ejemplos de método, no dos recursos finales aceptados.

## 9. Estados actuales que importan al generar

| Persona | Autoridad / estado | Acción permitida por esa condición |
|---|---|---|
| Leonora | t48 aprobada; t49 pendiente | Reutilizar t48; no reemplazarla por C2/B o una expresión |
| Mireya | Identidad y técnica v2 aprobadas; unión de llaves pendiente | Corrección acotada de sujeción, sin rediseñar el rostro |
| Ivo | Manifiesto registra identidad/técnica C3 aprobadas | Conservar base; no extender aprobación a toda variante |
| Inés | Rediseños y t50 candidatos; sin nueva base aprobada | Revisar neutral; no generar expresiones como si estuviera aprobado |
| Mara, Nilo, Saúl y Bruna | Candidatos con revisión pendiente | No producir tandas de expresiones desde una base sin confirmar |

Este es el elenco del prototipo judicial. No son automáticamente los ocho candidatos románticos del nuevo diseño social. Una persona nueva necesita ficha propia; no hereda cara, ropa, especie u orientación de una entidad existente.

Fuente operativa: [referencias y bloqueos](<produccion-arte/mundo-v03/referencias-y-bloqueos.json>), contrastada con [decisiones](<memoria-salverna/decisiones.md>).

**Problema conocido:** algunos prompts del catálogo todavía describen Leonora C2 y contradicen la base t48 —por ejemplo, no añadir velo—. No ejecutarlos literalmente contra la identidad actual. Un número de versión o un archivo llamado «activo» no resuelve esa contradicción por sí solo.

## 10. Revisión del resultado antes de otra generación

1. **Identidad:** ¿es esta persona, con sus proporciones y silueta? Comparar con la autoridad correcta.
2. **Actuación:** ¿se distingue la intención sin caricatura ni gesto genérico? ¿Conserva carácter?
3. **Dibujo:** ¿la irregularidad pertenece al trazo y a la forma o es ruido añadido?
4. **Pintura:** ¿hay superficies tranquilas, matices locales y bordes selectivos? ¿Cara y ropa comparten lenguaje?
5. **Color:** ¿cada material conserva su pigmento? Comprobar blancos, piel y negros sin filtro global.
6. **Construcción:** ¿ropa, cierres, joyas y tocados tienen sentido? ¿Manos y objetos se sostienen físicamente?
7. **Transparencia:** comprobar alfa real sobre fondo claro y oscuro; no juzgar sólo una miniatura del generador.
8. **Montaje móvil:** revisar a escala de uso, con diálogo/interfaz y recortes reales; no sólo ampliar la imagen aislada.

Corregir la causa concreta antes de propagar el fallo al elenco. No aprobar por cantidad ni declarar una anatomía perfecta porque el prompt pidió cinco dedos.

La aprobación debe identificar qué imagen y qué aspecto acepta. Técnica aprobada, identidad aprobada, corrección pendiente y variante pendiente pueden coexistir.

## 11. Entrega y registro de una tanda

Conservar, sin sobrescribir la base aprobada:

- ID y nombre del recurso; operación: nuevo diseño, expresión o corrección.
- Prompt exacto enviado y versión ES/EN correspondiente; indicar si son resumen y versión extensa.
- Lista ordenada de adjuntos y rol de cada uno.
- Resultado original recibido y dimensiones reales.
- Estado: candidato, revisado, aprobado o rechazado, con causa.
- Derivados de preparación separados del original: recortes, escala y origen.
- Prueba de alfa y captura del montaje cuando exista.

Los objetivos de preparación —por ejemplo, encargos históricos de sprite 1024×1536— no garantizan la salida del generador. El encuadre de cada recurso depende de su función: no imponer a todos la proporción de cabeza o el corte usado en Leonora t48.

Para cambios de IDs, fichas, fuentes o dependencias, ejecutar `python memoria-salverna/validar_memoria.py`. Esa validación no sustituye la inspección editorial ni visual.

## 12. Fuentes para continuar

- [Reglas centrales de autoría](<REGLAS-CENTRALES-SALVERNA.md>).
- [Estándar de calidad](<ESTANDAR-CALIDAD-SALVERNA.md>).
- [Regla de vestuario con referentes](<produccion-arte/REGLA-VESTUARIO-CON-REFERENTES.md>).
- [Peinado, maquillaje y actuación](<produccion-arte/REGLA-PEINADO-MAQUILLAJE-ACTUACION.md>).
- [Estudio de originales y evolución de técnica](<produccion-arte/mundo-v03/ESTILO-REFERENTES-v06.md>).
- [Control de continuidad de color t29](<produccion-arte/mundo-v03/tanda-29-elenco-beta/CONTROL-COLOR.md>).
- [Referencias y bloqueos actuales](<produccion-arte/mundo-v03/referencias-y-bloqueos.json>).
- [Encargo exacto de t48](<produccion-arte/mundo-v03/tanda-48-leonora-color-local/encargo-bilingue.json>).
- [Prompts t49 ES](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/prompts-es.json>) y [EN](<produccion-arte/mundo-v03/tanda-49-leonora-tres-expresiones/prompts-en.json>).

Las fuentes técnicas antiguas pueden describir pruebas no aprobadas. Las decisiones posteriores y el ORIGINAL aprobado prevalecen. Esta guía añade estructura documental y plantillas, no nuevas imágenes o aprobaciones.

## English handoff summary

Salverna uses handcrafted pressure-varied material-colour outlines, broad matte painting, localised texture and distinctive adult faces. Costume construction, hairstyle, makeup and acting require specific references and character intent. Initial designs may use separately labelled technique, costume and colour references. Every expression edit uses only the SAME character's ORIGINAL approved base as sole visual authority; preserve exact identity, costume, palette, framing and painting. Never chain expressions or attach other characters for style. Leonora t48 is approved; t49 variants remain pending. Prompt templates are drafting tools, not approved characters or guarantees of output quality. Review actual images, transparency and phone-scale composition before expanding a batch.
