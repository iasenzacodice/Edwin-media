"""Copioni della stagione 3 (congegni 56-81). Il 55 è scritto a mano (s55.py).
Ogni scena: pannello + voce (+ opzioni: posa, x, zoom, scossa). Le schermate sono vere: s3/demo -> s3/shots."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))

L = lambda t: ('label', t)
CTA = "Seguimi per il prossimo congegno, arriva presto."
S = {}

# ---------------------------------------------------------------- riga 19
S[56] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Prima e dopo', "Chiedere un'app"), ('body', 'Ogni venerdì: la stessa richiesta, fatta male e fatta bene.')],
  "Ecco la nuova rubrica del venerdì, prima e dopo. La stessa richiesta, fatta male e fatta bene.", dict(posa='saluta')),
 ([('chat', 'Prima', [('tu', "Fammi un'app"), ('ed', 'Certo. Ecco una lista dove scrivere delle cose.')])],
  "Prima. Scrivi fammi un'app e basta. Claude fa del suo meglio, ma deve indovinare tutto.", dict(scossa=True)),
 ([('duo', [('56_banale', 'tel', 'Prima'), ('55_piena', 'tel', 'Dopo')])],
  "Il risultato? A sinistra una lista anonima. A destra l'app delle abitudini, fatta su misura.", {}),
 ([L('Dopo: le 4 domande'), ('rows', [('Per chi è?', 'io, ogni sera'), ('Cosa deve fare?', 'spuntare'), ('Come appare?', 'grande'), ('Dove la uso?', 'telefono')])],
  "Cosa è cambiato? Quattro risposte. Per chi è, cosa deve fare, come appare e dove la usi.", {}),
 ([L('Il trucco'), ('typed', 'Prima di cominciare, fammi tu le domande che ti servono.')],
  "E se non sai cosa scrivere, chiedi a Claude di farti lui le domande. Rispondi, e il resto viene da sé.", {}),
 ([L('Da sapere'), ('body', 'Una richiesta vaga non è un errore: è solo un punto di partenza da correggere.'), ('stamp', 'Chiedi meglio')],
  "Una richiesta vaga non è un errore, è solo un punto di partenza. Si corregge parlando.", dict(zoom=True)),
], cta="Ci vediamo venerdì prossimo con un nuovo prima e dopo.")

S[57] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Un viaggio in vista?', 'Fallo diventare una mappa.'), ('body', 'Tappe, giorni e consigli, tutto in una pagina da toccare.')],
  "Hai un viaggio in programma? Invece di una lista, fatti fare una mappa da toccare.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Faccio la Puglia in 5 giorni a giugno, in auto. Fammi una mappa con le tappe, un giorno per tappa e un consiglio per ognuna.')],
  "Racconta il viaggio: quanti giorni, come ti sposti, cosa ti piace.", {}),
 ([('shot', '57_mappa', 'web', {'label': 'Il risultato vero'})],
  "Ecco la mappa. A sinistra i giorni, sulla cartina le tappe collegate dal percorso.", {}),
 ([('shot', [(0.0, '57_mappa'), (1.2, '57_mappa_lecce')], 'web', {'taps': [(0.6, 0.35, 0.43)]})],
  "Tocchi una tappa e si apre la scheda, con il consiglio del giorno.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Aggiungi dove mangiare la sera e i chilometri tra una tappa e l’altra'), ('ed', 'Fatto. Ho aggiunto i chilometri sul percorso e una cena per ogni tappa.')])],
  "Poi la arricchisci a parole. I ristoranti, i chilometri, le spiagge da non perdere.", {}),
 ([L('Da sapere'), ('body', 'Orari, prezzi e strade cambiano: controlla sempre le informazioni prima di partire.'), ('stamp', 'Controlla prima')],
  "Una cosa importante. Orari e prezzi cambiano, quindi prima di partire controlla le informazioni sui siti ufficiali.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 20
S[58] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Un sito per il negozio?', 'Senza agenzia.'), ('body', 'Orari, indirizzo e un pulsante per ordinare. Il resto è decorazione.')],
  "Hai un negozio e niente sito? Ti faccio vedere come nasce in pochi minuti.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi il sito del Forno Rossi: pane col lievito madre, orari, indirizzo con la mappa e un pulsante per ordinare con un messaggio. Colori caldi.')],
  "Descrivi la tua attività, cosa deve trovare il cliente e che atmosfera vuoi.", {}),
 ([('shot', '58_sito', 'web', {'label': 'Il risultato vero'})],
  "Ecco il sito. In alto il messaggio principale, sotto gli orari e dove trovarci.", {}),
 ([('shot', '58_sito_tel', 'tel', {'label': 'Sul telefono'})],
  "E sul telefono si sistema da solo. È lì che lo guarderanno quasi tutti i tuoi clienti.", {}),
 ([L('Cosa non deve mancare'), ('rows', [('Cosa fai, in una frase', ''), ('Orari e indirizzo', ''), ('Come contattarti', ''), ('Foto vere del negozio', '')])],
  "Le quattro cose che non devono mai mancare. Cosa fai, orari e indirizzo, come contattarti, e foto vere.", {}),
 ([L('Da sapere'), ('body', 'Gli esempi qui sono inventati. Nel tuo metti dati veri e controlla ogni numero di telefono.'), ('stamp', 'Dati veri')],
  "Il Forno Rossi è inventato. Nel tuo sito metti dati veri e controlla ogni numero, uno per uno.", dict(zoom=True)),
])

S[59] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Il sito è quasi giusto?', 'Correggilo a parole.'), ('body', 'Niente pannelli complicati: dici cosa cambiare.')],
  "Il sito è quasi perfetto, ma vorresti cambiare qualcosa? Non serve toccare niente, basta dirlo.", dict(posa='saluta')),
 ([('shot', '58_sito', 'web', {'label': 'Prima'})],
  "Riprendiamo il sito del forno. Mettiamo che il titolo ti sembri piccolo e i colori non ti convincano.", {}),
 ([L('Richiesta a Claude'), ('typed', 'Fai il titolo più grande, passa al verde e aggiungi una sezione per le torte su ordinazione.')],
  "Lo scrivi così, tutto in una richiesta. Titolo più grande, verde, e una sezione nuova per le torte.", {}),
 ([('shot', [(0.0, '58_sito'), (0.9, '59_sito_v2')], 'web', {'label': 'Dopo'})],
  "Ed ecco fatto. Titolo, colori e la sezione nuova, senza toccare una riga di codice.", {}),
 ([L('Si può chiedere'), ('rows', [('Colori e caratteri', ''), ('Sezioni nuove', ''), ('Testi più corti', ''), ('Ordine delle parti', '')])],
  "Puoi chiedere colori e caratteri, sezioni nuove, testi più corti, o di spostare le parti.", {}),
 ([L('Da sapere'), ('body', 'Una modifica alla volta è più facile da controllare. Se qualcosa si rompe, chiedi di tornare indietro.'), ('stamp', 'Un passo alla volta')],
  "Il consiglio, una modifica alla volta. E se qualcosa non va, chiedi di tornare alla versione di prima.", dict(zoom=True)),
])

S[60] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Il sito è pronto.', 'Ora mostralo a tutti.'), ('body', 'Un link da mandare su WhatsApp, da stampare o da mettere in vetrina.')],
  "Il sito è pronto. Ma come lo fai vedere agli altri? Con un link.", dict(posa='saluta')),
 ([L('Come si fa'), ('rows', [('Apri il sito che hai creato', ''), ('Premi Pubblica', ''), ('Copia il link', ''), ('Mandalo a chi vuoi', '')])],
  "Apri quello che hai creato, premi pubblica e copia il link. Chi lo apre vede il sito, non la tua conversazione.", {}),
 ([('shot', '58_sito_tel', 'tel', {'label': 'Aperto dal link'})],
  "Chi riceve il link lo apre dal telefono, come un qualsiasi sito.", {}),
 ([('chat', 'Dove metterlo', [('tu', 'Dove lo posso usare?'), ('ed', 'Nella bio di Instagram, nel profilo di Google, su un biglietto o in vetrina.')])],
  "Mettilo nella bio, nella scheda del negozio, su un biglietto da visita o su un cartello in vetrina.", {}),
 ([L('E se lo cambi?'), ('body', 'Quando modifichi il sito, ricordati di pubblicare di nuovo la versione aggiornata.')],
  "E se poi lo modifichi, ricordati di pubblicare di nuovo la versione aggiornata.", {}),
 ([L('Da sapere'), ('body', 'Pubblicare vuol dire che chiunque abbia il link può vederlo: niente dati privati sulla pagina.'), ('stamp', 'Pubblico vuol dire pubblico')],
  "Ricorda, pubblico vuol dire pubblico. Chiunque abbia il link lo vede, quindi niente dati privati sulla pagina.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 21
S[61] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Un videogioco?', 'Sì, in una sera.'), ('body', 'Un gioco vero, da giocare sul telefono. Anche con i bambini.')],
  "Stasera facciamo una cosa divertente. Un videogioco vero, in una sera.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi un gioco per il telefono: un automa salta tra piattaforme e raccoglie monete. Tre livelli, si tocca lo schermo per saltare.')],
  "Descrivi il gioco come una storia. Chi è il protagonista, cosa deve fare, come si comanda.", {}),
 ([('shot', '61_titolo', 'tel', {'label': 'Il risultato vero'})],
  "Ecco la schermata iniziale, con i livelli da scegliere. L'ultimo si sblocca giocando.", {}),
 ([('shot', '61_gioco', 'tel', {'taps': [(0.8, 0.6, 0.55), (1.6, 0.7, 0.45)]})],
  "E si gioca davvero. Tocchi lo schermo, l'automa salta e raccoglie le monete.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'È troppo difficile per mio figlio'), ('ed', 'Ho rallentato i salti e aggiunto una vita in più nel primo livello.')])],
  "Troppo difficile? Troppo facile? Lo dici e il gioco cambia. È il modo più bello per imparare insieme.", {}),
 ([L('Da sapere'), ('body', 'I giochi semplici vengono bene subito. Per quelli grandi: un pezzo alla volta.'), ('stamp', 'Si gioca')],
  "I giochi semplici vengono bene subito. Per quelli più grandi, si costruisce un pezzo alla volta.", dict(zoom=True)),
])

S[62] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Prima e dopo', 'Chiedere un gioco'), ('body', 'Stessa idea, due richieste diverse.')],
  "Venerdì, quindi prima e dopo. Oggi chiediamo un gioco.", dict(posa='saluta')),
 ([('chat', 'Prima', [('tu', 'Fammi un gioco'), ('ed', 'Ecco un quadrato che salta un ostacolo.')])],
  "Prima. Fammi un gioco. Claude ne fa uno, ma non sa per chi, né come vuoi giocarci.", dict(scossa=True)),
 ([('duo', [('62_banale', 'tel', 'Prima'), ('61_gioco', 'tel', 'Dopo')])],
  "A sinistra un quadrato blu e la tastiera, che sul telefono non c'è. A destra il gioco vero.", {}),
 ([L('Dopo: cosa ho aggiunto'), ('rows', [('Che gioco è', 'salti e monete'), ('Come si comanda', 'tocco'), ('Quanti livelli', 'tre'), ('Per chi', '8 anni')])],
  "Cosa è cambiato? Che gioco è, come si comanda, quanti livelli e per chi è.", {}),
 ([L('Il trucco'), ('typed', 'Il gioco lo usa un bambino di 8 anni sul telefono.')],
  "Il dettaglio che cambia tutto è dire chi gioca e su cosa. Un bambino sul telefono non ha la tastiera.", {}),
 ([L('Da sapere'), ('body', 'Prova il gioco tu per primo e chiedi le correzioni una alla volta.'), ('stamp', 'Prima e dopo')],
  "Prova sempre il gioco tu per primo, e chiedi le correzioni una alla volta.", dict(zoom=True)),
], cta="Ci vediamo venerdì prossimo con un nuovo prima e dopo.")

S[63] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Una festa di compleanno?', 'Caccia al tesoro digitale.'), ('body', 'Indizi sul telefono, codici nascosti in casa, premio finale.')],
  "C'è una festa in arrivo? Organizziamo una caccia al tesoro, con gli indizi sul telefono.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi una caccia al tesoro per il compleanno di Sofia, 8 anni: 5 indovinelli sulla casa, ognuno sblocca il successivo con un codice.')],
  "Dai a Claude l'età, il posto e quanti indizi vuoi. Lui scrive gli indovinelli e costruisce il gioco.", {}),
 ([('shot', '63_indizio', 'tel', {'label': 'Il risultato vero', 'taps': [(1.4, 0.5, 0.62)]})],
  "Ogni indizio è un indovinello. I bambini trovano il codice nascosto e lo scrivono.", {}),
 ([('shot', [(0.0, '63_indizio'), (0.6, '63_ok')], 'tel')],
  "Codice giusto, e si sblocca l'indizio dopo. Fino al tesoro.", {}),
 ([L('Prima della festa'), ('rows', [('Nascondi i codici', ''), ('Prova tutto il giro', ''), ('Tieni un aiutino pronto', '')])],
  "Prima della festa nascondi i codici, prova tu tutto il giro e tieni pronto un aiutino.", {}),
 ([L('Da sapere'), ('body', 'Con i bambini piccoli stai vicino: il telefono è un mezzo, la festa siete voi.'), ('stamp', 'Buona caccia')],
  "Con i più piccoli stai vicino. Il telefono è solo un mezzo, la festa siete voi.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 22
S[64] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Cento foto delle vacanze?', 'Diventano un video.'), ('body', 'Titoli, ordine, passaggi morbidi. La musica la scegli tu.')],
  "Hai cento foto delle vacanze nel telefono? Facciamole diventare un video da rivedere.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Ti mando le foto dell’estate. Fammi un video di 3 minuti, in ordine di data, con un titolo per ogni posto.')],
  "Dai a Claude le foto e spiegagli come lo vuoi. Durata, ordine, titoli.", {}),
 ([('shot', '64_titolo', 'vid', {'label': 'Il risultato vero'})],
  "Ecco l'apertura. Il titolo sulla prima foto, poi le foto scorrono una dopo l'altra.", {}),
 ([('shot', [(0.0, '64_monti'), (1.6, '64_fine')], 'vid')],
  "Ogni posto ha il suo titolo, e alla fine una chiusura. Il risultato è un file video da scaricare.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Più lento, e togli le foto mosse'), ('ed', 'Fatto. Ogni foto resta quattro secondi e ne ho tolte sei sfocate.')])],
  "Poi lo sistemi a parole. Più lento, meno foto, un titolo diverso.", {}),
 ([L('Da sapere'), ('body', 'La musica mettila tu: quella famosa ha i diritti. Chiedi il permesso a chi compare nelle foto.'), ('stamp', 'Ricordi in ordine')],
  "Due regole. La musica famosa ha i diritti, quindi scegli tu cosa usare. E chiedi sempre il permesso a chi compare nelle foto.", dict(zoom=True)),
])

S[65] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Difficile da spiegare?', 'Fanne un video animato.'), ('body', 'Disegni che si muovono valgono più di mille parole.')],
  "Devi spiegare una cosa a tanta gente? Un piccolo video animato funziona meglio di un foglio.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi un video animato di un minuto per spiegare la differenziata ai condòmini: i bidoni, cosa ci va dentro, i casi dubbi.')],
  "Dici l'argomento, chi lo guarderà e quanto deve durare.", {}),
 ([('shot', '65_s1', 'vid', {'label': 'Il risultato vero'})],
  "Ecco l'inizio. I quattro bidoni, ognuno con il suo colore, e gli oggetti che ci cadono dentro.", {}),
 ([('shot', '65_s2', 'vid')],
  "Poi i casi dubbi, uno per scena. La freccia mostra dove va, e la frase sotto spiega perché.", {}),
 ([L('Funziona per'), ('rows', [('Regole del condominio', ''), ('Istruzioni di lavoro', ''), ('Una ricetta', ''), ('Una lezione a scuola', '')])],
  "Funziona per tante cose. Le regole del condominio, le istruzioni al lavoro, una ricetta, una lezione.", {}),
 ([L('Da sapere'), ('body', 'Le regole della differenziata cambiano da Comune a Comune: controlla le tue prima di pubblicarlo.'), ('stamp', 'Controlla le fonti')],
  "Attenzione, le regole cambiano da Comune a Comune. Controlla le tue, prima di mandarlo a tutti.", dict(zoom=True)),
])

S[66] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'La tua attività', 'ha un volto?'), ('body', 'Logo, colori e caratteri: una piccola identità in un pomeriggio.')],
  "La tua attività ha un volto riconoscibile? Facciamo logo e colori, insieme.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi un logo per il Forno Rossi, dal 1962: tondo, caldo, con una pagnotta. Poi i colori e i caratteri da usare ovunque.')],
  "Racconta chi sei, da quando, e che sensazione vuoi dare.", {}),
 ([('shot', '66_logo', 'web', {'label': 'Il risultato vero'})],
  "Ecco la scheda. Il logo tondo, la versione lunga, i colori con i loro codici e i caratteri.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Fammene tre versioni diverse'), ('ed', 'Eccole: una classica, una moderna e una disegnata a mano.')])],
  "Non ti convince? Chiedi tre strade diverse e scegli quella che ti somiglia.", {}),
 ([L('Dove usarlo'), ('rows', [('Insegna e sacchetti', ''), ('Sito e social', ''), ('Biglietti da visita', ''), ('Menù e volantini', '')])],
  "Poi lo usi dappertutto. L'insegna, i sacchetti, il sito, i biglietti, i volantini.", {}),
 ([L('Da sapere'), ('body', 'Prima di stamparlo, controlla che non somigli al marchio di qualcun altro.'), ('stamp', 'Tutto tuo')],
  "Prima di stamparlo, controlla che non somigli al marchio di qualcun altro. Il logo deve essere solo tuo.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 23
S[67] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Bollette e carburante?', 'Tutto in un colpo d’occhio.'), ('body', 'Una dashboard: una pagina che riassume i tuoi numeri.')],
  "Le bollette dell'anno sono sparse ovunque? Mettiamole in una pagina sola, che si capisce al volo.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Ti allego le spese di casa del 2026. Fammi una pagina con i totali, la spesa mese per mese e dove vanno i soldi.')],
  "Allega i tuoi numeri, anche un foglio disordinato, e di' cosa vuoi vedere.", {}),
 ([('shot', '67_dash', 'web', {'label': 'Il risultato vero'})],
  "Ecco la pagina. In alto i totali, sotto i mesi e le voci, dalla più pesante alla più leggera.", {}),
 ([L('Si capisce subito'), ('rows', [('Dicembre è il mese più caro', '454 €'), ('Il gas è salito', '+4%'), ('Il carburante pesa di più', '1.704 €')])],
  "E si capisce subito quello che conta. Dicembre è il mese più caro, il gas è salito, il carburante pesa più di tutto.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Aggiungi il confronto con il 2025'), ('ed', 'Fatto. Ogni mese ora ha anche la barra dell’anno scorso.')])],
  "E puoi chiedere confronti, filtri, o un riepilogo da mandare in famiglia.", {}),
 ([L('Da sapere'), ('body', 'Controlla due o tre totali sul foglio originale. Se i dati sono sbagliati, la pagina sarà bella ma sbagliata.'), ('stamp', 'Ricontrolla')],
  "Controlla sempre due o tre totali sul foglio originale. Una pagina bella con dati sbagliati resta sbagliata.", dict(zoom=True)),
])

S[68] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Prima e dopo', 'Chiedere un grafico'), ('body', 'Un grafico serve a rispondere a una domanda.')],
  "Venerdì, prima e dopo. Oggi un grafico.", dict(posa='saluta')),
 ([('chat', 'Prima', [('tu', 'Fammi un grafico delle spese'), ('ed', 'Ecco una torta con i dodici mesi.')])],
  "Prima. Fammi un grafico delle spese. E arriva una torta con dodici fette tutte uguali.", dict(scossa=True)),
 ([('duo', [('68_banale', 'web', 'Prima'), ('67_dash', 'web', 'Dopo')])],
  "A sinistra non si capisce niente. A destra si vede subito qual è il mese più caro.", {}),
 ([L('Dopo: la richiesta'), ('typed', 'Voglio capire in che mese spendo di più. Barre dalla più alta, il mese più caro in rosso.')],
  "La differenza è la domanda. Non fammi un grafico, ma voglio capire in che mese spendo di più.", {}),
 ([L('Le domande giuste'), ('rows', [('Cosa voglio capire?', ''), ('Che dati uso?', ''), ('Chi lo guarderà?', '')])],
  "Prima di chiedere un grafico, chiediti cosa vuoi capire, che dati usi e chi lo guarderà.", {}),
 ([L('Da sapere'), ('body', 'Le torte vanno bene con poche fette. Per confrontare mesi, meglio le barre.'), ('stamp', 'Prima e dopo')],
  "Piccola regola. Le torte vanno bene con poche fette. Per confrontare tanti mesi, meglio le barre.", dict(zoom=True)),
], cta="Ci vediamo venerdì prossimo con un nuovo prima e dopo.")

S[69] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Quanto costa il viaggio?', 'Fatti un calcolatore.'), ('body', 'Uno strumento piccolo, fatto per una domanda sola.')],
  "Weekend in auto con gli amici? Invece di fare i conti a mano, fatti un calcolatore.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi un calcolatore per il costo di un viaggio in auto: chilometri, consumo, prezzo del carburante, pedaggi e persone. Il risultato a testa.')],
  "Elenca cosa entra nel conto e cosa vuoi sapere alla fine.", {}),
 ([('shot', '69_calc', 'tel', {'label': 'Il risultato vero'})],
  "Ecco lo strumento. Scrivi i numeri e il conto si fa da solo, con la quota a testa.", {}),
 ([('shot', [(0.0, '69_calc'), (1.0, '69_calc3')], 'tel', {'taps': [(0.5, 0.82, 0.6)]})],
  "Se uno degli amici non viene, cambi le persone e la quota si aggiorna subito.", {}),
 ([L('Altre idee'), ('rows', [('Dividere le bollette', ''), ('Quanta pittura serve', ''), ('La rata di un acquisto', ''), ('Le dosi di una ricetta', '')])],
  "Puoi farne uno per tutto. Dividere le bollette, la pittura per una stanza, le dosi di una ricetta.", {}),
 ([L('Da sapere'), ('body', 'Fai una prova con un conto che conosci già: se torna, il calcolatore è giusto.'), ('stamp', 'Fai la prova')],
  "Prima di fidarti, fai una prova con un conto che conosci già. Se torna, il calcolatore è giusto.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 24
S[70] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Chiudi l’app', 'e ritrovi tutto?'), ('body', 'Un’app che si ricorda i tuoi dati tra una volta e l’altra.')],
  "Un'app che si ricorda quello che hai scritto anche domani. Ti mostro come chiederla.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi la lista della spesa di casa, divisa per reparto. Deve ricordarsi le cose anche quando la chiudo.')],
  "La frase chiave è deve ricordarsi le cose anche quando la chiudo.", {}),
 ([('shot', '70_spesa', 'tel', {'label': 'Il risultato vero'})],
  "Ecco la lista, divisa per reparti. Spunti quello che hai preso.", {}),
 ([('shot', [(0.0, '70_spesa'), (1.0, '70_spesa2')], 'tel', {'taps': [(0.5, 0.86, 0.2)]})],
  "Aggiungi lo yogurt, chiudi tutto, e domani la lista è ancora lì.", {}),
 ([('chat', 'Chiedilo sempre', [('tu', 'Dove vengono salvati i dati?'), ('ed', 'Te lo spiego, e se vuoi aggiungo un pulsante per scaricarne una copia.')])],
  "Chiedi sempre dove vengono salvati i dati. E in un'app così, niente informazioni delicate.", {}),
 ([L('Da sapere'), ('body', 'Per cose importanti tieni anche una copia: chiedi un pulsante per scaricare la lista.'), ('stamp', 'Fai una copia')],
  "E per le cose importanti tieni anche una copia. Chiedi un pulsante per scaricarla.", dict(zoom=True)),
])

S[71] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'La tua app', 'sul telefono.'), ('body', 'Un’icona come le altre, accanto alle tue app.')],
  "Hai creato un'app e vuoi averla sul telefono come le altre? Si fa in tre tocchi.", dict(posa='saluta')),
 ([L('I passi'), ('rows', [('Pubblica l’app e apri il link', ''), ('Tocca il tasto Condividi', ''), ('Aggiungi alla schermata Home', '')])],
  "Pubblica l'app e apri il link sul telefono. Poi condividi, e aggiungi alla schermata Home.", {}),
 ([('shot', [(0.0, '70_spesa'), (1.4, '71_home')], 'tel', {'label': 'Sul telefono'})],
  "Ed ecco la nuova icona, accanto alle altre.", {}),
 ([('shot', [(0.0, '71_home'), (1.4, '70_spesa')], 'tel', {'taps': [(0.6, 0.5, 0.33)]})],
  "La tocchi e si apre subito, senza cercare il link ogni volta.", {}),
 ([L('Fallo per'), ('rows', [('La lista della spesa', ''), ('Il calcolatore del viaggio', ''), ('Le abitudini del mattino', '')])],
  "Fallo per gli strumenti che usi tutti i giorni. La spesa, il calcolatore, le abitudini.", {}),
 ([L('Da sapere'), ('body', 'È un collegamento al link: serve internet per aprirla, e non passa dallo store.'), ('stamp', 'Tre tocchi')],
  "Una cosa da sapere. È un collegamento al link, quindi di solito serve internet per aprirla.", dict(zoom=True)),
])

S[72] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Chi lava i piatti stasera?', 'Decide l’app.'), ('body', 'I turni di casa, giusti e senza discussioni.')],
  "In casa si litiga su chi lava i piatti? Facciamo decidere a un'app, così nessuno si lamenta.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi un’app con i turni di casa per Giulia, Marco e Luca: sei faccende, due a testa, che ruotano ogni settimana.')],
  "Dai i nomi, le faccende e ogni quanto devono girare.", {}),
 ([('shot', '72_turni', 'tel', {'label': 'Il risultato vero'})],
  "Ecco la settimana. Ognuno ha le sue due faccende, e si spuntano quando sono fatte.", {}),
 ([('shot', [(0.0, '72_turni'), (1.0, '72_turni2')], 'tel', {'taps': [(0.5, 0.86, 0.06)]})],
  "Arriva lunedì, tocchi ruota e le faccende passano al prossimo. Giusto per tutti.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Luca ha 10 anni, dagli le cose più leggere'), ('ed', 'Fatto. Luca ruota solo tra spazzatura, cane e tavola.')])],
  "Puoi tenere conto delle età, dei turni di lavoro, di chi è via nel fine settimana.", {}),
 ([L('Da sapere'), ('body', 'L’app aiuta, ma le regole decidetele insieme a tavola.'), ('stamp', 'Pace in casa')],
  "L'app aiuta, ma le regole decidetele insieme, a tavola. Funziona molto meglio.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 25
S[73] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Un libretto da stampare?', 'Impaginato bene.'), ('body', 'Copertina, foto, date: un PDF pronto per la stampa.')],
  "Devi preparare un libretto per un'associazione? Facciamolo impaginato bene, pronto da stampare.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi il programma 2027 del circolo bocce Le Querce: copertina, una pagina con le date delle gare e delle cene. In PDF, A4.')],
  "Dici cosa contiene, per chi è e il formato. Qui un PDF in A4.", {}),
 ([('shot', '73_cop', 'doc', {'label': 'Il risultato vero'})],
  "Ecco la copertina, semplice e pulita.", {}),
 ([('shot', '73_int', 'doc')],
  "E dentro le date, una per riga, ognuna con due parole di spiegazione.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Metti il logo del circolo e le foto della festa'), ('ed', 'Allegale e le sistemo io, una per pagina.')])],
  "Poi aggiungi le foto vere e il logo. Claude le impagina al posto giusto.", {}),
 ([L('Da sapere'), ('body', 'Stampane una copia di prova prima di farne cento: i colori a schermo ingannano.'), ('stamp', 'Copia di prova')],
  "Prima di stamparne cento, fanne una di prova. I colori sullo schermo ingannano.", dict(zoom=True)),
])

S[74] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Prima e dopo', 'Chiedere un PDF'), ('body', 'Stesso circolo, stesso programma, due risultati.')],
  "Venerdì, prima e dopo. Oggi un documento da stampare.", dict(posa='saluta')),
 ([('chat', 'Prima', [('tu', 'Scrivi il programma del circolo'), ('ed', 'Ecco un testo con le attività previste.')])],
  "Prima. Scrivi il programma del circolo. Arriva un testo generico, senza date e senza vita.", dict(scossa=True)),
 ([('duo', [('74_banale', 'doc', 'Prima'), ('73_int', 'doc', 'Dopo')])],
  "A sinistra un muro di parole. A destra un libretto che i soci leggono davvero.", {}),
 ([L('Dopo: cosa ho detto'), ('rows', [('Per chi', 'i soci'), ('Cosa', 'le date del 2027'), ('Stile', 'caldo, con foto'), ('Formato', 'PDF A4')])],
  "Cosa è cambiato? Per chi è, cosa contiene, lo stile e il formato.", {}),
 ([L('Il trucco'), ('typed', 'Ecco le date vere: 14 marzo gara, 25 aprile pranzo, 19 giugno torneo, 11 settembre festa.')],
  "E il dettaglio più importante, i dati veri. Senza date vere, Claude può solo restare sul vago.", {}),
 ([L('Da sapere'), ('body', 'Se non dai le informazioni, non devono comparire inventate: controlla ogni data.'), ('stamp', 'Prima e dopo')],
  "Controlla sempre ogni data. Le informazioni importanti dalle tu, non devono comparire inventate.", dict(zoom=True)),
], cta="Ci vediamo venerdì prossimo con un nuovo prima e dopo.")

S[75] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Le solite slide noiose?', 'Falle muovere.'), ('body', 'Titoli grandi, poche parole e numeri che crescono davanti a tutti.')],
  "Devi presentare qualcosa e temi che si addormentino tutti? Facciamo slide che si muovono.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi 8 slide per l’assemblea di condominio sul nuovo cortile: tre proposte con i costi, grafici animati, pochissimo testo.')],
  "Dici l'occasione, quante slide, e che le vuoi animate e con poco testo.", {}),
 ([('shot', '75_s1', 'web', {'label': 'Il risultato vero'})],
  "La prima slide. Un titolo grande e una riga sola, niente muri di testo.", {}),
 ([('shot', '75_s2', 'web')],
  "Poi i costi. Le barre crescono una alla volta, e tutti guardano la stessa cosa.", {}),
 ([L('Durante la presentazione'), ('rows', [('Si va avanti con le frecce', ''), ('Funziona da qualsiasi computer', ''), ('Basta il link', '')])],
  "Si aprono dal link, su qualsiasi computer, e vai avanti con le frecce.", {}),
 ([L('Da sapere'), ('body', 'Prova le slide sul computer della sala prima dell’assemblea. Tieni anche una copia in PDF.'), ('stamp', 'Prova generale')],
  "Fai sempre una prova sul computer della sala. E tieni una copia in PDF, non si sa mai.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 26
S[76] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Il menù è scritto a mano?', 'Facciamolo bello.'), ('body', 'Un menù da stampare, in ordine e leggibile.')],
  "Il menù del locale è ancora un foglio scritto a mano? Facciamolo bello e da stampare.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi il menù della Trattoria da Nino, foglio A4: primi, secondi e dolci con i prezzi, stile osteria di una volta.')],
  "Dai i piatti con i prezzi, il formato e lo stile del locale.", {}),
 ([('shot', '76_menu', 'doc', {'label': 'Il risultato vero'})],
  "Ecco il menù. Le sezioni separate, i prezzi allineati, e in fondo la nota sulle allergie.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Fai anche la versione in inglese'), ('ed', 'Eccola, stessa grafica. Ho tenuto i nomi dei piatti in italiano.')])],
  "In un attimo anche la versione per i turisti, con la stessa grafica.", {}),
 ([L('Con lo stesso stile'), ('rows', [('Il volantino della serata', ''), ('Il cartello degli orari', ''), ('Il buono regalo', '')])],
  "Con lo stesso stile fai il volantino, il cartello degli orari, il buono regalo.", {}),
 ([L('Da sapere'), ('body', 'Prezzi e allergeni li controlli tu, riga per riga: sono informazioni che contano.'), ('stamp', 'Rileggi i prezzi')],
  "Prezzi e allergeni li controlli tu, riga per riga. Sono informazioni che contano.", dict(zoom=True)),
])

S[77] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Collezione nel cassetto?', 'Fanne un catalogo.'), ('body', 'Foto, schede e filtri: ritrovi tutto in un secondo.')],
  "Hai una collezione nel cassetto? Francobolli, monete, vinili. Facciamone un catalogo.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Ti mando le foto e l’elenco dei francobolli del nonno. Fammi un catalogo con una scheda per ognuno, la ricerca e i filtri per paese e anno.')],
  "Dai a Claude le foto e un elenco, anche fatto a mano. Spiega come vuoi cercare.", {}),
 ([('shot', '77_cat', 'web', {'label': 'Il risultato vero'})],
  "Ecco il catalogo. Una scheda per ogni pezzo, la ricerca in alto e i filtri.", {}),
 ([L('I filtri'), ('rows', [('Italia', '10 pezzi'), ("Anni '60", ''), ('Animali', ''), ('Da valutare', '')])],
  "Tocchi un filtro e restano solo i pezzi che cerchi. Su duecento, in un attimo.", {}),
 ([('chat', 'Chiedimi ancora', [('tu', 'Quanto valgono?'), ('ed', 'Non posso darti un valore sicuro: ti preparo la lista per un perito.')])],
  "E se chiedi quanto valgono? Una stima seria la fa un esperto. Claude ti prepara la lista da portargli.", {}),
 ([L('Da sapere'), ('body', 'Tieni una copia del catalogo e delle foto: è il ricordo di una vita.'), ('stamp', 'Al sicuro')],
  "Tieni sempre una copia, delle foto e del catalogo. È il ricordo di una vita.", dict(zoom=True)),
])

S[78] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Duecento file a caso?', 'In ordine in un colpo.'), ('body', 'Rinominare, dividere in cartelle, unire i PDF.')],
  "La cartella dei download è un disastro? Mettiamo in ordine duecento file in un colpo.", dict(posa='saluta')),
 ([('shot', '78_prima', 'web', {'label': 'Prima'})],
  "Ecco come si presenta. Nomi senza senso, foto e documenti tutti mescolati.", dict(scossa=True)),
 ([L('Richiesta a Claude'), ('typed', 'Rinomina le foto con data e luogo, mettile in una cartella per viaggio, e sposta i PDF in Documenti. Prima fammi vedere il piano.')],
  "Collega la cartella o carica i file, e spiega l'ordine che vuoi. E chiedi di vedere prima il piano.", {}),
 ([('shot', '78_dopo', 'web', {'label': 'Dopo'})],
  "Ed ecco il risultato. Una cartella per ogni viaggio, le foto con data e luogo, i documenti a parte.", {}),
 ([L('Si può fare'), ('rows', [('Unire tanti PDF in uno', ''), ('Rimpicciolire le foto', ''), ('Trovare i doppioni', '')])],
  "Puoi anche unire tanti PDF in uno, rimpicciolire le foto, trovare i doppioni.", {}),
 ([L('Da sapere'), ('body', 'Prima di tutto fai una copia della cartella. E controlla il piano prima di dire sì.'), ('stamp', 'Copia prima')],
  "La regola d'oro, prima di tutto fai una copia della cartella. E controlla il piano prima di dire sì.", dict(zoom=True)),
])

# ---------------------------------------------------------------- riga 27
S[79] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Un sito completo', 'in un pomeriggio.'), ('body', 'Più pagine, un modulo di iscrizione, il link da mandare.')],
  "Ultima riga della stagione. Mettiamo insieme tutto e costruiamo un sito completo, in un pomeriggio.", dict(posa='saluta')),
 ([L('Richiesta a Claude'), ('typed', 'Fammi il sito del torneo di calcetto dei bar: home con data e posti liberi, pagina delle regole e una per iscrivere la squadra. Colori blu e giallo.')],
  "Dici quali pagine vuoi, cosa c'è in ognuna e i colori.", {}),
 ([('shot', '79_home', 'web', {'label': 'Il risultato vero'})],
  "Ecco la home. La data, il campo, e i numeri che contano: squadre, posti liberi, giorni mancanti.", {}),
 ([('shot', [(0.0, '79_regole'), (1.6, '79_iscr')], 'web', {'taps': [(1.0, 0.93, 0.05)]})],
  "Poi le regole, e la pagina per iscriversi. Si compila e arriva la conferma.", {}),
 ([L('Il pomeriggio'), ('rows', [('Prima bozza', '15 min'), ('Correzioni a parole', '1 ora'), ('Testi e foto veri', '1 ora'), ('Pubblica e condividi', '5 min')])],
  "Come si divide il pomeriggio? Prima bozza, correzioni a parole, testi e foto veri, poi pubblichi.", {}),
 ([L('Da sapere'), ('body', 'Se raccogli i dati delle persone, chiedi solo quelli che servono e spiega a cosa servono.'), ('stamp', 'Pochi dati')],
  "Se raccogli iscrizioni, chiedi solo i dati che servono, e spiega a cosa servono.", dict(zoom=True)),
])

S[80] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Prima e dopo', 'Il brief perfetto'), ('body', 'L’ultimo della stagione: come si chiede un progetto grande.')],
  "Ultimo prima e dopo della stagione. Come si chiede un progetto grande.", dict(posa='saluta')),
 ([('chat', 'Prima', [('tu', 'Fammi un sito'), ('ed', 'Ecco un sito di benvenuto.')])],
  "Prima. Fammi un sito. E arriva una pagina di benvenuto, uguale a mille altre.", dict(scossa=True)),
 ([('duo', [('80_banale', 'web', 'Prima'), ('79_home', 'web', 'Dopo')])],
  "A sinistra una pagina vuota di senso. A destra il sito del torneo, pronto per le iscrizioni.", {}),
 ([L('Il brief in 5 righe'), ('rows', [('Obiettivo', 'iscrizioni'), ('Pubblico', 'i bar del paese'), ('Pagine', 'home, regole, iscriviti'), ('Stile', 'blu e giallo'), ('Passi', 'bozza, poi dettagli')])],
  "Il brief perfetto sta in cinque righe. Obiettivo, pubblico, pagine, stile, e i passi.", {}),
 ([L('Il trucco finale'), ('typed', 'Facciamo un passo alla volta: prima la bozza, poi la sistemiamo insieme.')],
  "E l'ultima riga è la più importante. Un passo alla volta, prima la bozza e poi i dettagli.", {}),
 ([L('Da sapere'), ('body', 'Più il progetto è grande, più conviene dividerlo in pezzi piccoli.'), ('stamp', 'Brief perfetto')],
  "Più il progetto è grande, più conviene dividerlo in pezzi piccoli. Vale per tutto, non solo per i siti.", dict(zoom=True)),
], cta="Ci vediamo nella prossima stagione con nuovi prima e dopo.")

S[81] = dict(POSA='banco', X=470, sc=[
 ([('title2', 'Il viaggio è finito.', 'Il tuo comincia ora.'), ('body', 'Ventisette tappe: app, siti, giochi, video e documenti.')],
  "Siamo arrivati alla fine dell'atlante. Ventisette tappe, e adesso tocca a te.", dict(posa='saluta')),
 ([('shot', [(0.0, '55_piena'), (1.2, '61_gioco'), (2.4, '69_calc'), (3.6, '63_ok')], 'tel', {'label': 'Fatti in questa stagione'})],
  "Un'app per le abitudini, un videogioco, un calcolatore, una caccia al tesoro.", {}),
 ([('shot', [(0.0, '57_mappa'), (1.2, '67_dash'), (2.4, '75_s2'), (3.6, '79_home')], 'web')],
  "Una mappa di viaggio, i numeri di casa, le slide animate, un sito completo. Tutto senza scrivere codice.", {}),
 ([L('Le rotte della stagione'), ('rows', [('Di’ per chi è e cosa fa', ''), ('Correggi a parole', ''), ('Un passo alla volta', ''), ('Controlla i dati', '')])],
  "Le regole del viaggio sono quattro. Di' per chi è e cosa fa, correggi a parole, un passo alla volta, controlla i dati.", {}),
 ([('chat', 'Tocca a te', [('ed', 'Cosa vorresti costruire?'), ('ed', 'Scrivilo nei commenti: magari diventa una tappa.')])],
  "E adesso dimmi tu. Cosa vorresti costruire? Scrivilo nei commenti, magari diventa una tappa della prossima stagione.", {}),
 ([L('Da sapere'), ('body', 'Le idee migliori nascono da un problema vero di casa o di lavoro. Comincia da lì.'), ('stamp', 'Buon viaggio')],
  "Le idee migliori nascono da un problema vero, di casa o di lavoro. Comincia da lì.", dict(zoom=True)),
], cta="Grazie di aver viaggiato con me. Ci vediamo nella stagione quattro.")

for n, d in S.items():
    out = [f'NUM = {n}', f"POSA = {d['POSA']!r}", f"EDWIN_X = {d['X']}", 'SCENE = [']
    for p, v, o in d['sc']:
        assert '!' not in v and '...' not in v, v
        extra = ''.join(f', {k}={val!r}' for k, val in o.items())
        out.append(f' dict(panel={p!r}, voce={v!r}{extra}),')
    out.append(f" dict(panel=[('cta',)], voce={d.get('cta', CTA)!r}, posa='saluta'),")
    out.append(']')
    open(os.path.join(HERE, f's{n}.py'), 'w').write('\n'.join(out) + '\n')
print('ok', len(S))
