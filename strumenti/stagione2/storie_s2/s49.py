NUM = 49
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Trasloco', 'in vista?'), ('body', 'Scatoloni, contratti, indirizzi da cambiare. Facciamo un piano.')], voce='Trasloco in vista? Scatoloni, contratti, indirizzi da cambiare. Facciamo un piano.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Trasloco il 15 gennaio, da Bologna a Modena, due adulti e un gatto. Fammi una lista settimana per settimana.')], voce='Mi dai la data e qualche dettaglio. Anche il gatto, che è importante.'),
 dict(panel=[('label', 'Il piano', 'esempio inventato'), ('rows', [('-4 settimane', 'preventivi ditte'), ('-3 settimane', 'disdetta utenze'), ('-1 settimana', 'scatoloni per stanza'), ('Il giorno', 'gatto dalla nonna')])], voce='Ti preparo le cose da fare settimana per settimana. Il gatto dalla nonna, il giorno del trasloco.', x=560, pop=33),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Chi devo avvisare del cambio di indirizzo?'), ('ed', 'Ecco la lista: banca, medico, assicurazione e altri 6.')])], voce='E la lista di chi avvisare del nuovo indirizzo. È sempre più lunga di quanto pensi.', zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Per scadenze e documenti ufficiali, controlla sui siti del Comune e degli enti.'), ('stamp', 'Siti ufficiali')], voce='Per i documenti ufficiali, controlla sempre sui siti del Comune. Io organizzo, non timbro.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
