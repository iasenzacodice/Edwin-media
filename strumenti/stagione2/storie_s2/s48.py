NUM = 48
POSA = 'regge'
EDWIN_X = 540
SCENE = [
 dict(panel=[('title2', 'Vuoi imparare', 'qualcosa di nuovo?'), ('body', 'Ti preparo un corso su misura, a tappe, con i tuoi tempi.')], voce='Vuoi imparare qualcosa di nuovo? Ti preparo un corso tutto tuo, a tappe.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', "Voglio imparare a fare il pane in casa. Ho un'ora la domenica. Preparami un corso di un mese.")], voce='Mi dici cosa vuoi imparare, da dove parti e quanto tempo hai.', posa='banco'),
 dict(panel=[('label', 'Il corso', 'esempio inventato'), ('rows', [('Settimana 1', 'farina, acqua, lievito'), ('Settimana 2', 'il primo filone'), ('Settimana 3', 'il lievito madre'), ('Settimana 4', 'la focaccia')])], voce='Io ti preparo le tappe, una per settimana, con la lista delle cose da comprare.', x=470),
 dict(panel=[('chat', 'Domenica', [('tu', 'Il pane è venuto basso e duro'), ('ed', "Lievitazione corta. Proviamo un'ora in più.")])], voce="E dopo ogni lezione mi racconti com'è andata. Il pane basso e duro capita a tutti, anche agli autòmi.", zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Va bene saltare una tappa: il corso si adatta, non ti giudica.'), ('stamp', 'Con i tuoi tempi')], voce='Se salti una settimana, il corso si adatta. Nessun voto, solo pane.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
