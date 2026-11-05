"""Didascalie della stagione 3: numero -> (gancio, cosa si impara, invito, hashtag tema, titolo TikTok)."""
F = "Edwin Arc è un personaggio creato con l'intelligenza artificiale. Esempi inventati, risultati veri fatti con Claude."
T = {
 55: ("Stagione 3: da oggi si costruisce. 🧭", "Un'app tutta tua in 5 minuti, senza codice e senza store: chiedi a Claude per chi è, cosa deve fare e come deve apparire. Poi la sistemi a parole.", "Salva il video e prova con la tua prima app.", "senzacodice", "La tua prima app in 5 minuti"),
 56: ("Prima e dopo n. 1: chiedere un'app. ✉️", "«Fammi un'app» dà una lista anonima. Quattro risposte cambiano tutto: per chi è, cosa fa, come appare, dove la usi. E se non sai cosa scrivere, chiedi a Claude di farti lui le domande.", "Scrivi nei commenti l'app che vorresti.", "primaedopo", "Prima e dopo: chiedere un'app"),
 57: ("Un viaggio in vista? 🗺️", "Dai a Claude giorni, mezzo e gusti: ti costruisce una mappa da toccare, con le tappe, il percorso e un consiglio per ogni giorno. Orari e prezzi controllali sempre sui siti ufficiali.", "Salva il video per il prossimo viaggio.", "viaggi", "Una mappa del tuo viaggio"),
 58: ("Un sito per il negozio, senza agenzia. 🥖", "Descrivi l'attività e cosa deve trovare il cliente: Claude crea il sito, bello anche sul telefono. Orari, indirizzo, contatti e foto vere non devono mai mancare.", "Salva il video e giralo a chi ha un negozio.", "piccoleimprese", "Un sito per il negozio"),
 59: ("Il sito è quasi giusto? ✏️", "Non serve toccare il codice: dici cosa cambiare. Colori, titolo più grande, una sezione nuova. Una modifica alla volta, e se qualcosa non va torni alla versione di prima.", "Salva il video per quando sistemerai il tuo sito.", "senzacodice", "Cambiare il sito a parole"),
 60: ("Il sito è pronto: ora mostralo. 🔗", "Pubblica, copia il link e mettilo dove serve: bio, scheda del negozio, biglietti, vetrina. Pubblico vuol dire pubblico: niente dati privati sulla pagina.", "Salva il video prima di pubblicare.", "senzacodice", "Pubblicare con un link"),
 61: ("Un videogioco in una sera. 🎮", "Descrivi il gioco come una storia: protagonista, obiettivo, comandi, livelli. Claude lo costruisce e ci giochi davvero sul telefono. Troppo difficile? Lo dici e cambia.", "Scrivi nei commenti che gioco inventeresti.", "giochi", "Un videogioco in una sera"),
 62: ("Prima e dopo n. 2: chiedere un gioco. ✉️", "«Fammi un gioco» dà un quadrato che salta con la tastiera. Dire chi gioca, su cosa e come si comanda dà un gioco vero da telefono.", "Salva il video e prova con i tuoi figli.", "primaedopo", "Prima e dopo: chiedere un gioco"),
 63: ("Una caccia al tesoro per la festa. 🗝️", "Età, posto e numero di indizi: Claude scrive gli indovinelli e costruisce il gioco, ogni codice sblocca l'indizio dopo. Prova tu il giro prima della festa.", "Salva il video per il prossimo compleanno.", "famiglia", "La caccia al tesoro digitale"),
 64: ("Cento foto diventano un video. 🎞️", "Dai a Claude le foto e spiega come lo vuoi: durata, ordine, titoli. Ottieni un file video da rivedere. La musica sceglila tu e chiedi il permesso a chi compare.", "Salva il video per le foto delle vacanze.", "ricordi", "Un video dalle tue foto"),
 65: ("Difficile da spiegare? Fanne un video animato. 💡", "Argomento, pubblico e durata: Claude prepara un video animato che spiega con disegni e frasi brevi. Le regole che citi controllale sempre alla fonte.", "Scrivi nei commenti cosa vorresti spiegare.", "spiegare", "Un video che spiega"),
 66: ("La tua attività ha un volto? 🎨", "Racconta chi sei e che sensazione vuoi dare: Claude propone logo, colori e caratteri da usare ovunque. Prima di stampare, controlla che non somigli al marchio di altri.", "Salva il video per la tua attività.", "branding", "Logo e colori"),
 67: ("Tutti i numeri di casa in una pagina. 📊", "Allega le spese, anche disordinate: Claude crea una dashboard con totali, mesi e voci, dalla più pesante. Controlla due o tre totali sul foglio originale.", "Salva il video e prova con le tue bollette.", "soldi", "Una dashboard dei tuoi numeri"),
 68: ("Prima e dopo n. 3: chiedere un grafico. ✉️", "Una torta da dodici fette non dice niente. «Voglio capire in che mese spendo di più» dà barre ordinate e il mese più caro in rosso. Il grafico risponde a una domanda.", "Salva il video per il prossimo grafico.", "primaedopo", "Prima e dopo: chiedere un grafico"),
 69: ("Quanto costa il viaggio in auto? 🚗", "Elenca cosa entra nel conto e cosa vuoi sapere: Claude ti fa un calcolatore su misura, con la quota a testa. Fai una prova con un conto che conosci già.", "Salva il video per il prossimo weekend.", "senzacodice", "Un calcolatore su misura"),
 70: ("Un'app che si ricorda tutto. 🛒", "Chiedi che si ricordi le cose anche quando la chiudi: la lista è lì anche domani. Chiedi sempre dove vengono salvati i dati, e niente informazioni delicate.", "Salva il video e prova con la lista della spesa.", "senzacodice", "Un'app che ricorda"),
 71: ("La tua app sul telefono. 📱", "Pubblica, apri il link sul telefono, Condividi e Aggiungi alla schermata Home: l'icona è lì accanto alle altre. È un collegamento al link, di solito serve internet.", "Salva il video e prova subito.", "smartphone", "L'app sul telefono"),
 72: ("Chi lava i piatti stasera? 🧽", "Nomi, faccende e ogni quanto ruotano: Claude crea l'app dei turni di casa, giusti per tutti. Le regole però decidetele insieme a tavola.", "Giralo a chi vive con te.", "famiglia", "I turni di casa"),
 73: ("Un libretto impaginato in PDF. 📘", "Contenuto, pubblico e formato: Claude impagina copertina e pagine interne, pronte per la stampa. Fai sempre una copia di prova prima di stamparne cento.", "Salva il video per la tua associazione.", "documenti", "Un libretto in PDF"),
 74: ("Prima e dopo n. 4: chiedere un PDF. ✉️", "«Scrivi il programma» dà un muro di parole. Per chi è, cosa contiene, stile, formato e soprattutto i dati veri danno un libretto che si legge davvero.", "Salva il video prima del prossimo documento.", "primaedopo", "Prima e dopo: chiedere un PDF"),
 75: ("Slide che non fanno dormire. 🎬", "Occasione, numero di slide, poco testo e grafici animati: Claude prepara una presentazione che si apre da un link. Prova sempre sul computer della sala.", "Salva il video per la prossima riunione.", "presentazioni", "Le slide animate"),
 76: ("Il menù da stampare. 🍝", "Piatti, prezzi, formato e stile del locale: Claude impagina il menù, e in un attimo anche la versione in inglese. Prezzi e allergeni controllali tu, riga per riga.", "Giralo a chi ha un locale.", "ristorazione", "Il menù da stampare"),
 77: ("Una collezione diventa un catalogo. 🔍", "Foto ed elenco, anche scritto a mano: Claude crea il catalogo con schede, ricerca e filtri. Per il valore serve un esperto: Claude ti prepara la lista da portargli.", "Scrivi nei commenti cosa collezioni.", "collezionismo", "Il catalogo della collezione"),
 78: ("Duecento file in ordine in un colpo. 🗂️", "Collega la cartella o carica i file e spiega l'ordine che vuoi: nomi con data e luogo, una cartella per viaggio, documenti a parte. Prima fai una copia e controlla il piano.", "Salva il video e sistema i tuoi download.", "organizzazione", "200 file in ordine"),
 79: ("Un sito completo in un pomeriggio. ⚽", "Pagine, contenuti e colori: Claude costruisce home, regole e iscrizioni, poi lo pubblichi con un link. Se raccogli dati, chiedi solo quelli che servono.", "Salva il video per il prossimo evento.", "senzacodice", "Un sito completo in un pomeriggio"),
 80: ("Prima e dopo n. 5: il brief perfetto. ✉️", "Cinque righe: obiettivo, pubblico, pagine, stile e passi. E l'ultima è la più importante: prima la bozza, poi i dettagli. Vale per ogni progetto grande.", "Salva il video: è il trucco della stagione.", "primaedopo", "Il brief perfetto"),
 81: ("Fine dell'atlante: tocca a te. 🧳", "Ventisette tappe tra app, siti, giochi, video e documenti, tutto senza codice. Le rotte: di' per chi è, correggi a parole, un passo alla volta, controlla i dati.", "Scrivi nei commenti cosa vuoi costruire nella stagione 4.", "senzacodice", "Il tuo atlante"),
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
        assert instagram(n).count('#') == 5 + instagram(n).count('#1') + instagram(n).count('#2') + instagram(n).count('#3') + instagram(n).count('#4') + instagram(n).count('#5'), n
    print(instagram(56)); print(tiktok(56))
