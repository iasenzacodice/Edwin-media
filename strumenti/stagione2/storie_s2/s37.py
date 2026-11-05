NUM = 37
POSA = 'banco'
EDWIN_X = 540
SCENE = [
 dict(panel=[('title2', 'Ogni volta', 'ricominci da zero?'), ('body', "Con la memoria attiva, mi ricordo le cose importanti tra una chat e l'altra.")], voce='Ogni volta ricominci a spiegarmi chi sei? Con la memoria attiva, mi ricordo le cose importanti.'),
 dict(panel=[('chat', 'Lunedì', [('tu', 'Sono vegetariano e cucino per due'), ('ed', 'Ricevuto.')])], voce='Lunedì mi dici che sei vegetariano e cucini per due.', x=470),
 dict(panel=[('chat', "Venerdì, un'altra chat", [('tu', 'Idee per la cena?'), ('ed', 'Lasagne di verdure per due persone.')])], voce="Venerdì mi chiedi idee per la cena, in un'altra conversazione. E io non ti propongo l'arrosto.", zoom=True),
 dict(panel=[('label', 'Comandi tu'), ('rows', [('Vedi cosa ricordo', ''), ('Correggi o cancella', ''), ('Spegni la memoria', '')])], voce='Puoi vedere cosa ricordo, correggerlo o farmi dimenticare qualcosa. E puoi spegnere la memoria quando vuoi.', x=600),
 dict(panel=[('label', 'Da sapere'), ('body', 'Dimmi solo quello che ti fa comodo che io ricordi. Il resto, tienilo per te.'), ('stamp', 'Ricordo il giusto')], voce='Dimmi solo quello che ti è utile che io ricordi. Gli autòmi sono discreti, ma meno sanno meglio è.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
