"""Storie Instagram delle 13:00, stagione 2 (righe 10-18).
8 secondi, 1080x1920: targa NUOVI CONGEGNI, le 3 copertine nuove che entrano una alla volta,
Edwin che fa una cosa diversa ogni settimana, poi indica e dice "Tocca la mia foto e vai a vederli".
Uso: python3 storia_s2.py 10 [11 ...]
"""
import sys, os, math, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 's2'))
from reel_maker import sfx_whoosh, sfx_tick, sfx_clank, wav_write
from edwin_svg import head_svg, body_svg, render, gear
import griglia as G
import importlib.util
_sp = importlib.util.spec_from_file_location('griglia_s3', os.path.join(HERE, 's3', 'griglia.py')); G3 = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(G3)

W, H, FPS, DUR, SR = 1080, 1920, 30, 8.0, 44100
NF = int(DUR * FPS)
OUT = os.path.join(HERE, 'out_s3', 'storie'); os.makedirs(OUT, exist_ok=True)
CACHE = os.path.join(OUT, 'cache'); os.makedirs(CACHE, exist_ok=True)
COP = os.path.join(HERE, 'out_s3', 'copertine')
DK, CR, BR, GO, CU, TE, RO, BW, MU = '#2A1E16', '#F7F0E0', '#C08A3E', '#E3B657', '#B45A30', '#2f8a83', '#B3261E', '#5A341C', '#DCA24A'
LORA, LORA_I, INTER_B = G.LORA, '/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf', G.INTER_B
INTER_M = '/usr/share/fonts/opentype/inter/Inter-Medium.otf'
hexc, font = G.hexc, G.font


def ease(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)


def back(x):             # entrata con piccolo rimbalzo
    x = min(1.0, max(0.0, x)); c = 1.70158
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2


