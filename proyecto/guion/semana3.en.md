# Semana 3 · Lantern Night

**Eighty years since the fire.** Eighty years ago the Royal Archive burned on Census Night. This week Valcenda lights lanterns on the river for everything that was lost. The Queen will come down to the wharves on Saturday.

## Apertura

- **nota**: Madam: the Unsigned Sheet is on every breakfast table. Nobody admits to reading it. Everybody quotes it.
- **nota**: And Mara Calce is back. She's waiting in the hall with her hat on, which is her way of saying she isn't leaving.
- si `marca(hoja_retirada)`: The salons are saying you had the sheets gathered up at the ball. Some call it prudence. Others, fear.
- si `marca(pista_archivo_interno)`: The Archive clerk signalled to you as you passed: bundle 80 has gone out again. This time nobody wrote it down.
- si `marca(irene_recelosa)`: Irene didn't come to Monday's tea. She sent word she had work. It's the first time she's sent an excuse.
- si `marca(irene_agradecida)`: Irene sends her regards through Bruna. Bruna says it's the first time Irene has sent anyone her regards.
- si `marca(rumor_compromiso_paso)`: Houses Lobreda and Veyra no longer ask for neighbouring tables: they ask for the same one. The rumour of the pass engagement has a date, though no one has said it.
- Opción **Receive Mara Calce** → Mara drops the Sheet on your desk. “I sold twice as many Chronicles this week. Don't look at me like that: I didn't write it. I wish I had. But it's badly printed: no press of mine leaves smudges like that.” Before leaving, she asks what you know. You don't answer. She smiles, as though that were an answer.
- Opción **Send her away with a polite note** → Mara returns your note with one line beneath yours: “Then I'll find out on my own.” The handwriting is large and hurried.

## Peticiones

- **camila** pide `s3_subasta`: Camila: “They're auctioning my husband's spyglass with the Archive's things. I don't want to buy it. I want to know who does.”
  - Si se cumple: You tell Camila who took the spyglass: House Marén. Camila laughs without humour. “The insurers. Of course. They buy everything that sinks.”
  - Si no: Camila doesn't ask again. But twice that week you see her watching the river from the bridge.
- **celia** pide `s3_clase`: Celia: “I want to go to the protocol lesson. If the Queen speaks to me at the river, I want to know how to answer. And I want to go without Nilo.”
  - Si se cumple: Celia comes back from the palace standing even straighter, if that's possible. She tells Nilo she didn't need anyone. Nilo claps far too loudly.
  - Si no: Celia practises curtsies alone in front of the corridor mirror. She counts them under her breath.

## An auction for the Archive · día 9 · jardines
*recepcion · plazas 2–4 · cualquiera*

> At the Serravalle Gardens, objects saved from the fire, or said to have been, go under the hammer. The proceeds go to restoring the Archive.

Requisito: estatus 5, presencia 4, chisme 4
- \+ Houses bid for charity and, above all, to be seen
- \+ Some lots interest more than one of your eight
- − A badly judged bid is remembered longer than a dance

**Carta**

*Dear Matchmaker,*

Eighty years on, things saved from the fire still turn up in attics: an inkwell, a map, a spyglass no one can explain. On Tuesday we'll auction them in my gardens, for the Archive. Bring your young people. Let them bid, let them be seen and, if possible, let them not overpay for an inkwell.

*Leonora Serravalle*

**Incidente (día 9)** · Lot 12 comes up: a chest of scorched, uncatalogued papers. A man in grey gloves bids at once, and high. Nobody knows who he's bidding for.

- **Bid for the chest on the Archive's behalf** (estatus, d 5)
  - Éxito: {mejor} raises the bid calmly until the man in grey gloves gives up. The chest will go back to the Archive, and the room applauds.
  - A medias: {mejor} drops out in time. The man in grey gloves takes the chest, but he's paid three times its worth.
  - Fallo: The bidding runs away and {mejor} is left holding a price that can't be paid. Leonora smooths it over with a smile. No one will forget.
