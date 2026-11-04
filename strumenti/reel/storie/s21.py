NUM = 21
TITOLO = ('Cercare', 'con le fonti')
SET = ('colosso', 'testa')
POSA = 'regge'
EDWIN_X = 520
DIETRO = ''
DAVANTI = '<g transform="translate(870 1350)"><circle cx="0" cy="0" r="100" fill="#E8F6F4" stroke="#2A1E16" stroke-width="6"/><ellipse cx="0" cy="0" rx="40" ry="100" fill="none" stroke="#2A1E16" stroke-width="4"/><line x1="-100" y1="0" x2="100" y2="0" stroke="#2A1E16" stroke-width="4"/><path d="M-60 -50 q30 -16 40 14 q-16 26 -44 10 z" fill="#6E9E5A"/><path d="M20 20 q40 -6 46 30 q-30 20 -50 -4 z" fill="#6E9E5A"/><path d="M-120 0 A120 120 0 0 1 120 0" stroke="#C08A3E" stroke-width="10" fill="none"/><rect x="-10" y="100" width="20" height="40" fill="#C08A3E"/><rect x="-60" y="134" width="120" height="16" rx="6" fill="#7A4A26"/></g><g transform="translate(520 1356) scale(1.35)"><circle cx="0" cy="0" r="56" fill="#fff" fill-opacity="0.45" stroke="#9C4A26" stroke-width="14"/><line x1="40" y1="40" x2="100" y2="100" stroke="#9C4A26" stroke-width="22" stroke-linecap="round"/></g>'
SCENE = [
 dict(panel=[('title2', "Ti serve un'informazione", 'aggiornata?'), ('img', '<g transform="translate(390 98) scale(1.45)"><circle cx="-12" cy="-6" r="40" fill="#E8F6F4" stroke="#2A1E16" stroke-width="4"/><ellipse cx="-12" cy="-6" rx="16" ry="40" fill="none" stroke="#2A1E16" stroke-width="3"/><line x1="-52" y1="-6" x2="28" y2="-6" stroke="#2A1E16" stroke-width="3"/><path d="M-30 -30 q10 -6 14 6 q-6 10 -16 4 z" fill="#6E9E5A"/>\n<circle cx="26" cy="20" r="18" fill="#fff" fill-opacity="0.6" stroke="#9C4A26" stroke-width="6"/><line x1="38" y1="33" x2="56" y2="52" stroke="#9C4A26" stroke-width="9" stroke-linecap="round"/></g><text x="540" y="136" font-family="Lora" font-weight="700" font-size="96" fill="#B3261E">?</text>', 190)], voce="Ti serve un'informazione aggiornata? Quello che so può essere vecchio, ma posso cercare per te."),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Cerca sul web gli orari del museo Egizio di Torino per sabato e dammi i link.')], voce='Chiedimi di cercare, chiaramente. La parola magica è cerca.'),
 dict(panel=[('label', 'Risultato', 'esempio inventato'), ('rows', [('Apertura', '9:00'), ('Chiusura', '18:30'), ('Fonte', 'sito ufficiale')])], voce="Ti rispondo e ti dico dove l'ho letto. Meglio se è un sito ufficiale."),
 dict(panel=[('label', 'Chiedimi ancora'), ('body', 'Vuoi esserne sicuro?'), ('buttons', ['Apri il link', 'Confronta tre siti'], 0)], voce='Apri il link e controlla che dica davvero quello che ti ho detto. Oppure chiedimi di confrontare più siti.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Anche il web sbaglia: per le cose importanti telefona o controlla di persona.'), ('stamp', 'Controlla la fonte')], voce='Anche il uèb sbaglia. Per le cose importanti, telefona o controlla di persona.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.'),
]
