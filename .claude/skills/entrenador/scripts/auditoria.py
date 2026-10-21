#!/usr/bin/env python3
"""Audita cuántas series semanales recibe cada músculo en las rutinas HTML.

Uso:  python3 scripts/auditoria.py [carpeta_del_repo]
Lee rutina_*.html, cuenta series = rondas × ejercicios (de ".sub": "N rondas" / "N veces"),
las reparte por músculo según references/musculos.json y muestra:
  1) series por músculo y rutina,
  2) series por músculo y semana para cada combinación de la rotación.
Avisa de ejercicios sin mapear (hay que añadirlos al JSON).
"""
import json, re, sys, html
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = json.loads((HERE.parent / "references" / "musculos.json").read_text(encoding="utf-8"))
MAP.pop("_doc", None)
MUSCLES = ["pecho", "hombro_ant", "hombro_lat", "hombro_post", "triceps", "biceps", "dorsal",
           "espalda_alta", "lumbar", "cuadriceps", "gluteo", "isquios", "gemelos", "aductores",
           "antebrazo", "core", "oblicuos", "cardio"]
# Combinaciones semanales: un Push × un Pull × una full body (y la alternativa A+B+C)
import itertools
PUSH = ["rutina_push.html", "rutina_push_B.html"]
PULL = ["rutina_pull.html", "rutina_pull_B.html"]
FULL = ["rutina_A.html", "rutina_B.html", "rutina_C.html"]
WEEKS = {" + ".join(x.replace("rutina_", "").replace(".html", "") for x in c): list(c)
         for c in itertools.product(PUSH, PULL, FULL)}
WEEKS["A + B + C"] = FULL

def sections(text):
    for sec in re.findall(r"<section>(.*?)</section>", text, re.S):
        sub = re.search(r'<p class="sub">(.*?)</p>', sec, re.S)
        sub = html.unescape(re.sub(r"<[^>]+>", "", sub.group(1))) if sub else ""
        m = re.search(r"(\d+)\s+(?:rondas|veces)", sub)
        rounds = int(m.group(1)) if m else 0
        names = [html.unescape(n) for n in re.findall(r'<p class="nm">(.*?)</p>', sec)]
        yield rounds, names

def audit(path):
    text = path.read_text(encoding="utf-8")
    tot = {m: 0.0 for m in MUSCLES}
    missing = set()
    for rounds, names in sections(text):
        if not rounds:
            continue  # calentamiento / estiramientos
        for n in names:
            if n not in MAP:
                missing.add(n)
                continue
            for mus, f in MAP[n].items():
                tot[mus] += rounds * f
    return tot, missing

def table(rows, cols, title, flags=True):
    print(f"\n### {title}\n")
    print("| músculo | " + " | ".join(cols) + " |")
    print("|---|" + "---|" * len(cols))
    for m in MUSCLES:
        vals = [rows[c][m] for c in cols]
        flag = ""
        if flags and m != "cardio":
            mn = min(vals)
            flag = "  ⚠ 0" if mn == 0 else ("  ⚠ <4" if mn < 4 else "")
        print(f"| {m} | " + " | ".join(f"{v:g}" for v in vals) + f" |{flag}")

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    files = sorted(root.glob("rutina_*.html"))
    per = {}
    missing = set()
    for f in files:
        per[f.name], mis = audit(f)
        missing |= mis
    cols = [f.name.replace("rutina_", "").replace(".html", "") for f in files]
    table({c: per[f.name] for c, f in zip(cols, files)}, cols, "Series por músculo y rutina (1 = motor principal, 0,5 = secundario)", flags=False)
    weeks = {}
    for wk, fl in WEEKS.items():
        if all((root / x).exists() for x in fl):
            weeks[wk] = {m: sum(per[x][m] for x in fl) for m in MUSCLES}
    print("\n### Series por músculo y SEMANA (Push × Pull × full body; objetivo 6–12 en grupos grandes, nada en 0)\n")
    print("| músculo | mínimo | semana del mínimo | máximo | semana del máximo |")
    print("|---|---|---|---|---|")
    for m in MUSCLES:
        lo = min(weeks, key=lambda w: weeks[w][m]); hi = max(weeks, key=lambda w: weeks[w][m])
        flag = "" if m == "cardio" else ("  ⚠ 0" if weeks[lo][m] == 0 else ("  ⚠ <4" if weeks[lo][m] < 4 else ""))
        print(f"| {m} | {weeks[lo][m]:g} | {lo} | {weeks[hi][m]:g} | {hi} |{flag}")
    if missing:
        print("\n⚠ Ejercicios sin mapear en musculos.json:", "; ".join(sorted(missing)))

if __name__ == "__main__":
    main()
