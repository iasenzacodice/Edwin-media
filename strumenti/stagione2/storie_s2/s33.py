NUM = 33
POSA = 'regge'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Un progetto grande', 'ti spaventa?'), ('body', 'Ristrutturare il bagno, organizzare una festa, cambiare lavoro.')], voce='Un progetto grande ti spaventa? Il segreto è tagliarlo a fette.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Devo rifare il bagno entro marzo. Dividimi il lavoro in passi con le date.')], voce="Dimmi l'obiettivo e la scadenza.", posa='banco'),
 dict(panel=[('label', 'Il piano', 'esempio inventato'), ('rows', [('Preventivi', 'entro 20 nov'), ('Scelta piastrelle', 'entro 10 dic'), ('Lavori', 'gennaio'), ('Collaudo', 'febbraio')])], voce='Ti preparo i passi in ordine, con le date. Ogni passo ha una sola cosa da fare.', x=520),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Il secondo passo è in ritardo'), ('ed', 'Sposto le date. Marzo è ancora salvo.')])], voce='Se qualcosa slitta, me lo dici e ricalcolo tutto. Il piano si adatta, non si butta.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Spunta i passi fatti: vedere la lista che si accorcia dà una carica incredibile.'), ('stamp', 'Una fetta alla volta')], voce='E spunta ogni passo fatto. Vedere la lista che si accorcia è meglio di un caffè.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
