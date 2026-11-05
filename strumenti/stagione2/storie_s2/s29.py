NUM = 29
POSA = 'banco'
EDWIN_X = 560
SCENE = [
 dict(panel=[('title2', 'Domani presenti', 'e non hai le slide?'), ('body', 'Respira. In cinque minuti ne facciamo una bozza seria.')], voce='Domani devi presentare e non hai neanche una slide? Respira. In cinque minuti facciamo una bozza seria.', posa='indica'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Presentazione di 6 slide sui risultati del gruppo di lettura: numeri, libri più amati, prossimi passi.')], voce="Dimmi l'argomento, quante slide e cosa non deve mancare."),
 dict(panel=[('label', 'La scaletta', 'esempio inventato'), ('rows', [('1. Titolo', ''), ("2. I numeri dell'anno", ''), ('3. I tre libri più amati', ''), ('4. Prossimi passi', '')])], voce="Prima ti propongo la scaletta, così decidi tu l'ordine. Poi preparo le slide, con titoli brevi e un grafico dove serve.", x=470),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Meno testo, più immagini'), ('ed', 'Ridotto. Ogni slide ora ha al massimo tre righe.')])], voce='Troppo testo? Lo dici e lo tolgo. Le slide piene di parole le legge solo chi le ha scritte.', zoom=True),
 dict(panel=[('label', 'E poi'), ('rows', [('Scaricala in PowerPoint o PDF', ''), ('Correggi a mano quello che vuoi', '')]), ('stamp', 'Provala a voce')], voce='La scarichi in PowerPoint o in PDF. E provala a voce almeno una volta, cronometro alla mano.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
