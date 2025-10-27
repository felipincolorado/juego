## src/screens/gui_loadsave.rpy
## Menú Cargar/Guardar – The Gilded Cage (Ren'Py 8.4.x)
## Versión estandarizada: TAB robusto (pygame + cooldown), bloqueo Save en main_menu,
## guías dinámicas, keycaps cuadrados alineados a la derecha.

# --------------------------
# Estado global
# --------------------------
default aod_ls_sel         = 1
default aod_ls_preview     = 1
default aod_input_mode     = "kb"   # "kb" o "pad"
default _aod_tab_down      = False  # estado TAB para modo nuclear
default _aod_tab_cooldown  = 0      # cooldown de frames tras alternar

# =========================
# CONFIG & ESTILOS
# =========================
init -30 python:
    # ---- Flags / ajustes ----
    AOD_ENABLE_PYGAME_TAB = True     # lector nuclear de TAB via pygame

    # ---- Escalado base ----
    try:
        _AOD_SCALE = float(config.screen_height) / 1080.0
        _AOD_SCALE = max(0.70, min(2.00, _AOD_SCALE))
    except Exception:
        _AOD_SCALE = 1.0

    # ---- Helpers de assets ----
    def aod_frame_or_solid(path, ltrb, fallback_color):
        try:
            if renpy.loader.loadable(path):
                l, t, r, b = ltrb
                return Frame(path, l, t, r, b)
        except Exception:
            pass
        return Solid(fallback_color)

    # ---- Paleta (ESTANDARIZADA) ----
    AOD_COL_BG      = "#0f1218"
    AOD_COL_PANEL   = "#141925"
    AOD_COL_TEXT    = "#E6E6E6"
    AOD_COL_ACCENT  = "#c9a86a"
    AOD_COL_MUTED   = "#BFC6D4"
    AOD_COL_DIVIDER = "#1e2a3d"
    AOD_COL_THUMB   = "#c9a86a"

    # ---- Métricas globales (ESTANDARIZADAS) ----
    AOD_MARGIN       = int(round(40 * _AOD_SCALE))
    AOD_GUTTER       = int(round(18 * _AOD_SCALE))
    AOD_FOOTER_H     = int(round(44 * _AOD_SCALE))
    AOD_SIDE_PAD     = int(round(32 * _AOD_SCALE))
    AOD_INNER_PAD    = int(round(12 * _AOD_SCALE))

    # ---- Métricas específicas LoadSave ----
    LS_ROW_H        = int(round(140 * _AOD_SCALE))
    LS_ROW_SPACING  = max(12, int(round(0.12 * LS_ROW_H)))
    def ls_block_height(): return LS_ROW_H + LS_ROW_SPACING

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

    # ---- Assets ----
    AOD_ASSET_ROOT    = "assets/art/gui/"
    def ui9(name, ltrb, fallback): return aod_frame_or_solid(AOD_ASSET_ROOT + name, ltrb, fallback)
    
    AOD_BG_MAIN       = AOD_ASSET_ROOT + "bg_main.png"
    AOD_PANEL_BG      = ui9("panel_bg.png",         (24,24,24,24), AOD_COL_PANEL)
    AOD_VALUE_BG      = ui9("value_bg.png",         (12,12,12,12), "#1f293b")
    AOD_ROW_BG_IDLE   = ui9("row_bg.png",           (16,16,16,16), "#202b3f")
    AOD_ROW_BG_HOVER  = ui9("row_bg_hover.png",     (16,16,16,16), "#2b3a55")
    AOD_ROW_BG_SEL    = ui9("row_selected.png",     (16,16,16,16), "#314262")
    AOD_PREVIEW_PANEL = ui9("ls_preview_panel.png", (16,16,16,16), "#0f1826")
    AOD_PREVIEW_BG    = ui9("ls_preview_bg.png",    (12,12,12,12), "#0b1220")
    AOD_PREVIEW_PH    = AOD_ASSET_ROOT + "ls_preview_placeholder.png"

    # ---- Keycaps (ESTANDARIZADOS) ----
    AOD_ICON_SIZE  = int(round(44 * _AOD_SCALE))
    AOD_CAP_UD     = "↑/↓"
    AOD_CAP_ENT    = "↵"
    AOD_CAP_ESC    = "Esc"
    AOD_CAP_TAB    = "⇥"

    # ---- Config LoadSave ----
    AOD_SLOTS_TOTAL      = 60
    AOD_THUMB_W          = int(round(276 * _AOD_SCALE))
    AOD_THUMB_H          = int(round(156 * _AOD_SCALE))
    AOD_TIME_PILL_W      = int(round(174 * _AOD_SCALE))
    AOD_LS_MOCK          = False
    AOD_SHOW_LIST_THUMBS = False
    AOD_RIGHT_BREATH     = int(round(56 * _AOD_SCALE))

    # ---- Persistencia metadatos ----
    if not isinstance(getattr(persistent, "aod_slot_meta", None), dict):
        persistent.aod_slot_meta = {}
    def aod_get_slot_meta(i): return dict(persistent.aod_slot_meta.get(i, {}))

    # ---- Scroll helper ----
    def aod_ls_ensure_visible(adj, n, vp_h):
        row_h = ls_block_height()
        y_top = max(0, int(n - 1) * row_h)
        y_bot = y_top + row_h
        try: adj.page = vp_h
        except Exception: pass
        cur = float(getattr(adj, "value", 0.0))
        if y_top < cur:
            try: adj.value = y_top
            except Exception: pass
        elif y_bot > cur + vp_h:
            try: adj.value = max(0.0, y_bot - vp_h)
            except Exception: pass

    # ---- Input helpers ----
    def aod_gamepad_present():
        try:
            try:
                import pygame_sdl2 as pygame
            except Exception:
                import pygame
            if hasattr(pygame, "joystick"):
                pygame.joystick.init()
                return pygame.joystick.get_count() > 0
        except Exception:
            pass
        return False

    def aod_set_input_mode(mode):
        if mode not in ("kb", "pad"):
            return
        store.aod_input_mode = mode
        try:
            persistent.aod_last_input_mode = mode
        except Exception:
            pass

    def aod_detect_input_mode():
        try:
            if hasattr(persistent, "aod_last_input_mode") and persistent.aod_last_input_mode in ("kb","pad"):
                aod_set_input_mode(persistent.aod_last_input_mode)
                return
        except Exception:
            pass
        aod_set_input_mode("pad" if aod_gamepad_present() else "kb")

    # ---- TAB: quitar del keymap global ----
    def aod_tab_grab(enable):
        import renpy.config
        if enable:
            if not hasattr(store, "_aod_tab_backup"):
                store._aod_tab_backup = {}
            for action_name in list(renpy.config.keymap.keys()):
                original = renpy.config.keymap[action_name]
                if not isinstance(original, list):
                    continue
                filtered = []
                changed = False
                for binding in original:
                    bs = str(binding).upper()
                    if "TAB" in bs:
                        changed = True
                    else:
                        filtered.append(binding)
                if changed:
                    store._aod_tab_backup[action_name] = list(original)
                    renpy.config.keymap[action_name] = filtered
        else:
            if hasattr(store, "_aod_tab_backup"):
                for action_name, original in store._aod_tab_backup.items():
                    renpy.config.keymap[action_name] = original
                store._aod_tab_backup = {}

    # ---- TAB nuclear: pygame con cooldown + bloqueo main_menu ----
    def _poll_tab_and_toggle(target):
        if not AOD_ENABLE_PYGAME_TAB:
            return

        # Bloquear Save en main_menu
        if target == "save" and main_menu:
            cd = int(getattr(store, "_aod_tab_cooldown", 0) or 0)
            if cd > 0:
                store._aod_tab_cooldown = cd - 1
                return

            is_down = False
            try:
                try:
                    import pygame_sdl2 as pygame
                except Exception:
                    import pygame
                keys = pygame.key.get_pressed()
                is_down = bool(keys[getattr(pygame, "K_TAB", 9)])
            except Exception:
                pass

            prev = bool(getattr(store, "_aod_tab_down", False))
            if is_down and not prev:
                store._aod_tab_down = True
                store._aod_tab_cooldown = 10
                renpy.notify(_("No puedes guardar sin iniciar partida"))
            elif not is_down and prev:
                store._aod_tab_down = False
            return

        # Cooldown normal
        cd = int(getattr(store, "_aod_tab_cooldown", 0) or 0)
        if cd > 0:
            store._aod_tab_cooldown = cd - 1
            return

        is_down = False
        try:
            try:
                import pygame_sdl2 as pygame
            except Exception:
                import pygame
            keys = pygame.key.get_pressed()
            is_down = bool(keys[getattr(pygame, "K_TAB", 9)])
        except Exception:
            is_down = False

        prev = bool(getattr(store, "_aod_tab_down", False))

        if is_down and not prev:
            store._aod_tab_down = True
            store._aod_tab_cooldown = 10
            aod_set_input_mode("kb")

            try:
                current_is_load = bool(renpy.get_screen("load"))
                current = "load" if current_is_load else "save"
                renpy.hide_screen(current)
            except:
                pass

            renpy.show_screen(target)
            renpy.restart_interaction()

        elif (not is_down) and prev:
            store._aod_tab_down = False

