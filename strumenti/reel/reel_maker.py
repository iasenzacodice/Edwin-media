"""Trasforma un carosello di Edwin in un Reel parlato (1080x1920, 30 fps).

Uso: python3 reel_maker.py contenuti/c11.py uscita_dir
Il file di contenuto definisce: NUM, TITOLO (2 righe), ICONA, SCENE (lista di dict: panel, voce).
"""
import sys, os, re, math, subprocess, wave, importlib.util, hashlib
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from edwin_svg import head_svg, body_svg, render, gear, CYAN, BRASS, COPPER, COPPER_D, BROWN, DARK, GOLD, GOLD_L

W, H, FPS = 1080, 1920, 30
SR = 24000
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache'); os.makedirs(CACHE, exist_ok=True)

CREAM, PAPER, INK, ROSSO = '#F7F0E0', '#EBDDBF', '#8C7350', '#B3261E'
F_LORA = '/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'
F_INTER = '/usr/share/fonts/opentype/inter/Inter-Regular.otf'
F_INTER_SB = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
F_INTER_B = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
F_MONO = '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'
F_MONO_B = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'


def font(path, size, weight=None):
    f = ImageFont.truetype(path, size)
    if weight and 'Variable' in path:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def hexc(c, a=255):
    c = c.lstrip('#'); return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), a)


def wrap(draw, text, f, maxw):
    lines = []
    for para in text.split('\n'):
        cur = ''
        for w in para.split(' '):
            cand = (cur + ' ' + w).strip()
            if draw.textlength(cand, font=f) <= maxw or not cur:
                cur = cand
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- sfondo e scenografia
def svg_png(svg, name):
    p = os.path.join(CACHE, name)
    if not os.path.exists(p):
        render(svg, p)
    return Image.open(p).convert('RGBA')


def background():
    g = []
    for x in range(0, W + 1, 54):
        g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#E0CDA6" stroke-width="2"/>')
    for y in range(0, H + 1, 54):
        g.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#E0CDA6" stroke-width="2"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
<defs><radialGradient id="lamp" cx="0.5" cy="0.62" r="0.5"><stop offset="0" stop-color="#FFF6DD" stop-opacity="0.95"/><stop offset="1" stop-color="#FFF6DD" stop-opacity="0"/></radialGradient>
<linearGradient id="bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8A5530"/><stop offset="1" stop-color="#6E4122"/></linearGradient>
<linearGradient id="front" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A341C"/><stop offset="1" stop-color="#3A2214"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="#EFE3C8"/>
{''.join(g)}
<ellipse cx="540" cy="1180" rx="620" ry="560" fill="url(#lamp)"/>
<g opacity="0.16">{gear(60, 1000, 210, 14, BRASS, hole='#EFE3C8', rot=8)}{gear(1040, 820, 170, 12, BRASS, hole='#EFE3C8', rot=4)}</g>
<rect x="18" y="0" width="34" height="{H}" fill="{BRASS}"/><rect x="12" y="640" width="46" height="26" rx="6" fill="{COPPER}"/><rect x="12" y="1240" width="46" height="26" rx="6" fill="{COPPER}"/>
<rect x="1028" y="0" width="34" height="{H}" fill="{BRASS}"/><rect x="1022" y="420" width="46" height="26" rx="6" fill="{COPPER}"/><rect x="1022" y="1100" width="46" height="26" rx="6" fill="{COPPER}"/>
<circle cx="1045" cy="980" r="34" fill="#F7F0E0" stroke="{BRASS}" stroke-width="8"/><line x1="1045" y1="980" x2="1060" y2="962" stroke="{ROSSO}" stroke-width="5" stroke-linecap="round"/>
<rect x="0" y="1500" width="{W}" height="34" fill="url(#bench)"/>
<rect x="0" y="1534" width="{W}" height="{H - 1534}" fill="url(#front)"/>
<rect x="0" y="1534" width="{W}" height="6" fill="#2A1E16" opacity="0.5"/>
<g opacity="0.25">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#2A1E16" stroke-width="3"/>' for y in (1640, 1760, 1880))}</g>
</svg>'''
    return svg_png(svg, 'bg_v2.png')


def bench_layer():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
<defs><radialGradient id="lamp" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFF6DD" stop-opacity="0.75"/><stop offset="1" stop-color="#FFF6DD" stop-opacity="0"/></radialGradient>
<linearGradient id="bench" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8A5530"/><stop offset="1" stop-color="#6E4122"/></linearGradient>
<linearGradient id="front" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A341C"/><stop offset="1" stop-color="#3A2214"/></linearGradient></defs>
<ellipse cx="540" cy="1250" rx="460" ry="420" fill="url(#lamp)"/>
<rect x="0" y="1500" width="{W}" height="34" fill="url(#bench)"/>
<rect x="0" y="1534" width="{W}" height="{H - 1534}" fill="url(#front)"/>
<rect x="0" y="1534" width="{W}" height="6" fill="#2A1E16" opacity="0.5"/>
<g opacity="0.25">{''.join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#2A1E16" stroke-width="3"/>' for y in (1640, 1760, 1880))}</g>
</svg>'''
    return svg_png(svg, 'bench_v1.png')


