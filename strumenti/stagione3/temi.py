"""Stagione 3 "L'atlante del viaggiatore": argomenti e disegni dei congegni (SVG 500x500).
Le puntate della rubrica "Prima e dopo" (56, 62, 68, 74, 80) non hanno congegno: hanno la cartolina (griglia.py)."""
import math
DK = '#2A1E16'
O = f'stroke="{DK}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"'
O6 = f'stroke="{DK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
CR, PA, BR, CU, MU, TE, RO, GO, BW = '#F7F0E0', '#FBF7EC', '#C08A3E', '#B45A30', '#DCA24A', '#2f8a83', '#B3261E', '#E3B657', '#5A341C'
NV, SK, GR = '#2E4A62', '#9CC3C9', '#6E9E5A'
PED = (56, 62, 68, 74, 80)


def lines(x, y, w, n, gap=30, col='#8C7350', sw=8, var=(1, .8, .9, .6, .85)):
    return ''.join(f'<line x1="{x}" y1="{y + i * gap}" x2="{x + w * var[i % len(var)]:.0f}" y2="{y + i * gap}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>' for i in range(n))


def check(x, y, s=1.0, col=TE):
    return f'<path d="M{x - 14 * s} {y} l{10 * s} {11 * s} l{20 * s} {-24 * s}" fill="none" stroke="{col}" stroke-width="{9 * s}" stroke-linecap="round" stroke-linejoin="round"/>'


def phone(x, y, w, h, inner=''):
    return (f'<g transform="translate({x} {y})"><rect x="0" y="0" width="{w}" height="{h}" rx="{w * 0.16:.0f}" fill="{DK}"/>'
            f'<rect x="{w * 0.07:.0f}" y="{h * 0.07:.0f}" width="{w * 0.86:.0f}" height="{h * 0.84:.0f}" rx="{w * 0.08:.0f}" fill="{PA}"/>'
            f'<rect x="{w * 0.38:.0f}" y="{h * 0.025:.0f}" width="{w * 0.24:.0f}" height="{h * 0.025:.0f}" rx="4" fill="#4a3a2e"/>{inner}</g>')


def browser(x, y, w, h, bar=DK, fill=PA):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" {O}/><rect x="{x}" y="{y}" width="{w}" height="54" rx="16" fill="{bar}" {O}/>'
            + ''.join(f'<circle cx="{x + 32 + i * 30}" cy="{y + 27}" r="9" fill="{c}"/>' for i, c in enumerate((RO, MU, TE))))


def star(cx, cy, r, col):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{col}" {O6}/>'


def pin(x, y, col=RO, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 C-30 -40 -34 -60 -34 -76 A34 34 0 0 1 34 -76 C34 -60 30 -40 0 0 Z" fill="{col}" {O6}/>'
            f'<circle cx="0" cy="-76" r="12" fill="{CR}" stroke="{DK}" stroke-width="5"/></g>')


DEV = {}
# 55 la prima app: il telefono con le spunte delle abitudini e la serie di giorni
DEV[55] = (phone(140, 30, 220, 440,
                 f'<rect x="15" y="31" width="190" height="60" rx="14" fill="{TE}"/><text x="110" y="72" font-family="Lora" font-weight="700" font-size="28" text-anchor="middle" fill="#fff">Abitudini</text>'
                 + ''.join(f'<rect x="30" y="{112 + i * 66}" width="44" height="44" rx="10" fill="#fff" stroke="{DK}" stroke-width="5"/><line x1="90" y1="{134 + i * 66}" x2="{180 - (i % 2) * 30}" y2="{134 + i * 66}" stroke="#8C7350" stroke-width="8" stroke-linecap="round"/>' for i in range(4))
                 + check(52, 134) + check(52, 200) + check(52, 266)
                 + ''.join(f'<circle cx="{40 + i * 28}" cy="390" r="10" fill="{GO if i < 5 else "#E6DCC6"}" stroke="{DK}" stroke-width="3"/>' for i in range(6)))
           + f'<g transform="translate(420 130)"><rect x="-14" y="-82" width="28" height="22" rx="4" fill="{BR}" {O6}/><circle r="64" fill="{MU}" {O}/><circle r="48" fill="{CR}" {O6}/>'
           + f'<path d="M0 0 L0 -48 A48 48 0 0 1 41.6 24 Z" fill="{TE}" opacity="0.8"/><line x1="0" y1="0" x2="0" y2="-40" stroke="{DK}" stroke-width="7" stroke-linecap="round"/><circle r="7" fill="{DK}"/>'
           + f'<text x="0" y="104" font-family="Lora" font-weight="700" font-size="30" text-anchor="middle" fill="{DK}">5 min</text></g>')
