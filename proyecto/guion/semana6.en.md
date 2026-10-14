# Semana 6 · The Grand Ball of the Seal

**The first frost.** The first frost falls on Valcenda. On Sunday, in the Hall of Columns, the Queen will seal the season's unions in the Archive's book.

## Apertura

- **nota**: Madam: it's the last week. The dance card is on your desk, and the note from the Archive underneath it.
- **nota**: The note says “before the ball.” The Archive opens on Friday night, to prepare the book of seals.
- si `marca(acuerdo_lavanda)`: Saúl and Isolda have sent their fathers a letter together. This time they actually sent it.
- si `marca(deuda_saldada)`: Camila came to thank you in person. She brought an old spyglass: “Isolda Marén gave it back to me. Neither of us cried. Almost.”
- si `marca(celia_rechaza_paso)`: Celia has returned the last page of the articles unsigned. Her father isn't speaking to her. She dances alone every morning, without counting.
- Opción **Go to the Archive on Friday night** → You note it in your diary with a single word: “Archive.” Then you cross it out, and write it again.
- Opción **Don't go: some things are better not known** → You put the note away with the envelope from the first week. If the season ends without your knowing, let it end that way.

## Peticiones

- **nilo** pide no ir a nada el día 4: Nilo: “Don't send me anywhere on Saturday. I have to tell someone what happens to me on moonlit nights. If I don't do it now, I never will.”
  - Si se cumple: On Sunday Nilo arrives at the ball looking like someone who has slept for the first time in years. He doesn't say whom he told. It shows.
  - Si no: Nilo tells no one. He smiles all week, as always. As always, too much.

## The first frost · día 1 · jardines
*paseo · plazas 2–4 · cualquiera*

> The gardens wake up white. The last stroll of the season, for saying quietly what won't be said at the ball.

Requisito: presencia 4, chisme 4, baile 3
- \+ What's said in the cold is remembered a long time
- − Leonora has invited the parents too

**Carta**

*Dear Matchmaker,*

My asters froze last night. That's autumn for you: just when it's finally lovely, it ends. On Wednesday we'll walk among the frost one last time. Bring whoever still has something to say.

*Leonora Serravalle*

**Desenlace · favorable** — Footprints in the frost
- publico: {grupo} strolled through the frozen Serravalle gardens. They left footprints in the frost, and some went in pairs.
- privado: As you part, Leonora says: “It's been a good season. I shall miss it, and I shan't say so in public.”

**Desenlace · medias** — Cold
- publico: The first-frost stroll was brief: it was too cold to say anything.
- privado: Some parents watched every step. No one dared take one.

**Desenlace · desaire** — Ice
- publico: There were slips at the frost stroll, and not all of them were on the ice.
- privado: Leonora sends you a jar of liniment. No note. A great deal of meaning.

## The Grand Ball of the Seal · día 5 · salon
*baile · plazas 8–8 · cualquiera · OBLIGATORIO*

> Twelve waltzes, eight young people and a book open on a lectern. At the end of the night, the Queen will seal whatever the season has joined.


**Carta**

*To the Matchmaker of the Season,*

Her Majesty expects you on Sunday in the Hall of Columns with your eight young people. There will be twelve waltzes and a single book. Fill in the dance card with care: what is danced tonight is sealed at dawn. Her Majesty wishes to add, in her own hand, that she has enjoyed this season more than any other.

*Mireya, Keeper of the Lists*

## The Salon Chronicle · Special issue · The Grand Ball of the Seal

*Twelve waltzes, one book and one Sheet. This Chronicle doesn't remember a night like it, and it has been remembering nights for thirty years.*

- **What the Queen sealed**: At dawn Her Majesty sealed the season's unions. The full list is on page two. The tears, on every page.
- **The archivist**: The author of the Unsigned Sheet is Irene Salvat, of the Royal Archive. This Chronicle, which suspected everyone but her, takes off its hat. And offers her a job.
- **The last sheet**: The Unsigned Sheet took its leave at the Grand Ball. It remains unsigned. This Chronicle is still looking, though no longer offering a reward.
- **A note from the publisher**: This Chronicle signs everything it prints. This season it has learned that signing isn't enough: one must also be right.

*End of the season. Mara Calce, publisher.*

## The Unsigned Sheet · Final issue · nº 5

*Eighty years on, what did not burn.*

