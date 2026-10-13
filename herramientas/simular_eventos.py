#!/usr/bin/env python3
"""Simula los desenlaces de cada evento de una semana con todas las combinaciones válidas de asistentes
(sistemas §3), eligiendo en el incidente la mejor opción y la peor. Sirve para ajustar la dificultad.
Uso: python herramientas/simular_eventos.py [semana]   (por defecto 1)"""
import itertools, os, sys, yaml
from collections import Counter
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(R, "proyecto", "datos")
per = {p["id"]: p for p in yaml.safe_load(open(os.path.join(D, "personajes.yaml")))["elenco"]}
sem = sys.argv[1] if len(sys.argv) > 1 else "1"
datos = yaml.safe_load(open(os.path.join(D, "semanas", f"semana{sem}.yaml")))

def grupo(ids, h):
    vals = sorted((per[i]["habilidades"][h] for i in ids), reverse=True)
    return min(5, vals[0] + (1 if any(v >= 3 for v in vals[1:]) else 0))

def valido(ev, ids):
    g = [per[i]["genero"] for i in ids]
    r = ev["regla"]
    return (r == "cualquiera" or (r == "dama_caballero" and sorted(g) == ["f", "m"])
            or (r == "solo_damas" and set(g) == {"f"}) or (r == "solo_caballeros" and set(g) == {"m"}))

def resolver(ev, ids, mejor=True):
    req = ev["requisito"]
    cob = sum(min(grupo(ids, h), v) for h, v in req.items()) / sum(req.values())
    base = 1 if cob >= 1 else 0 if cob >= .8 else -1 if cob >= .6 else -2
    an = sum((1 if per[i]["gusta"] == ev["tipo"] else 0) - (1 if per[i]["no_gusta"] == ev["tipo"] else 0) for i in ids) / len(ids)
    an = int(an) if abs(an) >= 1 else 0
    inc = 0
    if ev.get("incidente"):
        res = []
        for o in ev["incidente"]["opciones"]:
            v = grupo(ids, o["habilidad"])
            res.append(1 if v >= o["d"] else 0 if v == o["d"] - 1 else -1)
        inc = max(res) if mejor else min(res)
    t = base + an + inc
    return "favorable" if t >= 1 else "medias" if t >= -1 else "desaire"

for ev in datos["eventos"]:
    if "requisito" not in ev:
        continue
    for modo in (True, False):
        c = Counter()
        for n in range(ev["plazas"]["min"], ev["plazas"]["max"] + 1):
            for ids in itertools.combinations(per, n):
                if valido(ev, ids):
                    c[resolver(ev, ids, modo)] += 1
        tot = sum(c.values())
        if not tot:
            continue
        print(f"{ev['id']:14} {'mejor' if modo else 'peor ':5} opción · {tot:3} combinaciones · " +
              " · ".join(f"{k} {100*c[k]//tot}%" for k in ("favorable", "medias", "desaire")))
