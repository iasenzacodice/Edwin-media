NUM = 61
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Un videogioco?', 'Sì, in una sera.'), ('body', 'Un gioco vero, da giocare sul telefono. Anche con i bambini.')], voce='Stasera facciamo una cosa divertente. Un videogioco vero, in una sera.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi un gioco per il telefono: un automa salta tra piattaforme e raccoglie monete. Tre livelli, si tocca lo schermo per saltare.')], voce='Descrivi il gioco come una storia. Chi è il protagonista, cosa deve fare, come si comanda.'),
 dict(panel=[('shot', '61_titolo', 'tel', {'label': 'Il risultato vero'})], voce="Ecco la schermata iniziale, con i livelli da scegliere. L'ultimo si sblocca giocando."),
 dict(panel=[('shot', '61_gioco', 'tel', {'taps': [(0.8, 0.6, 0.55), (1.6, 0.7, 0.45)]})], voce="E si gioca davvero. Tocchi lo schermo, l'automa salta e raccoglie le monete."),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'È troppo difficile per mio figlio'), ('ed', 'Ho rallentato i salti e aggiunto una vita in più nel primo livello.')])], voce='Troppo difficile? Troppo facile? Lo dici e il gioco cambia. È il modo più bello per imparare insieme.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'I giochi semplici vengono bene subito. Per quelli grandi: un pezzo alla volta.'), ('stamp', 'Si gioca')], voce='I giochi semplici vengono bene subito. Per quelli più grandi, si costruisce un pezzo alla volta.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
