NUM = 74
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Prima e dopo', 'Chiedere un PDF'), ('body', 'Stesso circolo, stesso programma, due risultati.')], voce='Venerdì, prima e dopo. Oggi un documento da stampare.', posa='saluta'),
 dict(panel=[('chat', 'Prima', [('tu', 'Scrivi il programma del circolo'), ('ed', 'Ecco un testo con le attività previste.')])], voce='Prima. Scrivi il programma del circolo. Arriva un testo generico, senza date e senza vita.', scossa=True),
 dict(panel=[('duo', [('74_banale', 'doc', 'Prima'), ('73_int', 'doc', 'Dopo')])], voce='A sinistra un muro di parole. A destra un libretto che i soci leggono davvero.'),
 dict(panel=[('label', 'Dopo: cosa ho detto'), ('rows', [('Per chi', 'i soci'), ('Cosa', 'le date del 2027'), ('Stile', 'caldo, con foto'), ('Formato', 'PDF A4')])], voce='Cosa è cambiato? Per chi è, cosa contiene, lo stile e il formato.'),
 dict(panel=[('label', 'Il trucco'), ('typed', 'Ecco le date vere: 14 marzo gara, 25 aprile pranzo, 19 giugno torneo, 11 settembre festa.')], voce='E il dettaglio più importante, i dati veri. Senza date vere, Claude può solo restare sul vago.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Se non dai le informazioni, non devono comparire inventate: controlla ogni data.'), ('stamp', 'Prima e dopo')], voce='Controlla sempre ogni data. Le informazioni importanti dalle tu, non devono comparire inventate.', zoom=True),
 dict(panel=[('cta',)], voce='Ci vediamo venerdì prossimo con un nuovo prima e dopo.', posa='saluta'),
]
