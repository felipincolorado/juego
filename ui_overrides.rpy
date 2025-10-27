## =============================================================================
## THE GILDED CAGE — Diálogo FE-style + Barra de Controles | Ren'Py 8.4.x
## Archivo: game/src/screens/ui_overrides.rpy
## Mantiene id "what". Incluye detección simple de entrada (kb/pad).
## =============================================================================

# ------------------ PALETA / HELPERS -----------------------------------------
init -30 python:
    AOD_COL_BG     = "#0f1218"
    AOD_COL_PANEL  = "#121723"
    AOD_COL_ACCENT = "#c9a86a"
    AOD_COL_TEXT   = "#f2f2f2"
    AOD_COL_MUTED  = "#a6adbb"

    def aod_rgba(hex_rgb, alpha=0.90):
        if len(hex_rgb) == 7:
            a = int(round(alpha * 255.0))
            return hex_rgb + "{:02x}".format(a)
        return hex_rgb

    # Fallbacks a sólidos (si no tienes 9-slice aún).
    AOD_PANEL_BG   = Solid(aod_rgba(AOD_COL_PANEL, 0.92))
    AOD_BAR_BG     = Solid(aod_rgba("#0e121a", 0.92))

# ------------------ ESTADO DE DISPOSITIVO ------------------------------------
# Heurística: guardamos el último input (kb/pad).

init -10 python:
    # Helper para mostrar etiquetas distintas según dispositivo
    def aod_hint(label, kb, pad):
        from renpy.store import aod_input_mode
        return f"{label}: {pad if aod_input_mode == 'pad' else kb}"

# ------------------ SAY (ventana de diálogo) ---------------------------------
screen say(who, what):
    style_prefix "say"

    # Ventana centrada, con márgenes laterales (a lo FE).
    window:
        id "window"
        background AOD_PANEL_BG
        xalign 0.5
        yalign 0.86
        xmaximum 1680
        xminimum 1480
        yminimum 220
        padding (36, 28)

        # Nameplate sobrio arriba-izq (no gigante; puede sobresalir levemente)
        if who is not None:
            frame:
                background Solid(aod_rgba("#181e2a", 0.94))
                padding (14, 8)
                xminimum 300
                yminimum 42
                xpos 6
                ypos 6
                text who style "say_label"

        # Texto principal (centrado dentro del rectángulo)
        text what id "what" style "say_dialogue" xalign 0.5

    # Barra de controles inferior (siempre visible en diálogo)
    use aod_control_bar

# ------------------ BARRA INFERIOR DE CONTROLES ------------------------------
screen aod_control_bar():
    zorder 200

    # Captura de teclas para detectar último dispositivo
    # (Si tu gamepad usa otros nombres, igual no rompe; F1 alterna manual).
    key "K_SPACE"  action SetVariable("aod_input_mode", "kb")
    key "K_RETURN" action SetVariable("aod_input_mode", "kb")
    key "mouseup_1" action SetVariable("aod_input_mode", "kb")

    key "pad_a"     action SetVariable("aod_input_mode", "pad")
    key "pad_b"     action SetVariable("aod_input_mode", "pad")
    key "pad_start" action SetVariable("aod_input_mode", "pad")
    key "pad_x"     action SetVariable("aod_input_mode", "pad")

    # F1 = fallback manual si tu gamepad no emite eventos "pad_*"
    key "K_F1" action If(aod_input_mode == "kb",
                         SetVariable("aod_input_mode", "pad"),
                         SetVariable("aod_input_mode", "kb"))

    frame:
        background AOD_BAR_BG
        xalign 0.5
        yalign 0.98
        xfill True
        yminimum 48
        padding (18, 10)

        # Orden de derecha a izquierda (como en tu referencia)
        hbox:
            spacing 22
            xalign 1.0

            # Ajustes / Preferencias
            textbutton aod_hint("Menu", "Esc", "Start") style "aod_hint_btn" action ShowMenu("preferences")

            # Log / Historial
            textbutton aod_hint("Log", "L", "Back") style "aod_hint_btn" action ShowMenu("history")

            # Auto-advance (toggle)
            textbutton aod_hint("Auto", "A", "X") style "aod_hint_btn" action Preference("auto-forward", "toggle")

            # Skip (toggle rápido)
            textbutton aod_hint("Skip", "Ctrl", "RB") style "aod_hint_btn" action Skip()

            # Avance (informativo; el “dismiss” es con Space/Enter o A)
            text aod_hint("Avanzar", "Enter / Space", "A") style "aod_hint_text"

# ------------------ ESTILOS ---------------------------------------------------
style say_window is default:
    background AOD_PANEL_BG

style say_label is default:
    color AOD_COL_ACCENT
    size 26
    bold True
    outlines [(2, "#000000")]

style say_dialogue is default:
    color AOD_COL_TEXT
    size 30
    line_spacing 2
    outlines [(1, "#000000")]

style aod_hint_btn is default:
    background None
    padding (6, 4)

style aod_hint_btn_text is default:
    color AOD_COL_MUTED
    hover_color AOD_COL_TEXT
    size 20
    outlines [(1, "#000000")]

style aod_hint_text is default:
    color AOD_COL_MUTED
    size 18
    outlines [(1, "#000000")]