def svgimg(svg, w, h, key, scale=1.0):
    p = os.path.join(CACHE, key + '.png')
    if not os.path.exists(p):
        render(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{svg}</svg>', p, scale)
    return Image.open(p).convert('RGBA')


# ------------------------------------------------------------------ oggetti di scena (400 x 440, appoggiati in basso)
S = f'stroke="{DK}" stroke-width="6" stroke-linejoin="round"'


def p10(t):   # torchio da stampa: escono documento, slide e foglio di calcolo
    o = (f'<rect x="60" y="120" width="280" height="230" rx="18" fill="{CU}" {S}/><rect x="90" y="150" width="220" height="40" rx="8" fill="{DK}"/>'
         + gear(330, 120, 54, 10, GO, rot=t * 140) + gear(250, 92, 34, 8, BR, rot=-t * 220)
         + f'<rect x="40" y="340" width="320" height="50" rx="10" fill="{BW}" {S}/><rect x="70" y="390" width="26" height="46" fill="{DK}"/><rect x="304" y="390" width="26" height="46" fill="{DK}"/>')
    kinds = ['doc', 'slide', 'xls']
    for i, k in enumerate(kinds):
        a = ease((t - 0.5 - i * 1.0) / 0.7)
        if a <= 0:
            continue
        x, y = 110 + (1 - a) * 20, 300 - (1 - a) * 90 - i * 4 + (0 if a < 1 else 0)
        y = 330 - 14 * i if a >= 1 else 200 + a * (130 - 14 * i)
        rot = (-6, 4, -2)[i]
        inner = {'doc': f'<line x1="20" y1="22" x2="140" y2="22" stroke="{CU}" stroke-width="8"/>' + ''.join(f'<line x1="20" y1="{44 + j * 16}" x2="{150 - j * 14}" y2="{44 + j * 16}" stroke="#8C7350" stroke-width="5"/>' for j in range(3)),
                 'slide': f'<rect x="16" y="14" width="148" height="78" fill="#FFF8E8" stroke="{TE}" stroke-width="5"/><rect x="30" y="56" width="20" height="26" fill="{TE}"/><rect x="58" y="44" width="20" height="38" fill="{MU}"/><rect x="86" y="34" width="20" height="48" fill="{CU}"/>',
                 'xls': f'<rect x="16" y="14" width="148" height="78" fill="#fff" stroke="{TE}" stroke-width="4"/>' + ''.join(f'<line x1="{16 + j * 37}" y1="14" x2="{16 + j * 37}" y2="92" stroke="{TE}" stroke-width="3"/>' for j in range(1, 4)) + ''.join(f'<line x1="16" y1="{14 + j * 20}" x2="164" y2="{14 + j * 20}" stroke="{TE}" stroke-width="3"/>' for j in range(1, 4))}[k]
        o += f'<g transform="translate({x:.0f} {y - 106:.0f}) rotate({rot} 90 53)"><rect x="0" y="0" width="180" height="106" fill="#fff" {S}/>{inner}</g>'
    return o


def p11(t):   # orologio e calendario: le lancette corrono, le caselle si spuntano
    m, h = t * 300, t * 25
    o = (f'<circle cx="200" cy="120" r="100" fill="{CR}" {S}/><circle cx="200" cy="120" r="84" fill="none" stroke="{BR}" stroke-width="6"/>'
         + ''.join(f'<line x1="{200 + 70 * math.cos(a * math.pi / 6):.0f}" y1="{120 + 70 * math.sin(a * math.pi / 6):.0f}" x2="{200 + 80 * math.cos(a * math.pi / 6):.0f}" y2="{120 + 80 * math.sin(a * math.pi / 6):.0f}" stroke="{DK}" stroke-width="5"/>' for a in range(12))
         + f'<line x1="200" y1="120" x2="{200 + 46 * math.sin(math.radians(h)):.0f}" y2="{120 - 46 * math.cos(math.radians(h)):.0f}" stroke="{DK}" stroke-width="10" stroke-linecap="round"/>'
         + f'<line x1="200" y1="120" x2="{200 + 70 * math.sin(math.radians(m)):.0f}" y2="{120 - 70 * math.cos(math.radians(m)):.0f}" stroke="{RO}" stroke-width="6" stroke-linecap="round"/><circle cx="200" cy="120" r="10" fill="{DK}"/>'
         + f'<rect x="60" y="240" width="280" height="196" rx="10" fill="#fff" {S}/><rect x="60" y="240" width="280" height="46" rx="10" fill="{TE}" {S}/>'
         + f'<text x="200" y="274" font-family="Inter" font-weight="700" font-size="26" fill="#fff" text-anchor="middle">GENNAIO</text>')
    for i in range(6):
        cx, cy = 106 + (i % 3) * 94, 326 + (i // 3) * 64
        o += f'<rect x="{cx - 36}" y="{cy - 24}" width="72" height="48" rx="6" fill="{CR}" stroke="#C8B89A" stroke-width="3"/>'
        if t > 0.6 + i * 0.45:
            o += f'<path d="M{cx - 16} {cy} l12 12 l22 -24" stroke="{TE}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    return o


def p12(t):   # lente che scorre sulle righe e le evidenzia
    o = f'<rect x="50" y="40" width="300" height="396" rx="8" fill="#fff" {S}/><text x="80" y="92" font-family="Liberation Mono" font-weight="700" font-size="26" fill="{DK}">RESOCONTO</text>'
    for j in range(8):
        y = 130 + j * 36
        if t > 0.5 + j * 0.35 and j % 2 == 0:
            o += f'<rect x="72" y="{y - 12}" width="{230 - (j * 13) % 60}" height="24" fill="{GO}" opacity="0.7"/>'
        o += f'<line x1="78" y1="{y}" x2="{300 - (j * 13) % 60}" y2="{y}" stroke="#8C7350" stroke-width="6"/>'
    k = min(t, 3.4) / 0.35
    ly = 130 + min(5.0, k) * 36
    lx = 160 + 60 * math.sin(t * 5)
    o += (f'<line x1="{lx + 50:.0f}" y1="{ly + 50:.0f}" x2="{lx + 110:.0f}" y2="{ly + 110:.0f}" stroke="{BW}" stroke-width="22" stroke-linecap="round"/>'
          f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="64" fill="#E8F6F4" fill-opacity="0.45" stroke="{BR}" stroke-width="14"/>')
    return o


def p13(t):   # quaderno e penna d'oca: la scrittura cresce
    o = (f'<path d="M200 120 Q120 96 30 112 V420 Q120 404 200 428 Z" fill="#fff" {S}/><path d="M200 120 Q280 96 370 112 V420 Q280 404 200 428 Z" fill="#fff" {S}/>'
         f'<rect x="210" y="380" width="80" height="50" rx="8" fill="{DK}"/><rect x="222" y="370" width="56" height="16" rx="4" fill="{BR}"/>')
    n = 220
    prog = min(1.0, max(0.0, (t - 0.3) / 3.0))
    pts = []
    for line in range(5):
        x0, x1, y = (60, 180, 160 + line * 48) if line < 3 else (220, 340, 160 + (line - 3) * 48)
        for k in range(40):
            u = k / 39
            pts.append((x0 + (x1 - x0) * u, y + 7 * math.sin(u * 30 + line)))
    m = max(2, int(len(pts) * prog))
    path = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts[:m])
    # solo tratti della stessa riga collegati
    segs, cur = [], []
    for i, (x, y) in enumerate(pts[:m]):
        if i % 40 == 0 and cur:
            segs.append(cur); cur = []
        cur.append((x, y))
    segs.append(cur)
    for s in segs:
        if len(s) > 1:
            o += '<path d="M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in s) + f'" stroke="{BW}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    tx, ty = pts[m - 1]
    o += (f'<g transform="translate({tx:.0f} {ty:.0f}) rotate(-35)"><path d="M0 0 L-6 -40 Q-30 -150 10 -220 Q30 -140 6 -40 Z" fill="{CR}" {S}/>'
          f'<line x1="0" y1="0" x2="2" y2="-200" stroke="{BR}" stroke-width="4"/></g>')
    return o


def p14(t):   # schedario: il cassetto si apre e ci cadono le cartelle
    a = ease((t - 0.3) / 0.6)
    o = f'<rect x="80" y="40" width="240" height="396" rx="10" fill="{BW}" {S}/>'
    for i in (0, 2):
        y = 60 + i * 124
        o += f'<rect x="96" y="{y}" width="208" height="108" rx="6" fill="#7A4A26" {S}/><rect x="160" y="{y + 40}" width="80" height="22" rx="6" fill="{GO}" stroke="{DK}" stroke-width="4"/>'
    y, dx = 184, a * 60
    cols = [TE, RO, GO, CU]
    for i, c in enumerate(cols):
        f = ease((t - 1.0 - i * 0.55) / 0.35)
        if f > 0:
            fy = y - 120 * (1 - f) - 18
            o += f'<g transform="translate({120 + dx + i * 40:.0f} {fy:.0f}) rotate({(i - 1.5) * 4})"><rect x="0" y="0" width="70" height="60" rx="4" fill="{c}" {S}/><rect x="6" y="-14" width="30" height="18" rx="4" fill="{c}" {S}/></g>'
    o += f'<rect x="{96 + dx:.0f}" y="{y}" width="208" height="108" rx="6" fill="#9C5A30" {S}/><rect x="{160 + dx:.0f}" y="{y + 40}" width="80" height="22" rx="6" fill="{GO}" stroke="{DK}" stroke-width="4"/>'
    return o


def p15(t):   # cavalletto con il grafico che cresce
    o = (f'<line x1="120" y1="300" x2="70" y2="436" stroke="{BW}" stroke-width="16" stroke-linecap="round"/><line x1="280" y1="300" x2="330" y2="436" stroke="{BW}" stroke-width="16" stroke-linecap="round"/>'
         f'<line x1="200" y1="300" x2="200" y2="436" stroke="{BW}" stroke-width="14"/>'
         f'<rect x="40" y="40" width="320" height="270" rx="8" fill="#fff" {S}/><line x1="70" y1="270" x2="330" y2="270" stroke="{DK}" stroke-width="5"/>')
    vals, cols = (0.35, 0.55, 0.75, 1.0), (MU, BR, CU, TE)
    pts = []
    for i, (v, c) in enumerate(zip(vals, cols)):
        g = ease((t - 0.4 - i * 0.5) / 0.5) * v * 170
        x = 88 + i * 62
        o += f'<rect x="{x}" y="{270 - g:.0f}" width="44" height="{g:.0f}" fill="{c}" stroke="{DK}" stroke-width="4"/>'
        pts.append((x + 22, 270 - g - 22))
    if t > 2.6:
        a = ease((t - 2.6) / 0.6)
        o += f'<path d="M{pts[0][0]} {pts[0][1]:.0f} L{pts[0][0] + (pts[3][0] - pts[0][0]) * a:.0f} {pts[0][1] + (pts[3][1] - pts[0][1]) * a:.0f}" stroke="{RO}" stroke-width="8" stroke-linecap="round"/>'
    return o


def p16(t):   # lavagna: lettere col gesso e la spunta; flashcard sul banco
    o = (f'<line x1="110" y1="300" x2="80" y2="436" stroke="{BW}" stroke-width="14" stroke-linecap="round"/><line x1="290" y1="300" x2="320" y2="436" stroke="{BW}" stroke-width="14" stroke-linecap="round"/>'
         f'<rect x="30" y="40" width="340" height="270" rx="6" fill="#2F3B33" stroke="#7A4A26" stroke-width="16"/>')
    for i, s in enumerate(('A', 'B', 'C')):
        if t > 0.5 + i * 0.6:
            o += f'<text x="{90 + i * 80}" y="150" font-family="Lora" font-weight="700" font-size="76" fill="#F3E9D2" text-anchor="middle">{s}</text>'
    if t > 2.5:
        a = ease((t - 2.5) / 0.5)
        o += f'<path d="M110 230 l40 40 l{100 * a:.0f} -{90 * a:.0f}" stroke="{GO}" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    o += f'<rect x="250" y="210" width="34" height="14" rx="4" fill="#F3E9D2"/>'
    return o


def p17(t):   # scatoloni del trasloco: ne cadono due dall'alto
    def box(x, y, w, h, lab, rot=0):
        return (f'<g transform="translate({x:.0f} {y:.0f}) rotate({rot})"><rect x="{-w / 2}" y="{-h}" width="{w}" height="{h}" fill="#C9965A" {S}/>'
                f'<rect x="-12" y="{-h}" width="24" height="{h}" fill="#E3C28A"/><rect x="{-w / 2}" y="{-h}" width="{w}" height="{h}" fill="none" {S}/>'
                f'<text x="0" y="{-h / 2 + 10}" font-family="Liberation Mono" font-weight="700" font-size="26" fill="{DK}" text-anchor="middle">{lab}</text></g>')
    o = box(120, 436, 170, 140, 'CASA') + box(290, 436, 150, 120, 'LIBRI')
    for i, (x, w, h, lab, base, t0) in enumerate(((150, 150, 120, 'CUCINA', 296, 0.6), (270, 120, 100, 'FRAGILE', 316, 1.6))):
        f = (t - t0) / 0.45
        if f <= 0:
            continue
        y = base - 600 * (1 - min(1, f)) ** 2
        if 1 < f < 1.5:
            y -= 18 * math.sin((f - 1) / 0.5 * math.pi)
        o += box(x, y, w, h, lab, (-4, 5)[i])
    return o


def p18(t):   # regalo di fine stagione: il coperchio salta, escono stelle e la medaglia 54
    o = ''
    a = ease((t - 1.4) / 0.4)
    for k in range(9):
        if t > 1.5:
            f = min(1.0, (t - 1.5) / 1.2)
            ang = math.radians(-160 + k * 17.5)
            r = 40 + 190 * ease(f)
            x, y = 200 + r * math.cos(ang), 250 + r * math.sin(ang)
            c = (GO, RO, TE)[k % 3]
            o += f'<g transform="translate({x:.0f} {y:.0f}) rotate({t * 200 + k * 40:.0f})"><path d="M0 -16 L5 -5 L16 -4 L8 4 L10 16 L0 10 L-10 16 L-8 4 L-16 -4 L-5 -5 Z" fill="{c}" stroke="{DK}" stroke-width="3"/></g>'
    o += (f'<rect x="80" y="250" width="240" height="186" fill="{RO}" {S}/><rect x="180" y="250" width="40" height="186" fill="{GO}" stroke="{DK}" stroke-width="4"/>')
    lx, ly, rot = 200 + 60 * a, 250 - 120 * a, 22 * a
    o += (f'<g transform="translate({lx:.0f} {ly:.0f}) rotate({rot:.0f})"><rect x="-136" y="-50" width="272" height="56" fill="#C8352B" {S}/><rect x="-20" y="-50" width="40" height="56" fill="{GO}" stroke="{DK}" stroke-width="4"/>'
          f'<path d="M0 -50 C-60 -110 -90 -60 0 -50 C90 -60 60 -110 0 -50 Z" fill="{GO}" {S}/></g>')
    m = ease((t - 1.8) / 0.7)
    if m > 0:
        my = 250 - 140 * m
        o += (f'<g transform="translate(200 {my:.0f})"><path d="M-24 20 L-44 100 L-22 90 L-10 112 L4 40 Z" fill="{RO}"/><path d="M24 20 L44 100 L22 90 L10 112 L-4 40 Z" fill="{TE}"/>'
              f'<circle cx="0" cy="0" r="62" fill="{GO}" {S}/><circle cx="0" cy="0" r="46" fill="none" stroke="{BR}" stroke-width="5"/>'
              f'<text x="0" y="22" font-family="Lora" font-weight="700" font-size="58" fill="{DK}" text-anchor="middle">81</text></g>')
    return o


PROPS = {19: p11, 20: p10, 21: p16, 22: p15, 23: p12, 24: p14, 25: p13, 26: p17, 27: p18}
# posa di Edwin mentre lavora, posa finale (indica le copertine o saluta)
POSE = {r: ('banco', ('indica', 'saluta')[r % 2]) for r in range(19, 28)}
T_SWITCH = 3.7


# ------------------------------------------------------------------ pezzi fissi
def background(r):
    m = Image.open(os.path.join(HERE, 'out_s3', 'master_vuoto.png')).convert('RGB')
    y0 = G3.row_y(r) - G3.EXT
    bg = m.crop((G.TW, y0, 2 * G.TW, y0 + 1920)).filter(ImageFilter.GaussianBlur(22))
    paper = Image.new('RGB', (W, H), hexc('#EFE3C8')[:3])
    bg = Image.blend(bg, paper, 0.45).convert('RGBA')
    d = ImageDraw.Draw(bg)
    for y in range(0, H, 54):
        d.line((0, y, W, y), fill=(42, 30, 22, 9), width=2)
    # pavimento dell'officina sotto Edwin
    d.rectangle((0, 1700, W, H), fill=hexc('#7A4A26'))
    d.rectangle((0, 1700, W, 1716), fill=hexc(BR))
    for x in range(-40, W, 120):
        d.line((x, 1716, x + 60, H), fill=(42, 30, 22, 60), width=4)
    return bg


def plate():
    w, h = 760, 190
    im = Image.new('RGBA', (w + 80, h + 80), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((40, 40, 40 + w, 40 + h), 22, fill=hexc(DK), outline=hexc(BR), width=8)
    d.rounded_rectangle((56, 56, 24 + w, 24 + h), 14, outline=hexc('#7A5A32'), width=3)
    f = font(LORA, 64, 700)
    d.text((40 + w / 2 + 20, 40 + 66), 'NUOVI CONGEGNI', font=f, fill=hexc('#F3E2B8'), anchor='mm')
    d.text((40 + w / 2 + 20, 40 + 138), 'IN OFFICINA', font=f, fill=hexc('#F3E2B8'), anchor='mm')
    for x, y in ((64, 64), (16 + w, 64), (64, 16 + h), (16 + w, 16 + h)):
        d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=hexc(BR))
    d.ellipse((0, 0, 110, 110), fill=hexc(BR), outline=hexc(DK), width=5)
    d.ellipse((12, 12, 98, 98), fill=hexc(GO))
    d.text((55, 57), '+3', font=font(LORA, 44, 700), fill=hexc(DK), anchor='mm')
    return G.sticker(im, 14, -1.5)


def cover_card(n, rot):
    c = Image.open(os.path.join(COP, f'reel{n}_copertina.png')).convert('RGBA').crop((0, 240, 1080, 1680))
    cw, ch = 286, 381
    c = c.resize((cw, ch), Image.LANCZOS)
    im = Image.new('RGBA', (cw + 16, ch + 70), hexc(DK)); im.alpha_composite(c, (8, 8))
    d = ImageDraw.Draw(im)
    d.text((im.width / 2, ch + 40), f'REEL  ·  N. {n}', font=font(INTER_B, 26), fill=hexc('#F3E2B8'), anchor='mm')
    return G.sticker(im, 12, rot)


def bubble():
    w, h = 430, 136
    im = Image.new('RGBA', (w + 20, h + 70), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((10, 10, 10 + w, 10 + h), 34, fill=hexc('#FFFDF6'), outline=hexc(DK), width=6)
    d.polygon([(70, 10 + h - 4), (40, h + 62), (130, 10 + h - 4)], fill=hexc('#FFFDF6'))
    d.line([(70, 10 + h), (40, h + 62), (130, 10 + h)], fill=hexc(DK), width=6, joint='curve')
    f = font(LORA_I, 42, 600)
    d.text((10 + w / 2, 10 + 46), 'Tocca la mia foto', font=f, fill=hexc(DK), anchor='mm')
    d.text((10 + w / 2, 10 + 94), 'e vai a vederli', font=f, fill=hexc(CU), anchor='mm')
    return im


def week_tag(r):
    im = Image.new('RGBA', (560, 90), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    tw = d.textlength(f'settimana {r}', font=font(LORA_I, 54, 600))
    d.rounded_rectangle((0, 12, tw + 26, 80), 34, fill=hexc(CR), outline=hexc(DK), width=4)
    d.text((13, 45), f'settimana {r}', font=font(LORA_I, 54, 600), fill=hexc(CU), anchor='lm')
    x = 40 + tw
    d.rounded_rectangle((x, 18, x + 200, 72), 8, fill=hexc(TE))
    d.text((x + 100, 46), 'STAGIONE 3', font=font(INTER_B, 26), fill=(255, 255, 255, 255), anchor='mm')
    return im.crop(im.getbbox())


def ai_badge():
    im = Image.new('RGBA', (520, 60), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, 519, 59), 30, fill=(42, 30, 22, 150))
    d.text((260, 31), "Personaggio creato con l'IA", font=font(INTER_M, 28), fill=(255, 255, 255, 235), anchor='mm')
    return im


BENCH_Y, ED_DROP = 1590, 74


def bench_img():
    svg = (f'<rect x="10" y="10" width="440" height="44" rx="8" fill="#9C5A30" {S}/><rect x="40" y="54" width="380" height="96" fill="#7A4A26" {S}/>'
           f'<rect x="70" y="72" width="140" height="56" rx="6" fill="#9C5A30" stroke="{DK}" stroke-width="4"/><rect x="250" y="72" width="140" height="56" rx="6" fill="#9C5A30" stroke="{DK}" stroke-width="4"/>'
           f'<circle cx="140" cy="100" r="8" fill="{GO}"/><circle cx="320" cy="100" r="8" fill="{GO}"/>')
    return svgimg(svg, 460, 160, 'banco')


# ------------------------------------------------------------------ Edwin
SB, SH, ES = 0.74, 0.85, 0.64
_ed = {}


def edwin(pose, arm_q, gear_q, eyes):
    k = (pose, arm_q, gear_q, eyes)
    if k in _ed:
        return _ed[k]
    bp = os.path.join(CACHE, f'b_{pose}_{arm_q}_{gear_q}.png')
    if not os.path.exists(bp):
        render(body_svg(gear_rot=gear_q * 7.5, arm=arm_q / 3, pose=pose), bp, SB * ES)
    hp = os.path.join(CACHE, f'h_{eyes}.png')
    if not os.path.exists(hp):
        render(head_svg(0.1, eyes), hp, SH * ES)
    b, h = Image.open(bp).convert('RGBA'), Image.open(hp).convert('RGBA')
    BH = b.height
    hy = int(SB * ES * 170) - h.height + int(SB * ES * 48)
    top = min(0, hy)
    im = Image.new('RGBA', (max(b.width, h.width), BH - top), (0, 0, 0, 0))
    im.alpha_composite(b, ((im.width - b.width) // 2, -top))
    im.alpha_composite(h, ((im.width - h.width) // 2, hy - top))
    im = im.crop(im.getbbox())
    st = G.sticker(im, 12, 0, shadow=True)
    _ed[k] = st
    return st


# ------------------------------------------------------------------ audio
def audio(r, path):
    n = int(DUR * SR); a = np.zeros(n)
    def put(sig, t, g=1.0):
        i = int(t * SR); j = min(n, i + len(sig)); a[i:j] += g * sig[:j - i]
    wh, tk, cl = sfx_whoosh(), sfx_tick(), sfx_clank()
    put(wh, 0.05, 0.7)
    for i in range(3):
        put(tk, 0.55 + i * 0.45, 0.9)
    # ticchettio dell'officina mentre Edwin lavora
    t = 0.3
    while t < T_SWITCH:
        put(tk, t, 0.22); t += 0.25
    put(cl, T_SWITCH, 0.6)
    # piccolo carillon: arpeggio dolce in loop
    notes = [523.25, 659.25, 783.99, 1046.5, 783.99, 659.25]
    if r == 27:
        notes = [587.33, 739.99, 880.0, 1174.66, 880.0, 739.99]
    tt, k = 0.0, 0
    while tt < DUR - 0.3:
        f = notes[k % len(notes)]; d = 0.9
        x = np.arange(int(d * SR)) / SR
        s = (np.sin(2 * np.pi * f * x) + 0.3 * np.sin(4 * np.pi * f * x)) * np.exp(-x * 4.5)
        put(s, tt, 0.11); tt += 0.3; k += 1
    # ding quando appare il fumetto
    x = np.arange(int(1.2 * SR)) / SR
    put((np.sin(2 * np.pi * 1318.5 * x) + 0.4 * np.sin(2 * np.pi * 2637 * x)) * np.exp(-x * 3.5), T_SWITCH + 0.2, 0.25)
    fade = np.ones(n); fl = int(0.5 * SR); fade[-fl:] = np.linspace(1, 0, fl)
    a = a * fade
    a = a / max(1e-6, np.abs(a).max()) * 0.8
    wav_write(path, a, SR)


# ------------------------------------------------------------------ composizione
def make(r):
    nums = [55 + (r - 19) * 3 + i for i in range(3)]
    bg = background(r)
    pl = plate()
    cards = [cover_card(n, rot) for n, rot in zip(nums, (-3.5, 1.5, 4))]
    bub, wk, ai = bubble(), week_tag(r), ai_badge()
    fsub = font(LORA_I, 40, 500)
    sub = Image.new('RGBA', (W, 60), (0, 0, 0, 0))
    ImageDraw.Draw(sub).text((W / 2, 30), 'Sono appena arrivati sul profilo', font=fsub, fill=hexc(DK), anchor='mm')
    wav = os.path.join(OUT, f'audio{r}.wav'); audio(r, wav)
    dst = os.path.join(OUT, f'storia_riga{r}.mp4')
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
           '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', str(DUR), dst]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    pose_work, pose_end = POSE[r]
    bench = bench_img()
    pcache = {}
    for f in range(NF):
        t = f / FPS
        fr = bg.copy()
        # targa che scende
        a = back(t / 0.45)
        fr.alpha_composite(pl, (int(W / 2 - pl.width / 2), int(195 - (1 - a) * 330)))
        if t > 0.35:
            sa = Image.new('RGBA', sub.size, (0, 0, 0, 0)); sa = Image.blend(sa, sub, ease((t - 0.35) / 0.3))
            fr.alpha_composite(sa, (0, 492))
        # copertine
        for i, c in enumerate(cards):
            p = (t - 0.55 - i * 0.45) / 0.35
            if p <= 0:
                continue
            s = 0.55 + 0.45 * back(p)
            ci = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.BICUBIC) if s != 1 else c
            cx, cy = 210 + i * 330, 830 + (i == 1) * 14
            fr.alpha_composite(ci, (int(cx - ci.width / 2), int(cy - ci.height / 2)))
        if t > 1.6:
            wa = Image.blend(Image.new('RGBA', wk.size, (0, 0, 0, 0)), wk, ease((t - 1.6) / 0.3))
            fr.alpha_composite(wa, (W - 70 - wk.width, 1078))
        # oggetto di scena
        qt = round(t * 15) / 15
        pk = (r, qt)
        if pk not in pcache:
            pcache[pk] = svgimg(PROPS[r](qt), 400, 440, f'p{r}_{int(qt * 15)}', 1.0)
        pim = pcache[pk]
        fr.alpha_composite(pim, (600, 1712 - pim.height))
        # Edwin
        working = t < T_SWITCH
        pose = pose_work if working else pose_end
        arm_q = int(round(1.5 + 1.5 * math.sin(t * 7))) if working else int(round(1.5 + 1.5 * math.sin(t * 4)))
        gear_q = int(t * 12) % 12
        eyes = 'happy' if (T_SWITCH <= t < T_SWITCH + 0.7) else ('blink' if (int(t * FPS) % 95) in (60, 61, 62) else 'open')
        ed = edwin(pose, arm_q, gear_q, eyes)
        bob = int(4 * math.sin(t * 6))
        hop = -int(26 * math.sin(min(1, (t - T_SWITCH) / 0.35) * math.pi)) if T_SWITCH <= t < T_SWITCH + 0.35 else 0
        ex = 320
        fr.alpha_composite(ed, (int(ex - ed.width / 2), BENCH_Y + ED_DROP - ed.height + bob + hop))
        fr.alpha_composite(bench, (ex - bench.width // 2, BENCH_Y))
        # fumetto
        if t >= T_SWITCH + 0.15:
            b = back((t - T_SWITCH - 0.15) / 0.3)
            bi = bub.resize((max(1, int(bub.width * b)), max(1, int(bub.height * b))), Image.BICUBIC) if b != 1 else bub
            bx, by = 590, 1150
            fr.alpha_composite(bi, (int(bx - bi.width * 0.15), int(by + bub.height - bi.height)))
        fr.alpha_composite(ai, (W // 2 - ai.width // 2, 1800))
        pr.stdin.write(fr.tobytes())
    pr.stdin.close(); pr.wait()
    return dst


if __name__ == '__main__':
    for a in sys.argv[1:]:
        print(make(int(a)))