# 57 la mappa interattiva del viaggio: carta piegata con le tappe e il percorso
DEV[57] = (f'<path d="M50 120 L170 80 L300 120 L450 80 L450 400 L300 440 L170 400 L50 440 Z" fill="{PA}" {O}/>'
           + f'<path d="M170 80 L170 400 M300 120 L300 440" stroke="#C8B89A" stroke-width="6"/>'
           + f'<path d="M60 300 q60 -30 90 10 q40 50 90 0 q50 -60 110 -20 q30 20 70 -10" fill="none" stroke="{SK}" stroke-width="22" stroke-linecap="round"/>'
           + f'<path d="M110 370 C150 250 240 340 260 230 S360 160 390 200" fill="none" stroke="{RO}" stroke-width="9" stroke-dasharray="18 14" stroke-linecap="round"/>'
           + pin(110, 370, TE, 0.8) + pin(260, 236, MU, 0.8) + pin(390, 204, RO, 1.0)
           + f'<g transform="translate(360 300)"><rect x="0" y="0" width="120" height="80" rx="10" fill="#fff" {O6}/><rect x="10" y="10" width="100" height="40" fill="{SK}"/><path d="M10 50 l30 -26 l22 18 l18 -12 l30 20 Z" fill="{GR}"/><line x1="14" y1="64" x2="80" y2="64" stroke="#8C7350" stroke-width="6"/></g>')
# 58 il sito per l'attività: pagina con tenda del negozio, orari, mappa e pulsante per scrivere
DEV[58] = (browser(40, 60, 420, 380)
           + ''.join(f'<path d="M{70 + i * 60} 130 l60 0 l0 40 a30 30 0 0 1 -60 0 Z" fill="{(RO, CR)[i % 2]}" {O6}/>' for i in range(6))
           + f'<text x="250" y="240" font-family="Lora" font-weight="700" font-size="36" text-anchor="middle" fill="{DK}">Bottega</text>'
           + lines(80, 280, 150, 3, 30, sw=7)
           + f'<rect x="270" y="262" width="160" height="100" rx="8" fill="{SK}" {O6}/><path d="M270 330 q50 -30 80 0 t80 -10" fill="none" stroke="{GR}" stroke-width="12"/>' + pin(350, 316, RO, 0.55)
           + f'<rect x="80" y="380" width="200" height="44" rx="22" fill="{GR}" {O6}/><path d="M118 392 a14 14 0 1 1 -6 22 l-10 4 l4 -10 a14 14 0 0 1 12 -16 Z" fill="#fff"/><line x1="146" y1="402" x2="250" y2="402" stroke="#fff" stroke-width="8" stroke-linecap="round"/>')
# 59 cambiarlo a parole: la pagina con il pennello e il fumetto della richiesta
DEV[59] = (browser(40, 110, 320, 300)
           + f'<rect x="70" y="190" width="260" height="70" rx="8" fill="{TE}" {O6}/>' + lines(80, 300, 220, 3, 30, sw=7)
           + ''.join(f'<rect x="{80 + i * 70}" y="{380}" width="54" height="16" rx="6" fill="{c}"/>' for i, c in enumerate((RO, MU, TE)))
           + f'<path d="M260 30 h200 a24 24 0 0 1 24 24 v70 a24 24 0 0 1 -24 24 h-120 l-40 34 l6 -34 h-46 a24 24 0 0 1 -24 -24 v-70 a24 24 0 0 1 24 -24 Z" fill="#fff" {O}/>'
           + f'<text x="360" y="80" font-family="Lora" font-style="italic" font-weight="700" font-size="30" text-anchor="middle" fill="{DK}">più grande,</text><text x="360" y="118" font-family="Lora" font-style="italic" font-weight="700" font-size="30" text-anchor="middle" fill="{TE}">verde!</text>'
           + f'<g transform="translate(400 330) rotate(35)"><rect x="-18" y="-130" width="36" height="140" rx="10" fill="{BW}" {O6}/><rect x="-22" y="10" width="44" height="30" fill="{BR}" {O6}/><path d="M-22 40 Q-26 90 0 110 Q26 90 22 40 Z" fill="{TE}" {O6}/></g>')
