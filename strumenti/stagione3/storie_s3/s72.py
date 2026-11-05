NUM = 72
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Chi lava i piatti stasera?', 'Decide l’app.'), ('body', 'I turni di casa, giusti e senza discussioni.')], voce="In casa si litiga su chi lava i piatti? Facciamo decidere a un'app, così nessuno si lamenta.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi un’app con i turni di casa per Giulia, Marco e Luca: sei faccende, due a testa, che ruotano ogni settimana.')], voce='Dai i nomi, le faccende e ogni quanto devono girare.'),
 dict(panel=[('shot', '72_turni', 'tel', {'label': 'Il risultato vero'})], voce='Ecco la settimana. Ognuno ha le sue due faccende, e si spuntano quando sono fatte.'),
 dict(panel=[('shot', [(0.0, '72_turni'), (1.0, '72_turni2')], 'tel', {'taps': [(0.5, 0.86, 0.06)]})], voce='Arriva lunedì, tocchi ruota e le faccende passano al prossimo. Giusto per tutti.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Luca ha 10 anni, dagli le cose più leggere'), ('ed', 'Fatto. Luca ruota solo tra spazzatura, cane e tavola.')])], voce='Puoi tenere conto delle età, dei turni di lavoro, di chi è via nel fine settimana.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'L’app aiuta, ma le regole decidetele insieme a tavola.'), ('stamp', 'Pace in casa')], voce="L'app aiuta, ma le regole decidetele insieme, a tavola. Funziona molto meglio.", zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
