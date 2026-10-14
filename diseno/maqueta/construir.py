#!/usr/bin/env python3
"""Construye la maqueta HTML (index.html) con los datos reales y los retratos incrustados."""
import base64, json, os, yaml
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
M = os.path.join(R, "diseno", "maqueta")
D = os.path.join(R, "proyecto", "datos")
per = yaml.safe_load(open(os.path.join(D, "personajes.yaml"), encoding="utf-8"))
fich = yaml.safe_load(open(os.path.join(D, "textos", "fichas.yaml"), encoding="utf-8"))["fichas"]
sem = yaml.safe_load(open(os.path.join(D, "semanas", "semana1.yaml"), encoding="utf-8"))
lug = {l["id"]: l["nombre"]["es"] for l in yaml.safe_load(open(os.path.join(D, "lugares.yaml"), encoding="utf-8"))["lugares"]}
REG = {"cualquiera": "Abierta a cualquiera", "dama_caballero": "Una dama y un caballero"}
pers = {}
for p in per["elenco"]:
    f = fich[p["id"]]
    pers[p["id"]] = dict(id=p["id"], pila=p["pila"], nombre=p["nombre"]["es"], genero=p["genero"], edad=p["edad"],
                         habilidades=p["habilidades"], linea=p["linea"]["es"], casa=per["casas"][p["casa"]]["es"],
                         bio=f["biografia"]["es"], entradas=[e["texto"]["es"] for e in f["entradas"]])
evs = []
for e in sem["eventos"]:
    evs.append(dict(id=e["id"], tipo=e["tipo"], lugar=e["lugar"], lugarN={"palacio": "Palacio", "academia": "Academia"}.get(e["lugar"], lug[e["lugar"]]),
                    dia=e["dia"], plazas=e["plazas"], regla=e["regla"], reglaN=REG[e["regla"]], obligatorio=e["obligatorio"],
                    requisito=e.get("requisito"), titulo=e["titulo"]["es"], anfitrion=e["anfitrion"]["es"], resumen=e["resumen"]["es"],
                    a_favor=[x["es"] for x in e.get("a_favor", [])], en_contra=[x["es"] for x in e.get("en_contra", [])],
                    carta={k: e["carta"][k]["es"].strip() for k in ("saludo", "cuerpo", "firma")}))
datos = dict(elenco=list(pers.values()), pers=pers, eventos=evs)
img = {k: "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(M, f"{k}_carta.jpg"), "rb").read()).decode() for k in pers}
t = open(os.path.join(M, "plantilla.html"), encoding="utf-8").read()
t = t.replace("/*DATOS*/null", json.dumps(datos, ensure_ascii=False)).replace("/*IMAGENES*/null", json.dumps(img))
open(os.path.join(M, "index.html"), "w", encoding="utf-8").write(t)
print("index.html", len(t) // 1024, "KB")