# 60 pubblicarlo con un link: mappamondo e anello di catena
DEV[60] = (f'<g transform="translate(220 230)"><circle r="170" fill="{SK}" {O}/>'
           + f'<path d="M-120 -70 q40 -40 90 -20 q30 30 0 60 q-40 10 -50 50 q-30 10 -50 -30 Z" fill="{GR}" {O6}/><path d="M30 40 q50 -30 90 10 q10 50 -30 80 q-40 0 -60 -40 Z" fill="{GR}" {O6}/><path d="M40 -120 q40 0 60 30 q-30 20 -60 0 Z" fill="{GR}" {O6}/>'
           + f'<ellipse rx="170" ry="60" fill="none" stroke="{DK}" stroke-width="4" stroke-opacity="0.4"/><ellipse rx="70" ry="170" fill="none" stroke="{DK}" stroke-width="4" stroke-opacity="0.4"/></g>'
           + f'<g transform="translate(360 380) rotate(-35)"><rect x="-110" y="-38" width="130" height="76" rx="38" fill="none" stroke="{DK}" stroke-width="40"/><rect x="-110" y="-38" width="130" height="76" rx="38" fill="none" stroke="{GO}" stroke-width="24"/>'
           + f'<rect x="-20" y="-38" width="130" height="76" rx="38" fill="none" stroke="{DK}" stroke-width="40"/><rect x="-20" y="-38" width="130" height="76" rx="38" fill="none" stroke="{BR}" stroke-width="24"/></g>')
# 61 il videogioco: controller e un livello a piattaforme con il personaggio
DEV[61] = (f'<rect x="40" y="40" width="420" height="250" rx="16" fill="{NV}" {O}/>'
           + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" opacity="0.8"/>' for x, y in ((90, 80), (200, 70), (330, 90), (420, 70), (150, 120)))
           + f'<rect x="70" y="230" width="140" height="30" fill="{GR}" stroke="{DK}" stroke-width="5"/><rect x="250" y="180" width="110" height="30" fill="{GR}" stroke="{DK}" stroke-width="5"/><rect x="380" y="130" width="60" height="30" fill="{GR}" stroke="{DK}" stroke-width="5"/>'
           + star(410, 100, 18, GO)
           + f'<g transform="translate(140 196)"><rect x="-18" y="-34" width="36" height="34" rx="6" fill="{GO}" stroke="{DK}" stroke-width="4"/><circle cx="-6" cy="-20" r="5" fill="{TE}"/><circle cx="8" cy="-20" r="5" fill="{TE}"/><line x1="0" y1="-34" x2="0" y2="-46" stroke="{CU}" stroke-width="4"/><circle cx="0" cy="-48" r="5" fill="{TE}"/></g>'
           + f'<path d="M120 320 h260 a70 70 0 0 1 60 100 l-20 30 a40 40 0 0 1 -60 0 l-30 -40 h-100 l-30 40 a40 40 0 0 1 -60 0 l-20 -30 a70 70 0 0 1 60 -100 Z" fill="{CU}" {O}/>'
           + f'<path d="M150 360 v50 M125 385 h50" stroke="{DK}" stroke-width="14" stroke-linecap="round"/><circle cx="340" cy="370" r="14" fill="{GO}" {O6}/><circle cx="375" cy="400" r="14" fill="{TE}" {O6}/>')
# 63 la caccia al tesoro: forziere aperto, chiave e indovinello
DEV[63] = (f'<g transform="translate(40 50) rotate(-6)"><rect x="0" y="0" width="190" height="230" fill="{PA}" {O}/><text x="95" y="60" font-family="Lora" font-weight="700" font-size="60" text-anchor="middle" fill="{RO}">?</text>' + lines(25, 110, 140, 3, 34, sw=7) + '</g>'
           + f'<path d="M210 250 h240 v170 a10 10 0 0 1 -10 10 h-220 a10 10 0 0 1 -10 -10 Z" fill="{BW}" {O}/><path d="M210 250 q120 -150 240 0" fill="{CU}" {O}/>'
           + f'<rect x="210" y="250" width="240" height="28" fill="{BR}" {O6}/><rect x="310" y="270" width="40" height="50" rx="6" fill="{GO}" {O6}/><circle cx="330" cy="290" r="7" fill="{DK}"/>'
           + star(260, 205, 20, GO) + star(400, 200, 16, GO)
           + f'<g transform="translate(130 400) rotate(-20)"><circle cx="-60" cy="0" r="30" fill="none" stroke="{DK}" stroke-width="20"/><circle cx="-60" cy="0" r="30" fill="none" stroke="{GO}" stroke-width="10"/><rect x="-32" y="-8" width="110" height="16" fill="{GO}" {O6}/><rect x="50" y="8" width="12" height="24" fill="{GO}" {O6}/><rect x="70" y="8" width="12" height="18" fill="{GO}" {O6}/></g>')
