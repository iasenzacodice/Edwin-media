NUM = 63
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Una festa di compleanno?', 'Caccia al tesoro digitale.'), ('body', 'Indizi sul telefono, codici nascosti in casa, premio finale.')], voce="C'è una festa in arrivo? Organizziamo una caccia al tesoro, con gli indizi sul telefono.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi una caccia al tesoro per il compleanno di Sofia, 8 anni: 5 indovinelli sulla casa, ognuno sblocca il successivo con un codice.')], voce="Dai a Claude l'età, il posto e quanti indizi vuoi. Lui scrive gli indovinelli e costruisce il gioco."),
 dict(panel=[('shot', '63_indizio', 'tel', {'label': 'Il risultato vero', 'taps': [(1.4, 0.5, 0.62)]})], voce='Ogni indizio è un indovinello. I bambini trovano il codice nascosto e lo scrivono.'),
 dict(panel=[('shot', [(0.0, '63_indizio'), (0.6, '63_ok')], 'tel')], voce="Codice giusto, e si sblocca l'indizio dopo. Fino al tesoro."),
 dict(panel=[('label', 'Prima della festa'), ('rows', [('Nascondi i codici', ''), ('Prova tutto il giro', ''), ('Tieni un aiutino pronto', '')])], voce='Prima della festa nascondi i codici, prova tu tutto il giro e tieni pronto un aiutino.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Con i bambini piccoli stai vicino: il telefono è un mezzo, la festa siete voi.'), ('stamp', 'Buona caccia')], voce='Con i più piccoli stai vicino. Il telefono è solo un mezzo, la festa siete voi.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