Today this Sheet publishes folios 80 to 84 of the Royal Archive: the houses that, on Census Night, burned their own lineages to keep what wasn't theirs. Their names are below. Let the Queen do justice; we have only done remembering.
- si `marca(nombres_protegidos_final) o nivel(irene, isolda) >= A o nivel(irene, teo) >= A`: The pages of the Threshold Pact stay where they were. Those who only wanted to hide have the right to stay hidden.
- si `marca(hoja_completa) o no (marca(nombres_protegidos_final) o nivel(irene, isolda) >= A o nivel(irene, teo) >= A)`: We also publish the pages of the Threshold Pact, with all their names. Among them, a house of Greda Alta whose sons do not go out on moonlit nights.

*— Signed: I. S., archivist. There's no need to hide any more.*

## Sólo para sus ojos


## Gancho


## Epílogos

### nilo
- si `marca(nilo_confiesa) y union(nilo, camila)`: Nilo married Camila in the spring. On moonlit nights she closes the conservatory shutters and waters the plants until dawn. She has never asked him to promise anything.
- si `marca(nilo_confiesa) o marca(nilo_elige_promesa)`: Nilo learned to weigh what he promises. Someone in Valcenda knows his secret and keeps it. He no longer spends moonlit nights alone.
- si `marca(hoja_completa) o marca(nilo_visto)`: The final Sheet put House Lobreda on every tongue. Nilo went back to Greda Alta before winter. He still helps everyone, but from a distance now.
- si no: Nilo went on promising before anyone had finished asking. He nearly always delivered. Nearly.

### saul
- si `union(saul, dario)`: Saúl stayed in Valcenda. The army received a very correct and very brief letter. In the Veyra study there are now two pairs of gloves on the desk, and neither is worn.
- si `union(saul, isolda)`: Saúl and Isolda married for the convoys and love each other as partners. Their house has a door that can always be closed, and both of them use it.
- si `union(saul, celia)`: Saúl did his duty by the Greda pass and by his house. He is a proper husband, punctual and loyal. Some mornings, at the riding school, he stands a long time looking at nothing.
- si no: Saúl went back to Tiria after the Grand Ball, as ordered. He writes letters to Valcenda that never say anything, and that someone keeps in a drawer.

### dario
- si `union(saul, dario) o union(dario, celia)`: Dario let someone know him, and didn't die of fright. He still stumbles with talent, but only when he chooses to.
- si `marca(dario_sin_mascara) o marca(dario_guarda_secreto_isolda)`: Dario didn't marry this season. He stood up to his aunt and put off the inheritance another year. He says it's the bravest thing he's ever done, and that his knees were shaking.
- si no: Dario inherited House Miravés without wanting it. His carriage still has its curtains drawn. Now he is the one who won't open them.

### teo
- si `union(teo, celia) o union(teo, irene)`: Teo married someone who laughs with him and not at him. The mills are still struggling. The notebook of verse is on its third volume.
- si `union(teo, camila)`: Teo and Camila married for the accounts and make each other laugh every morning. The Rovena mills pay their wages on time. Teo says it's the funniest marriage in Valcenda, and nobody argues.
- si `marca(teo_conversacion_seria) o marca(teo_sin_chiste)`: Teo didn't marry this season. But he said something sincere once, in front of someone, and since then he hasn't been able to go back to being just a clown.
- si no: Teo is the most sought-after guest in Valcenda. People invite him to make them laugh. Nobody invites him for anything else.

### celia
- si `union(teo, celia) o union(dario, celia)`: Celia dances for pleasure. Sometimes she misses the third turn and laughs before anyone else. She has burned the list.
- si `union(saul, celia)`: Celia married for the Greda pass. She is the most admired lady in Valcenda. She still counts her steps, very quietly.
- si `marca(celia_rechaza_paso)`: Celia didn't marry. She turned down an engagement everyone took for granted and opened a dancing academy at the Greda Gate. Her pupils don't count their steps.
- si no: Celia is still perfect. One public mistake, one winter afternoon, nearly broke her. She got up on her own, but she hasn't danced since.

### irene
- si `union(irene, isolda) o union(teo, irene)`: Irene risked being seen, and someone saw all of her. She works at the Archive by day and, now, at night she only sleeps.
- si `marca(irene_descubierta) y marca(nombres_protegidos_final)`: Irene published the abuses and kept quiet about those who were only hiding. The Queen named her keeper of the recovered folios. Mara Calce offers her a job every week. She says no, every week, very politely.
- si `marca(irene_descubierta)`: Irene signed the last Sheet with her initials. She published everything. The truth won, and she lost two friends. She still doesn't know whether it was a fair trade.
- si no: No one knows who wrote the Unsigned Sheet. At the Archive, an archivist with small, very neat handwriting still works at night.

