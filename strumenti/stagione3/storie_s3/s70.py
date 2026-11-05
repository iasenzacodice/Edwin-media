NUM = 70
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Chiudi l’app', 'e ritrovi tutto?'), ('body', 'Un’app che si ricorda i tuoi dati tra una volta e l’altra.')], voce="Un'app che si ricorda quello che hai scritto anche domani. Ti mostro come chiederla.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi la lista della spesa di casa, divisa per reparto. Deve ricordarsi le cose anche quando la chiudo.')], voce='La frase chiave è deve ricordarsi le cose anche quando la chiudo.'),
 dict(panel=[('shot', '70_spesa', 'tel', {'label': 'Il risultato vero'})], voce='Ecco la lista, divisa per reparti. Spunti quello che hai preso.'),
 dict(panel=[('shot', [(0.0, '70_spesa'), (1.0, '70_spesa2')], 'tel', {'taps': [(0.5, 0.86, 0.2)]})], voce='Aggiungi lo yogurt, chiudi tutto, e domani la lista è ancora lì.'),
 dict(panel=[('chat', 'Chiedilo sempre', [('tu', 'Dove vengono salvati i dati?'), ('ed', 'Te lo spiego, e se vuoi aggiungo un pulsante per scaricarne una copia.')])], voce="Chiedi sempre dove vengono salvati i dati. E in un'app così, niente informazioni delicate."),
 dict(panel=[('label', 'Da sapere'), ('body', 'Per cose importanti tieni anche una copia: chiedi un pulsante per scaricare la lista.'), ('stamp', 'Fai una copia')], voce='E per le cose importanti tieni anche una copia. Chiedi un pulsante per scaricarla.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
