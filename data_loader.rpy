## src/systems/data_loader.rpy
##
## Sistema para cargar datos desde archivos JSON externos.
##

init python:
    import json

    def load_judgment_data(judgment_id):
        """
        Carga los datos de un juicio desde un archivo JSON.
        Devuelve un diccionario o None si hay un error.
        """
        file_path = "data/judgments/judgment_{}.json".format(judgment_id)
        try:
            # Usamos renpy.file para que Ren'Py encuentre el archivo dentro del compilado
            with renpy.file(file_path) as f:
                return json.load(f)
        except Exception as e:
            renpy.log_error("Error cargando el archivo de juicio {}: {}".format(file_path, e))
            return None