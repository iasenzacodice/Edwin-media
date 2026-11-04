"""Reel stile "Edwin fa la cosa" (come i Reel già pubblicati): scenografia della riga, oggetti in mano,
pannelli che simulano la richiesta e la risposta, righe che compaiono, pulsanti "chiedimi ancora", timbri.

Uso: python3 reel2.py storie/s12.py uscita_dir
"""
import sys, os, math, re, subprocess, importlib.util, hashlib, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import reel_maker as R
from reel_maker import (W, H, FPS, SR, font, wrap, hexc, F_LORA, F_INTER, F_INTER_SB, F_INTER_B, F_MONO, F_MONO_B,
                        CREAM, ROSSO, svg_png, title_plate, subtitle, badge, scene_audio, wav_write, sfx_whoosh, sfx_tick, sfx_clank)
from edwin_svg import head_svg, body_svg, render, gear, CYAN, BRASS, COPPER, COPPER_D, BROWN, DARK, GOLD, GOLD_L

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
LORA_I = '/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'
DECK = 1470          # piano su cui poggia il busto di Edwin
RED, RED_D = '#C9302C', '#8E1F1C'


# ================================================================ scenografie
def lattice(x, y, w, h, col=RED, step=70, sw=10):
    out = [f'<rect x="{x}" y="{y}" width="{sw}" height="{h}" fill="{col}"/><rect x="{x + w - sw}" y="{y}" width="{sw}" height="{h}" fill="{col}"/>']
    yy = y
    while yy < y + h:
        out.append(f'<line x1="{x}" y1="{yy}" x2="{x + w}" y2="{yy + step}" stroke="{col}" stroke-width="{sw * 0.8}"/>')
        out.append(f'<rect x="{x}" y="{yy}" width="{w}" height="{sw * 0.8}" fill="{col}"/>')
        yy += step
    return ''.join(out)


def rivets(x0, y0, x1, y1, n, col=COPPER_D, r=6):
    return ''.join(f'<circle cx="{x0 + (x1 - x0) * i / (n - 1):.0f}" cy="{y0 + (y1 - y0) * i / (n - 1):.0f}" r="{r}" fill="{col}"/>' for i in range(n))


def paper(col='#EFE3C8', line='#E2D2AE'):
    g = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{line}" stroke-width="2"/>' for x in range(0, W + 1, 54))
    g += ''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{line}" stroke-width="2"/>' for y in range(0, H + 1, 54))
    return f'<rect width="{W}" height="{H}" fill="{col}"/>{g}'


