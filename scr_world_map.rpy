# game/src/screens/scr_world_map.rpy

screen aod_world_map():
    # Fondo del mapa: sólido gris si no hay imagen
    add Solid("#1a1a1a")

    # Encabezado de estado
    frame:
        xalign 0.02
        yalign 0.05
        has vbox
        text "Mapa nocturno" size 30
        text "Acciones: [aod_actions_left]   Tensión: [aod_tension]/6"
        text "Nodo actual: [aod_current_node]"

    # Botones grandes (MVP). Luego los reemplazamos por hotspots/coords.
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 12
        textbutton "[map_label('NODE_HOME')]" action Function(aod_set_node, "NODE_HOME")
        textbutton "[map_label('NODE_ALLEY')]" action Function(map_travel, "NODE_ALLEY")
        textbutton "[map_label('NODE_CLUB')]"  action Function(map_travel, "NODE_CLUB")

    # Footer
    frame:
        xalign 0.98
        yalign 0.95
        has hbox
        textbutton "Volver a la habitación" action Jump("aod_room_night")

label aod_open_map:
    call screen aod_world_map
    return
