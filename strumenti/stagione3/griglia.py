"""Stagione 3 (righe 19-27): "L'atlante del viaggiatore".
Tutta la griglia è un'unica carta geografica d'epoca (3 colonne x 9 righe, tessere 1080x1440),
con la rotta rossa che tocca i congegni nell'ordine di uscita; in fondo la carta si strappa
e si vede la cima vera della stagione 2. Ritaglia le copertine 1080x1920 di ogni Reel.

Uso: python3 s3/griglia.py
"""
import sys, os, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, 's2'))
import griglia as G2                       # adesivi, font, Edwin della stagione 2
import importlib.util
_sp = importlib.util.spec_from_file_location('temi_s3', os.path.join(HERE, 'temi.py')); _T = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_T)
DEV, TEMI, PED = _T.DEV, _T.TEMI, _T.PED
from edwin_svg import render

TW, TH, EXT = 1080, 1440, 240
MW, MH = 3 * TW, EXT + 9 * TH + EXT
DK, CR, BR, GO, CU, TE, RO, MU, BW = '#2A1E16', '#F7F0E0', '#C08A3E', '#E3B657', '#B45A30', '#2f8a83', '#B3261E', '#DCA24A', '#5A341C'
INK = (58, 40, 26)
LORA, LORA_I = G2.LORA, '/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'
INTER_B = G2.INTER_B
OUT = os.path.join(ROOT, 'out_s3'); os.makedirs(OUT, exist_ok=True)
CACHE = os.path.join(OUT, 'cache'); os.makedirs(CACHE, exist_ok=True)
S2_MASTER = os.path.join(ROOT, 'out_s2', 'master.png')
hexc, font, sticker, place = G2.hexc, G2.font, G2.sticker, G2.place
TEAR = 205                                   # lo strappo è 205 px sopra il fondo della riga 19


def row_y(r):
    return EXT + (27 - r) * TH


def col_x(c):
    return c * TW


def post_pos(n):           # in ogni riga esce prima la destra, poi il centro, poi la sinistra
    return 19 + (n - 55) // 3, 2 - (n - 55) % 3


# Edwin: una tessera per riga, mai sulla cartolina di "Prima e dopo"
EDWIN = {19: (2, 'saluta', -3), 20: (1, 'regge', 2), 21: (0, 'indica', -2), 22: (1, 'testa', 5), 23: (2, 'regge', -3),
         24: (0, 'saluta', 3), 25: (2, 'indica', 2), 26: (1, 'regge', -2), 27: (0, 'saluta', 3)}
DEV_IN_EDWIN = {'saluta': (320, 1090), 'regge': (540, 1110), 'indica': (800, 650), 'testa': (770, 1130)}
# nome della regione (in basso, scritto sulla carta) e decorazione della fascia bassa
REGIONE = {20: (0, 'PORTO DEI SITI'), 21: (2, 'ISOLA DEI GIOCHI'), 22: (0, 'VALLE DELLA REGIA'), 23: (0, 'MONTI DEI DATI'),
           24: (2, 'TERRA DELLE APP'), 25: (0, 'BAIA DEI LIBRI'), 26: (2, 'COSTA DELLA BOTTEGA'), 27: (2, "CAPO DELL'ARRIVO")}
DECOR = {20: (2, 'bussola'), 21: (1, 'nave'), 22: (2, 'nave'), 23: (1, 'bussola'), 24: (1, 'serpente'),
         25: (1, 'nave'), 26: (0, 'bussola'), 27: (1, 'mongolfiera')}
BAND_Y = 1318                                # centro della fascia bassa libera di ogni tessera


def T(r, c, tx, ty):
    return (col_x(c) + tx, row_y(r) + ty)


def dev_center(n):
    r, c = post_pos(n)
    e = EDWIN[r]
    if e[0] == c:
        dx, dy = DEV_IN_EDWIN[e[1]]
        return T(r, c, dx, dy - (70 if r == 19 else 0))
    return T(r, c, 540, 860 if n in PED else (820 if r == 19 else 880))


# ------------------------------------------------------------------ la carta geografica
def land_field():
    """Campo continuo: > 0 terra, < 0 mare. Rumore morbido + spinte locali (mare sotto le navi, terra sotto i nomi)."""
    rng = np.random.default_rng(31)
    k = 6
    h, w = MH // k, MW // k
    f = ndimage.gaussian_filter(rng.standard_normal((h, w)), 26) * 9.0
    f += ndimage.gaussian_filter(rng.standard_normal((h, w)), 60) * 16.0
    f += ndimage.gaussian_filter(rng.standard_normal((h, w)), 7) * 0.9
    f = (f - f.mean()) / f.std()
    yy, xx = np.mgrid[0:h, 0:w]
    def bump(x, y, s, a):
        nonlocal f
        f += a * np.exp(-(((xx - x / k) ** 2 + (yy - y / k) ** 2) / (2 * (s / k) ** 2)))
    for r, (c, _) in REGIONE.items():
        x, y = T(r, c, 540, BAND_Y); bump(x, y, 260, 2.2)
    for r, (c, kind) in DECOR.items():
        x, y = T(r, c, 540 + (180 if kind == 'bussola' else 0), BAND_Y)
        bump(x, y, 240, -2.6 if kind in ('nave', 'serpente') else (-1.2 if kind == 'bussola' else 0))
    return Image.fromarray(f.astype(np.float32), mode='F').resize((MW, MH), Image.BICUBIC)


