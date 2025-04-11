label varricm1_1:
    scene bb
    "You enter the bookshop. The room is quiet and filled with bookshelves so closely packed you nearly need to turn sideways to pass between them."
    "They are filled to the brim with books, some laying horizontally atop others simply because there isn't enough space to display them all."
    "Further within the shop, there's the clicking of someone typing on a keyboard, then a sigh, followed by the irritated sound of someone repetitively hitting the backspace with mounting frustration."
    "You move around a step stool beside one of the shelves to find the source of the noise, assuming it to be the Bertrand that the sign referenced outside."
    "A Dwarf stands at the counter, glaring at a laptop's screen. He doesn't seem to notice you, as focused as he is on whatever he's writing."       
    show varric
    u "Maferath's balls…"
    
    menu:
        "Say nothing.":
            jump varricm1_2
        "Ask him if he can help.":
            jump varricm1_3

label varricm1_2:
    "You watch as he runs a hand over his face. His eyes don't move from the hole he's boring into the screen."
    "The laptop is older, though it might have been top of the line when it was new. There's a sticker stuck to the front you can't make out at this angle."
    "Behind him, mounted on the wall, is an out of place crossbow. Its design looks entirely unique and it must be cherished, judging by its condition and place of honor."
    "There's a plush armchair on your side of the counter. A side table with a red lamp sits beside it."
    "The Dwarf suddenly snaps the laptop shut. Upset, but still being delicate with the machinery."
    "He looks up and glosses over you before he seems to realize your presence and startles."
    v "Did you plan on staring all day, or were you going to say something?"
    jump varricm1_3

label varricm1_3:
    s "Could you help me find something?"
    v "Course. How can I help you out?"
    hide varric
    show varrichappy
    "He braces his hands on the counter, presenting himself as open and friendly."
    "He's an older man, and his smile is as boxy as his build. Something about him makes you want to trust him instinctively."
    s "I'm looking for a guide on farming. Or gardening. Or how to just keep a plant alive for more than two days."
    "The man laughs and it fills the small shop with noise. He begins to move around the counter."
    v "Not from around here, are you?"
    s "I just moved in."
    "You follow him as he goes around you to the shelves. He takes a knee as he rolls his eyes over the spines of the books."
    v "What made you come here? Can't be the bustling nightlife."
    "He chuckles to himself."
    s "It's a long story."
    v "Those are my favorite, personally."
    "He pulls out a book and stands. When he hands it to you, you see that the title is {color=#6200ff}{i}'Idiot's Guide to Farming'{/i}{/color}."
    v "Think that should get you started for now. I'd talk to Harding before you actually start routing around in the mud, though."
    s "Harding?"
    v "She'll sell you seeds and tools so you aren't digging with your bare hands."
    "He turns to the side to look out the front window. He points to a farmhouse in the distance. "
    v "Tell her I sent you. She's a good kid, she'll help you."
    "He shrugs, and his grin says the two have a storied history. "
    v "Might talk your ear off, but you'll get a lot of that here. Seeker tells me I don't know what 'silence' means."
    s "I'll talk to her, thank you. The book?"
    "You hold up the book to him. There's no price tag on either cover. He waves a hand."
    v "Don't worry about it. Consider it a housewarming gift. Welcome to town."
    s "Thank you, Bartrand."
    "He laughs again, harder this time. He shakes his head and waves a hand at your embarrassment."
    v "No, no. Bartrand's my brother."
    "He sighs as he collects himself. He crosses his arms over his chest."
    v "I'm sure he's rolling in his grave as we speak. I'm Varric."
    menu:
        "Why do you call it Bartrand's Books, then?":
            jump varricm1_4

        "Thank you, Varric.":
            jump varricm1_5

label varricm1_4:
    s "Why do you call it Bartrand's Books then?"
    v "Alliteration sells, Sprout. Plus…"
    "His grin turns mischievous."
    v "He would absolutely hate it." 
    "You can't help but snort. Varric seems to take that as the highest compliment."
    jump varricm1_5

label varricm1_5:
    s "Thanks, Varric."
    v "Don't sweat it, Sprout. I'll have the sequel ready for you when you get through that one."
    s "I'll go talk to Harding now."
    "He strolls over to the door with you, holding it open for you. He leans against it, the very picture of casual."
    v "Tell her I'll see her at lunch." 
    "You nod and start to head in the direction of the farmhouse before you stop and look back at him." 
    s "{color=#008000}'Sprout'{/color}?" 
    v "Consider it your other house warming gift." 
    "He gestures at you, as though that explains anything."
    v "Sprang up out of nowhere, green as can be." 
    "He winks and speaks in a conspiratorial stage whisper."
    v "It'll grow on you, Sprout."
    $ varricm1 = True
    jump show_date

