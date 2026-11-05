"""Reel della stagione 2 (stile collage "taccuino dell'inventore").

Ogni Reel si apre sulla sua copertina e la scena è la stessa casella senza adesivi: il cartellino del titolo resta in alto,
Edwin è un adesivo animato (bocca, occhi, braccia, posa che cambia), il congegno sta sul taccuino in basso,
i pannelli entrano come adesivi che si attaccano. Tipi di pannello in più rispetto a reel2: 'chat' (fumetti in ordine).
Opzioni di scena: posa, x (Edwin si sposta), zoom (primo piano), scossa (Edwin sbaglia), pop (un congegno che salta fuori).

Uso: python3 reel_s2.py storie_s2/s28.py uscita_dir
"""
import sys, os, math, subprocess, importlib.util, hashlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 's2'))
import reel2 as R2
from reel_maker import (W, H, FPS, SR, font, wrap, hexc, F_LORA, F_INTER, F_INTER_SB, F_MONO_B, CREAM, subtitle, scene_audio, wav_write,
                        sfx_whoosh, sfx_tick, sfx_clank)
from edwin_svg import head_svg, body_svg, render, CYAN, BRASS, COPPER, DARK, GOLD
import griglia as G

CACHE = os.path.join(HERE, 'cache_s2'); os.makedirs(CACHE, exist_ok=True)
S2 = os.path.join(HERE, 'out_s2')
DESK = 1490                 # bordo alto del taccuino su cui poggia Edwin
PX0, PY0 = 80, 332          # pannelli
SUBST = (('quattromilaottantotto', '4.088'), ('quattromilacinquecento', '4.500'), ('uèb', 'web'), ('fàil', 'file'), ('ciàt', 'chat'), ('autòmi', 'automi'), ('Èduin', 'Edwin'))


# ------------------------------------------------------------------ elementi fissi
def background(n):
    r, c = G.post_pos(n)
    vu = Image.open(os.path.join(S2, 'master_vuoto.png')).convert('RGBA')
    return vu.crop((G.col_x(c), G.row_y(r) - G.EXT, G.col_x(c) + W, G.row_y(r) - G.EXT + H))


def notebook():
    """Striscia di taccuino in basso (un adesivo grande, un po' ruotato) con spirale e righe."""
    p = os.path.join(CACHE, 'taccuino_v2.png')
    if os.path.exists(p):
        return Image.open(p).convert('RGBA')
    w, h = W + 160, H - DESK + 120
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((0, 40, w, h), fill=hexc('#F7F0E0'))
    for y in range(120, h, 62):
        d.line((0, y, w, y), fill=hexc('#BFDCDD'), width=4)
    d.line((150, 40, 150, h), fill=hexc('#D97B6C'), width=4)
    for x in range(50, w, 72):
        d.ellipse((x + 6, 62, x + 26, 82), fill=hexc('#5A4A3A'))
        d.arc((x, 4, x + 32, 76), 180, 360, fill=hexc('#8C7A62'), width=8)
        d.arc((x, 4, x + 32, 76), 180, 300, fill=hexc('#C9B79A'), width=3)
    st = G.sticker(im, 16, -1.2)
    st.save(p)
    return st


def badge_dark():
    f = font(F_INTER_SB, 26)
    img = Image.new('RGBA', (W, 60), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    t = "Personaggio creato con l'IA"
    tw = d.textlength(t, font=f)
    d.rounded_rectangle((W / 2 - tw / 2 - 22, 6, W / 2 + tw / 2 + 22, 54), 24, fill=(42, 30, 22, 170))
    d.text((W / 2, 30), t, font=f, fill=(243, 233, 210, 235), anchor='mm')
    return img


def outline(img, border=14):
    """Bordo crema dell'adesivo calcolato al volo (per Edwin che si muove)."""
    a = img.split()[3]
    pad = border + 4
    big = Image.new('L', (img.width + 2 * pad, img.height + 2 * pad), 0); big.paste(a, (pad, pad))
    grown = big.filter(ImageFilter.GaussianBlur(border * 0.55)).point(lambda v: 255 if v > 18 else 0)
    out = Image.new('RGBA', big.size, (0, 0, 0, 0))
    sh = Image.new('RGBA', big.size, (42, 30, 22, 0)); sh.putalpha(grown.point(lambda v: int(v * 0.35)))
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)), (0, 0))
    edge = Image.new('RGBA', big.size, hexc('#F7F0E0')); edge.putalpha(grown)
    out.alpha_composite(edge, (-6, -10))
    out.alpha_composite(img, (pad - 6, pad - 10))
    return out, pad