# 64 il video dalle foto: pellicola con le foto e il tasto play
DEV[64] = (f'<g transform="rotate(-8 250 250)"><rect x="20" y="130" width="460" height="230" fill="{DK}"/>'
           + ''.join(f'<rect x="{34 + i * 40}" y="142" width="22" height="18" rx="3" fill="{CR}"/><rect x="{34 + i * 40}" y="330" width="22" height="18" rx="3" fill="{CR}"/>' for i in range(11))
           + ''.join(f'<rect x="{40 + i * 145}" y="172" width="130" height="146" rx="4" fill="{SK}"/>' for i in range(3))
           + f'<path d="M40 318 l50 -60 l30 30 l30 -40 l20 70 Z" fill="{GR}"/><circle cx="140" cy="210" r="16" fill="{GO}"/>'
           + f'<circle cx="250" cy="230" r="28" fill="{MU}"/><path d="M200 318 q50 -70 100 0 Z" fill="{CU}"/>'
           + f'<path d="M330 318 l40 -80 l40 80 Z" fill="{CR}"/><path d="M360 318 l40 -50 l40 50 Z" fill="{TE}"/></g>'
           + f'<circle cx="390" cy="410" r="62" fill="{RO}" {O}/><path d="M372 380 L372 440 L420 410 Z" fill="#fff"/>')
# 65 il video animato che spiega: ciak e lampadina
DEV[65] = (f'<g transform="translate(60 200)"><rect x="0" y="60" width="280" height="200" rx="10" fill="{DK}"/>'
           + f'<g transform="rotate(-16 0 60)"><rect x="0" y="0" width="280" height="56" rx="6" fill="{DK}"/>' + ''.join(f'<path d="M{20 + i * 60} 0 l40 0 l-20 56 l-40 0 Z" fill="#fff"/>' for i in range(5)) + '</g>'
           + lines(30, 120, 220, 3, 40, col='#E6DCC6', sw=8) + '</g>'
           + f'<g transform="translate(370 150)"><circle r="78" fill="{GO}" {O}/><rect x="-34" y="70" width="68" height="50" rx="8" fill="{BR}" {O6}/><line x1="-34" y1="90" x2="34" y2="90" stroke="{DK}" stroke-width="5"/>'
           + f'<path d="M-22 30 q22 -60 44 0" fill="none" stroke="{DK}" stroke-width="6"/>'
           + ''.join(f'<line x1="0" y1="-96" x2="0" y2="-126" stroke="{DK}" stroke-width="8" stroke-linecap="round" transform="rotate({a})"/>' for a in (-60, -30, 0, 30, 60)) + '</g>'
)
# 66 logo e colori: tavolozza di campioni, un marchio tondo e il pennino
DEV[66] = (''.join(f'<g transform="translate({100 + i * 34} {270 - i * 22}) rotate({-22 + i * 11} 50 200)"><rect x="0" y="0" width="100" height="210" rx="10" fill="#fff" {O6}/><rect x="0" y="0" width="100" height="130" rx="10" fill="{c}" {O6}/></g>' for i, c in enumerate((RO, MU, TE, NV)))
           + f'<g transform="translate(340 170)"><circle r="110" fill="{CR}" {O}/><circle r="86" fill="none" stroke="{TE}" stroke-width="10"/><path d="M-50 30 L0 -50 L50 30 Z" fill="{CU}" {O6}/><circle cx="0" cy="44" r="12" fill="{TE}"/></g>'
           + f'<g transform="translate(400 390) rotate(40)"><path d="M-24 -110 h48 v70 l-24 80 l-24 -80 Z" fill="{BR}" {O6}/><circle cx="0" cy="-20" r="8" fill="{DK}"/><line x1="0" y1="-12" x2="0" y2="36" stroke="{DK}" stroke-width="4"/></g>')
