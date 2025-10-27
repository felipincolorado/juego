## src/core/definitions.rpy
##
## Definiciones centrales del juego: Personajes y Variables Globales.
##

# --- Personajes ---
# El color es un código hexadecimal. Elige uno que se ajuste a tu paleta.
define e = Character("Elara", color="#d2b48c")
define p = Character("Protagonista", color="#a0a0a0")
define protagonista = Character("Protagonista", color="#a0a0a0")

# --- Variables Globales ---
# Usamos 'default' para que las variables se inicialicen al empezar una nueva partida
# o se restablezcan si no existen en una partida cargada.
default player_trust_elara = 0
default player_alchemy_skill = 1

# --- Configuración Inicial (init python block) ---
init python:
    # Aquí irán configuraciones avanzadas de Python en el futuro.
    # Por ahora, lo dejamos limpio.
    pass