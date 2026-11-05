NUM = 36
POSA = 'banco'
EDWIN_X = 600
SCENE = [
 dict(panel=[('title2', 'Riunione finita.', 'E il verbale?'), ('body', 'Dagli appunti disordinati a un verbale chiaro, in un minuto.')], voce='Riunione finita e nessuno vuole scrivere il verbale? Lo scrivo io.'),
 dict(panel=[('label', 'I tuoi appunti'), ('typed', 'marco dice ok preventivo. budget max 5k?? sara chiama fornitore. prossima riunione giovedì forse')], voce='Mi dai gli appunti, anche così, scritti di corsa. Oppure la trascrizione che fa il telefono.'),
 dict(panel=[('label', 'Il verbale', 'esempio inventato'), ('rows', [('Decisione', 'preventivo approvato'), ('Budget', 'massimo 5.000 €'), ('Sara', 'chiama il fornitore'), ('Da confermare', 'riunione giovedì')])], voce='Io li metto in ordine. Decisioni, chi fa cosa, e cosa resta da chiarire.', x=520),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Scrivi la mail per mandarlo a tutti'), ('ed', 'Eccola, breve e con i compiti in grassetto.')])], voce='E se vuoi, ti preparo anche la mail per mandarlo a tutti. Così tutti sanno chi deve fare cosa.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Quello che non era chiaro negli appunti lo segno come da verificare, non me lo invento.'), ('stamp', 'Niente invenzioni')], voce='Quello che non è chiaro lo segno da verificare. Non invento decisioni, ne nascono già abbastanza in riunione.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