# 67 la dashboard: pannello con lancetta, barre e linea
DEV[67] = (f'<rect x="30" y="70" width="440" height="360" rx="20" fill="{NV}" {O}/>'
           + f'<rect x="56" y="96" width="180" height="150" rx="12" fill="{PA}"/><path d="M80 210 A66 66 0 0 1 212 210" fill="none" stroke="{TE}" stroke-width="18"/><path d="M174 156 A66 66 0 0 1 212 210" fill="none" stroke="{RO}" stroke-width="18"/><line x1="146" y1="210" x2="190" y2="160" stroke="{DK}" stroke-width="8" stroke-linecap="round"/><circle cx="146" cy="210" r="10" fill="{DK}"/>'
           + f'<rect x="258" y="96" width="186" height="150" rx="12" fill="{PA}"/>' + ''.join(f'<rect x="{278 + i * 40}" y="{226 - h}" width="26" height="{h}" fill="{c}"/>' for i, (h, c) in enumerate(((50, MU), (80, BR), (60, MU), (110, CU))))
           + f'<rect x="56" y="268" width="388" height="136" rx="12" fill="{PA}"/><path d="M80 380 L150 340 L210 360 L280 300 L340 320 L420 286" fill="none" stroke="{TE}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
           + ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{GO}" stroke="{DK}" stroke-width="4"/>' for x, y in ((150, 340), (280, 300), (420, 286))))
# 69 il calcolatore su misura: calcolatrice, auto e pompa del carburante
DEV[69] = (f'<rect x="50" y="50" width="240" height="380" rx="24" fill="{BW}" {O}/><rect x="76" y="80" width="188" height="80" rx="8" fill="#DDEBD8" {O6}/>'
           + f'<text x="250" y="138" font-family="Liberation Mono" font-weight="700" font-size="40" text-anchor="end" fill="{DK}">42,80</text>'
           + ''.join(f'<rect x="{80 + c * 62}" y="{184 + r * 58}" width="48" height="44" rx="8" fill="{(CR, CR, MU)[c] if r < 3 else (CR, CR, RO)[c]}" stroke="{DK}" stroke-width="5"/>' for r in range(4) for c in range(3))
           + f'<g transform="translate(370 330)"><path d="M-100 0 l20 -50 q10 -20 30 -20 h100 q20 0 30 20 l20 50 v40 h-200 Z" fill="{TE}" {O}/><rect x="-60" y="-60" width="50" height="40" rx="4" fill="{SK}"/><rect x="0" y="-60" width="50" height="40" rx="4" fill="{SK}"/>'
           + f'<circle cx="-60" cy="40" r="26" fill="{DK}"/><circle cx="-60" cy="40" r="10" fill="{CR}"/><circle cx="60" cy="40" r="26" fill="{DK}"/><circle cx="60" cy="40" r="10" fill="{CR}"/></g>'
           + f'<g transform="translate(400 110)"><rect x="-40" y="-60" width="80" height="140" rx="10" fill="{RO}" {O6}/><rect x="-26" y="-44" width="52" height="40" rx="4" fill="{CR}"/><path d="M40 -20 h22 v80 q0 20 -16 20" fill="none" stroke="{DK}" stroke-width="8"/></g>')
# 70 l'app che si ricorda i dati: telefono con la lista e il cassetto della memoria
DEV[70] = (phone(60, 40, 200, 410, ''.join(f'<rect x="24" y="{60 + i * 64}" width="152" height="46" rx="10" fill="#fff" stroke="{DK}" stroke-width="4"/><circle cx="46" cy="{83 + i * 64}" r="10" fill="{(TE, MU, CU, TE, MU)[i]}"/><line x1="66" y1="{83 + i * 64}" x2="{150 - (i % 3) * 18}" y2="{83 + i * 64}" stroke="#8C7350" stroke-width="7" stroke-linecap="round"/>' for i in range(5)))
           + f'<path d="M260 240 h40" stroke="{DK}" stroke-width="8" stroke-dasharray="10 8"/>'
           + f'<g transform="translate(310 160)"><path d="M0 30 v200 a75 26 0 0 0 150 0 v-200" fill="{BR}" {O}/><ellipse cx="75" cy="30" rx="75" ry="26" fill="{GO}" {O}/>'
           + f'<path d="M0 100 a75 26 0 0 0 150 0 M0 170 a75 26 0 0 0 150 0" fill="none" stroke="{DK}" stroke-width="7"/></g>'
           + f'<g transform="translate(385 120)"><circle r="40" fill="{TE}" {O6}/>' + check(0, 4, 1.4, '#fff') + '</g>')
# 71 l'app sulla schermata Home: telefono con le icone e la nuova icona d'ottone
DEV[71] = (phone(110, 30, 260, 450, ''.join(f'<rect x="{30 + c * 66}" y="{50 + r * 72}" width="50" height="50" rx="14" fill="{f}"/>' for r in range(4) for c in range(3) for f in [(TE, MU, CU, SK, RO, GR, MU, NV, TE, CU, SK, MU)[r * 3 + c]]))
           + f'<g transform="translate(240 380)"><rect x="-58" y="-58" width="116" height="116" rx="30" fill="{GO}" {O}/><circle r="30" fill="{BR}" {O6}/><circle r="12" fill="{TE}"/></g>'
           + f'<g transform="translate(400 160)"><circle r="46" fill="{TE}" {O}/><path d="M0 -24 v48 M-24 0 h48" stroke="#fff" stroke-width="12" stroke-linecap="round"/></g>'
           + f'<path d="M380 210 q-20 100 -80 140" fill="none" stroke="{DK}" stroke-width="7" stroke-dasharray="12 10" stroke-linecap="round"/>')
# 72 l'app dei turni di casa: ruota dei turni con scopa, piatti e bucato
DEV[72] = (f'<g transform="translate(250 280)"><circle r="200" fill="{PA}" {O}/>'
           + ''.join(f'<path d="M0 0 L{200 * math.cos(math.radians(a)):.1f} {200 * math.sin(math.radians(a)):.1f} A200 200 0 0 1 {200 * math.cos(math.radians(a + 90)):.1f} {200 * math.sin(math.radians(a + 90)):.1f} Z" fill="{c}" {O6}/>' for a, c in ((-90, TE), (0, MU), (90, CU), (180, SK)))
           + f'<g transform="translate(70 -70) rotate(30)"><rect x="-6" y="-70" width="12" height="90" fill="{BW}"/><path d="M-30 20 h60 l10 40 h-80 Z" fill="{GO}" {O6}/></g>'
           + f'<g transform="translate(75 75)"><ellipse rx="44" ry="16" fill="#fff" {O6}/><ellipse cy="-14" rx="44" ry="16" fill="#fff" {O6}/><ellipse cy="-28" rx="44" ry="16" fill="#fff" {O6}/></g>'
           + f'<g transform="translate(-75 75)"><rect x="-40" y="-40" width="80" height="80" rx="10" fill="#fff" {O6}/><circle r="24" fill="{SK}" {O6}/></g>'
           + f'<g transform="translate(-75 -75)"><path d="M-40 0 l20 -26 h40 l20 26 l-14 10 v34 h-52 v-34 Z" fill="{RO}" {O6}/></g>'
           + f'<circle r="34" fill="{BR}" {O}/><path d="M0 -20 L12 10 L-12 10 Z" fill="{DK}"/></g>'
           + f'<path d="M250 100 l-26 -46 h52 Z" fill="{RO}" {O6}/>')
# 73 il libretto in PDF: libro aperto impaginato
DEV[73] = (f'<path d="M250 110 Q160 70 40 90 V420 Q160 400 250 440 Z" fill="{PA}" {O}/><path d="M250 110 Q340 70 460 90 V420 Q340 400 250 440 Z" fill="{PA}" {O}/>'
           + f'<rect x="70" y="130" width="150" height="110" rx="6" fill="{SK}" {O6}/><path d="M70 240 l50 -50 l30 30 l30 -40 l40 60 Z" fill="{GR}"/><circle cx="110" cy="164" r="14" fill="{GO}"/>'
           + lines(74, 270, 140, 4, 30, sw=7)
           + f'<text x="355" y="160" font-family="Lora" font-weight="700" font-size="34" text-anchor="middle" fill="{CU}">Capitolo 1</text>'
           + lines(290, 200, 70, 6, 30, sw=6) + lines(380, 200, 60, 6, 30, sw=6)
           + f'<g transform="translate(410 400)"><rect x="-48" y="-30" width="96" height="60" rx="8" fill="{RO}" {O6}/><text x="0" y="12" font-family="Liberation Mono" font-weight="700" font-size="30" text-anchor="middle" fill="#fff">PDF</text></g>')
# 75 la presentazione animata: schermo con slide che entrano e linee di movimento
DEV[75] = (f'<rect x="40" y="60" width="420" height="290" rx="14" fill="{DK}" {O}/><rect x="60" y="80" width="380" height="250" rx="6" fill="{PA}"/>'
           + f'<rect x="90" y="110" width="200" height="30" rx="6" fill="{CU}"/>' + lines(90, 170, 150, 3, 34, sw=8)
           + f'<g transform="translate(330 200)"><circle r="56" fill="{TE}" stroke="{DK}" stroke-width="5"/><path d="M0 0 L0 -56 A56 56 0 0 1 48 28 Z" fill="{MU}" stroke="{DK}" stroke-width="5"/></g>'
           + f'<path d="M420 230 l-30 0 M420 250 l-50 0 M420 210 l-20 0" stroke="{RO}" stroke-width="8" stroke-linecap="round"/>'
           + f'<path d="M220 350 v60 M140 440 l80 -30 l80 30" fill="none" {O}/>'
           + f'<g transform="translate(400 410)"><circle r="48" fill="{RO}" {O}/><path d="M-14 -24 L-14 24 L24 0 Z" fill="#fff"/></g>')
# 76 il menù o volantino da stampare: stampante con il foglio che esce
DEV[76] = (f'<g transform="translate(140 30) rotate(-4)"><rect x="0" y="0" width="230" height="250" fill="#fff" {O}/><text x="115" y="56" font-family="Lora" font-weight="700" font-size="40" text-anchor="middle" fill="{RO}">MENÙ</text>'
           + ''.join(f'<line x1="30" y1="{90 + i * 34}" x2="150" y2="{90 + i * 34}" stroke="#8C7350" stroke-width="7" stroke-linecap="round"/><text x="200" y="{98 + i * 34}" font-family="Liberation Mono" font-weight="700" font-size="22" text-anchor="end" fill="{DK}">{p}</text>' for i, p in enumerate(('8', '12', '10', '6')))
           + '</g>'
           + f'<rect x="60" y="250" width="380" height="150" rx="20" fill="{BW}" {O}/><rect x="110" y="236" width="280" height="30" rx="6" fill="{DK}"/>'
           + f'<rect x="110" y="380" width="280" height="90" rx="6" fill="{CR}" {O6}/>' + lines(140, 410, 210, 2, 30, sw=6)
           + f'<circle cx="390" cy="300" r="14" fill="{GR}" {O6}/><rect x="300" y="290" width="60" height="20" rx="6" fill="{GO}"/>')
# 77 il catalogo della collezione: schede con francobolli e l'imbuto dei filtri
DEV[77] = (''.join(f'<g transform="translate({60 + c * 130} {70 + r * 160})"><rect x="0" y="0" width="110" height="140" rx="10" fill="#fff" {O6}/>'
                   f'<rect x="14" y="14" width="82" height="70" fill="{col}" stroke="{DK}" stroke-width="4" stroke-dasharray="6 5"/>'
                   f'<line x1="14" y1="104" x2="90" y2="104" stroke="#8C7350" stroke-width="6" stroke-linecap="round"/><line x1="14" y1="124" x2="64" y2="124" stroke="#8C7350" stroke-width="6" stroke-linecap="round"/></g>'
                   for r in range(2) for c in range(3) for col in [(RO, TE, MU, SK, CU, GR)[r * 3 + c]])
           + f'<g transform="translate(380 400)"><path d="M-80 -60 h160 l-60 70 v60 l-40 -20 v-40 Z" fill="{GO}" {O}/></g>'
           + f'<g transform="translate(160 420)"><rect x="-110" y="-30" width="220" height="60" rx="30" fill="#fff" {O6}/><circle cx="-70" cy="0" r="14" fill="none" stroke="{DK}" stroke-width="6"/><line x1="-60" y1="10" x2="-48" y2="22" stroke="{DK}" stroke-width="6"/><line x1="-30" y1="0" x2="70" y2="0" stroke="#8C7350" stroke-width="6" stroke-linecap="round"/></g>')
# 78 200 file sistemati: mucchio di fogli che diventa cartelle ordinate
DEV[78] = (''.join(f'<rect x="{40 + dx}" y="{120 + dy}" width="110" height="140" rx="6" fill="{c}" {O6} transform="rotate({a} {95 + dx} {190 + dy})"/>' for dx, dy, a, c in ((0, 60, -24, CR), (20, 20, 14, '#FFF6DA'), (-10, 0, -8, PA), (30, 80, 30, '#fff'), (10, 40, 4, CR)))
           + f'<text x="100" y="420" font-family="Lora" font-weight="700" font-size="56" text-anchor="middle" fill="{RO}">200</text>'
           + f'<path d="M200 250 h70" stroke="{DK}" stroke-width="14" stroke-linecap="round"/><path d="M260 220 l36 30 l-36 30" fill="none" stroke="{DK}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
           + ''.join(f'<g transform="translate(310 {90 + i * 110})"><path d="M0 0 h50 l14 -16 h86 v96 h-150 Z" fill="{c}" {O6}/><rect x="16" y="22" width="110" height="28" rx="4" fill="{CR}" stroke="{DK}" stroke-width="4"/></g>' for i, c in enumerate((TE, MU, CU)))
           + check(400, 440, 1.6, GR))
# 79 il sito completo in un pomeriggio: più pagine impilate e la clessidra
DEV[79] = (browser(130, 40, 320, 230, bar=TE) + browser(90, 100, 320, 230, bar=CU) + browser(50, 160, 320, 260)
           + f'<rect x="80" y="240" width="260" height="60" rx="8" fill="{SK}"/>' + lines(80, 330, 200, 2, 30, sw=7) + f'<rect x="80" y="380" width="120" height="26" rx="13" fill="{TE}"/>'
           + f'<g transform="translate(410 370)"><rect x="-56" y="-100" width="112" height="16" rx="6" fill="{BW}" {O6}/><rect x="-56" y="84" width="112" height="16" rx="6" fill="{BW}" {O6}/>'
           + f'<path d="M-44 -84 h88 q0 50 -44 84 q44 34 44 84 h-88 q0 -50 44 -84 q-44 -34 -44 -84 Z" fill="#E8F6F4" {O6}/><path d="M-26 -60 h52 q-10 30 -26 44 q-16 -14 -26 -44 Z" fill="{GO}"/><path d="M-34 74 q34 -40 68 0 Z" fill="{GO}"/></g>')
# 81 il tuo atlante: libro dell'atlante aperto, bussola e bandierina di arrivo
DEV[81] = (f'<path d="M250 140 Q150 100 30 120 V430 Q150 410 250 450 Z" fill="{PA}" {O}/><path d="M250 140 Q350 100 470 120 V430 Q350 410 250 450 Z" fill="{PA}" {O}/>'
           + f'<path d="M60 300 q40 -60 100 -30 q40 30 70 -10 V430 Q150 410 60 420 Z" fill="{SK}" opacity="0.8"/><path d="M90 220 q30 -40 70 -10 q20 30 -10 50 q-40 10 -60 -40 Z" fill="{GR}" {O6}/>'
           + f'<path d="M290 200 C320 300 380 230 420 330" fill="none" stroke="{RO}" stroke-width="8" stroke-dasharray="14 10" stroke-linecap="round"/>'
           + f'<line x1="420" y1="330" x2="420" y2="230" stroke="{DK}" stroke-width="8"/><path d="M420 232 l56 20 l-56 22 Z" fill="{RO}" {O6}/>'
           + f'<g transform="translate(150 110)"><circle r="70" fill="{GO}" {O}/><circle r="52" fill="{CR}" {O6}/><path d="M0 -44 L12 0 L0 44 L-12 0 Z" fill="{RO}" stroke="{DK}" stroke-width="4"/><path d="M0 0 L12 0 L0 44 L-12 0 Z" fill="{DK}"/><circle r="6" fill="{GO}"/></g>')

TEMI = {
    55: ('La prima app', 'in 5 minuti'), 56: ('Prima e dopo', "chiedere un'app"), 57: ('Una mappa', 'del tuo viaggio'),
    58: ('Un sito', 'per il negozio'), 59: ('Cambiarlo', 'a parole'), 60: ('Pubblicarlo', 'con un link'),
    61: ('Un videogioco', 'in una sera'), 62: ('Prima e dopo', 'chiedere un gioco'), 63: ('La caccia', 'al tesoro'),
    64: ('Un video', 'dalle tue foto'), 65: ('Un video', 'che spiega'), 66: ('Logo', 'e colori'),
    67: ('Una dashboard', 'dei tuoi numeri'), 68: ('Prima e dopo', 'chiedere un grafico'), 69: ('Un calcolatore', 'su misura'),
    70: ("Un'app", 'che ricorda'), 71: ("L'app", 'sul telefono'), 72: ('I turni', 'di casa'),
    73: ('Un libretto', 'in PDF'), 74: ('Prima e dopo', 'chiedere un PDF'), 75: ('Le slide', 'animate'),
    76: ('Il menù', 'da stampare'), 77: ('Il catalogo', 'della collezione'), 78: ('200 file', 'in ordine'),
    79: ('Un sito', 'in un pomeriggio'), 80: ('Prima e dopo', 'il brief perfetto'), 81: ('Il tuo', 'atlante'),
}
