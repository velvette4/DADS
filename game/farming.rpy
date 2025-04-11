screen farming():
    add "farm"  # Background image for the farm
    textbutton "Get Seeds":
        action[
            Function(add_item, "Blood Lotus", 3),
            Function(add_item, "Elfroot", 3),
            Function(add_item, "Fertilizer", 3),
        ]
    textbutton "Exit Farm" xpos 1500 ypos 50 action Jump("show_date")

    # Watering can button to toggle watering_mode
    textbutton "Watering Can" action ToggleVariable("watering_mode") xpos 50 ypos 50
    if watering_mode:
        text "Watering Can: ON" color "#6200ff" xpos 50 ypos 100
    else:
        text "Watering Can: OFF" color "#9b1b30" xpos 50 ypos 100

    textbutton "Harvest" action ToggleVariable("harvest_mode") xpos 500 ypos 50
    if harvest_mode:
        text "Harvest Mode: ON" color "#6200ff" xpos 500 ypos 100
    else:
        text "Harvest Mode: OFF" color "#9b1b30" xpos 500 ypos 100

    # Inventory button
    textbutton "Inventory" xpos 0.5 ypos 50 action Show("seeds_inventory")

    if fertilizer_mode:
        textbutton "Fertilizer Mode: ON" xpos 1000 ypos 50

    # Row 1 (Tile 1)
    imagebutton:
        # Check the current state and show appropriate image
        if a1_planted and a1watered and a1_plant_state == required_growth(a1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif a1_planted and a1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered images
        elif a1watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif a1_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"  # Hover image
        xpos 203
        ypos 238

        action [
            If(
                planting_mode and not a1_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("a1_planted", current_seed),  # Set the planted seed
                    SetVariable("a1_plant_state", 0),  # Reset plant state
                    SetVariable("a1watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not a1_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("a1_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not a1watered and a1_planted and a1_plant_state < required_growth(a1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("a1watered", True),  # Water the tile
                    SetVariable("a1_plant_state", a1_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and a1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        a1_plant_state >= required_growth(a1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if a1_fertilized == False else random.randint(3, 6),
                                inventory.update({a1_planted: inventory.get(a1_planted, 0) + random_amount})
                            )),
                            SetVariable("a1_planted", None),  # Reset planted state
                            SetVariable("a1_plant_state", 0),  # Reset plant state
                            SetVariable("a1watered", False),  # Reset watered state
                            SetVariable("a1_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if b1_planted and b1watered and b1_plant_state == required_growth(b1_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif b1_planted and b1watered:
            idle "images/watered/plantedwatered.png"
        elif b1watered:
            idle "images/watered/a1_watered.png"
        elif b1_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 439
        ypos 238

        action [
            If(
                planting_mode and not b1_planted,
                [
                    SetVariable("b1_planted", current_seed),
                    SetVariable("b1_plant_state", 0),
                    SetVariable("b1watered", False),
                    Function(lambda: (
                        inventory.update({current_seed: inventory.get(current_seed, 1) - 1}),
                        inventory.pop(current_seed) if inventory.get(current_seed, 0) <= 0 else None,
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not b1_fertilized,
                [
                    SetVariable("b1_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 1) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),

            If(
                watering_mode and not b1watered and b1_planted and b1_plant_state < required_growth(b1_planted),
                [
                    SetVariable("b1watered", True),
                    SetVariable("b1_plant_state", b1_plant_state + 1),
                ]
            ),

            If(
                harvest_mode and b1_planted,
                [
                    If(
                        b1_plant_state >= required_growth(b1_planted),
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if not b1_fertilized else random.randint(3, 6),
                                inventory.update({b1_planted: inventory.get(b1_planted, 0) + random_amount})
                            )),
                            SetVariable("b1_planted", None),
                            SetVariable("b1_plant_state", 0),
                            SetVariable("b1watered", False),
                            SetVariable("b1_fertilized", False),
                        ]
                    ),
                ]
            ),

            Jump("farming_start"),
        ]




            

    imagebutton:
        if c1_planted and c1watered and c1_plant_state == required_growth(c1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif c1_planted and c1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered image
        elif c1watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif c1_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"
        xpos 675
        ypos 238
        action [
            If(
                planting_mode and not c1_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("c1_planted", current_seed),  # Set the planted seed
                    SetVariable("c1_plant_state", 0),  # Reset plant state
                    SetVariable("c1watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not c1_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("c1_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not c1watered and c1_planted and c1_plant_state < required_growth(c1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("c1watered", True),  # Water the tile
                    SetVariable("c1_plant_state", c1_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and c1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        c1_plant_state >= required_growth(c1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if c1_fertilized == False else random.randint(3, 6),
                                inventory.update({c1_planted: inventory.get(c1_planted, 0) + random_amount})
                            )),
                            SetVariable("c1_planted", None),  # Reset planted state
                            SetVariable("c1_plant_state", 0),  # Reset plant state
                            SetVariable("c1watered", False),  # Reset watered state
                            SetVariable("c1_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if d1_planted and d1watered and d1_plant_state == required_growth(d1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif d1_planted and d1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered image
        elif d1watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif d1_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"
        xpos 911
        ypos 238
        action [
            If(
                planting_mode and not d1_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("d1_planted", current_seed),  # Set the planted seed
                    SetVariable("d1_plant_state", 0),  # Reset plant state
                    SetVariable("d1watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not d1_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("d1_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not d1watered and d1_planted and d1_plant_state < required_growth(d1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("d1watered", True),  # Water the tile
                    SetVariable("d1_plant_state", d1_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and d1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        d1_plant_state >= required_growth(d1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if d1_fertilized == False else random.randint(3, 6),
                                inventory.update({d1_planted: inventory.get(d1_planted, 0) + random_amount})
                            )),
                            SetVariable("d1_planted", None),  # Reset planted state
                            SetVariable("d1_plant_state", 0),  # Reset plant state
                            SetVariable("d1watered", False),  # Reset watered state
                            SetVariable("d1_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if e1_planted and e1watered and e1_plant_state == required_growth(e1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif e1_planted and e1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered image
        elif e1watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif e1_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"
        xpos 1147
        ypos 238
        action [
            If(
                planting_mode and not e1_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("e1_planted", current_seed),  # Set the planted seed
                    SetVariable("e1_plant_state", 0),  # Reset plant state
                    SetVariable("e1watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not e1_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("e1_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not e1watered and e1_planted and e1_plant_state < required_growth(e1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("e1watered", True),  # Water the tile
                    SetVariable("e1_plant_state", e1_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and e1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        e1_plant_state >= required_growth(e1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if e1_fertilized == False else random.randint(3, 6),
                                inventory.update({e1_planted: inventory.get(e1_planted, 0) + random_amount})
                            )),
                            SetVariable("e1_planted", None),  # Reset planted state
                            SetVariable("e1_plant_state", 0),  # Reset plant state
                            SetVariable("e1watered", False),  # Reset watered state
                            SetVariable("e1_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if f1_planted and f1watered and f1_plant_state == required_growth(f1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif f1_planted and f1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered image
        elif f1watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif f1_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"
        xpos 1383
        ypos 238
        action [
            If(
                planting_mode and not f1_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("f1_planted", current_seed),  # Set the planted seed
                    SetVariable("f1_plant_state", 0),  # Reset plant state
                    SetVariable("f1watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not f1_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("f1_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not f1watered and f1_planted and f1_plant_state < required_growth(f1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("f1watered", True),  # Water the tile
                    SetVariable("f1_plant_state", f1_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and f1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        f1_plant_state >= required_growth(f1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if f1_fertilized == False else random.randint(3, 6),
                                inventory.update({f1_planted: inventory.get(f1_planted, 0) + random_amount})
                            )),
                            SetVariable("f1_planted", None),  # Reset planted state
                            SetVariable("f1_plant_state", 0),  # Reset plant state
                            SetVariable("f1watered", False),  # Reset watered state
                            SetVariable("f1_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    # Row 2
    imagebutton:
        if a2_planted and a2watered and a2_plant_state == required_growth(a2_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif a2_planted and a2watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered image
        elif a2watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif a2_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"
        xpos 203
        ypos 476
        action [
            If(
                planting_mode and not a2_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("a2_planted", current_seed),  # Set the planted seed
                    SetVariable("a2_plant_state", 0),  # Reset plant state
                    SetVariable("a2watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not a2_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("a2_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not a2watered and a2_planted and a2_plant_state < required_growth(a2_planted),  # Only if plant is not fully grown
                [
                    SetVariable("a2watered", True),  # Water the tile
                    SetVariable("a2_plant_state", a2_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and a2_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        a2_plant_state >= required_growth(a2_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if a2_fertilized == False else random.randint(3, 6),
                                inventory.update({a2_planted: inventory.get(a2_planted, 0) + random_amount})
                            )),
                            SetVariable("a2_planted", None),  # Reset planted state
                            SetVariable("a2_plant_state", 0),  # Reset plant state
                            SetVariable("a2watered", False),  # Reset watered state
                            SetVariable("a2_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if b2_planted and b2watered and b2_plant_state == required_growth(b2_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif b2_planted and b2watered:
            idle "images/watered/plantedwatered.png"
        elif b2watered:
            idle "images/watered/a1_watered.png"
        elif b2_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 439
        ypos 476
        action [
            If(
                planting_mode and not b2_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("b2_planted", current_seed),  # Set the planted seed
                    SetVariable("b2_plant_state", 0),  # Reset plant state
                    SetVariable("b2watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not b2_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("b2_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not b2watered and b2_planted and b2_plant_state < required_growth(b2_planted),  # Only if plant is not fully grown
                [
                    SetVariable("b2watered", True),  # Water the tile
                    SetVariable("b2_plant_state", b2_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and b2_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        b2_plant_state >= required_growth(b2_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if b2_fertilized == False else random.randint(3, 6),
                                inventory.update({b2_planted: inventory.get(b2_planted, 0) + random_amount})
                            )),
                            SetVariable("b2_planted", None),  # Reset planted state
                            SetVariable("b2_plant_state", 0),  # Reset plant state
                            SetVariable("b2watered", False),  # Reset watered state
                            SetVariable("b2_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if c2_planted and c2watered and c2_plant_state == required_growth(c2_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif c2_planted and c2watered:
            idle "images/watered/plantedwatered.png"
        elif c2watered:
            idle "images/watered/a1_watered.png"
        elif c2_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 675
        ypos 476
        action [
            If(
                planting_mode and not c2_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("c2_planted", current_seed),  # Set the planted seed
                    SetVariable("c2_plant_state", 0),  # Reset plant state
                    SetVariable("c2watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not c2_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("c2_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not c2watered and c2_planted and c2_plant_state < required_growth(c2_planted),  # Only if plant is not fully grown
                [
                    SetVariable("c2watered", True),  # Water the tile
                    SetVariable("c2_plant_state", c2_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and c2_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        c2_plant_state >= required_growth(c2_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if c2_fertilized == False else random.randint(3, 6),
                                inventory.update({c2_planted: inventory.get(c2_planted, 0) + random_amount})
                            )),
                            SetVariable("c2_planted", None),  # Reset planted state
                            SetVariable("c2_plant_state", 0),  # Reset plant state
                            SetVariable("c2watered", False),  # Reset watered state
                            SetVariable("c2_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if d2_planted and d2watered and d2_plant_state == required_growth(d2_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif d2_planted and d2watered:
            idle "images/watered/plantedwatered.png"
        elif d2watered:
            idle "images/watered/a1_watered.png"
        elif d2_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 911
        ypos 476
        action [
            If(
                planting_mode and not d2_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("d2_planted", current_seed),  # Set the planted seed
                    SetVariable("d2_plant_state", 0),  # Reset plant state
                    SetVariable("d2watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not d2_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("d2_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not d2watered and d2_planted and d2_plant_state < required_growth(d2_planted),  # Only if plant is not fully grown
                [
                    SetVariable("d2watered", True),  # Water the tile
                    SetVariable("d2_plant_state", d2_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and d2_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        d2_plant_state >= required_growth(d2_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if d2_fertilized == False else random.randint(3, 6),
                                inventory.update({d2_planted: inventory.get(d2_planted, 0) + random_amount})
                            )),
                            SetVariable("d2_planted", None),  # Reset planted state
                            SetVariable("d2_plant_state", 0),  # Reset plant state
                            SetVariable("d2watered", False),  # Reset watered state
                            SetVariable("d2_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if e2_planted and e2watered and e2_plant_state == required_growth(e2_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif e2_planted and e2watered:
            idle "images/watered/plantedwatered.png"
        elif e2watered:
            idle "images/watered/a1_watered.png"
        elif e2_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 1147
        ypos 476
        action [
            If(
                planting_mode and not e2_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("e2_planted", current_seed),  # Set the planted seed
                    SetVariable("e2_plant_state", 0),  # Reset plant state
                    SetVariable("e2watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not e2_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("e2_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not e2watered and e2_planted and e2_plant_state < required_growth(e2_planted),  # Only if plant is not fully grown
                [
                    SetVariable("e2watered", True),  # Water the tile
                    SetVariable("e2_plant_state", e2_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and e2_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        e2_plant_state >= required_growth(e2_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if e2_fertilized == False else random.randint(3, 6),
                                inventory.update({e2_planted: inventory.get(e2_planted, 0) + random_amount})
                            )),
                            SetVariable("e2_planted", None),  # Reset planted state
                            SetVariable("e2_plant_state", 0),  # Reset plant state
                            SetVariable("e2watered", False),  # Reset watered state
                            SetVariable("e2_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if f2_planted and f2watered and f2_plant_state == required_growth(f2_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif f2_planted and f2watered:
            idle "images/watered/plantedwatered.png"
        elif f2watered:
            idle "images/watered/a1_watered.png"
        elif f2_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 1383
        ypos 476
        action [
            If(
                planting_mode and not f2_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("f2_planted", current_seed),  # Set the planted seed
                    SetVariable("f2_plant_state", 0),  # Reset plant state
                    SetVariable("f2watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not f2_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("f2_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not f2watered and f2_planted and f2_plant_state < required_growth(f2_planted),  # Only if plant is not fully grown
                [
                    SetVariable("f2watered", True),  # Water the tile
                    SetVariable("f2_plant_state", f2_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and f2_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        f2_plant_state >= required_growth(f2_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if f2_fertilized == False else random.randint(3, 6),
                                inventory.update({f2_planted: inventory.get(f2_planted, 0) + random_amount})
                            )),
                            SetVariable("f2_planted", None),  # Reset planted state
                            SetVariable("f2_plant_state", 0),  # Reset plant state
                            SetVariable("f2watered", False),  # Reset watered state
                            SetVariable("f2_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]


    # Row 3
    imagebutton:
        if a3_planted and a3watered and a3_plant_state == required_growth(a3_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"
        elif a3_planted and a3watered:  # Planted and watered
            idle "images/watered/plantedwatered.png"
        elif a3watered:  # Watered but not planted
            idle "images/watered/a1_watered.png"
        elif a3_planted:  # Planted but not watered
            idle "images/planted/planted.png"
        else:  # Default idle
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 203
        ypos 714
        action [
            If(
                planting_mode and not a3_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("a3_planted", current_seed),  # Set the planted seed
                    SetVariable("a3_plant_state", 0),  # Reset plant state
                    SetVariable("a3watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not a3_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("a3_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not a3watered and a3_planted and a3_plant_state < required_growth(a3_planted),  # Only if plant is not fully grown
                [
                    SetVariable("a3watered", True),  # Water the tile
                    SetVariable("a3_plant_state", a3_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and a3_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        a3_plant_state >= required_growth(a3_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if a3_fertilized == False else random.randint(3, 6),
                                inventory.update({a3_planted: inventory.get(a3_planted, 0) + random_amount})
                            )),
                            SetVariable("a3_planted", None),  # Reset planted state
                            SetVariable("a3_plant_state", 0),  # Reset plant state
                            SetVariable("a3watered", False),  # Reset watered state
                            SetVariable("a3_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if b3_planted and b3watered and b3_plant_state == required_growth(b3_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif b3_planted and b3watered:
            idle "images/watered/plantedwatered.png"
        elif b3watered:
            idle "images/watered/a1_watered.png"
        elif b3_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 439
        ypos 714
        action [
            If(
                planting_mode and not b3_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("b3_planted", current_seed),  # Set the planted seed
                    SetVariable("b3_plant_state", 0),  # Reset plant state
                    SetVariable("b3watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not b3_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("b3_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not b3watered and b3_planted and b3_plant_state < required_growth(b3_planted),  # Only if plant is not fully grown
                [
                    SetVariable("b3watered", True),  # Water the tile
                    SetVariable("b3_plant_state", b3_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and b3_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        b3_plant_state >= required_growth(b3_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if b3_fertilized == False else random.randint(3, 6),
                                inventory.update({b3_planted: inventory.get(b3_planted, 0) + random_amount})
                            )),
                            SetVariable("b3_planted", None),  # Reset planted state
                            SetVariable("b3_plant_state", 0),  # Reset plant state
                            SetVariable("b3watered", False),  # Reset watered state
                            SetVariable("b3_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if c3_planted and c3watered and c3_plant_state == required_growth(c3_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif c3_planted and c3watered:
            idle "images/watered/plantedwatered.png"
        elif c3watered:
            idle "images/watered/a1_watered.png"
        elif c3_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 675
        ypos 714
        action [
            If(
                planting_mode and not c3_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("c3_planted", current_seed),  # Set the planted seed
                    SetVariable("c3_plant_state", 0),  # Reset plant state
                    SetVariable("c3watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not c3_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("c3_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not c3watered and c3_planted and c3_plant_state < required_growth(c3_planted),  # Only if plant is not fully grown
                [
                    SetVariable("c3watered", True),  # Water the tile
                    SetVariable("c3_plant_state", c3_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and c3_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        c3_plant_state >= required_growth(c3_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if c3_fertilized == False else random.randint(3, 6),
                                inventory.update({c3_planted: inventory.get(c3_planted, 0) + random_amount})
                            )),
                            SetVariable("c3_planted", None),  # Reset planted state
                            SetVariable("c3_plant_state", 0),  # Reset plant state
                            SetVariable("c3watered", False),  # Reset watered state
                            SetVariable("c3_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if d3_planted and d3watered and d3_plant_state == required_growth(d3_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif d3_planted and d3watered:
            idle "images/watered/plantedwatered.png"
        elif d3watered:
            idle "images/watered/a1_watered.png"
        elif d3_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 911
        ypos 714
        action [
            If(
                planting_mode and not d3_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("d3_planted", current_seed),  # Set the planted seed
                    SetVariable("d3_plant_state", 0),  # Reset plant state
                    SetVariable("d3watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not d3_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("d3_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not d3watered and d3_planted and d3_plant_state < required_growth(d3_planted),  # Only if plant is not fully grown
                [
                    SetVariable("d3watered", True),  # Water the tile
                    SetVariable("d3_plant_state", d3_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and d3_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        d3_plant_state >= required_growth(d3_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if d3_fertilized == False else random.randint(3, 6),
                                inventory.update({d3_planted: inventory.get(d3_planted, 0) + random_amount})
                            )),
                            SetVariable("d3_planted", None),  # Reset planted state
                            SetVariable("d3_plant_state", 0),  # Reset plant state
                            SetVariable("d3watered", False),  # Reset watered state
                            SetVariable("d3_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if e3_planted and e3watered and e3_plant_state == required_growth(e3_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif e3_planted and e3watered:
            idle "images/watered/plantedwatered.png"
        elif e3watered:
            idle "images/watered/a1_watered.png"
        elif e3_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 1147
        ypos 714
        action [
            If(
                planting_mode and not e3_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("e3_planted", current_seed),  # Set the planted seed
                    SetVariable("e3_plant_state", 0),  # Reset plant state
                    SetVariable("e3watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not e3_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("e3_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not e3watered and e3_planted and e3_plant_state < required_growth(e3_planted),  # Only if plant is not fully grown
                [
                    SetVariable("e3watered", True),  # Water the tile
                    SetVariable("e3_plant_state", e3_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and e3_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        e3_plant_state >= required_growth(e3_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if e3_fertilized == False else random.randint(3, 6),
                                inventory.update({e3_planted: inventory.get(e3_planted, 0) + random_amount})
                            )),
                            SetVariable("e3_planted", None),  # Reset planted state
                            SetVariable("e3_plant_state", 0),  # Reset plant state
                            SetVariable("e3watered", False),  # Reset watered state
                            SetVariable("e3_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

    imagebutton:
        if f3_planted and f3watered and f3_plant_state == required_growth(f3_planted):
            idle "images/harvestable/a1_harvestable.png"
        elif f3_planted and f3watered:
            idle "images/watered/plantedwatered.png"
        elif f3watered:
            idle "images/watered/a1_watered.png"
        elif f3_planted:
            idle "images/planted/planted.png"
        else:
            idle "images/idle/a1_idle.png"

        hover "images/hover/a1_hover.png"
        xpos 1383
        ypos 714
        action [
            If(
                planting_mode and not f3_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("f3_planted", current_seed),  # Set the planted seed
                    SetVariable("f3_plant_state", 0),  # Reset plant state
                    SetVariable("f3watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not f3_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("f3_fertilized", True),
                    Function(lambda: (
                        inventory.update({current_fertilizer: inventory.get(current_fertilizer, 0) - 1}),
                        inventory.pop(current_fertilizer) if inventory.get(current_fertilizer, 0) <= 0 else None,
                        setattr(store, "current_fertilizer", None) if inventory.get(current_fertilizer, 0) == 0 else None,
                        setattr(store, "fertilizer_mode", False) if inventory.get(current_fertilizer, 0) == 0 else None
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not f3watered and f3_planted and f3_plant_state < required_growth(f3_planted),  # Only if plant is not fully grown
                [
                    SetVariable("f3watered", True),  # Water the tile
                    SetVariable("f3_plant_state", f3_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and f3_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        f3_plant_state >= required_growth(f3_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if f3_fertilized == False else random.randint(3, 6),
                                inventory.update({f3_planted: inventory.get(f3_planted, 0) + random_amount})
                            )),
                            SetVariable("f3_planted", None),  # Reset planted state
                            SetVariable("f3_plant_state", 0),  # Reset plant state
                            SetVariable("f3watered", False),  # Reset watered state
                            SetVariable("f3_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            Jump("farming_start"),
        ]