def sky(top='#BFDCDD', bottom='#EEF2E6'):
    return (f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')


def cloud(x, y, s=1.0, op=0.9):
    return (f'<g transform="translate({x} {y}) scale({s})" opacity="{op}"><ellipse cx="0" cy="0" rx="90" ry="34" fill="#fff"/>'
            f'<ellipse cx="-50" cy="-16" rx="50" ry="36" fill="#fff"/><ellipse cx="40" cy="-26" rx="60" ry="44" fill="#fff"/></g>')


def railing(y=DECK, col='#3A2A1E', deck='#6E4122'):
    posts = ''.join(f'<rect x="{x}" y="{y - 130}" width="14" height="130" fill="{col}"/>' for x in range(60, W, 160))
    return (f'<rect x="0" y="{y - 132}" width="{W}" height="14" rx="7" fill="{col}"/>'
            f'<rect x="0" y="{y - 70}" width="{W}" height="9" fill="{col}"/>{posts}'
            f'<rect x="0" y="{y}" width="{W}" height="30" fill="{deck}"/><rect x="0" y="{y + 30}" width="{W}" height="8" fill="#2A1E16" opacity="0.5"/>')


def under(y=DECK + 38, col='#4A2C18'):
    return (f'<rect x="0" y="{y}" width="{W}" height="{H - y}" fill="{col}"/>'
            '<g opacity="0.35">' + ''.join(f'<line x1="0" y1="{yy}" x2="{W}" y2="{yy}" stroke="#1E140E" stroke-width="4"/>' for yy in range(y + 90, H, 120)) + '</g>')


def set_layers(kind, variant=''):
    """Restituisce (svg sfondo, svg primo piano) della scenografia della riga."""
    bg, fg = '', ''
    if kind == 'officina':           # riga 4: torre d'ottone, gru col gancio, banco da lavoro
        bg = paper() + f'''
<rect x="820" y="0" width="200" height="{H}" fill="{BRASS}"/><rect x="820" y="0" width="34" height="{H}" fill="{GOLD_L}" opacity="0.6"/>
{''.join(f'<rect x="812" y="{y}" width="216" height="22" fill="{COPPER}"/>' for y in (320, 820, 1320))}
{rivets(840, 360, 840, 1280, 9)}{rivets(1000, 360, 1000, 1280, 9)}
<g opacity="0.9">{gear(930, 1080, 120, 14, COPPER, hole='#EFE3C8', rot=10)}</g>
<line x1="170" y1="0" x2="170" y2="760" stroke="#2A1E16" stroke-width="6"/>
<path d="M170 760 v40 a36 36 0 1 1 -40 36" stroke="#5A341C" stroke-width="14" fill="none" stroke-linecap="round"/>
<g><path d="M110 1080 h120 l-20 -60 h-80 z" fill="#3A2A1E"/><ellipse cx="170" cy="1080" rx="64" ry="14" fill="#FFE9A8"/></g>
<line x1="170" y1="900" x2="170" y2="1020" stroke="#2A1E16" stroke-width="4"/>
<ellipse cx="170" cy="1250" rx="210" ry="180" fill="#FFF3C9" opacity="0.45"/>'''
        fg = f'''<rect x="0" y="{DECK}" width="{W}" height="36" fill="#8A5530"/><rect x="0" y="{DECK + 36}" width="{W}" height="{H - DECK - 36}" fill="#5A341C"/>
<rect x="0" y="{DECK + 36}" width="{W}" height="8" fill="#2A1E16" opacity="0.5"/>
<g opacity="0.3">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#2A1E16" stroke-width="3"/>' for y in (1640, 1760, 1880))}</g>'''
    elif kind == 'colosso':          # righe 5-7: passerella sul Colosso
        bg = sky()
        bg += cloud(200, 380, 1.1) + cloud(900, 260, 0.8, 0.8)
        if variant == 'torso':
            bg += f'''<path d="M-80 {H} L-80 700 Q260 560 560 640 Q760 700 820 900 L860 {H} Z" fill="#8C4A28"/>
<path d="M-80 760 Q260 620 560 700 Q740 750 800 920" stroke="{COPPER}" stroke-width="28" fill="none"/>
{rivets(40, 760, 760, 920, 12, '#5A2A14', 8)}
<circle cx="380" cy="1080" r="150" fill="{BRASS}"/><circle cx="380" cy="1080" r="112" fill="#2A1E16"/><circle cx="380" cy="1080" r="70" fill="{CYAN}" opacity="0.85"/>'''
        elif variant == 'braccio':
            bg += f'''<path d="M760 {H} L700 600 Q760 420 1180 380 L1180 {H} Z" fill="{BRASS}"/>
<path d="M700 600 Q760 420 1180 380" stroke="{GOLD_L}" stroke-width="26" fill="none"/>
{rivets(730, 640, 1060, 470, 8, COPPER_D, 8)}
<g>{gear(250, 980, 210, 16, COPPER, hole='#BFDCDD', rot=6)}</g>
'''
        else:  # testa
            bg += f'''<rect x="-40" y="420" width="760" height="1100" rx="160" fill="{BRASS}"/>
<rect x="40" y="520" width="600" height="110" rx="55" fill="#5A341C"/>
<circle cx="340" cy="960" r="200" fill="{COPPER}"/><circle cx="340" cy="960" r="150" fill="#2A1E16"/><circle cx="340" cy="960" r="100" fill="{CYAN}" opacity="0.9"/>
{rivets(20, 470, 660, 470, 10, COPPER_D, 9)}'''
        bg += lattice(930, 0, 110, H, RED, 90, 12)
        fg = railing(col='#3A2A1E', deck='#7A4A26') + under(col='#4A2C18')
    elif kind == 'gru':              # riga 8: braccio della gru rosso nel cielo
        def truss(x1, y1, x2, y2, h, n):
            import math as mm
            L = mm.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; nx, ny = -uy, ux
            top = [(x1 + ux * L * i / n + nx * h, y1 + uy * L * i / n + ny * h) for i in range(n + 1)]
            bot = [(x1 + ux * L * i / n, y1 + uy * L * i / n) for i in range(n + 1)]
            o = f'<line x1="{top[0][0]:.0f}" y1="{top[0][1]:.0f}" x2="{top[-1][0]:.0f}" y2="{top[-1][1]:.0f}" stroke="{RED}" stroke-width="16"/>'
            o += f'<line x1="{bot[0][0]:.0f}" y1="{bot[0][1]:.0f}" x2="{bot[-1][0]:.0f}" y2="{bot[-1][1]:.0f}" stroke="{RED}" stroke-width="16"/>'
            for i in range(n):
                a, b = (top[i], bot[i + 1]) if i % 2 == 0 else (bot[i], top[i + 1])
                o += f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" stroke="{RED}" stroke-width="10"/>'
                o += f'<line x1="{top[i][0]:.0f}" y1="{top[i][1]:.0f}" x2="{bot[i][0]:.0f}" y2="{bot[i][1]:.0f}" stroke="{RED}" stroke-width="8"/>'
            return o
        bg = sky('#B6D7DA', '#EEF2E6') + cloud(820, 1180, 1.0) + cloud(200, 1000, 0.8, 0.8)
        bg += truss(-60, 760, 1140, 300, 110, 12)
        bg += f'<line x1="990" y1="350" x2="990" y2="1150" stroke="#2A1E16" stroke-width="6"/><rect x="960" y="330" width="60" height="40" rx="8" fill="{RED_D}"/>'
        bg += f'<path d="M990 1150 v34 a32 32 0 1 1 -36 32" stroke="#5A341C" stroke-width="13" fill="none" stroke-linecap="round"/>'
        fg = railing(col=RED_D, deck='#7A4A26') + under(col='#3E2A1C')
    elif kind == 'dirigibile':       # riga 9: ponte della gondola del dirigibile E. ARC
        bg = sky('#AFD3E0', '#F1EFE4') + cloud(150, 1300, 1.2) + cloud(950, 1180, 0.9)
        bg += f'''<ellipse cx="540" cy="420" rx="760" ry="330" fill="#D9A04A"/>
<ellipse cx="540" cy="380" rx="700" ry="250" fill="#E8B95C" opacity="0.6"/>
{''.join(f'<path d="M{x} 100 Q{x + 40} 420 {x} 740" stroke="#B9802F" stroke-width="6" fill="none"/>' for x in range(-80, 1200, 170))}
<text x="800" y="712" font-family="Lora" font-weight="700" font-size="120" fill="#5A341C">E.</text>
{''.join(f'<line x1="{x}" y1="700" x2="{x + (540 - x) * 0.1:.0f}" y2="1220" stroke="#5A341C" stroke-width="5"/>' for x in (120, 400, 680, 960))}'''
        fg = f'''<path d="M-40 {DECK - 140} L{W + 40} {DECK - 140} L{W - 40} {H} L40 {H} Z" fill="#6B3E1F"/>
<rect x="-40" y="{DECK - 150}" width="{W + 80}" height="26" rx="13" fill="{BRASS}"/>
{''.join(f'<circle cx="{x}" cy="{DECK - 40}" r="34" fill="#BFDCDD" stroke="{BRASS}" stroke-width="10"/>' for x in (150, 930))}
{rivets(40, DECK + 60, 1040, DECK + 60, 14, '#3A2214', 7)}
<g opacity="0.3">{''.join(f'<line x1="40" y1="{y}" x2="{W - 40}" y2="{y}" stroke="#2A1E16" stroke-width="3"/>' for y in (1660, 1780))}</g>'''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{bg}</svg>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{fg}</svg>')


# ================================================================ pannelli (stile Reel pubblicati)
PX0, PX1, PY0 = 80, 1000, 262


def check_icon(d, x, y, r, on=True):
    d.ellipse((x - r, y - r, x + r, y + r), fill=hexc(COPPER if on else '#D9C7A0'))
    d.line((x - r * 0.45, y, x - r * 0.1, y + r * 0.38, x + r * 0.5, y - r * 0.38), fill=(255, 255, 255, 255), width=max(2, int(r * 0.28)), joint='curve')


def panel(blocks, prog=99.0, cache={}):
    """prog = secondi dall'inizio della scena: governa scrittura a macchina, righe che compaiono, pulsante premuto."""
    S = 2
    pw = (PX1 - PX0) * S
    inner = pw - 96 * S
    dm = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    L = 48 * S
    items, y = [], 40 * S
    for b in blocks:
        k = b[0]
        if k == 'label':
            items.append((k, y, b[1], b[2] if len(b) > 2 else None)); y += 58 * S
        elif k == 'title':
            f = font(F_LORA, 54 * S, 700); ls = wrap(dm, b[1], f, inner)
            items.append((k, y, ls)); y += len(ls) * 66 * S + 12 * S
        elif k == 'title2':
            items.append((k, y, b[1], b[2])); y += 2 * 80 * S + 10 * S
        elif k == 'body':
            f = font(F_LORA, 38 * S, 500); ls = wrap(dm, b[1], f, inner)
            items.append((k, y, ls)); y += len(ls) * 52 * S + 14 * S
        elif k == 'img':
            h = b[2] * S
            items.append((k, y, b[1], h)); y += h + 14 * S
        elif k == 'typed':
            f = font(F_MONO_B, 36 * S); ls = wrap(dm, b[1], f, inner)
            items.append((k, y, ls)); y += len(ls) * 50 * S + 10 * S
        elif k == 'rows':
            items.append((k, y, b[1])); y += len(b[1]) * 56 * S + 6 * S
        elif k == 'buttons':
            items.append((k, y, b[1], b[2] if len(b) > 2 else 0)); y += len(b[1]) * 76 * S + 6 * S
        elif k == 'stamp':
            items.append((k, y, b[1])); y += 104 * S
        elif k == 'cta':
            items.append((k, y, *b[1:])); y += 270 * S
    ph = y + 26 * S
    img = Image.new('RGBA', (pw + 40 * S, ph + 60 * S), (0, 0, 0, 0))
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((10 * S, 16 * S, pw + 10 * S, ph + 16 * S), 12 * S, fill=(42, 30, 22, 90))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10 * S)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, pw, ph), 12 * S, fill=hexc(CREAM), outline=hexc(DARK), width=4 * S)
    d.rounded_rectangle((10 * S, 10 * S, pw - 10 * S, ph - 10 * S), 6 * S, outline=hexc('#D9C7A0'), width=2 * S)
    for it in items:
        k, y = it[0], it[1]
        if k == 'label':
            f = font(F_MONO_B, 24 * S)
            txt = ' '.join(it[2].upper())
            d.text((L, y), txt, font=f, fill=hexc(COPPER))
            if it[3]:
                fi = font(LORA_I, 26 * S, 500)
                d.text((pw - L, y + 12 * S), it[3], font=fi, fill=hexc('#8C7350'), anchor='rm')
            d.line((L, y + 40 * S, pw - L, y + 40 * S), fill=hexc('#D9C7A0'), width=2 * S)
        elif k == 'title':
            f = font(F_LORA, 54 * S, 700)
            for i, l in enumerate(it[2]):
                d.text((L, y + i * 66 * S), l, font=f, fill=hexc(DARK))
        elif k == 'title2':
            f = font(F_LORA, 68 * S, 700)
            d.text((pw / 2, y + 38 * S), it[2], font=f, fill=hexc(DARK), anchor='mm')
            d.text((pw / 2, y + 118 * S), it[3], font=f, fill=hexc(COPPER), anchor='mm')
        elif k == 'body':
            f = font(F_LORA, 38 * S, 500)
            for i, l in enumerate(it[2]):
                d.text((L, y + i * 52 * S), l, font=f, fill=hexc(DARK))
        elif k == 'img':
            key = hashlib.md5(it[2].encode()).hexdigest()[:10]
            p = os.path.join(CACHE, f'img_{key}_{it[3]}.png')
            if not os.path.exists(p):
                svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{pw // S}" height="{it[3] // S}" viewBox="0 0 {pw // S} {it[3] // S}">{it[2]}</svg>'
                render(svg, p, S)
            im = Image.open(p).convert('RGBA')
            img.alpha_composite(im, (0, y))
        elif k == 'typed':
            f = font(F_MONO_B, 36 * S)
            n = int(max(0, prog - 0.3) * 30)
            left = n
            for i, l in enumerate(it[2]):
                vis = l[:max(0, left)]
                d.text((L, y + i * 50 * S), vis, font=f, fill=hexc(DARK))
                done_line = left >= len(l)
                left -= len(l)
                if not done_line or (left <= 0 and i == len(it[2]) - 1):
                    cx = L + d.textlength(vis, font=f) + 4 * S
                    if int(prog * 2.5) % 2 == 0 or not done_line:
                        d.rectangle((cx, y + i * 50 * S + 2 * S, cx + 18 * S, y + i * 50 * S + 40 * S), fill=hexc(COPPER))
                    break
        elif k == 'rows':
            fr = font(F_INTER, 34 * S); fv = font(F_MONO_B, 32 * S)
            if prog < 0.9:   # Edwin ci pensa: tre puntini
                for j in range(3):
                    on = int(prog * 6) % 3 == j
                    d.ellipse((L + j * 34 * S, y + 12 * S, L + j * 34 * S + 20 * S, y + 32 * S), fill=hexc(COPPER if on else '#D9C7A0'))
                continue
            prog2 = prog - 0.6
            shown = int(max(0, prog2 - 0.3) / 0.75) + 1
            for i, (t, v) in enumerate(it[2]):
                if i >= shown:
                    break
                yy = y + i * 56 * S
                a = min(1.0, (prog2 - 0.3 - i * 0.75) / 0.25) if prog < 90 else 1
                col = DARK if a > 0.6 else '#B8A88A'
                if v == 'no':   # cosa da NON fare: croce rossa
                    rr = 18 * S; cx0, cy0 = L + 18 * S, yy + 22 * S
                    d.ellipse((cx0 - rr, cy0 - rr, cx0 + rr, cy0 + rr), fill=hexc(ROSSO if a > 0.6 else '#D9C7A0'))
                    for sx in (-1, 1):
                        d.line((cx0 - rr * 0.42, cy0 - sx * rr * 0.42, cx0 + rr * 0.42, cy0 + sx * rr * 0.42), fill=(255, 255, 255, 255), width=int(rr * 0.28))
                else:
                    check_icon(d, L + 18 * S, yy + 22 * S, 18 * S, a > 0.6)
                d.text((L + 54 * S, yy + 22 * S), t, font=fr, fill=hexc(col), anchor='lm')
                if v and v != 'no':
                    d.text((pw - L, yy + 22 * S), v, font=fv, fill=hexc(col), anchor='rm')
                if i < len(it[2]) - 1:
                    d.line((L + 54 * S, yy + 46 * S, pw - L, yy + 46 * S), fill=hexc('#E5D8BC'), width=2 * S)
        elif k == 'buttons':
            fb = font(F_INTER_SB, 34 * S)
            press = it[3]
            for i, t in enumerate(it[2]):
                yy = y + i * 76 * S
                on = (i == press) and 1.4 <= prog < 90
                bx0, bx1 = L + 60 * S, pw - L - 60 * S
                dd = 3 * S if on else 0
                if not on:
                    d.rounded_rectangle((bx0, yy + 6 * S, bx1, yy + 66 * S), 30 * S, fill=hexc('#BFAF90'))
                d.rounded_rectangle((bx0, yy + dd, bx1, yy + 60 * S + dd), 30 * S, fill=hexc(DARK if on else '#FBF7EC'), outline=hexc(DARK), width=3 * S)
                d.text(((bx0 + bx1) / 2, yy + 30 * S + dd), t, font=fb, fill=hexc(CREAM if on else DARK), anchor='mm')
        elif k == 'stamp':
            if prog >= 1.2:
                f = font(F_LORA, 40 * S, 700)
                st = Image.new('RGBA', (900 * S, 110 * S), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
                tw = ds.textlength(it[2].upper(), font=f)
                ds.rectangle((10 * S, 10 * S, tw + 70 * S, 100 * S), outline=hexc(ROSSO), width=5 * S)
                ds.text((40 * S, 55 * S), it[2].upper(), font=f, fill=hexc(ROSSO), anchor='lm')
                sc = 1 + max(0, 1.45 - prog) * 1.6
                st = st.rotate(5, resample=Image.BICUBIC)
                if sc > 1.01:
                    st = st.resize((int(st.width * sc), int(st.height * sc)), Image.BICUBIC)
                img.alpha_composite(st, (int(pw / 2 - (tw + 80 * S) * sc / 2), int(y + 10 * S - 50 * S * (sc - 1))))
        elif k == 'cta':
            f1 = font(F_LORA, 62 * S, 700); f2 = font(F_INTER_SB, 42 * S)
            l1, l2 = (it[2], it[3]) if len(it) > 2 else ('SEGUI PER IL', 'PROSSIMO CONGEGNO')
            d.text((pw / 2, y + 40 * S), l1, font=f1, fill=hexc(DARK), anchor='mm')
            d.text((pw / 2, y + 122 * S), l2, font=f1, fill=hexc(COPPER), anchor='mm')
            d.text((pw / 2, y + 208 * S), '@ia.senza.codice', font=f2, fill=hexc(DARK), anchor='mm')
    return img.resize((img.width // S, img.height // S), Image.LANCZOS)


def panel_static(blocks):
    """Il pannello cambia nel tempo solo se ha testo battuto, righe, pulsanti o timbri."""
    return not any(b[0] in ('typed', 'rows', 'buttons', 'stamp') for b in blocks)


def panel_settle(blocks):
    t = 0.0
    for b in blocks:
        if b[0] == 'typed':
            t = max(t, 0.3 + len(b[1]) / 30 + 0.2)
        elif b[0] == 'rows':
            t = max(t, 0.9 + len(b[1]) * 0.75 + 0.3)
        elif b[0] == 'buttons':
            t = max(t, 1.6)
        elif b[0] == 'stamp':
            t = max(t, 1.5)
    return t


# ================================================================ montaggio
def build(story_path, outdir):
    spec = importlib.util.spec_from_file_location('s', story_path); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    os.makedirs(outdir, exist_ok=True)
    voice, speed = 'im_nicola:0.75+if_sara:0.25', 1.05
    import voce_neurale as vn

    segs, timeline, t = [np.zeros(int(0.25 * SR), np.float32)], [], 0.25
    for i, sc in enumerate(C.SCENE):
        y, times = scene_audio(vn, sc['voce'], voice, speed)
        start = t
        for a, b, s in times:
            for k, v in (('uèb', 'web'), ('fàil', 'file'), ('ciàt', 'chat'), ('autòmi', 'automi'), ('Èduin', 'Edwin')):
                s = s.replace(k, v)
            timeline.append(('sub', start + a, start + b, s))
        segs.append(y); t += len(y) / SR
        # se il pannello ha bisogno di più tempo (righe, testo battuto), la scena aspetta
        need = panel_settle(sc['panel']) + 0.8
        pause = max(0.6 if i < len(C.SCENE) - 1 else 0.5, need - len(y) / SR)
        timeline.append(('scene', start, t + pause, i))
        segs.append(np.zeros(int(pause * SR), np.float32)); t += pause
    LOOP, INTRO, XF = 1.0, 0.8, 0.45
    total = t + LOOP
    voice_y = np.concatenate(segs + [np.zeros(int(LOOP * SR), np.float32)])
    wav_write(os.path.join(outdir, 'voce.wav'), voice_y / (np.max(np.abs(voice_y)) + 1e-9) * 0.9, SR)

    nfr = int(math.ceil(total * FPS)); hop = SR // FPS
    env = np.array([np.sqrt(np.mean(voice_y[f * hop:(f + 1) * hop] ** 2)) if f * hop < len(voice_y) else 0 for f in range(nfr)])
    env = np.clip(env / (np.percentile(env[env > 0], 95) + 1e-9), 0, 1)
    sm = np.convolve(env, [0.25, 0.5, 0.25], mode='same')
    armv = np.convolve(env, np.ones(int(FPS * 0.6)) / int(FPS * 0.6), mode='same')

    # effetti
    SR2 = 44100
    fx = np.zeros(int(total * SR2) + SR2, np.float32)
    def add(sig, at, gain):
        i = int(max(0, at) * SR2); fx[i:i + len(sig)] += sig[:len(fx) - i] * gain
    wh, tk, cl = sfx_whoosh(), sfx_tick(), sfx_clank()
    scenes = [e for e in timeline if e[0] == 'scene']
    for e in scenes[1:]:
        add(wh, e[1] - 0.12, 0.35)
    for e in scenes:
        for b in C.SCENE[e[3]]['panel']:
            if b[0] == 'typed':
                for k in range(0, len(b[1]), 2):
                    add(tk, e[1] + 0.3 + k / 30, 0.10)
            if b[0] == 'rows':
                for k in range(len(b[1])):
                    add(tk, e[1] + 0.9 + k * 0.75, 0.35)
            if b[0] == 'buttons':
                add(tk, e[1] + 1.4, 0.5)
            if b[0] == 'stamp':
                add(cl, e[1] + 1.2, 0.35)
    add(cl, total - LOOP - 0.05, 0.2)
    wav_write(os.path.join(outdir, 'fx.wav'), fx, SR2)

    # livelli fissi
    cov_path = glob.glob(f'/home/claude/edwin-media/media/riga*/carosello{C.NUM}_tiktok_copertina.png')[0]
    cov = Image.open(cov_path).convert('RGBA').resize((W, H), Image.LANCZOS)
    g = np.zeros((H, W, 4), np.uint8); g[..., :3] = (42, 30, 22)
    g[..., 3] = (np.clip((np.arange(H) - 1380) / 360, 0, 1) * 235)[:, None].astype(np.uint8)
    cov = Image.alpha_composite(cov, Image.fromarray(g))
    bgs, fgs = set_layers(*C.SET)
    key = hashlib.md5((bgs + fgs).encode()).hexdigest()[:10]
    bg = svg_png(bgs, f'set_bg_{key}.png'); fg = svg_png(fgs, f'set_fg_{key}.png')
    plate = title_plate(C.NUM, *C.TITOLO)
    bdg = badge()
    def prop_img(svg, name):
        return svg_png(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{svg}</svg>', f'prop_{name}_{hashlib.md5(svg.encode()).hexdigest()[:8]}.png')
    behind = prop_img(getattr(C, 'DIETRO', ''), 'dietro')      # oggetti dietro Edwin
    front = prop_img(getattr(C, 'DAVANTI', ''), 'davanti')     # oggetti davanti a Edwin (in mano, sul parapetto)
    base = bg.copy(); base.alpha_composite(behind)
    over = fg.copy(); over.alpha_composite(front)

    POSE = getattr(C, 'POSA', 'banco')
    EX = getattr(C, 'EDWIN_X', 540)
    SCALE_B, SCALE_H = 0.76, 0.87
    heads, bodies = {}, {}
    def head(m, e):
        k = (m, e)
        if k not in heads:
            p = os.path.join(CACHE, f'h87_{m}_{e}.png')
            if not os.path.exists(p):
                render(head_svg(m / 5, e), p, SCALE_H)
            heads[k] = Image.open(p).convert('RGBA')
        return heads[k]
    def body(r, a, pose):
        k = (r, a, pose)
        if k not in bodies:
            p = os.path.join(CACHE, f'b76v4_{pose}_{r}_{a}.png')
            if not os.path.exists(p):
                render(body_svg(gear_rot=r * 3.75, arm=a / 3, pose=pose), p, SCALE_B)
            bodies[k] = Image.open(p).convert('RGBA')
        return bodies[k]

    rng = np.random.default_rng(C.NUM)
    blinks, tt = set(), 1.6
    while tt < total:
        f0 = int(tt * FPS); blinks.update({f0, f0 + 1, f0 + 2}); tt += 2.8 + rng.random() * 2.0

    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-i', os.path.join(outdir, 'voce.wav'), '-i', os.path.join(outdir, 'fx.wav'),
           '-filter_complex', '[1:a]aresample=44100,loudnorm=I=-16:TP=-1.5,aresample=44100[v];[2:a]volume=0.8[f];[v][f]amix=inputs=2:duration=longest:normalize=0,aresample=44100,apad[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', f'{total:.3f}', os.path.join(outdir, 'reel.mp4')]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    pcache, subs = {}, {}
    last = len(C.SCENE) - 1
    for f in range(nfr):
        ts = f / FPS
        cur, s0 = 0, 0.0
        for e in scenes:
            if e[1] <= ts + 1e-6:
                cur, s0 = e[3], e[1]
        in_loop = ts >= total - LOOP
        sc = C.SCENE[cur]
        prog = ts - s0
        # pannello
        blocks = sc['panel']
        if panel_static(blocks) or prog > panel_settle(blocks) + 0.1:
            pk = (cur, 'fine')
            pp = 99.0
        else:
            q = round(prog * 15) / 15
            pk = (cur, q); pp = q
        if pk not in pcache:
            pcache[pk] = panel(blocks, pp)
        pim = pcache[pk]
        kf = 1.0 if (cur == 0 and ts < 2) else min(1.0, prog / 0.25)
        if kf < 1:
            ease = 1 - (1 - kf) ** 3
            a = np.array(pim); a[..., 3] = (a[..., 3] * ease).astype(np.uint8); pim2 = Image.fromarray(a); dy = int(-36 * (1 - ease))
        else:
            pim2, dy = pim, 0
        # Edwin
        talk = sm[f]
        m = int(round(min(5, talk * 6)))
        eyes = 'happy' if (cur == last and talk < 0.05 and ts > total - LOOP - 0.6 and not in_loop) else ('blink' if f in blinks else 'open')
        bob = int(3 * math.sin(ts * 2 * math.pi * 0.6) + 4 * talk)
        kinds = [b[0] for b in sc['panel']]
        pose = sc.get('posa') or (('indica' if POSE != 'regge' else 'regge') if ('rows' in kinds or 'buttons' in kinds) and prog > 0.8 else POSE)
        if POSE == 'indica' and not sc.get('posa') and not ('rows' in kinds or 'buttons' in kinds) and cur not in (0,):
            pose = 'banco'
        happy = ('buttons' in kinds and 1.4 <= prog < 2.2) or ('stamp' in kinds and 1.25 <= prog < 2.0)
        if happy and eyes == 'open':
            eyes = 'happy'
        bi = body(f % 8 if talk > 0.1 else (f // 3) % 8, int(min(3, round(armv[f] * 4.5))), pose)
        bx = EX - bi.width // 2
        by = DECK + 30 - bi.height
        hd = head(m, eyes)
        hx = EX - hd.width // 2 + int(0.70 * 0)
        hy = by + int(SCALE_B * 170) - hd.height + int(SCALE_B * 48) + bob
        frame = base.copy()
        frame.alpha_composite(bi, (bx, by + bob // 2))
        frame.alpha_composite(hd, (hx, hy))
        frame.alpha_composite(over)
        z = 1.0 + 0.025 * min(1.0, prog / max(1.0, (scenes[cur][2] - scenes[cur][1])))
        if z > 1.001:
            zw, zh = int(W * z), int(H * z)
            frame = frame.resize((zw, zh), Image.BILINEAR).crop(((zw - W) // 2, int((zh - H) * 0.75), (zw - W) // 2 + W, int((zh - H) * 0.75) + H))
        frame.alpha_composite(plate, (0, 52)); frame.alpha_composite(bdg, (0, 1842))
        frame.alpha_composite(pim2, (PX0 - 10, PY0 + dy))
        s_txt = None
        for e in timeline:
            if e[0] == 'sub' and (e[1] - 0.05 if e[1] > 0.5 else 0) <= ts < e[2] + 0.4:
                s_txt = e[3]
        if s_txt and s_txt not in subs:
            subs[s_txt] = subtitle(s_txt)
        if s_txt and not in_loop:
            frame.alpha_composite(subs[s_txt], ((W - subs[s_txt].width) // 2, 1600))
        # apertura sulla copertina e ritorno per il loop
        if ts < INTRO + XF:
            p = 0.0 if ts < INTRO else (ts - INTRO) / XF; p = p * p * (3 - 2 * p)
            frame = Image.blend(cov, frame, p) if p > 0 else cov.copy()
            frame.alpha_composite(bdg, (0, 1842))
            if s_txt:
                frame.alpha_composite(subs[s_txt], ((W - subs[s_txt].width) // 2, 1600))
        elif in_loop:
            p = min(1.0, (ts - (total - LOOP)) / XF); p = p * p * (3 - 2 * p)
            frame = Image.blend(frame, cov, p) if p < 1 else cov.copy()
            frame.alpha_composite(bdg, (0, 1842))
        pr.stdin.write(frame.tobytes())
    pr.stdin.close(); pr.wait()
    with open(os.path.join(outdir, 'copione.txt'), 'w') as fh:
        for e in timeline:
            if e[0] == 'sub':
                fh.write(f'{e[1]:6.2f}-{e[2]:6.2f}  {e[3]}\n')
    print('fatto', outdir, round(total, 1), 's')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
