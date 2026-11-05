"""Stagione 2: argomenti e disegni dei congegni (SVG 500x500, centro 250,250)."""
DK = '#2A1E16'
O = f'stroke="{DK}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"'
O6 = f'stroke="{DK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
CR, PA, BR, CU, MU, TE, RO, GO, BW = '#F7F0E0', '#FBF7EC', '#C08A3E', '#B45A30', '#DCA24A', '#2f8a83', '#B3261E', '#E3B657', '#5A341C'


def lines(x, y, w, n, gap=30, col='#8C7350', sw=8, var=(1, .8, .9, .6, .85)):
    return ''.join(f'<line x1="{x}" y1="{y + i * gap}" x2="{x + w * var[i % len(var)]:.0f}" y2="{y + i * gap}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>' for i in range(n))


def sheet(x, y, w, h, fill=PA):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" {O}/>'


def check(x, y, s=1.0, col=TE):
    return f'<path d="M{x - 14 * s} {y} l{10 * s} {11 * s} l{20 * s} {-24 * s}" fill="none" stroke="{col}" stroke-width="{9 * s}" stroke-linecap="round" stroke-linejoin="round"/>'


DEV = {}
DEV[28] = (sheet(110, 70, 250, 330) + f'<rect x="110" y="70" width="250" height="56" rx="10" fill="{TE}" {O}/>' + lines(140, 170, 190, 6, 34)
           + f'<g transform="translate(345 330)"><circle r="92" fill="{MU}" {O}/>'
           + '<circle cx="-34" cy="0" r="17" fill="#fff" stroke="#2A1E16" stroke-width="6"/><circle cx="30" cy="-34" r="17" fill="#fff" stroke="#2A1E16" stroke-width="6"/><circle cx="30" cy="34" r="17" fill="#fff" stroke="#2A1E16" stroke-width="6"/>'
           + '<line x1="-18" y1="-8" x2="15" y2="-27" stroke="#2A1E16" stroke-width="7"/><line x1="-18" y1="8" x2="15" y2="27" stroke="#2A1E16" stroke-width="7"/></g>')
DEV[29] = (f'<line x1="250" y1="360" x2="160" y2="470" {O}/><line x1="250" y1="360" x2="340" y2="470" {O}/><line x1="250" y1="360" x2="250" y2="470" {O}/>'
           + f'<rect x="60" y="70" width="380" height="290" rx="12" fill="{PA}" {O}/><rect x="60" y="70" width="380" height="54" rx="12" fill="{CU}" {O}/>'
           + f'<rect x="110" y="250" width="50" height="70" fill="{TE}" {O6}/><rect x="185" y="200" width="50" height="120" fill="{MU}" {O6}/><rect x="260" y="160" width="50" height="160" fill="{RO}" {O6}/>'
           + f'<path d="M350 300 q30 -60 60 -120" fill="none" stroke="{TE}" stroke-width="10" stroke-linecap="round"/><path d="M392 170 l22 4 l-6 22" fill="none" stroke="{TE}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
           + f'<circle cx="250" cy="52" r="20" fill="{BR}" {O6}/>')
DEV[30] = (sheet(70, 70, 360, 360) + ''.join(f'<line x1="70" y1="{y}" x2="430" y2="{y}" stroke="#C8B89A" stroke-width="5"/>' for y in (140, 210, 280, 350))
           + ''.join(f'<line x1="{x}" y1="70" x2="{x}" y2="430" stroke="#C8B89A" stroke-width="5"/>' for x in (190, 310))
           + f'<rect x="70" y="70" width="360" height="70" rx="10" fill="{TE}" {O}/>'
           + f'<rect x="310" y="350" width="120" height="80" fill="{GO}" {O}/>'
           + '<text x="370" y="403" font-family="Liberation Mono" font-weight="700" font-size="34" text-anchor="middle" fill="#2A1E16">=Σ</text>'
           + ''.join(f'<text x="{x}" y="{y}" font-family="Liberation Mono" font-weight="700" font-size="28" text-anchor="end" fill="#5A341C">{t}</text>' for x, y, t in ((410, 190, '120'), (410, 260, '85'), (410, 330, '40')))
           + f'<g transform="translate(360 120) rotate(30)"><rect x="-14" y="-90" width="28" height="140" fill="{MU}" {O6}/><path d="M-14 50 L0 82 L14 50 Z" fill="{CR}" {O6}/></g>')
