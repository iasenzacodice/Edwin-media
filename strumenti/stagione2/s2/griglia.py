"""Stagione 2 (righe 10-18): collage "taccuino dell'inventore".
Disegna l'intera griglia come un unico foglio (3 colonne x 9 righe, tessere 1080x1440 come la griglia Instagram 3:4),
poi ritaglia le copertine 1080x1920 di ogni Reel (la tessera al centro, 240 px delle righe vicine sopra e sotto).

Uso: python3 s2/griglia.py [uscita_dir]
"""
import sys, os, math, glob, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from temi import DEV, TEMI
from edwin_svg import head_svg, body_svg, render, gear as gear_svg

TW, TH, EXT = 1080, 1440, 240
MW, MH = 3 * TW, EXT + 9 * TH + EXT
DK, CR, PAPER = '#2A1E16', '#F7F0E0', '#EFE3C8'
TE, MU, CU, BR, GO, RO, BW = '#2f8a83', '#DCA24A', '#B45A30', '#C08A3E', '#E3B657', '#B3261E', '#5A341C'
LORA = '/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'
INTER_B = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
OUT = sys.argv[1] if (__name__ == '__main__' and len(sys.argv) > 1) else os.path.join(os.path.dirname(HERE), 'out_s2')
CACHE = os.path.join(OUT, 'cache'); os.makedirs(CACHE, exist_ok=True)
R9 = '/home/claude/edwin-media/media/riga9'


def row_y(r):            # bordo alto della tessera della riga r
    return EXT + (18 - r) * TH


def col_x(c):
    return c * TW


def post_pos(n):         # congegno -> (riga, colonna); in ogni riga esce prima la destra, poi il centro, poi la sinistra
    r = 10 + (n - 28) // 3
    return r, 2 - (n - 28) % 3


# Edwin: una tessera per riga (a zig-zag), posa diversa ogni volta
EDWIN = {10: (2, 'saluta', -3), 11: (1, 'regge', 2), 12: (0, 'indica', -2), 13: (2, 'testa', 6), 14: (1, 'regge', -3),
         15: (0, 'indica', 3), 16: (2, 'regge', -2), 17: (1, 'saluta', 3), 18: (0, 'testa', -6)}


def hexc(c, a=255):
    c = c.lstrip('#'); return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), a)


def font(path, size, weight=None):
    f = ImageFont.truetype(path, size)
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def svg_img(svg, name, scale=1.0):
    p = os.path.join(CACHE, name)
    if not os.path.exists(p):
        render(svg, p, scale)
    return Image.open(p).convert('RGBA')


