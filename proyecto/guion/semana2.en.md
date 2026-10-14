# Semana 2 · First impressions

**Autumn reckonings.** The autumn debts fall due. Houses that owe money smile more than usual and spend less than they pretend.

## Apertura

- **nota**: Madam: the unsigned envelope is still on your desk. Folio 80, the Census Night bundle.
- **nota**: You could ask at the Archive, discreetly. Or keep it and wait for whoever wrote it to write again.
- Opción **Ask discreetly at the Archive** → A clerk tells you that bundle “isn't lent out.” Then he lowers his voice: “Though someone asked for it a month ago. Someone from inside.”
- Opción **Keep it and wait** → You keep it with the other letters. If whoever wrote it wants something from you, they'll write again.

## Peticiones

- **teo** pide `s2_molinos`: Teo: “My father is opening the mills this week. If someone from your cast goes, the whole riverbank will talk about the Rovenas. If no one goes, so will they.”
  - Si se cumple: Teo sends you a note with a single line of verse: “Thank you, and don't let my pride find out.”
  - Si no: Teo says nothing. It's the first time he hasn't made a joke about something.
- **isolda** pide `s2_cena_salvat`: Isolda, very quietly: “If… if there were a free seat at the dinner on the Street of Seals, I'd like to go. Only if there's one spare.”
  - Si se cumple: Isolda thanks you three times and wears a new feather in her hair. She doesn't explain why that dinner.
  - Si no: Isolda says she understands perfectly. She says it too quickly.

## A day at the mills · día 4 · muelles
*paseo · plazas 2–4 · cualquiera*

> Two days upriver, among waterwheels and lunches in the sun. The Rovenas want to be talked about, and kindly.

Requisito: presencia 5, estatus 4, intelecto 5
- \+ Two days together bring the guests much closer
- − The sky threatens rain, and the riverbank turns to mud
- − Whoever goes can't attend anything else on Thursday or Friday

**Carta**

*Distinguished Matchmaker,*

The Rovena mills have ground the grain Valcenda eats for three generations. This autumn we open their doors for two days: boats, lunch beside the wheels and a simple supper at the river house. My son insists your young people will enjoy themselves. I insist they talk about it afterwards.

*Aurelio Rovena*

**Incidente (día 5)** · It's raining. Under the eaves, a group of tenants waits for Mr Rovena: they're owed two months' wages. The guests are watching.

- **Go over to the tenants and listen to them** (presencia, d 5)
  - Éxito: {mejor} listens to them in the rain without hurrying them. When Rovena arrives, there's no more shouting: there's a payment date.
  - A medias: The tenants calm down, more or less. One of them keeps glaring at the guests.
  - Fallo: {mejor} can't find the words. The shouting reaches the dining room.
- **Go through the mill's accounts with the steward** (intelecto, d 5)
  - Éxito: The accounts half add up: the mills make money, but a debt to the Miravés eats the harvest advances. There's money for the wages if something else waits.
  - A medias: The steward shows some accounts and hides others. Something doesn't add up, and {mejor} notices.
  - Fallo: The steward takes offence. Rovena finds out someone has looked at his books.
- **Distract the guests with a good story by the fire** (chisme, d 4)
  - Éxito: By the fire, {mejor} tells a story so good that nobody looks out of the window.
  - A medias: The story works until someone asks about the shouting outside.
  - Fallo: The story falls apart halfway. Everyone looks out of the window at once.

**Indisposición (días [6, 7])** · asistente de s2_molinos que también esté en s2_baile_casas, el de Presencia más baja: {a} came back from the mills with a fever. Bruna says {a|he|she} won't be up before Monday.

**Reemplazo en `s2_baile_casas`** · {a} won't be able to dance on Sunday. The ball is required: someone must take {a|his|her} place.
- Send someone else in {a|his|her} place
- Go with one couple fewer
- Send apologies to the hosts
- resultado_reducir: A single couple will dance for your house. The gap will show, but not as much as an empty chair.
- resultado_retirar: The houses receive your apologies. They accept them aloud and discuss them under their breath.

**Desenlace · favorable** — Two days upriver
- publico: The Rovenas' guests came back from the mills delighted, muddy and full of stories. The riverbank is speaking well of the house, for once.
  - si `asiste(teo)`: Teo Rovena showed off his family's mills with a pride no one knew he had. Some forgot he'd ever joked about them.
- privado: Aurelio Rovena wrote you a thank-you letter far too long for a man who says he has no time.
  - si `opcion(s2_molinos) == cuentas`: You now know the Rovena mills owe money to House Miravés. Teo doesn't know. Or he pretends very well.

**Desenlace · medias** — Mud and goodwill
- publico: The day at the Rovena mills was pleasant whenever it wasn't raining. It rained a good deal.
- privado: Teo asks you, as if in passing, whether anyone mentioned the wages. You don't answer. He doesn't press.

