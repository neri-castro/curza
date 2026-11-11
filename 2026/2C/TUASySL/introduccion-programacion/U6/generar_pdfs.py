"""Genera los PDFs de enunciados de U6 desde los enunciados.md.
Requiere: pip install reportlab   (uso: python3 generar_pdfs.py)"""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.pdfgen import canvas

NAVY = HexColor("#1B365D"); ORANGE = HexColor("#FF7F00"); LIGHT = HexColor("#F8FAFC")
GREY = HexColor("#6B7280"); BORDER = HexColor("#CBD5E1"); TEXT = HexColor("#1F2937")
W, H = A4; LM = 48; CW = W - 2 * LM

st = {
 "title": ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=18, leading=22, alignment=1, textColor=NAVY),
 "sub": ParagraphStyle("s", fontName="Helvetica", fontSize=9.5, leading=12, alignment=1, textColor=ORANGE),
 "body": ParagraphStyle("b", fontName="Helvetica", fontSize=9, leading=12.5, textColor=TEXT),
 "box": ParagraphStyle("bx", fontName="Helvetica", fontSize=8.7, leading=12, textColor=TEXT, spaceAfter=3),
 "bar": ParagraphStyle("br", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=white),
 "prob": ParagraphStyle("p", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=NAVY, spaceBefore=14, spaceAfter=4),
 "polya": ParagraphStyle("pl", fontName="Helvetica", fontSize=8.7, leading=12.5, textColor=TEXT),
}

def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    codes = []
    def keep(m):
        codes.append('<font name="Courier" size="8.5">%s</font>' % m.group(1)); return "\0%d\0" % (len(codes) - 1)
    t = re.sub(r"`([^`]+)`", keep, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    return re.sub("\0(\\d+)\0", lambda m: codes[int(m.group(1))], t)

def footer(c, doc, total):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, H - 30, W, 30, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 8.5); c.drawString(LM, H - 19, "UNIVERSIDAD NACIONAL DEL COMAHUE — CURZAS")
    c.setFont("Helvetica", 8.5); c.drawRightString(W - LM, H - 19, doc.hdr_right)
    c.setStrokeColor(BORDER); c.line(LM, 38, W - LM, 38)
    c.setFillColor(GREY); c.setFont("Helvetica", 7.5)
    c.drawString(LM, 28, "TUASySL - Introducción a la Programación")
    c.drawRightString(W - LM, 28, "Sede Atlántica | CURZAS - UNCo | Página %d de %d" % (c.getPageNumber(), total))
    c.restoreState()

class Num(canvas.Canvas):
    def __init__(s, *a, **k): super().__init__(*a, **k); s.pages = []
    def showPage(s): s.pages.append(dict(s.__dict__)); s._startPage()
    def save(s):
        n = len(s.pages)
        for p in s.pages:
            s.__dict__.update(p); footer(s, s.doc_ref, n); super().showPage()
        super().save()

def box(flows, bar=None, border=None):
    t = Table([[flows]], colWidths=[CW - (0 if not bar else 0)])
    style = [("BACKGROUND", (0,0), (-1,-1), LIGHT), ("LEFTPADDING", (0,0), (-1,-1), 12),
             ("RIGHTPADDING", (0,0), (-1,-1), 10), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 5)]
    if bar: style.append(("LINEBEFORE", (0,0), (0,-1), 5, ORANGE))
    if border: style.append(("BOX", (0,0), (-1,-1), 0.6, BORDER))
    t.setStyle(TableStyle(style)); return t

def parse(md):
    head, *secs = re.split(r"\n## ", md)
    probs = []
    for s in secs:
        title, *rest = s.split("\n", 1)
        body = rest[0] if rest else ""
        body = re.split(r"\n---", body)[0]
        paras = [p.strip() for p in body.strip().split("\n\n") if p.strip()]
        probs.append((title.strip(), paras))
    return probs

