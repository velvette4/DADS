label show_date:
    # Display the current date
    $ current_date = calendar.get_date()
    
    # Check for special event
    if calendar.current_day == 3 and calendar.seasons[calendar.current_season_index] == "Spring":
        jump spring3
    else:
        jump activity

label activity:
    #$ inventory = {"blood lotus": 2} use this to set the number of seeds
    "what do you want to do?"
    menu gardening_choice:
        "plant":
            call screen farming

        "Go to Bartrand's Books":
            jump varricm1_1
            
        "sell":
            jump sell_menu
        "go to sleep":
            $ calendar.next_day()
            $ a1watered = False
            $ a2watered = False
            $ a3watered = False
            $ b1watered = False
            $ b2watered = False
            $ b3watered = False
            $ c1watered = False
            $ c2watered = False
            $ c3watered = False
            $ d1watered = False
            $ d2watered = False
            $ d3watered = False
            $ e1watered = False
            $ e2watered = False
            $ e3watered = False
            $ f1watered = False
            $ f2watered = False
            $ f3watered = False
            jump show_date

label farming_start:
    call screen farming