NUM = 75
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Le solite slide noiose?', 'Falle muovere.'), ('body', 'Titoli grandi, poche parole e numeri che crescono davanti a tutti.')], voce='Devi presentare qualcosa e temi che si addormentino tutti? Facciamo slide che si muovono.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi 8 slide per l’assemblea di condominio sul nuovo cortile: tre proposte con i costi, grafici animati, pochissimo testo.')], voce="Dici l'occasione, quante slide, e che le vuoi animate e con poco testo."),
 dict(panel=[('shot', '75_s1', 'web', {'label': 'Il risultato vero'})], voce='La prima slide. Un titolo grande e una riga sola, niente muri di testo.'),
 dict(panel=[('shot', '75_s2', 'web')], voce='Poi i costi. Le barre crescono una alla volta, e tutti guardano la stessa cosa.'),
 dict(panel=[('label', 'Durante la presentazione'), ('rows', [('Si va avanti con le frecce', ''), ('Funziona da qualsiasi computer', ''), ('Basta il link', '')])], voce='Si aprono dal link, su qualsiasi computer, e vai avanti con le frecce.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Prova le slide sul computer della sala prima dell’assemblea. Tieni anche una copia in PDF.'), ('stamp', 'Prova generale')], voce='Fai sempre una prova sul computer della sala. E tieni una copia in PDF, non si sa mai.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
