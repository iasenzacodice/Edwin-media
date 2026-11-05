NUM = 55
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', "Un'app tutta tua?", 'Bastano 5 minuti.'), ('body', 'Niente codice, niente store. Solo una richiesta scritta bene.')],
      voce="Benvenuto nella stagione tre. Da oggi costruiamo cose vere. Prima tappa, un'app tutta tua in cinque minuti.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', "Fammi un'app per spuntare ogni giorno 4 abitudini: acqua, camminata, lettura e a letto presto. Grande e semplice, da usare sul telefono.")],
      voce="Scrivi cosa vuoi come lo diresti a un amico. Per chi è, cosa deve fare e come deve apparire."),
 dict(panel=[('shot', '55_vuota', 'tel', {'label': 'Il risultato vero'})],
      voce="E in pochi secondi l'app è lì, pronta da usare. Questa l'abbiamo fatta davvero, non è un disegno."),
 dict(panel=[('shot', [(0.0, '55_vuota'), (1.6, '55_piena')], 'tel', {'taps': [(0.6, 0.18, 0.31), (1.0, 0.18, 0.41), (1.4, 0.18, 0.61)]})],
      voce="Tocchi le abitudini fatte e si spuntano. Il cerchio si riempie e i giorni di fila crescono."),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi «meditare 5 minuti» e fai i colori più caldi'), ('ed', 'Fatto. Ora le abitudini sono cinque, e il verde è diventato arancio.')])],
      voce="Vuoi cambiare qualcosa? Lo chiedi a parole. Un'abitudine in più, un colore diverso, un pulsante più grande."),
 dict(panel=[('label', 'Da sapere'), ('body', "Si apre con un link, senza passare dallo store. Più dettagli dai, più l'app ti somiglia."), ('stamp', 'Provala oggi')],
      voce="Si apre con un link, senza passare dallo store. E più dettagli dai, più l'app ti somiglia.", zoom=True),
 dict(panel=[('cta',)], voce="Seguimi, nel prossimo congegno impariamo a chiederla ancora meglio.", posa='saluta'),
]
