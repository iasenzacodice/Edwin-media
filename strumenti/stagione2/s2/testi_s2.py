"""Didascalie della stagione 2: numero -> (gancio, cosa si impara, invito, hashtag tema, titolo TikTok)."""
F = "Edwin Arc è un personaggio creato con l'intelligenza artificiale."
T = {
 28: ("Stagione 2: si fa sul serio. 📄", "Non solo risposte in chat: chiedi all'IA un documento vero, con titoli e sezioni, da scaricare in Word o PDF o condividere con un link.", "Salva il video per la prossima festa di condominio.", "documenti", "Un documento da condividere"),
 29: ("Domani presenti e non hai le slide? 📊", "Dai all'IA argomento e scaletta: ti prepara una presentazione da scaricare in PowerPoint o PDF, con poco testo e un grafico dove serve.", "Salva il video e provala a voce prima di presentare.", "presentazioni", "Una presentazione in 5 minuti"),
 30: ("Un foglio che fa i conti da solo. 🧮", "L'IA ti prepara un foglio Excel con le formule già pronte: tu scrivi chi ha pagato, il resto si aggiorna. E i totali, controllali sempre.", "Salva il video per la prossima vacanza tra amici.", "excel", "Un foglio che fa i conti"),
 31: ("La settimana ti scappa di mano? 📅", "Se colleghi il tuo calendario, l'IA legge i tuoi impegni, trova i buchi liberi e ti propone gli appuntamenti. La conferma la dai sempre tu.", "Salva il video e prova lunedì mattina.", "agenda", "L'agenda della settimana con l'IA"),
 32: ("E se fosse l'IA a scriverti ogni lunedì? ⏰", "Con le attività programmate l'IA fa una cosa da sola, all'ora che decidi tu: il riepilogo della settimana, le scadenze di casa, le notizie del tuo settore.", "Scrivi nei commenti cosa ti faresti mandare ogni mattina.", "organizzazione", "I promemoria automatici"),
 33: ("Un progetto grande ti spaventa? 🗂️", "Chiedi all'IA di dividerlo in passi con le date. Se qualcosa slitta, ricalcola tutto: il piano si adatta, non si butta.", "Salva il video e taglia a fette il tuo prossimo progetto.", "organizzazione", "Un progetto in tanti passi"),
 34: ("Una domanda da cento link? 🔎", "Con la ricerca approfondita l'IA legge decine di fonti e ti dà un report ordinato, con le fonti per ogni affermazione. Apri le fonti e, per le scelte importanti, chiedi anche a un tecnico.", "Salva il video per la prossima decisione difficile.", "ricerca", "La ricerca approfondita"),
 35: ("Un contratto da firmare? ✍️", "Allegalo all'IA, con i tuoi dati coperti: ti segnala rinnovi automatici, penali e disdette, e te li spiega in parole semplici. Non è un avvocato: per le cose importanti chiedi a un professionista.", "Salva il video prima della prossima firma.", "contratti", "Leggere un contratto con l'IA"),
 36: ("Riunione finita, e il verbale? 📝", "Dai all'IA i tuoi appunti, anche disordinati: li trasforma in un verbale con decisioni, compiti e cose da verificare. Senza inventare niente.", "Salva il video e giralo a chi scrive sempre i verbali.", "lavoro", "Dalla riunione al verbale"),
 37: ("Ogni volta ricominci da zero? 🧠", "Con la memoria attiva l'IA si ricorda le cose importanti tra una chat e l'altra. Puoi vedere cosa ricorda, correggerlo, farglielo dimenticare o spegnere la memoria.", "Salva il video e decidi tu cosa farle ricordare.", "memoria", "La memoria di Claude"),
 38: ("Insegnalo una volta, lo rifà sempre uguale. 📒", "Con le skill spieghi all'IA un procedimento che ripeti spesso, come registrare le fatture, e la volta dopo basta un messaggio. Le prime volte controlla il risultato.", "Scrivi nei commenti quale procedimento le insegneresti.", "skill", "Le skill su misura"),
 39: ("Sembra scritto da un robot? 🖋️", "Dai all'IA qualche testo scritto da te: impara il tuo modo di scrivere e prepara messaggi che sembrano tuoi. Rileggi sempre prima di mandare.", "Salva il video e prova con il prossimo messaggio.", "scrittura", "Scrivere come te con l'IA"),
 40: ("I tuoi documenti sono nel cloud? ☁️", "Se colleghi il tuo spazio, per esempio Google Drive, l'IA cerca e legge i tuoi file e ti dice da quale documento ha preso la risposta. Il collegamento lo togli quando vuoi.", "Salva il video per la prossima ricerca tra i file.", "documenti", "I tuoi file collegati"),
 41: ("La cartella Download è un disastro? 🗃️", "Con l'app sul computer l'IA rinomina i file e li mette in cartelle chiare. Prima ti mostra il piano e aspetta il tuo sì. E fai sempre una copia dei file importanti.", "Salva il video e prova sulla cartella più disordinata.", "organizzazione", "Riordinare le cartelle"),
 42: ("Moduli online infiniti? 🖱️", "Con il browser collegato l'IA compila i moduli al posto tuo e si ferma prima dell'invio: controlli e premi tu. Password e pagamenti restano sempre roba tua.", "Salva il video per la prossima iscrizione.", "browser", "Compilare un modulo online"),
 43: ("Troppi numeri da spiegare? 📈", "Dai i dati all'IA e dille dove andrà: ti prepara un'infografica chiara da stampare o condividere. Ma i numeri controllali tu.", "Salva il video e scrivi nei commenti che dati vorresti raccontare.", "grafici", "Un'infografica in un attimo"),
 44: ("Una festa in arrivo? 🎉", "Dai all'IA chi festeggia, quando, dove e lo stile: ti propone l'invito, lo ritocchi a parole e lo scarichi come immagine o PDF. Rileggi data, ora e indirizzo.", "Salva il video per la prossima festa.", "inviti", "Un invito per la festa"),
 45: ("Un sito senza programmare? 🌐", "Per un evento basta una pagina: data, luogo con mappa, programma e un pulsante per confermare. L'IA la costruisce e tu la condividi con un link. Niente dati personali di tutti, mi raccomando.", "Salva il video per la prossima cena di classe.", "senzacodice", "Un sito per un evento"),
 46: ("Esame in arrivo? 🃏", "Dai all'IA i tuoi appunti: ti prepara flashcard e quiz, ti interroga e ti dice cosa ripassare. Controlla le carte con il libro.", "Salva il video e giralo a chi sta studiando.", "studiare", "Studiare con le flashcard"),
 47: ("Compiti di matematica e non ricordi niente? ✏️", "Chiedi all'IA di fare da tutor senza dare le soluzioni: fa domande un passo alla volta e la risposta la trova il ragazzo. Con i più piccoli, stai vicino.", "Salva il video per la prossima sera di compiti.", "scuola", "Il tutor dei compiti"),
 48: ("Vuoi imparare qualcosa di nuovo? 🍞", "L'IA ti prepara un corso su misura, a tappe, con i tuoi tempi. Dopo ogni lezione le racconti com'è andata e il corso si adatta.", "Scrivi nei commenti cosa vorresti imparare.", "imparare", "Un corso su misura"),
 49: ("Trasloco in vista? 📦", "Dai all'IA la data e qualche dettaglio: ti prepara il piano settimana per settimana e la lista di chi avvisare del nuovo indirizzo. Per i documenti ufficiali, controlla sui siti del Comune.", "Salva il video e giralo a chi sta per traslocare.", "casa", "Il trasloco organizzato"),
 50: ("Le favole sono finite? 🌙", "Con l'IA ne inventi una nuova ogni sera, con i personaggi che piacciono a tuo figlio e la durata giusta. La scrive lei, la magia la fai tu leggendola.", "Scrivi nei commenti i personaggi della prossima favola.", "famiglia", "Una favola della buonanotte"),
 51: ("Devi fare un discorso? 🥂", "Racconta all'IA la persona, qualche ricordo e quanto deve durare: ti propone scaletta e testo. Poi leggilo ad alta voce e cambia le parole che non diresti mai.", "Salva il video per il prossimo brindisi.", "discorsi", "Un discorso da ricordare"),
 52: ("Ti fidi ciecamente? Non farlo. 🛡️", "Chiedi all'IA di ricontrollare: cosa potrebbe essere sbagliato, quali sono le fonti, rifallo passo per passo. Per salute, soldi e leggi il controllo finale lo fa una persona competente.", "Salva il video: è il trucco più utile della stagione.", "verificare", "Fatti controllare"),
 53: ("Serata in famiglia senza idee? 🎲", "L'IA ti costruisce un gioco a quiz da fare sul telefono, con le domande che vuoi tu, il punteggio e le squadre. Provalo prima di cena.", "Scrivi nei commenti la domanda più difficile per la tua famiglia.", "giochi", "Un gioco per la famiglia"),
 54: ("Fine della stagione 2: il tuo primo progetto. 🧰", "Piano a passi, documento per tutti, promemoria e pagina per le iscrizioni: metti insieme i congegni della stagione. Comincia da qualcosa di piccolo, le decisioni restano tue.", "Scrivi nei commenti cosa vuoi imparare nella stagione 3.", "progetti", "Il tuo primo progetto con l'IA"),
}


def instagram(n):
    g, c, i, h, _ = T[n]
    return f"{g}\n{c}\n{i}\n\n{F}\n\n#intelligenzaartificiale #ia #claude #{h} #tecnologiafacile"


def tiktok(n):
    g, c, i, h, t = T[n]
    first = c.split('. ')[0].rstrip('.') + '.'
    return t, f"{g} {first} Edwin Arc è un personaggio creato con l'IA. #intelligenzaartificiale #ia #claude #{h} #tecnologiafacile"


if __name__ == '__main__':
    for n in T:
        assert instagram(n).count('#') == 5 and tiktok(n)[1].count('#') == 5, n
    print(instagram(34)); print(tiktok(34))
