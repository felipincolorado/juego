## src/systems/judgment_system.rpy
##
## El sistema central de juicios "Duelo de Espejos".
##

init python:
    class Judgment:
        """
        Gestiona el estado y la lógica de un juicio individual.
        """
        def __init__(self, data):
            self.judgment_id = data["id"]
            self.judge_name = data["judge_name"]
            self.initial_data = data
            self.verdict_bar = data.get("initial_verdict", 0)
            self.judge_mood = data.get("judge_mood_modifier", 0)
            self.current_phase = 0
            self.is_over = False

        def apply_dialogue_result(self, value):
            """Aplica un cambio a la barra de veredicto."""
            self.verdict_bar += value
            self.check_end_conditions()

        def check_end_conditions(self):
            """Comprueba si el juicio ha terminado."""
            if self.verdict_bar >= 100 or self.verdict_bar <= -100:
                self.is_over = True

        # --- Métodos para el sistema de guardado/carga ---
        def __getstate__(self):
            """Define qué datos guardar cuando el juego se guarda."""
            return {
                'judgment_id': self.judgment_id,
                'verdict_bar': self.verdict_bar,
                'judge_mood': self.judge_mood,
                'current_phase': self.current_phase,
                'is_over': self.is_over
            }

        def __setstate__(self, state):
            """Restaura el estado de la clase cuando el juego se carga."""
            # Recargamos los datos base desde el JSON
            base_data = load_judgment_data(state['judgment_id'])
            self.__init__(base_data)
            # Restauramos el estado dinámico
            self.verdict_bar = state['verdict_bar']
            self.judge_mood = state['judge_mood']
            self.current_phase = state['current_phase']
            self.is_over = state['is_over']