DEV[31] = (f'<rect x="70" y="90" width="360" height="340" rx="16" fill="{PA}" {O}/><rect x="70" y="90" width="360" height="80" rx="16" fill="{RO}" {O}/>'
           + ''.join(f'<rect x="{x}" y="60" width="20" height="60" rx="10" fill="{BR}" {O6}/>' for x in (140, 240, 340))
           + ''.join(f'<rect x="{100 + c * 62}" y="{195 + r * 58}" width="48" height="44" rx="6" fill="{f}" stroke="#2A1E16" stroke-width="4"/>'
                     for r in range(4) for c in range(5) for f in [[CR, CR, MU, CR, CR, TE, CR, CR, CR, CU, CR, CR, MU, CR, CR, CR, CR, CR, TE, CR][r * 5 + c]]))
DEV[32] = (f'<g transform="translate(250 270)"><path d="M-150 -150 l-40 -40 M150 -150 l40 -40" {O} fill="none"/>'
           + f'<circle cx="-110" cy="-140" r="52" fill="{GO}" {O}/><circle cx="110" cy="-140" r="52" fill="{GO}" {O}/>'
           + f'<circle r="170" fill="{BR}" {O}/><circle r="136" fill="{PA}" {O6}/>'
           + ''.join(f'<line x1="0" y1="-118" x2="0" y2="-100" stroke="#2A1E16" stroke-width="8" transform="rotate({a})"/>' for a in range(0, 360, 30))
           + f'<line x1="0" y1="0" x2="0" y2="-88" stroke="#2A1E16" stroke-width="12" stroke-linecap="round"/><line x1="0" y1="0" x2="62" y2="24" stroke="{RO}" stroke-width="10" stroke-linecap="round"/><circle r="14" fill="{DK}"/>'
           + f'<path d="M-120 150 l-30 50 M120 150 l30 50" {O} fill="none"/></g>')
DEV[33] = (f'<rect x="90" y="80" width="320" height="380" rx="16" fill="{CU}" {O}/><rect x="120" y="120" width="260" height="310" fill="{PA}" {O6}/>'
           + f'<rect x="180" y="58" width="140" height="50" rx="14" fill="{BR}" {O}/>'
           + ''.join(f'<rect x="145" y="{y}" width="40" height="40" rx="6" fill="#fff" stroke="#2A1E16" stroke-width="6"/><line x1="205" y1="{y + 20}" x2="{w}" y2="{y + 20}" stroke="#8C7350" stroke-width="8" stroke-linecap="round"/>' for y, w in ((150, 350), (220, 330), (290, 345), (360, 320)))
           + check(165, 172) + check(165, 242) + check(165, 312)
           + f'<line x1="410" y1="60" x2="410" y2="200" {O}/><path d="M410 64 l64 22 l-64 22 Z" fill="{RO}" {O6}/>')
