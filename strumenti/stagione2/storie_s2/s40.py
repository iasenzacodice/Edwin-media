NUM = 40
POSA = 'banco'
EDWIN_X = 600
SCENE = [
 dict(panel=[('title2', 'I tuoi documenti', 'sono nel cloud?'), ('body', 'Se colleghi il tuo spazio, li cerco e li leggo io.')], voce='I tuoi documenti sono su Google Drive? Se lo colleghi, li cerco e li leggo io.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', "Trova il preventivo del giardiniere dell'anno scorso e dimmi quanto avevamo pagato.")], voce='Mi chiedi una cosa che non ricordi dove hai messo.', pop=28),
 dict(panel=[('label', 'Trovato', 'esempio inventato'), ('rows', [('Preventivo_giardino.pdf', 'marzo'), ('Totale', '640 €'), ('Fattura pagata', 'aprile')])], voce="Io cerco tra i tuoi file e ti rispondo, dicendoti da quale documento l'ho preso.", x=520),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Confrontalo con quello nuovo'), ('ed', 'Il nuovo costa 90 € in più, per due tagli in più.')])], voce='Posso anche confrontare due documenti. Il nuovo preventivo costa di più, ma ti spiego perché.', zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Il collegamento lo attivi tu e lo togli quando vuoi. Vedo solo quello che mi permetti.'), ('stamp', 'Accesso tuo')], voce='Il collegamento lo attivi tu e lo togli quando vuoi. Vedo solo quello a cui mi dai accesso.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
