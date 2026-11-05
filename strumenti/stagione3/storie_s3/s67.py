NUM = 67
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Bollette e carburante?', 'Tutto in un colpo d’occhio.'), ('body', 'Una dashboard: una pagina che riassume i tuoi numeri.')], voce="Le bollette dell'anno sono sparse ovunque? Mettiamole in una pagina sola, che si capisce al volo.", posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Ti allego le spese di casa del 2026. Fammi una pagina con i totali, la spesa mese per mese e dove vanno i soldi.')], voce="Allega i tuoi numeri, anche un foglio disordinato, e di' cosa vuoi vedere."),
 dict(panel=[('shot', '67_dash', 'web', {'label': 'Il risultato vero'})], voce='Ecco la pagina. In alto i totali, sotto i mesi e le voci, dalla più pesante alla più leggera.'),
 dict(panel=[('label', 'Si capisce subito'), ('rows', [('Dicembre è il mese più caro', '454 €'), ('Il gas è salito', '+4%'), ('Il carburante pesa di più', '1.704 €')])], voce='E si capisce subito quello che conta. Dicembre è il mese più caro, il gas è salito, il carburante pesa più di tutto.'),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Aggiungi il confronto con il 2025'), ('ed', 'Fatto. Ogni mese ora ha anche la barra dell’anno scorso.')])], voce='E puoi chiedere confronti, filtri, o un riepilogo da mandare in famiglia.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Controlla due o tre totali sul foglio originale. Se i dati sono sbagliati, la pagina sarà bella ma sbagliata.'), ('stamp', 'Ricontrolla')], voce='Controlla sempre due o tre totali sul foglio originale. Una pagina bella con dati sbagliati resta sbagliata.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
