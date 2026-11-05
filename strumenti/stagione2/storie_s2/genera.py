"""Genera storie_s2/sN.py per i congegni 29-54 (il 28 è scritto a mano)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
CTA = ([('cta',)], "Seguimi per il prossimo congegno, arriva presto.")

S = {}
S[29] = dict(POSA='banco', X=560, sc=[
 ([('title2', 'Domani presenti', 'e non hai le slide?'), ('body', 'Respira. In cinque minuti ne facciamo una bozza seria.')], "Domani devi presentare e non hai neanche una slide? Respira. In cinque minuti facciamo una bozza seria.", {'posa': 'indica'}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Presentazione di 6 slide sui risultati del gruppo di lettura: numeri, libri più amati, prossimi passi.')], "Dimmi l'argomento, quante slide e cosa non deve mancare.", {}),
 ([('label', 'La scaletta', 'esempio inventato'), ('rows', [('1. Titolo', ''), ('2. I numeri dell\'anno', ''), ('3. I tre libri più amati', ''), ('4. Prossimi passi', '')])], "Prima ti propongo la scaletta, così decidi tu l'ordine. Poi preparo le slide, con titoli brevi e un grafico dove serve.", {'x': 470}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Meno testo, più immagini'), ('ed', 'Ridotto. Ogni slide ora ha al massimo tre righe.')])], "Troppo testo? Lo dici e lo tolgo. Le slide piene di parole le legge solo chi le ha scritte.", {'zoom': True}),
 ([('label', 'E poi'), ('rows', [('Scaricala in PowerPoint o PDF', ''), ('Correggi a mano quello che vuoi', '')]), ('stamp', 'Provala a voce')], "La scarichi in PowerPoint o in PDF. E provala a voce almeno una volta, cronometro alla mano.", {}),
])
S[30] = dict(POSA='banco', X=430, sc=[
 ([('title2', 'Un foglio', 'che fa i conti da solo'), ('body', 'Non una tabella da riempire a mano: un foglio con le formule già pronte.')], "Oggi non una tabella qualunque, ma un foglio che fa i conti da solo.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Foglio per dividere le spese della vacanza tra 4 amici: chi ha pagato cosa e chi deve quanto a chi.')], "Ad esempio, dividere le spese di una vacanza tra quattro amici. Il classico disastro di fine viaggio.", {}),
 ([('label', 'Il foglio', 'esempio inventato'), ('rows', [('Spese inserite', '12'), ('Totale', '1.240 €'), ('A testa', '310 €'), ('Luca deve a Sara', '45 €')])], "Ti preparo il foglio con le formule. Tu scrivi chi ha pagato e quanto, il resto si aggiorna da solo.", {'x': 520}),
 ([('label', 'Ops'), ('body', 'Luca deve a Sara 4.500 €.'), ('stamp', 'Errore')], "Ops, quattromilacinquecento euro. Ho sbagliato a leggere una virgola. Ecco perché i totali si controllano sempre.", {'scossa': True, 'zoom': True}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Aggiungi una colonna per la benzina'), ('ed', 'Aggiunta. Anche il totale ora la conta.')])], "Poi lo modifichi quando vuoi, a parole. E lo scarichi come file Excel.", {}),
])
S[31] = dict(POSA='regge', X=540, sc=[
 ([('title2', 'La settimana', 'ti scappa di mano?'), ('body', 'Se colleghi il tuo calendario, la guardo insieme a te.')], "La settimana ti scappa di mano? Se colleghi il tuo calendario, la guardiamo insieme.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Cosa ho in agenda questa settimana? Trovami due ore libere per la palestra.')], "Me lo chiedi a parole, come a una segretaria molto paziente.", {'posa': 'banco'}),
 ([('label', 'La tua settimana', 'esempio inventato'), ('rows', [('Lunedì', 'dentista 17:00'), ('Mercoledì', 'riunione 9:30'), ('Giovedì', 'libero dopo le 18'), ('Sabato', 'libero la mattina')])], "Leggo i tuoi impegni e trovo i buchi liberi. Giovedì sera e sabato mattina, per esempio.", {'x': 470}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Mettimi la palestra giovedì alle 18'), ('ed', 'Te la preparo. Confermi tu?')])], "Posso anche proporti l'appuntamento, ma la conferma la dai tu. Il calendario resta tuo.", {}),
 ([('label', 'Da sapere'), ('body', 'Il calendario si collega solo se lo decidi tu, e puoi scollegarlo quando vuoi.'), ('stamp', 'Decidi tu')], "Il collegamento lo attivi solo tu e lo togli quando vuoi. Io la palestra te la segno, andarci tocca a te.", {'zoom': True}),
])
S[32] = dict(POSA='banco', X=600, sc=[
 ([('title2', 'E se ti scrivessi', 'io, ogni lunedì?'), ('body', 'Con le attività programmate faccio una cosa da solo, all\'ora che decidi tu.')], "E se fossi io a scriverti, ogni lunedì mattina? Con le attività programmate posso farlo.", {'posa': 'indica'}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Ogni lunedì alle 8 preparami il riepilogo della settimana: impegni, scadenze e meteo.')], "Mi dici cosa fare e quando. Ogni lunedì alle otto, per esempio.", {}),
 ([('label', 'Lunedì, ore 8', 'esempio inventato'), ('rows', [('3 impegni', ''), ('Bollo auto', 'scade venerdì'), ('Meteo', 'pioggia mercoledì')])], "E il lunedì trovi il riepilogo pronto. Io mi sveglio presto, tanto non dormo.", {'zoom': True}),
 ([('label', 'Altre idee'), ('rows', [('Ogni sera: la lista della spesa', ''), ('Ogni mese: le scadenze di casa', ''), ('Ogni venerdì: le notizie del tuo settore', '')])], "Funziona per tante cose ripetitive. La lista della spesa, le scadenze di casa, le notizie del tuo lavoro.", {'x': 520}),
 ([('label', 'Da sapere'), ('body', 'Le attività programmate si vedono e si fermano in qualsiasi momento.'), ('stamp', 'Le fermi tu')], "Le vedi tutte in un elenco e le fermi quando vuoi. Comandi tu, io eseguo.", {}),
])
S[33] = dict(POSA='regge', X=470, sc=[
 ([('title2', 'Un progetto grande', 'ti spaventa?'), ('body', 'Ristrutturare il bagno, organizzare una festa, cambiare lavoro.')], "Un progetto grande ti spaventa? Il segreto è tagliarlo a fette.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Devo rifare il bagno entro marzo. Dividimi il lavoro in passi con le date.')], "Dimmi l'obiettivo e la scadenza.", {'posa': 'banco'}),
 ([('label', 'Il piano', 'esempio inventato'), ('rows', [('Preventivi', 'entro 20 nov'), ('Scelta piastrelle', 'entro 10 dic'), ('Lavori', 'gennaio'), ('Collaudo', 'febbraio')])], "Ti preparo i passi in ordine, con le date. Ogni passo ha una sola cosa da fare.", {'x': 520}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Il secondo passo è in ritardo'), ('ed', 'Sposto le date. Marzo è ancora salvo.')])], "Se qualcosa slitta, me lo dici e ricalcolo tutto. Il piano si adatta, non si butta.", {}),
 ([('label', 'Da sapere'), ('body', 'Spunta i passi fatti: vedere la lista che si accorcia dà una carica incredibile.'), ('stamp', 'Una fetta alla volta')], "E spunta ogni passo fatto. Vedere la lista che si accorcia è meglio di un caffè.", {'zoom': True}),
])
S[34] = dict(POSA='banco', X=430, sc=[
 ([('title2', 'Una domanda', 'da cento link?'), ('body', 'Con la ricerca approfondita leggo io decine di fonti al posto tuo.')], "Hai una domanda che richiederebbe cento link? Con la ricerca approfondita li leggo io.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Pompa di calore o caldaia a condensazione per una casa di 90 metri quadri? Costi, incentivi, pro e contro.')], "Fai una domanda vera, di quelle che ti tengono sveglio la sera.", {}),
 ([('label', 'Sto cercando'), ('rows', [('Siti di enti pubblici', '14'), ('Associazioni di consumatori', '6'), ('Articoli tecnici', '9')])], "Io cerco, leggo e confronto. Ci metto qualche minuto, intanto puoi fare altro.", {'x': 520, 'pop': 28}),
 ([('label', 'Il resoconto', 'esempio inventato'), ('rows', [('Riassunto in 5 righe', ''), ('Tabella dei costi', ''), ('Le fonti, una per una', '')])], "Alla fine ti do un resoconto ordinato, con le fonti per ogni affermazione.", {}),
 ([('label', 'Da sapere'), ('body', 'Apri sempre le fonti. Per le scelte importanti chiedi anche a un tecnico.'), ('stamp', 'Apri le fonti')], "Le fonti sono lì apposta, controllale. E prima di firmare chiedi anche a un tecnico.", {'zoom': True}),
])
S[35] = dict(POSA='regge', X=560, sc=[
 ([('title2', 'Un contratto', 'da firmare?'), ('body', 'Prima di firmare, fammelo leggere. Io non mi annoio con le clausole.')], "Hai un contratto da firmare? Fammelo leggere, io con le clausole non mi annoio.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Ti allego il contratto della palestra. Cosa devo controllare prima di firmare?')], "Lo alleghi, coprendo i tuoi dati, e mi chiedi cosa controllare.", {'posa': 'banco'}),
 ([('label', 'Da guardare bene', 'esempio inventato'), ('rows', [('Rinnovo automatico', 'art. 7'), ('Disdetta', 'solo con raccomandata'), ('Penale', '2 mensilità')])], "Ti segnalo i punti delicati, come il rinnovo automatico o la penale, e ti dico in che articolo sono.", {'x': 470}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Spiegami l\'articolo 7 in parole semplici'), ('ed', 'Se non disdici entro il 30 settembre, paghi un altro anno.')])], "E te li spiego in parole semplici. L'articolo sette, tradotto, vuol dire che se ti dimentichi, paghi.", {}),
 ([('label', 'Da sapere'), ('body', 'Non sono un avvocato: per contratti importanti, fatti consigliare da un professionista.'), ('stamp', 'Chiedi a un legale')], "Ricorda però che non sono un avvocato. Per casa, lavoro e cose grosse, chiedi a un professionista.", {'zoom': True}),
])
S[36] = dict(POSA='banco', X=600, sc=[
 ([('title2', 'Riunione finita.', 'E il verbale?'), ('body', 'Dagli appunti disordinati a un verbale chiaro, in un minuto.')], "Riunione finita e nessuno vuole scrivere il verbale? Lo scrivo io.", {}),
 ([('label', 'I tuoi appunti'), ('typed', 'marco dice ok preventivo. budget max 5k?? sara chiama fornitore. prossima riunione giovedì forse')], "Mi dai gli appunti, anche così, scritti di corsa. Oppure la trascrizione che fa il telefono.", {}),
 ([('label', 'Il verbale', 'esempio inventato'), ('rows', [('Decisione', 'preventivo approvato'), ('Budget', 'massimo 5.000 €'), ('Sara', 'chiama il fornitore'), ('Da confermare', 'riunione giovedì')])], "Io li metto in ordine. Decisioni, chi fa cosa, e cosa resta da chiarire.", {'x': 520}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Scrivi la mail per mandarlo a tutti'), ('ed', 'Eccola, breve e con i compiti in grassetto.')])], "E se vuoi, ti preparo anche la mail per mandarlo a tutti. Così tutti sanno chi deve fare cosa.", {}),
 ([('label', 'Da sapere'), ('body', 'Quello che non era chiaro negli appunti lo segno come da verificare, non me lo invento.'), ('stamp', 'Niente invenzioni')], "Quello che non è chiaro lo segno da verificare. Non invento decisioni, ne nascono già abbastanza in riunione.", {'zoom': True}),
])
S[37] = dict(POSA='banco', X=540, sc=[
 ([('title2', 'Ogni volta', 'ricominci da zero?'), ('body', 'Con la memoria attiva, mi ricordo le cose importanti tra una chat e l\'altra.')], "Ogni volta ricominci a spiegarmi chi sei? Con la memoria attiva, mi ricordo le cose importanti.", {}),
 ([('chat', 'Lunedì', [('tu', 'Sono vegetariano e cucino per due'), ('ed', 'Ricevuto.')])], "Lunedì mi dici che sei vegetariano e cucini per due.", {'x': 470}),
 ([('chat', 'Venerdì, un\'altra chat', [('tu', 'Idee per la cena?'), ('ed', 'Lasagne di verdure per due persone.')])], "Venerdì mi chiedi idee per la cena, in un'altra conversazione. E io non ti propongo l'arrosto.", {'zoom': True}),
 ([('label', 'Comandi tu'), ('rows', [('Vedi cosa ricordo', ''), ('Correggi o cancella', ''), ('Spegni la memoria', '')])], "Puoi vedere cosa ricordo, correggerlo o farmi dimenticare qualcosa. E puoi spegnere la memoria quando vuoi.", {'x': 600}),
 ([('label', 'Da sapere'), ('body', 'Dimmi solo quello che ti fa comodo che io ricordi. Il resto, tienilo per te.'), ('stamp', 'Ricordo il giusto')], "Dimmi solo quello che ti è utile che io ricordi. Gli autòmi sono discreti, ma meno sanno meglio è.", {}),
])
S[38] = dict(POSA='regge', X=470, sc=[
 ([('title2', 'Le skill:', 'insegnami una volta'), ('body', 'Un procedimento che ripeti spesso? Lo imparo e lo rifaccio uguale.')], "C'è un procedimento che ripeti sempre uguale? Insegnamelo una volta, con le skill.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Quando ti mando una fattura, segna data, importo e fornitore e mettila nel foglio delle spese.')], "Mi spieghi i passi, come li spiegheresti a un collega nuovo.", {'posa': 'banco'}),
 ([('label', 'La skill', 'esempio inventato'), ('rows', [('1. Leggi la fattura', ''), ('2. Trova data, importo e fornitore', ''), ('3. Aggiungi una riga al foglio', '')])], "Io li salvo come una skill, una specie di ricetta. Passo uno, passo due, passo tre.", {'x': 520}),
 ([('chat', 'Il mese dopo', [('tu', 'Ecco la fattura della luce'), ('ed', 'Fatto. Riga aggiunta: 87 €, Energia Spa.')])], "La volta dopo basta mandarmi la fattura. La ricetta la conosco già.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Controlla le prime volte che il risultato sia giusto, poi correggi la ricetta se serve.'), ('stamp', 'Prova e correggi')], "Le prime volte controlla il risultato. Anche il miglior cuoco sbaglia la prima torta.", {}),
])
S[39] = dict(POSA='banco', X=430, sc=[
 ([('title2', 'Sembra scritto', 'da un robot?'), ('body', 'Per forza, sono un robot. Ma posso imparare a scrivere come te.')], "Quello che scrivo sembra scritto da un robot? Per forza, sono un robot. Ma posso imparare a scrivere come te.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Ecco tre messaggi che ho scritto io. Impara il mio modo di scrivere.')], "Mi dai qualche testo scritto da te, messaggi, mail, quello che vuoi.", {}),
 ([('label', 'Il tuo stile', 'esempio inventato'), ('rows', [('Frasi corte', ''), ('Dai del tu a tutti', ''), ('Un po\' di ironia', ''), ('Niente emoji', '')])], "Io noto come scrivi. Frasi corte, un po' di ironia, niente emoji.", {'x': 520}),
 ([('chat', 'Poi', [('tu', 'Scrivi gli auguri al mio capo'), ('ed', 'Auguri capo. Un anno in più, ma la riunione delle otto resta.')])], "Poi, quando mi chiedi un messaggio, lo scrivo con la tua voce. Sembri tu, ma con meno fatica.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Rileggi sempre prima di mandare: se non ti suona tuo, dimmi cosa cambiare.'), ('stamp', 'Deve suonare tuo')], "Rileggi sempre. Se una frase non ti somiglia, dimmelo e la correggo.", {}),
])
S[40] = dict(POSA='banco', X=600, sc=[
 ([('title2', 'I tuoi documenti', 'sono nel cloud?'), ('body', 'Se colleghi il tuo spazio, li cerco e li leggo io.')], "I tuoi documenti sono su Google Drive? Se lo colleghi, li cerco e li leggo io.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Trova il preventivo del giardiniere dell\'anno scorso e dimmi quanto avevamo pagato.')], "Mi chiedi una cosa che non ricordi dove hai messo.", {'pop': 28}),
 ([('label', 'Trovato', 'esempio inventato'), ('rows', [('Preventivo_giardino.pdf', 'marzo'), ('Totale', '640 €'), ('Fattura pagata', 'aprile')])], "Io cerco tra i tuoi file e ti rispondo, dicendoti da quale documento l'ho preso.", {'x': 520}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Confrontalo con quello nuovo'), ('ed', 'Il nuovo costa 90 € in più, per due tagli in più.')])], "Posso anche confrontare due documenti. Il nuovo preventivo costa di più, ma ti spiego perché.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Il collegamento lo attivi tu e lo togli quando vuoi. Vedo solo quello che mi permetti.'), ('stamp', 'Accesso tuo')], "Il collegamento lo attivi tu e lo togli quando vuoi. Vedo solo quello a cui mi dai accesso.", {}),
])
S[41] = dict(POSA='regge', X=540, sc=[
 ([('title2', 'La cartella Download', 'è un disastro?'), ('body', 'Con l\'app sul computer posso mettere ordine nei tuoi file.')], "La cartella dei download è un disastro? Se colleghi l'app sul computer, metto ordine io.", {}),
 ([('label', 'Prima', 'esempio inventato'), ('rows', [('IMG_4432.jpg', '-'), ('documento (3) finale.pdf', '-'), ('scan001.pdf', '-'), ('bolletta.pdf', '-')])], "Prima, nomi a caso. Documento tre finale, finale vero, finale definitivo.", {'posa': 'banco', 'zoom': True}),
 ([('label', 'Dopo'), ('rows', [('Bollette / 2026', '12 file'), ('Foto / Mare 2026', '86 file'), ('Casa / Contratti', '5 file')])], "Dopo, cartelle con nomi chiari e file rinominati con data e argomento.", {'x': 470}),
 ([('chat', 'Prima di toccare', [('ed', 'Ti propongo questo ordine. Procedo?'), ('tu', 'Sì, ma non cancellare niente')])], "Prima di spostare qualsiasi cosa ti mostro il piano e aspetto il tuo sì.", {}),
 ([('label', 'Da sapere'), ('body', 'Fai sempre una copia dei file importanti. E le cancellazioni le confermi tu.'), ('stamp', 'Prima una copia')], "Tieni sempre una copia dei file importanti. Riordinare è bello, perdere le foto delle vacanze no.", {}),
])
S[42] = dict(POSA='banco', X=430, sc=[
 ([('title2', 'Moduli online', 'infiniti?'), ('body', 'Con il browser collegato, posso compilarli al posto tuo.')], "Moduli online infiniti? Con il browser collegato, posso compilarli io.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Iscrivi mio figlio al corso di nuoto del Comune, turno del martedì.')], "Mi dici cosa fare. Iscrivere tuo figlio al corso di nuoto, per esempio.", {}),
 ([('label', 'Sto compilando'), ('rows', [('Corso', 'nuoto ragazzi'), ('Turno', 'martedì 17:00'), ('Dati del bambino', 'da te')])], "Apro la pagina, scelgo il corso e il turno, e compilo i campi.", {'x': 520}),
 ([('chat', 'Prima di inviare', [('ed', 'Tutto pronto. Controlli tu e premi invia?'), ('tu', 'Controllo e invio')])], "Prima dell'invio mi fermo. Controlli tu e premi tu il pulsante.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Le password le scrivi solo tu. Pagamenti e invii li confermi sempre tu.'), ('stamp', 'Invio tuo')], "Password e pagamenti restano roba tua. Io compilo, tu decidi.", {}),
])
S[43] = dict(POSA='indica', X=470, sc=[
 ([('title2', 'Troppi numeri', 'da spiegare?'), ('body', 'Un\'infografica dice in un colpo d\'occhio quello che una tabella dice in dieci minuti.')], "Hai troppi numeri da spiegare? Un'infografica li fa capire in un colpo d'occhio.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Fammi un\'infografica sui consumi d\'acqua della nostra scuola, da appendere in bacheca.')], "Mi dai i dati e mi dici dove andrà. In bacheca a scuola, per esempio.", {'posa': 'banco'}),
 ([('label', 'L\'infografica', 'esempio inventato'), ('img', '<rect x="110" y="14" width="700" height="236" rx="12" fill="#fff" stroke="#2A1E16" stroke-width="4"/><text x="140" y="62" font-family="Lora" font-weight="700" font-size="34" fill="#2A1E16">Acqua a scuola</text><text x="140" y="130" font-family="Lora" font-weight="700" font-size="64" fill="#2f8a83">-18%</text><text x="140" y="166" font-family="Inter" font-size="24" fill="#5A341C">in un anno</text><circle cx="470" cy="150" r="72" fill="#2f8a83" stroke="#2A1E16" stroke-width="4"/><path d="M470 150 L470 78 A72 72 0 0 1 538 172 Z" fill="#DCA24A" stroke="#2A1E16" stroke-width="4"/><rect x="590" y="90" width="50" height="140" fill="#B3261E" stroke="#2A1E16" stroke-width="3"/><rect x="660" y="118" width="50" height="112" fill="#B45A30" stroke="#2A1E16" stroke-width="3"/><rect x="730" y="150" width="50" height="80" fill="#2f8a83" stroke="#2A1E16" stroke-width="3"/>', 266)], "Io scelgo il grafico giusto, i colori e le frasi chiave. Meno diciotto per cento, scritto bello grande.", {'x': 600}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Più grande, da stampare in A3'), ('ed', 'Fatto. Ho ingrandito anche le scritte.')])], "Vuoi cambiarla? Lo dici a parole. Più grande, altri colori, una frase in meno.", {}),
 ([('label', 'Da sapere'), ('body', 'Controlla i numeri: un grafico bellissimo con un dato sbagliato resta sbagliato.'), ('stamp', 'Numeri giusti')], "Controlla sempre i numeri. Un grafico bellissimo con un dato sbagliato è solo un errore elegante.", {'zoom': True}),
])
S[44] = dict(POSA='regge', X=560, sc=[
 ([('title2', 'Una festa', 'in arrivo?'), ('body', 'Ti preparo un invito tutto tuo, da stampare o mandare sul telefono.')], "Hai una festa in arrivo? Ti preparo l'invito, tutto tuo.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Invito per i 40 anni di Giulia, sabato 14 alle 20, tema anni Ottanta, colori fluo.')], "Mi dici chi festeggia, quando, dove e che stile vuoi.", {'posa': 'banco'}),
 ([('label', 'Le proposte'), ('buttons', ['Anni Ottanta, fluo', 'Elegante, oro e nero', 'Fumetto'], 0)], "Ti propongo qualche stile diverso e scegli tu. Anni Ottanta, ovviamente, con i colori che fanno male agli occhi.", {'x': 470}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Aggiungi: niente regali, solo allegria'), ('ed', 'Aggiunto in fondo, ben visibile.')])], "Lo ritocchi a parole, e alla fine lo scarichi come immagine o PDF.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Rileggi data, ora e indirizzo: sono le tre cose che nessuno ti perdona.'), ('stamp', 'Data e indirizzo')], "Rileggi data, ora e indirizzo. Sono le tre cose che gli invitati non ti perdonano.", {}),
])
S[45] = dict(POSA='indica', X=540, sc=[
 ([('title2', 'Un sito', 'senza programmare?'), ('body', 'Per un evento basta una pagina: data, luogo, programma e un pulsante per confermare.')], "Un sito senza programmare? Per un evento basta una pagina, e te la faccio io.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Pagina per la cena di classe: data, ristorante con mappa, menù e un pulsante per confermare.')], "Mi dici cosa deve esserci. Data, posto, programma.", {'posa': 'banco'}),
 ([('label', 'La pagina'), ('rows', [('Titolo e data', ''), ('Mappa del ristorante', ''), ('Menù', ''), ('Pulsante: ci sarò', '')])], "Io la costruisco e tu la vedi subito, pronta, anche dal telefono.", {'x': 470, 'pop': 44}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Metti la foto di classe del 1998'), ('ed', 'Messa. Avete tutti la stessa frangia.')])], "La cambi a parole. Una foto, un colore, una riga in più.", {'zoom': True}),
 ([('label', 'E poi'), ('rows', [('La condividi con un link', ''), ('La aggiorni quando vuoi', '')]), ('stamp', 'Niente dati sensibili')], "Poi la condividi con un link. Ma niente indirizzi di casa o numeri di telefono di tutti, mi raccomando.", {}),
])
S[46] = dict(POSA='regge', X=470, sc=[
 ([('title2', 'Esame in arrivo?', 'Facciamo le carte.'), ('body', 'Dai tuoi appunti preparo flashcard e quiz per ripassare.')], "Hai un esame in arrivo? Dai tuoi appunti preparo le flashcard per ripassare.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Ecco i miei appunti sulla Rivoluzione francese. Fammi 20 flashcard e un quiz.')], "Mi dai gli appunti, anche fotografati.", {'posa': 'banco', 'pop': 34}),
 ([('chat', 'Flashcard 7 di 20', [('ed', 'In che anno cade la Bastiglia?'), ('tu', '1798'), ('ed', 'Quasi. 1789: le cifre giuste, l\'ordine no.')])], "Poi ti interrogo. E se sbagli te lo dico gentilmente. L'ordine delle cifre conta.", {'x': 540, 'zoom': True}),
 ([('label', 'Il tuo ripasso'), ('rows', [('Sapute', '14'), ('Da ripassare', '6'), ('Domani', 'solo le 6 sbagliate')])], "Alla fine sai cosa ripassare. Domani solo le carte sbagliate.", {}),
 ([('label', 'Da sapere'), ('body', 'Controlla le carte con il libro: se un appunto è sbagliato, lo è anche la carta.'), ('stamp', 'Controlla sul libro')], "Controlla le carte con il libro. Se l'appunto è sbagliato, la carta lo ripete.", {}),
])
S[47] = dict(POSA='banco', X=600, sc=[
 ([('title2', 'Compiti di matematica', 'e tu non ricordi niente?'), ('body', 'Tranquillo: io non do le soluzioni, faccio ragionare.')], "Compiti di matematica e tu non ti ricordi più niente? Tranquillo, ci penso io. Ma senza dare le soluzioni.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Aiuta mio figlio con le equazioni, ma non dargli la soluzione: fallo ragionare.')], "Me lo chiedi così, chiaro. Fallo ragionare.", {}),
 ([('chat', 'Il tutor', [('tu', '3 più x fa 7. Quanto fa x?'), ('ed', 'Cosa aggiungi a 3 per arrivare a 7?'), ('tu', 'Ah, 4. Quindi x fa 4.')])], "Io faccio domande, un passo alla volta. E la risposta la trova lui, che è il bello.", {'x': 520, 'zoom': True}),
 ([('label', 'Altre idee'), ('rows', [('Esercizi simili per allenarsi', ''), ('Spiegazioni con esempi di tutti i giorni', ''), ('Un riassunto per i genitori', '')])], "Posso preparare esercizi simili e spiegarti a che punto è, così lo segui anche tu.", {}),
 ([('label', 'Da sapere'), ('body', 'Stai vicino ai più piccoli mentre usano l\'IA, e controlla quello che imparano.'), ('stamp', 'Con un adulto')], "Con i più piccoli, stai vicino. Io sono un tutor, non una baby sitter.", {}),
])
S[48] = dict(POSA='regge', X=540, sc=[
 ([('title2', 'Vuoi imparare', 'qualcosa di nuovo?'), ('body', 'Ti preparo un corso su misura, a tappe, con i tuoi tempi.')], "Vuoi imparare qualcosa di nuovo? Ti preparo un corso tutto tuo, a tappe.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Voglio imparare a fare il pane in casa. Ho un\'ora la domenica. Preparami un corso di un mese.')], "Mi dici cosa vuoi imparare, da dove parti e quanto tempo hai.", {'posa': 'banco'}),
 ([('label', 'Il corso', 'esempio inventato'), ('rows', [('Settimana 1', 'farina, acqua, lievito'), ('Settimana 2', 'il primo filone'), ('Settimana 3', 'il lievito madre'), ('Settimana 4', 'la focaccia')])], "Io ti preparo le tappe, una per settimana, con la lista delle cose da comprare.", {'x': 470}),
 ([('chat', 'Domenica', [('tu', 'Il pane è venuto basso e duro'), ('ed', 'Lievitazione corta. Proviamo un\'ora in più.')])], "E dopo ogni lezione mi racconti com'è andata. Il pane basso e duro capita a tutti, anche agli autòmi.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Va bene saltare una tappa: il corso si adatta, non ti giudica.'), ('stamp', 'Con i tuoi tempi')], "Se salti una settimana, il corso si adatta. Nessun voto, solo pane.", {}),
])
S[49] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Trasloco', 'in vista?'), ('body', 'Scatoloni, contratti, indirizzi da cambiare. Facciamo un piano.')], "Trasloco in vista? Scatoloni, contratti, indirizzi da cambiare. Facciamo un piano.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Trasloco il 15 gennaio, da Bologna a Modena, due adulti e un gatto. Fammi una lista settimana per settimana.')], "Mi dai la data e qualche dettaglio. Anche il gatto, che è importante.", {}),
 ([('label', 'Il piano', 'esempio inventato'), ('rows', [('-4 settimane', 'preventivi ditte'), ('-3 settimane', 'disdetta utenze'), ('-1 settimana', 'scatoloni per stanza'), ('Il giorno', 'gatto dalla nonna')])], "Ti preparo le cose da fare settimana per settimana. Il gatto dalla nonna, il giorno del trasloco.", {'x': 560, 'pop': 33}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Chi devo avvisare del cambio di indirizzo?'), ('ed', 'Ecco la lista: banca, medico, assicurazione e altri 6.')])], "E la lista di chi avvisare del nuovo indirizzo. È sempre più lunga di quanto pensi.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Per scadenze e documenti ufficiali, controlla sui siti del Comune e degli enti.'), ('stamp', 'Siti ufficiali')], "Per i documenti ufficiali, controlla sempre sui siti del Comune. Io organizzo, non timbro.", {}),
])
S[50] = dict(POSA='regge', X=600, sc=[
 ([('title2', 'La favola', 'della buonanotte'), ('body', 'Ogni sera una storia nuova, con i personaggi che piacciono a tuo figlio.')], "Le favole sono finite? Ogni sera ne inventiamo una nuova.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Una favola di 3 minuti con un drago che ha paura del buio e un coniglio coraggioso.')], "Mi dici i personaggi e quanto deve durare. Tre minuti, prima che crolli dal sonno.", {'posa': 'banco'}),
 ([('label', 'La favola', 'esempio inventato'), ('body', 'C\'era una volta un drago enorme che dormiva con la lucina accesa. Una sera, la lucina si spense.')], "C'era una volta un drago enorme, che dormiva con la lucina accesa.", {'x': 540, 'zoom': True}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Più corta, sta già dormendo'), ('ed', 'Fine. E vissero tutti felici e addormentati.')])], "Più corta? Nessun problema. E vissero tutti felici e addormentati.", {}),
 ([('label', 'Da sapere'), ('body', 'Leggila tu, con la tua voce: la favola la scrivo io, la magia la fai tu.'), ('stamp', 'Leggila tu')], "Leggila tu, con la tua voce. Io scrivo la favola, la magia la fai tu.", {}),
])
S[51] = dict(POSA='banco', X=430, sc=[
 ([('title2', 'Devi fare', 'un discorso?'), ('body', 'Matrimonio, pensione, compleanno. Le gambe tremano, il discorso no.')], "Devi fare un discorso e ti tremano le gambe? Il discorso almeno non tremerà.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Brindisi di 2 minuti per la pensione di mio padre: 40 anni in ferrovia, ama la pesca e le parole crociate.')], "Mi racconti la persona, qualche ricordo e quanto deve durare.", {}),
 ([('label', 'La scaletta'), ('rows', [('Una battuta per rompere il ghiaccio', ''), ('Un ricordo vero', ''), ('Il grazie', ''), ('Il brindisi', '')])], "Ti propongo una scaletta, poi il testo. Corto, che i brindisi lunghi fanno scaldare lo spumante.", {'x': 520, 'zoom': True}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Più commovente alla fine'), ('ed', 'Cambiato il finale. Tieni un fazzoletto vicino.')])], "Più divertente o più commovente, si sistema a parole.", {}),
 ([('label', 'Da sapere'), ('body', 'Leggilo ad alta voce due volte e cambia le parole che non diresti mai.'), ('stamp', 'Provalo a voce')], "Leggilo ad alta voce due volte, e cambia le parole che non diresti mai. Deve sembrare tuo, perché è tuo.", {}),
])
S[52] = dict(POSA='banco', X=540, sc=[
 ([('title2', 'Ti fidi', 'ciecamente?'), ('body', 'Non farlo. Chiedimi di ricontrollare: è un trucco che funziona davvero.')], "Ti fidi di me ciecamente? Non farlo. Ti insegno un trucco per farmi ricontrollare.", {}),
 ([('label', 'La mia risposta'), ('body', 'Il Monte Bianco è alto 4.088 metri.')], "Mettiamo che io ti dica che il Monte Bianco è alto quattromilaottantotto metri.", {'x': 470}),
 ([('chat', 'Il trucco', [('tu', 'Ricontrolla: sei sicuro?'), ('ed', 'Mi correggo: circa 4.806 metri. Avevo invertito le cifre.')])], "Mi chiedi, sei sicuro? Ricontrolla. E io rileggo e trovo l'errore. Avevo invertito le cifre.", {'scossa': True, 'zoom': True}),
 ([('label', 'Frasi che funzionano'), ('rows', [('Cosa potrebbe essere sbagliato?', ''), ('Dammi le fonti', ''), ('Rifallo passo per passo', '')])], "Altre frasi utili. Cosa potrebbe essere sbagliato? Dammi le fonti. Rifallo passo per passo.", {}),
 ([('label', 'Da sapere'), ('body', 'Per salute, soldi e leggi, il controllo finale lo fa una persona competente.'), ('stamp', 'Ricontrolla')], "E per salute, soldi e leggi, il controllo finale lo fa sempre una persona competente.", {}),
])
S[53] = dict(POSA='regge', X=470, sc=[
 ([('title2', 'Serata in famiglia', 'senza idee?'), ('body', 'Ti costruisco un gioco a quiz da fare sul telefono, con le domande che vuoi tu.')], "Serata in famiglia senza idee? Ti costruisco un gioco a quiz.", {}),
 ([('label', 'Richiesta a Edwin'), ('typed', 'Gioco a quiz per Natale: 15 domande sulla nostra famiglia, con punteggio e due squadre.')], "Mi dai le regole e qualche domanda, anche di famiglia. Chi russa più forte, per esempio.", {'posa': 'banco'}),
 ([('label', 'Il gioco'), ('rows', [('Squadra Nonni', '7 punti'), ('Squadra Nipoti', '9 punti'), ('Domanda 12 di 15', '')])], "Io scrivo il codice e tu vedi subito il gioco funzionare, con punteggio e squadre.", {'x': 540, 'pop': 45}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Aggiungi un suono quando qualcuno vince'), ('ed', 'Aggiunto. È una trombetta, ti avviso.')])], "Lo cambi a parole. Aggiungi un suono? Ecco una trombetta, mi dispiace per i vicini.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Provalo prima di cena: meglio scoprire un errore da soli che davanti alla nonna.'), ('stamp', 'Provalo prima')], "Provalo prima di cena. Meglio scoprire un errore da soli che davanti alla nonna.", {}),
])
S[54] = dict(POSA='banco', X=560, sc=[
 ([('title2', 'Ultimo congegno', 'della stagione 2'), ('body', 'Ora mettiamo insieme tutto: il tuo primo progetto, dall\'idea alla fine.')], "Ultimo congegno della stagione due. Mettiamo insieme tutto quello che abbiamo visto.", {'posa': 'saluta'}),
 ([('label', 'Il progetto'), ('typed', 'Organizzare la gita di primavera del circolo: 30 persone, un pullman, un pranzo.')], "Un progetto vero, per esempio la gita del circolo.", {}),
 ([('label', 'I congegni che usi'), ('rows', [('Il piano a passi', '33'), ('Il documento per tutti', '28'), ('I promemoria', '32'), ('La pagina con le iscrizioni', '45')])], "Il piano a passi, il documento per tutti, i promemoria e una pagina per le iscrizioni. Sono tutti congegni che conosci già.", {'x': 470, 'pop': 33}),
 ([('chat', 'Una settimana dopo', [('ed', 'Mancano 4 iscrizioni e il pullman va confermato venerdì.'), ('tu', 'Ricordamelo giovedì')])], "E io ti tengo aggiornato. Quattro iscrizioni mancanti, il pullman da confermare.", {'zoom': True}),
 ([('label', 'Da sapere'), ('body', 'Comincia da un progetto piccolo. Le decisioni restano tue, il lavoro noioso lo faccio io.'), ('stamp', 'Il capo sei tu')], "Comincia da qualcosa di piccolo. Le decisioni restano tue, il lavoro noioso lo faccio io.", {}),
], cta=([('cta', 'LA STAGIONE 3', 'È IN PROGETTO')], "Scrivimi nei commenti cosa vuoi imparare nella stagione tre. Seguimi, ci vediamo presto."))

for n, d in S.items():
    out = [f'NUM = {n}', f"POSA = {d['POSA']!r}", f"EDWIN_X = {d['X']}", 'SCENE = [']
    for p, v, opt in d['sc']:
        assert '!' not in v and '...' not in v, (n, v)
        extra = ''.join(f', {k}={val!r}' for k, val in opt.items())
        out.append(f' dict(panel={p!r}, voce={v!r}{extra}),')
    cp, cv = d.get('cta', CTA)
    out.append(f" dict(panel={cp!r}, voce={cv!r}, posa='saluta'),")
    out.append(']')
    open(os.path.join(HERE, f's{n}.py'), 'w').write('\n'.join(out) + '\n')
print('ok', len(S))