def build(md_path, out, doc_title, subtitle, intro, bar_text, hdr_right="Tecnicatura en Admin. de Sistemas y Software Libre"):
    probs = parse(open(md_path, encoding="utf-8").read())
    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=LM, rightMargin=LM, topMargin=48, bottomMargin=52, title=doc_title, author="TUASySL - CURZAS")
    doc.hdr_right = hdr_right
    doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(LM, 52, CW, H - 100, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
    el = [Spacer(1, 6), Paragraph(doc_title, st["title"]), Spacer(1, 3), Paragraph(subtitle, st["sub"]), Spacer(1, 12),
          box([Paragraph(inline(x), st["box"]) for x in intro], bar=True), Spacer(1, 14)]
    b = Table([[Paragraph(bar_text, st["bar"])]], colWidths=[CW])
    b.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), NAVY), ("LEFTPADDING", (0,0), (-1,-1), 10), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
    el += [b]
    for title, paras in probs:
        grp = [Paragraph(inline(title.replace(":", ":", 1).upper().replace("PROBLEMA", "PROBLEMA", 1)) if False else inline(re.sub(r"^(Problema \d+):", lambda m: m.group(1).upper() + ":", title)), st["prob"])]
        guia = None
        for p in paras:
            if p.startswith("*Solución"): continue
            if p.startswith("**Guía:**"): guia = p[len("**Guía:**"):].strip(); continue
            p = p.replace("\n", " ")
            if len(grp) == 1 and not any(q.startswith("**Consigna") for q in paras) and not p.startswith("**"):
                p = "**Consigna:** " + p
            p = re.sub(r"\s(?=[a-f]\) \S)", "\n", p)  # a) b) c) en líneas aparte
            for line in p.split("\n"):
                line = re.sub(r"^([a-f]\)) ", r"**\1** ", line)
                grp.append(Paragraph(inline(line), st["body"]))
        if not guia:
            guia = "¿Cuáles son los datos de entrada, las constantes y la salida esperada? ¿Qué estructura (for, dict, set, lista) conviene usar y por qué? ¿Qué resultado esperás obtener con los datos del enunciado?"
        pol = [Paragraph("<b>Fase Polya / Guía de Resolución:</b>", st["polya"]), Spacer(1, 5)]
        qs = [q for q in re.split(r"(?<=\?)\s+", guia or "") if q]
        qs.append("Espacio para boceto de código:")
        for i, q in enumerate(qs, 1): pol.append(Paragraph("%d. %s" % (i, inline(q)), st["polya"]))
        pol.append(Spacer(1, 38))
        grp += [Spacer(1, 5), box(pol, border=True)]
        el.append(KeepTogether(grp))
    class C(Num):
        def __init__(s, *a, **k): super().__init__(*a, **k); s.doc_ref = doc
    doc.build(el, canvasmaker=C)

import os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
build(D+"ejercicios_librerias/enunciados.md", D+"ejercicios_librerias/practica_extra_librerias.pdf",
 "PRÁCTICA EXTRA: LIBRERÍAS EN PYTHON", "Módulos Estándar: os, sys y platform — Ejercicios Complementarios",
 ["**Objetivo de la Práctica:** Reforzar el uso de módulos estándar combinándolos con lo visto en U4 (funciones) y U5 (bucles, slicing, listas).",
  "**Estilo y Buenas Prácticas (PEP 8):** Usar convención *snake_case* para variables y funciones, *SCREAMING_SNAKE_CASE* para constantes e importar las librerías al inicio del archivo.",
  "**Metodología Polya:** Identificar la función de la librería requerida, planificar el script y verificar el resultado por pantalla."],
 "SECUENCIA DE PROBLEMAS PRÁCTICOS")
build(D+"ejercicios_listas_tuplas/enunciados.md", D+"ejercicios_listas_tuplas/practica_extra_listas_tuplas.pdf",
 "PRÁCTICA EXTRA: LISTAS Y TUPLAS EN PYTHON", "Guía de Ejercicios y Registro de Trabajo (Método de Polya)",
 ["**Pautas de Trabajo:** Resolver cada problema con la estructura de repetición fija *for* (por elementos o por índices con range(len())). No utilizar *while*.",
  "**Estilo y Buenas Prácticas (PEP 8):** *snake_case* para variables y listas, *SCREAMING_SNAKE_CASE* para constantes.",
  "**Metodología Polya:** Completar las 4 fases: comprender, planificar, ejecutar y verificar con prueba de escritorio."],
 "SECUENCIA DE PROBLEMAS PRÁCTICOS")
build(D+"ejercicios_conjuntos_diccionarios/enunciados.md", D+"ejercicios_conjuntos_diccionarios/practica_extra_conjuntos_diccionarios.pdf",
 "PRÁCTICA EXTRA: DICCIONARIOS Y CONJUNTOS", "Estructuras de Datos: dict y set — Ejercicios Complementarios",
 ["**Objetivo de la Práctica:** Ejercitar las operaciones de diccionarios (dict) y conjuntos (set) y decidir cuál conviene según el problema.",
  "**Estilo y Buenas Prácticas (PEP 8):** *snake_case* para variables y funciones, *SCREAMING_SNAKE_CASE* para constantes.",
  "**Metodología Polya:** Comprender el problema, planificar la estructura de datos, codificar y verificar el resultado por pantalla."],
 "SECUENCIA DE PROBLEMAS PRÁCTICOS")