def title_plate(num, l1, l2):
    img = Image.new('RGBA', (W * 2, 400), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = 260, 60, 1900, 340
    d.rounded_rectangle((x0 + 12, y0 + 16, x1 + 12, y1 + 16), 24, fill=(42, 30, 22, 110))
    d.rounded_rectangle((x0, y0, x1, y1), 24, fill=hexc(BRASS))
    d.rounded_rectangle((x0 + 14, y0 + 14, x1 - 14, y1 - 14), 16, fill=hexc('#2E2017'))
    for (cx, cy) in ((x0 + 40, y0 + 40), (x1 - 40, y0 + 40), (x0 + 40, y1 - 40), (x1 - 40, y1 - 40)):
        d.ellipse((cx - 9, cy - 9, cx + 9, cy + 9), fill=hexc(BRASS))
    f1 = font(F_LORA, 92, 700)
    for txt, y, col in ((l1, 128, GOLD_L), (l2, 238, '#F3E9D2')):
        tw = d.textlength(txt.upper(), font=f1)
        d.text(((x0 + x1) / 2 - tw / 2, y), txt.upper(), font=f1, fill=hexc(col), anchor='lm')
    # numero nel tondo d'ottone
    d.ellipse((200, 20, 340, 160), fill=hexc(BRASS)); d.ellipse((214, 34, 326, 146), fill=hexc(GOLD))
    fn = font(F_LORA, 64, 700)
    d.text((270, 92), str(num), font=fn, fill=hexc(DARK), anchor='mm')
    return img.resize((W, 200), Image.LANCZOS)


# ---------------------------------------------------------------- pannelli
PX0, PX1, PY0 = 70, 1010, 268


def panel(blocks, typed=None):
    """blocks: lista di (tipo, testo...). typed = numero di caratteri visibili del blocco 'esempio'."""
    S = 2
    inner = (PX1 - PX0 - 96) * S
    tmp = Image.new('RGBA', (10, 10)); dm = ImageDraw.Draw(tmp)
    items, y = [], 46 * S
    for b in blocks:
        k = b[0]
        if k == 'label':
            items.append((k, y, b[1])); y += 62 * S
        elif k == 'title':
            f = font(F_LORA, 58 * S, 700); ls = wrap(dm, b[1], f, inner)
            items.append((k, y, ls)); y += len(ls) * 72 * S + 14 * S
        elif k == 'title2':  # gancio: due righe, la seconda rame
            items.append((k, y, b[1], b[2])); y += 2 * 84 * S + 16 * S
        elif k == 'body':
            f = font(F_INTER, 38 * S); ls = wrap(dm, b[1], f, inner)
            items.append((k, y, ls)); y += len(ls) * 52 * S + 18 * S
        elif k == 'example':
            f = font(F_MONO_B, 34 * S); ls = wrap(dm, b[2], f, inner - 60 * S)
            h = (70 + len(ls) * 46 + 26) * S
            items.append((k, y, b[1], ls, h)); y += h + 22 * S
        elif k == 'chat':
            f = font(F_MONO_B, 32 * S); rows = []
            for who, t in b[2]:
                for i, l in enumerate(wrap(dm, (who + ' ' + t) if who else t, f, inner - 60 * S)):
                    rows.append(l)
            h = (70 + len(rows) * 44 + 26) * S
            items.append((k, y, b[1], rows, h)); y += h + 22 * S
        elif k == 'tip':  # consiglio di Edwin, corsivo
            f = font(F_LORA, 36 * S, 500); ls = wrap(dm, b[1], f, inner - 40 * S)
            items.append((k, y, ls)); y += len(ls) * 48 * S + 20 * S
        elif k == 'chips':
            items.append((k, y, b[1])); y += 92 * S
        elif k == 'stamp':
            items.append((k, y, b[1])); y += 86 * S
        elif k == 'cta':
            y += 10 * S; items.append((k, y, *b[1:])); y += 300 * S
    ph = y + 30 * S
    pw = (PX1 - PX0) * S
    img = Image.new('RGBA', (pw + 40 * S, ph + 40 * S), (0, 0, 0, 0))
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((10 * S, 16 * S, pw + 10 * S, ph + 16 * S), 14 * S, fill=(42, 30, 22, 90))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10 * S)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, pw, ph), 14 * S, fill=hexc(CREAM), outline=hexc(DARK), width=4 * S)
    d.rounded_rectangle((10 * S, 10 * S, pw - 10 * S, ph - 10 * S), 8 * S, outline=hexc('#D9C7A0'), width=2 * S)
    L = 48 * S
    for it in items:
        k, y = it[0], it[1]
        if k == 'label':
            f = font(F_MONO_B, 28 * S)
            txt = ' '.join(it[2].upper())
            d.text((L, y), txt, font=f, fill=hexc(COPPER))
            tw = d.textlength(txt, font=f)
            d.line((L + tw + 20 * S, y + 17 * S, pw - L, y + 17 * S), fill=hexc('#D9C7A0'), width=3 * S)
        elif k == 'title':
            f = font(F_LORA, 58 * S, 700)
            for i, l in enumerate(it[2]):
                d.text((L, y + i * 72 * S), l, font=f, fill=hexc(DARK))
        elif k == 'title2':
            f = font(F_LORA, 70 * S, 700)
            d.text((pw / 2, y + 40 * S), it[2], font=f, fill=hexc(DARK), anchor='mm')
            d.text((pw / 2, y + 124 * S), it[3], font=f, fill=hexc(COPPER), anchor='mm')
        elif k == 'body':
            f = font(F_INTER, 38 * S)
            for i, l in enumerate(it[2]):
                d.text((L, y + i * 52 * S), l, font=f, fill=hexc('#4A3020'))
        elif k in ('example', 'chat'):
            hdr, ls, h = it[2], it[3], it[4]
            d.rectangle((L, y, pw - L, y + h), fill=hexc('#FBF7EC'), outline=hexc(DARK), width=3 * S)
            ok = k == 'chat' or hdr.lower().startswith(('meglio', 'così'))
            d.rectangle((L, y, pw - L, y + 8 * S), fill=hexc('#4C8A3C' if ok else COPPER))
            fh = font(F_MONO_B, 26 * S)
            d.text((L + 28 * S, y + 26 * S), ' '.join(hdr.upper()), font=fh, fill=hexc('#3E7A30' if ok else COPPER))
            f = font(F_MONO_B, (34 if k == 'example' else 32) * S)
            lh = (46 if k == 'example' else 44) * S
            left = typed if typed is not None else 10 ** 9
            for i, l in enumerate(ls):
                vis = l[:max(0, left)]
                left -= len(l)
                if who := re.match(r'^(Tu:|Io:|Edwin:)', vis):
                    d.text((L + 28 * S, y + 74 * S + i * lh), vis, font=f, fill=hexc(DARK))
                    d.text((L + 28 * S, y + 74 * S + i * lh), who.group(1), font=f, fill=hexc(COPPER))
                else:
                    d.text((L + 28 * S, y + 74 * S + i * lh), vis, font=f, fill=hexc(DARK))
                if typed is not None and 0 <= left + len(l) <= len(l) and left <= 0:
                    cx = L + 28 * S + d.textlength(vis, font=f) + 4 * S
                    d.rectangle((cx, y + 76 * S + i * lh, cx + 16 * S, y + 74 * S + i * lh + 38 * S), fill=hexc(COPPER))
                    break
        elif k == 'tip':
            f = font('/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf', 36 * S, 500)
            d.rectangle((L, y + 4 * S, L + 8 * S, y + len(it[2]) * 48 * S - 4 * S), fill=hexc(BRASS))
            for i, l in enumerate(it[2]):
                d.text((L + 28 * S, y + i * 48 * S), l, font=f, fill=hexc('#5A341C'))
        elif k == 'chips':
            f = font(F_INTER_SB, 32 * S); x = L
            for i, c in enumerate(it[2]):
                tw = d.textlength(c, font=f)
                fill = hexc(DARK) if i == 0 else hexc(CREAM)
                d.rounded_rectangle((x, y, x + tw + 56 * S, y + 70 * S), 35 * S, fill=fill, outline=hexc(DARK), width=3 * S)
                d.text((x + 28 * S, y + 35 * S), c, font=f, fill=hexc(CREAM if i == 0 else DARK), anchor='lm')
                x += tw + 76 * S
        elif k == 'stamp':
            f = font(F_LORA, 40 * S, 700)
            st = Image.new('RGBA', (900 * S, 110 * S), (0, 0, 0, 0)); ds = ImageDraw.Draw(st)
            tw = ds.textlength(it[2].upper(), font=f)
            ds.rectangle((10 * S, 10 * S, tw + 70 * S, 100 * S), outline=hexc(ROSSO), width=5 * S)
            ds.text((40 * S, 55 * S), it[2].upper(), font=f, fill=hexc(ROSSO), anchor='lm')
            st = st.rotate(4, resample=Image.BICUBIC, expand=False)
            img.alpha_composite(st, (int(pw - tw - 160 * S), int(y - 10 * S)))
        elif k == 'cta':
            f1 = font(F_LORA, 66 * S, 700); f2 = font(F_INTER_SB, 44 * S)
            l1, l2 = (it[2], it[3]) if len(it) > 2 else ('SEGUI PER IL', 'PROSSIMO CONGEGNO')
            d.text((pw / 2, y + 40 * S), l1, font=f1, fill=hexc(DARK), anchor='mm')
            d.text((pw / 2, y + 126 * S), l2, font=f1, fill=hexc(COPPER), anchor='mm')
            d.text((pw / 2, y + 216 * S), '@ia.senza.codice', font=f2, fill=hexc(DARK), anchor='mm')
    return img.resize((img.width // S, img.height // S), Image.LANCZOS)


def example_len(blocks):
    for b in blocks:
        if b[0] == 'example':
            return len(b[2].replace(' ', ' '))
        if b[0] == 'chat':
            return sum(len((w + ' ' + t) if w else t) for w, t in b[2])
    return 0


# ---------------------------------------------------------------- sottotitoli e badge
def subtitle(text):
    S = 2
    f = font(F_INTER_SB, 44 * S)
    dm = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    ls = wrap(dm, text, f, 860 * S)
    lw = max(dm.textlength(l, font=f) for l in ls)
    bw, bh = lw + 64 * S, len(ls) * 60 * S + 36 * S
    img = Image.new('RGBA', (int(bw), int(bh)), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, bw - 1, bh - 1), 18 * S, fill=(30, 21, 15, 225))
    for i, l in enumerate(ls):
        d.text((bw / 2, 18 * S + 30 * S + i * 60 * S), l, font=f, fill=(255, 255, 255, 255), anchor='mm')
    return img.resize((img.width // S, img.height // S), Image.LANCZOS)


def badge():
    f = font(F_INTER_SB, 26)
    img = Image.new('RGBA', (W, 60), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    t = 'Personaggio creato con l\'IA'
    tw = d.textlength(t, font=f)
    d.rounded_rectangle((W / 2 - tw / 2 - 22, 6, W / 2 + tw / 2 + 22, 54), 24, fill=(243, 233, 210, 60))
    d.text((W / 2, 30), t, font=f, fill=(243, 233, 210, 200), anchor='mm')
    return img


# ---------------------------------------------------------------- pacco sul banco
def package(num, icon_svg):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="330" height="300">
<path d="M20 70 L250 70 L300 30 L70 30 Z" fill="#D9B07A"/>
<path d="M250 70 L300 30 L300 250 L250 290 Z" fill="#B88A55"/>
<rect x="20" y="70" width="230" height="220" fill="#CFA36B"/>
<rect x="125" y="70" width="22" height="220" fill="#E3C79A" opacity="0.7"/>
<rect x="44" y="96" width="182" height="132" fill="#F7F0E0" stroke="#2A1E16" stroke-width="4"/>
<g transform="translate(135 162)">{icon_svg}</g>
<g transform="rotate(-6 135 262)"><rect x="52" y="240" width="170" height="40" fill="none" stroke="{ROSSO}" stroke-width="4"/>
<text x="137" y="268" font-family="Lora" font-weight="700" font-size="22" fill="{ROSSO}" text-anchor="middle">CONGEGNO {num}</text></g>
</svg>'''
    return svg_png(svg, f'pacco_{num}_{hashlib.md5(icon_svg.encode()).hexdigest()[:6]}.png')


# ---------------------------------------------------------------- audio
def load_tts():
    sys.argv_backup = sys.argv
    import voce_neurale as vn
    return vn


def wav_write(path, y, sr):
    y = np.clip(y, -1, 1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((y * 32767).astype(np.int16).tobytes())


def split_sentences(t):
    return [x.strip() for x in re.split(r'(?<=[.?])\s+', t) if x.strip()]


def silences(y, sr, thr_db=-38, min_len=0.09):
    hop = int(0.01 * sr)
    n = len(y) // hop
    r = np.sqrt(np.mean(y[:n * hop].reshape(n, hop) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(r / (np.max(r) + 1e-9))
    sil = db < thr_db
    out, i = [], 0
    while i < n:
        if sil[i]:
            j = i
            while j < n and sil[j]:
                j += 1
            if (j - i) * 0.01 >= min_len:
                out.append((i * 0.01, j * 0.01))
            i = j
        else:
            i += 1
    return out


def trim(y, sr):
    s = silences(y, sr, -45, 0.0)
    a = 0; b = len(y)
    if s and s[0][0] == 0:
        a = int(s[0][1] * sr)
    if s and abs(s[-1][1] - len(y) / sr) < 0.02:
        b = int(s[-1][0] * sr)
    return y[max(0, a - int(0.02 * sr)):min(len(y), b + int(0.05 * sr))]


def scene_audio(vn, text, voice, speed):
    """Genera la scena come un'unica battuta e restituisce audio + tempi delle frasi (misurati)."""
    lex = hashlib.md5(open(os.path.join(HERE, 'voce_neurale.py'), 'rb').read()).hexdigest()[:8]
    key = hashlib.md5(f'{text}|{voice}|{speed}|v3|{lex}'.encode()).hexdigest()[:12]
    p = os.path.join(CACHE, f'tts_{key}.npy')
    if os.path.exists(p):
        y = np.load(p)
    else:
        y, _ = vn.tts(text, voice, speed, gap=0.0)
        y = trim(y, SR)
        np.save(p, y)
    sents = split_sentences(text)
    cuts = []
    if len(sents) > 1:
        internal = [s for s in silences(y, SR) if s[0] > 0.2 and s[1] < len(y) / SR - 0.2]
        internal.sort(key=lambda s: -(s[1] - s[0]))
        chosen = sorted(internal[:len(sents) - 1])
        if len(chosen) == len(sents) - 1:
            cuts = chosen
    # ricompone: tra una frase e l'altra almeno 0.35 s di pausa
    pieces, times, t0, cur = [], [], 0, 0.0
    if cuts:
        bounds = [0.0] + [((a + b) / 2) for a, b in cuts] + [len(y) / SR]
        for i in range(len(sents)):
            seg = y[int(bounds[i] * SR):int(bounds[i + 1] * SR)]
            seg = trim(seg, SR)
            pieces.append(seg)
            times.append((cur, cur + len(seg) / SR, sents[i]))
            cur += len(seg) / SR
            if i < len(sents) - 1:
                pieces.append(np.zeros(int(0.35 * SR), np.float32)); cur += 0.35
        y2 = np.concatenate(pieces)
    else:
        y2 = y
        tot = sum(len(s) for s in sents); c = 0
        for s in sents:
            a = c / tot * len(y) / SR; c += len(s); times.append((a, c / tot * len(y) / SR, s))
    return y2.astype(np.float32), times


def sfx_whoosh(sr=44100, dur=0.28):
    n = int(sr * dur); t = np.arange(n) / sr
    noise = np.random.default_rng(1).standard_normal(n)
    env = np.sin(np.pi * t / dur) ** 2
    # filtro passa basso semplice variabile
    out = np.zeros(n); a = 0.0
    for i in range(n):
        k = 0.02 + 0.25 * env[i]
        a += k * (noise[i] - a); out[i] = a
    return (out * env * 0.5).astype(np.float32)


def sfx_tick(sr=44100):
    n = int(sr * 0.035); t = np.arange(n) / sr
    return (np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 180) * 0.6 + np.random.default_rng(2).standard_normal(n) * np.exp(-t * 300) * 0.25).astype(np.float32)


def sfx_clank(sr=44100):
    n = int(sr * 0.4); t = np.arange(n) / sr
    s = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * d) for f, d in ((620, 9), (1340, 14), (2210, 20)))
    return (s * 0.25).astype(np.float32)


# ---------------------------------------------------------------- montaggio
def build(content_path, outdir):
    spec = importlib.util.spec_from_file_location('c', content_path); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    os.makedirs(outdir, exist_ok=True)
    voice, speed = 'im_nicola:0.75+if_sara:0.25', 1.05
    vn = load_tts()

    # audio scena per scena
    segs, timeline, t = [], [], 0.25  # breve respiro iniziale ma scena già illuminata
    segs.append(np.zeros(int(0.25 * SR), np.float32))
    for i, sc in enumerate(C.SCENE):
        y, times = scene_audio(vn, sc['voce'], voice, speed)
        start = t
        for a, b, s in times:
            timeline.append(('sub', start + a, start + b, s))
        segs.append(y); t += len(y) / SR
        end_pause = 0.6 if i < len(C.SCENE) - 1 else 0.5
        timeline.append(('scene', start, t + end_pause, i))
        segs.append(np.zeros(int(end_pause * SR), np.float32)); t += end_pause
    LOOP = 1.0  # ritorno alla copertina, per il loop
    INTRO, XF = 0.8, 0.45
    total = t + LOOP
    voice_y = np.concatenate(segs)
    voice_y = np.concatenate([voice_y, np.zeros(int(LOOP * SR), np.float32)])
    wav_write(os.path.join(outdir, 'voce.wav'), voice_y / (np.max(np.abs(voice_y)) + 1e-9) * 0.9, SR)

    # envelope per il labiale
    nfr = int(math.ceil(total * FPS))
    env = np.zeros(nfr)
    hop = SR // FPS
    for f in range(nfr):
        seg = voice_y[f * hop:(f + 1) * hop]
        env[f] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0
    env = env / (np.percentile(env[env > 0], 95) + 1e-9) if np.any(env > 0) else env
    env = np.clip(env, 0, 1)
    sm = np.convolve(env, [0.25, 0.5, 0.25], mode='same')

    # effetti sonori
    SR2 = 44100
    fx = np.zeros(int(total * SR2) + SR2, np.float32)
    def add(sig, at, gain):
        i = int(at * SR2); fx[i:i + len(sig)] += sig[:len(fx) - i] * gain
    wh, tk, cl = sfx_whoosh(), sfx_tick(), sfx_clank()
    scenes = [e for e in timeline if e[0] == 'scene']
    for e in scenes[1:]:
        add(wh, e[1] - 0.12, 0.35)
    add(cl, total - LOOP - 0.05, 0.25)
    TYPE_CPS = 32
    for e in scenes:
        n = example_len(C.SCENE[e[3]]['panel'])
        if n and C.SCENE[e[3]].get('type', True):
            t0 = e[1] + 0.35
            for k in range(0, n, 2):
                add(tk, t0 + k / TYPE_CPS, 0.10)
    wav_write(os.path.join(outdir, 'fx.wav'), fx, SR2)

    # grafica statica
    bg = background()
    plate = title_plate(C.NUM, *C.TITOLO)
    bdg = badge()
    pk = package(C.NUM, C.ICONA)
    heads = {}
    def head(m, e):
        k = (m, e)
        if k not in heads:
            p = os.path.join(CACHE, f'head82_{m}_{e}.png')
            if not os.path.exists(p):
                render(head_svg(m / 5, e), p, 0.82)
            heads[k] = Image.open(p).convert('RGBA')
        return heads[k]
    bodies = {}
    def body_img(r, a):
        k = (r, a)
        if k not in bodies:
            p = os.path.join(CACHE, f'bodyv2_{r}_{a}.png')
            if not os.path.exists(p):
                render(body_svg(gear_rot=r * 3.75, arm=a / 3), p, 0.72)
            bodies[k] = Image.open(p).convert('RGBA')
        return bodies[k]
    # gesto del braccio: segue l'intensità del parlato, lento
    win = int(FPS * 0.6)
    armv = np.convolve(env, np.ones(win) / win, mode='same')
    panels = {}
    for i, scn in enumerate(C.SCENE):
        hgt = panel(scn['panel']).height
        if PY0 + hgt > 772:
            print('ATTENZIONE pannello troppo alto, scena', i, hgt)
    subs = {}

    import glob
    cov_path = glob.glob(f'/home/claude/edwin-media/media/riga*/carosello{C.NUM}_tiktok_copertina.png')[0]
    cov = Image.open(cov_path).convert('RGBA').resize((W, H), Image.LANCZOS)
    blur = cov.filter(ImageFilter.GaussianBlur(9))
    # sfumatura scura in basso: sottotitoli e badge leggibili, nasconde i post vicini
    g = np.zeros((H, W, 4), np.uint8); g[..., :3] = (42, 30, 22)
    ramp = np.clip((np.arange(H) - 1380) / 360, 0, 1) * 235
    g[..., 3] = ramp[:, None].astype(np.uint8)
    cov = Image.alpha_composite(cov, Image.fromarray(g))
    veil = Image.new('RGBA', (W, H), (239, 227, 200, 95))
    base = Image.alpha_composite(blur, veil)
    base.alpha_composite(bench_layer())
    base.alpha_composite(plate, (0, 52))
    base.alpha_composite(pk, (64, 1236))
    base.alpha_composite(bdg, (0, 1842))

    # occhi: battito ogni ~3.5 s, felici sull'ultima scena e sul loop
    rng = np.random.default_rng(C.NUM)
    blinks = set()
    tt = 1.2
    while tt < total:
        f0 = int(tt * FPS); blinks.update({f0, f0 + 1, f0 + 2}); tt += 2.8 + rng.random() * 2.0

    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-i', os.path.join(outdir, 'voce.wav'), '-i', os.path.join(outdir, 'fx.wav'),
           '-filter_complex', '[1:a]aresample=44100,loudnorm=I=-16:TP=-1.5,aresample=44100[v];[2:a]volume=0.8[f];[v][f]amix=inputs=2:duration=longest:normalize=0,aresample=44100,apad[a]',
           '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p',
           '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-t', f'{total:.3f}', os.path.join(outdir, 'reel.mp4')]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    INTRO, XF = 0.8, 0.45
    last_scene = len(C.SCENE) - 1
    for f in range(nfr):
        tsec = f / FPS
        # scena corrente
        cur = 0; sc_start = 0
        for e in scenes:
            if e[1] <= tsec + 1e-6:
                cur, sc_start = e[3], e[1]
        in_loop = tsec >= total - LOOP
        if in_loop:
            cur, sc_start = 0, total - LOOP
        sc = C.SCENE[cur]
        frame = base.copy()
        # pannello (scorre giù dall'alto in 0.22 s, tranne la prima scena e il loop: già fermi)
        n = example_len(sc['panel'])
        typed = None
        if n and sc.get('type', True) and not in_loop:
            typed = int((tsec - sc_start - 0.35) * TYPE_CPS)
            if typed >= n:
                typed = None
            elif typed < 0:
                typed = 0
        key = (cur, typed)
        if key not in panels:
            panels[key] = panel(sc['panel'], typed)
        pimg = panels[key]
        k = min(1.0, (tsec - sc_start) / 0.22) if (cur != 0 or tsec > 1) and not in_loop else 1.0
        if f == 0:
            k = 1.0
        ease = 1 - (1 - k) ** 3
        dy = int(-40 * (1 - ease))
        if k < 1:
            pimg2 = pimg.copy(); a = np.array(pimg2); a[..., 3] = (a[..., 3] * ease).astype(np.uint8); pimg2 = Image.fromarray(a)
        else:
            pimg2 = pimg
        # Edwin
        talk = sm[f]
        m = int(round(min(5, talk * 6)))
        if (not in_loop) and cur == last_scene and talk < 0.05 and tsec > total - LOOP - 0.5:
            eyes = 'happy'
        else:
            eyes = 'blink' if f in blinks else 'open'
        bob = int(3 * math.sin(tsec * 2 * math.pi * 0.6) + 4 * talk)
        al = int(min(3, round(armv[f] * 4.5)))
        body = body_img(f % 8 if talk > 0.1 else (f // 3) % 8, al)
        bx = (W - body.width) // 2
        by = 1500 - body.height + 20
        hd = head(m, eyes)
        hx = (W - hd.width) // 2
        hy = by - hd.height + 34 + bob
        frame.alpha_composite(body, (bx, by + bob // 2))
        frame.alpha_composite(hd, (hx, hy))
        frame.alpha_composite(pimg2, (PX0 - 10, PY0 + dy))
        # sottotitolo
        s_txt = None
        for e in timeline:
            if e[0] == 'sub' and (e[1] - 0.05 if e[1] > 0.5 else 0) <= tsec < e[2] + 0.4:
                s_txt = e[3]
        if s_txt and not in_loop:
            if s_txt not in subs:
                subs[s_txt] = subtitle(s_txt)
            si = subs[s_txt]
            frame.alpha_composite(si, ((W - si.width) // 2, 1590))
        # apertura sulla copertina del post e ritorno alla copertina per il loop
        if tsec < INTRO + XF:
            p = 0.0 if tsec < INTRO else (tsec - INTRO) / XF
            p = p * p * (3 - 2 * p)
            sub_layer = None
            frame = Image.blend(cov, frame, p) if p > 0 else cov.copy()
            frame.alpha_composite(bdg, (0, 1842))
            if s_txt:
                frame.alpha_composite(subs[s_txt], ((W - subs[s_txt].width) // 2, 1590))
        elif in_loop:
            p = min(1.0, (tsec - (total - LOOP)) / XF)
            p = p * p * (3 - 2 * p)
            frame = Image.blend(frame, cov, p) if p < 1 else cov.copy()
            frame.alpha_composite(bdg, (0, 1842))
        pr.stdin.write(frame.tobytes())
    pr.stdin.close(); pr.wait()
    # testo per controllo
    with open(os.path.join(outdir, 'copione.txt'), 'w') as fh:
        for e in timeline:
            if e[0] == 'sub':
                fh.write(f'{e[1]:6.2f}-{e[2]:6.2f}  {e[3]}\n')
    print('fatto', outdir, round(total, 1), 's')


if __name__ == '__main__':
    sys.argv_real = sys.argv
    build(sys.argv[1], sys.argv[2])
