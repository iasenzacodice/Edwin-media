NUM = 57
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Un viaggio in vista?', 'Fallo diventare una mappa.'), ('body', 'Tappe, giorni e consigli, tutto in una pagina da toccare.')], voce='Hai un viaggio in programma? Invece di una lista, fatti fare una mappa da toccare.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Faccio la Puglia in 5 giorni a giugno, in auto. Fammi una mappa con le tappe, un giorno per tappa e un consiglio per ognuna.')], voce='Racconta il viaggio: quanti giorni, come ti sposti, cosa ti piace.'),
 dict(panel=[('shot', '57_mappa', 'web', {'label': 'Il risultato vero'})], voce='Ecco la mappa. A sinistra i giorni, sulla cartina le tappe collegate dal percorso.'),
 dict(panel=[('shot', [(0.0, '57_mappa'), (1.2, '57_mappa_lecce')], 'web', {'taps': [(0.6, 0.35, 0.43)]})], voce='Tocchi una tappa e si apre la scheda, con il consiglio del giorno.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi dove mangiare la sera e i chilometri tra una tappa e l’altra'), ('ed', 'Fatto. Ho aggiunto i chilometri sul percorso e una cena per ogni tappa.')])], voce='Poi la arricchisci a parole. I ristoranti, i chilometri, le spiagge da non perdere.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Orari, prezzi e strade cambiano: controlla sempre le informazioni prima di partire.'), ('stamp', 'Controlla prima')], voce='Una cosa importante. Orari e prezzi cambiano, quindi prima di partire controlla le informazioni sui siti ufficiali.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
