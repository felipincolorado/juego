## =============================================================================
## THE GILDED CAGE - CONFIGURACIÓN GLOBAL
## Ubicación: game/src/core/config.rpy
## =============================================================================

# -------- PALETA DE COLORES (prioridad máxima) --------
init -100 python:
    # Colores principales del juego
    TGC_PRIMARY    = "#FFFFFF"  # Blanco para texto
    TGC_ACCENT     = "#F2F6FF"
    TGC_GOLD       = "#c9a86a"
    TGC_GOLD_LIGHT = "#d4af37"
    TGC_CRIMSON    = "#8b0000"
    TGC_ROSE_BLUE  = "#6B8EC9"
    TGC_OUTLINE    = "#0a0f1a"
    
    # Texto
    TGC_TEXT_CPS   = 40  # Velocidad de typewriter

# -------- VARIABLES GLOBALES DEL JUEGO --------
# Nombre del jugador
default player_name = "Aleric"

# Sistema de confianza
default bridia_trust = 0
default rose_affinity = 0
default chose_correct_response = False

# Flags de historia
default protagonist_died = True
default player_is_reincarnation = True
default bridia_failures_count = 2
default sabotage_detected = False
default church_threat_level = 80
default rose_color_system = True
default bridia_rose_color = "azul"

# Exploración nocturna
default night_0_escaped = False
default night_1_escaped = False
default night_2_escaped = False
default night_3_escaped = False

# Rugosa (Guardia)
default rugosa_met = False
default rugosa_trust = 0
default rugosa_seeds_given = 0
default seeds_inventory = 0

# Achievements
init -99 python:
    if not hasattr(persistent, "achievements"):
        persistent.achievements = {}

# -------- CONFIGURACIÓN DE REN'PY --------
init -98 python:
    # Velocidad de texto
    config.default_text_cps = 40
    
    # NO MODIFICAR config.replace_text (causa errores)
    # NO MODIFICAR config.custom_text_tags (causa errores)
