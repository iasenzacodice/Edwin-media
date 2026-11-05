NUM = 32
POSA = 'banco'
EDWIN_X = 600
SCENE = [
 dict(panel=[('title2', 'E se ti scrivessi', 'io, ogni lunedì?'), ('body', "Con le attività programmate faccio una cosa da solo, all'ora che decidi tu.")], voce='E se fossi io a scriverti, ogni lunedì mattina? Con le attività programmate posso farlo.', posa='indica'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Ogni lunedì alle 8 preparami il riepilogo della settimana: impegni, scadenze e meteo.')], voce='Mi dici cosa fare e quando. Ogni lunedì alle otto, per esempio.'),
 dict(panel=[('label', 'Lunedì, ore 8', 'esempio inventato'), ('rows', [('3 impegni', ''), ('Bollo auto', 'scade venerdì'), ('Meteo', 'pioggia mercoledì')])], voce='E il lunedì trovi il riepilogo pronto. Io mi sveglio presto, tanto non dormo.', zoom=True),
 dict(panel=[('label', 'Altre idee'), ('rows', [('Ogni sera: la lista della spesa', ''), ('Ogni mese: le scadenze di casa', ''), ('Ogni venerdì: le notizie del tuo settore', '')])], voce='Funziona per tante cose ripetitive. La lista della spesa, le scadenze di casa, le notizie del tuo lavoro.', x=520),
 dict(panel=[('label', 'Da sapere'), ('body', 'Le attività programmate si vedono e si fermano in qualsiasi momento.'), ('stamp', 'Le fermi tu')], voce='Le vedi tutte in un elenco e le fermi quando vuoi. Comandi tu, io eseguo.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