# ------------------------------------------------------------------ adesivi
def sticker(img, border=20, rot=0.0, shadow=True):
    """Bordo crema spesso + ombra morbida, poi rotazione."""
    pad = border + 40
    big = Image.new('RGBA', (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    big.alpha_composite(img, (pad, pad))
    a = big.split()[3]
    grown = a.filter(ImageFilter.GaussianBlur(border * 0.55)).point(lambda v: 255 if v > 18 else 0)
    grown = grown.filter(ImageFilter.GaussianBlur(1.2))
    out = Image.new('RGBA', big.size, (0, 0, 0, 0))
    if shadow:
        sh = Image.new('RGBA', big.size, (42, 30, 22, 0)); sh.putalpha(grown.point(lambda v: int(v * 0.42)))
        sh = sh.filter(ImageFilter.GaussianBlur(14))
        out.alpha_composite(sh, (10, 16))
    edge = Image.new('RGBA', big.size, hexc(CR)); edge.putalpha(grown)
    out.alpha_composite(edge)
    out.alpha_composite(big)
    if rot:
        out = out.rotate(rot, resample=Image.BICUBIC, expand=True)
    return out


def place(canvas, st, cx, cy):
    canvas.alpha_composite(st, (int(cx - st.width / 2), int(cy - st.height / 2)))
    return (int(cx - st.width / 2), int(cy - st.height / 2), int(cx + st.width / 2), int(cy + st.height / 2))


def device_img(n, size):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500" viewBox="0 0 500 500">{DEV[n]}</svg>'
    im = svg_img(svg, f'dev{n}_{size}.png', size / 500)
    bb = im.getbbox()
    return im.crop(bb)


def edwin_img(pose, scale=1.0):
    if pose == 'testa':
        return svg_img(head_svg(0.15, 'happy' if scale > 1.5 else 'open'), f'ed_testa_{scale}.png', 0.87 * scale)
    b = svg_img(body_svg(pose=pose, arm=0.5), f'ed_b_{pose}_{scale}.png', 0.76 * scale)
    h = svg_img(head_svg(0.12, 'open'), f'ed_h_{scale}.png', 0.87 * scale)
    W = max(b.width, h.width)
    hy = int(0.76 * scale * 170) - h.height + int(0.76 * scale * 48)
    top = min(0, hy)
    im = Image.new('RGBA', (W, b.height - top), (0, 0, 0, 0))
    im.alpha_composite(b, ((W - b.width) // 2, -top))
    im.alpha_composite(h, ((W - h.width) // 2, hy - top))
    return im.crop(im.getbbox())


def title_card(n, rot):
    l1, l2 = TEMI[n]
    S = 2
    w, h = 760, 270
    img = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, w * S - 1, h * S - 1), 18 * S, fill=hexc(CR), outline=hexc(DK), width=5 * S)
    d.rounded_rectangle((12 * S, 12 * S, w * S - 12 * S, h * S - 12 * S), 12 * S, outline=hexc('#D9C7A0'), width=3 * S)
    size = 88
    while True:
        f = font(LORA, size * S, 700)
        if max(d.textlength(l1, font=f), d.textlength(l2, font=f)) <= 590 * S or size <= 56:
            break
        size -= 2
    d.text((w * S / 2 + 26 * S, 98 * S), l1, font=f, fill=hexc(CU), anchor='mm')
    d.text((w * S / 2 + 26 * S, 192 * S), l2, font=f, fill=hexc(DK), anchor='mm')
    img = img.resize((w, h), Image.LANCZOS)
    # numero nel tondo d'ottone, a cavallo dell'angolo
    out = Image.new('RGBA', (w + 60, h + 60), (0, 0, 0, 0))
    out.alpha_composite(img, (30, 30))
    dn = ImageDraw.Draw(out)
    dn.ellipse((0, 0, 124, 124), fill=hexc(BR), outline=hexc(DK), width=5)
    dn.ellipse((14, 14, 110, 110), fill=hexc(GO))
    dn.text((62, 64), str(n), font=font(LORA, 58, 700), fill=hexc(DK), anchor='mm')
    return sticker(out, 16, rot)


# ------------------------------------------------------------------ sfondo a fasce
SLOPE = -0.42           # le fasce salgono verso destra
BANDS = [(TE, 'ingranaggi'), (PAPER, 'griglia'), (MU, 'puntini'), (CU, 'righe'), ('#3A2A20', 'ingranaggi'), (PAPER, 'griglia'), (TE, 'puntini'), (MU, 'righe'), (CU, 'puntini')]
BAND_H = 1500


def background_svg():
    defs = f'''<defs>
<pattern id="p_griglia" width="54" height="54" patternUnits="userSpaceOnUse"><path d="M54 0 L0 0 0 54" fill="none" stroke="#000" stroke-opacity="0.07" stroke-width="2"/></pattern>
<pattern id="p_puntini" width="46" height="46" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="5" fill="#000" fill-opacity="0.09"/><circle cx="35" cy="35" r="5" fill="#000" fill-opacity="0.09"/></pattern>
<pattern id="p_righe" width="40" height="40" patternUnits="userSpaceOnUse" patternTransform="rotate(-30)"><rect width="40" height="12" fill="#000" fill-opacity="0.08"/></pattern>
<pattern id="p_ingranaggi" width="300" height="300" patternUnits="userSpaceOnUse">
 <g fill="none" stroke="#fff" stroke-opacity="0.10" stroke-width="10">{gear_ring(80, 80, 56, 10)}{gear_ring(220, 210, 40, 8)}</g></pattern>
</defs>'''
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{MW}" height="{MH}">', defs]
    # fasce: y = SLOPE*x + c ; si parte da sotto e si sale
    c0 = MH + 1600
    i = 0
    c = c0
    while c > -MW * abs(SLOPE) - BAND_H:
        col, pat = BANDS[i % len(BANDS)]
        c2 = c - BAND_H
        pts = f'0,{c} {MW},{c + SLOPE * MW} {MW},{c2 + SLOPE * MW} 0,{c2}'
        parts.append(f'<polygon points="{pts}" fill="{col}"/><polygon points="{pts}" fill="url(#p_{pat})"/>')
        c = c2; i += 1
    parts.append('</svg>')
    return ''.join(parts)


def gear_ring(cx, cy, r, teeth):
    pts = []
    for k in range(teeth * 4):
        a = k * math.pi * 2 / (teeth * 4)
        rr = r if (k % 4) in (0, 1) else r * 0.8
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}"/><circle cx="{cx}" cy="{cy}" r="{r * 0.35:.1f}"/>'


# ------------------------------------------------------------------ raccordi
def dev_center(n):
    r, c = post_pos(n)
    e = EDWIN[r]
    x0, y0 = col_x(c), row_y(r)
    if e[0] == c:      # nella tessera di Edwin il congegno sta accanto a lui
        return x0 + DEV_IN_EDWIN[e[1]][0], y0 + DEV_IN_EDWIN[e[1]][1] - (60 if r == 10 else 0)
    return x0 + 540, y0 + (840 if r == 10 else 880)


DEV_IN_EDWIN = {'saluta': (320, 1090), 'regge': (540, 1110), 'indica': (800, 650), 'testa': (770, 1130)}


def P(r, c, tx, ty):
    return (col_x(c) + tx, row_y(r) + ty)


def smooth(pts):
    """Curva morbida (Catmull-Rom) che passa per tutti i punti."""
    d = f'M{pts[0][0]:.0f} {pts[0][1]:.0f}'
    for i in range(len(pts) - 1):
        p0 = pts[max(0, i - 1)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(len(pts) - 1, i + 2)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {p2[0]:.0f} {p2[1]:.0f}'
    return d


def wave(col, r_from, r_to, start_side=0):
    """Punti di un'onda dentro una colonna: in ogni riga passa dalla fascia bassa alla fascia sotto il titolo,
    alternando il lato, così il filo serpeggia dietro gli adesivi e non corre mai sulle giunture."""
    pts, side = [], start_side
    for r in range(r_from, r_to + 1):
        pts.append(P(r, col, (230, 850)[side], 1260))
        side = 1 - side
        pts.append(P(r, col, (230, 850)[side], 490))
    return pts


# percorsi dei raccordi lunghi (calcolati una volta, usati sotto e sopra gli adesivi)
def long_routes():
    A = [dev_center(28), P(10, 2, 120, 560)] + wave(2, 11, 13, 1) + [P(14, 2, 850, 1260), dev_center(40)]
    B = [dev_center(34), P(12, 1, 850, 1150)] + wave(1, 13, 15, 0) + [P(16, 2, 180, 1250), dev_center(46)]
    C = [dev_center(38), P(13, 0, 850, 1250)] + wave(0, 14, 17, 0) + [dev_center(54)]
    return {'A': A, 'B': B, 'C': C}


def connectors_under():
    """Linea tratteggiata dei congegni e i tre fili lunghi: passano dietro gli adesivi."""
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{MW}" height="{MH}">']
    pts = [dev_center(n) for n in range(28, 55)]
    d = f'M{pts[0][0]} {pts[0][1]}'
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if y1 == y2:
            d += f' L{x2} {y2}'
        else:
            d += f' C{x1 - 500} {y1 - 700} {x2 + 500} {y2 + 700} {x2} {y2}'
    p.append(f'<path d="{d}" fill="none" stroke="{DK}" stroke-opacity="0.5" stroke-width="10" stroke-dasharray="26 22" stroke-linecap="round"/>')
    R = long_routes()
    p.append(cable(smooth(R['A']), CU))          # filo di rame: documento (28) -> file collegati (40)
    p.append(hose(smooth(R['B'])))               # tubo flessibile d'ottone: ricerca (34) -> studiare (46)
    p.append(cable(smooth(R['C']), TE))          # filo verde: skill (38) -> primo progetto (54)
    p.append('</svg>')
    return ''.join(p)


def cable(d, col):
    return (f'<path d="{d}" fill="none" stroke="{DK}" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-opacity="0.28" stroke-width="5" stroke-linecap="round" transform="translate(-4 -4)"/>')


def hose(d):
    """Tubo flessibile d'ottone a soffietto."""
    return (f'<path d="{d}" fill="none" stroke="{DK}" stroke-width="50" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{BR}" stroke-width="38" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#8A5E22" stroke-width="38" stroke-dasharray="6 16"/>'
            f'<path d="{d}" fill="none" stroke="{GO}" stroke-opacity="0.7" stroke-width="9" transform="translate(-7 -7)"/>')


def connectors_over():
    """Sopra gli adesivi: manometro sul tubo e spine alle estremità dei fili (in zone libere, mai sulle giunture)."""
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{MW}" height="{MH}">']
    R = long_routes()
    # manometro sul tubo, nella fascia libera sotto il titolo della riga 14 (colonna centrale)
    gx, gy = [q for q in R['B'] if q[1] == row_y(14) + 490][0]
    p.append(f'<circle cx="{gx}" cy="{gy}" r="74" fill="{BR}" stroke="{DK}" stroke-width="8"/><circle cx="{gx}" cy="{gy}" r="55" fill="{CR}" stroke="{DK}" stroke-width="5"/>'
             + ''.join(f'<line x1="{gx}" y1="{gy - 48}" x2="{gx}" y2="{gy - 37}" stroke="{DK}" stroke-width="5" transform="rotate({a} {gx} {gy})"/>' for a in range(-120, 121, 40))
             + f'<line x1="{gx}" y1="{gy}" x2="{gx + 34}" y2="{gy - 28}" stroke="{RO}" stroke-width="7" stroke-linecap="round"/><circle cx="{gx}" cy="{gy}" r="8" fill="{DK}"/>')
    # valvola sul tubo, nella fascia bassa della riga 13 (colonna centrale)
    vx, vy = R['B'][2]
    p.append(f'<circle cx="{vx}" cy="{vy}" r="46" fill="none" stroke="{DK}" stroke-width="20"/><circle cx="{vx}" cy="{vy}" r="46" fill="none" stroke="{RO}" stroke-width="10"/>'
             + ''.join(f'<line x1="{vx}" y1="{vy}" x2="{vx + 46 * math.cos(a * math.pi / 2 + 0.4):.0f}" y2="{vy + 46 * math.sin(a * math.pi / 2 + 0.4):.0f}" stroke="{RO}" stroke-width="10"/>' for a in range(4))
             + f'<circle cx="{vx}" cy="{vy}" r="14" fill="{DK}"/>')
    p.append('</svg>')
    return ''.join(p)


def tape(canvas, box, rnd):
    """Due pezzi di nastro adesivo sugli angoli di un adesivo (dentro la casella)."""
    x0, y0, x1, y1 = box
    d = ImageDraw.Draw(canvas, 'RGBA')
    for (cx, cy, a) in rnd.sample([(x0 + 60, y0 + 60, -40), (x1 - 60, y0 + 60, 40), (x0 + 60, y1 - 60, 40), (x1 - 60, y1 - 60, -40)], 2):
        w, h = 150, 46
        pts = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        poly = [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in pts]
        d.polygon(poly, fill=(243, 227, 184, 205), outline=(201, 179, 138, 255))


# ------------------------------------------------------------------ passaggio dalla stagione 1
def season_seam(canvas):
    """In basso: la vera cima della riga 9; in fondo alla riga 10 la carta si strappa e si vede lo stesso cielo."""
    y9 = row_y(10) + TH
    for c, f in enumerate(('carosello27_tiktok_copertina.png', 'carosello26_tiktok_copertina.png', 'reel25_copertina.png')):
        im = Image.open(os.path.join(R9, f)).convert('RGBA')
        canvas.alpha_composite(im.crop((0, 240, 1080, 240 + EXT)), (col_x(c), y9))
        sky = im.crop((0, 0, 1080, 240))      # il cielo sopra la riga 9, già allineato al bordo
        canvas.alpha_composite(sky, (col_x(c), y9 - 240))
    # bordo strappato: maschera irregolare continua su tutta la larghezza
    rnd = random.Random(3)
    pts, x = [], 0
    while x <= MW:
        pts.append((x, y9 - 205 + rnd.randint(-22, 22) + int(18 * math.sin(x / 140))))
        x += rnd.randint(18, 40)
    return pts


def tear_layers(pts):
    y9 = row_y(10) + TH
    mask = Image.new('L', (MW, MH), 255)
    d = ImageDraw.Draw(mask)
    d.polygon(pts + [(MW, y9), (0, y9)], fill=0)
    fib = Image.new('RGBA', (MW, MH), (0, 0, 0, 0)); df = ImageDraw.Draw(fib)
    df.line(pts, fill=hexc('#FBF6EA'), width=14)
    sh = Image.new('RGBA', (MW, MH), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    ds.line([(x, y + 12) for x, y in pts], fill=(42, 30, 22, 90), width=18)
    sh = sh.filter(ImageFilter.GaussianBlur(8))
    return mask, fib, sh


def banner():
    S = 2
    w, h = 640, 150
    img = Image.new('RGBA', (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.polygon([(0, 0), (w * S, 0), (w * S - 40 * S, h * S / 2), (w * S, h * S), (0, h * S), (40 * S, h * S / 2)], fill=hexc(RO), outline=hexc(DK))
    d.line([(0, 0), (w * S, 0), (w * S - 40 * S, h * S / 2), (w * S, h * S), (0, h * S), (40 * S, h * S / 2), (0, 0)], fill=hexc(DK), width=5 * S)
    d.text((w * S / 2, h * S / 2 + 4 * S), 'STAGIONE 2', font=font(LORA, 78 * S, 700), fill=hexc(CR), anchor='mm')
    return img.resize((w, h), Image.LANCZOS)


# ------------------------------------------------------------------ composizione
def build():
    rnd = random.Random(12)
    canvas = svg_img(background_svg(), 'bg.png').copy()
    pts = season_seam(canvas)
    under = svg_img(connectors_under(), 'under.png')
    canvas.alpha_composite(under)
    # strappo della carta: sopra il cielo vero della riga 9 tutto quello che è sotto la linea viene tolto
    mask, fib, sh = tear_layers(pts)
    sky = Image.new('RGBA', (MW, MH), (0, 0, 0, 0))
    y9 = row_y(10) + TH
    for c, f in enumerate(('carosello27_tiktok_copertina.png', 'carosello26_tiktok_copertina.png', 'reel25_copertina.png')):
        im = Image.open(os.path.join(R9, f)).convert('RGBA')
        sky.alpha_composite(im.crop((0, 0, 1080, 240)), (col_x(c), y9 - 240))
        sky.alpha_composite(im.crop((0, 240, 1080, 240 + EXT)), (col_x(c), y9))
    paper_part = canvas.copy(); paper_part.putalpha(mask)
    canvas = sky.copy(); canvas.alpha_composite(sh); canvas.alpha_composite(paper_part); canvas.alpha_composite(fib)

    boxes = {}
    for n in range(28, 55):
        r, c = post_pos(n)
        x0, y0 = col_x(c), row_y(r)
        e = EDWIN[r]
        if e[0] == c:
            pose, rot = e[1], e[2]
            ed = edwin_img(pose, 2.1 if pose == 'testa' else 1.18)
            bottom = 1230 if pose == 'testa' else (1215 if r == 10 else 1370)
            top_lim = 445                      # sotto il cartellino del titolo, con aria
            st = sticker(ed, 20, rot)
            if st.height > bottom - top_lim:
                k = (bottom - top_lim) / st.height
                ed = ed.resize((int(ed.width * k), int(ed.height * k)), Image.LANCZOS)
                st = sticker(ed, 20, rot)
            ey = y0 + bottom - st.height / 2
            ex = x0 + 540 + (-70 if pose == 'indica' else 60 if pose == 'saluta' else -80 if pose == 'testa' else 0)
            boxes[n, 'edwin'] = place(canvas, st, ex, ey)
            dx, dy = DEV_IN_EDWIN[pose]
            if r == 10:
                dy -= 60               # resta sopra lo strappo della carta
            size = {'saluta': 360, 'regge': 380, 'indica': 360, 'testa': 400}[pose]
            boxes[n, 'dev'] = place(canvas, sticker(device_img(n, size), 18, rnd.uniform(-8, 8)), x0 + dx, y0 + dy)
        else:
            size = 600 if r == 10 else 640
            boxes[n, 'dev'] = place(canvas, sticker(device_img(n, size), 20, rnd.uniform(-5, 5)), *dev_center(n))
            if n % 2 == 0:
                tape(canvas, boxes[n, 'dev'], rnd)
        boxes[n, 'title'] = place(canvas, title_card(n, rnd.uniform(-2.2, 2.2)), x0 + 540, y0 + 230)
    over = svg_img(connectors_over(), 'over.png')
    canvas.alpha_composite(over)
    # foglio senza adesivi (sfondo dei Reel): fasce, raccordi e strappo, senza titoli, congegni ed Edwin
    vuoto = sky.copy(); vuoto.alpha_composite(sh); vuoto.alpha_composite(paper_part); vuoto.alpha_composite(fib); vuoto.alpha_composite(over)
    vuoto.save(os.path.join(OUT, 'master_vuoto.png'))
    # striscione della stagione 2, appuntato sul bordo strappato con due chiodini d'ottone
    b = banner()
    bx, by = col_x(1) + 540, y9 - 110
    place(canvas, sticker(b, 14, -2), bx, by)
    dd = ImageDraw.Draw(canvas)
    for tx in (bx - 250, bx + 250):
        dd.ellipse((tx - 16, by - 70, tx + 16, by - 38), fill=hexc(GO), outline=hexc(DK), width=4)
    canvas.save(os.path.join(OUT, 'master.png'))
    return canvas, boxes


def covers(canvas):
    os.makedirs(os.path.join(OUT, 'copertine'), exist_ok=True)
    top_ext = canvas.crop((0, 0, MW, EXT))
    for n in range(28, 55):
        r, c = post_pos(n)
        y0 = row_y(r) - EXT
        cov = canvas.crop((col_x(c), y0, col_x(c) + TW, y0 + 1920)).convert('RGB')
        cov.save(os.path.join(OUT, 'copertine', f'reel{n}_copertina.png'))


def preview(canvas):
    """Anteprima della griglia come su Instagram: tessere 3:4 con la linea bianca tra le caselle, più la riga 9 sotto."""
    s = 0.25
    tw, th, g = int(TW * s), int(TH * s), 4
    rows = list(range(18, 9, -1))
    r9 = [Image.open(os.path.join(R9, f)).convert('RGB').crop((0, 240, 1080, 1680)) for f in ('carosello27_tiktok_copertina.png', 'carosello26_tiktok_copertina.png', 'reel25_copertina.png')]
    im = Image.new('RGB', (3 * tw + 2 * g, (len(rows) + 1) * th + len(rows) * g), 'white')
    for i, r in enumerate(rows):
        for c in range(3):
            t = canvas.crop((col_x(c), row_y(r), col_x(c) + TW, row_y(r) + TH)).convert('RGB').resize((tw, th), Image.LANCZOS)
            im.paste(t, (c * (tw + g), i * (th + g)))
    for c in range(3):
        im.paste(r9[c].resize((tw, th), Image.LANCZOS), (c * (tw + g), len(rows) * (th + g)))
    im.save(os.path.join(OUT, 'griglia_stagione2.png'))


if __name__ == '__main__':
    cv, boxes = build()
    covers(cv)
    preview(cv)
    import json
    json.dump({f'{k[0]}_{k[1]}': v for k, v in boxes.items()}, open(os.path.join(OUT, 'boxes.json'), 'w'))
    print('ok')
