"""Edwin Arc disegnato in SVG (stile piatto dei Reel), sprite per testa e corpo."""
import subprocess, os

GOLD, GOLD_L, BRASS, COPPER, COPPER_D = '#D9A04A', '#E8B95C', '#C08A3E', '#9C4A26', '#7A3519'
BROWN, DARK, CYAN, CREAM = '#5A341C', '#2A1E16', '#3FE0D0', '#F3E9D2'

W, H = 600, 560  # tela della testa


def head_svg(mouth=0.0, eyes='open', glow=1.0):
    """mouth 0..1, eyes: open | blink | happy"""
    ry = 4 + 15 * mouth
    if eyes == 'open':
        le = f'''<circle cx="235" cy="330" r="27" fill="{CYAN}"/><circle cx="244" cy="320" r="7" fill="#d9fffb"/>'''
        re_ = f'''<circle cx="365" cy="330" r="29" fill="{CYAN}"/><circle cx="375" cy="319" r="7.5" fill="#d9fffb"/>'''
    elif eyes == 'blink':
        le = f'<rect x="210" y="326" width="50" height="8" rx="4" fill="{CYAN}"/>'
        re_ = f'<rect x="338" y="326" width="54" height="8" rx="4" fill="{CYAN}"/>'
    else:  # happy ^ ^
        le = f'<path d="M212 340 Q235 306 258 340" stroke="{CYAN}" stroke-width="10" fill="none" stroke-linecap="round"/>'
        re_ = f'<path d="M340 340 Q365 304 390 340" stroke="{CYAN}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    spring = 'M300 190 ' + ' '.join(f'L{285 if i % 2 else 315} {180 - i * 11}' for i in range(7)) + ' L300 100'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <radialGradient id="glow"><stop offset="0" stop-color="{CYAN}" stop-opacity="{0.55 * glow:.2f}"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
 <linearGradient id="head" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GOLD_L}"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