DEV[34] = (''.join(f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="6" fill="{c}" {O}/>' for x, y, w, c in ((70, 380, 300, TE), (90, 334, 270, CU), (60, 288, 290, MU), (100, 242, 250, RO)))
           + f'<g transform="translate(320 170)"><circle r="110" fill="#E8F6F4" fill-opacity="0.85" stroke="{BR}" stroke-width="26"/><circle r="110" fill="none" {O}/>'
           + f'<path d="M-50 -40 a70 70 0 0 1 60 -30" stroke="#fff" stroke-width="12" fill="none" stroke-linecap="round"/>'
           + f'<line x1="78" y1="78" x2="150" y2="150" stroke="{BW}" stroke-width="36" stroke-linecap="round"/></g>')
DEV[35] = (sheet(90, 50, 300, 400) + f'<text x="240" y="110" font-family="Lora" font-weight="700" font-size="34" text-anchor="middle" fill="{DK}">CONTRATTO</text>'
           + lines(125, 160, 230, 7, 34)
           + f'<rect x="120" y="248" width="215" height="26" fill="{GO}" opacity="0.75"/>'
           + f'<g transform="translate(330 380)"><circle r="62" fill="{RO}" {O6}/><circle r="44" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="8 6"/><path d="M-30 50 l-20 60 l28 -14 l14 26 l14 -60" fill="{RO}" {O6}/></g>'
           + f'<g transform="translate(400 170) rotate(35)"><rect x="-22" y="-120" width="44" height="170" rx="8" fill="{GO}" {O}/><rect x="-22" y="50" width="44" height="40" fill="{DK}"/><path d="M-22 90 L-10 120 L10 120 L22 90 Z" fill="#F4D35E" {O6}/></g>')
DEV[36] = (f'<rect x="50" y="170" width="300" height="200" rx="18" fill="{BR}" {O}/>'
           + ''.join(f'<g transform="translate({x} 250)"><circle r="56" fill="{DK}"/><circle r="40" fill="{CU}"/><circle r="12" fill="{CR}"/>'
                     + ''.join(f'<circle cx="{24 * __import__("math").cos(a * 2.094):.1f}" cy="{24 * __import__("math").sin(a * 2.094):.1f}" r="7" fill="{DK}"/>' for a in range(3)) + '</g>' for x in (130, 270))
           + f'<rect x="90" y="320" width="220" height="30" rx="6" fill="{DK}"/>'
           + f'<path d="M350 230 L400 230 L400 120 L460 120" fill="none" stroke="{DK}" stroke-width="8" stroke-dasharray="14 10"/>'
           + sheet(330, 40, 140, 170) + lines(350, 80, 100, 4, 30, sw=7))
DEV[37] = (f'<rect x="70" y="200" width="360" height="230" rx="14" fill="{CU}" {O}/>'
           + ''.join(f'<rect x="{x}" y="{y}" width="200" height="140" rx="8" fill="{c}" {O6} transform="rotate({r} {x + 100} {y + 140})"/>' for x, y, c, r in ((110, 110, CR, -8), (150, 90, PA, 2), (190, 100, '#FFF6DA', 9)))
           + lines(220, 140, 130, 3, 28, sw=7)
           + f'<rect x="200" y="290" width="100" height="40" rx="10" fill="{BR}" {O6}/>'
           + f'<circle cx="250" cy="250" r="10" fill="{DK}"/>')
DEV[38] = (f'<rect x="90" y="60" width="300" height="390" rx="14" fill="{TE}" {O}/><rect x="120" y="60" width="270" height="390" rx="10" fill="{PA}" {O}/>'
           + ''.join(f'<circle cx="160" cy="{y}" r="22" fill="{MU}" {O6}/><text x="160" y="{y + 10}" font-family="Lora" font-weight="700" font-size="28" text-anchor="middle" fill="{DK}">{i + 1}</text><line x1="200" y1="{y}" x2="350" y2="{y}" stroke="#8C7350" stroke-width="8" stroke-linecap="round"/>' for i, y in enumerate((140, 230, 320)))
           + f'<g transform="translate(380 400)"><circle r="70" fill="{BR}" {O}/>'
           + ''.join(f'<rect x="-14" y="-92" width="28" height="30" fill="{BR}" {O6} transform="rotate({a})"/>' for a in range(0, 360, 45))
           + f'<circle r="70" fill="{BR}"/><circle r="26" fill="{CR}" {O6}/></g>')
DEV[39] = (sheet(70, 90, 340, 320) + lines(105, 150, 270, 4, 36)
           + f'<path d="M110 330 c30 -50 50 30 80 -10 s40 -40 60 10 s30 20 60 -20" fill="none" stroke="{TE}" stroke-width="9" stroke-linecap="round"/>'
           + f'<g transform="translate(360 250) rotate(40)"><rect x="-26" y="-190" width="52" height="170" rx="20" fill="{DK}"/><rect x="-26" y="-60" width="52" height="24" fill="{GO}"/>'
           + f'<path d="M-26 -20 L-26 30 L0 90 L26 30 L26 -20 Z" fill="{GO}" {O6}/><line x1="0" y1="20" x2="0" y2="80" stroke="{DK}" stroke-width="5"/></g>')
DEV[40] = (f'<path d="M110 260 a80 80 0 0 1 60 -120 a100 100 0 0 1 180 20 a70 70 0 0 1 40 100 Z" fill="#E8F6F4" {O}/>'
           + f'<rect x="150" y="190" width="90" height="64" rx="6" fill="{MU}" {O6}/><rect x="260" y="200" width="90" height="54" rx="6" fill="{CU}" {O6}/>'
           + f'<path d="M250 260 L250 340 Q250 380 210 380 L120 380" fill="none" stroke="{CU}" stroke-width="18" stroke-linecap="round"/>'
           + f'<rect x="60" y="350" width="70" height="60" rx="10" fill="{BR}" {O}/><line x1="40" y1="366" x2="60" y2="366" {O}/><line x1="40" y1="394" x2="60" y2="394" {O}/>')
DEV[41] = (f'<rect x="60" y="230" width="380" height="210" rx="16" fill="{BW}" {O}/>'
           + ''.join(f'<path d="M{x} {y} l0 -170 l60 0 l14 -20 l70 0 l0 190 Z" fill="{c}" {O6}/><rect x="{x + 20}" y="{y - 120}" width="90" height="34" rx="4" fill="{CR}" stroke="#2A1E16" stroke-width="4"/>' for x, y, c in ((90, 330, TE), (200, 320, MU), (310, 330, CU)))
           + f'<rect x="60" y="300" width="380" height="140" rx="16" fill="{BW}" {O}/><rect x="200" y="340" width="100" height="30" rx="10" fill="{BR}" {O6}/>')
DEV[42] = (f'<rect x="40" y="70" width="420" height="340" rx="16" fill="{PA}" {O}/><rect x="40" y="70" width="420" height="56" rx="16" fill="{DK}"/>'
           + ''.join(f'<circle cx="{x}" cy="98" r="10" fill="{c}"/>' for x, c in ((74, RO), (104, MU), (134, TE)))
           + ''.join(f'<rect x="80" y="{y}" width="{w}" height="46" rx="8" fill="#fff" stroke="#2A1E16" stroke-width="6"/>' for y, w in ((160, 340), (230, 340), (300, 200)))
           + lines(96, 183, 160, 2, 70, col='#5A341C', sw=8)
           + f'<rect x="300" y="300" width="120" height="46" rx="10" fill="{TE}" {O6}/>'
           + f'<path d="M370 340 l0 90 l24 -22 l18 40 l18 -8 l-18 -40 l32 -2 Z" fill="#fff" {O6}/>')
DEV[43] = (f'<rect x="80" y="40" width="340" height="430" rx="14" fill="{PA}" {O}/><rect x="80" y="40" width="340" height="70" rx="14" fill="{MU}" {O}/>'
           + f'<g transform="translate(180 200)"><circle r="62" fill="{TE}" {O6}/><path d="M0 0 L0 -62 A62 62 0 0 1 59 19 Z" fill="{CU}" {O6}/><path d="M0 0 L59 19 A62 62 0 0 1 -20 59 Z" fill="{GO}" {O6}/></g>'
           + ''.join(f'<rect x="{x}" y="{390 - h}" width="34" height="{h}" fill="{c}" {O6}/>' for x, h, c in ((280, 60, TE), (325, 110, CU), (370, 160, RO)))
           + f'<path d="M120 430 L180 380 L240 410 L300 340" fill="none" stroke="{TE}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
           + ''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="{CU}" {O6}/>' for x, y in ((120, 430), (180, 380), (240, 410), (300, 340))))
DEV[44] = (f'<rect x="70" y="200" width="360" height="240" rx="12" fill="{CU}" {O}/>'
           + f'<rect x="110" y="70" width="280" height="260" rx="10" fill="{PA}" {O}/>'
           + f'<text x="250" y="160" font-family="Lora" font-weight="700" font-size="44" text-anchor="middle" fill="{RO}">FESTA</text>' + lines(150, 210, 200, 3, 34)
           + f'<path d="M70 200 L250 330 L430 200" fill="{CU}" {O}/><path d="M70 440 L210 330 M430 440 L290 330" {O} fill="none"/>'
           + f'<g transform="translate(250 330)"><path d="M0 0 l-50 -30 l0 60 Z M0 0 l50 -30 l0 60 Z" fill="{GO}" {O6}/><circle r="16" fill="{RO}" {O6}/></g>')
DEV[45] = (f'<rect x="40" y="70" width="420" height="360" rx="16" fill="{PA}" {O}/><rect x="40" y="70" width="420" height="56" rx="16" fill="{TE}" {O}/>'
           + ''.join(f'<circle cx="{x}" cy="98" r="10" fill="#fff"/>' for x in (74, 104, 134))
           + f'<rect x="70" y="150" width="360" height="150" fill="#BFDCDD" {O6}/><path d="M70 300 L170 200 L230 250 L300 180 L430 300 Z" fill="{TE}" {O6}/><circle cx="380" cy="190" r="22" fill="{GO}"/>'
           + lines(80, 330, 200, 2, 30) + f'<rect x="300" y="350" width="130" height="50" rx="25" fill="{RO}" {O6}/>')
DEV[46] = (''.join(f'<rect x="{x}" y="{y}" width="260" height="180" rx="16" fill="{c}" {O} transform="rotate({r} {x + 130} {y + 90})"/>' for x, y, c, r in ((80, 260, TE, -10), (120, 200, MU, 6), (150, 120, PA, -4)))
           + f'<text x="280" y="250" font-family="Lora" font-weight="700" font-size="110" text-anchor="middle" fill="{CU}" transform="rotate(-4 280 210)">?</text>')
DEV[47] = (f'<rect x="80" y="70" width="320" height="380" rx="12" fill="{PA}" {O}/>' + ''.join(f'<line x1="80" y1="{y}" x2="400" y2="{y}" stroke="#BFDCDD" stroke-width="4"/>' for y in range(130, 450, 40))
           + f'<line x1="130" y1="70" x2="130" y2="450" stroke="{RO}" stroke-width="4"/>'
           + f'<text x="148" y="200" font-family="Liberation Mono" font-weight="700" font-size="44" fill="{DK}">3 + ? = 7</text>'
           + f'<circle cx="250" cy="330" r="46" fill="#FFF6C8" {O6}/><path d="M238 336 l8 -18 l8 18 l8 -18" fill="none" stroke="{CU}" stroke-width="5"/><rect x="232" y="372" width="36" height="22" fill="#8C7350" {O6}/>'
           + f'<g transform="translate(400 380) rotate(30)"><rect x="-18" y="-140" width="36" height="200" fill="{MU}" {O6}/><path d="M-18 60 L0 100 L18 60 Z" fill="{CR}" {O6}/><rect x="-18" y="-140" width="36" height="30" fill="{CU}" {O6}/></g>')
DEV[48] = (f'<rect x="40" y="60" width="420" height="380" rx="14" fill="#EFE3C8" {O}/>'
           + f'<path d="M90 400 C190 400 120 280 230 280 S330 160 410 120" fill="none" stroke="{CU}" stroke-width="12" stroke-dasharray="20 14" stroke-linecap="round"/>'
           + ''.join(f'<g transform="translate({x} {y})"><line x1="0" y1="0" x2="0" y2="-70" {O}/><path d="M0 -70 l50 16 l-50 16 Z" fill="{c}" {O6}/><circle r="16" fill="{BR}" {O6}/>'
                     f'<text x="0" y="40" font-family="Lora" font-weight="700" font-size="34" text-anchor="middle" fill="{DK}">{t}</text></g>' for x, y, c, t in ((100, 380, TE, '1'), (240, 270, MU, '2'), (400, 130, RO, '3'))))
DEV[49] = (''.join(f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" fill="#CFA36B" {O}/><rect x="{w / 2 - 16}" width="32" height="{h}" fill="#E3C79A"/><rect width="{w}" height="{h}" fill="none" {O}/></g>' for x, y, w, h in ((60, 280, 220, 170), (240, 300, 200, 150), (130, 120, 220, 160)))
           + f'<rect x="150" y="190" width="120" height="44" fill="{PA}" {O6}/><text x="210" y="222" font-family="Liberation Mono" font-weight="700" font-size="26" text-anchor="middle" fill="{DK}">CUCINA</text>'
           + f'<path d="M300 380 l40 0 m-16 -16 l16 16 l-16 16" fill="none" stroke="{RO}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>')
DEV[50] = (f'<path d="M250 200 Q160 160 60 190 L60 440 Q160 410 250 450 Z" fill="{PA}" {O}/><path d="M250 200 Q340 160 440 190 L440 440 Q340 410 250 450 Z" fill="{PA}" {O}/>'
           + lines(90, 240, 120, 5, 34) + lines(280, 240, 120, 5, 34)
           + f'<path d="M330 60 a70 70 0 1 0 60 110 a56 56 0 1 1 -60 -110 Z" fill="{GO}" {O6}/>'
           + ''.join(f'<path d="M{x} {y} l8 18 l20 2 l-15 13 l5 20 l-18 -11 l-18 11 l5 -20 l-15 -13 l20 -2 Z" fill="{MU}" {O6}/>' for x, y in ((150, 70), (220, 120))))
DEV[51] = (f'<g transform="rotate(-14 180 260)"><path d="M130 90 L230 90 L215 230 Q180 270 145 230 Z" fill="#FFF3C4" {O}/><path d="M138 160 L222 160 L215 230 Q180 270 145 230 Z" fill="{GO}"/><path d="M130 90 L230 90 L215 230 Q180 270 145 230 Z" fill="none" {O}/><line x1="180" y1="262" x2="180" y2="380" {O}/><line x1="130" y1="390" x2="230" y2="390" {O}/></g>'
           + f'<g transform="rotate(14 320 260)"><path d="M270 90 L370 90 L355 230 Q320 270 285 230 Z" fill="#FFF3C4" {O}/><path d="M278 160 L362 160 L355 230 Q320 270 285 230 Z" fill="{GO}"/><path d="M270 90 L370 90 L355 230 Q320 270 285 230 Z" fill="none" {O}/><line x1="320" y1="262" x2="320" y2="380" {O}/><line x1="270" y1="390" x2="370" y2="390" {O}/></g>'
           + ''.join(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MU}" stroke-width="8" stroke-linecap="round"/>' for x1, y1, x2, y2 in ((250, 40, 250, 10), (205, 50, 190, 25), (295, 50, 310, 25))))
DEV[52] = (sheet(70, 60, 320, 390) + lines(105, 120, 250, 8, 36)
           + f'<ellipse cx="230" cy="228" rx="110" ry="32" fill="none" stroke="{RO}" stroke-width="8"/>'
           + f'<g transform="translate(360 350)"><path d="M0 -100 L90 -70 L80 20 Q60 80 0 110 Q-60 80 -80 20 L-90 -70 Z" fill="{TE}" {O}/>{check(0, 10, 2.6, "#fff")}</g>')
DEV[53] = (f'<rect x="50" y="160" width="400" height="290" rx="14" fill="{PA}" {O}/>'
           + ''.join(f'<rect x="{80 + i * 56}" y="{190 + (i % 2) * 0}" width="50" height="50" fill="{[TE, MU, CU, RO, GO, TE][i]}" stroke="#2A1E16" stroke-width="5"/>' for i in range(6))
           + ''.join(f'<rect x="{80 + 5 * 56}" y="{246 + i * 56}" width="50" height="50" fill="{[CU, GO, TE][i]}" stroke="#2A1E16" stroke-width="5"/>' for i in range(3))
           + f'<g transform="translate(150 340) rotate(-12)"><rect x="-60" y="-60" width="120" height="120" rx="20" fill="#fff" {O}/>'
           + ''.join(f'<circle cx="{x}" cy="{y}" r="12" fill="{DK}"/>' for x, y in ((-30, -30), (0, 0), (30, 30))) + '</g>'
           + f'<g transform="translate(330 120)"><circle cy="-50" r="30" fill="{RO}" {O6}/><path d="M-36 40 Q-30 -20 0 -24 Q30 -20 36 40 Z" fill="{RO}" {O6}/></g>')
DEV[54] = (f'<rect x="60" y="210" width="380" height="230" rx="16" fill="{RO}" {O}/><path d="M170 210 L170 150 Q170 120 200 120 L300 120 Q330 120 330 150 L330 210" fill="none" {O}/>'
           + f'<rect x="60" y="270" width="380" height="30" fill="{DK}"/><rect x="220" y="260" width="60" height="50" rx="8" fill="{BR}" {O6}/>'
           + f'<g transform="translate(120 180) rotate(-30)"><rect x="-12" y="-110" width="24" height="120" fill="#9AA4AA" {O6}/><path d="M-30 -130 a30 30 0 1 0 60 0 l-14 0 l0 22 l-32 0 l0 -22 Z" fill="#9AA4AA" {O6}/></g>'
           + f'<g transform="translate(380 160)"><circle r="56" fill="{BR}" {O}/>'
           + ''.join(f'<rect x="-11" y="-74" width="22" height="24" fill="{BR}" {O6} transform="rotate({a})"/>' for a in range(0, 360, 45)) + f'<circle r="56" fill="{BR}"/><circle r="20" fill="{CR}" {O6}/></g>')

TEMI = {
    28: ('Un documento', 'da condividere'), 29: ('Una presentazione', 'in 5 minuti'), 30: ('Un foglio', 'che fa i conti'),
    31: ("L'agenda", 'della settimana'), 32: ('I promemoria', 'automatici'), 33: ('Un progetto', 'in tanti passi'),
    34: ('La ricerca', 'approfondita'), 35: ('Leggere', 'un contratto'), 36: ('Dalla riunione', 'al verbale'),
    37: ('La memoria', 'di Claude'), 38: ('Le skill', 'su misura'), 39: ('Scrivere', 'come te'),
    40: ('I tuoi file', 'collegati'), 41: ('Riordinare', 'le cartelle'), 42: ('Compilare', 'un modulo online'),
    43: ("Un'infografica", 'in un attimo'), 44: ('Un invito', 'per la festa'), 45: ('Un sito', 'per un evento'),
    46: ('Studiare', 'con le flashcard'), 47: ('Il tutor', 'dei compiti'), 48: ('Un corso', 'su misura'),
    49: ('Il trasloco', 'organizzato'), 50: ('Una favola', 'della buonanotte'), 51: ('Un discorso', 'da ricordare'),
    52: ('Fatti', 'controllare'), 53: ('Un gioco', 'per la famiglia'), 54: ('Il tuo primo', 'progetto'),
}
