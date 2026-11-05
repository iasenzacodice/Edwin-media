NUM = 52
POSA = 'banco'
EDWIN_X = 540
SCENE = [
 dict(panel=[('title2', 'Ti fidi', 'ciecamente?'), ('body', 'Non farlo. Chiedimi di ricontrollare: è un trucco che funziona davvero.')], voce='Ti fidi di me ciecamente? Non farlo. Ti insegno un trucco per farmi ricontrollare.'),
 dict(panel=[('label', 'La mia risposta'), ('body', 'Il Monte Bianco è alto 4.088 metri.')], voce='Mettiamo che io ti dica che il Monte Bianco è alto quattromilaottantotto metri.', x=470),
 dict(panel=[('chat', 'Il trucco', [('tu', 'Ricontrolla: sei sicuro?'), ('ed', 'Mi correggo: circa 4.806 metri. Avevo invertito le cifre.')])], voce="Mi chiedi, sei sicuro? Ricontrolla. E io rileggo e trovo l'errore. Avevo invertito le cifre.", scossa=True, zoom=True),
 dict(panel=[('label', 'Frasi che funzionano'), ('rows', [('Cosa potrebbe essere sbagliato?', ''), ('Dammi le fonti', ''), ('Rifallo passo per passo', '')])], voce='Altre frasi utili. Cosa potrebbe essere sbagliato? Dammi le fonti. Rifallo passo per passo.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Per salute, soldi e leggi, il controllo finale lo fa una persona competente.'), ('stamp', 'Ricontrolla')], voce='E per salute, soldi e leggi, il controllo finale lo fa sempre una persona competente.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
