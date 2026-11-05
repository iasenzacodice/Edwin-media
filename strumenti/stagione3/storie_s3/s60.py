NUM = 60
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Il sito è pronto.', 'Ora mostralo a tutti.'), ('body', 'Un link da mandare su WhatsApp, da stampare o da mettere in vetrina.')], voce='Il sito è pronto. Ma come lo fai vedere agli altri? Con un link.', posa='saluta'),
 dict(panel=[('label', 'Come si fa'), ('rows', [('Apri il sito che hai creato', ''), ('Premi Pubblica', ''), ('Copia il link', ''), ('Mandalo a chi vuoi', '')])], voce='Apri quello che hai creato, premi pubblica e copia il link. Chi lo apre vede il sito, non la tua conversazione.'),
 dict(panel=[('shot', '58_sito_tel', 'tel', {'label': 'Aperto dal link'})], voce='Chi riceve il link lo apre dal telefono, come un qualsiasi sito.'),
 dict(panel=[('chat', 'Dove metterlo', [('tu', 'Dove lo posso usare?'), ('ed', 'Nella bio di Instagram, nel profilo di Google, su un biglietto o in vetrina.')])], voce='Mettilo nella bio, nella scheda del negozio, su un biglietto da visita o su un cartello in vetrina.'),
 dict(panel=[('label', 'E se lo cambi?'), ('body', 'Quando modifichi il sito, ricordati di pubblicare di nuovo la versione aggiornata.')], voce='E se poi lo modifichi, ricordati di pubblicare di nuovo la versione aggiornata.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Pubblicare vuol dire che chiunque abbia il link può vederlo: niente dati privati sulla pagina.'), ('stamp', 'Pubblico vuol dire pubblico')], voce='Ricorda, pubblico vuol dire pubblico. Chiunque abbia il link lo vede, quindi niente dati privati sulla pagina.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
