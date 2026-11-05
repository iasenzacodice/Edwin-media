NUM = 28
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Stagione 2.', 'Si fa sul serio.'), ('body', 'Oggi niente risposte in chat: un documento vero, da tenere e condividere.')],
      voce="Bentornato nella stagione due. Oggi niente risposte in chat, facciamo un documento vero, da tenere e condividere.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Fammi un documento con il regolamento del condominio per la festa di Natale: orari, rumore, chi porta cosa.')],
      voce="Mettiamo che tu debba organizzare la festa di Natale del condominio. Mi chiedi un documento con regole e compiti.", posa='banco'),
 dict(panel=[('label', 'Il documento', 'esempio inventato'), ('rows', [('Titolo e data', ''), ('Orari della festa', '18-23'), ('Regole sul rumore', ''), ('Chi porta cosa', '12 nomi'), ('Contatti', '')])],
      voce="Io creo un documento a parte, con titoli e sezioni. Non è un messaggio che scorre via, è un file che resta.", x=420),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi una tabella con chi porta cosa'), ('ed', 'Fatto. Ho anche messo in grassetto le scadenze.')])],
      voce="Vuoi una tabella? Chiedila. Lo modifico io, oppure lo correggi tu direttamente, come un normale documento."),
 dict(panel=[('label', 'E poi'), ('rows', [('Scaricalo in Word o PDF', ''), ('Condividi il link', ''), ('Stampalo per la bacheca', '')])],
      voce="Alla fine lo scarichi in Word o in PDF, oppure condividi il link con i vicini. Così nessuno può dire che non lo sapeva.", zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Rileggi sempre nomi, date e numeri prima di mandarlo a tutti.'), ('stamp', 'Rileggi prima')],
      voce="Prima di mandarlo a tutto il palazzo, rileggi nomi e date. Il vicino del terzo piano è permaloso, lo so."),
 dict(panel=[('cta',)], voce="Seguimi per il prossimo congegno, arriva presto.", posa='saluta'),
]