# ===== ESTILOS (ESTANDARIZADOS) =====
style aod_vbar is vscrollbar:
    xsize int(round(14 * _AOD_SCALE))
    unscrollable "hide"
    thumb Solid(AOD_COL_THUMB)

style aod_cta_button is default:
    background Solid("#23314a")
    hover_background Solid("#2e3e58")
    insensitive_background Solid("#1a2333")
    padding (int(round(18 * _AOD_SCALE)), int(round(14 * _AOD_SCALE)))
    xminimum 0
    xmaximum 1920

style aod_cta_text is default:
    color AOD_COL_TEXT
    size AOD_SIZE_TEXT

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

# =========================
# FILA DE SLOT
# =========================
screen aod_slot_row(i, mode):
    python:
        is_selected = (aod_ls_sel == i)
        is_auto = (i == 1)
        
        if AOD_LS_MOCK:
            title = _("Autoguardado") if is_auto else _("Slot {i}").format(i=i)
            meta = {"chapter": _("Capítulo pendiente"), "location": "—"}
            when_txt = _("hoy 12:{:02d}").format((i*7) % 60)
            has_data = True
            screenshot = None
        else:
            title = _("Autoguardado") if is_auto else (FileSaveName(i) or _("Slot {i}").format(i=i))
            has_data = FileLoadable(i)
            meta = aod_get_slot_meta(i) if has_data else {}
            when_txt = FileTime(i, empty=_("No hay partida"))
            screenshot = FileScreenshot(i) if (has_data and AOD_SHOW_LIST_THUMBS) else None

        chapter  = meta.get("chapter", _("Capítulo pendiente"))
        location = meta.get("location", _("—"))
        diff     = meta.get("difficulty", _("—"))
        mode_txt = meta.get("mode", _("—"))
        runtime  = meta.get("playtime", _("—"))

        is_hovered = (aod_ls_preview == i)
        bg = (AOD_ROW_BG_SEL if is_selected else (AOD_ROW_BG_HOVER if is_hovered else AOD_ROW_BG_IDLE))

    frame:
        background None
        xfill True
        ysize LS_ROW_H
        padding (AOD_INNER_PAD, AOD_INNER_PAD)

        button:
            xfill True
            ysize LS_ROW_H
            keyboard_focus False
            background bg
            hover_background bg

            hovered SetVariable("aod_ls_preview", i)
            unhovered If(aod_ls_preview == i, SetVariable("aod_ls_preview", aod_ls_sel), NullAction())
            action [ SetVariable("aod_ls_sel", i), SetVariable("aod_ls_preview", i) ]

            hbox:
                spacing AOD_SPACING_HBOX
                xfill True
                yalign 0.5

                null width int(round(10 * _AOD_SCALE))

                frame:
                    background AOD_VALUE_BG
                    xsize int(round(86 * _AOD_SCALE))
                    ysize int(round(86 * _AOD_SCALE))
                    yalign 0.5

                vbox:
                    spacing AOD_SPACING_VBOX
                    xfill True
                    yalign 0.5

                    hbox:
                        spacing AOD_SPACING_VBOX
                        xfill True
                        yalign 0.5

                        frame:
                            background None
                            xfill True
                            yminimum int(round(32 * _AOD_SCALE))
                            text title color AOD_COL_TEXT size AOD_SIZE_TEXT yalign 0.5

                        frame:
                            background AOD_VALUE_BG
                            padding (AOD_INNER_PAD, int(round(6 * _AOD_SCALE)))
                            xsize AOD_TIME_PILL_W
                            yalign 0.5
                            text when_txt color AOD_COL_MUTED size AOD_SIZE_INFO xalign 0.5

                    text "[chapter]  •  [location]" color AOD_COL_TEXT size AOD_SIZE_SUBTEXT

                    hbox:
                        spacing AOD_SPACING_HBOX
                        yalign 0.5
                        for label, value in [(_("Dificultad:"), diff), (_("Modo:"), mode_txt), (_("Tiempo:"), runtime)]:
                            if value != _("—"):
                                frame:
                                    background AOD_VALUE_BG
                                    padding (AOD_INNER_PAD, int(round(6 * _AOD_SCALE)))
                                    yalign 0.5
                                    text _("{l} {v}").format(l=label, v=value) color AOD_COL_TEXT size AOD_SIZE_INFO

                null width int(round(16 * _AOD_SCALE))

                frame:
                    background AOD_VALUE_BG
                    xsize AOD_THUMB_W
                    ysize AOD_THUMB_H
                    yalign 0.5
                    if screenshot:
                        add screenshot fit "cover" xsize AOD_THUMB_W ysize AOD_THUMB_H
                    else:
                        text (_("Vista previa") if AOD_LS_MOCK else _("Sin imagen")) color AOD_COL_MUTED size AOD_SIZE_INFO xalign 0.5 yalign 0.5