def map_base():
    p = os.path.join(CACHE, 'mappa.png')
    if os.path.exists(p):
        return Image.open(p).convert('RGBA')
    field = np.asarray(land_field())
    land = field > 0.15
    land = ndimage.binary_opening(land, iterations=6)
    lab, nlab = ndimage.label(land)
    d_out = ndimage.distance_transform_edt(~land).astype(np.float32)   # distanza dalla costa, in mare
    d_in = ndimage.distance_transform_edt(land).astype(np.float32)     # distanza dalla costa, a terra
    rng = np.random.default_rng(5)
    # carta: pergamena con macchie leggere
    stain = ndimage.gaussian_filter(rng.standard_normal((MH // 8, MW // 8)), 12)
    stain = np.asarray(Image.fromarray((stain / np.abs(stain).max()).astype(np.float32), mode='F').resize((MW, MH), Image.BICUBIC))
    grain = rng.standard_normal((MH, MW)).astype(np.float32)
    sea = np.array(hexc('#A8C9C1')[:3], np.float32); sea_d = np.array(hexc('#8FB5AE')[:3], np.float32)
    paper = np.array(hexc('#EEDDB2')[:3], np.float32)
    tints = [np.array(hexc(c)[:3], np.float32) for c in ('#C9D29A', '#E8B9A2', '#E9CF86', '#B9D2B4')]
    img = np.empty((MH, MW, 3), np.float32)
    # mare: più scuro al largo, più chiaro vicino alla costa
    t = np.clip(d_out / 420.0, 0, 1)[..., None]
    img[:] = sea * (1 - t) + sea_d * t
    # terra: pergamena, con la fascia acquerellata lungo la costa (colore diverso per ogni isola)
    tint_idx = (lab % len(tints))
    tint = np.stack(tints)[tint_idx]
    band = np.clip(1 - d_in / 70.0, 0, 1)[..., None] * 0.85
    landc = paper * (1 - band) + tint * band
    img = np.where(land[..., None], landc, img)
    # increspature d'inchiostro in mare, parallele alla costa
    a = np.zeros((MH, MW), np.float32)
    for dist, al in ((16, 0.55), (38, 0.40), (66, 0.28), (100, 0.16)):
        a = np.maximum(a, np.clip(1 - np.abs(d_out - dist) / 2.2, 0, 1) * al * (~land))
    # costa: tratto d'inchiostro
    a = np.maximum(a, np.clip(1 - np.abs(d_in - 2.5) / 3.0, 0, 1) * 0.95 * land)
    ink = np.array(INK, np.float32)
    img = img * (1 - a[..., None]) + ink * a[..., None]
    img *= (1 + 0.05 * stain[..., None])
    img += grain[..., None] * 3.0
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), 'RGB').convert('RGBA')
    np.save(os.path.join(CACHE, 'land.npy'), np.packbits(land))
    im.save(p)
    return im


def land_mask():
    return np.unpackbits(np.load(os.path.join(CACHE, 'land.npy')))[:MH * MW].reshape(MH, MW).astype(bool)


# ------------------------------------------------------------------ decorazioni (SVG su tutto il foglio)
def compass(cx, cy, r):
    o = f'<g transform="translate({cx} {cy})" opacity="0.92">'
    o += f'<circle r="{r}" fill="#F3E6C4" stroke="#3A281A" stroke-width="5"/><circle r="{r * 0.84:.0f}" fill="none" stroke="#3A281A" stroke-width="2.5"/>'
    o += ''.join(f'<line x1="0" y1="{-r * 0.84:.0f}" x2="0" y2="{-r:.0f}" stroke="#3A281A" stroke-width="3" transform="rotate({a})"/>' for a in range(0, 360, 15))
    for a, L, col in ((45, 0.62, '#C08A3E'), (135, 0.62, '#C08A3E'), (225, 0.62, '#C08A3E'), (315, 0.62, '#C08A3E'), (0, 0.95, '#B3261E'), (90, 0.95, '#2A1E16'), (180, 0.95, '#2A1E16'), (270, 0.95, '#2A1E16')):
        w = r * 0.14
        o += (f'<g transform="rotate({a})"><path d="M0 {-r * L:.0f} L{w:.0f} 0 L0 0 Z" fill="{col}" stroke="#3A281A" stroke-width="2.5"/>'
              f'<path d="M0 {-r * L:.0f} L{-w:.0f} 0 L0 0 Z" fill="#F7F0E0" stroke="#3A281A" stroke-width="2.5"/></g>')
    o += f'<circle r="{r * 0.09:.0f}" fill="#E3B657" stroke="#3A281A" stroke-width="3"/>'
    o += f'<text x="0" y="{-r - 14:.0f}" font-family="Lora" font-weight="700" font-size="{r * 0.3:.0f}" text-anchor="middle" fill="#3A281A">N</text></g>'
    return o


def ship(cx, cy, s, flip=False):
    sc = f'scale({-s if flip else s} {s})'
    return (f'<g transform="translate({cx} {cy}) {sc}">'
            '<path d="M-110 10 Q0 70 120 10 L100 50 Q0 80 -96 50 Z" fill="#7A4A26" stroke="#2A1E16" stroke-width="6" stroke-linejoin="round"/>'
            '<line x1="0" y1="14" x2="0" y2="-170" stroke="#2A1E16" stroke-width="8"/><line x1="-60" y1="10" x2="-60" y2="-110" stroke="#2A1E16" stroke-width="7"/>'
            '<path d="M6 -160 Q80 -110 6 -30 Z" fill="#F7F0E0" stroke="#2A1E16" stroke-width="5"/><path d="M-6 -150 Q-70 -110 -6 -40 Z" fill="#F3E6C4" stroke="#2A1E16" stroke-width="5"/>'
            '<path d="M-56 -104 Q-10 -80 -56 -20 Z" fill="#F7F0E0" stroke="#2A1E16" stroke-width="5"/>'
            '<path d="M0 -172 l40 10 l-40 10 Z" fill="#B3261E" stroke="#2A1E16" stroke-width="4"/>'
            '<path d="M-150 66 q20 -12 40 0 t40 0 M60 74 q20 -12 40 0 t40 0" fill="none" stroke="#3A281A" stroke-width="5" stroke-linecap="round"/></g>')


def serpent(cx, cy, s):
    return (f'<g transform="translate({cx} {cy}) scale({s})">'
            '<path d="M-200 30 q40 -90 80 0" fill="#2f8a83" stroke="#2A1E16" stroke-width="7"/><path d="M-60 30 q40 -110 80 0" fill="#2f8a83" stroke="#2A1E16" stroke-width="7"/>'
            '<path d="M80 30 q10 -120 70 -130 q50 0 60 40 q-10 30 -50 20 q-30 0 -30 70 Z" fill="#2f8a83" stroke="#2A1E16" stroke-width="7" stroke-linejoin="round"/>'
            '<circle cx="168" cy="-74" r="10" fill="#F7F0E0" stroke="#2A1E16" stroke-width="4"/><circle cx="170" cy="-74" r="4" fill="#2A1E16"/>'
            '<path d="M120 -98 l-10 -30 l24 18 l6 -30 l14 28" fill="#E3B657" stroke="#2A1E16" stroke-width="5" stroke-linejoin="round"/>'
            '<path d="M-230 40 q30 -14 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0" fill="none" stroke="#3A281A" stroke-width="5" stroke-linecap="round"/></g>')


def balloon(cx, cy, s):
    return (f'<g transform="translate({cx} {cy}) scale({s})">'
            '<path d="M0 -190 C110 -190 120 -70 40 0 L-40 0 C-120 -70 -110 -190 0 -190 Z" fill="#B3261E" stroke="#2A1E16" stroke-width="7"/>'
            '<path d="M0 -190 C40 -170 40 -60 18 0 L-18 0 C-40 -60 -40 -170 0 -190 Z" fill="#E3B657" stroke="#2A1E16" stroke-width="5"/>'
            '<line x1="-36" y1="0" x2="-24" y2="50" stroke="#2A1E16" stroke-width="5"/><line x1="36" y1="0" x2="24" y2="50" stroke="#2A1E16" stroke-width="5"/>'
            '<rect x="-30" y="50" width="60" height="44" rx="6" fill="#7A4A26" stroke="#2A1E16" stroke-width="6"/></g>')


def mountain(cx, cy, s):
    return (f'<g transform="translate({cx} {cy}) scale({s})" opacity="0.85"><path d="M-50 0 L0 -70 L50 0 Z" fill="#E6D3A3" stroke="#3A281A" stroke-width="4" stroke-linejoin="round"/>'
            '<path d="M0 -70 L14 0" stroke="#3A281A" stroke-width="3"/>'
            + ''.join(f'<line x1="{6 + i * 7}" y1="{-50 + i * 10}" x2="{14 + i * 7}" y2="{-50 + i * 10}" stroke="#3A281A" stroke-width="2.5"/>' for i in range(5)) + '</g>')


def tree(cx, cy, s):
    return (f'<g transform="translate({cx} {cy}) scale({s})" opacity="0.85"><line x1="0" y1="0" x2="0" y2="-26" stroke="#3A281A" stroke-width="4"/>'
            '<circle cx="0" cy="-40" r="20" fill="#9BB37A" stroke="#3A281A" stroke-width="4"/></g>')


def route_points():
    """La rotta: esce dallo strappo (dove la stagione 2 è finita, colonna di sinistra) e tocca i congegni in ordine."""
    start = T(19, 0, 300, TH - TEAR - 40)
    return [start] + [dev_center(n) for n in range(55, 82)]


def overlay_svg(names=True):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{MW}" height="{MH}">']
    # meridiani e paralleli, mai sulle giunture
    for x in range(270, MW, 540):
        p.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{MH}" stroke="#3A281A" stroke-opacity="0.16" stroke-width="3"/>')
    for y in range(EXT + 360, MH, 720):
        p.append(f'<line x1="0" y1="{y}" x2="{MW}" y2="{y}" stroke="#3A281A" stroke-opacity="0.16" stroke-width="3"/>')
    # montagne e alberi sparsi sulla terra (dove non ci sono adesivi: fasce laterali e basse)
    land = land_mask()
    rnd = random.Random(8)
    for _ in range(900):
        x, y = rnd.randrange(60, MW - 60), rnd.randrange(EXT, MH - EXT - TEAR)
        tx, ty = x % TW, (y - EXT) % TH
        if not (ty > 1220 or tx < 150 or tx > 930):
            continue
        if ty > 1390 or ty < 40 or tx < 40 or tx > 1040:
            continue
        rr, cc = 27 - (y - EXT) // TH, x // TW
        busy = (REGIONE.get(rr, (-1,))[0] == cc) or (DECOR.get(rr, (-1,))[0] == cc)
        if busy and ty > 1200:
            continue
        if land[y, x] and land[y - 60, x] and land[min(MH - 1, y + 20), x]:
            p.append(mountain(x, y, rnd.uniform(0.55, 0.85)) if rnd.random() < 0.55 else tree(x, y, rnd.uniform(0.6, 0.9)))
    # decorazioni nella fascia bassa
    for r, (c, kind) in DECOR.items():
        x, y = T(r, c, 540, BAND_Y)
        if kind == 'bussola':
            p.append(compass(x + 180, y, 108))
        elif kind == 'nave':
            p.append(ship(x - 180, y + 40, 0.7, flip=(r % 2 == 0)))
        elif kind == 'serpente':
            p.append(serpent(x - 40, y + 30, 0.75))
        else:
            p.append(balloon(x + 230, y + 30, 0.6))
    # nomi delle regioni, a mano, come sulle carte antiche
    for r, (c, name) in (REGIONE.items() if names else []):
        x, y = T(r, c, 540, BAND_Y + 30)
        size = 50 if len(name) < 16 else 44

    # la rotta rossa tratteggiata
    pts = route_points()
    d = f'M{pts[0][0]} {pts[0][1]}'
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if abs(y1 - y2) < 10:
            d += f' C{x1 + (x2 - x1) * 0.3:.0f} {y1 + 160} {x1 + (x2 - x1) * 0.7:.0f} {y2 + 160} {x2} {y2}'
        else:
            d += f' C{x1 - 520} {y1 - 640} {x2 + 520} {y2 + 640} {x2} {y2}'
    p.append(f'<path d="{d}" fill="none" stroke="#F7F0E0" stroke-opacity="0.7" stroke-width="24" stroke-linecap="round"/>')
    p.append(f'<path d="{d}" fill="none" stroke="{RO}" stroke-width="12" stroke-dasharray="30 22" stroke-linecap="round"/>')
    for r, (c, name) in (REGIONE.items() if names else []):
        x, y = T(r, c, 540, BAND_Y + 30)
        size = 50 if len(name) < 16 else 44
        p.append(f'<text x="{x}" y="{y}" font-family="Lora" font-style="italic" font-weight="600" font-size="{size}" letter-spacing="9" text-anchor="middle" fill="#3A281A" stroke="#EFE0B8" stroke-width="14" stroke-linejoin="round" paint-order="stroke">{name}</text>')
    p.append('</svg>')
    return ''.join(p)


# ------------------------------------------------------------------ adesivi della stagione 3
def stamp(text, col, w=118, h=140):
    """Francobollo con il bordo dentellato."""
    S = 2
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, w * S - 1, h * S - 1), fill=hexc('#FFFDF6'))
    rr = 7 * S
    for x in range(0, w * S + 1, 18 * S):
        d.ellipse((x - rr, -rr, x + rr, rr), fill=(0, 0, 0, 0)); d.ellipse((x - rr, h * S - rr, x + rr, h * S + rr), fill=(0, 0, 0, 0))
    for y in range(0, h * S + 1, 18 * S):
        d.ellipse((-rr, y - rr, rr, y + rr), fill=(0, 0, 0, 0)); d.ellipse((w * S - rr, y - rr, w * S + rr, y + rr), fill=(0, 0, 0, 0))
    d.rectangle((14 * S, 14 * S, (w - 14) * S, (h - 14) * S), fill=hexc(col), outline=hexc(DK), width=3 * S)
    d.text((w * S / 2, h * S / 2 + 4 * S), text, font=font(LORA, (52 if len(text) < 3 else 40) * S, 700), fill=hexc(CR), anchor='mm')
    return im.resize((w, h), Image.LANCZOS)


