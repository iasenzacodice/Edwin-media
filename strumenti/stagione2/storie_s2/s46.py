NUM = 46
POSA = 'regge'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Esame in arrivo?', 'Facciamo le carte.'), ('body', 'Dai tuoi appunti preparo flashcard e quiz per ripassare.')], voce='Hai un esame in arrivo? Dai tuoi appunti preparo le flashcard per ripassare.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Ecco i miei appunti sulla Rivoluzione francese. Fammi 20 flashcard e un quiz.')], voce='Mi dai gli appunti, anche fotografati.', posa='banco', pop=34),
 dict(panel=[('chat', 'Flashcard 7 di 20', [('ed', 'In che anno cade la Bastiglia?'), ('tu', '1798'), ('ed', "Quasi. 1789: le cifre giuste, l'ordine no.")])], voce="Poi ti interrogo. E se sbagli te lo dico gentilmente. L'ordine delle cifre conta.", x=540, zoom=True),
 dict(panel=[('label', 'Il tuo ripasso'), ('rows', [('Sapute', '14'), ('Da ripassare', '6'), ('Domani', 'solo le 6 sbagliate')])], voce='Alla fine sai cosa ripassare. Domani solo le carte sbagliate.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Controlla le carte con il libro: se un appunto è sbagliato, lo è anche la carta.'), ('stamp', 'Controlla sul libro')], voce="Controlla le carte con il libro. Se l'appunto è sbagliato, la carta lo ripete."),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
