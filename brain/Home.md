---
tags: [home]
---
# 🧠 Second Brain · @ia.senza.codice

> Cattura tutto in **[[00 Inbox/Leggimi|Inbox]]**, poi ogni settimana sposta e collega. Una nota = un'idea.

## Navigazione
- 🚀 **Progetti** (hanno una fine): [[Stagione 1]] · [[Stagione 2]]
- 🧭 **Aree** (da curare sempre): [[Edwin Arc]] · [[Voce di Edwin]] · [[Stile e regole dei testi]] · [[Crescita del profilo]]
- 📚 **Risorse**: [[Banca delle idee]] · [[Prompt utili]] · [[Strumenti]]
- 🗓️ **Diario**: crea la nota di oggi con il pulsante del calendario (Note giornaliere)
- ♻️ [[Revisione settimanale]]

## Da pubblicare (richiede il plugin Dataview)
```dataview
TABLE riga, tipo, stato
FROM "brain/Contenuti"
WHERE stato != "pubblicato"
SORT numero ASC
```

## Idee in attesa
```dataview
LIST
FROM "brain/00 Inbox" OR #idea
WHERE file.name != "Leggimi"
SORT file.ctime DESC
LIMIT 15
```

## Contenuti migliori (compila i numeri dopo la pubblicazione)
```dataview
TABLE salvataggi, condivisioni, visualizzazioni
FROM "brain/Contenuti"
WHERE salvataggi
SORT salvataggi DESC
LIMIT 10
```
