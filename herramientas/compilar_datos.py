#!/usr/bin/env python3
"""Valida los datos de Salverna, los exporta a JSON y genera el guion legible.

Uso:
  python herramientas/compilar_datos.py            # valida, exporta y genera el guion
  python herramientas/compilar_datos.py --solo-validar

Comprueba:
  - Cada texto {es, en} tiene las dos lenguas y no está vacío.
  - Las variables ({a}, {grupo}, {a|o|a}…) coinciden entre es y en.
  - El español no usa «vos» ni «vosotros».
  - Los lugares, personajes y eventos citados existen.
Salidas: proyecto/datos/json/*.json y proyecto/guion/*.md
Requisitos: Python 3 y PyYAML (pip install pyyaml).
"""
import json
import os
import re
import sys

import yaml

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RAIZ, "proyecto", "datos")
SALIDA_JSON = os.path.join(DATOS, "json")
SALIDA_GUION = os.path.join(RAIZ, "proyecto", "guion")

PROHIBIDAS_ES = re.compile(
    r"\b(vosotros|vosotras|vuestr[oa]s?|os|sois|habéis|tenéis|dejadme|déjadme|dejádmelo|venid|mirad|escuchad)\b",
    re.IGNORECASE,
)
VARIABLE = re.compile(r"\{([a-z_]+)(\|[^{}]*)?\}")
FUNCIONES = {"asiste", "asistio", "desenlace", "opcion", "cercania", "nivel", "nivel_max", "rep",
             "marca", "semana", "estado", "gusta", "no_gusta", "asistio_gusta", "desaires", "chispa"}

errores = []
avisos = []


def cargar(ruta):
    with open(ruta, encoding="utf-8") as f:
        return yaml.safe_load(f)


def archivos_yaml():
    for base, _, nombres in os.walk(DATOS):
        if base.startswith(SALIDA_JSON):
            continue
        for n in sorted(nombres):
            if n.endswith((".yaml", ".yml")):
                yield os.path.join(base, n)


def variables(texto):
    """Variables que deben aparecer en las dos lenguas. Las de concordancia ({a|o|a})
    pueden faltar en inglés, que casi nunca necesita género."""
    return sorted({m.group(1) for m in VARIABLE.finditer(texto or "") if not m.group(2)})


def recorrer(nodo, ruta, archivo, ids):
    if isinstance(nodo, dict):
        if "es" in nodo or "en" in nodo:
            es, en = nodo.get("es"), nodo.get("en")
            if not isinstance(es, str) or not es.strip():
                errores.append(f"{archivo}: {ruta}: falta el español")
            if not isinstance(en, str) or not en.strip():
                errores.append(f"{archivo}: {ruta}: falta el inglés")
            if isinstance(es, str) and isinstance(en, str):
                if variables(es) != variables(en):
                    errores.append(f"{archivo}: {ruta}: variables distintas es={variables(es)} en={variables(en)}")
                m = PROHIBIDAS_ES.search(es)
                if m:
                    errores.append(f"{archivo}: {ruta}: forma de «vosotros» prohibida: «{m.group(0)}»")
        for k, v in nodo.items():
            if k in ("si", "desbloqueo") and isinstance(v, str):
                revisar_condicion(v, f"{ruta}.{k}", archivo, ids)
            if k == "lugar" and isinstance(v, str) and v not in ids["lugares"]:
                errores.append(f"{archivo}: {ruta}: lugar desconocido «{v}»")
            recorrer(v, f"{ruta}.{k}", archivo, ids)
    elif isinstance(nodo, list):
        for i, v in enumerate(nodo):
            recorrer(v, f"{ruta}[{i}]", archivo, ids)


def revisar_condicion(cond, ruta, archivo, ids):
    for nombre, args in re.findall(r"([a-z_]+)\(([^)]*)\)", cond):
        if nombre not in FUNCIONES:
            avisos.append(f"{archivo}: {ruta}: función de condición no documentada «{nombre}»")
        if nombre in ("marca", "rep", "semana"):
            continue
        for a in [x.strip() for x in args.split(",") if x.strip()]:
            if a == "*" or a.isdigit():
                continue
            if a not in ids["personas"] and a not in ids["eventos"]:
                errores.append(f"{archivo}: {ruta}: identificador desconocido «{a}» en «{cond}»")


