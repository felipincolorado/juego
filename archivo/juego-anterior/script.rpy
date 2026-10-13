## src/core/script.rpy
##
## Punto de entrada principal del juego.
##

label start:
    # Opción A: muerte → tribunal (más cinematográfico)
    jump prologo_muerte

    # Opción B: entrar directo al juicio
    # jump prologo_tribunal
