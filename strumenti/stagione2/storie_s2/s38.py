NUM = 38
POSA = 'regge'
EDWIN_X = 470
SCENE = [
 dict(panel=[('title2', 'Le skill:', 'insegnami una volta'), ('body', 'Un procedimento che ripeti spesso? Lo imparo e lo rifaccio uguale.')], voce="C'è un procedimento che ripeti sempre uguale? Insegnamelo una volta, con le skill."),
 dict(panel=[('label', 'Richiesta a Edwin'), ('typed', 'Quando ti mando una fattura, segna data, importo e fornitore e mettila nel foglio delle spese.')], voce='Mi spieghi i passi, come li spiegheresti a un collega nuovo.', posa='banco'),
 dict(panel=[('label', 'La skill', 'esempio inventato'), ('rows', [('1. Leggi la fattura', ''), ('2. Trova data, importo e fornitore', ''), ('3. Aggiungi una riga al foglio', '')])], voce='Io li salvo come una skill, una specie di ricetta. Passo uno, passo due, passo tre.', x=520),
 dict(panel=[('chat', 'Il mese dopo', [('tu', 'Ecco la fattura della luce'), ('ed', 'Fatto. Riga aggiunta: 87 €, Energia Spa.')])], voce='La volta dopo basta mandarmi la fattura. La ricetta la conosco già.', zoom=True),
 dict(panel=[('label', 'Da sapere'), ('body', 'Controlla le prime volte che il risultato sia giusto, poi correggi la ricetta se serve.'), ('stamp', 'Prova e correggi')], voce='Le prime volte controlla il risultato. Anche il miglior cuoco sbaglia la prima torta.'),
 dict(panel=[('cta',)], voce='Seguimi per il prossimo congegno, arriva presto.', posa='saluta'),
]
