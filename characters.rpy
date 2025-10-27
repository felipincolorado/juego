## =============================================================================
## THE GILDED CAGE - DEFINICIÓN DE PERSONAJES
## Ubicación: game/src/core/characters.rpy
## Requiere: game/src/core/config.rpy (init -100)
## =============================================================================

# -------- PERSONAJES (init -50) --------
init -50:
    
    # Narrador (para líneas descriptivas)
    define narrator = Character(
        None,
        what_color="#FFFFFF",
        what_outlines=[(1, "#000000")]
    )

    # Protagonista dinámico
    define p = Character(
        "[player_name]",
        dynamic=True,
        what_color="#FFFFFF",
        what_outlines=[(1, "#000000")]
    )

    # Bridia Cerúlea (Rosa Azul)
    define b = Character(
        "Bridia Cerúlea",
        what_color="#FFFFFF",
        who_color="#c9a86a",
        what_outlines=[(1, "#000000")],
        who_outlines=[(1, "#000000")],
        voice_tag="bridia"
    )

    # Hierarca de Hierro (Juez)
    define j = Character(
        "Hierarca de Hierro",
        what_color="#FFFFFF",
        who_color="#c9a86a",
        what_outlines=[(1, "#000000")],
        who_outlines=[(1, "#000000")]
    )

    # Inquisidor Basalto
    define inq = Character(
        "Inquisidor Basalto",
        what_color="#FFFFFF",
        who_color="#c9a86a",
        what_outlines=[(1, "#000000")],
        who_outlines=[(1, "#000000")]
    )

    # Novicio Cuarzo (Acólito)
    define acolito = Character(
        "Novicio Cuarzo",
        what_color="#FFFFFF",
        who_color="#c9a86a",
        what_outlines=[(1, "#000000")],
        who_outlines=[(1, "#000000")]
    )

    # Guardia genérica
    define guardia = Character(
        "Guardia",
        what_color="#FFFFFF",
        who_color="#8B7355",
        what_outlines=[(1, "#000000")],
        who_outlines=[(1, "#000000")]
    )

    # Rugosa Cairn (cuando se revele su nombre)
    define rug = Character(
        "Rugosa Cairn",
        what_color="#FFFFFF",
        who_color="#8B7355",
        what_outlines=[(1, "#000000")],
        who_outlines=[(1, "#000000")]
    )
