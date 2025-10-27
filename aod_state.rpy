# game/src/core/aod_state.rpy

# --------- DEFAULTS (estado de la partida) ----------
default aod_day            = 0
default aod_actions_left   = 2          # 2 macro-acciones por noche (ajustable)
default aod_tension        = 0          # 0-6 reloj de riesgo nocturno
default aod_notoriety      = 0          # 0-100 memoria de riesgo
default aod_current_node   = "NODE_HOME"

# Stats ocultos 0-5
default aod_stats = {
    "alchemy": 0,
    "cunning": 0,
    "grit":    0
}

# Afinidades 0-100 (ocultas); usamos umbrales 20/40/60/80 para floración
default aod_affinity = {
    "bridia": 0,
    "rugora_spinara": 0
}

# Pruebas / Hechos (IDs normalizados tipo FACT_VERUM_347)
default aod_facts = set()

# --------- UTILIDADES SENCILLAS ----------
init python:
    import json

    def aod_gain_affinity(char_id, amount):
        if char_id not in store.aod_affinity: return
        store.aod_affinity[char_id] = max(0, min(100, store.aod_affinity[char_id] + int(amount)))
        renpy.notify(f"Afinidad ({char_id}) {'+' if amount>=0 else ''}{amount}")

    def aod_add_fact(fact_id):
        store.aod_facts.add(fact_id)
        renpy.notify(f"Nuevo hecho: {fact_id}")

    def aod_has_fact(fact_id):
        return fact_id in store.aod_facts

    def aod_set_node(node_id):
        store.aod_current_node = node_id

    def aod_inc_tension(delta=1):
        store.aod_tension = max(0, min(6, store.aod_tension + int(delta)))

    def aod_reset_night():
        store.aod_actions_left = 2
        store.aod_tension      = 0
        # Notoriedad puede bajar un poquito noche a noche si quieres:
        store.aod_notoriety    = max(0, store.aod_notoriety - 2)
        store.aod_current_node = "NODE_HOME"

label aod_start_night:
    $ aod_reset_night()
    $ aod_day += 1
    # Aquí podrías hacer un autoguardado si quieres:
    # $ renpy.save("auto_noche")
    jump aod_room_night

label aod_end_night:
    # Efectos de cierre de noche (bajada de tensión, etc. ya lo hace reset)
    "Cierras los ojos. El murmullo de Basaltia se apaga."
    jump aod_start_night
