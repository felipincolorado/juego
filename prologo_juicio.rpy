## =============================================================================
## THE GILDED CAGE - PRÓLOGO (Solo Labels)
## Ubicación: game/src/chapters/prologo_juicio.rpy
## Requiere: config.rpy, characters.rpy, assets.rpy
## =============================================================================

# =============================================================================
# ACTO 0: EL VACÍO (MUERTE)
# =============================================================================
label prologo_muerte:
    
    window show
    scene bg black with fade
    stop music fadeout 1.0
    stop sound fadeout 1.0

    if renpy.loadable("assets/audio/sfx/heartbeat_fading.ogg"):
        play sound "assets/audio/sfx/heartbeat_fading.ogg" fadein 0.8

    narrator "{i}Frío.{/i}"
    narrator "{i}El veneno corre por tus venas.{/i}"
    narrator "{i}No puedes respirar.{/i}"
    narrator "{i}Todo... se apaga...{/i}"

    stop sound fadeout 0.8
    centered "{size=32}{i}...{/i}{/size}"

    if renpy.loadable("assets/audio/sfx/reincarnation_surge.ogg"):
        play sound "assets/audio/sfx/reincarnation_surge.ogg"

    scene bg white with Dissolve(0.2)
    pause 0.5

    jump prologo_tribunal

