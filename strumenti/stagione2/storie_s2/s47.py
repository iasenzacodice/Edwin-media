NUM = 47
POSA = 'banco'
EDWIN_X = 600
SCENE = [
 dict(panel=[('title2', 'Compiti di matematica', 'e tu non ricordi niente?'), ('body', 'Tranquillo: io non do le soluzioni, faccio ragionare.')], voce='Compiti di matematica e tu non ti ricordi più niente? Tranquillo, ci penso io. Ma senza dare le soluzioni.'),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Aiuta mio figlio con le equazioni, ma non dargli la soluzione: fallo ragionare.')], voce='Me lo chiedi così, chiaro. Fallo ragionare.'),
 dict(panel=[('chat', 'Il tutor', [('tu', '3 più x fa 7. Quanto fa x?'), ('ed', 'Cosa aggiungi a 3 per arrivare a 7?'), ('tu', 'Ah, 4. Quindi x fa 4.')])], voce='Io faccio domande, un passo alla volta. E la risposta la trova lui, che è il bello.', x=520, zoom=True),
 dict(panel=[('label', 'Altre idee'), ('rows', [('Esercizi simili per allenarsi', ''), ('Spiegazioni con esempi di tutti i giorni', ''), ('Un riassunto per i genitori', '')])], voce='Posso preparare esercizi simili e spiegarti a che punto è, così lo segui anche tu.'),
 dict(panel=[('label', 'Da sapere'), ('body', "Stai vicino ai più piccoli mentre usano l'IA, e controlla quello che imparano."), ('stamp', 'Con un adulto')], voce='Con i più piccoli, stai vicino. Io sono un tutor, non una baby sitter.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