def guion_semana(datos, lengua):
    t = lambda x: (x or {}).get(lengua, "") if isinstance(x, dict) else ""
    s = datos["semana"]
    out = [f"# Semana {s['numero']} · {t(s['nombre'])}", "", f"**{t(s['hecho_del_reino']['titulo'])}.** {t(s['hecho_del_reino']['texto'])}", ""]
    ap = datos.get("apertura")
    if ap:
        out += ["## Apertura", ""] + [f"- **{l.get('habla') or 'narración'}**: {t(l)}" for l in ap.get("lineas", [])]
        for r in ap.get("recuerdos", []):
            out.append(f"- si `{r['si']}`: {t(r['texto'])}")
        for d in ap.get("decision", []):
            out.append(f"- Opción **{t(d['texto'])}** → {t(d.get('resultado'))}")
        out.append("")
    if datos.get("peticiones"):
        out += ["## Peticiones", ""]
        for pe in datos["peticiones"]:
            out += [f"- **{pe['personaje']}** pide " + (f"no ir a nada el día {pe['dia']}" if pe.get("tipo") == "no_asistir" else f"`{pe['evento']}`") + f": {t(pe['texto'])}",
                    f"  - Si se cumple: {t(pe['si_cumple'])}", f"  - Si no: {t(pe['si_no'])}"]
        out.append("")
    for ev in datos["eventos"]:
        out += [f"## {t(ev['titulo'])} · día {ev['dia']} · {ev['lugar']}",
                f"*{ev['tipo']} · plazas {ev['plazas']['min']}–{ev['plazas']['max']} · {ev['regla']}"
                f"{' · OBLIGATORIO' if ev.get('obligatorio') else ''}*", "",
                f"> {t(ev['resumen'])}", ""]
        if "requisito" in ev:
            out.append("Requisito: " + ", ".join(f"{k} {v}" for k, v in ev["requisito"].items()))
        for x in ev.get("a_favor", []):
            out.append(f"- \\+ {t(x)}")
        for x in ev.get("en_contra", []):
            out.append(f"- − {t(x)}")
        c = ev.get("carta")
        if c:
            out += ["", "**Carta**", "", f"*{t(c['saludo'])}*", "", t(c["cuerpo"]).strip(), "", f"*{t(c['firma'])}*"]
        inc = ev.get("incidente")
        if inc:
            out += ["", f"**Incidente (día {inc['dia']})** · {t(inc['situacion'])}", ""]
            for o in inc["opciones"]:
                out += [f"- **{t(o['texto'])}** ({o['habilidad']}, d {o['d']})",
                        f"  - Éxito: {t(o['exito'])}", f"  - A medias: {t(o['medias'])}", f"  - Fallo: {t(o['fallo'])}"]
        ir = ev.get("incidente_riesgo")
        if ir:
            out += ["", f"**Incidente de riesgo (si `{ir['si']}`, sustituye al anterior)** · {t(ir['situacion'])}", ""]
            for o in ir["opciones"]:
                out += [f"- **{t(o['texto'])}** ({o['habilidad']}, d {o['d']})",
                        f"  - Éxito: {t(o['exito'])}", f"  - A medias: {t(o['medias'])}", f"  - Fallo: {t(o['fallo'])}"]
        ind = ev.get("indisposicion")
        if ind:
            out += ["", f"**Indisposición (días {ind['dias']})** · {ind['quien']}: {t(ind['aviso'])}"]
        rz = ev.get("reemplazo")
        if rz:
            out += ["", f"**Reemplazo en `{rz['evento']}`** · {t(rz['texto'])}"]
            out += [f"- {t(v)}" for v in rz["opciones"].values()]
            for k in ("resultado_reducir", "resultado_retirar"):
                if k in rz:
                    out.append(f"- {k}: {t(rz[k])}")
        for nombre, d in (ev.get("desenlaces") or {}).items():
            out += ["", f"**Desenlace · {nombre}**" + (f" — {t(d.get('titulo'))}" if d.get("titulo") else "")]
            for clave in ("publico", "privado"):
                if clave in d:
                    out.append(f"- {clave}: {t(d[clave])}")
                    for v in d[clave].get("variantes", []):
                        out.append(f"  - si `{v['si']}`: {t(v['texto'])}")
        if "completada" in ev:
            out += ["", "**Al completarse**"]
            for clave in ("publico", "privado"):
                d = ev["completada"][clave]
                out.append(f"- {clave}: {t(d)}")
                for v in d.get("variantes", []):
                    out.append(f"  - si `{v['si']}`: {t(v['texto'])}")
        out.append("")
    if "cierre" not in datos:
        return "\n".join(out + ["*(Cierre pendiente: se escribe en la parte 2.)*", ""])
    cr = datos["cierre"]["cronica"]
    out += [f"## {t(cr['cabecera'])} · {t(cr['subtitulo'])}", "", f"*{t(cr['entradilla'])}*", ""]
    for n in cr["noticias"]:
        out.append(f"- **{t(n['titular'])}**" + (f": {t(n.get('texto'))}" if n.get("texto") else " (texto del desenlace)"))
    out += ["", f"*{t(cr['pie'])}*", ""]
    h = datos["cierre"].get("hoja")
    if h:
        out += [f"## {t(h['cabecera'])} · nº {h['numero']}", "", f"*{t(h['entradilla'])}*", ""]
        if "secreto_por_protagonista" in h:
            out.append("Secreto según quién tenga más fama:")
            out += [f"- **{k}**: {t(v)}" for k, v in h["secreto_por_protagonista"].items()]
        if "cuerpo" in h:
            out.append(t(h["cuerpo"]))
            out += [f"- si `{v['si']}`: {t(v['texto'])}" for v in h["cuerpo"].get("variantes", [])]
        out += ["", f"*{t(h['pie'])}*", ""]
    out += ["## Sólo para sus ojos", ""]
    for o in datos["cierre"]["solo_sus_ojos"]["observaciones"]:
        out.append(f"- si `{o['si']}`: {t(o['texto'])}")
    gancho = datos["cierre"]["gancho"]
    if "sobre" in gancho:
        g = gancho["sobre"]
        out += ["", "## El sobre sin firma", "", f"*{t(g['saludo'])}*", "", t(g["cuerpo"]).strip(), "",
                f"> {t(gancho['nota_final'])}", ""]
    else:
        out += ["", "## Gancho", ""] + [f"- **{l.get('habla') or 'narración'}**: {t(l)}" for l in gancho.get("lineas", [])] + [""]
    return "\n".join(out)


