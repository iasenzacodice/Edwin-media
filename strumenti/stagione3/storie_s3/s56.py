NUM = 56
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Prima e dopo', "Chiedere un'app"), ('body', 'Ogni venerdì: la stessa richiesta, fatta male e fatta bene.')], voce='Ecco la nuova rubrica del venerdì, prima e dopo. La stessa richiesta, fatta male e fatta bene.', posa='saluta'),
 dict(panel=[('chat', 'Prima', [('tu', "Fammi un'app"), ('ed', 'Certo. Ecco una lista dove scrivere delle cose.')])], voce="Prima. Scrivi fammi un'app e basta. Claude fa del suo meglio, ma deve indovinare tutto.", scossa=True),
 dict(panel=[('duo', [('56_banale', 'tel', 'Prima'), ('55_piena', 'tel', 'Dopo')])], voce="Il risultato? A sinistra una lista anonima. A destra l'app delle abitudini, fatta su misura."),
 dict(panel=[('label', 'Dopo: le 4 domande'), ('rows', [('Per chi è?', 'io, ogni sera'), ('Cosa deve fare?', 'spuntare'), ('Come appare?', 'grande'), ('Dove la uso?', 'telefono')])], voce='Cosa è cambiato? Quattro risposte. Per chi è, cosa deve fare, come appare e dove la usi.'),
 dict(panel=[('label', 'Il trucco'), ('typed', 'Prima di cominciare, fammi tu le domande che ti servono.')], voce='E se non sai cosa scrivere, chiedi a Claude di farti lui le domande. Rispondi, e il resto viene da sé.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Una richiesta vaga non è un errore: è solo un punto di partenza da correggere.'), ('stamp', 'Chiedi meglio')], voce='Una richiesta vaga non è un errore, è solo un punto di partenza. Si corregge parlando.', zoom=True),
 dict(panel=[('cta',)], voce='Ci vediamo venerdì prossimo con un nuovo prima e dopo.', posa='saluta'),
]