def title_tag(n, rot):
    """Etichetta da valigia: angoli smussati, occhiello d'ottone, cuciture, francobollo con il numero."""
    l1, l2 = TEMI[n]
    ped = n in PED
    S = 2
    w, h = 780, 246
    img = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    poly = [(70 * S, 0), (w * S, 0), (w * S, h * S), (70 * S, h * S), (0, h * S - 70 * S), (0, 70 * S)]
    d.polygon(poly, fill=hexc(TE if ped else CR))
    d.line(poly + [poly[0]], fill=hexc(DK), width=5 * S, joint='curve')
    inner = [(80 * S, 14 * S), (w * S - 14 * S, 14 * S), (w * S - 14 * S, h * S - 14 * S), (80 * S, h * S - 14 * S), (14 * S, h * S - 76 * S), (14 * S, 76 * S), (80 * S, 14 * S)]
    for (x1, y1), (x2, y2) in zip(inner, inner[1:]):
        L = math.hypot(x2 - x1, y2 - y1); k = 0
        while k < L:
            a, b = k / L, min(1, (k + 14 * S) / L)
            d.line((x1 + (x2 - x1) * a, y1 + (y2 - y1) * a, x1 + (x2 - x1) * b, y1 + (y2 - y1) * b), fill=hexc('#7FC4BC' if ped else '#C9B48A'), width=3 * S)
            k += 26 * S
    ex, ey = 58 * S, h * S / 2
    d.ellipse((ex - 26 * S, ey - 26 * S, ex + 26 * S, ey + 26 * S), fill=hexc(BR), outline=hexc(DK), width=4 * S)
    d.ellipse((ex - 11 * S, ey - 11 * S, ex + 11 * S, ey + 11 * S), fill=hexc('#3A281A'))
    size = 84
    while True:
        f = font(LORA, size * S, 700)
        if max(d.textlength(l1, font=f), d.textlength(l2, font=f)) <= 520 * S or size <= 54:
            break
        size -= 2
    cx = (100 + (w - 140)) / 2 * S
    d.text((cx, 88 * S), l1, font=f, fill=hexc(GO if ped else CU), anchor='mm')
    d.text((cx, 172 * S), l2, font=f, fill=hexc(CR if ped else DK), anchor='mm')
    img = img.resize((w, h), Image.LANCZOS)
    out = Image.new('RGBA', (w + 90, h + 60), (0, 0, 0, 0))
    out.alpha_composite(img, (0, 40))
    st = stamp(f'#{PED.index(n) + 1}' if ped else str(n), RO if ped else MU).rotate(7, resample=Image.BICUBIC, expand=True)
    out.alpha_composite(st, (w + 90 - st.width, 0))
    return sticker(out, 16, rot)