**Desenlace · desaire** — Shouting in the rain
- publico: At the Rovena mills, the tenants demanded their wages in front of the guests. The Chronicle regrets not being there; it already has three versions.
- privado: Teo hasn't written to you since. His father has: to say never again.

## Supper on the Street of Seals · día 6 · archivo
*cena · plazas 2–3 · cualquiera*

> The Salvat family receives guests at home, above the Archive's stores. People talk quietly, out of habit.

Requisito: intelecto 5, chisme 5, estatus 3
- \+ Here people really know who owes what to whom
- − Conversations are long and nobody dances

**Carta**

*Dear Madam,*

My daughter Irene assures me you are someone to be trusted, and my daughter is almost never wrong. On Saturday we dine at home, above the stores. There's no music and no mirrors: there's good wine and better papers. Bring whoever knows how to listen. On this street, those who listen, learn.

*Tomás Salvat*

**Incidente (día 6)** · An old clerk, a little drunk, mentions that someone requested the Census Night bundle a month ago “and brought it back lighter.” Irene sets her glass down.

- **Coax the clerk into saying who asked for it** (chisme, d 5)
  - Éxito: The clerk doesn't remember the name, but he does remember the handwriting in the register: “Small, very neat. Someone from here.”
  - A medias: The clerk starts to tell it and Tomás Salvat pours him more wine so he'll forget.
  - Fallo: The question sounds like an interrogation. The table falls silent.
- **Ask, with a scholar's interest, to see the lending register** (intelecto, d 5)
  - Éxito: Tomás Salvat shows the register with an archivist's pride. On the bundle's line the signature has been struck out; the date is written in small, very neat handwriting.
  - A medias: They're shown the register, but the bundle's page is folded over. Nobody dares unfold it at the table.
  - Fallo: Tomás Salvat smiles and says the books don't leave the work table. The conversation moves on.
- **Gracefully change the subject, out of courtesy to the hosts** (presencia, d 4)
  - Éxito: A toast to daughters who learn their parents' trade. Irene raises her glass and, for a moment, looks at {mejor} with relief.
  - A medias: The subject changes, but the clerk keeps muttering in his corner.
  - Fallo: The toast comes too late and sounds as if everyone is hiding something.

**Desenlace · favorable** — Wine and good papers
- publico: {grupo} dined with the Salvats on the Street of Seals. They say the talk was of history until midnight, and nobody was bored.
  - si `asiste(isolda)`: Miss Marén, so quiet, asked a question about the port records that silenced the whole table. Irene Salvat answered it for half an hour.
- privado: On parting, Irene sends you a two-line note: “Come back. On this street people listen better than in ballrooms.” The handwriting is small and very neat.
  - si `asiste(isolda) y asiste(irene)`: Isolda and Irene stayed talking on the stairs after everyone had left. Isolda came back without the feather in her hair. She didn't seem to mind.

**Desenlace · medias** — A quiet supper
- publico: {grupo} dined with the Salvats. It was a serious supper, on a serious street.
- privado: Tomás Salvat saw them to the door and checked the street before closing it. Left and right.

**Desenlace · desaire** — Too many questions
- publico: Word is that at the Salvats' someone asked what they shouldn't. Archivists will not soon forget it.
- privado: Irene didn't return your greeting this morning. She saw you. She decided not to.

## The Houses' Ball · día 7 · salon
*baile · plazas 4–4 · parejas · OBLIGATORIO*

> Every house presents its young people at the Hall of Columns. You present two couples, and Valcenda decides who shines.

Requisito: baile 5, estatus 4, presencia 5
- \+ Dancing together draws people twice as close as a supper
- − Houses in debt will be watching who dances with whom

**Carta**

*To the Matchmaker of the Season,*

As every autumn, the houses will open the Hall of Columns for the first great ball. Two couples are yours in the second waltz. May I remind you, with all respect, that the Queen will read Monday's Chronicle. Houses Lobreda and Veyra have asked for neighbouring tables. Don't ask why; you already know.

*Mireya, Keeper of the Lists*

**Incidente (día 7)** · As the second waltz begins, printed sheets appear on the tables, unsigned. The whole hall reads at once. Some glance at {a} and {b}.

- **Keep dancing as if nothing had happened** (baile, d 5)
  - Éxito: Both couples keep the waltz without losing the beat. By the third turn, the hall is watching the dance again, not the sheets.
  - A medias: One couple loses the step for a moment. Just long enough for someone to note it down.
  - Fallo: The waltz falls apart. The couples stand still in the middle of the hall, reading like everyone else.
- **Ask the hosts to gather up the sheets** (estatus, d 5)
  - Éxito: The servants gather the sheets before the third waltz. The ones left travel hidden in gloves, which looks worse for those reading them.
  - A medias: Half are gathered. The other half are already in pockets.
  - Fallo: The request comes too late and reads as fear. What does the Matchmaker have to hide?
