NUM = 30
POSA = 'banco'
EDWIN_X = 430
SCENE = [
 dict(panel=[('title2', 'Un foglio', 'che fa i conti da solo'), ('body', 'Non una tabella da riempire a mano: un foglio con le formule già pronte.')], voce='Oggi non una tabella qualunque, ma un foglio che fa i conti da solo.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Foglio per dividere le spese della vacanza tra 4 amici: chi ha pagato cosa e chi deve quanto a chi.')], voce='Ad esempio, dividere le spese di una vacanza tra quattro amici. Il classico disastro di fine viaggio.'),
 dict(panel=[('label', 'Il foglio', 'esempio inventato'), ('rows', [('Spese inserite', '12'), ('Totale', '1.240 €'), ('A testa', '310 €'), ('Luca deve a Sara', '45 €')])], voce='Ti preparo il foglio con le formule. Tu scrivi chi ha pagato e quanto, il resto si aggiorna da solo.', x=520),
 dict(panel=[('label', 'Ops'), ('body', 'Luca deve a Sara 4.500 €.'), ('stamp', 'Errore')], voce='Ops, quattromilacinquecento euro. Ho sbagliato a leggere una virgola. Ecco perché i totali si controllano sempre.', scossa=True, zoom=True),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi una colonna per la benzina'), ('ed', 'Aggiunta. Anche il totale ora la conta.')])], voce='Poi lo modifichi quando vuoi, a parole. E lo scarichi come file Excel.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