# =============================================================================
# ACTO I: EL JUICIO
# =============================================================================
label prologo_tribunal:

    scene bg courtroom with Dissolve(0.8)

    if renpy.loadable("assets/audio/music/church_of_thorns_theme.ogg"):
        play music "assets/audio/music/church_of_thorns_theme.ogg" fadein 1.2

    centered "{size=28}{color=#8B4513}TRIBUNAL INQUISITORIAL{/color}\n{size=22}Iglesia de las Espinas • Basaltia\nAño 347 desde la Fundación{/size}{/size}"
    pause 1.0

    narrator "{i}Parpadeas.{/i}"
    narrator "{i}Luz cegadora.{/i}"

    if renpy.loadable("assets/audio/sfx/gavel_heavy.ogg"):
        play sound "assets/audio/sfx/gavel_heavy.ogg"
    with vpunch

    show judge neutral at char_center with dissolve
    
    j "El acusado ingirió {color=[TGC_GOLD]}Verum{/color}."
    j "Ritual completado."
    
    show judge suspicious at char_center with dissolve
    j "Sin reacción."
    j "Se declara {b}deceso{/b}."

    if renpy.loadable("assets/audio/sfx/crowd_murmur_approval.ogg"):
        play sound "assets/audio/sfx/crowd_murmur_approval.ogg"

    show bridia neutral at char_left behind judge with dissolve
    
    narrator "{i}En el estrado, una mujer de túnica azul profundo.{/i}"
    narrator "{i}No mira al hierarca. Te observa a ti.{/i}"

    narrator "{i}Tu mano se mueve.{/i}"
    
    if renpy.loadable("assets/audio/sfx/chains_rattle.ogg"):
        play sound "assets/audio/sfx/chains_rattle.ogg"

    acolito "(Susurro) S-señor... el cuerpo..."
    acolito "El cuerpo {b}respira{/b}."

    show judge angry at focus_close with dissolve
    j "¿{i}Qué{/i}?"

    show bridia worried at char_left with dissolve
    
    narrator "{i}La mujer de azul se acerca al frasco vacío.{/i}"
    narrator "{i}Respira. Pausa. Vuelve a respirar.{/i}"

    show bridia serious at char_left with dissolve
    b "Ese frasco... el olor no es el mío."
    b "Pido {b}suspensión{/b} para verificarlo."

    show judge angry at focus_close with dissolve
    j "Incomprobable ahora."
    j "El acusado {b}murió{/b} bajo {i}tu{/i} alquimia."

    show inquisitor neutral at char_center behind bridia with dissolve
    inq "Conveniente."
    inq "Tus dos {i}fallos{/i} previos pesan."
    inq "Un tercero te quitaría la voz."

    narrator "{i}Respiras. Aire áspero. Vuelves.{/i}"

    if renpy.loadable("assets/audio/sfx/crowd_gasp.ogg"):
        play sound "assets/audio/sfx/crowd_gasp.ogg"

    show judge suspicious at char_right with dissolve
    j "...Vive."

    show bridia neutral at char_left with dissolve
    b "Entonces procede el {i}interrogatorio{/i}."

    # -------- INTERROGATORIO: NOMBRE --------
    j "Acusado."
    j "{b}Nombre{/b}."

    $ player_name = ""
    $ _ok = renpy.call_screen("name_input")
    
    if not player_name or player_name.strip() == "":
        $ player_name = "Aleric"

    p "...{b}[player_name]{/b}."
    
    j "Ocupación."

    # -------- SUGERENCIA DE BRIDIA --------
    show bridia smirk at char_center with move
    b "{size=-6}(Bajo) Di 'Aprendiz de Rosa Azul'.{/size}"
    b "{size=-6}Si quieres salir vivo de aquí.{/size}"
    
    show bridia neutral at char_left with move
    show inquisitor neutral at char_center with dissolve
    show judge neutral at char_right with dissolve

    # -------- DECISIÓN CLAVE --------
    menu:
        "Soy... aprendiz de Rosa Azul... de Lady Bridia Cerúlea.":
            $ chose_correct_response = True
            $ bridia_trust += 20
            $ rose_affinity += 15
            
            p "Soy... aprendiz de {color=[TGC_ROSE_BLUE]}Rosa Azul{/color}..."
            p "...de Lady Bridia Cerúlea."
            
            if renpy.loadable("assets/audio/sfx/crowd_shocked.ogg"):
                play sound "assets/audio/sfx/crowd_shocked.ogg"
            
            show bridia smirk at char_left with dissolve
            
            $ persistent.achievements["rosa_azul_reconocida"] = True
            $ renpy.notify("✓ Logro: Heredero del Azul")

        "Soy... aprendiz de alquimia... bajo Lady Bridia.":
            $ chose_correct_response = False
            $ bridia_trust += 8
            
            p "Soy... aprendiz de alquimia..."
            p "...bajo Lady Bridia."
            
            show bridia worried at char_left with dissolve

        "Soy... su estudiante.":
            $ chose_correct_response = False
            $ bridia_trust += 2
            
            p "Soy... su estudiante."
            
            show bridia worried at char_left with dissolve

    show inquisitor suspicious at char_center with dissolve
    inq "Demasiado oportuno."
    inq "Muere, revive y ya es tu pupilo."

    show bridia serious at char_left with dissolve
    b "O {i}sobrevive{/i} a algo que yo no preparé."
    b "Si de verdad buscan verdad, denme {b}custodia tutelar{/b}."

    show judge neutral at char_right with dissolve
    j "Concedida."
    j "{color=[TGC_GOLD]}Tres días{/color} de observación bajo su sello."

    show judge angry at char_right with dissolve
    j "Un error."
    j "Un falseo."
    j "Una {b}sola{/b} mentira..."
    j "...y {color=[TGC_CRIMSON]}{b}ambos{/b}{/color} responden ante este estrado."

    if renpy.loadable("assets/audio/sfx/gavel_heavy.ogg"):
        play sound "assets/audio/sfx/gavel_heavy.ogg"
    with vpunch

    show bridia neutral at char_left
    b "Acepto."

    show inquisitor neutral at char_center with dissolve
    inq "Tres días, Defensora."
    inq "Que enseñen algo."

    hide inquisitor
    hide judge

    show bridia serious at char_center with move
    b "{size=-6}Camina.{/size}"
    b "{size=-6}No confundas {i}necesidad{/i} con {i}confianza{/i}.{/size}"

    scene bg black with Dissolve(0.8)
    stop music fadeout 1.2

    jump pasillo_revelacion

