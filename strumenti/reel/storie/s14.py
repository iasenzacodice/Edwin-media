NUM = 14
TITOLO = ('Spiegamelo', 'semplice')
SET = ('colosso', 'torso')
POSA = 'indica'
EDWIN_X = 620
DIETRO = '<g transform="translate(180 1150)"><rect x="-120" y="-140" width="240" height="190" fill="#2F3B33" stroke="#7A4A26" stroke-width="14"/><text x="0" y="-60" font-family="Lora" font-weight="700" font-size="40" fill="#F3E9D2" text-anchor="middle">SPREAD</text><text x="0" y="0" font-family="Lora" font-size="56" fill="#F3E9D2" text-anchor="middle">= ?</text><line x1="-90" y1="50" x2="-120" y2="330" stroke="#7A4A26" stroke-width="12"/><line x1="90" y1="50" x2="120" y2="330" stroke="#7A4A26" stroke-width="12"/></g>'
DAVANTI = ''
SCENE = [
 dict(panel=[('title2', 'Certe cose sembrano', 'scritte per pochi?'), ('img', '<g transform="translate(390 98) scale(1.45)"><circle cx="0" cy="-14" r="34" fill="#FFF6C8" stroke="#2A1E16" stroke-width="4"/><path d="M-8 -12 Q-14 4 -10 18 M8 -12 Q14 4 10 18" stroke="#9C4A26" stroke-width="4" fill="none"/>\n<rect x="-16" y="18" width="32" height="10" fill="#8C7350"/><rect x="-14" y="30" width="28" height="9" fill="#8C7350"/>\n<line x1="-48" y1="-46" x2="-40" y2="-38" stroke="#DCA24A" stroke-width="4"/><line x1="48" y1="-46" x2="40" y2="-38" stroke="#DCA24A" stroke-width="4"/><line x1="0" y1="-62" x2="0" y2="-54" stroke="#DCA24A" stroke-width="4"/></g><text x="540" y="136" font-family="Lora" font-weight="700" font-size="96" fill="#B3261E">?</text>', 190)], voce='Il mutuo, lo spread, come funziona un vaccino. Certe cose sembrano scritte per pochi? Te le spiego io, senza vergogna.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', "Spiegami cos'è lo spread come se avessi 10 anni.")], voce='Chiedimelo in parole semplici. Il trucco dei dieci anni funziona sempre.'),
 dict(panel=[('label', 'Risposta di Edwin', 'esempio semplificato'), ('body', 'Due amici chiedono un prestito. A quello meno affidabile chiedono più interessi. Lo spread è quella differenza.')], voce='Ecco, niente paroloni. Due amici, un prestito, e la differenza negli interessi.'),
 dict(panel=[('label', 'Chiedimi ancora'), ('body', 'Vuoi capire meglio?'), ('buttons', ['Fammi un esempio con la spesa', "Ora un po' più difficile"], 1)], voce='Poi chiedimi un esempio della vita di tutti i giorni, oppure di salire di un livello, quando sei pronto.'),
 dict(panel=[('label', 'Fatti interrogare'), ('rows', [('Chi paga più interessi?', ''), ('Perché?', ''), ('Cosa succede se lo spread sale?', '')])], voce='E alla fine fatti interrogare con tre domande. Se sbagli, te lo rispiego in un altro modo.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Per salute, soldi e leggi: prima capisci con me, poi decidi con un esperto.'), ('stamp', 'Chiedi a un esperto')], voce='Ricorda, semplice non vuol dire sicuro. Per salute, soldi e leggi, prima capisci con me, poi decidi con un esperto.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
