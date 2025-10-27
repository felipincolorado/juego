# game/src/core/assets.rpy
# Fondos / sprites con fallbacks SEGUROS (sin imports raros).

init -45 python:
    def tgc_has(path):
        try:
            return renpy.loadable(path)
        except Exception:
            return False

init -40:
    # --- BACKGROUNDS ---
    if tgc_has("assets/art/backgrounds/bg_courtroom_day.png"):
        image bg courtroom = "assets/art/backgrounds/bg_courtroom_day.png"
    else:
        image bg courtroom = Solid("#0a0f1a")

    if tgc_has("assets/art/backgrounds/bg_courtroom_corridor.png"):
        image bg corridor = "assets/art/backgrounds/bg_courtroom_corridor.png"
    else:
        image bg corridor = Solid("#101826")

    if tgc_has("assets/art/backgrounds/bg_bridia_house_ext.png"):
        image bg bridia_house_ext = "assets/art/backgrounds/bg_bridia_house_ext.png"
    else:
        image bg bridia_house_ext = Solid("#0e141f")

    if tgc_has("assets/art/backgrounds/bg_bridia_house_hall.png"):
        image bg bridia_house_hall = "assets/art/backgrounds/bg_bridia_house_hall.png"
    else:
        image bg bridia_house_hall = Solid("#131b29")

    if tgc_has("assets/art/backgrounds/bg_city_street_night.png"):
        image bg city_street_night = "assets/art/backgrounds/bg_city_street_night.png"
    else:
        image bg city_street_night = Solid("#050810")

    image bg black = Solid("#000")
    image bg white = Solid("#ffffff")

    # --- JUEZ / HIERARCA ---
    if tgc_has("assets/art/characters/judge/judge_neutral.png"):
        image judge neutral = "assets/art/characters/judge/judge_neutral.png"
    else:
        image judge neutral = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/judge/judge_angry.png"):
        image judge angry = "assets/art/characters/judge/judge_angry.png"
    else:
        image judge angry = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/judge/judge_suspicious.png"):
        image judge suspicious = "assets/art/characters/judge/judge_suspicious.png"
    else:
        image judge suspicious = Solid((0,0,0,0), xsize=400, ysize=800)

    # --- BRIDIA ---
    if tgc_has("assets/art/characters/bridia/bridia_neutral.png"):
        image bridia neutral = "assets/art/characters/bridia/bridia_neutral.png"
    else:
        image bridia neutral = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/bridia/bridia_worried.png"):
        image bridia worried = "assets/art/characters/bridia/bridia_worried.png"
    else:
        image bridia worried = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/bridia/bridia_smirk.png"):
        image bridia smirk = "assets/art/characters/bridia/bridia_smirk.png"
    else:
        image bridia smirk = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/bridia/bridia_serious.png"):
        image bridia serious = "assets/art/characters/bridia/bridia_serious.png"
    else:
        image bridia serious = Solid((0,0,0,0), xsize=400, ysize=800)

    # --- INQUISIDOR ---
    if tgc_has("assets/art/characters/inquisitor/inquisitor_neutral.png"):
        image inquisitor neutral = "assets/art/characters/inquisitor/inquisitor_neutral.png"
    else:
        image inquisitor neutral = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/inquisitor/inquisitor_angry.png"):
        image inquisitor angry = "assets/art/characters/inquisitor/inquisitor_angry.png"
    else:
        image inquisitor angry = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/inquisitor/inquisitor_suspicious.png"):
        image inquisitor suspicious = "assets/art/characters/inquisitor/inquisitor_suspicious.png"
    else:
        image inquisitor suspicious = Solid((0,0,0,0), xsize=400, ysize=800)

    # --- GUARDIA (Rugora si lo usas luego) ---
    if tgc_has("assets/art/characters/guard/guard_neutral.png"):
        image guard neutral = "assets/art/characters/guard/guard_neutral.png"
    else:
        image guard neutral = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/guard/guard_suspicious.png"):
        image guard suspicious = "assets/art/characters/guard/guard_suspicious.png"
    else:
        image guard suspicious = Solid((0,0,0,0), xsize=400, ysize=800)

    if tgc_has("assets/art/characters/guard/guard_serious.png"):
        image guard serious = "assets/art/characters/guard/guard_serious.png"
    else:
        image guard serious = Solid((0,0,0,0), xsize=400, ysize=800)

init -38:
    # --- POSICIONES ---
    transform char_left:
        xpos 0.25
        yalign 1.0

    transform char_center:
        xpos 0.50
        yalign 1.0

    transform char_right:
        xpos 0.75
        yalign 1.0

    transform char_far_left:
        xpos 0.10
        yalign 1.0

    transform char_far_right:
        xpos 0.90
        yalign 1.0

    # --- EFECTOS DE CÁMARA ---
    transform focus_close:
        zoom 1.0
        xalign 0.5
        yalign 0.3
        easein 0.5 zoom 1.3

    transform fade_in_slow:
        alpha 0.0
        easein 2.0 alpha 1.0

    transform shake:
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        linear 0.1 xoffset 0
