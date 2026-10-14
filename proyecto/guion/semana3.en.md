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

## Boats at dusk · día 12 · muelles
*paseo · plazas 2–2 · cualquiera*

> On the eve of the Lanterns, the boatmen hire out boats for two. There's little rowing and a great deal of talking.

Requisito: presencia 4, chisme 5, intelecto 4
- \+ Two people alone in a boat get acquainted quickly
- − At nightfall the Serel current runs toward Arcos Bajos

**Carta**

*Madam,*

On Friday, the eve of the Lanterns, the guild hires out boats for two from the Exchange wharf. You row as far as the bridge and come back before dark. If you don't come back before dark, blame the current, which runs toward Arcos Bajos and has no manners at all.

*For the guild, the master boatman*

**Incidente (día 12)** · Night falls sooner than expected and the current carries the boat toward Arcos Bajos. On the bank, in a workshop that ought to be closed, a lamp is lit and a press is running.

- **Row firmly back to the wharf** (presencia, d 4)
  - Éxito: {mejor} rows against the current without losing good humour. They reach the wharf with red hands, laughing.
  - A medias: They make it back, but late and soaked. The boatman doesn't charge for the delay, out of pity.
  - Fallo: The oars cross, the boat spins twice and the guild has to rescue them. Half the wharf sees it.
- **Drift closer and see who's working in the workshop** (chisme, d 4)
  - Éxito: Through the window: a slender figure in clerk's sleeves, hanging sheets up to dry. At the sound of the oars, it puts out the lamp.
  - A medias: All they see are sheets hung up like washing. Then the lamp goes out.
  - Fallo: The boat knocks against the workshop jetty. The lamp goes out at once and someone slams the shutters.
- **Steer by the lanterns already hung and find slack water** (intelecto, d 4)
  - Éxito: {mejor} finds slack water under the bridge. They wait for the current to ease, and while they wait they talk more than all autumn.
  - A medias: They find the slack water, but it's cold. They talk little, sitting close.
  - Fallo: The slack water turns out to be a mudbank. They wait for the boatmen with water up to their ankles.

**Desenlace · favorable** — Under the bridge
- publico: {grupo} went boating on the eve of the Lanterns. They came back late, and nobody on the wharf dared ask what they'd been talking about.
- privado: The boatman says it's the latest boat back this autumn, and the only one that came back without an argument.
  - si `chispa(a, b)`: Stepping off the boat, {a} offered {b} a hand, and they took a little longer than necessary to let go.
  - si `asiste(irene)`: When they drifted near Arcos Bajos, Irene began talking very quickly about something else.

**Desenlace · medias** — Cold water
- publico: {grupo} went boating and came back soaked. The Serel has no respect for family names.
- privado: Bruna sets two pairs of gloves to dry by the fire and asks no questions.

**Desenlace · desaire** — Rescue at the wharf
- publico: The boatmen's guild had to rescue {grupo} on the eve of the Lanterns. Valcenda has been laughing all morning.
- privado: Each blames the other. Very politely, mind you.

## The Lantern Vigil · día 13 · muelles
*encargo_real · plazas 3–3 · cualquiera · OBLIGATORIO*

> Valcenda sets lanterns afloat on the Serel for what burned eighty years ago. This year the Queen comes down to the wharves and will speak to your young people.

Requisito: presencia 5, estatus 5, intelecto 5
- \+ The Queen will remember whoever speaks to her well
- \+ A night of remembrance: people speak from the heart
- − It's a commemoration: a joke at the wrong moment weighs double
- − Half of Valcenda has a Sheet in its pocket

**Carta**

*To the Matchmaker of the Season,*

Her Majesty will come down to the Serel wharves on Saturday at dusk to release the first lantern for the Archive. She wishes three of the season's young people to accompany her, at your choosing. The Queen will speak with them. I beg you to choose those who can remember without sorrow, and listen without looking at the clock.

*Mireya, Keeper of the Lists*

**Incidente (día 13)** · The Queen releases her lantern and turns to the young people. “Tell me, what do you think Valcenda lost that night?” She looks at {a}. Behind her, on the water, a lantern made from a printed sheet burns slowly.

- **Answer honestly: the names and the proof** (intelecto, d 5)
  - Éxito: {mejor} speaks of the records no one could rebuild: who was whose child, who owned what. The Queen listens without interrupting. “Exactly,” she says. “And someone took advantage.”
  - A medias: The answer is good, but long. The Queen nods politely and looks at the water.
  - Fallo: {mejor} gets tangled in dates and surnames. Several houses clear their throats at once.
- **Answer as Mireya taught: brief, dignified, no names** (estatus, d 5)
  - Éxito: “Its memory, Your Majesty. That's why we're here.” The Queen smiles for the first time that night. Mireya breathes.
  - A medias: The answer is correct. The Queen has heard it a hundred times and is grateful, but won't remember it.
  - Fallo: The bow comes out crooked and the sentence half finished. Mireya closes her eyes.