BRIEF = {56: ("fammi un'app", ('Per chi: io, ogni sera', 'Cosa fa: spunta le abitudini', 'Come appare: semplice, grande', 'Dove: sul telefono')),
         62: ('fammi un gioco', ('Che gioco: salti e monete', 'Comandi: tocco sullo schermo', 'Livelli: tre, sempre più difficili', 'Per chi: mio figlio, 8 anni')),
         68: ('fammi un grafico', ('Dati: spese di 12 mesi', 'Domanda: dove spendo di più?', 'Tipo: barre, dalla più alta', 'Dove va: in una mail')),
         74: ('fammi un documento', ('Per chi: i soci del circolo', 'Cosa: il programma dell’anno', 'Stile: caldo, con le foto', 'Formato: PDF di 8 pagine')),
         80: ('fammi un sito', ('Obiettivo: iscrizioni al torneo', 'Pagine: home, regole, iscriviti', 'Stile: colori della squadra', 'Passi: prima la bozza, poi i dettagli'))}


def postcard(n):
    """Cartolina della rubrica: a sinistra la richiesta vaga (PRIMA), a destra quella fatta bene (DOPO)."""
    S = 2
    w, h = 820, 560
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * S - 1, h * S - 1), 14 * S, fill=hexc('#FFFDF6'), outline=hexc(DK), width=6 * S)
    # bordo "posta aerea" a strisce rosse e blu
    bw = 20 * S
    k = 0
    for x in range(-h * S, w * S + h * S, 26 * S):
        col = hexc(RO) if (k % 2 == 0) else hexc('#2E4A62'); k += 1
        poly = [(x, 0), (x + 13 * S, 0), (x + 13 * S - bw, bw), (x - bw, bw)]
        for dy in (0, h * S - bw):
            d.polygon([(px, py + dy) for px, py in poly], fill=col)
    for y in range(0, h * S, 26 * S):
        col = hexc(RO) if (k % 2 == 0) else hexc('#2E4A62'); k += 1
        for x0 in (0, w * S - bw):
            d.polygon([(x0, y), (x0 + bw, y + bw), (x0 + bw, y + bw + 13 * S), (x0, y + 13 * S)], fill=col)
    d.rounded_rectangle((bw, bw, w * S - bw, h * S - bw), 6 * S, fill=hexc('#FFFDF6'))
    d.rounded_rectangle((0, 0, w * S - 1, h * S - 1), 14 * S, outline=hexc(DK), width=6 * S)
    mid = w * S * 0.42
    d.line((mid, 60 * S, mid, h * S - 50 * S), fill=hexc('#C9B48A'), width=3 * S)
    vague, brief = BRIEF[n]
    fT = font(LORA, 52 * S, 700)
    d.text((mid / 2, 80 * S), 'PRIMA', font=fT, fill=hexc(RO), anchor='mm')
    d.text(((mid + w * S) / 2 - 95 * S, 80 * S), 'DOPO', font=fT, fill=hexc(TE), anchor='mm')
    # prima: fumetto con la richiesta vaga e il punto interrogativo
    bx0, by0, bx1, by1 = 50 * S, 150 * S, mid - 40 * S, 290 * S
    d.rounded_rectangle((bx0, by0, bx1, by1), 30 * S, fill=hexc('#F3E9D2'), outline=hexc(DK), width=4 * S)
    d.polygon([(bx0 + 50 * S, by1 - 2 * S), (bx0 + 30 * S, by1 + 40 * S), (bx0 + 100 * S, by1 - 2 * S)], fill=hexc('#F3E9D2'))
    d.line([(bx0 + 50 * S, by1), (bx0 + 30 * S, by1 + 40 * S), (bx0 + 100 * S, by1)], fill=hexc(DK), width=4 * S)
    fv = font(LORA_I, 40 * S, 600)
    while d.textlength(f'«{vague}»', font=fv) > (bx1 - bx0 - 30 * S):
        fv = font(LORA_I, int(fv.size / S) * S - 2 * S, 600)
    d.text(((bx0 + bx1) / 2, (by0 + by1) / 2), f'«{vague}»', font=fv, fill=hexc(DK), anchor='mm')
    d.text((mid / 2 + 30 * S, 410 * S), '?', font=font(LORA, 150 * S, 700), fill=hexc(RO), anchor='mm')
    # dopo: la scheda con le quattro voci e la spunta
    fs = 25
    while max(d.textlength(l, font=font(INTER_B, fs * S)) for l in brief) > (w * S - bw - 20 * S) - (mid + 74 * S):
        fs -= 1
    fb = font(INTER_B, fs * S)
    y = 160 * S
    for line in brief:
        d.ellipse((mid + 40 * S, y - 9 * S, mid + 58 * S, y + 9 * S), fill=hexc(TE))
        d.text((mid + 74 * S, y), line, font=fb, fill=hexc(DK), anchor='lm')
        y += 74 * S
    cx, cy = w * S - 110 * S, h * S - 100 * S
    d.ellipse((cx - 56 * S, cy - 56 * S, cx + 56 * S, cy + 56 * S), fill=hexc(TE), outline=hexc(DK), width=5 * S)
    d.line([(cx - 26 * S, cy + 2 * S), (cx - 6 * S, cy + 24 * S), (cx + 30 * S, cy - 22 * S)], fill=(255, 255, 255, 255), width=14 * S, joint='curve')
    im = im.resize((w, h), Image.LANCZOS)
    # francobollo con l'annullo
    out = Image.new('RGBA', (w + 60, h + 60), (0, 0, 0, 0)); out.alpha_composite(im, (0, 60))
    st = stamp(f'N.{PED.index(n) + 1}', '#2E4A62', 128, 150).rotate(-6, resample=Image.BICUBIC, expand=True)
    out.alpha_composite(st, (w + 60 - st.width - 6, 0))
    do = ImageDraw.Draw(out)
    px, py = w - 130, 120
    do.ellipse((px - 64, py - 64, px + 64, py + 64), outline=(58, 40, 26, 190), width=5)
    do.ellipse((px - 52, py - 52, px + 52, py + 52), outline=(58, 40, 26, 150), width=2)
    do.text((px, py - 14), 'PRIMA', font=font(INTER_B, 22), fill=(58, 40, 26, 210), anchor='mm')
    do.text((px, py + 14), 'E DOPO', font=font(INTER_B, 22), fill=(58, 40, 26, 210), anchor='mm')
    for i in range(3):
        yy = py - 20 + i * 20
        do.line([(px + 64 + k * 8, yy + 6 * math.sin(k / 2)) for k in range(0, 14)], fill=(58, 40, 26, 170), width=4)
    return out


