screen farming():
    add "farm"  # Background image for the farm
    textbutton "Get Seeds":
        action[
            Function(add_item, "blood lotus", 3),
            Function(add_item, "elfroot", 3),
            Function(add_item, "fertilizer", 3),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
        ]

    imagebutton:
        # Check the current state and show appropriate image for b1
        if b1_planted and b1watered and b1_plant_state == required_growth(b1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif b1_planted and b1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered images
        elif b1watered:  # If the tile is watered but not planted
            idle "images/watered/a1_watered.png"  # Display watered image
        elif b1_planted:  # If the tile is planted but not watered
            idle "images/planted/planted.png"  # Display planted image
        else:  # Default idle state
            idle "images/idle/a1_idle.png"  # Default idle image (empty)

        hover "images/hover/a1_hover.png"
        xpos 439
        ypos 238

        action [
            If(
                planting_mode and not b1_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("planting_mode", False),
                    SetVariable("b1_planted", current_seed),  # Set the planted seed
                    SetVariable("b1_plant_state", 0),  # Reset plant state
                    SetVariable("b1watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not b1_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("b1_fertilized", True),
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not b1watered and b1_planted and b1_plant_state < required_growth(b1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("b1watered", True),  # Water the tile
                    SetVariable("b1_plant_state", b1_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and b1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        b1_plant_state >= required_growth(b1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if b1_fertilized == False else random.randint(3, 6),
                                inventory.update({b1_planted: inventory.get(b1_planted, 0) + random_amount})
                            )),
                            SetVariable("b1_planted", None),  # Reset planted state
                            SetVariable("b1_plant_state", 0),  # Reset plant state
                            SetVariable("b1watered", False),  # Reset watered state
                            SetVariable("b1_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                    SetVariable("planting_mode", False),
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
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
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
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
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
                planting_mode and not e4_planted,  # Check planting mode and unplanted condition
                [
                    SetVariable("planting_mode", False),
                    SetVariable("e4_planted", current_seed),  # Set the planted seed
                    SetVariable("e4_plant_state", 0),  # Reset plant state
                    SetVariable("e4watered", False),  # Reset watered state
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                        setattr(store, "planting_mode", False) if inventory.get(current_seed, 0) == 0 else None
                    )),
                ]
            ),

            If(
                fertilizer_mode and not e4_fertilized,  # Check planting mode and unplanted condition
                [
                    SetVariable("e4_fertilized", True),
                    SetVariable("fertilizer_mode", False),
                    Function(lambda: (
                        inventory.pop(current_seed) if inventory[current_seed] == 1 
                        else inventory.update({current_seed: inventory[current_seed] - 1}),
                        setattr(store, "current_seed", None) if inventory.get(current_seed, 0) == 0 else None,
                    )),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and not e4watered and e4_planted and e4_plant_state < required_growth(e4_planted),  # Only if plant is not fully grown
                [
                    SetVariable("e4watered", True),  # Water the tile
                    SetVariable("e4_plant_state", e4_plant_state + 1),  # Increase plant state
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and e4_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        e4_plant_state >= required_growth(e4_planted),  # Only harvest if plant is fully grown
                        [
                            Function(lambda: (
                                random_amount := random.randint(1, 2) if e4_fertilized == False else random.randint(3, 6),
                                inventory.update({e4_planted: inventory.get(e4_planted, 0) + random_amount})
                            )),
                            SetVariable("e4_planted", None),  # Reset planted state
                            SetVariable("e4_plant_state", 0),  # Reset plant state
                            SetVariable("e4watered", False),  # Reset watered state
                            SetVariable("e4_fertilized", False)
                        ]
                    ),
                ]
            ),
            
            # Only show the farming screen if any change occurred
            If(
                planting_mode or watering_mode or harvest_mode,  # Check if any mode was active and performed an action
                Jump("farming_start")  # Show farming screen after actions
            ),
        ]





# Menu that shows up after clicking the tile
# label gardeninga1:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ a1planted = True
#             $ a1plant_type = "Cheese"
#             jump a1planting

#         "Elfroot":
#             $ a1planted = True
#             $ a1plant_type = "Elfroot"
#             jump a1planting

#         "Blood Lotus":
#             $ a1planted = True
#             $ a1plant_type = "Blood Lotus"
#             jump a1planting

#         "Royal Elfroot":
#             $ a1planted = True
#             $ a1plant_type = "Royal Elfroot"
#             jump a1planting

# label gardeninga2:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ a2planted = True
#             $ a2plant_type = "Cheese"
#             jump a2planting

#         "Elfroot":
#             $ a2planted = True
#             $ a2plant_type = "Elfroot"
#             jump a2planting

#         "Blood Lotus":
#             $ a2planted = True
#             $ a2plant_type = "Blood Lotus"
#             jump a2planting

#         "Royal Elfroot":
#             $ a2planted = True
#             $ a2plant_type = "Royal Elfroot"
#             jump a2planting

# label gardeninga3:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ a3planted = True
#             $ a3plant_type = "Cheese"
#             jump a3planting

#         "Elfroot":
#             $ a3planted = True
#             $ a3plant_type = "Elfroot"
#             jump a3planting

#         "Blood Lotus":
#             $ a3planted = True
#             $ a3plant_type = "Blood Lotus"
#             jump a3planting

#         "Royal Elfroot":
#             $ a3planted = True
#             $ a3plant_type = "Royal Elfroot"
#             jump a3planting

# label gardeningb1:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ b1planted = True
#             $ b1plant_type = "Cheese"
#             jump b1planting

#         "Elfroot":
#             $ b1planted = True
#             $ b1plant_type = "Elfroot"
#             jump b1planting

#         "Blood Lotus":
#             $ b1planted = True
#             $ b1plant_type = "Blood Lotus"
#             jump b1planting

#         "Royal Elfroot":
#             $ b1planted = True
#             $ b1plant_type = "Royal Elfroot"
#             jump b1planting

# label gardeningb2:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ b2planted = True
#             $ b2plant_type = "Cheese"
#             jump b2planting

#         "Elfroot":
#             $ b2planted = True
#             $ b2plant_type = "Elfroot"
#             jump b2planting

#         "Blood Lotus":
#             $ b2planted = True
#             $ b2plant_type = "Blood Lotus"
#             jump b2planting

#         "Royal Elfroot":
#             $ b2planted = True
#             $ b2plant_type = "Royal Elfroot"
#             jump b2planting

# label gardeningb3:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ b3planted = True
#             $ b3plant_type = "Cheese"
#             jump b3planting

#         "Elfroot":
#             $ b3planted = True
#             $ b3plant_type = "Elfroot"
#             jump b3planting

#         "Blood Lotus":
#             $ b3planted = True
#             $ b3plant_type = "Blood Lotus"
#             jump b3planting

#         "Royal Elfroot":
#             $ b3planted = True
#             $ b3plant_type = "Royal Elfroot"
#             jump b3planting

# label gardeningc1:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ c1planted = True
#             $ c1plant_type = "Cheese"
#             jump c1planting

#         "Elfroot":
#             $ c1planted = True
#             $ c1plant_type = "Elfroot"
#             jump c1planting

#         "Blood Lotus":
#             $ c1planted = True
#             $ c1plant_type = "Blood Lotus"
#             jump c1planting

#         "Royal Elfroot":
#             $ c1planted = True
#             $ c1plant_type = "Royal Elfroot"
#             jump c1planting

# label gardeningc2:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ c2planted = True
#             $ c2plant_type = "Cheese"
#             jump c2planting

#         "Elfroot":
#             $ c2planted = True
#             $ c2plant_type = "Elfroot"
#             jump c2planting

#         "Blood Lotus":
#             $ c2planted = True
#             $ c2plant_type = "Blood Lotus"
#             jump c2planting

#         "Royal Elfroot":
#             $ c2planted = True
#             $ c2plant_type = "Royal Elfroot"
#             jump c2planting

# label gardeningc3:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ c3planted = True
#             $ c3plant_type = "Cheese"
#             jump c3planting

#         "Elfroot":
#             $ c3planted = True
#             $ c3plant_type = "Elfroot"
#             jump c3planting

#         "Blood Lotus":
#             $ c3planted = True
#             $ c3plant_type = "Blood Lotus"
#             jump c3planting

#         "Royal Elfroot":
#             $ c3planted = True
#             $ c3plant_type = "Royal Elfroot"
#             jump c3planting

# label gardeningd1:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ d1planted = True
#             $ d1plant_type = "Cheese"
#             jump d1planting

#         "Elfroot":
#             $ d1planted = True
#             $ d1plant_type = "Elfroot"
#             jump d1planting

#         "Blood Lotus":
#             $ d1planted = True
#             $ d1plant_type = "Blood Lotus"
#             jump d1planting

#         "Royal Elfroot":
#             $ d1planted = True
#             $ d1plant_type = "Royal Elfroot"
#             jump d1planting

# label gardeningd2:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ d2planted = True
#             $ d2plant_type = "Cheese"
#             jump d2planting

#         "Elfroot":
#             $ d2planted = True
#             $ d2plant_type = "Elfroot"
#             jump d2planting

#         "Blood Lotus":
#             $ d2planted = True
#             $ d2plant_type = "Blood Lotus"
#             jump d2planting

#         "Royal Elfroot":
#             $ d2planted = True
#             $ d2plant_type = "Royal Elfroot"
#             jump d2planting

# label gardeningd3:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ d3planted = True
#             $ d3plant_type = "Cheese"
#             jump d3planting

#         "Elfroot":
#             $ d3planted = True
#             $ d3plant_type = "Elfroot"
#             jump d3planting

#         "Blood Lotus":
#             $ d3planted = True
#             $ d3plant_type = "Blood Lotus"
#             jump d3planting

#         "Royal Elfroot":
#             $ d3planted = True
#             $ d3plant_type = "Royal Elfroot"
#             jump d3planting

# label gardeninge1:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ e1planted = True
#             $ e1plant_type = "Cheese"
#             jump e1planting

#         "Elfroot":
#             $ e1planted = True
#             $ e1plant_type = "Elfroot"
#             jump e1planting

#         "Blood Lotus":
#             $ e1planted = True
#             $ e1plant_type = "Blood Lotus"
#             jump e1planting

#         "Royal Elfroot":
#             $ e1planted = True
#             $ e1plant_type = "Royal Elfroot"
#             jump e1planting

# label gardeninge2:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ e2planted = True
#             $ e2plant_type = "Cheese"
#             jump e2planting

#         "Elfroot":
#             $ e2planted = True
#             $ e2plant_type = "Elfroot"
#             jump e2planting

#         "Blood Lotus":
#             $ e2planted = True
#             $ e2plant_type = "Blood Lotus"
#             jump e2planting

#         "Royal Elfroot":
#             $ e2planted = True
#             $ e2plant_type = "Royal Elfroot"
#             jump e2planting

# label gardeninge3:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ e3planted = True
#             $ e3plant_type = "Cheese"
#             jump e3planting

#         "Elfroot":
#             $ e3planted = True
#             $ e3plant_type = "Elfroot"
#             jump e3planting

#         "Blood Lotus":
#             $ e3planted = True
#             $ e3plant_type = "Blood Lotus"
#             jump e3planting

#         "Royal Elfroot":
#             $ e3planted = True
#             $ e3plant_type = "Royal Elfroot"
#             jump e3planting

# label gardeningf1:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ f1planted = True
#             $ f1plant_type = "Cheese"
#             jump f1planting

#         "Elfroot":
#             $ f1planted = True
#             $ f1plant_type = "Elfroot"
#             jump f1planting

#         "Blood Lotus":
#             $ f1planted = True
#             $ f1plant_type = "Blood Lotus"
#             jump f1planting

#         "Royal Elfroot":
#             $ f1planted = True
#             $ f1plant_type = "Royal Elfroot"
#             jump f1planting

# label gardeningf2:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ f2planted = True
#             $ f2plant_type = "Cheese"
#             jump f2planting

#         "Elfroot":
#             $ f2planted = True
#             $ f2plant_type = "Elfroot"
#             jump f2planting

#         "Blood Lotus":
#             $ f2planted = True
#             $ f2plant_type = "Blood Lotus"
#             jump f2planting

#         "Royal Elfroot":
#             $ f2planted = True
#             $ f2plant_type = "Royal Elfroot"
#             jump f2planting

# label gardeningf3:
#     scene farm
#     "What do you want to plant?" 
#     menu:
#         "Cheese":
#             $ f3planted = True
#             $ f3plant_type = "Cheese"
#             jump f3planting

#         "Elfroot":
#             $ f3planted = True
#             $ f3plant_type = "Elfroot"
#             jump f3planting

#         "Blood Lotus":
#             $ f3planted = True
#             $ f3plant_type = "Blood Lotus"
#             jump f3planting

#         "Royal Elfroot":
#             $ f3planted = True
#             $ f3plant_type = "Royal Elfroot"
#             jump f3planting


