NUM = 34
POSA = 'banco'
EDWIN_X = 430
SCENE = [
 dict(panel=[('title2', 'Una domanda', 'da cento link?'), ('body', 'Con la ricerca approfondita leggo io decine di fonti al posto tuo.')], voce='Hai una domanda che richiederebbe cento link? Con la ricerca approfondita li leggo io.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Pompa di calore o caldaia a condensazione per una casa di 90 metri quadri? Costi, incentivi, pro e contro.')], voce='Fai una domanda vera, di quelle che ti tengono sveglio la sera.'),
 dict(panel=[('label', 'Sto cercando'), ('rows', [('Siti di enti pubblici', '14'), ('Associazioni di consumatori', '6'), ('Articoli tecnici', '9')])], voce='Io cerco, leggo e confronto. Ci metto qualche minuto, intanto puoi fare altro.', x=520, pop=28),
 dict(panel=[('label', 'Il resoconto', 'esempio inventato'), ('rows', [('Riassunto in 5 righe', ''), ('Tabella dei costi', ''), ('Le fonti, una per una', '')])], voce='Alla fine ti do un resoconto ordinato, con le fonti per ogni affermazione.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Apri sempre le fonti. Per le scelte importanti chiedi anche a un tecnico.'), ('stamp', 'Apri le fonti')], voce='Le fonti sono lì apposta, controllale. E prima di firmare chiedi anche a un tecnico.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
