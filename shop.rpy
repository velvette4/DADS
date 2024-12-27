label sell_menu:
    menu:
        "Sell Cheese" if has_item("Cheese"):  # Corrected to add a colon
            jump sell_Cheese
        "Sell Elfroot" if has_item("Elfroot"):  # Corrected to add a colon
            jump sell_Elfroot
        "Sell Blood Lotus" if has_item("Blood Lotus"):  # Corrected to add a colon
            jump sell_blood_lotus
        "Sell Royal Elfroot" if has_item("Royal Elfroot"):  # Corrected to add a colon
            jump sell_Royal_Elfroot
        "Do nothing":  # Added this as an alternative
            jump activity


label sell_Cheese:
    # Define the price per item
    $ price_per_Cheese = 10

    # Ask how many the player wants to sell
    $ max_sell = inventory["Cheese"]
    "You have [max_sell] Cheese. Each Cheese is worth $[price_per_Cheese]. How many do you want to sell?"

    # Show a menu for the player to choose the action
    menu:
        "Proceed with the sale":
            $ sell_amount = renpy.input("Enter the amount to sell:")

            # Convert the input to an integer and validate
            $ sell_amount = int(sell_amount) if sell_amount.isdigit() else 0
            if sell_amount > 0 and sell_amount <= max_sell:
                $ total_earnings = sell_amount * price_per_Cheese
                "You sold [sell_amount] Cheese for $[total_earnings]!"
                $ inventory["Cheese"] -= sell_amount
                $ player_money += total_earnings  # Increase the player's money
                jump activity
            else:
                "You don't have that much Cheese to sell."
                jump sell_Cheese

        "Cancel":
            "You chose not to sell anything."
            jump activity


label sell_Elfroot:
    # Define the price per item
    $ price_per_Elfroot = 15

    # Ask how many the player wants to sell
    $ max_sell = inventory["Elfroot"]
    "You have [max_sell] Elfroot. Each Elfroot is worth $[price_per_Elfroot]. How many do you want to sell?"

    # Show a menu for the player to choose the action
    menu:
        "Proceed with the sale":
            $ sell_amount = renpy.input("Enter the amount to sell:")

            # Convert the input to an integer and validate
            $ sell_amount = int(sell_amount) if sell_amount.isdigit() else 0
            if sell_amount > 0 and sell_amount <= max_sell:
                $ total_earnings = sell_amount * price_per_Elfroot
                "You sold [sell_amount] Elfroot for $[total_earnings]!"
                $ inventory["Elfroot"] -= sell_amount
                $ player_money += total_earnings  # Increase the player's money
                jump activity
            else:
                "You don't have that much Elfroot to sell."
                jump sell_Elfroot

        "Cancel":
            "You chose not to sell anything."
            jump activity

label sell_blood_lotus:
    # Define the price per item
    $ price_per_blood_lotus = 25

    # Ask how many the player wants to sell
    $ max_sell = inventory["Blood Lotus"]
    "You have [max_sell] Blood Lotus. Each Blood Lotus is worth $[price_per_blood_lotus]. How many do you want to sell?"

    # Show a menu for the player to choose the action
    menu:
        "Proceed with the sale":
            $ sell_amount = renpy.input("Enter the amount to sell:")

            # Convert the input to an integer and validate
            $ sell_amount = int(sell_amount) if sell_amount.isdigit() else 0
            if sell_amount > 0 and sell_amount <= max_sell:
                $ total_earnings = sell_amount * price_per_blood_lotus
                "You sold [sell_amount] Blood Lotus for $[total_earnings]!"
                $ inventory["Blood Lotus"] -= sell_amount
                $ player_money += total_earnings  # Increase the player's money
                jump activity
            else:
                "You don't have that much Blood Lotus to sell."
                jump sell_blood_lotus

        "Cancel":
            "You chose not to sell anything."
            jump activity

label sell_Royal_Elfroot:
    # Define the price per item
    $ price_per_Royal_Elfroot = 40

    # Ask how many the player wants to sell
    $ max_sell = inventory["Royal Elfroot"]
    "You have [max_sell] Royal Elfroot. Each Royal Elfroot is worth $[price_per_Royal_Elfroot]. How many do you want to sell?"

    # Show a menu for the player to choose the action
    menu:
        "Proceed with the sale":
            $ sell_amount = renpy.input("Enter the amount to sell:")

            # Convert the input to an integer and validate
            $ sell_amount = int(sell_amount) if sell_amount.isdigit() else 0
            if sell_amount > 0 and sell_amount <= max_sell:
                $ total_earnings = sell_amount * price_per_Royal_Elfroot
                "You sold [sell_amount] Royal Elfroot for $[total_earnings]!"
                $ inventory["Royal Elfroot"] -= sell_amount
                $ player_money += total_earnings  # Increase the player's money
                jump activity
            else:
                "You don't have that much Royal Elfroot to sell."
                jump sell_Royal_Elfroot

        "Cancel":
            "You chose not to sell anything."
            jump activity