NUM = 44
POSA = 'regge'
EDWIN_X = 560
SCENE = [
 dict(panel=[('title2', 'Una festa', 'in arrivo?'), ('body', 'Ti preparo un invito tutto tuo, da stampare o mandare sul telefono.')], voce="Hai una festa in arrivo? Ti preparo l'invito, tutto tuo."),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Invito per i 40 anni di Giulia, sabato 14 alle 20, tema anni Ottanta, colori fluo.')], voce='Mi dici chi festeggia, quando, dove e che stile vuoi.', posa='banco'),
 dict(panel=[('label', 'Le proposte'), ('buttons', ['Anni Ottanta, fluo', 'Elegante, oro e nero', 'Fumetto'], 0)], voce='Ti propongo qualche stile diverso e scegli tu. Anni Ottanta, ovviamente, con i colori che fanno male agli occhi.', x=470),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi: niente regali, solo allegria'), ('ed', 'Aggiunto in fondo, ben visibile.')])], voce='Lo ritocchi a parole, e alla fine lo scarichi come immagine o PDF.', zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Rileggi data, ora e indirizzo: sono le tre cose che nessuno ti perdona.'), ('stamp', 'Data e indirizzo')], voce='Rileggi data, ora e indirizzo. Sono le tre cose che gli invitati non ti perdonano.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
