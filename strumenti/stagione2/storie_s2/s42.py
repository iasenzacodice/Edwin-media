NUM = 42
POSA = 'banco'
EDWIN_X = 430
SCENE = [
 dict(panel=[('title2', 'Moduli online', 'infiniti?'), ('body', 'Con il browser collegato, posso compilarli al posto tuo.')], voce='Moduli online infiniti? Con il browser collegato, posso compilarli io.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Iscrivi mio figlio al corso di nuoto del Comune, turno del martedì.')], voce='Mi dici cosa fare. Iscrivere tuo figlio al corso di nuoto, per esempio.'),
 dict(panel=[('label', 'Sto compilando'), ('rows', [('Corso', 'nuoto ragazzi'), ('Turno', 'martedì 17:00'), ('Dati del bambino', 'da te')])], voce='Apro la pagina, scelgo il corso e il turno, e compilo i campi.', x=520),
 dict(panel=[('chat', 'Prima di inviare', [('ed', 'Tutto pronto. Controlli tu e premi invia?'), ('tu', 'Controllo e invio')])], voce="Prima dell'invio mi fermo. Controlli tu e premi tu il pulsante.", zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Le password le scrivi solo tu. Pagamenti e invii li confermi sempre tu.'), ('stamp', 'Invio tuo')], voce='Password e pagamenti restano roba tua. Io compilo, tu decidi.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
