# Escenas del capítulo 5: besos, confesiones y acuerdos

## saul y dario · The small parlour at the residence, the fire burning low
*beso_saul_dario · beso* · si `nivel(saul, dario) >= A`

- **dario**: Tomorrow you either leave for Tiria or you stay. And I still don't know which frightens me more.
- **saul**: This is what frightens me.
- **narración**: Saúl takes off his gloves, slowly, one and then the other. This time he doesn't lay them on the table: he lets them fall.
- **narración**: Dario is the one who moves closer. Saúl is the one who doesn't step away.
- **narración**: When Bruna comes in to stoke the fire, it's no longer needed.

> 

## irene y isolda · The Archive reading room, at night
*beso_irene_isolda · beso* · si `nivel(irene, isolda) >= A`

- **irene**: Before anything happens, I have to tell you something. About what I do at night.
- **isolda**: Is it dangerous?
- **irene**: For others. For people who may not deserve it.
- **isolda** (ruborizada): Then tell me afterwards. Right now it's my turn to go first.
- **narración**: Isolda says nothing more. She doesn't need to: this time, she's the one who leans in.

> 

## nilo y camila · The Ferrán conservatory, at nightfall
*beso_nilo_camila · beso* · si `nivel(nilo, camila) >= A`

- **camila**: I've thrown out Julián's plants. All but one.
- **nilo**: Why that one?
- **camila** (alegre): Because it's the one you watered.
- **narración**: Nilo opens his mouth to promise something. Camila closes it before he can.
- **narración**: For once, Nilo Lobreda offers nothing. He simply stays.

> 

## teo y celia · The empty ballroom, with a single violinist
*beso_teo_celia · beso* · si `nivel(teo, celia) >= A`

- **teo**: The violinist charged me double to stay. He says this time he doesn't have to play badly.
- **celia**: And are you going to dance well?
- **teo**: No. But I'm going to stop counting the jokes.
- **narración**: They dance. Teo doesn't tread on her. Celia doesn't count. By the third turn, neither of them is dancing any more.
- **narración**: The violinist keeps playing, his back turned, with great discretion and considerable pride.

> 

## dario y celia · The Academy, beside the piano
*beso_dario_celia · beso* · si `nivel(dario, celia) >= A`

- **celia**: Play something. But properly.
- **narración**: Dario plays. Without a single false note, and so slowly he seems like someone else.
- **dario**: It's the first time I've played without anyone applauding.
- **celia** (alegre): I've no intention of applauding. I have another idea.
- **narración**: The last note goes on ringing by itself. Neither of them finishes it.

> 

## teo y irene · The Salvats' library, between the shelves
*beso_teo_irene · beso* · si `nivel(teo, irene) >= A`

- **irene**: I've read all your verses. The ones in the notebook and the ones you crossed out.
- **teo** (ruborizada): And?
- **irene**: I believe them.
- **narración**: Teo starts a joke out of habit and forgets it halfway. Irene doesn't let him remember it.

> 

## dario y isolda · The Marén office, beside the model of the harbour
*conf_dario_isolda · confesion* · si `cercania(dario, isolda) >= 10`

- **dario**: Isolda. Since we were eight, I've defended you from everyone. I think I was also defending myself from this.
- **isolda**: Dario…
- **dario**: Don't say anything. I can see it in your face. It isn't “not yet.” It's “no.”
- **isolda** (ruborizada): It isn't you. It's that I… can't love any gentleman that way. You're the first person I've told.
- **narración**: Dario is silent for a long while. Then he holds out his hand, as when they were children, to come out of hiding.
- **dario** (alegre): Then I'll go on defending you. Now I know from what.

> 

## celia y saul · The Archive's empty record room
*conf_celia_saul · confesion* · si `cercania(celia, saul) >= 10 y marca(compromiso_paso_propuesto)`

- **celia**: Captain. I signed the first page thinking it was a business matter. It isn't any more. Not for me.
- **saul**: Miss Lobreda. Celia. You deserve someone who looks at you the way you're looking at me now.
- **celia** (molesta): And you can't?
- **saul**: No. And it isn't because of you. I ask you not to question me further, and I promise I will never lie to you about it.
- **narración**: Celia counts to three under her breath. Then she stops counting.
- **celia**: Then I won't sign the last page. Not out of pride. Because I want to dance with someone who isn't counting the steps to the door.

> 

## a y b · A corner of the ballroom, at the end of the evening
*conf_generica · confesion* · si `cercania(a, b) >= 10`

- **a**: I have to say it once, even though I already know the answer. I love you more than I should.
- **b**: I know. And I'm sorry. I can't give you the same.
- **narración**: {a} nods. It hurts less than expected, and more than {a} lets on.

> 

## saul y isolda · The Veyra study, with two glasses and a contract
*acuerdo_saul_isolda · acuerdo* · si `marca(lavanda_hablada)`

- **saul**: My father wants a formal tie with the Maréns. The army wants me back in Tiria unless I marry. And I want to stay in Valcenda.
- **isolda**: My father wants a son-in-law who'll protect the convoys. And I want no one ever to ask me why I'm not in love with my husband.
- **saul**: I offer you my name, my respect, and a door you can always close.
- **isolda**: And I offer you the same. And a house where no one looks at your gloves.
- **narración**: They toast without smiling. Then they smile without toasting. It's the most honest contract ever signed at that table.
- **isolda** [si `nivel(irene, isolda) >= A`]: Saúl. There's someone. I don't want to stop seeing her.
- **saul** [si `nivel(irene, isolda) >= A`]: I know. That's what the door is for.
- **saul** [si `nivel(irene, isolda) >= A y nivel(saul, dario) >= A`]: I have someone behind mine too.

> 

## saul y celia · A palace gallery, mid-afternoon
*acuerdo_saul_celia · acuerdo* · si `marca(compromiso_paso_propuesto) y no marca(celia_rechaza_paso) y no marca(acuerdo_lavanda)`

- **celia**: Our houses have already decided. All that's left is for us to decide.
- **saul**: I'll be a proper husband. Punctual. Loyal to your house. I'll never ask you for anything you don't wish to give.
- **celia**: That's the least romantic proposal I've ever received.
- **saul**: It's the most honest one I know how to make.
- **narración**: Celia counts the steps to the end of the gallery. Twelve. She counts them twice.
- **celia**: I'll think about it until the Grand Ball. If I say yes, it won't be for my house.

> 

## teo y camila · The Ferrán sitting room, the accounts on the table
*acuerdo_teo_camila · acuerdo* · si `cercania(teo, camila) >= 6 y no marca(deuda_saldada)`

- **camila**: Your father wants to marry you to money. I have money, and a debt they want to collect twice.
- **teo**: Are you proposing marriage, Mrs. Ferrán?
- **camila**: I'm proposing a business arrangement. Your name protects me from the Miravés; my fortune saves your mills. Julián loved you like a little brother.
- **teo**: And love?
- **camila** (alegre): I had it once. Now I want someone who makes me laugh in the mornings. You're very good at that.
- **teo**: That's the most serious joke anyone's ever told me.
- **narración**: They don't say yes. Nor no. Teo takes the accounts home to read, and doesn't make a single joke on the way.

> 