def device_img(n, size):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500" viewBox="0 0 500 500">{DEV[n]}</svg>'
    p = os.path.join(CACHE, f'dev{n}_{size}.png')
    if not os.path.exists(p):
        render(svg, p, size / 500)
    im = Image.open(p).convert('RGBA')
    return im.crop(im.getbbox())


def label_tape(canvas, box, rnd):
    """Due pezzi di nastro di carta sugli angoli (dentro la tessera)."""
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(canvas, 'RGBA')
    for (cx, cy, a) in rnd.sample([(x0 + 64, y0 + 64, -40), (x1 - 64, y0 + 64, 40), (x0 + 64, y1 - 64, 40), (x1 - 64, y1 - 64, -40)], 2):
        w, h = 150, 46
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        poly = [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2))]
        d.polygon(poly, fill=(236, 226, 196, 210), outline=(190, 170, 130, 255))


# ------------------------------------------------------------------ passaggio dalla stagione 2
def season_seam(canvas):
    """Sotto lo strappo si vede la cima vera della stagione 2 (stesso foglio, perfettamente allineato)."""
    yb = row_y(19) + TH                    # fondo della riga 19 = cima della riga 18
    s2 = Image.open(S2_MASTER).convert('RGBA').crop((0, 0, MW, 2 * EXT))   # in S2 la riga 18 comincia a y = EXT
    under = Image.new('RGBA', (MW, MH), (0, 0, 0, 0))
    under.alpha_composite(s2, (0, yb - EXT))
    rnd = random.Random(4)
    pts, x = [], 0
    while x <= MW:
        pts.append((x, yb - TEAR + rnd.randint(-20, 20) + int(16 * math.sin(x / 150 + 1))))
        x += rnd.randint(18, 40)
    mask = Image.new('L', (MW, MH), 255)
    ImageDraw.Draw(mask).polygon(pts + [(MW, MH), (0, MH)], fill=0)
    fib = Image.new('RGBA', (MW, MH), (0, 0, 0, 0)); ImageDraw.Draw(fib).line(pts, fill=hexc('#FBF3DE'), width=14)
    sh = Image.new('RGBA', (MW, MH), (0, 0, 0, 0)); ImageDraw.Draw(sh).line([(x, y + 12) for x, y in pts], fill=(42, 30, 22, 90), width=18)
    sh = sh.filter(ImageFilter.GaussianBlur(8))
    paper = canvas.copy(); paper.putalpha(mask)
    out = under; out.alpha_composite(sh); out.alpha_composite(paper); out.alpha_composite(fib)
    return out


