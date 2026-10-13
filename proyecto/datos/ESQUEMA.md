# Salverna · Esquema de datos y convención de textos (v1)

Todos los datos del juego viven en **YAML** dentro de `proyecto/datos/`. La herramienta `herramientas/compilar_datos.py` hace tres cosas:
- **valida** los archivos;
- los **exporta a JSON** (`proyecto/datos/json/`), que es lo que carga el motor;
- genera un **guion legible** (`proyecto/guion/`) para revisarlos.

El motor no necesita leer YAML.

---

## 1. Textos

### 1.1 Texto bilingüe

Todo texto visible es un objeto con las dos lenguas:

```yaml
texto: { es: "Lo he ensayado.", en: "I've rehearsed this." }
```

- Si falta una lengua, la validación da error.
- El español es la versión maestra.
- El inglés adapta la intención, no traduce palabra por palabra.

### 1.2 Variables

| Variable | Valor |
|---|---|
| `{a}`, `{b}`, `{c}`, `{d}` | Nombre de pila de los asistentes, en el orden de las plazas |
| `{mejor}` | En incidentes: el asistente con el valor más alto en la habilidad de la opción elegida (si hay empate, la primera plaza). En un desenlace, quien actuó en el incidente |
| `{grupo}` | Los asistentes enlazados: «Saúl e Isolda» · «Saul and Isolda» |
| `{amada}` | La persona amada (finales no correspondidos) |
| `{dia}` | El número del día |
| `{lugar}` | El nombre del lugar |
| `{rep}` | El cambio de reputación con signo («+2») |

**Regla del conector «y» → «e»:** delante de una palabra que empieza por sonido /i/ («Irene», «Isolda», «hijos») se escribe «e». Lo aplica la función que construye `{grupo}`.

### 1.3 Concordancia de género

Formato `{x|forma_masculina|forma_femenina}`, donde `x` es una variable de persona:

```yaml
es: "{a} llegó {a|cansado|cansada}."
en: "{a} arrived {a|tired|tired}."
```

En inglés sólo hace falta para los pronombres: `{a|he|she}`, `{a|his|her}`, `{a|him|her}`.

Género de cada persona:
- Masculino: Nilo, Saúl, Dario, Teo.
- Femenino: Celia, Irene, Isolda, Camila.
- La casamentera siempre se trata en femenino.

### 1.4 Variantes por condición

Cualquier texto puede llevar variantes. **Gana la primera** cuya condición se cumple; si no se cumple ninguna, se usa `texto`.

```yaml
texto: { es: "…", en: "…" }
variantes:
  - si: "asiste(celia) y asiste(teo)"
    texto: { es: "…", en: "…" }
```

---

## 2. Lenguaje de condiciones

Expresiones simples, unidas con `y`, `o` y `no`:

| Función | Significado |
|---|---|
| `asiste(id)` | La persona está asignada al evento actual |
| `asistio(evento, id)` | Asistió a ese evento esta temporada |
| `desenlace(evento) == favorable/medias/desaire` | Resultado guardado de ese evento |
| `opcion(evento) == id` | Opción elegida en su incidente |
| `cercania(id1, id2) >= n` | Cercanía de la pareja |
| `nivel(id1, id2) >= C/B/A` | Nivel de vínculo |
| `rep >= n` | Reputación de la casamentera |
| `marca(nombre)` | Marca de historia activa |
| `semana == n` | Semana actual |
| `estado(id) == agitada/indispuesta` | Estado de una persona |
| `gusta(id)`, `no_gusta(id)` | El tipo del evento actual le gusta o no le gusta |

---

## 3. Líneas de diálogo

```yaml
- habla: celia            # id de personaje · "reina" · "nota" (la asistente) · null (narración)
  expr: molesta           # neutral · alegre · molesta · ruborizada
  es: "No, no, no. Esto no estaba en lo que ensayé."
  en: "No, no, no. This wasn't in what I rehearsed."
```

- Una línea equivale a un toque, con un máximo de **3 líneas visibles**.
- Si `habla` es una plaza (`a`, `b`…), habla quien ocupe esa plaza.
- La expresión es la del retrato de quien habla.

