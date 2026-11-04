"""Genera i file storie/sN.py (Reel stile "Edwin fa la cosa") per i congegni delle righe 4-9."""
import importlib.util, math


def icon(n):
    spec = importlib.util.spec_from_file_location('c', f'contenuti/c{n}.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    return C.ICONA, C.TITOLO


def hook(n):
    ic, _ = icon(n)
    return f'<g transform="translate(390 98) scale(1.45)">{ic}</g><text x="540" y="136" font-family="Lora" font-weight="700" font-size="96" fill="#B3261E">?</text>'


def bars(vals, labels, hi=None):
    mx = max(vals); out = ''
    w = 560 / len(vals)
    for i, (v, l) in enumerate(zip(vals, labels)):
        h = v / mx * 150; x = 180 + i * w
        out += (f'<rect x="{x + 8:.0f}" y="{190 - h:.0f}" width="{w - 16:.0f}" height="{h:.0f}" fill="{"#B3261E" if i == hi else "#C08A3E"}"/>'
                f'<text x="{x + w / 2:.0f}" y="222" font-family="Inter" font-size="20" text-anchor="middle" fill="#5A341C">{l}</text>')
    return out + '<line x1="170" y1="190" x2="760" y2="190" stroke="#2A1E16" stroke-width="3"/>'


# oggetti di scena: (dietro Edwin, davanti a Edwin)
P = {}
P[11] = ('', '<g transform="translate(250 1440) rotate(-3)"><rect x="-110" y="-70" width="220" height="70" fill="#F7F0E0" stroke="#2A1E16" stroke-width="5"/>'
         '<line x1="-90" y1="-50" x2="60" y2="-50" stroke="#8C7350" stroke-width="5"/><line x1="-90" y1="-32" x2="80" y2="-32" stroke="#B3261E" stroke-width="5"/><line x1="-90" y1="-14" x2="40" y2="-14" stroke="#8C7350" stroke-width="5"/>'
         '<text x="60" y="-12" font-family="Lora" font-style="italic" font-size="26" fill="#B3261E">v2</text></g>'
         '<g transform="translate(880 1350) rotate(28)"><rect x="-20" y="-150" width="40" height="230" fill="#E3B657" stroke="#2A1E16" stroke-width="5"/><path d="M-20 80 L0 125 L20 80 Z" fill="#F3E9D2" stroke="#2A1E16" stroke-width="5"/><rect x="-20" y="-150" width="40" height="34" fill="#B45A30" stroke="#2A1E16" stroke-width="5"/></g>')
P[14] = ('<g transform="translate(180 1150)"><rect x="-120" y="-140" width="240" height="190" fill="#2F3B33" stroke="#7A4A26" stroke-width="14"/>'
         '<text x="0" y="-60" font-family="Lora" font-weight="700" font-size="40" fill="#F3E9D2" text-anchor="middle">SPREAD</text><text x="0" y="0" font-family="Lora" font-size="56" fill="#F3E9D2" text-anchor="middle">= ?</text>'
         '<line x1="-90" y1="50" x2="-120" y2="330" stroke="#7A4A26" stroke-width="12"/><line x1="90" y1="50" x2="120" y2="330" stroke="#7A4A26" stroke-width="12"/></g>', '')
P[15] = ('', '<g transform="translate(200 1380)"><rect x="-120" y="-150" width="240" height="210" rx="16" fill="#4A4F55" stroke="#2A1E16" stroke-width="6"/><rect x="-100" y="-130" width="200" height="170" rx="10" fill="#5C636B"/>'
         '<circle cx="0" cy="-45" r="46" fill="#C08A3E" stroke="#2A1E16" stroke-width="5"/>'
         + ''.join(f'<line x1="0" y1="-45" x2="{40 * math.cos(a / 6 * 6.283):.0f}" y2="{-45 + 40 * math.sin(a / 6 * 6.283):.0f}" stroke="#2A1E16" stroke-width="5"/>' for a in range(6))
         + '<rect x="70" y="-80" width="18" height="60" rx="6" fill="#C08A3E"/></g>')
P[17] = ('', '<g transform="translate(190 1420)"><rect x="-130" y="-50" width="260" height="90" rx="14" fill="#2A1E16"/><rect x="-110" y="-110" width="220" height="70" fill="#F7F0E0" stroke="#2A1E16" stroke-width="4"/>'
         '<line x1="-90" y1="-90" x2="60" y2="-90" stroke="#8C7350" stroke-width="4"/><line x1="-90" y1="-70" x2="80" y2="-70" stroke="#8C7350" stroke-width="4"/>'
         + ''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="#E3B657" stroke="#5A341C" stroke-width="3"/>' for y in (-14, 14) for x in range(-100, 110, 28)) + '</g>'
         '<g transform="translate(580 1356) rotate(3)"><rect x="-78" y="-100" width="156" height="200" fill="#fff" stroke="#2A1E16" stroke-width="5"/><rect x="-60" y="-82" width="38" height="44" fill="#C8B89A"/>'
         '<text x="10" y="-60" font-family="Liberation Mono" font-weight="700" font-size="18" fill="#2A1E16">CV</text><rect x="-60" y="-22" width="120" height="10" fill="#B45A30"/>'
         '<line x1="-60" y1="6" x2="60" y2="6" stroke="#8C7350" stroke-width="4"/><line x1="-60" y1="26" x2="50" y2="26" stroke="#8C7350" stroke-width="4"/><rect x="-60" y="50" width="120" height="10" fill="#B45A30"/><line x1="-60" y1="76" x2="40" y2="76" stroke="#8C7350" stroke-width="4"/></g>')
P[18] = ('', '<g transform="translate(860 1400)"><ellipse cx="0" cy="0" rx="120" ry="88" fill="#E8A0A0" stroke="#2A1E16" stroke-width="6"/><circle cx="104" cy="-14" r="34" fill="#E8A0A0" stroke="#2A1E16" stroke-width="6"/>'
         '<circle cx="96" cy="-20" r="5" fill="#2A1E16"/><circle cx="112" cy="-20" r="5" fill="#2A1E16"/><rect x="-30" y="-92" width="60" height="10" rx="4" fill="#2A1E16"/><circle cx="-40" cy="-30" r="8" fill="#2A1E16"/></g>'
         + ''.join(f'<ellipse cx="190" cy="{1468 - i * 16}" rx="56" ry="14" fill="#E3B657" stroke="#8C5A20" stroke-width="4"/>' for i in range(6)))
P[20] = ('', '<g transform="translate(180 1330)"><rect x="-130" y="-180" width="260" height="320" fill="#7A4A26" stroke="#2A1E16" stroke-width="6"/>'
         + ''.join(f'<rect x="-110" y="{-160 + i * 100}" width="220" height="84" fill="#9C5A30" stroke="#2A1E16" stroke-width="4"/><rect x="-60" y="{-134 + i * 100}" width="120" height="30" fill="#F7F0E0" stroke="#2A1E16" stroke-width="3"/><circle cx="0" cy="{-90 + i * 100}" r="8" fill="#E3B657"/>' for i in range(3))
         + ''.join(f'<text x="0" y="{-112 + i * 100}" font-family="Liberation Mono" font-weight="700" font-size="15" text-anchor="middle" fill="#2A1E16">{t}</text>' for i, t in enumerate(('PREFERENZE', 'CASA', 'LAVORO'))) + '</g>')
P[21] = ('', '<g transform="translate(870 1350)"><circle cx="0" cy="0" r="100" fill="#E8F6F4" stroke="#2A1E16" stroke-width="6"/><ellipse cx="0" cy="0" rx="40" ry="100" fill="none" stroke="#2A1E16" stroke-width="4"/>'
         '<line x1="-100" y1="0" x2="100" y2="0" stroke="#2A1E16" stroke-width="4"/><path d="M-60 -50 q30 -16 40 14 q-16 26 -44 10 z" fill="#6E9E5A"/><path d="M20 20 q40 -6 46 30 q-30 20 -50 -4 z" fill="#6E9E5A"/>'
         '<path d="M-120 0 A120 120 0 0 1 120 0" stroke="#C08A3E" stroke-width="10" fill="none"/><rect x="-10" y="100" width="20" height="40" fill="#C08A3E"/><rect x="-60" y="134" width="120" height="16" rx="6" fill="#7A4A26"/></g>'
         '<g transform="translate(520 1356) scale(1.35)"><circle cx="0" cy="0" r="56" fill="#fff" fill-opacity="0.45" stroke="#9C4A26" stroke-width="14"/><line x1="40" y1="40" x2="100" y2="100" stroke="#9C4A26" stroke-width="22" stroke-linecap="round"/></g>')
P[23] = ('<g transform="translate(200 1110)"><rect x="-150" y="-180" width="300" height="260" fill="#fff" stroke="#2A1E16" stroke-width="6"/><rect x="-150" y="-180" width="300" height="40" fill="#2f8a83"/>'
         + ''.join(f'<line x1="{x}" y1="-180" x2="{x}" y2="80" stroke="#2A1E16" stroke-width="2"/>' for x in (-70, 10, 90))
         + ''.join(f'<line x1="-150" y1="{y}" x2="150" y2="{y}" stroke="#C8B89A" stroke-width="2"/>' for y in range(-100, 80, 36))
         + '<rect x="-149" y="-28" width="298" height="36" fill="#E3B657" opacity="0.5"/><line x1="-110" y1="80" x2="-140" y2="380" stroke="#7A4A26" stroke-width="12"/><line x1="110" y1="80" x2="140" y2="380" stroke="#7A4A26" stroke-width="12"/></g>', '')
P[24] = ('', '<g transform="translate(870 1360)"><path d="M-30 100 L30 100 L14 -10 L-14 -10 Z" fill="#7A4A26"/><rect x="-90" y="90" width="180" height="40" rx="8" fill="#5A341C"/>'
         '<path d="M0 -10 L-70 -170 Q0 -200 70 -170 Z" fill="#E3B657" stroke="#8C5A20" stroke-width="6"/><circle cx="0" cy="-10" r="18" fill="#C08A3E"/></g>'
         '<g transform="translate(520 1350) scale(1.35)"><rect x="-56" y="-96" width="112" height="190" rx="18" fill="#2A1E16"/><rect x="-46" y="-80" width="92" height="150" rx="6" fill="#F7F0E0"/>'
         '<circle cx="0" cy="0" r="28" fill="#B3261E"/><rect x="-8" y="-16" width="16" height="26" rx="8" fill="#fff"/><path d="M-14 4 a14 14 0 0 0 28 0" stroke="#fff" stroke-width="4" fill="none"/></g>')
P[26] = ('<path d="M0 820 Q540 960 1080 820" stroke="#5A341C" stroke-width="5" fill="none"/>' + ''.join(
    f'<g transform="translate({x} {820 + 140 * (1 - ((x - 540) / 540) ** 2) * 0.9:.0f})"><path d="M-60 0 L60 0 L0 110 Z" fill="{c}"/><text x="0" y="40" font-family="Inter" font-weight="700" font-size="26" fill="#fff" text-anchor="middle">{t}</text></g>'
    for x, c, t in ((170, '#B45A30', '¡Hola!'), (420, '#2f8a83', 'Ciao'), (680, '#C08A3E', 'Hello'), (920, '#B3261E', 'Olá'))),
    '<g transform="translate(560 1356)"><path d="M0 -60 Q-60 -80 -120 -64 V60 Q-60 44 0 64 Z" fill="#fff" stroke="#2A1E16" stroke-width="5"/><path d="M0 -60 Q60 -80 120 -64 V60 Q60 44 0 64 Z" fill="#fff" stroke="#2A1E16" stroke-width="5"/>'
    '<line x1="-100" y1="-30" x2="-20" y2="-24" stroke="#8C7350" stroke-width="4"/><line x1="-100" y1="0" x2="-20" y2="6" stroke="#8C7350" stroke-width="4"/><line x1="20" y1="-24" x2="100" y2="-30" stroke="#8C7350" stroke-width="4"/><line x1="20" y1="6" x2="100" y2="0" stroke="#8C7350" stroke-width="4"/></g>')
P[27] = ('',
         '<g transform="translate(860 1350)"><path d="M-30 30 L-60 140 L-34 128 L-18 152 L4 50 Z" fill="#B3261E"/><path d="M30 30 L60 140 L34 128 L18 152 L-4 50 Z" fill="#2f8a83"/>'
         '<circle cx="0" cy="0" r="80" fill="#E3B657" stroke="#2A1E16" stroke-width="6"/><circle cx="0" cy="0" r="60" fill="none" stroke="#C08A3E" stroke-width="5"/><text x="0" y="30" font-family="Lora" font-weight="700" font-size="84" fill="#2A1E16" text-anchor="middle">5</text></g>')

DOC = ('<rect x="250" y="20" width="420" height="200" fill="#fff" stroke="#2A1E16" stroke-width="4"/><text x="280" y="62" font-family="Liberation Mono" font-weight="700" font-size="22" fill="#2A1E16">CONTRATTO</text>'
       '<text x="280" y="102" font-family="Liberation Mono" font-size="20" fill="#2A1E16">Nome:</text><rect x="380" y="84" width="230" height="24" fill="#111"/>'
       '<text x="280" y="142" font-family="Liberation Mono" font-size="20" fill="#2A1E16">Codice:</text><rect x="400" y="124" width="210" height="24" fill="#111"/><line x1="280" y1="180" x2="620" y2="180" stroke="#8C7350" stroke-width="4"/>')
XLS = ('<rect x="300" y="40" width="320" height="150" rx="14" fill="#fff" stroke="#2A1E16" stroke-width="4"/><rect x="320" y="70" width="90" height="90" rx="10" fill="#2f8a83"/>'
       '<text x="365" y="128" font-family="Inter" font-weight="700" font-size="36" fill="#fff" text-anchor="middle">X</text><text x="430" y="112" font-family="Liberation Mono" font-weight="700" font-size="22" fill="#2A1E16">spese.xlsx</text>'
       '<text x="430" y="144" font-family="Inter" font-size="18" fill="#8C7350">12 mesi · 4 colonne</text>')

CTA = "Seguimi per il prossimo congegno, arriva presto."
S = {
 11: dict(SET=('officina', ''), POSA='banco', X=560, sc=[
  ([('title2', 'La prima risposta', 'non ti convince?'), ('img', hook(11), 190)], "La prima risposta dell'IA non ti convince? Non ricominciare da capo, la sistemiamo insieme."),
  ([('label', 'Richiesta a Edwin'), ('typed', 'Scrivimi un messaggio per disdire la palestra.')], "Mettiamo che tu mi chieda un messaggio per disdire la palestra."),
  ([('label', 'Prima versione', 'esempio inventato'), ('body', "Gentile direzione, con la presente desidero comunicare la mia volontà di recedere dal contratto in essere.")], "Ecco la prima versione. Troppo formale? Nessun problema, dimmi cosa non va."),
  ([('label', 'Chiedimi ancora'), ('body', 'Cosa cambio?'), ('buttons', ['Più breve e più gentile', 'Cambia solo il finale', 'Dammi tre versioni'], 0)], "Puoi chiedermela più breve e più gentile, cambiare solo una parte, oppure farti dare tre versioni e scegliere."),
  ([('label', 'Seconda versione', 'esempio inventato'), ('body', "Ciao, dal mese prossimo vorrei disdire l'abbonamento. Grazie di tutto, è stato bello allenarmi da voi.")], "Due giri e il testo è tuo. E se una parola non ti è chiara, chiedimi di spiegartela."),
  ([('label', 'Da sapere'), ('body', 'Resta nella stessa conversazione: così ricordo quello che ci siamo detti.'), ('stamp', 'Correggere è normale')], "Resta nella stessa conversazione, così ricordo quello che ci siamo detti. Correggere è normale, anche per me."),
 ]),
 14: dict(SET=('colosso', 'torso'), POSA='indica', X=620, sc=[
  ([('title2', 'Certe cose sembrano', 'scritte per pochi?'), ('img', hook(14), 190)], "Il mutuo, lo spread, come funziona un vaccino. Certe cose sembrano scritte per pochi? Te le spiego io, senza vergogna."),
  ([('label', 'Richiesta a Edwin'), ('typed', "Spiegami cos'è lo spread come se avessi 10 anni.")], "Chiedimelo in parole semplici. Il trucco dei dieci anni funziona sempre."),
  ([('label', 'Risposta di Edwin', 'esempio semplificato'), ('body', "Due amici chiedono un prestito. A quello meno affidabile chiedono più interessi. Lo spread è quella differenza.")], "Ecco, niente paroloni. Due amici, un prestito, e la differenza negli interessi."),
  ([('label', 'Chiedimi ancora'), ('body', 'Vuoi capire meglio?'), ('buttons', ['Fammi un esempio con la spesa', "Ora un po' più difficile"], 1)], "Poi chiedimi un esempio della vita di tutti i giorni, oppure di salire di un livello, quando sei pronto."),
  ([('label', 'Fatti interrogare'), ('rows', [('Chi paga più interessi?', ''), ('Perché?', ''), ('Cosa succede se lo spread sale?', '')])], "E alla fine fatti interrogare con tre domande. Se sbagli, te lo rispiego in un altro modo."),
  ([('label', 'Da sapere'), ('body', 'Per salute, soldi e leggi: prima capisci con me, poi decidi con un esperto.'), ('stamp', 'Chiedi a un esperto')], "Ricorda, semplice non vuol dire sicuro. Per salute, soldi e leggi, prima capisci con me, poi decidi con un esperto."),
 ]),
 15: dict(SET=('colosso', 'torso'), POSA='banco', X=650, sc=[
  ([('title2', 'Ti fidi', 'e scrivi tutto?'), ('img', hook(15), 190)], "Ti fidi e scrivi tutto? Parlare con me è comodo, ma alcune cose è meglio non scriverle mai."),
  ([('label', 'Mai in chat'), ('rows', [('Password e codici segreti', 'no'), ('Numeri di carte e conti', 'no'), ('Dati di altre persone', 'no'), ('Segreti di lavoro', 'no')])], "Password, codici, numeri di carte e conti, dati di altre persone e segreti di lavoro. Nessun servizio serio te li chiede in chat."),
  ([('label', 'Foto di un contratto'), ('img', DOC, 240)], "Devi mandarmi un documento? Prima copri nome e numeri. Bastano due righe nere, e ti aiuto lo stesso."),
  ([('label', 'Meglio così'), ('typed', 'Un collega mi interrompe sempre in riunione. Come gliene parlo?')], "Per un consiglio su un collega, non mi serve il suo nome. Racconta la situazione e basta."),
  ([('label', "La regola d'oro"), ('body', 'Lo scriveresti su una cartolina? Se no, toglilo o cambialo.'), ('stamp', 'Togli, poi chiedi')], "La regola d'oro, prima di inviare chiediti se lo scriveresti su una cartolina. Se no, toglilo o cambialo."),
 ]),
 17: dict(SET=('colosso', 'braccio'), POSA='regge', X=580, sc=[
  ([('title2', 'Il curriculum', 'ti blocca?'), ('img', hook(17), 190)], "Il curriculum ti blocca? Foglio bianco e mille dubbi. Tu racconti, io do la forma."),
  ([('label', 'Richiesta a Edwin'), ('typed', 'Ho lavorato 8 anni in un magazzino, gestivo le consegne e 3 colleghi. Mi candido come responsabile.')], "Raccontami cosa hai fatto, anche in disordine, e che lavoro cerchi. Scrivi come parli."),
  ([('label', 'I tuoi punti forti', 'esempio inventato'), ('rows', [('Esperienza nel settore', '8 anni'), ('Gestione di un gruppo', '3 persone'), ('Organizzazione consegne', 'ogni giorno')])], "Io trovo i tuoi punti forti. Spesso le cose che dai per scontate sono proprio quelle che contano."),
  ([('label', 'Chiedimi ancora'), ('body', 'Andiamo avanti?'), ('buttons', ["Adattalo all'annuncio", 'Scrivi la lettera'], 0)], "Incolla l'annuncio e adatto il curriculum a quel lavoro. Poi posso scriverti anche la lettera di presentazione."),
  ([('label', 'Da sapere'), ('body', 'Niente esperienze o titoli inventati: al colloquio ti chiederanno tutto. Date e nomi controllali tu.'), ('stamp', 'Deve essere vero')], "Il curriculum deve essere vero, al colloquio ti chiederanno tutto. Io ti aiuto a raccontare bene la verità."),
 ]),
 18: dict(SET=('colosso', 'braccio'), POSA='indica', X=480, sc=[
  ([('title2', 'A fine mese i soldi', 'spariscono?'), ('img', hook(18), 190)], "A fine mese i soldi spariscono e non sai dove vanno? Mettiamo un po' d'ordine."),
  ([('label', 'Richiesta a Edwin'), ('typed', 'Entrano 1.800 euro. Affitto 650, spesa 400, bollette 150, auto 200, altro 250.')], "Scrivimi entrate e spese, anche a memoria e in disordine."),
  ([('label', 'Il tuo mese', 'esempio inventato'), ('rows', [('Affitto', '650 €'), ('Spesa', '400 €'), ('Altro', '250 €'), ('Auto', '200 €'), ('Bollette', '150 €'), ('Restano', '150 €')])], "Te le metto in ordine, dalla più pesante alla più leggera, con i totali. E vedi subito quanto resta."),
  ([('label', 'Dove vanno i soldi'), ('img', bars([650, 400, 250, 200, 150], ['Affitto', 'Spesa', 'Altro', 'Auto', 'Bollette'], 0), 240)], "Con un grafico capisci al volo cosa pesa di più. Vale più di cento numeri."),
  ([('label', 'Chiedimi ancora'), ('body', 'E adesso?'), ('buttons', ['5 idee per risparmiare', 'Foglio da scaricare'], 0)], "Poi chiedimi idee concrete per risparmiare, pensate per le tue spese. Idee pratiche, niente prediche."),
  ([('label', 'Da sapere'), ('body', 'Ricontrolla sempre i totali. Per prestiti, investimenti e tasse parla con un consulente.'), ('stamp', 'Ricontrolla')], "Ricontrolla sempre i totali. Per prestiti, investimenti e tasse, parla con un consulente."),
 ]),
 20: dict(SET=('colosso', 'testa'), POSA='banco', X=640, sc=[
  ([('title2', 'Ogni volta ripeti', 'le stesse cose?'), ('img', hook(20), 190)], "Ogni volta ripeti le stesse cose? Dammi del tu, scrivi semplice. Puoi dirmele una volta sola."),
  ([('label', 'Impostazioni · Preferenze'), ('typed', 'Dammi del tu e scrivi semplice. Frasi brevi, niente paroloni. Lavoro in un negozio.')], "Nelle impostazioni dell'app c'è uno spazio per le tue preferenze. Scrivi come vuoi le risposte e qualcosa di te."),
  ([('label', 'Da oggi'), ('rows', [('Ti do del tu', ''), ('Frasi brevi', ''), ('Niente paroloni', ''), ('Esempi dal tuo lavoro', '')])], "Da quel momento, ogni nuova conversazione parte già nella direzione giusta."),
  ([('label', 'Progetto «Casa»'), ('rows', [('Bollette', ''), ('Condominio', ''), ('Lavori', '')])], "Per un argomento che torna spesso, crea un progetto con le sue istruzioni e i suoi documenti. È come un cassetto in ordine."),
  ([('label', 'Da sapere'), ('body', 'Nelle preferenze scrivi come vuoi le risposte, mai password o informazioni private.'), ('stamp', 'Niente dati delicati')], "Le istruzioni si cambiano in un attimo. Solo una cosa, mai password o informazioni private."),
 ]),
 21: dict(SET=('colosso', 'testa'), POSA='regge', X=520, sc=[
  ([('title2', "Ti serve un'informazione", 'aggiornata?'), ('img', hook(21), 190)], "Ti serve un'informazione aggiornata? Quello che so può essere vecchio, ma posso cercare per te."),
  ([('label', 'Richiesta a Edwin'), ('typed', 'Cerca sul web gli orari del museo Egizio di Torino per sabato e dammi i link.')], "Chiedimi di cercare, chiaramente. La parola magica è cerca."),
  ([('label', 'Risultato', 'esempio inventato'), ('rows', [('Apertura', '9:00'), ('Chiusura', '18:30'), ('Fonte', 'sito ufficiale')])], "Ti rispondo e ti dico dove l'ho letto. Meglio se è un sito ufficiale."),
  ([('label', 'Chiedimi ancora'), ('body', 'Vuoi esserne sicuro?'), ('buttons', ['Apri il link', 'Confronta tre siti'], 0)], "Apri il link e controlla che dica davvero quello che ti ho detto. Oppure chiedimi di confrontare più siti."),
  ([('label', 'Da sapere'), ('body', 'Anche il web sbaglia: per le cose importanti telefona o controlla di persona.'), ('stamp', 'Controlla la fonte')], "Anche il uèb sbaglia. Per le cose importanti, telefona o controlla di persona."),
 ]),
 23: dict(SET=('gru', ''), POSA='indica', X=640, sc=[
  ([('title2', 'Un foglio pieno', 'di numeri?'), ('img', hook(23), 190)], "Un foglio pieno di numeri? Spese, presenze, vendite. Allegamelo e ti dico cosa c'è dentro."),
  ([('label', 'File allegato'), ('img', XLS, 220)], "Trascina il fàil nella ciàt, o usa la graffetta."),
  ([('label', 'Richiesta a Edwin'), ('typed', 'In quale mese abbiamo speso di più? E per cosa?')], "Poi fammi una domanda chiara. Una alla volta è più facile."),
  ([('label', 'Risposta', 'esempio inventato'), ('rows', [('Mese più caro', 'dicembre'), ('Voce più alta', 'regali'), ('Media al mese', '1.420 €')])], "Leggo le colonne e ti rispondo in parole semplici."),
  ([('label', 'Spese mese per mese'), ('img', bars([1300, 1250, 1380, 1290, 1350, 1500, 1620, 1400, 1310, 1360, 1420, 1980], list('GFMAMGLASOND'), 11), 240)], "E se vuoi, ti preparo un grafico. Vedere i numeri aiuta a capirli."),
  ([('label', 'Prima di allegare'), ('body', 'Togli nomi, codici fiscali e dati di altre persone. I totali controllali sul file originale.'), ('stamp', 'Dati coperti')], "Prima di allegare, togli nomi e dati personali. E controlla i totali sul fàil originale."),
 ]),
 24: dict(SET=('gru', ''), POSA='regge', X=520, sc=[
  ([('title2', 'Scrivere', 'ti stanca?'), ('img', hook(24), 190)], "Scrivere ti stanca? Puoi parlarmi a voce, come in una telefonata. Comodo mentre cucini o cammini."),
  ([('label', "Nell'app"), ('rows', [('Tocca il tasto della voce', ''), ('Parla normale', ''), ('Interrompimi quando vuoi', '')])], "Nell'app tocca il tasto della modalità vocale e parla normale, come con una persona."),
  ([('label', 'Tu, a voce'), ('body', '«Mi aiuti con la lista della spesa per una cena di sei persone? Uno è vegetariano.»')], "Ad esempio, mi aiuti con la lista della spesa per sei persone? E se uno è vegetariano? Domande a catena, senza scrivere niente."),
  ([('label', 'La lista', 'esempio inventato'), ('rows', [('Pasta', '1 kg'), ('Pomodori', '2 kg'), ('Formaggio', '300 g'), ('Verdure grigliate', 'per tutti')])], "Alla fine la conversazione resta scritta nella ciàt. La voce passa, l'elenco resta."),
  ([('label', 'Allenati'), ('body', '«Facciamo finta di essere al bar a Londra. Correggimi se sbaglio.»'), ('stamp', 'Occhio a dove parli')], "È perfetto anche per allenarti con le lingue. Solo, nei luoghi pubblici, evita di dire ad alta voce informazioni personali."),
 ]),
 26: dict(SET=('dirigibile', ''), POSA='regge', X=560, sc=[
  ([('title2', 'Vuoi imparare', 'una lingua?'), ('img', hook(26), 190)], "Vuoi imparare una lingua? Posso farti da insegnante paziente, a qualsiasi ora. E sbagliare con me non costa niente."),
  ([('label', 'Richiesta a Edwin'), ('typed', 'Voglio imparare lo spagnolo. Parto da zero e ho 15 minuti al giorno.')], "Dimmi da dove parti e quanto tempo hai."),
  ([('label', 'Il tuo piano', 'esempio inventato'), ('rows', [('Lunedì', 'saluti'), ('Martedì', 'numeri'), ('Mercoledì', 'al ristorante'), ('Giovedì', 'ripasso')])], "Ti preparo lezioni su misura, un pezzetto al giorno."),
  ([('label', 'Al ristorante'), ('typed', 'Edwin: ¿Qué desea tomar?\nTu: Un café, por favor.')], "Poi facciamo conversazione. Siamo al ristorante e io faccio il cameriere, anche quello scortese."),
  ([('label', 'Chiedimi ancora'), ('body', 'Come è andata?'), ('buttons', ['Correggimi in italiano', 'Ripassiamo 10 parole'], 0)], "Fatti correggere e chiedimi perché. Un errore spiegato non si ripete."),
  ([('label', 'Da sapere'), ('body', 'Io sono una palestra: quando puoi, parla con chi la lingua la usa ogni giorno.'), ('stamp', 'Allenati anche fuori')], "Ricorda, io sono una palestra. Quando puoi, parla con chi la lingua la usa ogni giorno."),
 ]),
 27: dict(SET=('dirigibile', ''), POSA='saluta', X=540, sc=[
  ([('title2', 'Ventisette congegni', 'dopo'), ('img', hook(27), 190)], "Ventisette congegni dopo, il dirigibile è pronto a partire. Prima, le cinque regole d'oro."),
  ([('label', "Le 5 regole d'oro"), ('rows', [('Chiedi chiaro', ''), ('Correggi senza paura', ''), ('Proteggi i tuoi dati', ''), ('Controlla', ''), ("L'ultima parola è tua", '')])], "Chiedi chiaro, correggi senza paura, proteggi i tuoi dati, controlla, e ricorda che l'ultima parola è tua."),
  ([('label', 'Chiedi chiaro'), ('typed', 'Scrivimi una mail gentile ma ferma al padrone di casa, massimo 5 righe.')], "Chi sei, cosa vuoi e come lo vuoi. E se la prima risposta non va, è solo una bozza."),
  ([('label', 'Controlla'), ('body', 'Numeri, date e fonti: anche gli automi sbagliano.'), ('stamp', 'Controlla')], "Numeri, date e fonti, controllali sempre. Anche gli autòmi sbagliano."),
  ([('label', "L'ultima parola"), ('body', 'Io ti aiuto a capire e a fare prima. Le decisioni importanti restano tue.'), ('stamp', 'Il capo sei tu')], "Io ti aiuto a capire e a fare prima, ma le decisioni restano tue. Io sono l'assistente, il capo sei tu."),
 ], cta=([('cta', 'LA STAGIONE 2', 'È IN VIAGGIO')], "La stagione due è in viaggio. Seguimi, ci vediamo in volo.")),
}

for n, d in S.items():
    ic, tit = icon(n)
    dietro, davanti = P[n]
    out = [f'NUM = {n}', f'TITOLO = {tit!r}', f'SET = {d["SET"]!r}', f'POSA = {d["POSA"]!r}', f'EDWIN_X = {d["X"]}',
           f'DIETRO = {dietro!r}', f'DAVANTI = {davanti!r}', 'SCENE = [']
    for p, v in d['sc']:
        assert '!' not in v and '...' not in v, v
        out.append(f' dict(panel={p!r}, voce={v!r}),')
    cp, cv = d.get('cta', ([('cta',)], CTA))
    fin = '' if d['POSA'] == 'regge' else ", posa='saluta'"
    out.append(f" dict(panel={cp!r}, voce={cv!r}{fin}),")
    out.append(']')
    open(f'storie/s{n}.py', 'w').write('\n'.join(out) + '\n')
print('ok', sorted(S))
