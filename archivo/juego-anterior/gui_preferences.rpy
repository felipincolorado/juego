## src/screens/gui_preferences.rpy
## Menú de Opciones (Preferences) para "The Gilded Cage".
## Versión estandarizada: Navegación por pestañas, controles personalizados, sistema de ayuda.
## Ren'Py 8.4.x

# ======================================================================
# BLOQUE DE CONFIGURACIÓN INICIAL (init -20)
# ======================================================================

init -20 python:
    # ---- Escalado base (ESTANDARIZADO) ----
    try:
        _AOD_SCALE = float(config.screen_height) / 1080.0
        _AOD_SCALE = max(0.70, min(2.00, _AOD_SCALE))
    except Exception:
        _AOD_SCALE = 1.0

    # ---- Helpers de assets (ESTANDARIZADOS) ----
    def aod_frame_or_solid(path, ltrb, fallback_color):
        try:
            if renpy.loadable(path):
                l, t, r, b = ltrb
                return Frame(path, l, t, r, b)
        except Exception:
            pass
        return Solid(fallback_color)

    def path_if_exists(path):
        try:
            if renpy.loadable(path):
                return path
        except Exception:
            pass
        return None

    # ---- Roots de assets (ESTANDARIZADOS) ----
    AOD_ASSET_ROOT = "assets/art/gui/"
    AOD_ICON_ROOT  = "assets/art/gui/icons/"

    def ui9(name, ltrb, fallback):
        return aod_frame_or_solid(AOD_ASSET_ROOT + name, ltrb, fallback)

    # ---- Paleta (ESTANDARIZADA) ----
    AOD_COL_BG      = "#0f1218"
    AOD_COL_PANEL   = "#141925"
    AOD_COL_TEXT    = "#E6E6E6"
    AOD_COL_ACCENT  = "#c9a86a"
    AOD_COL_ACCENT2 = "#181818"
    AOD_COL_MUTED   = "#BFC6D4"

    # ---- Métricas globales (ESTANDARIZADAS) ----
    AOD_MARGIN       = int(round(40 * _AOD_SCALE))
    AOD_GUTTER       = int(round(18 * _AOD_SCALE))
    AOD_FOOTER_H     = int(round(44 * _AOD_SCALE))
    AOD_SIDE_PAD     = int(round(32 * _AOD_SCALE))
    AOD_INNER_PAD    = int(round(12 * _AOD_SCALE))

    # ---- Métricas específicas Preferences ----
    AOD_ROW_H        = int(round(54 * _AOD_SCALE))
    AOD_TAB_H        = int(round(56 * _AOD_SCALE))

    # ---- Tamaños de texto (ESTANDARIZADOS) ----
    AOD_SIZE_TITLE   = int(round(26 * _AOD_SCALE))
    AOD_SIZE_TEXT    = int(round(20 * _AOD_SCALE))
    AOD_SIZE_SUBTEXT = int(round(18 * _AOD_SCALE))
    AOD_SIZE_INFO    = int(round(14 * _AOD_SCALE))
    AOD_SIZE_SMALL   = int(round(16 * _AOD_SCALE))

    # ---- Spacing (ESTANDARIZADOS) ----
    AOD_SPACING_HBOX = int(round(18 * _AOD_SCALE))
    AOD_SPACING_VBOX = int(round(12 * _AOD_SCALE))
    AOD_SPACING_FOOT = int(round(28 * _AOD_SCALE))

    # ---- Assets (ESTANDARIZADOS) ----
    AOD_ROW_BG_IDLE  = ui9("row_bg.png",         (16,16,16,16), "#202b3f")
    AOD_ROW_BG_HOVER = ui9("row_bg_hover.png",   (16,16,16,16), "#2b3a55")
    AOD_ROW_BG_SEL   = ui9("row_bg_selected.png",(16,16,16,16), "#314262")

    AOD_VALUE_BG        = ui9("value_bg.png",        (12,12,12,12), "#1f293b")
    AOD_VALUE_BG_ACTIVE = ui9("value_bg_active.png", (12,12,12,12), None)

    AOD_TAB_BG       = ui9("tab_bg.png",       (12,12,12,12), "#1b2434")
    AOD_TAB_BG_HOVER = ui9("tab_bg_hover.png", (12,12,12,12), "#23314a")
    AOD_TAB_BG_SEL   = ui9("tab_bg_s.png",     (12,12,12,12), "#2b3a55")

    AOD_HELP_BG    = ui9("help_bg.png",    (16,16,16,16), "#1a2130")
    AOD_CONTENT_BG = ui9("content_bg.png", (16,16,16,16), "#00000000")
    AOD_PANEL_BG   = ui9("panel_bg.png",   (24,24,24,24), "#00000000")

    AOD_ARROW_BOX_IDLE  = ui9("arrow_box.png",       (8,8,8,8), "#263349")
    AOD_ARROW_BOX_HOVER = ui9("arrow_box_hover.png", (8,8,8,8), "#2e3e58")
    AOD_ARROW_W = int(round(44 * _AOD_SCALE))

    AOD_ICON_ARROW_L = path_if_exists(AOD_ICON_ROOT + "arrow_left.png")
    AOD_ICON_ARROW_R = path_if_exists(AOD_ICON_ROOT + "arrow_right.png")

    AOD_BG_MAIN = "assets/art/gui/bg_main.png"

    # ---- Keycaps (ESTANDARIZADOS) ----
    AOD_ICON_SIZE   = int(round(44 * _AOD_SCALE))
    
    def icon_frame(name, fallback="#263349"):
        return aod_frame_or_solid(AOD_ICON_ROOT + name, (4,4,4,4), fallback)

    AOD_ICON_QE     = icon_frame("btn_qe.png")
    AOD_ICON_UD     = icon_frame("btn_ud.png")
    AOD_ICON_LR     = icon_frame("btn_lr.png")
    AOD_ICON_ENTER  = icon_frame("btn_enter.png")
    AOD_ICON_ESC    = icon_frame("btn_esc.png")

    AOD_CAP_QE     = "Q/E"
    AOD_CAP_UD     = "↑/↓"
    AOD_CAP_LR     = "←/→"
    AOD_CAP_ENTER  = "↵"
    AOD_CAP_ESC    = "Esc"

    # Respiro derecho
    AOD_RIGHT_BREATH = int(round(56 * _AOD_SCALE))

    # ---- Lista de idiomas ----
    AOD_LANGS = [
        ("es", "Español"),
        ("en", "English"),
    ]

    # ---- Tabs (id, etiqueta) ----
    AOD_TABS = [
        ("general",      "General"),
        ("audio",        "Audio"),
        ("texto",        "Texto & Flujo"),
        ("acces_idioma", "Accesibilidad & Idioma"),
    ]

    # ---- Ayudas ----
    AOD_HELP = {
        "Modo de pantalla":  ("MODO DE PANTALLA", "Ventana o pantalla completa; alterna con las flechas."),
        "Transiciones":      ("TRANSICIONES", "Activa/desactiva transiciones globales."),
        "Cursor del sistema":("CURSOR DEL SISTEMA", "Usa el cursor del sistema operativo."),
        "Restaurar posición":("RESTAURAR POSICIÓN", "Recupera la posición de la ventana al iniciar."),
        "Ahorro GL":         ("AHORRO DE ENERGÍA (GL)", "Reduce redibujado cuando la pantalla no cambia."),
        "Tearing":           ("TEARING", "Preferencia entre 'tearing' o 'frameskip'."),
        "Volumen música":    ("MÚSICA", "Ajusta el volumen musical. ←/→ cambia 5%."),
        "Volumen efectos":   ("EFECTOS", "Ajusta el volumen de efectos/sonidos."),
        "Volumen voz":       ("VOZ", "Ajusta el volumen de voces/diálogo."),
        "Silenciar música":  ("SILENCIAR MÚSICA", "Alterna entre silenciar y restaurar el volumen previo."),
        "Silenciar efectos": ("SILENCIAR EFECTOS", "Alterna entre silenciar y restaurar el volumen previo."),
        "Silenciar voz":     ("SILENCIAR VOZ", "Alterna entre silenciar y restaurar el volumen previo."),
        "Probar efectos":    ("PROBAR EFECTOS", "Reproduce un efecto corto para validar volumen."),
        "Probar voz":        ("PROBAR VOZ", "Reproduce una línea de voz de prueba."),
        "Velocidad del texto": ("VELOCIDAD DEL TEXTO", "0 detiene el tipeo. 1..10 acelera el texto (20..120 cps)."),
        "Auto-avance":         ("AUTO-AVANCE", "0 desactivado. 1..10 aumenta el tiempo entre líneas (0.5..3.5s)."),
        "Omitir no vistos":    ("OMITIR NO VISTOS", "Permite omitir líneas que no han sido leídas."),
        "Después de elegir":   ("DESPUÉS DE ELEGIR", "Seguir automáticamente (Continuar) o pausar (Detener)."),
        "Click cancela AFM":   ("CLICK Y AUTO-AVANCE", "Si está activado, un click cancela el auto-avance."),
        "Idioma":              ("IDIOMA", "Cambia el idioma del juego al instante (si hay traducción disponible)."),
    }

    AOD_USE_MOUSE_HOVER = False


