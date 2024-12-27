label show_date:
    # Display the current date
    $ current_date = calendar.get_date()
    
    # Check for special event
    if calendar.current_day == 3 and calendar.seasons[calendar.current_season_index] == "Spring":
        jump spring3
    else:
        jump activity

label activity:
    $ inventory_string = get_inventory_string()
    # Add an item
    $ add_item("blood lotus", 2)
    $ add_item("elfroot", 3)
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