## Este archivo contiene opciones que pueden cambiarse para personalizar el
## juego. (NO pegues código de pantallas ni líneas sueltas con $ aquí.)

## Básico ######################################################################

define config.name = _("TheGildedCage")
define gui.show_name = True
define config.version = "1.0"

define gui.about = _p("""
""")

define build.name = "TheGildedCage"

## Sonidos y música ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"
# define config.main_menu_music = "main-menu-theme.ogg"

## Transiciones ################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## Gestión de ventanas #########################################################

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preferencias por defecto ####################################################

default preferences.text_cps = 0
default preferences.afm_time = 15

## Directorio de guardado ######################################################

define config.save_directory = "TheGildedCage-1761083243"

## Icono #######################################################################

define config.window_icon = "gui/window_icon.png"

## --------- Mapeo de controles globales (Esc / click derecho / pad) ----------
init -1 python:
    # Tomamos el keymap actual y garantizamos que Esc y click derecho
    # activen el menú del juego (o "volver") como fallback global.
    km = dict(config.keymap)

    # Fusionamos con lo que ya hubiera en 'game_menu' (no lo pisamos).
    km['game_menu'] = list(set(km.get('game_menu', []) + ['K_ESCAPE', 'K_MENU', 'mouseup_3']))

    # Aseguramos que 'dismiss' incluya click derecho (cuando hay diálogo).
    km['dismiss'] = list(set(km.get('dismiss', []) + ['mouseup_3']))

    config.keymap = km

    # Gamepad: B/Start como back/menu global (fallback).
    try:
        pb = dict(getattr(config, 'pad_bindings', {}))
        pb['pad_b'] = 'game_menu'
        pb['pad_start'] = 'game_menu'
        config.pad_bindings = pb
    except Exception:
        pass
    
init -1 python:
    # Quita K_TAB de cualquier atajo de skip/toggle/fast-skip.
    for k in ("skip", "toggle_skip", "fast_skip"):
        try:
            config.keymap[k] = [key for key in config.keymap.get(k, []) if key != "K_TAB"]
        except Exception:
            pass

    # (Opcional) Deja Ctrl como skip, para no perder la función.
    try:
        config.keymap["skip"] = list(set(config.keymap.get("skip", []) + ["K_LCTRL", "K_RCTRL"]))
    except Exception:
        pass

    # Importante: NO usar aquí config.context_clear_layers = False
    # Si alguna vez quieres desactivarlo explícitamente, usa lista vacía:
    # config.context_clear_layers = []
## ---------------------------------------------------------------------------

## Configuración de 'Build' ####################################################
init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')

# define build.google_play_key = "..."
# define build.itch_project = "renpytom/test-project"
