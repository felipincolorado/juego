# Salverna · Plan maestro de producción

**Creado el 13 de octubre de 2026.** Este archivo es la **memoria del proyecto**. Toda sesión de trabajo empieza leyéndolo y termina actualizando la tabla de estado y el «siguiente paso».

## Objetivo

Construir el **paquete completo** para que otra persona (o ChatGPT) programe *Salverna* sin preguntar nada: canon, sistemas con números, datos, diálogos bilingües, escenas, finales, interfaz, audio, tipografías, inventario de imágenes y guía de implementación. Las imágenes las genera ChatGPT con los prompts de `diseno/`.

## Reglas de trabajo

1. **Una etapa por vez.** Cada etapa termina con un commit, la tabla de estado al día y una autocrítica breve.
2. **Lo escrito es propuesta.** El usuario aprueba o corrige. Las decisiones tomadas por defecto se marcan como tales y se registran en [DECISIONES.md](<DECISIONES.md>).
3. **Bilingüe desde el origen:**
   - Cada texto tiene un ID y sus versiones `es` y `en`.
   - El español es la versión maestra; el inglés es una adaptación natural con el mismo sentido y registro, no una traducción literal.
4. **Contenido como datos:** cada texto del juego vive en archivos estructurados (`proyecto/datos/`, JSON o YAML), además de una versión legible para revisar.
5. **Primero una porción vertical:** la semana 1 se escribe completa (todos los textos, misiones y resultados) y se revisa antes de producir las semanas 2–6.
6. **Antes de escribir pistas o finales, se cierra el canon.** No se escribe nada que dependa de una decisión abierta.

## Etapas

| # | Etapa | Entregables | Estado |
|---|---|---|---|
| E0 | Plan y memoria | Este archivo, `DECISIONES.md` | ✅ Hecho |
| E1 | **Canon cerrado** | `proyecto/canon/`: mundo resumido (desde `produccion/fuentes/ENTREGA-INTEGRAL-SALVERNA-2026-10-13.md`), elenco definitivo, glosario, calendario, misterio de la *Hoja* resuelto | ✅ v1 (`proyecto/canon/CANON.md`) |
| E2 | **Diseño de sistemas con números** | `proyecto/sistemas/`: semana y día, plazas, habilidades 0–5, fórmula de resultado de evento, cercanía, umbral romántico, reputación, cansancio, incidentes, Gran Baile, guardado | ✅ v1 (`proyecto/sistemas/SISTEMAS.md`) |
| E3 | **Modelo de datos y convención de textos** | `proyecto/datos/ESQUEMA.md`: personajes, eventos, escenas, líneas, condiciones, variables, IDs, formato ES/EN, género y concordancia | ✅ v1, más el validador `herramientas/compilar_datos.py` |
| E4 | **Semana 1 completa** (porción vertical) | Tutorial, apertura de la reina, invitaciones, misiones con opciones y resultados, comentarios en el mapa, escenas, crónica y gancho de la *Hoja*, en ES y EN | ⏳ Escrita; pendiente de **revisión del usuario** |
| E5 | Semanas 2–6 | Mismo contenido que E4 por semana; eventos obligatorios de historia | Pendiente |
| E6 | Escenas de vínculo | C, B, A, beso y propuesta de las parejas prioritarias y secundarias; acuerdo lavanda; confesiones no correspondidas; amistad y rivalidad | Pendiente |
| E7 | Gran Baile y finales | Carnet de baile, reacciones al doble beso, propuestas, crónica final, 67 epílogos de unión, 16 finales en solitario, reputación y resolución del misterio | Pendiente |
| E8 | **Interfaz y flujo** | Árbol de menús, todas las cadenas de interfaz en ES y EN, pantallas con tamaños (de `ESPEC-FLUJO-PANTALLAS-v3` y Figma v4), estados y transiciones; repaso final del flujo en Figma o en un prototipo HTML | ◐ Cadenas de interfaz escritas (`textos/ui.yaml`); falta el árbol de menús y el repaso del flujo |
| E9 | **Audio** | Lista de pistas musicales con prompts para el generador de canciones, lista de efectos y ambientes, fuentes libres **con licencia comercial verificada** y enlaces | Pendiente |
| E10 | Tipografías | Fuentes con licencia OFL comprobada, usos y tamaños, enlaces de descarga | Pendiente |
| E11 | Inventario de imágenes | Todas las imágenes: ID, archivo, tamaño, capa, prompt, estado | Pendiente |
| E12 | **Paquete para el programador** | `proyecto/LEEME-PROGRAMADOR.md`: arquitectura sugerida, motor, orden de implementación, criterios de aceptación y lista de pruebas | Pendiente |

**Orden:** E1 → E2 → E3 → E4 (revisión) → E5–E7. E8–E11 se intercalan cuando haya pausas de revisión. E12 va al final.

## Volumen estimado

Unas **55 000–65 000 palabras en español** y otras tantas en inglés. Incluye unos 400 comentarios breves, unas 30 invitaciones con resultados, 6 escenas de historia, unas 70 escenas de vínculo, 40 noticias de crónica, 5 *Hojas*, 83 cierres y la interfaz. Por eso se escribe por semanas y se revisa la primera.

## Motor (recomendación para E12, sin bloquear nada)

- Los archivos **Ren'Py** del juego anterior se movieron a `archivo/juego-anterior/`, intactos.
- Ren'Py encaja con un juego narrativo: diálogos, guardado y traducción integrada, con exportación a Android. El mapa con cartas sería un desarrollo propio con sus «screens».
- Alternativa: TypeScript con un empaquetador web para iOS y Android. Da más control de la interfaz, pero hay más que programar.
- **Los datos de E3 serán neutrales** (JSON más tablas de textos), para servir a cualquiera de los dos.

## Siguiente paso

La lista viva de pendientes está en [PENDIENTES.md](<PENDIENTES.md>), que se actualiza en cada sesión. Resumen:
1. El usuario revisa la semana 1 y confirma las decisiones por defecto.
2. Se escriben las semanas 2–6 (E5), con viajes largos, reemplazo, peticiones y la cartomante (`sistemas/MINIJUEGO-ADIVINA.md`).
3. Plan de programación (E12).