- **Don't answer: offer her a lantern to release for whomever she wishes** (presencia, d 5)
  - Éxito: The Queen takes the lantern and stays silent a long while. She releases it without saying for whom. When she turns back, her eyes are bright and she doesn't hide it.
  - A medias: The Queen accepts the lantern with distant courtesy. She releases it and moves on.
  - Fallo: The lantern goes out before it touches the water. Someone laughs, then stops short.

**Desenlace · favorable** — A thousand lanterns
- publico: The Queen released the first lantern and spoke at length with {grupo}. Nobody remembers a Lantern Night so beautiful, or so talked about.
  - si `asiste(celia) y asistio(s3_clase, celia)`: Celia Lobreda answered the Queen without a moment's hesitation. The Queen asked where she'd learned. “On my own, Your Majesty,” said Celia.
  - si `asiste(saul) y asiste(isolda) y marca(semilla_lavanda)`: Captain Veyra and Miss Marén released a lantern together. The Queen remarked that they made a fine pair. Neither knew what to say.
  - si `asiste(nilo)`: Nilo Lobreda helped the boatmen release the lanterns of those with no one to release them. The Queen saw, and said nothing.
- privado: Mireya sends you a note: “Her Majesty asks whether you believe, as she does, that some things did not burn.”
  - si `asiste(irene)`: Irene released a lantern with no name on it. When asked who it was for, she said: “For the ones nobody wrote down.”

**Desenlace · medias** — A proper evening
- publico: The Lantern Vigil was solemn and proper. The Queen greeted {grupo} courteously, and returned early to the palace.
- privado: Floating among the lanterns were scraps of printed sheets. Someone had used them as lantern paper.

**Desenlace · desaire** — A lantern gone out
- publico: On Lantern Night the Queen withdrew early. Word is that something among the Matchmaker's young people made her uncomfortable.
- privado: Mireya hasn't written. You already know what it means when Mireya doesn't write.

**Desenlace · sin_asistentes**
- publico: The Matchmaker did not accompany the Queen on Lantern Night. The Queen released her lantern alone.

## The Salon Chronicle · Issue 3 · Printed by Calce, Street of Seals

*A thousand lanterns on the river and one subject in every salon. This Chronicle won't tell you what it is, because you already know.*

- **The Queen at the river** (texto del desenlace)
- **The hammer in the gardens** (texto del desenlace)
- **Two in a boat** (texto del desenlace)
- **Curtsies** (texto del desenlace)
- **Printer wanted**: This Chronicle offers ten crowns to whoever can say where the Unsigned Sheet is printed. Not out of jealousy: out of professional interest.
- **Lanterns to spare**: The chandlers on the Street of Seals ran out of candles on Friday. They say someone bought forty at once, and paid in copper.

*The Chronicle signs everything it prints. Even this.*

## The Unsigned Sheet · nº 2

*Eighty years ago the Archive burned. Not all of it.*

Pages of the Threshold Pact survived, the document given up for lost that night. Some houses know it, because they bought them. Others fear it, because they are named in them.
- si `marca(cofre_para_archivo)`: This week a chest of burned papers went back to the Archive, and Valcenda applauded. Interesting. Why did nobody ask what was missing from it?
- si `no marca(cofre_para_archivo)`: This week someone paid three times over for a chest of burned papers. Interesting. Why pay so much for ash?

*— Folio 81, which follows where we left off.*

## Sólo para sus ojos

- si `marca(pista_sello_umbral)`: You sketch the chest's seal from memory: an open door inside a circle. You slip it between the pages of Sheet no. 2. It fits far too well.
- si `marca(pujador_miraves)`: Amalia Miravés wanted those papers. Dario's aunt buys nothing she doesn't need.
- si `marca(pista_taller_arcos)`: A workshop in Arcos Bajos with its press running at midnight and sheets hung up to dry. And a figure in clerk's sleeves.
- si `marca(pista_mala_impresion) y marca(pista_taller_arcos)`: Mara was right: the Sheet doesn't come from her presses, which print clean. It comes from an old press, run by someone who isn't a printer.
- si `marca(catalejo_maren)`: The Maréns paid out on the Clara de Nácar without a quarrel, and now they've bought her captain's spyglass. Isolda knows nothing. Or so it seems.
- si `marca(reina_interes) o marca(reina_conmovida)`: The Queen also believes something didn't burn. If so, the season doesn't end at a ball: it ends at the Archive.
- si `semana == 3`: Halfway through the season. Your young people have begun to speak familiarly in corners. You have begun to trust no one.

## Gancho

- **nota**: Madam: the Queen let slip at the palace that someone among your eight knows more about the Archive than they say.
- **nota**: And another thing. The gala at the theatre is on the 20th, under a full moon. Nilo has asked twice what time the performance ends.
