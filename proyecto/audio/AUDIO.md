# Salverna · Música, ambientes y efectos (v1)

**13 de octubre de 2026 · Propuesta.** Las licencias se comprobaron con fuentes secundarias. **Antes de descargar, revise la página oficial de cada licencia**: los términos cambian. No use nada cuya licencia no permita el uso comercial.

---

## 1. Dirección musical

**Idea:** a Bridgerton se le reconoce por el **pop moderno tocado por un cuarteto de cuerdas** de época. Se toma la **idea**, no las canciones:
- Toda la música es **original**, hecha con su generador de canciones.
- No se versionan canciones con derechos (ni de Bridgerton ni de nadie).
- No se piden imitaciones de artistas concretos.

**Instrumentos:** cuarteto de cuerdas (con violonchelo al frente en lo íntimo), clave o pianoforte, arpa y algo de flauta. Nada de sintetizadores en la música de juego.

**Tema principal:** un motivo de 4 notas. Se repite en la portada, en el Gran Baile y en el epílogo.

**Tema de la *Hoja*:** un motivo de pizzicato con una nota desafinada a propósito. Suena cada vez que aparece el sobre o la *Hoja*.

| ID | Pista | Dónde suena | Duración | Bucle | Prompt para el generador |
|---|---|---|---|---|---|
| `mus_portada` | La Temporada del Sello | Portada | 1:30 | Sí | *Original instrumental, elegant Regency-era string quartet with pianoforte, playing a modern pop-style melody, hopeful and romantic, memorable 4-note main theme, 92 bpm, no vocals, no synths, high-quality chamber recording* |
| `mus_reina` | La proclamación | Apertura de la reina | 0:45 | No | *Original solemn but warm royal fanfare for string quartet and harp, short, regal, 70 bpm, no brass, no vocals* |
| `mus_mapa` | Valcenda por la mañana | Mapa, planificación | 2:30 | Sí | *Original calm, light string quartet and harpsichord, gentle waltz feel 3/4, curious and elegant, background music for planning, unobtrusive, 84 bpm, no vocals* |
| `mus_semana` | La semana en marcha | Mapa, ejecución | 2:00 | Sí | *Original lively string quartet with pizzicato and harpsichord, playful momentum, Regency ballroom energy with a modern pop rhythm, 112 bpm, no vocals* |
| `mus_incidente` | Algo pasa en el salón | Incidente | 1:00 | Sí | *Original tense chamber strings, suspenseful tremolo and pizzicato, elegant drama, not horror, 100 bpm, no vocals* |
| `mus_favorable` | Velada lograda | Sello favorable (golpe corto) | 0:06 | No | *Short original string-quartet flourish, bright, triumphant but delicate, 6 seconds* |
| `mus_medias` | A medias | Sello a medias | 0:06 | No | *Short original string-quartet phrase, wry, unresolved ending, 6 seconds* |
| `mus_desaire` | Un desaire | Sello de desaire | 0:06 | No | *Short original cello and viola phrase, gentle disappointment, falling line, 6 seconds* |
| `mus_cronica` | La Crónica de salones | Cierre público | 1:30 | Sí | *Original witty chamber music, harpsichord and pizzicato strings, gossipy and mischievous, 96 bpm, no vocals* |
| `mus_privado` | Sólo para sus ojos | Cierre privado | 1:30 | Sí | *Original intimate solo cello with soft piano, tender and reflective, 66 bpm, no vocals* |
| `mus_vinculo` | Un balcón | Escenas de vínculo | 2:00 | Sí | *Original romantic string quartet ballad with modern pop chord progression, yearning, soft, 72 bpm, no vocals* |
| `mus_hoja` | La Hoja sin Firma | El sobre y la *Hoja* | 1:00 | Sí | *Original mysterious pizzicato strings and celesta, one deliberately off note, intrigue, quiet, 88 bpm, no vocals* |
| `mus_faroles` | Noche de los Faroles | Semana 3 | 2:00 | Sí | *Original bittersweet folk-tinged string ensemble with flute, remembrance and celebration, lanterns by a river, 80 bpm, no vocals* |
| `mus_gran_baile` | El último vals | Gran Baile | 3:00 | Sí | *Original grand romantic waltz 3/4 for string orchestra and harp, based on a 4-note main theme, sweeping, emotional climax, 88 bpm, no vocals* |
| `mus_epilogo` | Lo sellado | Epílogo y créditos | 2:30 | No | *Original gentle finale for string quartet and piano, nostalgic, warm resolution of a 4-note main theme, 70 bpm, no vocals* |

