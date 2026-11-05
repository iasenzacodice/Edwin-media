NUM = 51
POSA = 'banco'
EDWIN_X = 430
SCENE = [
 dict(panel=[('title2', 'Devi fare', 'un discorso?'), ('body', 'Matrimonio, pensione, compleanno. Le gambe tremano, il discorso no.')], voce='Devi fare un discorso e ti tremano le gambe? Il discorso almeno non tremerà.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Brindisi di 2 minuti per la pensione di mio padre: 40 anni in ferrovia, ama la pesca e le parole crociate.')], voce='Mi racconti la persona, qualche ricordo e quanto deve durare.'),
 dict(panel=[('label', 'La scaletta'), ('rows', [('Una battuta per rompere il ghiaccio', ''), ('Un ricordo vero', ''), ('Il grazie', ''), ('Il brindisi', '')])], voce='Ti propongo una scaletta, poi il testo. Corto, che i brindisi lunghi fanno scaldare lo spumante.', x=520, zoom=True),
 dict(panel=[('chat', 'Chiedimi ancora', [('tu', 'Più commovente alla fine'), ('ed', 'Cambiato il finale. Tieni un fazzoletto vicino.')])], voce='Più divertente o più commovente, si sistema a parole.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Leggilo ad alta voce due volte e cambia le parole che non diresti mai.'), ('stamp', 'Provalo a voce')], voce='Leggilo ad alta voce due volte, e cambia le parole che non diresti mai. Deve sembrare tuo, perché è tuo.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
