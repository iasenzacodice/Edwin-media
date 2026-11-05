NUM = 39
POSA = 'banco'
EDWIN_X = 430
SCENE = [
 dict(panel=[('title2', 'Sembra scritto', 'da un robot?'), ('body', 'Per forza, sono un robot. Ma posso imparare a scrivere come te.')], voce='Quello che scrivo sembra scritto da un robot? Per forza, sono un robot. Ma posso imparare a scrivere come te.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Ecco tre messaggi che ho scritto io. Impara il mio modo di scrivere.')], voce='Mi dai qualche testo scritto da te, messaggi, mail, quello che vuoi.'),
 dict(panel=[('label', 'Il tuo stile', 'esempio inventato'), ('rows', [('Frasi corte', ''), ('Dai del tu a tutti', ''), ("Un po' di ironia", ''), ('Niente emoji', '')])], voce="Io noto come scrivi. Frasi corte, un po' di ironia, niente emoji.", x=520),
 dict(panel=[('chat', 'Poi', [('tu', 'Scrivi gli auguri al mio capo'), ('ed', 'Auguri capo. Un anno in più, ma la riunione delle otto resta.')])], voce='Poi, quando mi chiedi un messaggio, lo scrivo con la tua voce. Sembri tu, ma con meno fatica.', zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Rileggi sempre prima di mandare: se non ti suona tuo, dimmi cosa cambiare.'), ('stamp', 'Deve suonare tuo')], voce='Rileggi sempre. Se una frase non ti somiglia, dimmelo e la correggo.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
