NUM = 45
POSA = 'indica'
EDWIN_X = 540
SCENE = [
 dict(panel=[('title2', 'Un sito', 'senza programmare?'), ('body', 'Per un evento basta una pagina: data, luogo, programma e un pulsante per confermare.')], voce='Un sito senza programmare? Per un evento basta una pagina, e te la faccio io.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Pagina per la cena di classe: data, ristorante con mappa, menù e un pulsante per confermare.')], voce='Mi dici cosa deve esserci. Data, posto, programma.', posa='banco'),
 dict(panel=[('label', 'La pagina'), ('rows', [('Titolo e data', ''), ('Mappa del ristorante', ''), ('Menù', ''), ('Pulsante: ci sarò', '')])], voce='Io la costruisco e tu la vedi subito, pronta, anche dal telefono.', x=470, pop=44),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Metti la foto di classe del 1998'), ('ed', 'Messa. Avete tutti la stessa frangia.')])], voce='La cambi a parole. Una foto, un colore, una riga in più.', zoom=True),
 dict(panel=[('label', 'E poi'), ('rows', [('La condividi con un link', ''), ('La aggiorni quando vuoi', '')]), ('stamp', 'Niente dati sensibili')], voce='Poi la condividi con un link. Ma niente indirizzi di casa o numeri di telefono di tutti, mi raccomando.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
