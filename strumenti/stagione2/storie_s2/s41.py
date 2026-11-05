NUM = 41
POSA = 'regge'
EDWIN_X = 540
SCENE = [
 dict(panel=[('title2', 'La cartella Download', 'è un disastro?'), ('body', "Con l'app sul computer posso mettere ordine nei tuoi file.")], voce="La cartella dei download è un disastro? Se colleghi l'app sul computer, metto ordine io."),
 dict(panel=[('label', 'Prima', 'esempio inventato'), ('rows', [('IMG_4432.jpg', '-'), ('documento (3) finale.pdf', '-'), ('scan001.pdf', '-'), ('bolletta.pdf', '-')])], voce='Prima, nomi a caso. Documento tre finale, finale vero, finale definitivo.', posa='banco', zoom=True),
 dict(panel=[('label', 'Dopo'), ('rows', [('Bollette / 2026', '12 file'), ('Foto / Mare 2026', '86 file'), ('Casa / Contratti', '5 file')])], voce='Dopo, cartelle con nomi chiari e file rinominati con data e argomento.', x=470),
 dict(panel=[('chat', 'Prima di toccare', [('ed', 'Ti propongo questo ordine. Procedo?'), ('tu', 'Sì, ma non cancellare niente')])], voce='Prima di spostare qualsiasi cosa ti mostro il piano e aspetto il tuo sì.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Fai sempre una copia dei file importanti. E le cancellazioni le confermi tu.'), ('stamp', 'Prima una copia')], voce='Tieni sempre una copia dei file importanti. Riordinare è bello, perdere le foto delle vacanze no.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