---

## 4. Archivos y estructura

| Archivo | Contenido |
|---|---|
| `personajes.yaml` | Elenco y recurrentes: habilidades, ejes, gustos, género, casa, cercanía de partida, orientación (sólo autoría) |
| `lugares.yaml` | Lugares del mapa: id, nombre ES/EN, barrio, tipo y si tiene edificio dibujado |
| `textos/ui.yaml` | **Todas** las cadenas de interfaz, con claves jerárquicas |
| `textos/tutorial.yaml` | Pasos del tutorial: disparador, qué se resalta y quién habla |
| `textos/barks.yaml` | Comentarios del elenco por situación, con 2 o más variantes |
| `textos/fichas.yaml` | Las 6 entradas de cada ficha, con su condición de desbloqueo |
| `semanas/semanaN.yaml` | Hechos del reino, eventos completos (carta, hoja, incidente y desenlaces), Crónica, cierre privado y gancho |

### 4.1 Evento (dentro de `semanaN.yaml`)

```yaml
- id: s1_recepcion
  tipo: recepcion
  lugar: palacio
  dia: 29
  duracion: 1
  plazas: { min: 2, max: 2 }
  regla: dama_caballero
  obligatorio: true
  requisito: { estatus: 4, presencia: 4, baile: 3 }
  anfitrion: { es: "La Corona", en: "The Crown" }
  titulo: { es: "…", en: "…" }
  resumen: { es: "…", en: "…" }        # una línea en la hoja
  a_favor: [{ es: "…", en: "…" }]      # líneas «+» de la hoja
  en_contra: [{ es: "…", en: "…" }]    # líneas «−» de la hoja
  carta: { saludo: {…}, cuerpo: {…}, firma: {…} }
  incidente:
    dia: 29
    situacion: { es: "…", en: "…" }
    cita: { habla: a, expr: molesta, es: "…", en: "…" }
    opciones:
      - id: conversacion
        habilidad: presencia
        d: 4
        texto: { es: "…", en: "…" }
        exito: { es: "…", en: "…" }
        medias: { es: "…", en: "…" }
        fallo: { es: "…", en: "…" }
  desenlaces:
    favorable: { titulo: {…}, publico: {…}, privado: {…} }
    medias:    { titulo: {…}, publico: {…}, privado: {…} }
    desaire:   { titulo: {…}, publico: {…}, privado: {…} }
    sin_asistentes: { publico: {…} }    # sólo en los obligatorios
```

La reacción del personaje en el resultado sale de sus comentarios (`bark.bien`, `bark.medias`, `bark.mal`). El evento no la repite.

### 4.2 Claves de interfaz

Las claves usan puntos: `hoja.boton.carta`, `ajustes.idioma`. El motor resuelve `ui("hoja.boton.carta")` según el idioma activo. **Ningún texto visible se escribe dentro del código.**

---

## 5. Campos añadidos al escribir la semana 1

| Campo | Dónde | Significado |
|---|---|---|
| `efectos: [marca, …]` | En un desenlace, una variante o el gancho | Marcas de historia que se activan si ese texto se muestra |
| `mejora: {habilidad, cantidad, tope}` | Eventos de tipo `clase` | Mejora de habilidad de cada asistente |
| `completada: {publico, privado}` | Eventos de tipo `clase` | Sustituye a `desenlaces`, porque las clases no tienen resultado |
| `cita: {habla: a, bark: incidente}` | En un incidente | Quien ocupa esa plaza dice una de sus frases de esa situación |
| `noticias[].fija · relleno · usa_desenlace_publico · usa_completada_publico` | En la Crónica | Cómo se compone: primero las fijas, después el obligatorio, luego los opcionales con asistentes y, por último, el relleno hasta llegar a 3 noticias (máximo 4) |
| `asistio(evento, *)` | Condiciones | Asistió alguien a ese evento |
| `objetos` | Por semana | Cartas o documentos que se pueden releer en la residencia |
| `objeto_guardado` | En un paso del tutorial | Guarda ese objeto al terminar el paso |

**Orden de las plazas en `dama_caballero`:** la plaza `a` es el caballero y la `b` es la dama.
