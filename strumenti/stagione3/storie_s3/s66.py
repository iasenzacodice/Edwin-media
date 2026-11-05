NUM = 66
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'La tua attività', 'ha un volto?'), ('body', 'Logo, colori e caratteri: una piccola identità in un pomeriggio.')], voce='La tua attività ha un volto riconoscibile? Facciamo logo e colori, insieme.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi un logo per il Forno Rossi, dal 1962: tondo, caldo, con una pagnotta. Poi i colori e i caratteri da usare ovunque.')], voce='Racconta chi sei, da quando, e che sensazione vuoi dare.'),
 dict(panel=[('shot', '66_logo', 'web', {'label': 'Il risultato vero'})], voce='Ecco la scheda. Il logo tondo, la versione lunga, i colori con i loro codici e i caratteri.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Fammene tre versioni diverse'), ('ed', 'Eccole: una classica, una moderna e una disegnata a mano.')])], voce='Non ti convince? Chiedi tre strade diverse e scegli quella che ti somiglia.'),
 dict(panel=[('label', 'Dove usarlo'), ('rows', [('Insegna e sacchetti', ''), ('Sito e social', ''), ('Biglietti da visita', ''), ('Menù e volantini', '')])], voce="Poi lo usi dappertutto. L'insegna, i sacchetti, il sito, i biglietti, i volantini."),
 dict(panel=[('label', 'Da sapere'), ('body', 'Prima di stamparlo, controlla che non somigli al marchio di qualcun altro.'), ('stamp', 'Tutto tuo')], voce='Prima di stamparlo, controlla che non somigli al marchio di qualcun altro. Il logo deve essere solo tuo.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
