NUM = 69
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Quanto costa il viaggio?', 'Fatti un calcolatore.'), ('body', 'Uno strumento piccolo, fatto per una domanda sola.')], voce='Weekend in auto con gli amici? Invece di fare i conti a mano, fatti un calcolatore.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi un calcolatore per il costo di un viaggio in auto: chilometri, consumo, prezzo del carburante, pedaggi e persone. Il risultato a testa.')], voce='Elenca cosa entra nel conto e cosa vuoi sapere alla fine.'),
 dict(panel=[('shot', '69_calc', 'tel', {'label': 'Il risultato vero'})], voce='Ecco lo strumento. Scrivi i numeri e il conto si fa da solo, con la quota a testa.'),
 dict(panel=[('shot', [(0.0, '69_calc'), (1.0, '69_calc3')], 'tel', {'taps': [(0.5, 0.82, 0.6)]})], voce='Se uno degli amici non viene, cambi le persone e la quota si aggiorna subito.'),
 dict(panel=[('label', 'Altre idee'), ('rows', [('Dividere le bollette', ''), ('Quanta pittura serve', ''), ('La rata di un acquisto', ''), ('Le dosi di una ricetta', '')])], voce='Puoi farne uno per tutto. Dividere le bollette, la pittura per una stanza, le dosi di una ricetta.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Fai una prova con un conto che conosci già: se torna, il calcolatore è giusto.'), ('stamp', 'Fai la prova')], voce='Prima di fidarti, fai una prova con un conto che conosci già. Se torna, il calcolatore è giusto.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
