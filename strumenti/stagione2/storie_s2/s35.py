NUM = 35
POSA = 'regge'
EDWIN_X = 560
SCENE = [
 dict(panel=[('title2', 'Un contratto', 'da firmare?'), ('body', 'Prima di firmare, fammelo leggere. Io non mi annoio con le clausole.')], voce='Hai un contratto da firmare? Fammelo leggere, io con le clausole non mi annoio.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Ti allego il contratto della palestra. Cosa devo controllare prima di firmare?')], voce='Lo alleghi, coprendo i tuoi dati, e mi chiedi cosa controllare.', posa='banco'),
 dict(panel=[('label', 'Da guardare bene', 'esempio inventato'), ('rows', [('Rinnovo automatico', 'art. 7'), ('Disdetta', 'solo con raccomandata'), ('Penale', '2 mensilità')])], voce='Ti segnalo i punti delicati, come il rinnovo automatico o la penale, e ti dico in che articolo sono.', x=470),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', "Spiegami l'articolo 7 in parole semplici"), ('ed', 'Se non disdici entro il 30 settembre, paghi un altro anno.')])], voce="E te li spiego in parole semplici. L'articolo sette, tradotto, vuol dire che se ti dimentichi, paghi."),
 dict(panel=[('label', 'Da sapere'), ('body', 'Non sono un avvocato: per contratti importanti, fatti consigliare da un professionista.'), ('stamp', 'Chiedi a un legale')], voce='Ricorda però che non sono un avvocato. Per casa, lavoro e cose grosse, chiedi a un professionista.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