# Varric Friendship1
    label varricf1_1:
        $ varricf1 = True
        python:
            remove_gift("Hawk Feather", 1)
        scene bbnight
        "Varric turns the feather in his fingers, examining the stripes running down it."
        "The fibers fold and bend easily to his touch. The feather is long and soft, surely from the bird's wing."
        "His expression is odd, more affected than you anticipated him being. He almost looks like he's seen a ghost."
        show varricshock
        v "Is this…?"
        s "It's a hawk feather. I found it out in the coop."
        "He looks at you like he's waiting for a punchline."
        v "And you're giving it to me?"
        menu: 
            "You don't have to keep it.":
                $ varricheart -= 5
                jump varricf1_2
            "I thought of your book when I saw it.":
                jump varricf1_3

    label varricf1_2:
        scene bbnight
        show varric
        s "You don't have to keep it."
        "His gaze drops back to the feather for a moment before he shakes his head."
        "He tucks the feather into his pocket as he speaks, putting on a casual air."
        v "No, no. You went through the effort of bringing it here."
        hide varric
        show varrichappy
        v "Would be rude to look a gift like this in the mouth."
        "His hand covers his own pocket, his heart, tapping it with his fingertips."
        v "Thanks for thinking of me, Sprout."
        jump show_date


    label varricf1_3:
        s "I thought of your book when I saw it."
        hide varricshock
        show varrichappy
        v "You read {color=#6200ff}{i}'Tale of the Champion'{/color}{/i}? "
        "He sounds doubtful, yet you can see the start of a smile creeping onto his face."
        menu:
            "I skimmed it.":
                pass
            "I might have.":
                pass
        
        "He laughs and hangs his head. One of his thumbs is still running up the spine of the feather in a soothing motion."
        v "'Course you did."
        s "Did all of that really happen?"
        "He sighs as he tucks the feather into his shirt pocket with his glasses. He shrugs."
        v "Depends on who you ask. I am prone towards extravagant lies."
        menu:
            "You were different in the book.":
                jump varricf1_4
            "You two were really close.":
                $ varricheart += 5
                jump varricf1_5

    label varricf1_4:
        s"You were different in the book."
        "He chuckles again, crossing his arms over his chest."
        hide varric
        show varrichappy
        v"It's my book. I'm entitled to a little embellishment."
        s "I find it hard to believe you won a fight against six guys."
        "He arches a brow, making a dastardly expression when paired with his smile."
        v "Don't think I can take care of myself, Sprout?"
        menu:
            "You should have said it was a dozen men.":
                jump varricf1_8

            "It just seemed unrealistic to me.":
                $ varricheart -= 5
                jump varricf1_9

    label varricf1_8:
        s "You should have said it was a dozen men."
        v "You flatter me, Sprout."
        s "Seriously. One guy against twelve dusters armed to the teeth."
        s "It would make a great scene."
        v "Think you could have written it better?"
        "You can tell it's a trick question. He's not trying to hide that fact."
        "You meet his challenge with a smirk of your own.You cross your arms."
        s "Just think I'd have some notes if I was your editor."
        "Varric laughs and reaches across the counter to smack your arm in a friendly gesture." 
        v "Over your dead body."
        s "Over {i}{b}their{/i}{/b} dead bodies. When you fill them with arrows. Like a pin cushion." 
        s "You're gonna make me blush."
        "His tone is sardonic and sweet as honey. It sticks to your bones and you giggle involuntarily at the warm feeling in your chest."
        $ varricf1 = True
        jump show_date

    label varricf1_9:
        s "It just seems unrealistic to me."
        "He holds up his hands in surrender."
        hide varric
        show varric
        v "Hey, I'm not asking you to believe it."
        v "I'm just saying that's how it happened."
        s "I can see how you got out of trouble when you talk like that." 
        hide varric
        show varrichappy
        v "Devilish good looks do help as well." 
        "You cross your arms as you smirk, quirking a brow."
        s " We're still talking about you?" 
        "Varric scoffs and turns away from you. He waves you off like a bothersome fly." 
        v "Get out of here, kid." 
        $ varricf1 = True
        jump show_date


    label varricf1_5:
        s "You were really close." 
        hide varrichappy 
        show varric
        "His smile falters. His gaze turns distant as he looks somewhere past your feet."
        "He licks his lips and nods."
        v "Yeah, we were."
        "His smile returns, along with his eyes on you. There's something behind them, however. A hidden sorrow."
        hide varric
        show varrichappy
        v "We were the only ones who could stand each other."
        s "What happened to them?"
        hide varrichappy
        show varric
        v "You read the book. Think you know the answer to that."
        s "They just left?"
        "Varric shrugs. His gaze slides away from you for a moment."
        "It returns the very next moment with a shift in the air. Something had happened just beyond your line of sight, like a wall had suddenly been erected when you weren't looking." 
        hide varric
        show varrichappy
        v "Well, they certainly couldn't have stayed."
        s "Where did they go?"
        hide varric
        show varrichappy
        "Varric chuckles, shaking his head." 
        v "If I told you that, it would ruin the ending."
        v "That's for the reader to decide." 
        menu:
            "Where do {i}you{/i} think they went?":
                jump varricf1_6
            "I'll get it out of you someday.":
                jump varricf1_7

    label varricf1_6:
        s "Where do {i}you{/i} think they went?"
        "Varric clicks his tongue and wags a finger in your direction."
        v "Nice try, Sprout."
        v "That's for me to know, and the rest of you to theorize."
        $ varricf1 = True
        jump show_date

    label varricf1_7:
        s "I'll get it out of you someday."
        s "Just wait."
        "Varric laughs, louder and brighter than all the little chuckles before."
        "He leans over the countertop, over his crossed arms. You can see the feather just peeking out of his pocket."
        v "I'll have to hold you to that, y'know."
        s "I mean it."
        v "Oh, I know you do."
        "He holds your eye for a moment, almost like he's searching for something."
        hide varrichappy
        show varric
        v "Maybe I should have went with 'dandelion' instead."
        v "Stubborn as a weed."
        $ varricf1 = True
        jump show_date




