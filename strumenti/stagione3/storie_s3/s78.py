NUM = 78
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Duecento file a caso?', 'In ordine in un colpo.'), ('body', 'Rinominare, dividere in cartelle, unire i PDF.')], voce='La cartella dei download è un disastro? Mettiamo in ordine duecento file in un colpo.', posa='saluta'),
 dict(panel=[('shot', '78_prima', 'web', {'label': 'Prima'})], voce='Ecco come si presenta. Nomi senza senso, foto e documenti tutti mescolati.', scossa=True),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Rinomina le foto con data e luogo, mettile in una cartella per viaggio, e sposta i PDF in Documenti. Prima fammi vedere il piano.')], voce="Collega la cartella o carica i file, e spiega l'ordine che vuoi. E chiedi di vedere prima il piano."),
 dict(panel=[('shot', '78_dopo', 'web', {'label': 'Dopo'})], voce='Ed ecco il risultato. Una cartella per ogni viaggio, le foto con data e luogo, i documenti a parte.'),
 dict(panel=[('label', 'Si può fare'), ('rows', [('Unire tanti PDF in uno', ''), ('Rimpicciolire le foto', ''), ('Trovare i doppioni', '')])], voce='Puoi anche unire tanti PDF in uno, rimpicciolire le foto, trovare i doppioni.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Prima di tutto fai una copia della cartella. E controlla il piano prima di dire sì.'), ('stamp', 'Copia prima')], voce="La regola d'oro, prima di tutto fai una copia della cartella. E controlla il piano prima di dire sì.", zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