# ------------------------------------------------------------------ pannello "chat"
def chat_panel(label, msgs, prog):
    S = 2
    pw = (1000 - PX0) * S
    dm = ImageDraw.Draw(Image.new('RGBA', (10, 10)))
    f = font(F_INTER, 34 * S); fl = font(F_MONO_B, 24 * S)
    lay, y = [], 96 * S
    for who, t in msgs:
        ls = wrap(dm, t, f, 560 * S)
        bw = max(dm.textlength(l, font=f) for l in ls) + 56 * S
        bh = len(ls) * 48 * S + 34 * S
        lay.append((who, ls, y, bw, bh)); y += bh + 22 * S
    ph = y + 10 * S
    img = Image.new('RGBA', (pw + 40 * S, ph + 60 * S), (0, 0, 0, 0))
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((10 * S, 16 * S, pw + 10 * S, ph + 16 * S), 12 * S, fill=(42, 30, 22, 90))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10 * S)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, pw, ph), 12 * S, fill=hexc(CREAM), outline=hexc(DARK), width=4 * S)
    d.text((48 * S, 40 * S), ' '.join(label.upper()), font=fl, fill=hexc(COPPER))
    d.line((48 * S, 80 * S, pw - 48 * S, 80 * S), fill=hexc('#D9C7A0'), width=2 * S)
    for i, (who, ls, yy, bw, bh) in enumerate(lay):
        t0 = 0.35 + i * 1.1
        if prog < t0:
            if prog > t0 - 0.6 and who == 'ed':      # Edwin sta scrivendo: tre puntini
                x0 = 48 * S
                d.rounded_rectangle((x0, yy, x0 + 150 * S, yy + 70 * S), 30 * S, fill=hexc('#EFE3C8'), outline=hexc(DARK), width=3 * S)
                for j in range(3):
                    on = int(prog * 6) % 3 == j
                    d.ellipse((x0 + (34 + j * 34) * S, yy + 25 * S, x0 + (54 + j * 34) * S, yy + 45 * S), fill=hexc(COPPER if on else '#C9B38A'))
            break
        mine = who == 'tu'
        x0 = pw - 48 * S - bw if mine else 48 * S
        d.rounded_rectangle((x0, yy, x0 + bw, yy + bh), 26 * S, fill=hexc('#2f8a83' if mine else '#EFE3C8'), outline=hexc(DARK), width=3 * S)
        for j, l in enumerate(ls):
            d.text((x0 + 28 * S, yy + 17 * S + j * 48 * S), l, font=f, fill=hexc('#FFFFFF' if mine else DARK))
    return img.resize((img.width // S, img.height // S), Image.LANCZOS)


def chat_settle(msgs):
    return 0.35 + len(msgs) * 1.1 + 0.2


def make_panel(blocks, prog):
    if blocks and blocks[0][0] == 'chat':
        return chat_panel(blocks[0][1], blocks[0][2], prog)
    return R2.panel(blocks, prog)


def settle(blocks):
    if blocks and blocks[0][0] == 'chat':
        return chat_settle(blocks[0][2])
    return R2.panel_settle(blocks)


def is_static(blocks):
    if blocks and blocks[0][0] == 'chat':
        return False
    return R2.panel_static(blocks)


# ------------------------------------------------------------------ montaggio
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
            for k, v in SUBST:
                s = s.replace(k, v)
            # sottotitoli mai su tre righe: una frase lunga si divide sulla virgola più vicina al centro
            if subtitle(s).height > 160 and ',' in s:
                cut = min((i for i, ch in enumerate(s) if ch == ','), key=lambda i: abs(i - len(s) / 2))
                s1, s2 = s[:cut + 1].strip(), s[cut + 1:].strip()
                m = a + (b - a) * len(s1) / max(1, len(s1) + len(s2))
                timeline.append(('sub', start + a, start + m, s1)); timeline.append(('sub', start + m, start + b, s2[0].upper() + s2[1:] if False else s2))
                continue
            timeline.append(('sub', start + a, start + b, s))
        segs.append(y); t += len(y) / SR
        need = settle(sc['panel']) + 0.8
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
    scenes = [e for e in timeline if e[0] == 'scene']

    # effetti sonori
    SR2 = 44100
    fx = np.zeros(int(total * SR2) + SR2, np.float32)
    def add(sig, at, gain):
        i = int(max(0, at) * SR2); fx[i:i + len(sig)] += sig[:len(fx) - i] * gain
    wh, tk, cl = sfx_whoosh(), sfx_tick(), sfx_clank()
    for e in scenes[1:]:
        add(wh, e[1] - 0.12, 0.35)
    for e in scenes:
        sc = C.SCENE[e[3]]
        for b in sc['panel']:
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
            if b[0] == 'chat':
                for k in range(len(b[2])):
                    add(tk, e[1] + 0.35 + k * 1.1, 0.45)
        if sc.get('scossa'):
            add(cl, e[1] + 0.1, 0.45)
        if sc.get('pop'):
            add(wh, e[1] + 0.5, 0.3)
    add(cl, total - LOOP - 0.05, 0.2)
    wav_write(os.path.join(outdir, 'fx.wav'), fx, SR2)

    # livelli fissi
    cov = Image.open(os.path.join(S2, 'copertine', f'reel{C.NUM}_copertina.png')).convert('RGBA')
    g = np.zeros((H, W, 4), np.uint8); g[..., :3] = (42, 30, 22)
    g[..., 3] = (np.clip((np.arange(H) - 1440) / 340, 0, 1) * 225)[:, None].astype(np.uint8)
    cov_sub = Image.alpha_composite(cov, Image.fromarray(g))        # copertina con il fondo scurito per i sottotitoli
    base = background(C.NUM)
    card = G.title_card(C.NUM, getattr(C, 'CARD_ROT', -1.2))
    card = card.resize((int(card.width * 0.8), int(card.height * 0.8)), Image.LANCZOS)
    nb = notebook()
    bdg = badge_dark()
    EX0 = getattr(C, 'EDWIN_X', 540)
    dev = G.sticker(G.device_img(C.NUM, 300), 14, getattr(C, 'DEV_ROT', 6))
    dev_x = getattr(C, 'DEV_X', 880 if EX0 <= 540 else 200)
    pops = {}

    SB, SH = 0.74, 0.85
    heads, bodies = {}, {}
    def head(m, e):
        k = (m, e)
        if k not in heads:
            p = os.path.join(CACHE, f'h_{m}_{e}.png')
            if not os.path.exists(p):
                render(head_svg(m / 5, e), p, SH)
            heads[k] = Image.open(p).convert('RGBA')
        return heads[k]
    def body(r, a, pose):
        k = (r, a, pose)
        if k not in bodies:
            p = os.path.join(CACHE, f'b_{pose}_{r}_{a}.png')
            if not os.path.exists(p):
                render(body_svg(gear_rot=r * 3.75, arm=a / 3, pose=pose), p, SB)
            bodies[k] = Image.open(p).convert('RGBA')
        return bodies[k]
    bw0 = body(0, 0, 'banco').width
    BH = body(0, 0, 'banco').height

    edcache = {}
    def edwin_sticker(gr, ar, pose, m, eyes, bob, tilt):
        bi = body(gr, ar, pose)
        hd = head(m, eyes)
        ed = Image.new('RGBA', (max(bi.width, hd.width), BH + hd.height), (0, 0, 0, 0))
        by = ed.height - bi.height
        ed.alpha_composite(bi, ((ed.width - bi.width) // 2, by + bob // 2))
        hy = by + int(SB * 170) - hd.height + int(SB * 48) + bob
        ed.alpha_composite(hd, ((ed.width - hd.width) // 2, max(0, hy)))
        ed = ed.crop(ed.getbbox())
        if tilt:
            ed = ed.rotate(tilt, resample=Image.BICUBIC, expand=True)
        return outline(ed, 14)

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
    ex_prev = EX0
    for f in range(nfr):
        ts = f / FPS
        cur, s0, s1 = 0, 0.0, 1.0
        for e in scenes:
            if e[1] <= ts + 1e-6:
                cur, s0, s1 = e[3], e[1], e[2]
        in_loop = ts >= total - LOOP
        sc = C.SCENE[cur]
        prog = ts - s0
        blocks = sc['panel']
        # pannello: entra come un adesivo che si attacca (piccolo rimbalzo)
        if is_static(blocks) or prog > settle(blocks) + 0.1:
            pk, pp = (cur, 'fine'), 99.0
        else:
            q = round(prog * 15) / 15; pk, pp = (cur, q), q
        if pk not in pcache:
            im = make_panel(blocks, pp)
            rot = sc.get('rot', ((cur * 37) % 5 - 2) * 0.6)
            pcache[pk] = im.rotate(rot, resample=Image.BICUBIC, expand=True) if rot else im
        pim = pcache[pk]
        kf = 1.0 if (cur == 0 and ts < 2) else min(1.0, prog / 0.3)
        # Edwin: posizione (si sposta tra una scena e l'altra), posa, bocca, occhi
        ex_target = sc.get('x', EX0)
        ex_from = C.SCENE[cur - 1].get('x', EX0) if cur > 0 else EX0
        mv = min(1.0, prog / 0.5); mv = mv * mv * (3 - 2 * mv)
        ex = ex_from + (ex_target - ex_from) * mv
        talk = sm[f]
        m = int(round(min(5, talk * 6)))
        kinds = [b[0] for b in blocks]
        pose = sc.get('posa') or (getattr(C, 'POSA', 'banco') if cur == 0 else ('indica' if ('rows' in kinds or 'buttons' in kinds) and prog > 0.8 else getattr(C, 'POSA', 'banco')))
        if pose == 'regge':            # nei Reel il congegno sta sul taccuino: mani mai chiuse sul vuoto
            pose = 'banco'
        eyes = 'blink' if f in blinks else 'open'
        if ('buttons' in kinds and 1.4 <= prog < 2.2) or ('stamp' in kinds and 1.25 <= prog < 2.0) or (cur == last and talk < 0.05 and not in_loop and ts > total - LOOP - 0.7):
            eyes = 'happy'
        if sc.get('scossa'):           # quando Edwin sbaglia non fa mai gli occhi felici
            eyes = ('blink' if int(prog * 8) % 2 else 'open') if prog < 1.2 else ('blink' if f in blinks else 'open')
        bob = int(3 * math.sin(ts * 2 * math.pi * 0.6) + 4 * talk)
        tilt = sc.get('tilt', 0) + (math.sin(prog * 40) * 3 * max(0, 1 - prog) if sc.get('scossa') else 0)
        gr = f % 8 if talk > 0.1 else (f // 3) % 8
        ar = int(min(3, round(armv[f] * 4.5)))
        ekey = (pose, gr, ar, m, eyes, bob, round(tilt, 1))
        if ekey in edcache:
            eds, pad = edcache[ekey]
        else:
            eds, pad = edwin_sticker(gr, ar, pose, m, eyes, bob, tilt)
            if len(edcache) < 1500:
                edcache[ekey] = (eds, pad)
        frame = base.copy()
        frame.alpha_composite(eds, (int(ex - eds.width / 2), int(DESK + 90 - eds.height + pad)))
        # congegno che salta fuori (pop)
        if sc.get('pop') and prog > 0.45:
            pn = sc['pop']
            if pn not in pops:
                pops[pn] = G.sticker(G.device_img(pn, 260), 12, -8)
            k = min(1.0, (prog - 0.45) / 0.35); s = 0.4 + 0.6 * (1 - (1 - k) ** 3) + 0.08 * math.sin(k * math.pi)
            pi = pops[pn].resize((max(1, int(pops[pn].width * s)), max(1, int(pops[pn].height * s))), Image.BICUBIC)
            px = 860 if ex < 540 else 220
            frame.alpha_composite(pi, (int(px - pi.width / 2), int(1150 - pi.height / 2)))
        frame.alpha_composite(nb, (-80, DESK - 40))
        frame.alpha_composite(dev, (int(dev_x - dev.width / 2), int(DESK + 20 - dev.height * 0.55)))
        # zoom di scena (primo piano su Edwin nelle battute)
        z = 1.0 + 0.025 * min(1.0, prog / max(1.0, s1 - s0))
        if sc.get('zoom'):
            zk = min(1.0, prog / 0.4); zk = zk * zk * (3 - 2 * zk)
            z += (0.16 if pim.height <= 440 else 0.07) * zk   # pannelli alti: primo piano più leggero, l'antenna non tocca il pannello
        if z > 1.001:
            zw, zh = int(W * z), int(H * z)
            cx = (ex / W) * zw - W / 2 if sc.get('zoom') else (zw - W) / 2
            cx = max(0, min(zw - W, cx))
            ky = 0.47 if sc.get('zoom') else 0.78   # nel primo piano la testa resta ferma e non va sotto il pannello
            frame = frame.resize((zw, zh), Image.BILINEAR).crop((int(cx), int((zh - H) * ky), int(cx) + W, int((zh - H) * ky) + H))
        frame.alpha_composite(card, (int(W / 2 - card.width / 2), 34))
        if kf < 1:
            ease = 1 - (1 - kf) ** 3
            s = 0.86 + 0.14 * ease + 0.04 * math.sin(kf * math.pi)
            p2 = pim.resize((max(1, int(pim.width * s)), max(1, int(pim.height * s))), Image.BICUBIC)
            a = np.array(p2); a[..., 3] = (a[..., 3] * min(1, ease * 1.4)).astype(np.uint8); p2 = Image.fromarray(a)
            frame.alpha_composite(p2, (int(PX0 - 10 + (pim.width - p2.width) / 2), int(PY0 + (pim.height - p2.height) / 2)))
        else:
            frame.alpha_composite(pim, (PX0 - 10, PY0))
        s_txt = None
        for e in timeline:
            if e[0] == 'sub' and (e[1] - 0.05 if e[1] > 0.5 else 0) <= ts < e[2] + 0.4:
                s_txt = e[3]
        if s_txt and s_txt not in subs:
            subs[s_txt] = subtitle(s_txt)
        if s_txt and not in_loop:
            frame.alpha_composite(subs[s_txt], ((W - subs[s_txt].width) // 2, 1640))
        frame.alpha_composite(bdg, (0, 1846))
        if ts < INTRO + XF:
            p = 0.0 if ts < INTRO else (ts - INTRO) / XF; p = p * p * (3 - 2 * p)
            frame = Image.blend(cov_sub, frame, p) if p > 0 else cov_sub.copy()
            frame.alpha_composite(bdg, (0, 1846))
            if s_txt:
                frame.alpha_composite(subs[s_txt], ((W - subs[s_txt].width) // 2, 1640))
        elif in_loop:
            p = min(1.0, (ts - (total - LOOP)) / XF); p = p * p * (3 - 2 * p)
            frame = Image.blend(frame, cov_sub, p) if p < 1 else cov_sub.copy()
            frame.alpha_composite(bdg, (0, 1846))
        pr.stdin.write(frame.tobytes())
    pr.stdin.close(); pr.wait()
    with open(os.path.join(outdir, 'copione.txt'), 'w') as fh:
        for e in timeline:
            if e[0] == 'sub':
                fh.write(f'{e[1]:6.2f}-{e[2]:6.2f}  {e[3]}\n')
    print('fatto', outdir, round(total, 1), 's')


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