# ======================================================================
# BLOQUE DE FUNCIONES HELPER (init -10)
# ======================================================================

init -10 python:
    # ---- AUDIO + TEXTO HELPERS ----
    def aod_get_action(rows, idx, key):
        try:
            r = rows[idx]
            act = r.get(key, None)
            return act if act is not None else NullAction()
        except Exception:
            return NullAction()

    def aod_get_submit_action(rows, idx):
        try:
            r = rows[idx]
            return r.get("right") or r.get("press") or NullAction()
        except Exception:
            return NullAction()

    def _aod_bootstrap_persistent():
        if not isinstance(getattr(persistent, "aod_muted", None), dict):
            persistent.aod_muted = {"music": False, "sound": False, "voice": False}
        if not isinstance(getattr(persistent, "aod_prev_vol", None), dict):
            persistent.aod_prev_vol = {"music": 1.0, "sound": 1.0, "voice": 1.0}
        renpy.save_persistent()
    _aod_bootstrap_persistent()

    def aod_get_pct(kind):
        try:
            v = preferences.get_mixer(kind)
            if v is None:
                v = 0.0
            p = int(round(float(v) * 100.0))
            return int(round(p / 5.0) * 5)
        except Exception:
            return 0

    def aod_set_pct(kind, pct):
        try:
            p = max(0, min(100, int(round(pct/5.0)*5)))
            preferences.set_mixer(kind, p / 100.0)
        except Exception:
            pass

    def aod_step_pct(kind, delta):
        aod_set_pct(kind, aod_get_pct(kind) + delta)

    def aod_is_muted(kind):
        m = getattr(persistent, "aod_muted", None)
        if not isinstance(m, dict):
            _aod_bootstrap_persistent()
            m = persistent.aod_muted
        return bool(m.get(kind, False))

    def aod_toggle_mute(kind):
        _aod_bootstrap_persistent()
        is_muted = bool(persistent.aod_muted.get(kind, False))
        if not is_muted:
            cur = preferences.get_mixer(kind)
            try:
                curf = float(cur) if cur is not None else 1.0
            except Exception:
                curf = 1.0
            persistent.aod_prev_vol[kind] = curf
            preferences.set_mixer(kind, 0.0)
            persistent.aod_muted[kind] = True
        else:
            prev = persistent.aod_prev_vol.get(kind, 1.0)
            try:
                preferences.set_mixer(kind, float(prev))
            except Exception:
                preferences.set_mixer(kind, 1.0)
            persistent.aod_muted[kind] = False
        renpy.save_persistent()

    def aod_test(kind):
        try:
            if kind == "sound":
                renpy.play("assets/audio/sfx/test_click.ogg", channel="sound")
            elif kind == "voice":
                renpy.play("assets/audio/sfx/test_voice.ogg", channel="voice")
        except Exception:
            if kind == "sound":
                try:
                    renpy.play("assets/audio/sfx/confirm.ogg", channel="sound")
                except:
                    pass

    # --- Texto & Flujo (niveles) ---
    def aod_cps_from_level(L):
        L = 0 if L < 0 else (10 if L > 10 else int(L))
        if L == 0: return 0
        return int(round(20 + (L - 1) * (100.0 / 9.0)))
    
    def aod_level_from_cps(cps):
        try: c = float(cps)
        except Exception: c = 0.0
        if c <= 0.0: return 0
        return max(1, min(10, int(round(1 + (c - 20.0) * 9.0 / 100.0))))
    
    def aod_sec_from_level(L):
        L = 0 if L < 0 else (10 if L > 10 else int(L))
        if L == 0: return 0.0
        return round(0.5 + (L - 1) * (3.0 / 9.0), 2)
    
    def aod_level_from_sec(sec):
        try: s = float(sec)
        except Exception: s = 0.0
        if s <= 0.0: return 0
        return max(1, min(10, int(round(1 + (s - 0.5) * 9.0 / 3.0))))
    
    def aod_get_level(kind):
        if kind == "textspeed":
            return aod_level_from_cps(preferences.text_cps)
        if kind == "afm":
            return aod_level_from_sec(preferences.afm_time)
        return 0
    
    def aod_set_level(kind, level):
        L = 0 if level < 0 else (10 if level > 10 else int(level))
        if kind == "textspeed":
            preferences.text_cps = aod_cps_from_level(L)
        elif kind == "afm":
            preferences.afm_time = aod_sec_from_level(L)
    
    def aod_step_level(kind, delta):
        aod_set_level(kind, aod_get_level(kind) + (1 if delta > 0 else -1))

    # ---- Idioma: helpers ----
    def aod_get_lang_code():
        code = getattr(persistent, "aod_language", None)
        if code:
            return code
        try:
            return renpy.game.preferences.language or "es"
        except Exception:
            return "es"

    def aod_set_lang_code(code):
        try:
            persistent.aod_language = code
            renpy.change_language(code)
            renpy.restart_interaction()
        except Exception:
            pass

    def aod_lang_index():
        cur = aod_get_lang_code()
        for i, (code, _name) in enumerate(AOD_LANGS):
            if code == cur:
                return i
        return 0

    def aod_lang_label():
        i = aod_lang_index()
        return AOD_LANGS[i][1] if 0 <= i < len(AOD_LANGS) else "—"

    def aod_lang_prev():
        if not AOD_LANGS:
            return
        i = (aod_lang_index() - 1) % len(AOD_LANGS)
        aod_set_lang_code(AOD_LANGS[i][0])

    def aod_lang_next():
        if not AOD_LANGS:
            return
        i = (aod_lang_index() + 1) % len(AOD_LANGS)
        aod_set_lang_code(AOD_LANGS[i][0])


