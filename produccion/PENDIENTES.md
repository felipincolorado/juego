# Salverna · Lista de pendientes (memoria)

Se actualiza al terminar cada sesión. **Lo que espera tu decisión va primero.**

## A. Decisiones tuyas (bloquean o cambian contenido)

| # | Pendiente | Mi propuesta por defecto | Dónde está |
|---|---|---|---|
| 1 | **Revisar la semana 1** (guion, comentarios y fichas) | — | `proyecto/guion/semana1.es.md`, `textos/barks.yaml`, `textos/fichas.yaml` |
| 2 | Autoría de *La Hoja sin Firma* | Irene (D5) | `DECISIONES.md` |
| 3 | Dario: humano o nocturno | Humano (D4) | `DECISIONES.md` |
| 4 | Motivo de la unión lavanda Saúl–Isolda | Alianza de convoyes (D3) | `DECISIONES.md` |
| 5 | Nilo y Celia (primos) | Ruta secundaria, desactivable (D6) | `DECISIONES.md` |
| 6 | Orientaciones, nombres y edades del elenco | Las propuestas (D1, D2, D7) | `DECISIONES.md` |
| 7 | Nombres inventados: meses (Vendimias, Nieblas, Escarchas), Salón de las Columnas, Teatro del Puente, Academia de la Puerta de Greda, Julián Ferrán y el *Clara de Nácar*, Oriana Vell | Mantenerlos | `canon/CANON.md` |
| 8 | **Peticiones semanales** de los personajes («Nilo quiere ir al paseo») | Sí, desde la semana 2 | `REVISION-CRITICA-SEMANA1.md` M6 |
| 9 | **Encuentro a medida** pagado con reputación | Sí, desde la semana 4, por 3 de reputación | M7 |
| 10 | **Minijuego de la cartomante** | Sí, desde la semana 2; diseño listo | `sistemas/MINIJUEGO-ADIVINA.md` |
| 11 | Pista del carruaje con las cortinas echadas (apunta a Dario y es pista falsa) | Mantenerla | M10 |
| 12 | Cartas entre personajes | No en la versión 1 (D12) | `DECISIONES.md` |
| 13 | Modelo de venta | Gratis con las semanas 1–2 y temporada completa a US$5,99, sin anuncios | `COMERCIALIZACION.md` |
| 14 | Nombre comercial | «Salverna: La Temporada del Sello», con subtítulo en la tienda | `COMERCIALIZACION.md` |
| 15 | Motor del juego (Ren'Py o web con TypeScript) | Se decide en el plan de programación (E12) | `PLAN-MAESTRO.md` |

## B. Tareas tuyas fuera de aquí

| # | Tarea | Notas |
|---|---|---|
| 1 | **Generar los 8 originales** con ChatGPT | `diseno/PROMPTS-ELENCO-ORIGINALES.md`, un chat por personaje. Corregir con `--solo-blancos 0.85` |
| 2 | **Corregir en Figma el texto de la secretaria** del marco v4 (`83:536`): «Estas son vuestras ocho jóvenes. Tocad…» | Usa «vosotros» y femenino. Texto correcto en `textos/tutorial.yaml` |
| 3 | Comprobar las licencias oficiales de Pixabay, Sonniss y Musopen antes de descargar audio | `proyecto/audio/AUDIO.md` |
| 4 | Generar la música con tu generador de canciones | 15 prompts en `AUDIO.md` |

## C. Trabajo mío pendiente (por orden)

1. Con tu revisión de la semana 1: **semanas 2 a 6** (E5), incluyendo:
   - viajes de varios días;
   - el primer reemplazo;
   - las peticiones;
   - la cartomante.
2. **Escenas de vínculo** (E6) y **Gran Baile y finales** (E7).
3. **Prompts de las tandas 3 y 4**: la reina, Oriana, las cartas de la cartomante, la cabecera de la Crónica y las imágenes de escena.
4. **Plan de programación** (E12): motor, arquitectura, orden de implementación, demo de la semana 1, criterios de aceptación y pruebas.
5. **Repaso del flujo en Figma** o en una maqueta HTML. Incluye las pantallas que faltan: ficha, incidente, resultado, Crónica, carnet de baile y la mesa de la cartomante.
6. **Prueba de juego** con 5–10 personas antes de producir todo: medir el balance real.

## Capítulo 2 · terminado (14 oct.)

- `semanas/semana2.yaml`: apertura con decisión, 2 peticiones, 3 eventos (excursión de 2 días, cena con pista, baile obligatorio de dos parejas), incidentes con 3 opciones y consecuencias, indisposición y reemplazo, Crónica nº 2, *Hoja* nº 1 (8 secretos posibles), «Sólo para sus ojos» y gancho.
- `escenas/vinculos_C.yaml`: 10 escenas C (las 7 prioritarias y 3 de parejas que parten con cercanía 2), más una genérica.
- Simulación de la semana 2: con la mejor opción, entre el 68 % y el 80 % de desenlaces favorables; con la peor, entre el 17 % y el 52 %.
- **Falta para el motor:** implementar la fama (sistemas §5 bis), las peticiones (§5 ter), la regla `parejas` y la elección de `indisposicion.quien`.
- **Siguiente:** capítulo 3 (Noche de los Faroles), con las escenas B.

## Capítulo 3 · terminado (14 oct.)

- `semanas/semana3.yaml`:
  - parte 1: recuerdos de la semana 2, decisión sobre Mara, peticiones de Camila y Celia, subasta del lote 12 y clase de protocolo;
  - parte 2: barcas al atardecer (pista del taller de Arcos Bajos), Velada de los Faroles con la reina (obligatoria, 3 plazas), Crónica nº 3, Hoja nº 2 (páginas del Pacto, folio 81), «Sólo para sus ojos» y gancho hacia el plenilunio.
- `escenas/vinculos_B.yaml`: 10 escenas B, en las que pasan al tú, más una genérica. Marcas nuevas que usarán los capítulos 4 y 5: `celia_cubre_nilo` (permite evitar el incidente de Nilo el día 20), `lavanda_hablada`, `saul_sin_guantes` y `celia_error_tapado`.
- Simulación de la semana 3: con la mejor opción, entre el 53 % y el 78 % de desenlaces favorables.
- **Siguiente:** capítulo 4 (Luna llena), en dos partes.

## Capítulo 4 · terminado (14 oct.)

- `semanas/semana4.yaml`:
  - apertura: recuerdos de la semana 3 y el té con Amalia Miravés (decisión);
  - peticiones: Nilo pide que no lo manden a nada el día 20 (`no_asistir`); Isolda quiere ir al teatro si va Irene (`requiere_con`);
  - eventos:
    - cena entre prensas en casa de Mara (juego de sospechas; Irene llega con tinta de imprenta en los dedos);
    - tiro con arco (la conversación seria de Teo);
    - **primera visita privada** (sólo parejas en nivel B, con variantes para las 7 parejas);
    - **teatro de gala**, obligatorio, con dos parejas y un `incidente_riesgo` que sustituye al normal si va Nilo: Nilo se va y el grupo cuenta sin él;
  - cierre: Crónica nº 4, Hoja nº 3 («alguien no es lo que aparenta»: apunta a Dario y roza a Nilo si lo vieron), 8 notas privadas y gancho hacia la semana 5 (tormentas, deuda de Camila, correo de Tiria para Saúl).
- `escenas/vinculos_A.yaml`: 6 escenas A de parejas con atracción mutua y una genérica.
- Simulación de la semana 4: con la mejor opción, entre el 66 % y el 69 % de desenlaces favorables. Si va Nilo al teatro, con la peor opción no hay ningún favorable.
- Marcas que usará el capítulo 5: `nilo_visto`, `nilo_cubierto`, `nilo_confia`, `amalia_conocida`, `amalia_saludada`, `teo_conversacion_seria`, `teo_bufon`, `isolda_hablo_primero`, `camila_espera_secreto`, `dario_sin_mascara`, `nombres_protegidos`, `pista_archivera`, `pista_ausencias`.
- **Siguiente:** capítulo 5 (Cierre de Cuentas): la cena de las deudas, los motivos de las uniones sin amor (el acuerdo lavanda, el compromiso del paso y la deuda), los besos y las confesiones no correspondidas.

## Capítulo 5 · terminado (14 oct.)

- `semanas/semana5.yaml`:
  - apertura: la orden de Tiria para Saúl (volver al ejército salvo que selle un compromiso) y la entrevista de Mara (decisión);
  - peticiones: la prueba de Nilo (su casa o la promesa a Camila, sólo si llegaron al nivel B) y Camila pide ir a la cena;
  - eventos:
    - clase de voz (+1 Presencia);
    - llegada de los convoyes, el motivo de la unión lavanda;
    - lectura de capitulaciones, el compromiso del paso. Irene está de guardia con un pliego en el delantal;
    - **cena de las deudas**, obligatoria: la deuda del *Clara de Nácar* y el secreto de los Marén;
    - última visita privada;
  - cierre: Crónica nº 5, Hoja nº 4 («llevará nombres»; la hora y la sala del incendio sólo constan en el registro interno; se suaviza si Irene crece), 7 notas privadas y gancho: el carnet de baile y la nota de Irene, «venga al Archivo antes del baile».
- `escenas/capitulo5.yaml`: 6 besos, 2 confesiones no correspondidas (Dario a Isolda; Celia a Saúl), una confesión genérica y 3 acuerdos sin amor (la lavanda Saúl–Isolda, el compromiso del paso Saúl–Celia y la deuda Teo–Camila).
- **Equilibrio pendiente:** con la mejor opción, la cena de las deudas sale favorable el 94 % de las veces. La fórmula topa en 5, y con tres personas casi siempre se cubre el requisito. Habría que revisar §3.1 (el +1 por segundo asistente) antes de programar, o aceptarlo, porque en los obligatorios lo que está en juego es la historia.
- **Siguiente:** capítulo 6 (Gran Baile del Sello): el carnet de baile, la confrontación con Irene en el Archivo, «Proteger los nombres», las propuestas y los epílogos de las 8 vidas.
