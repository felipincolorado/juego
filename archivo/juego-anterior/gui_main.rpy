## src/screens/gui_main.rpy
## Menú Principal profesional — The Gilded Cage
## Fondo dinámico, partículas, navegación teclado/gamepad, Start() canónico

# ==================================================
# CONFIGURACIÓN, COLORES Y FUENTES
# ==================================================
init -20 python:
    # Paleta
    MM_LIGHT_COLOR = "#F1D487"     # polvo dorado
    MM_IVORY       = "#EDE8D6"     # texto base
    MM_GOLD        = "#D4AF37"     # hover/selección
    MM_OUTLINE_COL = "#0a0f1a"
    MM_OUTLINE_PX  = 1
    PROLOGO_LABEL = "prologo_tribunal"


    # Rutas de fondo (fallbacks)
    MM_BG_CANDIDATES = [
        "assets/art/backgrounds/mm_judgment_hall.png",
        "assets/mm_judgment_hall.png",
        "images/backgrounds/mm_judgment_hall.png",
    ]

    def _safe_font(path, fallback=None):
        try:
            if path and renpy.loadable(path):
                return path
        except Exception:
            pass
        return fallback

    _ui_fallback    = getattr(gui, "interface_text_font", None)
    _title_fallback = _ui_fallback

    MM_FONT_UI    = _safe_font("assets/fonts/inter/Inter-Medium.ttf", _ui_fallback)
    MM_FONT_TITLE = _safe_font("assets/fonts/Cardo/Cardo-Regular.ttf", _title_fallback)

    def _mm_pick_bg():
        try:
            gbg = getattr(gui, "main_menu_background", None)
            if gbg and renpy.loadable(gbg):
                return gbg
        except Exception:
            pass
        for p in MM_BG_CANDIDATES:
            try:
                if renpy.loadable(p):
                    return p
            except Exception:
                pass
        return None

# ==================================================
# TRANSFORMS Y ESTILOS
# ==================================================
transform mm_hover_lift:
    on hover:
        linear 0.30 zoom 1.02 yoffset -2
    on idle:
        linear 0.30 zoom 1.00 yoffset 0

transform mm_idle_reset:
    linear 0.20 zoom 1.00 yoffset 0

transform mm_dust(x, y, dx, dy, dur=8.0, delay=0.0, z=0.85, a=0.30):
    additive 1.0
    alpha 0.0
    pos (x, y)
    zoom z
    pause delay
    linear dur alpha a xpos (x + dx) ypos (y + dy)
    linear 0.6 alpha 0.0
    repeat

init -10 python:
    MM_SELECT_ON_KEYS = True  # resalta con teclado/pad

style mm_btn is button:
    background None
    hover_background None
    selected_background None
    padding (6, 4, 6, 4)
    xfill False

style mm_btn_text is text:
    font (MM_FONT_TITLE or gui.interface_text_font)
    size 36
    color MM_IVORY
    hover_color MM_GOLD
    selected_color MM_GOLD
    outlines [ (MM_OUTLINE_PX, MM_OUTLINE_COL, 0, 0) ]
    xalign 0.0

# ==================================================
# FONDO (modular, mantiene proporción)
# ==================================================
screen _mm_bg():
    $ W = renpy.config.screen_width
    $ H = renpy.config.screen_height
    $ _path = _mm_pick_bg()
    if _path:
        $ iw, ih = renpy.image_size(_path)
        $ sx = float(W) / float(iw)
        $ sy = float(H) / float(ih)
        $ scale = sx if sx > sy else sy
        add _path zoom scale xalign 0.5 yalign 0.5
    else:
        add Solid("#0d1117")
        add Solid("#0f1726") alpha 0.5

