# Salverna · Paquete de cierre (14 oct. 2026)

Juego narrativo para móvil en vertical. Usted es la casamentera de ocho jóvenes durante una temporada de 6 semanas en Valcenda. **La historia está completa**, del capítulo 1 al 6, en español y en inglés. Antes de programar quedan unas correcciones; la lista está más abajo.

## Qué leer y en qué orden

1. `proyecto/canon/ARCO-TEMPORADA.md`: la historia de principio a fin. Es la brújula.
2. `proyecto/canon/CANON.md`: personajes, mundo, reglas de estilo y la verdad del misterio.
3. `proyecto/guion/*.es.md` (y `.en.md`): **los guiones legibles**. Están las 6 semanas, el tutorial y las escenas de vínculo C, B y A más el capítulo 5 (besos, confesiones y acuerdos). La historia también está aquí.
4. `produccion/LECTURA-COMPLETA-v1.md`: el diagnóstico de la lectura completa. **Ahí está lo que hay que corregir.**
5. `produccion/PENDIENTES.md`: el estado de cada capítulo y lo que necesita el motor.
6. `proyecto/sistemas/SISTEMAS.md` y `proyecto/datos/ESQUEMA.md`: las reglas con números y el formato de los datos.

## Para quien programa

- **Los datos de verdad** son los YAML de `proyecto/datos/`. No se editan los `.md` del guion: se generan.
- **Compilar:** `python3 herramientas/compilar_datos.py`. Valida y genera `proyecto/datos/json/` (lo que lee el motor) y `proyecto/guion/`.
- **Equilibrio:** `python3 herramientas/simular_eventos.py N` simula los eventos de la semana N.
- **Diseño:**
  - `diseno/maqueta/`: la maqueta HTML y los retratos recortados;
  - `diseno/figma-make/`: la guía y los mensajes para Figma Make;
  - `proyecto/interfaz/FLUJO-Y-MENUS.md`: el flujo de pantallas;
  - `proyecto/arte/`: el inventario de imágenes y las tipografías;
  - `proyecto/audio/AUDIO.md`: el audio.

## Correcciones pendientes, por orden (detalle en `LECTURA-COMPLETA-v1.md`)

| # | Gravedad | Qué | Dónde | Dirección recomendada |
|---|---|---|---|---|
| 1 | 🔴 | ¿Acepta Valcenda las uniones entre dos hombres o dos mujeres? Hoy el acuerdo lavanda y el Gran Baile se contradicen | `CANON.md` §3.3; `semana3.yaml` (Faroles); `semana6.yaml` (`propuestas`) | **Decisión de canon:** la costumbre de las casas no las acepta; la reina sí, y es reformista. Insinuarlo en la Velada de los Faroles (una frase de la reina sobre «registros que dicen la verdad de cada uno») y en el Gran Baile hacer del sello un acto público valiente. Lavanda queda como la salida de quien no se atreve |
| 2 | 🔴 | La confrontación cuenta pistas que no son de Irene | `semana6.yaml` (`confrontacion`); `compilar_datos.py` | Renombrar `pista_sello_umbral` → `dato_umbral` y `pista_clara_nacar` → `dato_clara_nacar`, en `semana3.yaml`, `semana5.yaml` y donde se usen |
| 3 | 🔴 | Irene «falta» al teatro aunque esté en el palco | `semana4.yaml`, `s4_teatro`, opción `observar` | Dar dos textos de éxito según `asiste(irene)`; si está, «falta un caballero que siempre llega primero» |
| 4 | 🟠 | El misterio se resuelve en el capítulo 2 | `semana2.yaml` (cena y notas), `semana4.yaml` (recuerdos) | Quitar «letra pequeña y muy ordenada» de la nota de Irene del capítulo 2 y de un recuerdo del capítulo 4. Dejarla sólo en el escribiente y en la nota del capítulo 5 |
| 5 | 🟠 | «Vinculado a Irene» es ambiguo | `semana6.yaml` | Cambiar `nivel_max(irene) >= B` por `marca(irene_agradecida) o marca(irene_casi_confiesa)`: la confianza de Irene en la casamentera, no en otro |
| 6 | 🟠 | Hilos abiertos: el favor de Amalia, la entrevista de Mara, «entregar los folios», qué es Amalia | `semana6.yaml` | Si hay `favor_amalia`, Amalia pide en el Gran Baile un vals con Dario: aceptarlo o no. La entrevista de Mara cambia una línea de su nota final. «Entregar» tiene su epílogo: la reina publica los abusos y guarda el Pacto. Una línea en el epílogo de Dario confirma, sin nombrarlo, la naturaleza de Amalia |
| 7 | 🟠 | Contradicciones entre rutas | `vinculos_B.yaml`, `vinculos_A.yaml`, `capitulo5.yaml` | Celia: «el primero que no he contado» sólo si `no nivel(dario, celia) >= C`. Teo: el cuaderno es «para una dama» sin decir cuál. Irene: una frase distinta para Teo |
| 8 | 🟠 | El Gran Baile es pasivo | `semana6.yaml` | Añadir un incidente cuando cae la *Hoja* final: recogerla, leerla en voz alta o bailar encima |
| 9 | 🟠 | Fechas: el incendio el 14 frente a los Faroles el 13; «once páginas» frente a los folios 80–84; el calendario viejo del canon | `semana4/5.yaml`, `semana1.yaml`, `CANON.md` §6 | Faroles el 14 (domingo); «faltan cinco folios»; borrar la tabla vieja del §6 |
| 10 | 🟠 | El equilibrio de los obligatorios de las semanas 4 y 5 | `SISTEMAS.md` §3.1 | Probar el +1 por segundo asistente sólo si tiene ≥ 4 |
| 11 | 🟠 | La habilidad Baile casi no se usa; la casamentera no tiene arco propio | Semanas 3–6 | Una opción de Baile por semana. Una decisión personal de la casamentera en el capítulo 5: aceptar el despacho de la reina, o no |
| 12 | 🟢 | Repeticiones: «por primera vez» (más de 30), «que es peor», «no dice nada», «Bruna…» | Todos los YAML | Una pasada de estilo con búsqueda de texto. Dejar como mucho una por capítulo |
| 13 | 🟢 | Una revisión del inglés por un hablante nativo | Todos los YAML | — |

**Después de corregir:** compilar (0 errores), simular las semanas 1 a 6 y releer los guiones.