# =========================
# PANTALLA PRINCIPAL
# =========================
screen aod_loadsave(mode="load"):
    tag menu
    modal True

    $ _cta_action = NullAction()

    on "show" action [
        SetVariable("aod_ls_preview", aod_ls_sel),
        Function(aod_detect_input_mode),
        Function(aod_tab_grab, True),
    ]
    on "hide" action Function(aod_tab_grab, False)
    on "replaced" action Function(aod_tab_grab, False)

    # Fondo
    $ _bg = Solid(AOD_COL_BG)
    if renpy.loader.loadable(AOD_BG_MAIN):
        $ iw, ih = renpy.image_size(AOD_BG_MAIN)
        $ zx = float(config.screen_width) / float(iw)
        $ zy = float(config.screen_height) / float(ih)
        $ _bg = Transform(AOD_BG_MAIN, zoom=max(zx, zy), xalign=0.5, yalign=0.5)
    add _bg

    default _adj = ui.adjustment()

    $ _W = config.screen_width  - AOD_MARGIN*2
    $ _H = config.screen_height - AOD_MARGIN*2
    $ _vp_h = _H - (AOD_FOOTER_H + int(round(120 * _AOD_SCALE)))
    $ _left_w  = int(_W * 0.68)
    $ _right_w = max(280, _W - _left_w - 1 - AOD_SPACING_VBOX - AOD_RIGHT_BREATH)

    frame:
        background AOD_PANEL_BG
        xalign 0.5 yalign 0.5
        xsize _W ysize _H
        padding (AOD_GUTTER, AOD_GUTTER)

        vbox:
            spacing AOD_GUTTER
            xfill True yfill True

            text (_("Cargar partidas") if mode=="load" else _("Guardar partida")):
                color AOD_COL_ACCENT
                size AOD_SIZE_TITLE
                xalign 0.0
                xoffset AOD_SIDE_PAD

            hbox:
                spacing AOD_SPACING_VBOX
                xfill True
                ysize _vp_h

                frame:
                    background AOD_VALUE_BG
                    padding (AOD_SIDE_PAD, AOD_INNER_PAD)
                    xsize _left_w
                    ysize _vp_h

                    fixed:
                        xfill True yfill True

                        viewport id "aod_ls_vp":
                            xfill True yfill True
                            draggable True
                            mousewheel True
                            yadjustment _adj
                            arrowkeys False
                            pagekeys False

                            frame:
                                background None
                                padding (0, 0, AOD_INNER_PAD, 0)
                                has vbox
                                spacing LS_ROW_SPACING
                                xfill True
                                for i in range(1, AOD_SLOTS_TOTAL + 1):
                                    use aod_slot_row(i, mode)

                        vbar adjustment _adj style "aod_vbar" yfill True xalign 1.0 xoffset -(AOD_INNER_PAD/2)

                frame:
                    background Solid(AOD_COL_DIVIDER)
                    xsize 1 ysize _vp_h

                frame:
                    background AOD_PREVIEW_PANEL
                    xsize _right_w ysize _vp_h
                    padding (AOD_SIDE_PAD, AOD_INNER_PAD, AOD_SIDE_PAD, AOD_INNER_PAD)

                    vbox:
                        spacing AOD_SPACING_VBOX
                        xfill True yfill True

                        $ _cur = aod_ls_preview
                        $ _slot_name = (_("Autoguardado") if _cur == 1 else _("Slot {n}").format(n=_cur))
                        text _slot_name color AOD_COL_ACCENT size AOD_SIZE_TEXT

                        frame:
                            background AOD_PREVIEW_BG
                            xfill True
                            ysize int(_vp_h * 0.52)
                            padding (AOD_INNER_PAD, AOD_INNER_PAD)
                            $ _has_data_sel_prev = (not AOD_LS_MOCK and FileLoadable(_cur))
                            if _has_data_sel_prev:
                                frame:
                                    xfill True yfill True
                                    add FileScreenshot(_cur) fit "cover"
                            elif renpy.loader.loadable(AOD_PREVIEW_PH):
                                add AOD_PREVIEW_PH fit "contain" xalign 0.5 yalign 0.5
                            else:
                                text _("Sin imagen") color AOD_COL_MUTED size AOD_SIZE_SMALL xalign 0.5 yalign 0.5

                        $ _meta = (aod_get_slot_meta(_cur) if (not AOD_LS_MOCK and FileLoadable(_cur)) else {})
                        $ _chapter  = _meta.get("chapter", _("Capítulo pendiente"))
                        $ _location = _meta.get("location", "—")
                        $ _speaker  = _meta.get("speaker", "")
                        $ _quote    = _meta.get("quote", "—")
                        $ _playtime = _meta.get("playtime", "—")
                        $ _mode_txt = _meta.get("mode", "—")

                        text _chapter  color AOD_COL_ACCENT size AOD_SIZE_TEXT
                        text _location color AOD_COL_TEXT   size AOD_SIZE_SMALL
                        if _speaker:
                            text (_speaker + ": " + _quote) color AOD_COL_TEXT size AOD_SIZE_INFO italic True
                        else:
                            text _quote color AOD_COL_TEXT size AOD_SIZE_INFO italic True

                        hbox:
                            spacing AOD_SPACING_VBOX
                            frame:
                                background AOD_VALUE_BG
                                padding (AOD_INNER_PAD, int(round(6 * _AOD_SCALE)))
                                text _("Tiempo: {t}").format(t=_playtime) color AOD_COL_TEXT size AOD_SIZE_INFO
                            frame:
                                background AOD_VALUE_BG
                                padding (AOD_INNER_PAD, int(round(6 * _AOD_SCALE)))
                                text _("Modo: {m}").format(m=_mode_txt) color AOD_COL_TEXT size AOD_SIZE_INFO

                        $ _sel = aod_ls_sel
                        $ _has_data_sel = (not AOD_LS_MOCK and FileLoadable(_sel))
                        $ _in_main = main_menu

                        $ _cta_label = (
                            _("Cargar") if mode=="load" else
                            (_("Sobrescribir") if _has_data_sel else _("Guardar"))
                        )
                        if mode == "load":
                            $ _cta_action = (FileLoad(_sel) if _has_data_sel else Function(renpy.notify, _("No hay partida en este slot")))
                        else:
                            if _in_main:
                                $ _cta_action = Function(renpy.notify, _("No puedes guardar desde el menú principal"))
                            elif _has_data_sel:
                                $ _cta_action = Confirm(_("¿Sobrescribir este slot?"), yes=FileSave(_sel))
                            else:
                                $ _cta_action = FileSave(_sel)

                        frame:
                            background None
                            xfill True
                            padding (AOD_INNER_PAD, 0, AOD_INNER_PAD, 0)
                            textbutton _cta_label:
                                style "aod_cta_button"
                                text_style "aod_cta_text"
                                xfill True
                                xalign 0.5
                                yalign 0.5
                                action _cta_action

                        if mode == "save" and _has_data_sel:
                            null height AOD_SPACING_VBOX
                            textbutton _("Cargar este slot"):
                                style "aod_cta_button"
                                text_style "aod_cta_text"
                                xfill True
                                action FileLoad(_sel)

            # ===== FOOTER (ESTANDARIZADO) =====
            $ _can_load_here = (mode == "save" and FileLoadable(aod_ls_sel))
            $ _is_pad = (aod_input_mode == "pad")
            $ _show_toggle = not (mode == "load" and main_menu)

            $ _keyboard_items = (
                ([(_("Cambiar modo"), AOD_CAP_TAB)] if _show_toggle else []) +
                (
                    [
                        (_("Mover"), AOD_CAP_UD),
                        (_("Confirmar"), AOD_CAP_ENT),
                        (_("Volver"), "Esc / MB2"),
                    ] if mode == "load" else
                    [
                        (_("Mover"), AOD_CAP_UD),
                        (_("Confirmar"), AOD_CAP_ENT),
                        (_("Cargar este slot"), "L"),
                        (_("Volver"), "Esc / MB2"),
                    ]
                )
            )

            $ _pad_items = (
                ([(_("Cambiar modo"), "LB/RB")] if _show_toggle else []) +
                (
                    [
                        (_("Mover"), "D-Pad"),
                        (_("Confirmar"), "A"),
                        (_("Volver"), "B"),
                    ] if mode == "load" else
                    [
                        (_("Mover"), "D-Pad"),
                        (_("Confirmar"), "A"),
                        (_("Cargar este slot"), "X"),
                        (_("Volver"), "B"),
                    ]
                )
            )

            $ _footer_items = (_pad_items if _is_pad else _keyboard_items)
            $ _footer_items = [it for it in _footer_items if (it[0] != _("Cargar este slot")) or _can_load_here]

            frame:
                background None
                yminimum AOD_FOOTER_H
                xfill True

                fixed:
                    xfill True yfill True

                    hbox:
                        xpos 1.0
                        xanchor 1.0
                        yalign 0.5
                        spacing AOD_SPACING_FOOT

                        for _label, _cap in _footer_items:
                            hbox:
                                spacing AOD_SPACING_VBOX
                                yalign 0.5
                                frame:
                                    style "aod_keycap"
                                    text _cap color AOD_COL_TEXT size (AOD_SIZE_INFO - 2) xalign 0.5 yalign 0.5
                                text _label style "aod_foot_label" yalign 0.5

    python:
        def _ls_move(adj, vp_h, delta):
            store.aod_ls_sel = max(1, min(AOD_SLOTS_TOTAL, store.aod_ls_sel + delta))
            store.aod_ls_preview = store.aod_ls_sel
            aod_ls_ensure_visible(adj, store.aod_ls_sel, vp_h)

        def _ls_page(adj, vp_h, delta_pages):
            per_page = max(1, int(vp_h / ls_block_height()))
            _ls_move(adj, vp_h, delta_pages * per_page)

    key "K_UP"       action Function(_ls_move, _adj, _vp_h, -1)
    key "K_DOWN"     action Function(_ls_move, _adj, _vp_h,  1)
    key "K_PAGEUP"   action Function(_ls_page, _adj, _vp_h, -1)
    key "K_PAGEDOWN" action Function(_ls_page, _adj, _vp_h,  1)
    key "pad_dpup"   action Function(_ls_move, _adj, _vp_h, -1)
    key "pad_dpdown" action Function(_ls_move, _adj, _vp_h,  1)

    key "K_TAB" action [
        Function(aod_set_input_mode, "kb"),
        If(mode=="load" and main_menu,
            Function(renpy.notify, _("No puedes guardar sin iniciar partida")),
            (ShowMenu("save") if mode=="load" else ShowMenu("load"))
        )
    ]
    key "pad_leftshoulder"  action [
        Function(aod_set_input_mode, "pad"),
        If(mode=="load" and main_menu,
            Function(renpy.notify, _("No puedes guardar sin iniciar partida")),
            (ShowMenu("save") if mode=="load" else ShowMenu("load"))
        )
    ]
    key "pad_rightshoulder" action [
        Function(aod_set_input_mode, "pad"),
        If(mode=="load" and main_menu,
            Function(renpy.notify, _("No puedes guardar sin iniciar partida")),
            (ShowMenu("save") if mode=="load" else ShowMenu("load"))
        )
    ]

    key "K_l"   action ( FileLoad(aod_ls_sel) if (mode=="save" and FileLoadable(aod_ls_sel)) else NullAction() )
    key "pad_x" action ( FileLoad(aod_ls_sel) if (mode=="save" and FileLoadable(aod_ls_sel)) else NullAction() )

    key "K_RETURN"    action _cta_action
    key "K_KP_ENTER"  action _cta_action
    key "pad_a"       action _cta_action

    key "K_ESCAPE"  action Return()
    key "mouseup_3" action Return()
    key "pad_b"     action Return()

    if AOD_ENABLE_PYGAME_TAB:
        timer 0.05 repeat True action Function(_poll_tab_and_toggle, ("save" if mode=="load" else "load"))

screen load():
    tag menu
    modal True
    use aod_loadsave("load")

screen save():
    tag menu
    modal True
    use aod_loadsave("save")