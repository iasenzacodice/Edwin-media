NUM = 68
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Prima e dopo', 'Chiedere un grafico'), ('body', 'Un grafico serve a rispondere a una domanda.')], voce='Venerdì, prima e dopo. Oggi un grafico.', posa='saluta'),
 dict(panel=[('chat', 'Prima', [('tu', 'Fammi un grafico delle spese'), ('ed', 'Ecco una torta con i dodici mesi.')])], voce='Prima. Fammi un grafico delle spese. E arriva una torta con dodici fette tutte uguali.', scossa=True),
 dict(panel=[('duo', [('68_banale', 'web', 'Prima'), ('67_dash', 'web', 'Dopo')])], voce='A sinistra non si capisce niente. A destra si vede subito qual è il mese più caro.'),
 dict(panel=[('label', 'Dopo: la richiesta'), ('typed', 'Voglio capire in che mese spendo di più. Barre dalla più alta, il mese più caro in rosso.')], voce='La differenza è la domanda. Non fammi un grafico, ma voglio capire in che mese spendo di più.'),
 dict(panel=[('label', 'Le domande giuste'), ('rows', [('Cosa voglio capire?', ''), ('Che dati uso?', ''), ('Chi lo guarderà?', '')])], voce='Prima di chiedere un grafico, chiediti cosa vuoi capire, che dati usi e chi lo guarderà.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Le torte vanno bene con poche fette. Per confrontare mesi, meglio le barre.'), ('stamp', 'Prima e dopo')], voce='Piccola regola. Le torte vanno bene con poche fette. Per confrontare tanti mesi, meglio le barre.', zoom=True),
 dict(panel=[('cta',)], voce='Ci vediamo venerdì prossimo con un nuovo prima e dopo.', posa='saluta'),
]
