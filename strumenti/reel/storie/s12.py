NUM = 12
TITOLO = ('Un weekend', 'organizzato')
SET = ('officina', '')
POSA = 'regge'
ICONA = '<rect x="-55" y="-40" width="110" height="80" fill="#fff" stroke="#2A1E16" stroke-width="4"/><line x1="-18" y1="-40" x2="-18" y2="40" stroke="#C8B89A" stroke-width="3"/><line x1="18" y1="-40" x2="18" y2="40" stroke="#C8B89A" stroke-width="3"/>\n<path d="M-42 26 Q-20 -6 0 12 T 38 -22" stroke="#B3261E" stroke-width="4" stroke-dasharray="7 6" fill="none"/><circle cx="-42" cy="26" r="7" fill="#9C4A26"/><path d="M38 -36 C50 -36 50 -20 38 -8 C26 -20 26 -36 38 -36 Z" fill="#B3261E"/>'
# mappa tenuta in mano
DAVANTI = """<g transform="translate(540 1372) rotate(-4)">
<rect x="-78" y="-62" width="156" height="118" fill="#F7F0E0" stroke="#2A1E16" stroke-width="5"/>
<line x1="-26" y1="-62" x2="-26" y2="56" stroke="#C8B89A" stroke-width="3"/><line x1="26" y1="-62" x2="26" y2="56" stroke="#C8B89A" stroke-width="3"/>
<path d="M-60 34 Q-30 -10 0 14 T 56 -34" stroke="#B3261E" stroke-width="5" stroke-dasharray="9 7" fill="none"/>
<circle cx="-60" cy="34" r="8" fill="#9C4A26"/><path d="M56 -50 C70 -50 70 -32 56 -18 C42 -32 42 -50 56 -50 Z" fill="#B3261E"/></g>
<g transform="translate(150 1400)"><rect x="-80" y="-60" width="160" height="130" rx="14" fill="#9C4A26" stroke="#2A1E16" stroke-width="5"/>
<rect x="-30" y="-86" width="60" height="30" rx="10" fill="none" stroke="#2A1E16" stroke-width="9"/>
<rect x="-80" y="-12" width="160" height="12" fill="#C08A3E"/><rect x="-46" y="-20" width="18" height="28" fill="#E3B657"/><rect x="28" y="-20" width="18" height="28" fill="#E3B657"/>
<rect x="-70" y="30" width="80" height="26" rx="4" fill="#F7F0E0" stroke="#2A1E16" stroke-width="3"/><text x="-30" y="49" font-family="Liberation Mono" font-weight="700" font-size="16" text-anchor="middle" fill="#2A1E16">FIRENZE</text></g>"""
HOOK = f"""<g transform="translate(390 98) scale(1.45)">{ICONA}</g>
<text x="560" y="150" font-family="Lora" font-weight="700" font-size="110" fill="#B3261E">?</text>
<g transform="translate(700 104) scale(1.1)"><rect x="-40" y="-30" width="80" height="64" rx="10" fill="#9C4A26" stroke="#2A1E16" stroke-width="4"/><rect x="-16" y="-46" width="32" height="18" rx="6" fill="none" stroke="#2A1E16" stroke-width="6"/></g>"""
SCENE = [
 dict(panel=[('title2', 'Un weekend fuori?', 'Ci penso io.'), ('img', HOOK, 190)],
      voce="Un weekend fuori e non sai da dove cominciare? Tu fai la valigia, al programma penso io."),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Weekend a Firenze in treno, sabato e domenica. Siamo in tre, con un bambino di 6 anni. Ci piacciono giardini e cucina tipica.')],
      voce="Scrivimi dove vai, quando, chi viaggia con te e cosa vi piace. Più dettagli mi dai, più il programma è su misura."),
 dict(panel=[('label', 'Sabato', 'esempio inventato'), ('rows', [('Arrivo in stazione', '9:30'), ('Giardino di Boboli', '10:30'), ('Pranzo in trattoria', '13:00'), ('Pausa al parco', '15:30'), ('Cena tipica', '19:30')])],
      voce="Ecco il programma ora per ora, con gli spostamenti a piedi e le pause giuste per il bambino. Domenica te la preparo uguale."),
 dict(panel=[('label', 'Chiedimi ancora'), ('body', 'Vuoi cambiarlo?'), ('buttons', ['E se piove?', 'Spendiamo meno'], 0)],
      voce="Vuoi cambiare qualcosa? Chiedimi la versione per la pioggia, oppure una più economica."),
 dict(panel=[('label', 'Prima di partire'), ('body', 'Orari e prezzi cambiano: controllali sempre sui siti ufficiali di musei e ristoranti.'), ('stamp', 'Siti ufficiali')],
      voce="Prima di partire, controlla orari e prezzi sui siti ufficiali. Musei e ristoranti a volte cambiano."),
 dict(panel=[('cta',)], voce="Seguimi per il prossimo congegno, arriva presto."),
]
