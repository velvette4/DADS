screen seeds_inventory():
    tag menu
    add "images/seeds_inventory_bg.png"  # Optional background for seed inventory

    vbox:
        spacing 10
        xalign 0.5
        yalign 0.5

        # Show available seeds
        for item_name, quantity in inventory.items():
            if quantity > 0 and not item_name == "fertilizer":  # Filter for seeds
                hbox:
                    spacing 10
                    text f"{item_name}: {quantity}"  # Display seed name and quantity

                    # Select button
                    textbutton "Select":
                        action [
                            SetVariable("current_seed", item_name),
                            SetVariable("planting_mode", True),
                            Hide("seeds_inventory")
                        ]
                        # Tooltip or indicator
                        hovered Notify(f"Selected {item_name} for planting.")

            elif quantity > 0 and item_name == "fertilizer":
                hbox:
                    spacing 10
                    text f"{item_name}: {quantity}"  # Display seed name and quantity

                    # Select button
                    textbutton "Select":
                        action [
                            SetVariable("current_fertilizer", item_name),
                            SetVariable("fertilizer_mode", True),
                            Hide("seeds_inventory")
                        ]
                        # Tooltip or indicator
                        hovered Notify(f"Fertilizer.")

    # Close button
    textbutton "Cancel":
        action[
            Hide("seeds_inventory"),
            Show("farming"),
        ]