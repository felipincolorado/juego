# game/src/screens/scr_room_night.rpy

screen aod_room_night():
    # Fondo: si no tienes imagen, usamos un color sólido
    add Solid("#0f0f1a")

    frame:
        xalign 0.02
        yalign 0.05
        has vbox
        text "Noche {aod_day}" size 28
        text "Acciones restantes: [aod_actions_left]"
        text "Tensión: [aod_tension]/6"
        text "Ubicación: [aod_current_node]"

    frame:
        xalign 0.98
        yalign 0.90
        has hbox
        textbutton "Dormir" action Jump("aod_end_night")
        textbutton "Menú"   action ShowMenu("preferences")
        textbutton "Explorar" action Jump("aod_open_map")

label aod_room_night:
    call screen aod_room_night
    return
