NUM = 76
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Il menù è scritto a mano?', 'Facciamolo bello.'), ('body', 'Un menù da stampare, in ordine e leggibile.')], voce='Il menù del locale è ancora un foglio scritto a mano? Facciamolo bello e da stampare.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi il menù della Trattoria da Nino, foglio A4: primi, secondi e dolci con i prezzi, stile osteria di una volta.')], voce='Dai i piatti con i prezzi, il formato e lo stile del locale.'),
 dict(panel=[('shot', '76_menu', 'doc', {'label': 'Il risultato vero'})], voce='Ecco il menù. Le sezioni separate, i prezzi allineati, e in fondo la nota sulle allergie.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Fai anche la versione in inglese'), ('ed', 'Eccola, stessa grafica. Ho tenuto i nomi dei piatti in italiano.')])], voce='In un attimo anche la versione per i turisti, con la stessa grafica.'),
 dict(panel=[('label', 'Con lo stesso stile'), ('rows', [('Il volantino della serata', ''), ('Il cartello degli orari', ''), ('Il buono regalo', '')])], voce='Con lo stesso stile fai il volantino, il cartello degli orari, il buono regalo.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Prezzi e allergeni li controlli tu, riga per riga: sono informazioni che contano.'), ('stamp', 'Rileggi i prezzi')], voce='Prezzi e allergeni li controlli tu, riga per riga. Sono informazioni che contano.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
