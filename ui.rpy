screen money_display():
    frame:
        align (0.95, 0.05)  # Position it in the top-right corner
        padding (10, 10)  # Correct padding as a tuple (left, top)
        background "#0008"  # Semi-transparent background
        text "Money: $[player_money]" size 22 color "#FFFFFF"
        for item_name, quantity in inventory.items():
            text f"{item_name}: {quantity}"

screen calendar_ui():
    frame:
        align (0.02, 0.02)  # Position the UI (top-left corner)
        background "#0008"  # Semi-transparent background
        padding (10, 10)  # Correct padding as a tuple (left, top)
        vbox:
            spacing 5
            text "Date: [calendar.get_date()]" color "#fff" size 20
            # Check for special event and display it on the UI
            if calendar.current_day == 3 and calendar.seasons[calendar.current_season_index] == "Spring":
                text "Event: Spring Festival 🎉" color "#ff0" size 18