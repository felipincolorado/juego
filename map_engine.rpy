# game/src/systems/map_engine.rpy

init python:
    import json

    _AOD_GRAPH_CACHE = None
    _AOD_RULES_CACHE = None

    def map_load_graph():
        """
        Lee game/data/maps/city_graph.json y cachea nodos, edges y rules.
        """
        global _AOD_GRAPH_CACHE, _AOD_RULES_CACHE
        if _AOD_GRAPH_CACHE is not None:
            return _AOD_GRAPH_CACHE, _AOD_RULES_CACHE

        try:
            with renpy.file("data/maps/city_graph.json") as f:
                data = json.load(f)
        except Exception as e:
            renpy.notify(f"[Mapa] No se pudo leer city_graph.json: {e}")
            data = {"nodes": [], "edges": [], "rules": {}}

        # Construye adyacencias simples
        adj = {}
        labels = {}
        for n in data.get("nodes", []):
            nid = n["id"]
            labels[nid] = n.get("label", nid)
            adj[nid] = []

        for e in data.get("edges", []):
            a = e.get("from"); b = e.get("to")
            if a in adj and b in adj:
                adj[a].append(b)

        rules = data.get("rules", {})
        _AOD_GRAPH_CACHE = {"adj": adj, "labels": labels}
        _AOD_RULES_CACHE = rules
        return _AOD_GRAPH_CACHE, _AOD_RULES_CACHE

    def map_label(nid):
        graph, _ = map_load_graph()
        return graph["labels"].get(nid, nid)

    def map_can_reach_direct(src, dst):
        graph, _ = map_load_graph()
        return dst in graph["adj"].get(src, [])

    def map_build_route(src, dst):
        """
        Devuelve la ruta (lista de nodos) desde src a dst aplicando reglas.
        MVP: si vas al CLUB y no estás en ALLEY, forzamos pasar por ALLEY.
        """
        _, rules = map_load_graph()
        route = []

        # Si destino es CLUB y la regla dice que requiere ALLEY:
        prereq = (rules.get("prerequisites", {}).get("NODE_CLUB") or [])
        requires_alley = ("NODE_ALLEY" in prereq)

        current = src

        if dst == "NODE_CLUB" and requires_alley and current != "NODE_ALLEY":
            # Paso 1: llegar a ALLEY (si no estás ya)
            if map_can_reach_direct(current, "NODE_ALLEY"):
                route.append("NODE_ALLEY")
                current = "NODE_ALLEY"
            else:
                # Si en el futuro hay más nodos, aquí haríamos pathfinding.
                renpy.notify("No hay ruta directa a Callejón desde aquí.")
                return []

        # Paso 2: del current al dst
        if map_can_reach_direct(current, dst):
            route.append(dst)
        else:
            renpy.notify("No hay ruta directa al destino.")
            return []

        return route

    def map_travel(target_node):
        """
        Consume 1 acción, avanza por cada paso de la ruta, sube tensión por paso,
        y deja al jugador en el último nodo.
        """
        graph, rules = map_load_graph()
        if store.aod_actions_left <= 0:
            renpy.notify("No te quedan acciones esta noche.")
            return

        src = store.aod_current_node
        route = map_build_route(src, target_node)
        if not route:
            return

        tension_per_step = int(rules.get("costs", {}).get("tension_per_step", 1))

        # Recorre la ruta
        for step in route:
            aod_set_node(step)
            aod_inc_tension(tension_per_step)

        # Consume la acción
        store.aod_actions_left -= int(rules.get("costs", {}).get("default_action_cost", 1))

        renpy.notify("Ruta: " + " → ".join([map_label(n) for n in route]))
        renpy.restart_interaction()