def guion_escenas(datos, lengua, titulo):
    t = lambda x: (x or {}).get(lengua, "") if isinstance(x, dict) else ""
    out = [f"# {titulo}", ""]
    for e in datos["escenas"]:
        out += [f"## {' y '.join(e['pareja'])} · {t(e['ambiente'])}", f"*{e['id']} · nivel {e['nivel']}*", ""]
        for l in e["lineas"]:
            quien = l.get("habla") or "narración"
            out.append(f"- **{quien}**" + (f" ({l['expr']})" if l.get("expr") else "")
                       + (f" [si `{l['si']}`]" if l.get("si") else "") + f": {t(l)}")
        out += ["", f"> {t(e.get('apunte'))}", ""]
    return "\n".join(out)


def guion_tutorial(datos, lengua):
    out = ["# Tutorial y apertura", ""]
    for p in datos["pasos"]:
        out.append(f"## {p['id']} · {p['pantalla']}")
        if p.get("resaltar"):
            out.append(f"*Resalta: {p['resaltar']}*")
        if p.get("descripcion"):
            out.append(f"*{p['descripcion'].strip()}*")
        for l in p.get("lineas", []):
            out.append(f"- **{l.get('habla') or 'narración'}**: {l.get(lengua, '')}")
        out.append("")
    return "\n".join(out)


def main():
    solo_validar = "--solo-validar" in sys.argv
    contenido = {os.path.relpath(r, DATOS): cargar(r) for r in archivos_yaml()}
    personajes = contenido.get("personajes.yaml", {})
    ids = {
        "personas": {p["id"] for p in personajes.get("elenco", [])} | {p["id"] for p in personajes.get("recurrentes", [])}
                    | {"a", "b", "c", "d"},  # plazas del evento actual
        "lugares": {l["id"] for l in contenido.get("lugares.yaml", {}).get("lugares", [])},
        "eventos": set(),
    }
    for nombre, d in contenido.items():
        if nombre.startswith("semanas"):
            ids["eventos"] |= {e["id"] for e in d.get("eventos", [])}
    for nombre, d in contenido.items():
        recorrer(d, "", nombre, ids)

    for a in avisos:
        print("AVISO:", a)
    for e in errores:
        print("ERROR:", e)
    print(f"{len(contenido)} archivos · {len(errores)} errores · {len(avisos)} avisos")
    if errores:
        sys.exit(1)
    if solo_validar:
        return

    os.makedirs(SALIDA_JSON, exist_ok=True)
    for nombre, d in contenido.items():
        destino = os.path.join(SALIDA_JSON, nombre.replace(os.sep, "_").rsplit(".", 1)[0] + ".json")
        with open(destino, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
    os.makedirs(SALIDA_GUION, exist_ok=True)
    for lengua in ("es", "en"):
        for nombre, d in contenido.items():
            if nombre.startswith("semanas"):
                base = os.path.basename(nombre).rsplit(".", 1)[0]
                texto = guion_semana(d, lengua)
            elif nombre.endswith("tutorial.yaml"):
                base, texto = "tutorial", guion_tutorial(d, lengua)
            elif nombre.startswith("escenas"):
                base = os.path.basename(nombre).rsplit(".", 1)[0]
                texto = guion_escenas(d, lengua, "Escenas de vínculo · " + base.split("_")[-1])
            else:
                continue
            with open(os.path.join(SALIDA_GUION, f"{base}.{lengua}.md"), "w", encoding="utf-8") as f:
                f.write(texto)
    print("JSON en", os.path.relpath(SALIDA_JSON, RAIZ), "· guion en", os.path.relpath(SALIDA_GUION, RAIZ))


if __name__ == "__main__":
    main()