# ======================================================================
# COMPONENTES DE FILAS (SCREENS REUTILIZABLES)
# ======================================================================

screen aod_row_arrows(idx, selected, label, value_text, on_left, on_right, hk,
                      col_label_w, col_arrow_w, col_value_w, row_h, hover_idx=-1):
    $ _is_hover = (hover_idx == idx)
    $ _bg = AOD_ROW_BG_SEL if selected else (AOD_ROW_BG_HOVER if _is_hover else AOD_ROW_BG_IDLE)
    frame:
        background _bg
        xfill True
        ysize row_h
        padding (AOD_INNER_PAD, int(round(8 * _AOD_SCALE)))
        $ _ctrl_h = row_h - int(round(16 * _AOD_SCALE))
        $ _sp = AOD_SPACING_VBOX
        $ val = value_text() if callable(value_text) else value_text
        hbox:
            spacing _sp
            yalign 0.5
            frame:
                background None
                xsize col_label_w
                yfill True
                button:
                    background None
                    action NullAction()
                    keyboard_focus False
                    hovered [ SetScreenVariable("help_key", hk), SetScreenVariable("row_hover", idx) ]
                    unhovered SetScreenVariable("row_hover", -1)
                    text label color AOD_COL_TEXT size AOD_SIZE_TEXT yalign 0.5
            button:
                xsize col_arrow_w
                ysize _ctrl_h
                yalign 0.5
                background AOD_ARROW_BOX_IDLE
                hover_background AOD_ARROW_BOX_HOVER
                keyboard_focus False
                action on_left
                hovered [ SetScreenVariable("help_key", hk), SetScreenVariable("row_hover", idx) ]
                unhovered SetScreenVariable("row_hover", -1)
                if AOD_ICON_ARROW_L:
                    add AOD_ICON_ARROW_L xalign 0.5 yalign 0.5
            button:
                background (AOD_VALUE_BG_ACTIVE if selected and AOD_VALUE_BG_ACTIVE else AOD_VALUE_BG)
                xsize col_value_w
                ysize _ctrl_h
                yalign 0.5
                padding (int(round(10 * _AOD_SCALE)), int(round(4 * _AOD_SCALE)))
                keyboard_focus False
                action NullAction()
                hovered [ SetScreenVariable("help_key", hk), SetScreenVariable("row_hover", idx) ]
                unhovered SetScreenVariable("row_hover", -1)
                text val color AOD_COL_TEXT size AOD_SIZE_TEXT xalign 0.5 yalign 0.5
            button:
                xsize col_arrow_w
                ysize _ctrl_h
                yalign 0.5
                background AOD_ARROW_BOX_IDLE
                hover_background AOD_ARROW_BOX_HOVER
                keyboard_focus False
                action on_right
                hovered [ SetScreenVariable("help_key", hk), SetScreenVariable("row_hover", idx) ]
                unhovered SetScreenVariable("row_hover", -1)
                if AOD_ICON_ARROW_R:
                    add AOD_ICON_ARROW_R xalign 0.5 yalign 0.5