**Alternativa sin generador:** valses de compositores en dominio público (Strauss II, Lanner, Waldteufel). La **composición** es libre, pero **la grabación tiene derechos propios**: hay que mirar la licencia de cada grabación en [Musopen](https://musopen.org/) antes de usarla.

---

## 2. Ambientes (bucles de 1 a 2 minutos)

| ID | Ambiente | Dónde |
|---|---|---|
| `amb_ciudad` | Ciudad de día lejana: carruajes, campanas, río | Mapa |
| `amb_salon` | Murmullo de salón, copas, abanicos | Recepción y baile |
| `amb_jardin` | Pájaros de otoño, hojas, agua de estanque | Paseo |
| `amb_imprenta` | Prensas de madera, papel, conversación baja | Imprenta |
| `amb_teatro` | Público que se acomoda, orquesta afinando | Teatro |
| `amb_noche` | Grillos, viento suave, un farol | Residencia de noche, gancho |
| `amb_lluvia` | Lluvia suave sobre tejado | Opcional (semanas 2 y 5) |
| `amb_muelles` | Agua, cuerdas de barco, gaviotas | Faroles (semana 3) |

## 3. Efectos de interfaz

| ID | Efecto | Cuándo |
|---|---|---|
| `sfx_sobre_abrir` | Papel que se despliega | Abrir una invitación |
| `sfx_carta` | Hoja de papel grueso | Abrir la carta completa |
| `sfx_carta_mano` | Naipe que se desliza | Repartir o tocar una carta de la mano |
| `sfx_asignar` | Naipe que se apoya en la mesa | Poner a alguien en un hueco |
| `sfx_quitar` | Naipe que se retira | Quitarlo |
| `sfx_lacre` | Sello que se presiona, y crujido de cera | Confirmar con el sello |
| `sfx_petalos` | Susurro suave | Pétalos del sello |
| `sfx_pluma` | Pluma que rasca | Nota de la asistente |
| `sfx_dia` | Campanada suave | Cambio de día |
| `sfx_aro_atencion` | Dos notas de arpa | Aparece un incidente |
| `sfx_pausa` | Cuerda que se apaga | Pausa |
| `sfx_error` | Toque seco de madera (nunca un zumbido) | Acción no permitida |
| `sfx_ficha_sube` | Tela que se desliza | Subir la ficha |
| `sfx_cronica` | Pliego que se despliega | Crónica |
| `sfx_sobre_puerta` | Papel que roza el suelo | Gancho de la semana 1 |
| `sfx_abanico` | Abanico que se abre | Expresión de Camila; detalles |
| `sfx_carruaje` | Ruedas sobre adoquín (corto) | Salen los viajes en el mapa |

## 4. Bibliotecas libres con uso comercial

| Biblioteca | Licencia | Atribución | Notas | Enlace |
|---|---|---|---|---|
| **Kenney** (sonidos de interfaz, cartas, impacto) | CC0 | No hace falta (se agradece «Kenney.nl») | La más segura. Usar la descarga original de kenney.nl, no copias en otros sitios | https://kenney.nl/assets?q=audio · [Interface Sounds en OpenGameArt](https://opengameart.org/content/interface-sounds) |
| **Freesound** | **Cada sonido tiene la suya**: CC0, CC-BY o CC-BY-NC | Sí con CC-BY | **Filtrar por «Creative Commons 0»** o CC-BY. **Nunca CC-BY-NC** (no comercial) | https://freesound.org |
| **Pixabay** (música y efectos) | Pixabay Content License | No | Se permite usar dentro del juego, pero no revender el archivo suelto. **Leer la licencia oficial antes de usarla** | https://pixabay.com/sound-effects/ |
| **Sonniss GDC Game Audio Bundle** | Libre de regalías, comercial y para siempre | No | Prohibido entrenar IA con los sonidos y redistribuirlos sueltos. Muy buena calidad para ambientes | https://sonniss.com/gameaudiogdc |
| **OpenGameArt** | Cada recurso tiene la suya | Según la licencia | Filtrar por CC0 | https://opengameart.org |
| **Musopen** | Cada grabación tiene la suya | Según la grabación | Sólo para música clásica | https://musopen.org |

**No usar:** BBC Sound Effects (su licencia es no comercial) ni sonidos sacados de vídeos o películas.

**Registro obligatorio:** el archivo `proyecto/audio/CREDITOS-AUDIO.csv` debe tener una fila por sonido con estas columnas: `id, archivo, fuente, autor, licencia, url, fecha_descarga`. Así se puede auditar cada licencia.

## 5. Formato técnico

- **Formato:** OGG Vorbis a 44,1 kHz. Música en estéreo a ~160 kbps; efectos en mono.
- **Volumen:** música a −16 LUFS, efectos y ambientes a −20 LUFS.
- Música y efectos tienen controles independientes en ajustes.
- La música hace un fundido de 1,5 s entre pistas, y el ambiente sigue al lugar en pantalla.
- Con «movimiento reducido» los sonidos no cambian, pero con el sonido silenciado **todo debe seguir entendiéndose** sin oír nada.

Fuentes consultadas:
- [Cinevva: guía de sonidos libres 2026](https://app.cinevva.com/guides/free-sound-effects-music)
- [Rekkerd: Sonniss GDC 2026](https://rekkerd.org/sonniss-releases-gdc-2026-game-audio-bundle/)
- [GameFromScratch: Sonniss 2024](https://gamefromscratch.com/sonniss-27-5gb-sound-effect-giveaway-at-gdc-2024/)
- [Kenney Interface Sounds (GitHub)](https://github.com/Calinou/kenney-interface-sounds)
- [Wikipedia: Musopen](https://en.wikipedia.org/wiki/Musopen)
- [La Fabrique du Net: Pixabay Music](https://www.lafabriquedunet.fr/logiciel/pixabay-music)