</defs>
<circle cx="300" cy="78" r="70" fill="url(#glow)"/>
<path d="{spring}" stroke="{COPPER}" stroke-width="8" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
<rect x="294" y="186" width="12" height="20" fill="{BRASS}"/>
<circle cx="300" cy="78" r="25" fill="{CYAN}"/><circle cx="292" cy="70" r="8" fill="#e6fffc"/>
<ellipse cx="300" cy="205" rx="46" ry="18" fill="{COPPER}"/>
<circle cx="138" cy="335" r="30" fill="{COPPER}"/><circle cx="138" cy="335" r="14" fill="{COPPER_D}"/>
<circle cx="462" cy="335" r="30" fill="{COPPER}"/><circle cx="462" cy="335" r="14" fill="{COPPER_D}"/>
<rect x="148" y="200" width="304" height="282" rx="48" fill="url(#head)"/>
<path d="M148 420 Q148 482 196 482 L404 482 Q452 482 452 420 Z" fill="{BRASS}" opacity="0.45"/>
<rect x="188" y="226" width="224" height="36" rx="18" fill="{BROWN}"/>
<circle cx="258" cy="244" r="13" fill="{BRASS}"/><circle cx="258" cy="244" r="8" fill="{CYAN}"/>
<circle cx="342" cy="244" r="13" fill="{BRASS}"/><circle cx="342" cy="244" r="8" fill="{CYAN}"/>
<circle cx="235" cy="330" r="50" fill="{COPPER}"/><circle cx="235" cy="330" r="38" fill="{DARK}"/>
<circle cx="365" cy="330" r="52" fill="{GOLD_L}" stroke="{BRASS}" stroke-width="6"/><circle cx="365" cy="330" r="40" fill="{DARK}"/>
{le}{re_}
<path d="M414 352 Q426 395 418 440" stroke="{BROWN}" stroke-width="4" stroke-dasharray="4 6" fill="none" stroke-linecap="round"/>
<circle cx="418" cy="442" r="6" fill="{BROWN}"/>
<ellipse cx="300" cy="{424 + ry * 0.35:.1f}" rx="{24 + 4 * mouth:.1f}" ry="{ry:.1f}" fill="{DARK}"/>
<ellipse cx="300" cy="{426 + ry * 0.75:.1f}" rx="{12 + 3 * mouth:.1f}" ry="{max(0.1, ry * 0.35):.1f}" fill="{COPPER}" opacity="{min(1, mouth * 2):.2f}"/>
<path d="M300 392 C270 378 236 384 214 404 C206 412 214 420 226 416 C250 406 278 412 300 412 C322 412 350 406 374 416 C386 420 394 412 386 404 C364 384 330 378 300 392 Z" fill="{BROWN}"/>
<circle cx="172" cy="226" r="5" fill="{COPPER_D}"/><circle cx="428" cy="226" r="5" fill="{COPPER_D}"/>
<circle cx="172" cy="456" r="5" fill="{COPPER_D}"/><circle cx="428" cy="456" r="5" fill="{COPPER_D}"/>
<rect x="250" y="482" width="100" height="16" fill="{BROWN}"/><rect x="244" y="498" width="112" height="12" rx="4" fill="{BRASS}"/>
<rect x="250" y="510" width="100" height="16" fill="{BROWN}"/><rect x="244" y="526" width="112" height="12" rx="4" fill="{BRASS}"/>
<rect x="250" y="538" width="100" height="22" fill="{BROWN}"/>
</svg>'''


def gear(cx, cy, r, teeth, color, hole=DARK, rot=0):
    import math
    pts = []
    for i in range(teeth * 4):
        a = math.radians(rot) + i * math.pi * 2 / (teeth * 4)
        rr = r if (i % 4) in (0, 1) else r * 0.84
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return (f'<polygon points="{" ".join(pts)}" fill="{color}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 0.62:.1f}" fill="{color}" stroke="{COPPER_D}" stroke-width="4"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * 0.24:.1f}" fill="{hole}"/>')


def body_svg(gear_rot=0, core=1.0, arm=0.0, pose='banco'):
    """Busto con braccia attaccate alle spalle: spalla, braccio, gomito, avambraccio, mano sul banco.
    arm: 0..1 piccolo movimento del braccio destro (gesto mentre parla)."""
    def limb(x1, y1, x2, y2, w, col, edge):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{edge}" stroke-width="{w + 8}" stroke-linecap="round"/>'
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
    def hand(x, y, flip=1, ang=0.0, kind='pugno'):
        """Mano con le dita lungo la direzione dell'avambraccio (ang in gradi, 0 = dita in giù)."""
        if abs(((ang + 180) % 360) - 180) > 90:   # mano alzata: palmo verso chi guarda, pollice verso la testa
            flip = -flip
        return (f'<g transform="translate({x} {y}) rotate({ang:.1f}) scale({flip} 1)">'
                f'<rect x="-30" y="-26" width="60" height="44" rx="16" fill="{GOLD}" stroke="{COPPER_D}" stroke-width="4"/>'
                + fingers(kind) + '</g>')
    def fingers(kind):
        r = lambda x, y, w, h: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{GOLD}" stroke="{COPPER_D}" stroke-width="4"/>'
        thumb = r(22, -18, 18, 26)
        if kind == 'aperta':      # mano aperta che saluta
            return (f'<g transform="rotate(12 -22 10)">{r(-30, 8, 15, 34)}</g>' + r(-12, 12, 15, 38) + f'<g transform="rotate(-10 14 10)">{r(6, 10, 15, 34)}</g>'
                    + f'<g transform="rotate(-35 30 -6)">{r(24, -16, 16, 32)}</g>')
        return r(-30, 8, 16, 22) + r(-11, 10, 16, 22) + r(8, 8, 16, 22) + thumb
    import math as _m
    def ang(ex, ey, hx, hy):
        return _m.degrees(_m.atan2(hy - ey, hx - ex)) - 90

    # spalle (dentro il busto), gomiti in fuori, mani sul banco
    lsx, lsy, lex, ley, lhx, lhy = 238, 96, 148, 300, 228, 452
    rsx, rsy = 522, 96
    rex, rey = 612 + 8 * arm, 300 - 14 * arm
    rhx, rhy = 532 + 10 * arm, 452 - 30 * arm
    if pose == 'regge':      # tiene un oggetto davanti al petto
        lex, ley, lhx, lhy = 160, 270, 282, 330 - 8 * arm
        rex, rey, rhx, rhy = 600, 270, 478, 330 - 8 * arm
    elif pose == 'indica':   # braccio destro alzato verso il pannello
        rex, rey = 650, 60 - 10 * arm
        rhx, rhy = 640 + 6 * arm, -80 - 20 * arm
    elif pose == 'saluta':   # mano destra che saluta
        rex, rey = 660, 120
        rhx, rhy = 700 + 30 * arm, -10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="690" viewBox="-20 -170 800 690">
<defs><radialGradient id="core"><stop offset="0" stop-color="#e6fffc"/><stop offset="0.45" stop-color="{CYAN}"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient></defs>
{gear(200, 70, 78, 12, COPPER, rot=gear_rot)}
{gear(560, 70, 78, 12, COPPER, rot=-gear_rot)}
<path d="M232 48 Q380 22 528 48 L560 480 L200 480 Z" fill="{BROWN}"/>
<path d="M262 50 L338 480 L292 480 L232 58 Z" fill="{COPPER}"/>
<path d="M498 50 L422 480 L468 480 L528 58 Z" fill="{COPPER}"/>
<rect x="214" y="160" width="332" height="24" fill="{BRASS}"/>
<circle cx="380" cy="250" r="{70 + 12 * core:.1f}" fill="url(#core)" opacity="{0.6 + 0.4 * core:.2f}"/>
<circle cx="380" cy="250" r="46" fill="{BRASS}"/><circle cx="380" cy="250" r="34" fill="{DARK}"/>
<circle cx="380" cy="250" r="24" fill="{CYAN}"/><circle cx="372" cy="242" r="7" fill="#e6fffc"/>
{limb(lsx, lsy, lex, ley, 46, BRASS, COPPER_D)}
{limb(lex, ley, lhx, lhy - 10, 42, GOLD, COPPER_D)}
{limb(rsx, rsy, rex, rey, 46, BRASS, COPPER_D)}
{limb(rex, rey, rhx, rhy - 10, 42, GOLD, COPPER_D)}
<circle cx="{lsx}" cy="{lsy}" r="44" fill="{COPPER}" stroke="{COPPER_D}" stroke-width="4"/><circle cx="{lsx}" cy="{lsy}" r="16" fill="{COPPER_D}"/>
<circle cx="{rsx}" cy="{rsy}" r="44" fill="{COPPER}" stroke="{COPPER_D}" stroke-width="4"/><circle cx="{rsx}" cy="{rsy}" r="16" fill="{COPPER_D}"/>
<circle cx="{lex}" cy="{ley}" r="26" fill="{COPPER}" stroke="{COPPER_D}" stroke-width="4"/><circle cx="{lex}" cy="{ley}" r="9" fill="{COPPER_D}"/>
<circle cx="{rex:.1f}" cy="{rey:.1f}" r="26" fill="{COPPER}" stroke="{COPPER_D}" stroke-width="4"/><circle cx="{rex:.1f}" cy="{rey:.1f}" r="9" fill="{COPPER_D}"/>
{hand(lhx, lhy, 1, ang(lex, ley, lhx, lhy))}
{hand(rhx, rhy, -1, ang(rex, rey, rhx, rhy), {'indica': 'aperta', 'saluta': 'aperta'}.get(pose, 'pugno'))}
</svg>'''


def render(svg, png, scale=1.0):
    p = png + '.svg'
    open(p, 'w').write(svg)
    subprocess.run(['rsvg-convert', '-z', str(scale), '-o', png, p], check=True)
    os.remove(p)
