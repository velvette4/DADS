# Seed selection buttons
screen inventory:
    vbox:
        # Debugging: Output the inventory count for each item
        text "Inventory count: cheese = [inventory.count('cheese')], elfroot = [inventory.count('elfroot')], royal elfroot = [inventory.count('royal elfroot')], blood lotus = [inventory.count('blood lotus')]"
        
        # Define a list of available seeds and their corresponding images
        $ seeds = [
            ("cheese", "images/seeds/cheese_seeds.png", "images/seeds/cheese_seeds_hover.png"),
            ("elfroot", "images/seeds/elfroot_seeds.png", "images/seeds/elfroot_seeds_hover.png"),
            ("royal elfroot", "images/seeds/royal_elfroot_seeds.png", "images/seeds/royal_elfroot_seeds_hover.png"),
            ("blood lotus", "images/seeds/blood_lotus_seeds.png", "images/seeds/blood_lotus_seeds_hover.png")
        ]

        # Iterate through the seeds and display a button if the seed is available in the inventory
        for seed, idle_img, hover_img in seeds:
            if inventory.count(seed) > 0:
                imagebutton:
                    idle idle_img
                    hover hover_img
                    action [
                        SetVariable("current_seed", seed),
                        Hide("inventory"),
                        ToggleVariable("planting_mode"),
                    ]  # Set planting mode to selected seed

        textbutton "Close Inventory" action Hide("inventory")


screen getseeds:
    textbutton "Get Seeds":
        action[
            Function(inventory.add_item, ("blood lotus", 3)),
            Function(inventory.add_item, ("elfroot", 3)),
        ]