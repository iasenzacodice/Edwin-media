NUM = 79
POSA = 'banco'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Un sito completo', 'in un pomeriggio.'), ('body', 'Più pagine, un modulo di iscrizione, il link da mandare.')], voce='Ultima riga della stagione. Mettiamo insieme tutto e costruiamo un sito completo, in un pomeriggio.', posa='saluta'),
 dict(panel=[('label', 'Richiesta a Claude'), ('typed', 'Fammi il sito del torneo di calcetto dei bar: home con data e posti liberi, pagina delle regole e una per iscrivere la squadra. Colori blu e giallo.')], voce="Dici quali pagine vuoi, cosa c'è in ognuna e i colori."),
 dict(panel=[('shot', '79_home', 'web', {'label': 'Il risultato vero'})], voce='Ecco la home. La data, il campo, e i numeri che contano: squadre, posti liberi, giorni mancanti.'),
 dict(panel=[('shot', [(0.0, '79_regole'), (1.6, '79_iscr')], 'web', {'taps': [(1.0, 0.93, 0.05)]})], voce='Poi le regole, e la pagina per iscriversi. Si compila e arriva la conferma.'),
 dict(panel=[('label', 'Il pomeriggio'), ('rows', [('Prima bozza', '15 min'), ('Correzioni a parole', '1 ora'), ('Testi e foto veri', '1 ora'), ('Pubblica e condividi', '5 min')])], voce='Come si divide il pomeriggio? Prima bozza, correzioni a parole, testi e foto veri, poi pubblichi.'),
 dict(panel=[('label', 'Da sapere'), ('body', 'Se raccogli i dati delle persone, chiedi solo quelli che servono e spiega a cosa servono.'), ('stamp', 'Pochi dati')], voce='Se raccogli iscrizioni, chiedi solo i dati che servono, e spiega a cosa servono.', zoom=True),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