def ribbon():
    """Cartiglio "STAGIONE 3" con le code ripiegate."""
    S = 2
    w, h = 700, 150
    im = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for side in (0, 1):
        x0 = 0 if side == 0 else w * S - 130 * S
        tail = [(x0, 40 * S), (x0 + 130 * S, 40 * S), (x0 + 130 * S, h * S), (x0, h * S)] if True else []
        notch = (x0 + 40 * S) if side == 0 else (x0 + 90 * S)
        poly = ([(x0, 40 * S), (x0 + 130 * S, 40 * S), (x0 + 130 * S, h * S), (x0, h * S), (notch, (40 + h) / 2 * S)] if side == 0
                else [(x0, 40 * S), (x0 + 130 * S, 40 * S), (notch, (40 + h) / 2 * S), (x0 + 130 * S, h * S), (x0, h * S)])
        d.polygon(poly, fill=hexc('#8C1C16'), outline=hexc(DK))
        d.line(poly + [poly[0]], fill=hexc(DK), width=4 * S)
    body = [(70 * S, 0), (w * S - 70 * S, 0), (w * S - 70 * S, 110 * S), (70 * S, 110 * S)]
    d.polygon(body, fill=hexc(RO)); d.line(body + [body[0]], fill=hexc(DK), width=5 * S)
    d.text((w * S / 2, 56 * S), 'STAGIONE 3', font=font(LORA, 70 * S, 700), fill=hexc(CR), anchor='mm')
    return im.resize((w, h), Image.LANCZOS)


