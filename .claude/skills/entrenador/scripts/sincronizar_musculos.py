#!/usr/bin/env python3
"""Copia en cada rutina_*.html el mapa ejercicio -> músculos (references/musculos.json),
solo con los ejercicios de esa página. Lo usa el resumen para colorear la figura.

Uso:  python3 .claude/skills/entrenador/scripts/sincronizar_musculos.py [carpeta_del_repo]
Hay que ejecutarlo cada vez que cambien los ejercicios de una rutina o musculos.json.
"""
import json, re, sys, html
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAP = json.loads((HERE.parent / "references" / "musculos.json").read_text(encoding="utf-8"))
MAP.pop("_doc", None)
TAG = re.compile(r'<script type="application/json" id="mus">.*?</script>\n?', re.S)

def expected(text):
    names = [html.unescape(n) for n in re.findall(r'<p class="nm">(.*?)</p>', text)]
    data = {n: MAP[n] for n in dict.fromkeys(names) if n in MAP}
    missing = sorted({n for n in names if n not in MAP})
    tag = '<script type="application/json" id="mus">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>\n"
    return tag, missing

def current(text):
    m = TAG.search(text)
    return m.group(0) if m else None

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    for f in sorted(root.glob("rutina_*.html")):
        text = f.read_text(encoding="utf-8")
        tag, missing = expected(text)
        if "</main>\n" + tag in text:
            state = "igual"
        else:
            text = TAG.sub("", text)  # siempre justo después de </main>, antes de los scripts
            text = text.replace("</main>\n", "</main>\n" + tag, 1)
            f.write_text(text, encoding="utf-8"); state = "actualizado"
        print(f"{f.name}: {state}" + (f"  ⚠ sin mapear: {'; '.join(missing)}" if missing else ""))

if __name__ == "__main__":
    main()
