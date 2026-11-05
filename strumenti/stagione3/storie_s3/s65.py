NUM = 65
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Difficile da spiegare?', 'Fanne un video animato.'), ('body', 'Disegni che si muovono valgono più di mille parole.')], voce='Devi spiegare una cosa a tanta gente? Un piccolo video animato funziona meglio di un foglio.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi un video animato di un minuto per spiegare la differenziata ai condòmini: i bidoni, cosa ci va dentro, i casi dubbi.')], voce="Dici l'argomento, chi lo guarderà e quanto deve durare."),
 dict(panel=[('shot', '65_s1', 'vid', {'label': 'Il risultato vero'})], voce="Ecco l'inizio. I quattro bidoni, ognuno con il suo colore, e gli oggetti che ci cadono dentro."),
 dict(panel=[('shot', '65_s2', 'vid')], voce='Poi i casi dubbi, uno per scena. La freccia mostra dove va, e la frase sotto spiega perché.'),
 dict(panel=[('label', 'Funziona per'), ('rows', [('Regole del condominio', ''), ('Istruzioni di lavoro', ''), ('Una ricetta', ''), ('Una lezione a scuola', '')])], voce='Funziona per tante cose. Le regole del condominio, le istruzioni al lavoro, una ricetta, una lezione.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Le regole della differenziata cambiano da Comune a Comune: controlla le tue prima di pubblicarlo.'), ('stamp', 'Controlla le fonti')], voce='Attenzione, le regole cambiano da Comune a Comune. Controlla le tue, prima di mandarlo a tutti.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
