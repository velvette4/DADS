label show_date:
    # Display the current date
    $ current_date = calendar.get_date()
    
    # Check for special event
    if calendar.current_day == 3 and calendar.seasons[calendar.current_season_index] == "Spring":
        jump spring3
    else:
        jump activity

label activity:
    $ inventory = {"blood lotus": 2}
    "what do you want to do?"
    menu gardening_choice:
        "plant":
            call screen farming
            
        "sell":
            jump sell_menu
        "go to sleep":
            $ calendar.next_day()
            $ watered = False
            jump show_date

label farming_start:
    call screen farming