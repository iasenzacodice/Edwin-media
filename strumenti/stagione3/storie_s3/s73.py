NUM = 73
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Un libretto da stampare?', 'Impaginato bene.'), ('body', 'Copertina, foto, date: un PDF pronto per la stampa.')], voce="Devi preparare un libretto per un'associazione? Facciamolo impaginato bene, pronto da stampare.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi il programma 2027 del circolo bocce Le Querce: copertina, una pagina con le date delle gare e delle cene. In PDF, A4.')], voce='Dici cosa contiene, per chi è e il formato. Qui un PDF in A4.'),
 dict(panel=[('shot', '73_cop', 'doc', {'label': 'Il risultato vero'})], voce='Ecco la copertina, semplice e pulita.'),
 dict(panel=[('shot', '73_int', 'doc')], voce='E dentro le date, una per riga, ognuna con due parole di spiegazione.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Metti il logo del circolo e le foto della festa'), ('ed', 'Allegale e le sistemo io, una per pagina.')])], voce='Poi aggiungi le foto vere e il logo. Claude le impagina al posto giusto.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Stampane una copia di prova prima di farne cento: i colori a schermo ingannano.'), ('stamp', 'Copia di prova')], voce='Prima di stamparne cento, fanne una di prova. I colori sullo schermo ingannano.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
