NUM = 71
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'La tua app', 'sul telefono.'), ('body', 'Un’icona come le altre, accanto alle tue app.')], voce="Hai creato un'app e vuoi averla sul telefono come le altre? Si fa in tre tocchi.", posa='saluta'),
 dict(panel=[('label', 'I passi'), ('rows', [('Pubblica l’app e apri il link', ''), ('Tocca il tasto Condividi', ''), ('Aggiungi alla schermata Home', '')])], voce="Pubblica l'app e apri il link sul telefono. Poi condividi, e aggiungi alla schermata Home."),
 dict(panel=[('shot', [(0.0, '70_spesa'), (1.4, '71_home')], 'tel', {'label': 'Sul telefono'})], voce='Ed ecco la nuova icona, accanto alle altre.'),
 dict(panel=[('shot', [(0.0, '71_home'), (1.4, '70_spesa')], 'tel', {'taps': [(0.6, 0.5, 0.33)]})], voce='La tocchi e si apre subito, senza cercare il link ogni volta.'),
 dict(panel=[('label', 'Fallo per'), ('rows', [('La lista della spesa', ''), ('Il calcolatore del viaggio', ''), ('Le abitudini del mattino', '')])], voce='Fallo per gli strumenti che usi tutti i giorni. La spesa, il calcolatore, le abitudini.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'È un collegamento al link: serve internet per aprirla, e non passa dallo store.'), ('stamp', 'Tre tocchi')], voce='Una cosa da sapere. È un collegamento al link, quindi di solito serve internet per aprirla.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
