label varricm1_1:
    scene bookstore
    "You enter the bookshop. The room is quiet and filled with bookshelves so closely packed you nearly need to turn sideways to pass between them."
    "They are filled to the brim with books, some laying horizontally atop others simply because there isn't enough space to display them all."
    "Further within the shop, there's the clicking of someone typing on a keyboard, then a sigh, followed by the irritated sound of someone repetitively hitting the backspace with mounting frustration."
    "You move around a step stool beside one of the shelves to find the source of the noise, assuming it to be the Bertrand that the sign referenced outside."
    "A Dwarf stands at the counter, glaring at a laptop's screen. He doesn't seem to notice you, as focused as he is on whatever he's writing."
    show v_angry
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
    hide v_angry
    show v_surprise
    v "Did you plan on staring all day, or were you going to say something?"

label varricm1_3:
    s "Could you help me find something?"
    hide v_angry
    show v_happy
    v "Course. How can I help you out?"
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
    return