# ------------------------------------------------------------------ composizione
def build():
    rnd = random.Random(21)
    canvas = map_base().copy()
    base = canvas.copy()
    ov = os.path.join(CACHE, 'overlay.png'); render(overlay_svg(), ov)
    canvas.alpha_composite(Image.open(ov).convert('RGBA'))
    canvas = season_seam(canvas)
    ov2 = os.path.join(CACHE, 'overlay_vuoto.png'); render(overlay_svg(False), ov2)
    base.alpha_composite(Image.open(ov2).convert('RGBA'))
    vuoto = season_seam(base)
    boxes = {}
    for n in range(55, 82):
        r, c = post_pos(n)
        x0, y0 = col_x(c), row_y(r)
        e = EDWIN[r]
        if e[0] == c:
            pose, rot = e[1], e[2]
            ed = G2.edwin_img(pose, 2.1 if pose == 'testa' else 1.18)
            bottom = 1230 if pose == 'testa' else (1150 if r == 19 else 1370)
            top_lim = 445
            st = sticker(ed, 20, rot)
            if st.height > bottom - top_lim:
                k = (bottom - top_lim) / st.height
                ed = ed.resize((int(ed.width * k), int(ed.height * k)), Image.LANCZOS)
                st = sticker(ed, 20, rot)
            ex = x0 + 540 + (-70 if pose == 'indica' else 60 if pose == 'saluta' else -80 if pose == 'testa' else 0)
            boxes[n, 'edwin'] = place(canvas, st, ex, y0 + bottom - st.height / 2)
            size = {'saluta': 360, 'regge': 380, 'indica': 360, 'testa': 400}[pose]
            boxes[n, 'dev'] = place(canvas, sticker(device_img(n, size), 18, rnd.uniform(-8, 8)), *dev_center(n))
        elif n in PED:
            pc = postcard(n)
            boxes[n, 'dev'] = place(canvas, sticker(pc, 18, rnd.uniform(-3, 3)), *dev_center(n))
        else:
            size = 590 if r == 19 else 640
            boxes[n, 'dev'] = place(canvas, sticker(device_img(n, size), 20, rnd.uniform(-5, 5)), *dev_center(n))
            if n % 2 == 1:
                label_tape(canvas, boxes[n, 'dev'], rnd)
        boxes[n, 'title'] = place(canvas, title_tag(n, rnd.uniform(-2.2, 2.2)), x0 + 540, y0 + 232)
    # cartiglio della stagione 3, appuntato sullo strappo
    yb = row_y(19) + TH
    b = ribbon()
    bx, by = col_x(1) + 540, yb - 112
    place(canvas, sticker(b, 14, -2), bx, by)
    dd = ImageDraw.Draw(canvas)
    for tx in (bx - 250, bx + 250):
        dd.ellipse((tx - 16, by - 70, tx + 16, by - 38), fill=hexc(GO), outline=hexc(DK), width=4)
    vuoto.save(os.path.join(OUT, 'master_vuoto.png'))
    canvas.save(os.path.join(OUT, 'master.png'))
    return canvas, boxes


