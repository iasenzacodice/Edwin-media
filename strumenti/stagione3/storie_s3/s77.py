NUM = 77
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Collezione nel cassetto?', 'Fanne un catalogo.'), ('body', 'Foto, schede e filtri: ritrovi tutto in un secondo.')], voce='Hai una collezione nel cassetto? Francobolli, monete, vinili. Facciamone un catalogo.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Ti mando le foto e l’elenco dei francobolli del nonno. Fammi un catalogo con una scheda per ognuno, la ricerca e i filtri per paese e anno.')], voce='Dai a Claude le foto e un elenco, anche fatto a mano. Spiega come vuoi cercare.'),
 dict(panel=[('shot', '77_cat', 'web', {'label': 'Il risultato vero'})], voce='Ecco il catalogo. Una scheda per ogni pezzo, la ricerca in alto e i filtri.'),
 dict(panel=[('label', 'I filtri'), ('rows', [('Italia', '10 pezzi'), ("Anni '60", ''), ('Animali', ''), ('Da valutare', '')])], voce='Tocchi un filtro e restano solo i pezzi che cerchi. Su duecento, in un attimo.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Quanto valgono?'), ('ed', 'Non posso darti un valore sicuro: ti preparo la lista per un perito.')])], voce='E se chiedi quanto valgono? Una stima seria la fa un esperto. Claude ti prepara la lista da portargli.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Tieni una copia del catalogo e delle foto: è il ricordo di una vita.'), ('stamp', 'Al sicuro')], voce='Tieni sempre una copia, delle foto e del catalogo. È il ricordo di una vita.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
