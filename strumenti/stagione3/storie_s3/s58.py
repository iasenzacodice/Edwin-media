NUM = 58
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Un sito per il negozio?', 'Senza agenzia.'), ('body', 'Orari, indirizzo e un pulsante per ordinare. Il resto è decorazione.')], voce='Hai un negozio e niente sito? Ti faccio vedere come nasce in pochi minuti.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi il sito del Forno Rossi: pane col lievito madre, orari, indirizzo con la mappa e un pulsante per ordinare con un messaggio. Colori caldi.')], voce='Descrivi la tua attività, cosa deve trovare il cliente e che atmosfera vuoi.'),
 dict(panel=[('shot', '58_sito', 'web', {'label': 'Il risultato vero'})], voce='Ecco il sito. In alto il messaggio principale, sotto gli orari e dove trovarci.'),
 dict(panel=[('shot', '58_sito_tel', 'tel', {'label': 'Sul telefono'})], voce='E sul telefono si sistema da solo. È lì che lo guarderanno quasi tutti i tuoi clienti.'),
 dict(panel=[('label', 'Cosa non deve mancare'), ('rows', [('Cosa fai, in una frase', ''), ('Orari e indirizzo', ''), ('Come contattarti', ''), ('Foto vere del negozio', '')])], voce='Le quattro cose che non devono mai mancare. Cosa fai, orari e indirizzo, come contattarti, e foto vere.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Gli esempi qui sono inventati. Nel tuo metti dati veri e controlla ogni numero di telefono.'), ('stamp', 'Dati veri')], voce='Il Forno Rossi è inventato. Nel tuo sito metti dati veri e controlla ogni numero, uno per uno.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
