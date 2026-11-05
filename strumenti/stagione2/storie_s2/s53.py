NUM = 53
POSA = 'regge'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Serata in famiglia', 'senza idee?'), ('body', 'Ti costruisco un gioco a quiz da fare sul telefono, con le domande che vuoi tu.')], voce='Serata in famiglia senza idee? Ti costruisco un gioco a quiz.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Gioco a quiz per Natale: 15 domande sulla nostra famiglia, con punteggio e due squadre.')], voce='Mi dai le regole e qualche domanda, anche di famiglia. Chi russa più forte, per esempio.', posa='banco'),
 dict(panel=[('label', 'Il gioco'), ('rows', [('Squadra Nonni', '7 punti'), ('Squadra Nipoti', '9 punti'), ('Domanda 12 di 15', '')])], voce='Io scrivo il codice e tu vedi subito il gioco funzionare, con punteggio e squadre.', x=540, pop=45),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi un suono quando qualcuno vince'), ('ed', 'Aggiunto. È una trombetta, ti avviso.')])], voce='Lo cambi a parole. Aggiungi un suono? Ecco una trombetta, mi dispiace per i vicini.', zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Provalo prima di cena: meglio scoprire un errore da soli che davanti alla nonna.'), ('stamp', 'Provalo prima')], voce='Provalo prima di cena. Meglio scoprire un errore da soli che davanti alla nonna.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
