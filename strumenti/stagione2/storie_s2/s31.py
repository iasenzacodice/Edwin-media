NUM = 31
POSA = 'regge'
EDWIN_X = 540
SCENE = [
 dict(panel=[('title2', 'La settimana', 'ti scappa di mano?'), ('body', 'Se colleghi il tuo calendario, la guardo insieme a te.')], voce='La settimana ti scappa di mano? Se colleghi il tuo calendario, la guardiamo insieme.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Cosa ho in agenda questa settimana? Trovami due ore libere per la palestra.')], voce='Me lo chiedi a parole, come a una segretaria molto paziente.', posa='banco'),
 dict(panel=[('label', 'La tua settimana', 'esempio inventato'), ('rows', [('Lunedì', 'dentista 17:00'), ('Mercoledì', 'riunione 9:30'), ('Giovedì', 'libero dopo le 18'), ('Sabato', 'libero la mattina')])], voce='Leggo i tuoi impegni e trovo i buchi liberi. Giovedì sera e sabato mattina, per esempio.', x=470),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Mettimi la palestra giovedì alle 18'), ('ed', 'Te la preparo. Confermi tu?')])], voce="Posso anche proporti l'appuntamento, ma la conferma la dai tu. Il calendario resta tuo."),
 dict(panel=[('label', 'Da sapere'), ('body', 'Il calendario si collega solo se lo decidi tu, e puoi scollegarlo quando vuoi.'), ('stamp', 'Decidi tu')], voce='Il collegamento lo attivi solo tu e lo togli quando vuoi. Io la palestra te la segno, andarci tocca a te.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