### isolda
- si `union(irene, isolda)`: Isolda said aloud what she wanted, in front of the whole court. Now she nearly always speaks first. When she doesn't, Irene waits.
- si `union(saul, isolda) y marca(isolda_hablo_primero)`: Isolda married Saúl for the convoys, with her eyes open. Behind her door there's someone she loves, and that someone knows it.
- si `union(saul, isolda)`: Isolda married Saúl for the convoys. It's a good alliance and a good husband. What she truly wanted she never told anyone.
- si no: Isolda went back to Port Nácar unmarried. She says little, and when she speaks, everyone falls silent to hear her. She still hasn't said what she most wanted to say.

### camila
- si `union(nilo, camila)`: Camila let herself be surprised. By a gentleman in a dreadful hat, twice on the same road. She says the third time no longer counts as chance.
- si `union(teo, camila)`: Camila married Teo for the accounts and discovered that laughing in the mornings is a kind of love too.
- si `marca(deuda_saldada)`: Camila didn't marry. She paid her debts, returned the spyglass to the sea and went to live alone on the coast. She says she's never been better. This time it's true.
- si no: Camila is still in Valcenda, watching everything, glass in hand. She's the best chaperone in the city. At night, she misses being surprised.

## Epílogo del misterio

- si `marca(irene_descubierta) y marca(nombres_protegidos_final)`: The truth about the fire came out, and those who were only hiding stayed safe. Valcenda learned that the truth can be told without doing harm. It took eighty years.
- si `marca(irene_descubierta)`: The whole truth about the fire came out, every name with it. There was justice and there was harm. In Greda Alta, one house closed its shutters for good.
- si `nivel(irene, isolda) >= A o nivel(irene, teo) >= A`: No one learned who wrote the Sheet. But the last one named none of those who were hiding: someone had convinced its author that silence, sometimes, is also justice.
- si no: No one learned who wrote the Sheet. The last one published everything. Valcenda read it, was scandalised and, as ever, no one asked whether it was true.

## Epílogo de la casamentera

- si `rep >= 12`: The Queen named you Matchmaker to the Crown. You've been given an office at the palace, overlooking the river. You prefer your residence, and so does Bruna.
- si `rep >= 4`: Your name is spoken with respect in the salons. Next season, six houses have already written to you. Bruna says this time she won't let you take more than eight.
- si no: Valcenda will soon forget you. Eight people won't. Some still write to you in winter, to tell you how they are.

## Confrontación en el Archivo

**Si `pistas >= 3 o nivel_max(irene) >= B`**
- **narración**: The Archive is dark but for one lamp. Irene waits by the lectern of the book of seals, wearing her clerk's sleeves.
- **irene**: You came. So you already know.
- **irene**: Yes. It's me. The envelope, the Sheets, the press in Arcos Bajos. I found the folios the houses burned to change who was whose child, and no one wanted to read them.
- **irene**: But among those folios there are others. Pages of the Pact, with the names of people who were only trying to hide. People I care about. Tomorrow I print the last issue, and I still don't know which names to include.
- **irene**: Someone told me to publish what was stolen and keep quiet about those who were hiding. I think they were right. But I wanted to hear it from you.
- Opción **“Publish the abuses. Protect the names.”** → Irene crosses out an entire list, slowly. She leaves only the names of those who stole. “Thank you,” she says. “I'd been waiting eighty years for someone to tell me that.” Then she laughs at herself: “Not eighty years. Three weeks.”
- Opción **“Publish all of it. One doesn't pick and choose the truth.”** → Irene nods without looking at you. “That's what I thought. I wish you'd told me something else.” She puts out the lamp.
- Opción **“Give me the folios. I'll take them to the Queen.”** → Irene hesitates a long time. Then she hands you the box. “If the Queen does with this what I didn't dare, it will have been worth it. If not, I'll never forgive you.”

**Si `no (pistas >= 3 o nivel_max(irene) >= B)`**
- **narración**: The Archive is dark. On the lectern of the book of seals lies a folded paper, in small, very neat handwriting.
- **narración**: “You still haven't found me. Perhaps it's better that way. Tomorrow you'll know what I decided.”
