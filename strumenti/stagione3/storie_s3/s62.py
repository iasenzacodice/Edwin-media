NUM = 62
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Prima e dopo', 'Chiedere un gioco'), ('body', 'Stessa idea, due richieste diverse.')], voce='Venerdì, quindi prima e dopo. Oggi chiediamo un gioco.', posa='saluta'),
 dict(panel=[('chat', 'Prima', [('tu', 'Fammi un gioco'), ('ed', 'Ecco un quadrato che salta un ostacolo.')])], voce='Prima. Fammi un gioco. Claude ne fa uno, ma non sa per chi, né come vuoi giocarci.', scossa=True),
 dict(panel=[('duo', [('62_banale', 'tel', 'Prima'), ('61_gioco', 'tel', 'Dopo')])], voce="A sinistra un quadrato blu e la tastiera, che sul telefono non c'è. A destra il gioco vero."),
 dict(panel=[('label', 'Dopo: cosa ho aggiunto'), ('rows', [('Che gioco è', 'salti e monete'), ('Come si comanda', 'tocco'), ('Quanti livelli', 'tre'), ('Per chi', '8 anni')])], voce='Cosa è cambiato? Che gioco è, come si comanda, quanti livelli e per chi è.'),
 dict(panel=[('label', 'Il trucco'), ('typed', 'Il gioco lo usa un bambino di 8 anni sul telefono.')], voce='Il dettaglio che cambia tutto è dire chi gioca e su cosa. Un bambino sul telefono non ha la tastiera.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Prova il gioco tu per primo e chiedi le correzioni una alla volta.'), ('stamp', 'Prima e dopo')], voce='Prova sempre il gioco tu per primo, e chiedi le correzioni una alla volta.', zoom=True),
 dict(panel=[('cta',)], voce='Ci vediamo venerdì prossimo con un nuovo prima e dopo.', posa='saluta'),
]