- **Find out who left the sheets** (chisme, d 4)
  - Éxito: Nobody saw who left them, but {mejor} notices the paper: stitched quire, edge trimmed off. Discard paper, the kind clerks use.
  - A medias: A servant swears the sheets arrived in a flower basket. The flowers came from the florist on the Street of Seals.
  - Fallo: The question spreads faster than the sheets. Now everyone suspects everyone.

**Desenlace · favorable** — The second waltz, the finest
- publico: Not even the unsigned sheets could spoil the second waltz: {grupo} danced as if they owned the hall. The Chronicle can't recall a first ball so talked about.
  - si `asiste(saul) y asiste(celia)`: Saúl Veyra and Celia Lobreda danced together again. The Lobreda and Veyra tables toasted at the same moment. Nobody says “rumour” now: they say “when.”
  - si `asiste(dario) y asiste(celia)`: Dario Miravés and Celia Lobreda, again. Valcenda is starting to speak of them like a piece of music: as a pair.
  - si `asiste(teo) y asiste(irene)`: Teo Rovena danced with Irene Salvat and, for once, made no jokes. She corrected his step twice. He thanked her both times.
- privado: Mireya sends you a note: “Her Majesty asked for the Chronicle before breakfast.”

**Desenlace · medias** — An interrupted ball
- publico: The Houses' Ball had two stars: the second waltz, which was proper, and some unsigned sheets, which were something else.
- privado: On the way out, you find a sheet on the seat of your carriage. Someone wanted to make sure you read it.

**Desenlace · desaire** — The ball of the sheets
- publico: All anyone will remember of the Houses' Ball is the scandal, and {grupo} standing frozen in the middle of the hall.
- privado: The Queen didn't ask for the Chronicle. Mireya says that's worse.

**Desenlace · sin_asistentes**
- publico: The Matchmaker presented no couples at the Houses' Ball. The other houses danced longer, and talked about her between waltzes.

## The Salon Chronicle · Issue 2 · Printed by Calce, Street of Seals

*A week of reckonings, a week of smiles. People never dance so well as when they owe money.*

- **The second waltz** (texto del desenlace)
- **A sheet without manners**: This Chronicle does not know who printed the sheet that circulated on Sunday, and regrets it: we'd have liked to hire them. We regret their lack of a signature even more.
- **Wheels and rain** (texto del desenlace)
- **Street of Seals** (texto del desenlace)
- **What was said at the printing house**: A guest at our reading evening confided to us the name of the season's match. We publish it with pleasure. If it isn't true, it soon will be.
- **Reckonings**: Three houses sold horses this week and none admits it. The stables of Alto Laurel are emptier than their promises.

*The Chronicle signs everything it prints. Let that be noted.*

## The Unsigned Sheet · nº 1

*Valcenda keeps its secrets in drawers. We keep the keys.*

Secreto según quién tenga más fama:
- **nilo**: Young Lobreda helps everyone. Ask at the Greda pass who pays the winter relief his house has owed for two years.
- **saul**: Captain Veyra refused two engagements before this season. His family says it was duty. Why does nobody ask why?
- **dario**: The Miravés heir has attended eleven outdoor parties in three years. He has arrived at every one as the sun was setting.
- **teo**: The Rovena mills haven't paid their tenants in two months. The house's wit doesn't stretch to wages.
- **celia**: Miss Lobreda rehearses every night with a dancing master her branch of the family cannot afford. Who pays?
- **irene**: An archivist was seen in the Archive's stores after midnight. The Archive says it's impossible. The Archive says many things.
- **isolda**: Two autumns ago, House Marén paid out on a sunken ship without a quarrel. Nácar insurers never pay without a quarrel. Why does Miss Marén turn pale whenever someone mentions the “Clara de Nácar”?
- **camila**: The widow Ferrán smiles a great deal for someone with a debt due this autumn. Ask House Miravés about the “Clara de Nácar.”

*Why does everyone read it and no one ask whether it's true? — Bundle 80.*

## Sólo para sus ojos

- si `marca(pista_letra_registro) y marca(sobre_guardado)`: You compare the handwriting on the unsigned envelope with what you were told about the register: small, very neat. It isn't proof. It's a coincidence that won't let you sleep.
- si `marca(pista_papel_descarte)`: You keep a copy of the Sheet next to last week's envelope. The paper comes from the same stitched quire.
- si `marca(deuda_rovena_vista)`: The Rovena mills owe money to the Miravés. Teo hasn't said so. Neither has Dario.
- si `marca(irene_agradecida)`: Irene sends you a book with no note. It's a history of the Archive before the fire. One page is folded down: the one about folio 80.
- si `semana == 2`: First week of reckonings, first Sheet. Someone in Valcenda has decided this season won't be only about dancing.

## Gancho

- **nota**: Madam: Mara Calce has called twice. She wants to know if you know who printed the Sheet. I told her no. Did I do right?
- **nota**: The Queen is coming down to the river next week, for the Lanterns. They say she hasn't done so since she was a girl.
