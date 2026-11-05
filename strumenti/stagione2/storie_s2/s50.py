NUM = 50
POSA = 'regge'
EDWIN_X = 600
SCENE = [
 dict(panel=[('title2', 'La favola', 'della buonanotte'), ('body', 'Ogni sera una storia nuova, con i personaggi che piacciono a tuo figlio.')], voce='Le favole sono finite? Ogni sera ne inventiamo una nuova.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Una favola di 3 minuti con un drago che ha paura del buio e un coniglio coraggioso.')], voce='Mi dici i personaggi e quanto deve durare. Tre minuti, prima che crolli dal sonno.', posa='banco'),
 dict(panel=[('label', 'La favola', 'esempio inventato'), ('body', "C'era una volta un drago enorme che dormiva con la lucina accesa. Una sera, la lucina si spense.")], voce="C'era una volta un drago enorme, che dormiva con la lucina accesa.", x=540, zoom=True),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Più corta, sta già dormendo'), ('ed', 'Fine. E vissero tutti felici e addormentati.')])], voce='Più corta? Nessun problema. E vissero tutti felici e addormentati.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Leggila tu, con la tua voce: la favola la scrivo io, la magia la fai tu.'), ('stamp', 'Leggila tu')], voce='Leggila tu, con la tua voce. Io scrivo la favola, la magia la fai tu.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