screen aod_row_button(idx, selected, label, button_text, on_press, hk,
                      col_label_w, col_button_w, row_h, hover_idx=-1):
    $ _is_hover = (hover_idx == idx)
    $ _bg = AOD_ROW_BG_SEL if selected else (AOD_ROW_BG_HOVER if _is_hover else AOD_ROW_BG_IDLE)
    frame:
        background _bg
        xfill True
        ysize row_h
        padding (AOD_INNER_PAD, int(round(8 * _AOD_SCALE)))
        $ _ctrl_h = row_h - int(round(16 * _AOD_SCALE))
        $ _sp = AOD_SPACING_VBOX
        hbox:
            spacing _sp
            yalign 0.5
            frame:
                background None
                xsize col_label_w
                yfill True
                button:
                    background None
                    action NullAction()
                    keyboard_focus False
                    hovered [ SetScreenVariable("help_key", hk), SetScreenVariable("row_hover", idx) ]
                    unhovered SetScreenVariable("row_hover", -1)
                    text label color AOD_COL_TEXT size AOD_SIZE_TEXT yalign 0.5
            button:
                xsize col_button_w
                ysize _ctrl_h
                yalign 0.5
                background AOD_ARROW_BOX_IDLE
                hover_background AOD_ARROW_BOX_HOVER
                keyboard_focus False
                action on_press
                hovered [ SetScreenVariable("help_key", hk), SetScreenVariable("row_hover", idx) ]
                unhovered SetScreenVariable("row_hover", -1)
                text button_text color AOD_COL_TEXT size AOD_SIZE_SUBTEXT xalign 0.5 yalign 0.5