# ==================================================
# MENÚ PRINCIPAL
# ==================================================
screen main_menu():
    tag menu
    modal True

    # 1) Fondo
    use _mm_bg

    # 2) Partículas
    default dust_seeds = None
    if dust_seeds is None:
        python:
            import random as _r
            rng = _r.Random()
            seeds = []
            N = 120
            W = renpy.config.screen_width
            H = renpy.config.screen_height
            for i in range(N):
                x = int(rng.uniform(W * 0.03, W * 0.97))
                y = int(rng.uniform(H * 0.10, H * 0.95))
                dx_mag = rng.uniform(W * 0.18, W * 0.36)
                dx = int(dx_mag if rng.random() < 0.5 else -dx_mag)
                dy = -int(rng.uniform(H * 0.28, H * 0.52))
                dur = rng.uniform(6.0, 9.0)
                delay = rng.uniform(0.0, 5.0)
                zoom = rng.uniform(0.60, 0.95)
                alpha = rng.uniform(0.20, 0.30)
                size = int(rng.uniform(14, 18))
                seeds.append((x, y, int(dx), int(dy), dur, delay, zoom, alpha, size))
            dust_seeds = seeds

    fixed:
        for (x,y,dx,dy,dur,delay,zoom,a,size) in dust_seeds:
            add Text("•", size=size, color=MM_LIGHT_COLOR) at mm_dust(x,y,dx,dy,dur,delay,zoom,a)

    # 3) Lógica de entradas
    default sel = 0
    default hover_idx = -1
    default input_dev = "mouse"

    python:
        # Opción "Continuar" si tu helper existe y el slot está disponible
        latest = _get_latest_save_slot() if hasattr(store, "_get_latest_save_slot") else None
        entries = []

        if latest is not None and FileLoadable(latest):
            entries.append( (_("Continuar"),
                [ If(renpy.loadable("assets/audio/sfx/menu_load.ogg"), Play("sound", "assets/audio/sfx/menu_load.ogg")),
                  FileLoad(latest) ]) )

        # Menú estándar (Start canónico; respetará config.start_label = "start")
        entries += [
            (_("Nueva Partida"),
                [ If(renpy.loadable("assets/audio/sfx/menu_start.ogg"), Play("sound", "assets/audio/sfx/menu_start.ogg")),
                  Start() ]),

            (_("Cargar Partida"),
                [ If(renpy.loadable("assets/audio/sfx/menu_files.ogg"), Play("sound", "assets/audio/sfx/menu_files.ogg")),
                  ShowMenu("load") ]),

            (_("Opciones"),
                [ If(renpy.loadable("assets/audio/sfx/menu_options.ogg"), Play("sound", "assets/audio/sfx/menu_options.ogg")),
                  ShowMenu("preferences") ]),
        ]

        # "Extras" solo si existe la pantalla
        if renpy.has_screen("extras_elegant"):
            entries.append( (_("Extras"),
                [ If(renpy.loadable("assets/audio/sfx/menu_extras.ogg"), Play("sound", "assets/audio/sfx/menu_extras.ogg")),
                  ShowMenu("extras_elegant") ]) )

        # Salir con confirm global (definida en ui_overrides.rpy)
        entries.append( (_("Salir"),
            ShowMenu("confirm",
                     message=_("¿Seguro que deseas salir del juego?"),
                     yes_action=Quit(confirm=False),
                     no_action=Hide("confirm"))
        ))

    if sel < 0 or sel >= len(entries):
        $ sel = 0
    if hover_idx >= len(entries):
        $ hover_idx = -1

    # 4) Botonera
    if entries:
        frame:
            background None
            xalign 1.0
            yalign 0.5
            right_padding 140
            xmaximum 460

            vbox:
                spacing 16
                xsize 420

                for i, (label, act) in enumerate(entries):
                    $ is_hover = (hover_idx == i)
                    $ is_keys  = (MM_SELECT_ON_KEYS and input_dev == "keys" and sel == i)
                    $ selected_visual = (is_hover or is_keys)
                    $ _tr = mm_hover_lift if selected_visual else mm_idle_reset

                    button style "mm_btn" selected selected_visual at _tr:
                        action act
                        hovered [ SetScreenVariable("hover_idx", i), SetScreenVariable("input_dev", "mouse") ]
                        unhovered If(hover_idx == i, SetScreenVariable("hover_idx", -1), NullAction())
                        text label style "mm_btn_text"
    else:
        text _("No hay opciones disponibles.") xpos 0.5 xanchor 0.5 ypos 0.85

    # 5) Teclado / Gamepad
    if entries:
        key "K_UP"       action [ SetScreenVariable("sel", (sel - 1) % len(entries)), SetScreenVariable("input_dev", "keys") ]
        key "K_DOWN"     action [ SetScreenVariable("sel", (sel + 1) % len(entries)), SetScreenVariable("input_dev", "keys") ]
        key "K_RETURN"   action [ entries[sel][1], SetScreenVariable("input_dev", "keys") ]
        key "K_KP_ENTER" action [ entries[sel][1], SetScreenVariable("input_dev", "keys") ]
        key "K_w"        action [ SetScreenVariable("sel", (sel - 1) % len(entries)), SetScreenVariable("input_dev", "keys") ]
        key "K_s"        action [ SetScreenVariable("sel", (sel + 1) % len(entries)), SetScreenVariable("input_dev", "keys") ]
        key "K_d"        action [ entries[sel][1], SetScreenVariable("input_dev", "keys") ]
        key "pad_up"     action [ SetScreenVariable("sel", (sel - 1) % len(entries)), SetScreenVariable("input_dev", "keys") ]
        key "pad_down"   action [ SetScreenVariable("sel", (sel + 1) % len(entries)), SetScreenVariable("input_dev", "keys") ]
        key "pad_a"      action [ entries[sel][1], SetScreenVariable("input_dev", "keys") ]

    # 6) Salir (Escape, botón derecho, gamepad)
    key "K_ESCAPE"  action ShowMenu("confirm", message=_("¿Seguro que deseas salir del juego?"), yes_action=Quit(confirm=False), no_action=Hide("confirm"))
    key "mouseup_3" action ShowMenu("confirm", message=_("¿Seguro que deseas salir del juego?"), yes_action=Quit(confirm=False), no_action=Hide("confirm"))
    key "pad_b"     action ShowMenu("confirm", message=_("¿Seguro que deseas salir del juego?"), yes_action=Quit(confirm=False), no_action=Hide("confirm"))