def covers(canvas):
    os.makedirs(os.path.join(OUT, 'copertine'), exist_ok=True)
    for n in range(55, 82):
        r, c = post_pos(n)
        y0 = row_y(r) - EXT
        canvas.crop((col_x(c), y0, col_x(c) + TW, y0 + 1920)).convert('RGB').save(os.path.join(OUT, 'copertine', f'reel{n}_copertina.png'))


def preview(canvas, scale=0.25, name='griglia_stagione3.png'):
    """Come su Instagram: tessere 3:4 con la linea bianca, e sotto la riga 18 vera."""
    tw, th, g = int(TW * scale), int(TH * scale), 4
    s2 = Image.open(S2_MASTER).convert('RGB')
    im = Image.new('RGB', (3 * tw + 2 * g, 10 * th + 9 * g), 'white')
    for i, r in enumerate(range(27, 18, -1)):
        for c in range(3):
            t = canvas.crop((col_x(c), row_y(r), col_x(c) + TW, row_y(r) + TH)).convert('RGB').resize((tw, th), Image.LANCZOS)
            im.paste(t, (c * (tw + g), i * (th + g)))
    for c in range(3):
        t = s2.crop((col_x(c), EXT, col_x(c) + TW, EXT + TH)).resize((tw, th), Image.LANCZOS)
        im.paste(t, (c * (tw + g), 9 * (th + g)))
    im.save(os.path.join(OUT, name))


if __name__ == '__main__':
    cv, boxes = build()
    covers(cv)
    preview(cv)
    import json
    json.dump({f'{k[0]}_{k[1]}': v for k, v in boxes.items()}, open(os.path.join(OUT, 'boxes.json'), 'w'))
    print('ok')
