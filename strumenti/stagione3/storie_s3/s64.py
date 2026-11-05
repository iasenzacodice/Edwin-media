NUM = 64
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Cento foto delle vacanze?', 'Diventano un video.'), ('body', 'Titoli, ordine, passaggi morbidi. La musica la scegli tu.')], voce='Hai cento foto delle vacanze nel telefono? Facciamole diventare un video da rivedere.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Ti mando le foto dell’estate. Fammi un video di 3 minuti, in ordine di data, con un titolo per ogni posto.')], voce='Dai a Claude le foto e spiegagli come lo vuoi. Durata, ordine, titoli.'),
 dict(panel=[('shot', '64_titolo', 'vid', {'label': 'Il risultato vero'})], voce="Ecco l'apertura. Il titolo sulla prima foto, poi le foto scorrono una dopo l'altra."),
 dict(panel=[('shot', [(0.0, '64_monti'), (1.6, '64_fine')], 'vid')], voce='Ogni posto ha il suo titolo, e alla fine una chiusura. Il risultato è un file video da scaricare.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Più lento, e togli le foto mosse'), ('ed', 'Fatto. Ogni foto resta quattro secondi e ne ho tolte sei sfocate.')])], voce='Poi lo sistemi a parole. Più lento, meno foto, un titolo diverso.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'La musica mettila tu: quella famosa ha i diritti. Chiedi il permesso a chi compare nelle foto.'), ('stamp', 'Ricordi in ordine')], voce='Due regole. La musica famosa ha i diritti, quindi scegli tu cosa usare. E chiedi sempre il permesso a chi compare nelle foto.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