# ======================================================================
# ESTILOS (ESTANDARIZADOS)
# ======================================================================

style aod_keycap is default:
    background Solid("#263349")
    xsize AOD_ICON_SIZE
    ysize AOD_ICON_SIZE
    xminimum AOD_ICON_SIZE
    yminimum AOD_ICON_SIZE
    padding (0, 0)

style aod_foot_label is default:
    color AOD_COL_MUTED
    size AOD_SIZE_SMALL


# ======================================================================
# SCREEN ÚNICO: preferences
# ======================================================================

screen preferences():
    tag menu
    modal True

    default current_tab_id = "general"
    default tab_sel = 0
    default row_sel = 0
    default help_key = None
    default row_hover = -1
    default nav_rows = []
    default _use_pad = True

    # Fondo
    $ _bg = Solid(AOD_COL_BG)
    if renpy.loadable(AOD_BG_MAIN):
        $ iw, ih = renpy.image_size(AOD_BG_MAIN)
        $ zx = float(config.screen_width)  / float(iw)
        $ zy = float(config.screen_height) / float(ih)
        $ _bg = Transform(AOD_BG_MAIN, zoom=max(zx, zy), xalign=0.5, yalign=0.5)
    add _bg

    $ _W = config.screen_width  - AOD_MARGIN*2
    $ _H = config.screen_height - AOD_MARGIN*2

    frame:
        background AOD_PANEL_BG
        xalign 0.5
        yalign 0.5
        xsize _W
        ysize _H
        padding (AOD_GUTTER, AOD_GUTTER)

        vbox:
            spacing AOD_GUTTER

            # ===== Tabs =====
            $ _tabs_n      = len(AOD_TABS)
            $ _gap         = int(round(10 * _AOD_SCALE))
            $ _tabs_area_w = _W
            $ _tab_w       = int((_tabs_area_w - _gap * (_tabs_n - 1)) / _tabs_n)
            hbox:
                spacing _gap
                xfill True
                for i, (tid, tlabel) in enumerate(AOD_TABS):
                    $ sel = (tid == current_tab_id)
                    button:
                        xsize _tab_w
                        yminimum AOD_TAB_H
                        background (AOD_TAB_BG_SEL if sel else AOD_TAB_BG)
                        hover_background (AOD_TAB_BG_SEL if sel else AOD_TAB_BG_HOVER)
                        padding (int(round(8 * _AOD_SCALE)), int(round(6 * _AOD_SCALE)))
                        keyboard_focus False
                        action [
                            SetScreenVariable("current_tab_id", tid),
                            SetScreenVariable("tab_sel", i),
                            SetScreenVariable("row_sel", 0),
                            SetScreenVariable("help_key", None)
                        ]
                        text tlabel color (AOD_COL_ACCENT2 if sel else AOD_COL_TEXT) size AOD_SIZE_SUBTEXT xalign 0.5 yalign 0.5

            # ===== Centro =====
            $ _center_h = _H - (AOD_GUTTER*3 + AOD_FOOTER_H + int(round(36 * _AOD_SCALE)))
            hbox:
                spacing AOD_GUTTER
                ysize _center_h
                xfill True

                # Distribución 68%/32% (igual que loadsave)
                $ _left_w = int(_W * 0.68)
                $ _right_w = max(280, _W - _left_w - AOD_GUTTER - AOD_RIGHT_BREATH)
                
                frame:
                    background AOD_CONTENT_BG
                    xsize _left_w
                    yfill True
                    padding (0, AOD_GUTTER)

                    # Anchos de columnas
                    $ _inner_w      = _left_w
                    $ _col_label_w  = int(_inner_w * 0.50)
                    $ _col_arrow_w  = AOD_ARROW_W
                    $ _col_value_w  = int(_inner_w * 0.30)

                    python:
                        rows = []
                        if current_tab_id == "general":
                            rows = [
                                { "label":"Modo de pantalla", "val": (lambda: ("Pantalla completa" if preferences.fullscreen else "Ventana")), "left": Preference("display", "toggle"), "right": Preference("display", "toggle"), "hk":"Modo de pantalla" },
                                { "label":"Transiciones", "val": (lambda: ("Activadas" if preferences.transitions == 2 else "Desactivadas")), "left": Preference("transitions", "toggle"), "right": Preference("transitions", "toggle"), "hk":"Transiciones" },
                                { "label":"Cursor del sistema", "val": (lambda: ("Activado" if preferences.system_cursor else "Desactivado")), "left": Preference("system cursor", "toggle"), "right": Preference("system cursor", "toggle"), "hk":"Cursor del sistema" },
                                { "label":"Restaurar posición", "val": (lambda: ("Sí" if preferences.restore_window_position else "No")), "left": Preference("restore window position", "toggle"), "right": Preference("restore window position", "toggle"), "hk":"Restaurar posición" },
                                { "label":"Ahorro de energía (GL)", "val": (lambda: ("Activado" if preferences.gl_powersave else "Desactivado")), "left": Preference("gl powersave", not preferences.gl_powersave), "right": Preference("gl powersave", not preferences.gl_powersave), "hk":"Ahorro GL" },
                                { "label":"Tearing (GL)", "val": (lambda: ("Tear" if preferences.gl_tearing else "Frameskip")), "left": Preference("gl tearing", not preferences.gl_tearing), "right": Preference("gl tearing", not preferences.gl_tearing), "hk":"Tearing" },
                            ]
                        elif current_tab_id == "audio":
                            rows = [
                                { "label":"Volumen música", "val": (lambda: ("Silenciado" if aod_is_muted("music") else "{}%".format(aod_get_pct("music")))), "left": Function(aod_step_pct, "music", -5), "right": Function(aod_step_pct, "music", +5), "hk":"Volumen música" },
                                { "label":"Silenciar música", "val": (lambda: ("Sí" if aod_is_muted("music") else "No")), "left": Function(aod_toggle_mute, "music"), "right": Function(aod_toggle_mute, "music"), "hk":"Silenciar música" },
                                { "label":"Volumen efectos", "val": (lambda: ("Silenciado" if aod_is_muted("sound") else "{}%".format(aod_get_pct("sound")))), "left": Function(aod_step_pct, "sound", -5), "right": Function(aod_step_pct, "sound", +5), "hk":"Volumen efectos" },
                                { "label":"Silenciar efectos", "val": (lambda: ("Sí" if aod_is_muted("sound") else "No")), "left": Function(aod_toggle_mute, "sound"), "right": Function(aod_toggle_mute, "sound"), "hk":"Silenciar efectos" },
                                { "type":"button", "label":"Reproducir efectos", "btn_text":"Reproducir", "press": Function(aod_test, "sound"), "hk":"Probar efectos" },
                                { "label":"Volumen voz", "val": (lambda: ("Silenciado" if aod_is_muted("voice") else "{}%".format(aod_get_pct("voice")))), "left": Function(aod_step_pct, "voice", -5), "right": Function(aod_step_pct, "voice", +5), "hk":"Volumen voz" },
                                { "label":"Silenciar voz", "val": (lambda: ("Sí" if aod_is_muted("voice") else "No")), "left": Function(aod_toggle_mute, "voice"), "right": Function(aod_toggle_mute, "voice"), "hk":"Silenciar voz" },
                                { "type":"button", "label":"Reproducir voz", "btn_text":"Reproducir", "press": Function(aod_test, "voice"), "hk":"Probar voz" },
                            ]
                        elif current_tab_id == "texto":
                            rows = [
                                { "label":"Velocidad del texto", "val": (lambda: ("0" if aod_get_level("textspeed")==0 else str(aod_get_level("textspeed")))), "left": Function(aod_step_level, "textspeed", -1), "right": Function(aod_step_level, "textspeed", +1), "hk":"Velocidad del texto" },
                                { "label":"Auto-avance", "val": (lambda: ("0" if aod_get_level("afm")==0 else str(aod_get_level("afm")))), "left": Function(aod_step_level, "afm", -1), "right": Function(aod_step_level, "afm", +1), "hk":"Auto-avance" },
                                { "label":"Omitir no vistos", "val": (lambda: ("Sí" if preferences.skip_unseen else "No")), "left": Function(lambda: setattr(preferences, "skip_unseen", not preferences.skip_unseen)), "right": Function(lambda: setattr(preferences, "skip_unseen", not preferences.skip_unseen)), "hk":"Omitir no vistos" },
                                { "label":"Después de elegir", "val": (lambda: ("Continuar" if preferences.skip_after_choices else "Detener")), "left": Function(lambda: setattr(preferences, "skip_after_choices", not preferences.skip_after_choices)), "right": Function(lambda: setattr(preferences, "skip_after_choices", not preferences.skip_after_choices)), "hk":"Después de elegir" },
                                { "label":"Click cancela AFM", "val": (lambda: ("Sí" if preferences.afm_after_click else "No")), "left": Function(lambda: setattr(preferences, "afm_after_click", not preferences.afm_after_click)), "right": Function(lambda: setattr(preferences, "afm_after_click", not preferences.afm_after_click)), "hk":"Click cancela AFM" },
                            ]
                        elif current_tab_id == "acces_idioma":
                            rows = [
                                { "label":"Idioma", "val": (lambda: aod_lang_label()), "left": Function(aod_lang_prev), "right": Function(aod_lang_next), "hk":"Idioma" },
                            ]
                        nav_rows = rows

                    vbox:
                        spacing AOD_SPACING_VBOX
                        xfill True
                        
                        frame:
                            background None
                            xfill True
                            padding (AOD_SIDE_PAD, 0)
                            if current_tab_id == "general":
                                text "GENERAL" color AOD_COL_ACCENT size AOD_SIZE_TITLE
                            elif current_tab_id == "audio":
                                text "AUDIO" color AOD_COL_ACCENT size AOD_SIZE_TITLE
                            elif current_tab_id == "texto":
                                text "TEXTO & FLUJO" color AOD_COL_ACCENT size AOD_SIZE_TITLE
                            elif current_tab_id == "acces_idioma":
                                text "ACCESIBILIDAD & IDIOMA" color AOD_COL_ACCENT size AOD_SIZE_TITLE

                        for i, r in enumerate(rows):
                            $ sel = (i == row_sel)
                            frame:
                                background None
                                xfill True
                                padding (AOD_SIDE_PAD, 0)
                                if r.get("type", None) == "button":
                                    $ _btn_w = int(_col_value_w + _col_arrow_w*2 + AOD_SPACING_VBOX*2)
                                    use aod_row_button(i, sel, r["label"], r.get("btn_text", "Reproducir"), r["press"], r["hk"], _col_label_w, _btn_w, AOD_ROW_H, row_hover)
                                else:
                                    use aod_row_arrows(i, sel, r["label"], r["val"], r["left"], r["right"], r["hk"], _col_label_w, _col_arrow_w, _col_value_w, AOD_ROW_H, row_hover)

                # Columna derecha (ayuda)
                $ _help_top_shift = AOD_GUTTER + AOD_SIZE_TITLE + AOD_SPACING_VBOX
                $ _help_bottom_shift = int(round(8 * _AOD_SCALE))

                frame:
                    background None
                    xsize _right_w
                    ysize _center_h
                    vbox:
                        spacing 0
                        xfill True
                        yfill True
                        null height _help_top_shift
                        frame:
                            background AOD_HELP_BG
                            xfill True
                            ysize _center_h - _help_top_shift - _help_bottom_shift
                            padding (AOD_SIDE_PAD, AOD_GUTTER + int(round(6 * _AOD_SCALE)))
                            $ _hk = None
                            if AOD_USE_MOUSE_HOVER and (row_hover != -1) and (row_hover < len(nav_rows)):
                                $ _hk = nav_rows[row_hover].get("hk", None)
                            elif (0 <= row_sel < len(nav_rows)):
                                $ _hk = nav_rows[row_sel].get("hk", None)
                            $ ht, hx = AOD_HELP.get(_hk, ("AYUDA", "Usa ↑/↓ para seleccionar; ←/→ para cambiar; Q/E para pestañas."))
                            vbox:
                                spacing AOD_SPACING_VBOX
                                text ht color AOD_COL_ACCENT size AOD_SIZE_TITLE
                                text hx color AOD_COL_TEXT size AOD_SIZE_SUBTEXT
                        null height _help_bottom_shift

            # ===== FOOTER (ESTANDARIZADO - alineado a la derecha) =====
            frame:
                background None
                yminimum AOD_FOOTER_H
                xfill True
                fixed:
                    xfill True yfill True
                    hbox:
                        xpos 1.0
                        xanchor 1.0
                        spacing AOD_SPACING_FOOT
                        yalign 0.5
                        $ _footer_items = [
                            (_("Cambiar pestaña"), AOD_CAP_QE),
                            (_("Mover foco"), AOD_CAP_UD),
                            (_("Cambiar valor"), AOD_CAP_LR),
                            (_("Confirmar"), AOD_CAP_ENTER),
                            (_("Volver"), AOD_CAP_ESC),
                        ]
                        for _label, _cap in _footer_items:
                            hbox:
                                spacing AOD_SPACING_VBOX
                                yalign 0.5
                                frame:
                                    style "aod_keycap"
                                    text _cap color AOD_COL_TEXT size (AOD_SIZE_INFO - 2) xalign 0.5 yalign 0.5
                                text _label style "aod_foot_label" yalign 0.5

    # ===== HOTKEYS =====
    key "K_q" action [SetScreenVariable("tab_sel", (tab_sel - 1) % len(AOD_TABS)), SetScreenVariable("current_tab_id", AOD_TABS[(tab_sel - 1) % len(AOD_TABS)][0]), SetScreenVariable("row_sel", 0), SetScreenVariable("help_key", None)]
    key "K_e" action [SetScreenVariable("tab_sel", (tab_sel + 1) % len(AOD_TABS)), SetScreenVariable("current_tab_id", AOD_TABS[(tab_sel + 1) % len(AOD_TABS)][0]), SetScreenVariable("row_sel", 0), SetScreenVariable("help_key", None)]
    key "K_PAGEUP" action [SetScreenVariable("tab_sel", (tab_sel - 1) % len(AOD_TABS)), SetScreenVariable("current_tab_id", AOD_TABS[(tab_sel - 1) % len(AOD_TABS)][0]), SetScreenVariable("row_sel", 0), SetScreenVariable("help_key", None)]
    key "K_PAGEDOWN" action [SetScreenVariable("tab_sel", (tab_sel + 1) % len(AOD_TABS)), SetScreenVariable("current_tab_id", AOD_TABS[(tab_sel + 1) % len(AOD_TABS)][0]), SetScreenVariable("row_sel", 0), SetScreenVariable("help_key", None)]
    if _use_pad:
        key "pad_leftshoulder" action [SetScreenVariable("tab_sel", (tab_sel - 1) % len(AOD_TABS)), SetScreenVariable("current_tab_id", AOD_TABS[(tab_sel - 1) % len(AOD_TABS)][0]), SetScreenVariable("row_sel", 0), SetScreenVariable("help_key", None)]
        key "pad_rightshoulder" action [SetScreenVariable("tab_sel", (tab_sel + 1) % len(AOD_TABS)), SetScreenVariable("current_tab_id", AOD_TABS[(tab_sel + 1) % len(AOD_TABS)][0]), SetScreenVariable("row_sel", 0), SetScreenVariable("help_key", None)]
    key "K_UP" action If(len(nav_rows) > 0, SetScreenVariable("row_sel", (row_sel - 1) % len(nav_rows)), NullAction())
    key "K_DOWN" action If(len(nav_rows) > 0, SetScreenVariable("row_sel", (row_sel + 1) % len(nav_rows)), NullAction())
    key "K_w" action If(len(nav_rows) > 0, SetScreenVariable("row_sel", (row_sel - 1) % len(nav_rows)), NullAction())
    key "K_s" action If(len(nav_rows) > 0, SetScreenVariable("row_sel", (row_sel + 1) % len(nav_rows)), NullAction())
    if _use_pad:
        key "pad_dpup" action If(len(nav_rows) > 0, SetScreenVariable("row_sel", (row_sel - 1) % len(nav_rows)), NullAction())
        key "pad_dpdown" action If(len(nav_rows) > 0, SetScreenVariable("row_sel", (row_sel + 1) % len(nav_rows)), NullAction())
    key "K_LEFT" action aod_get_action(nav_rows, row_sel, "left")
    key "K_RIGHT" action aod_get_action(nav_rows, row_sel, "right")
    key "K_a" action aod_get_action(nav_rows, row_sel, "left")
    key "K_d" action aod_get_action(nav_rows, row_sel, "right")
    if _use_pad:
        key "pad_dpleft" action aod_get_action(nav_rows, row_sel, "left")
        key "pad_dpright" action aod_get_action(nav_rows, row_sel, "right")
    key "K_RETURN" action aod_get_submit_action(nav_rows, row_sel)
    key "K_KP_ENTER" action aod_get_submit_action(nav_rows, row_sel)
    if _use_pad:
        key "pad_a" action aod_get_submit_action(nav_rows, row_sel)
    key "K_ESCAPE" action ShowMenu("main_menu")
    key "mouseup_3" action ShowMenu("main_menu")
    if _use_pad:
        key "pad_b" action ShowMenu("main_menu")