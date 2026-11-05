NUM = 59
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Il sito è quasi giusto?', 'Correggilo a parole.'), ('body', 'Niente pannelli complicati: dici cosa cambiare.')], voce='Il sito è quasi perfetto, ma vorresti cambiare qualcosa? Non serve toccare niente, basta dirlo.', posa='saluta'),
 dict(panel=[('shot', '58_sito', 'web', {'label': 'Prima'})], voce='Riprendiamo il sito del forno. Mettiamo che il titolo ti sembri piccolo e i colori non ti convincano.'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fai il titolo più grande, passa al verde e aggiungi una sezione per le torte su ordinazione.')], voce='Lo scrivi così, tutto in una richiesta. Titolo più grande, verde, e una sezione nuova per le torte.'),
 dict(panel=[('shot', [(0.0, '58_sito'), (0.9, '59_sito_v2')], 'web', {'label': 'Dopo'})], voce='Ed ecco fatto. Titolo, colori e la sezione nuova, senza toccare una riga di codice.'),
 dict(panel=[('label', 'Si può chiedere'), ('rows', [('Colori e caratteri', ''), ('Sezioni nuove', ''), ('Testi più corti', ''), ('Ordine delle parti', '')])], voce='Puoi chiedere colori e caratteri, sezioni nuove, testi più corti, o di spostare le parti.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Una modifica alla volta è più facile da controllare. Se qualcosa si rompe, chiedi di tornare indietro.'), ('stamp', 'Un passo alla volta')], voce='Il consiglio, una modifica alla volta. E se qualcosa non va, chiedi di tornare alla versione di prima.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
