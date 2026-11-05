NUM = 81
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Il viaggio è finito.', 'Il tuo comincia ora.'), ('body', 'Ventisette tappe: app, siti, giochi, video e documenti.')], voce="Siamo arrivati alla fine dell'atlante. Ventisette tappe, e adesso tocca a te.", posa='saluta'),
 dict(panel=[('shot', [(0.0, '55_piena'), (1.2, '61_gioco'), (2.4, '69_calc'), (3.6, '63_ok')], 'tel', {'label': 'Fatti in questa stagione'})], voce="Un'app per le abitudini, un videogioco, un calcolatore, una caccia al tesoro."),
 dict(panel=[('shot', [(0.0, '57_mappa'), (1.2, '67_dash'), (2.4, '75_s2'), (3.6, '79_home')], 'web')], voce='Una mappa di viaggio, i numeri di casa, le slide animate, un sito completo. Tutto senza scrivere codice.'),
 dict(panel=[('label', 'Le rotte della stagione'), ('rows', [('Di’ per chi è e cosa fa', ''), ('Correggi a parole', ''), ('Un passo alla volta', ''), ('Controlla i dati', '')])], voce="Le regole del viaggio sono quattro. Di' per chi è e cosa fa, correggi a parole, un passo alla volta, controlla i dati."),
 dict(panel=[('chat', 'Tocca a te', [('ed', 'Cosa vorresti costruire?'), ('ed', 'Scrivilo nei commenti: magari diventa una tappa.')])], voce='E adesso dimmi tu. Cosa vorresti costruire? Scrivilo nei commenti, magari diventa una tappa della prossima stagione.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Le idee migliori nascono da un problema vero di casa o di lavoro. Comincia da lì.'), ('stamp', 'Buon viaggio')], voce='Le idee migliori nascono da un problema vero, di casa o di lavoro. Comincia da lì.', zoom=True),
 dict(panel=[('cta',)], voce='Grazie di aver viaggiato con me. Ci vediamo nella stagione quattro.', posa='saluta'),
]