- **Find out who the man in grey gloves is bidding for** (chisme, d 4)
  - Éxito: A Serravalle servant recognises him: he's Amalia Miravés's steward. Dario's aunt wants those papers, and wants them quietly.
  - A medias: No one knows him, but his carriage waits with its curtains drawn, in broad daylight.
  - Fallo: The question reaches the man in grey gloves. He watches {mejor} for the rest of the auction.
- **Ask to examine the papers before bidding** (intelecto, d 5)
  - Éxito: Among the papers, half burned, is a seal {mejor} doesn't recognise: an open door inside a circle. Leonora closes the chest a little too quickly.
  - A medias: They're allowed a moment's look. There are dates from eighty years ago and one word repeated: “Threshold.”
  - Fallo: Leonora refuses kindly: “Lots are for buying, my dear, not for reading.” The room laughs.

**Desenlace · favorable** — Hammer and charity
- publico: The Serravalle auction raised more than any in ten years. {grupo} bid with elegance and left with the room on their side.
  - si `asiste(saul)`: Captain Veyra bought an old map of the Greda pass for a discreet sum and gave it to the Archive on the spot. No one had ever seen him give anything away.
  - si `asiste(teo)`: Teo Rovena played auctioneer for three lots when the real one lost his voice. He sold an inkwell for the price of a horse.
- privado: Leonora writes to thank you, and adds at the end: “Lot 12 wasn't on my list. I don't know who brought it.”
  - si `asiste(irene)`: Irene didn't bid on anything. But she didn't take her eyes off lot 12 until it was carried away, and she left without saying goodbye.
  - si `asiste(dario) y marca(pujador_miraves)`: When it came out who the man in grey gloves was bidding for, Dario went very serious. Then he laughed too loudly at something that wasn't funny.

**Desenlace · medias** — Lukewarm bids
- publico: The auction for the Archive was respectable. {grupo} bid little and wisely, which in this season of reckonings is saying a lot.
- privado: The chest from lot 12 left the gardens in a carriage without a crest. None of your eight knows where it went.
  - si `asiste(irene)`: Irene followed the carriage with her eyes to the end of the street. Then she asked {mejor} the time, though she was wearing a watch.

**Desenlace · desaire** — One bid too many
- publico: At the Serravalle auction someone bid more than they could pay. The Chronicle won't say who; everyone already knows.
- privado: Leonora hasn't invited you to Thursday's tea. It's the first time in three seasons.

## A lesson in protocol · día 10 · palacio
*clase · plazas 1–3 · cualquiera*

> Mireya teaches how to speak to the Queen: when, how much and, above all, when not to.

- \+ +1 Standing for each attendee (up to 4)
- \+ The Queen will be at the river on Saturday
- − Mireya does not forgive a crooked curtsy

**Carta**

*Madam Matchmaker:*

Her Majesty will come down to the river on Saturday and, for the first time in years, will speak to whoever approaches her. That worries me. On Wednesday, at the palace, I'll teach what needs knowing: how to greet her, how much to say and what must never be asked. Send anyone who would like the Queen to remember their name for the right reasons.

*Mireya, Keeper of the Lists*

**Al completarse**
- publico: {grupo} took a lesson in protocol with Mireya at the palace. Word is they left bowing to the columns.
- privado: Mireya sends you one line: “Passed.” Coming from her, that's nearly an embrace.
  - si `asiste(isolda)`: Isolda barely spoke all lesson. Mireya says it's just what the Queen prefers: someone who says little and, when she speaks, says something.
  - si `asiste(nilo)`: Nilo addressed Mireya too familiarly twice and corrected himself three times. Mireya made him repeat the greeting until he stopped smiling.
  - si `asiste(teo)`: Teo asked what one must never ask the Queen. Mireya told him: exactly that.
  - si `asiste(celia)`: Celia made a perfect curtsy on the first attempt. Mireya said nothing, and Celia knew that was praise.
  - si `asiste(dario)`: Dario already knew all the protocol. Mireya asked where he'd learned it. “At my aunt's,” he said. “We practise a great deal at night.”

*(Cierre pendiente: se escribe en la parte 2.)*