# =============================================================================
# ACTO II: PASILLO (Desconfianza explícita)
# =============================================================================
label pasillo_revelacion:

    scene bg corridor with Dissolve(1.0)

    show bridia neutral at char_center with dissolve
    narrator "{i}Respiras. La sala queda atrás.{/i}"

    show bridia serious at char_center with dissolve
    b "Estabas preparado para morir."
    b "Yo para cargar con ello."
    b "No confío en ti."
    b "Pero ahora {b}me perteneces{/b} por ley y por sentido común."

    show bridia neutral at char_center with dissolve
    b "Tres días."
    b "Día uno: {i}sobrevivir{/i}."
    b "Día dos: {i}aprender{/i}."
    b "Día tres: {i}convencer{/i}."

    scene bg black with Dissolve(0.8)

    jump llegada_casa

# =============================================================================
# LLEGADA A LA CASA
# =============================================================================
label llegada_casa:

    scene bg bridia_house_ext with Dissolve(0.8)

    show bridia neutral at char_center with dissolve
    b "Éste es mi taller."
    b "Y tu cuarto, si {i}aceptas{/i} la tutela."

    menu:
        "Aceptar":
            $ bridia_trust += 10
            show bridia smirk at char_center with dissolve
            b "Bien. Empezamos."
            jump entrar_casa

        "Dudar":
            $ bridia_trust += 3
            show bridia serious at char_center with dissolve
            b "Duda si quieres."
            b "Duermes aquí por ley y por seguridad."
            jump entrar_casa

        "Escapar":
            $ bridia_trust -= 10
            show bridia serious at char_center with dissolve
            b "Te advierto el toque de queda."
            jump escapar_toque_queda

# =============================================================================
# ESCAPE (Captura por guardia)
# =============================================================================
label escapar_toque_queda:

    scene bg black with Dissolve(0.5)
    narrator "{i}Calle, faroles, metal.{/i}"

    scene bg city_street_night with dissolve
    show guard neutral at char_center with dissolve
    
    guardia "Alto. Identificación. Toque de queda."

    menu:
        "Nombrar a Bridia (apresurado)":
            $ bridia_trust -= 2
            guardia "La Defensora no suele equivocarse."
            guardia "Te devuelvo. Por {i}ella{/i}."
            
        "Correr":
            $ bridia_trust -= 5
            guardia "Mala idea."
            narrator "{i}Te inmovilizan con gesto seco.{/i}"

    scene bg bridia_house_ext with Dissolve(0.6)
    show bridia serious at char_center with dissolve

    b "¿Contento?"
    b "Última vez que me haces perder la noche."

    $ bridia_trust = max(0, bridia_trust)
    $ night_0_escaped = True

    jump entrar_casa

# =============================================================================
# ENTRADA A LA CASA
# =============================================================================
label entrar_casa:

    scene bg bridia_house_hall with Dissolve(0.8)

    show bridia neutral at char_center with dissolve
    b "Reglas:"
    b "No toques frascos sin permiso."
    b "Dos golpes. Pausa. Uno más. Ése es {i}mi{/i} llamado."
    b "Cualquier otro patrón, asumo intrusión."

    show bridia serious at char_center with dissolve
    b "Eres mi responsabilidad, no mi amigo."
    b "Ganas mi confianza con hechos."

    scene bg black with Dissolve(0.8)

    centered "{size=36}{color=[TGC_ROSE_BLUE]}CAPÍTULO 1{/color}\n\n{size=28}Rosa Azul{/size}\n{size=20}Día 1: Sobrevivir{/size}{/size}"

    $ renpy.save("auto-1", "Capítulo 1 - Día 1")
    
    jump capitulo_uno

# =============================================================================
# PLACEHOLDER - CAPÍTULO 1
# =============================================================================
label capitulo_uno:
    
    centered "Fin del prólogo.\n\n{size=-4}(Capítulo 1 en desarrollo){/size}"
    
    return
