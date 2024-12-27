screen farming():
    add "farm"  # Background image for the farm
    textbutton "Get Seeds":
        action[
            Function(inventory.add_item, ("blood lotus", 3)),
            Function(inventory.add_item, ("elfroot", 3)),
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
    textbutton "Inventory" xpos 0.5 ypos 50 action Show("inventory")

    # Row 1 (Tile 1)
    imagebutton:
        # Check the current state of the tile and show appropriate image
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

        # Define the action when clicking the tile
        action [
            # Planting logic
            If(
                planting_mode,  # If planting mode is active
                [
                    SetVariable("a1_planted", current_seed),  # Set the planted seed (replace with actual plant name)
                    SetVariable("a1_plant_state", 0),  # Reset plant state
                    SetVariable("a1watered", False),  # Reset watered state
                    ToggleVariable("planting_mode"),  # Turn off planting mode after planting
                    Function(inventory.remove, current_seed),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and a1_planted and a1_plant_state < required_growth(a1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("a1watered", True),  # Water the tile
                    SetVariable("a1_plant_state", a1_plant_state + 1),  # Increase plant state without using min
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and a1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        a1_plant_state >= required_growth(a1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(inventory.append, a1_planted),  # Add the plant to the inventory
                            SetVariable("a1_planted", None),  # Reset planted state
                            SetVariable("a1_plant_state", 0),  # Reset plant state
                            SetVariable("a1watered", False),  # Reset watered state
                        ],
                        ##renpy.notify("This plot is not ready to harvest!")  # Notify if not ready
                    )
                ]
            ),
            
            # After all actions are performed, show the farming screen
            Show("farming")
        ]



    imagebutton:
        if b1_planted and b1watered and b1_plant_state == required_growth(b1_planted):  # Harvestable
            idle "images/harvestable/a1_harvestable.png"  # Display harvestable image
        elif b1_planted and b1watered:  # If both planted and watered
            idle "images/watered/plantedwatered.png"  # Display planted + watered image
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
            # Planting logic
            If(
                planting_mode,  # If planting mode is active
                [
                    SetVariable("b1_planted", current_seed),  # Set the planted seed (replace with actual plant name)
                    SetVariable("b1_plant_state", 0),  # Reset plant state
                    SetVariable("b1watered", False),  # Reset watered state
                    ToggleVariable("planting_mode"),  # Turn off planting mode after planting
                    Function(inventory.remove, current_seed),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and b1_planted and b1_plant_state < required_growth(b1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("b1watered", True),  # Water the tile
                    SetVariable("b1_plant_state", b1_plant_state + 1),  # Increase plant state without using min
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and b1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        b1_plant_state >= required_growth(b1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(inventory.append, b1_planted),  # Add the plant to the inventory
                            SetVariable("b1_planted", None),  # Reset planted state
                            SetVariable("b1_plant_state", 0),  # Reset plant state
                            SetVariable("b1watered", False),  # Reset watered state
                        ],
                        ##renpy.notify("This plot is not ready to harvest!")  # Notify if not ready
                    )
                ]
            ),
            
            # After all actions are performed, show the farming screen
            Show("farming")
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
            # Planting logic
            If(
                planting_mode,  # If planting mode is active
                [
                    SetVariable("c1_planted", current_seed),  # Set the planted seed (replace with actual plant name)
                    SetVariable("c1_plant_state", 0),  # Reset plant state
                    SetVariable("c1watered", False),  # Reset watered state
                    ToggleVariable("planting_mode"),  # Turn off planting mode after planting
                    Function(inventory.remove, current_seed),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and c1_planted and c1_plant_state < required_growth(c1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("c1watered", True),  # Water the tile
                    SetVariable("c1_plant_state", c1_plant_state + 1),  # Increase plant state without using min
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and c1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        c1_plant_state >= required_growth(c1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(inventory.append, c1_planted),  # Add the plant to the inventory
                            SetVariable("c1_planted", None),  # Reset planted state
                            SetVariable("c1_plant_state", 0),  # Reset plant state
                            SetVariable("c1watered", False),  # Reset watered state
                        ],
                        ##renpy.notify("This plot is not ready to harvest!")  # Notify if not ready
                    )
                ]
            ),
            
            # After all actions are performed, show the farming screen
            Show("farming")
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
            # Planting logic
            If(
                planting_mode,  # If planting mode is active
                [
                    SetVariable("d1_planted", current_seed),  # Set the planted seed (replace with actual plant name)
                    SetVariable("d1_plant_state", 0),  # Reset plant state
                    SetVariable("d1watered", False),  # Reset watered state
                    ToggleVariable("planting_mode"),  # Turn off planting mode after planting
                    Function(inventory.remove, current_seed),
                ]
            ),
            
            # Watering logic
            If(
                watering_mode and d1_planted and d1_plant_state < required_growth(d1_planted),  # Only if plant is not fully grown
                [
                    SetVariable("d1watered", True),  # Water the tile
                    SetVariable("d1_plant_state", d1_plant_state + 1),  # Increase plant state without using min
                ]
            ),
            
            # Harvesting logic
            If(
                harvest_mode and d1_planted,  # If harvest mode is active and the plot is planted
                [
                    If(
                        d1_plant_state >= required_growth(d1_planted),  # Only harvest if plant is fully grown
                        [
                            Function(inventory.append, d1_planted),  # Add the plant to the inventory
                            SetVariable("d1_planted", None),  # Reset planted state
                            SetVariable("d1_plant_state", 0),  # Reset plant state
                            SetVariable("d1watered", False),  # Reset watered state
                        ]
                    ),
                ]
            ),
            # After all actions, show the farming screen
            Show("farming")
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
            # Planting logic
            If(
                planting_mode,  # If planting mode is active
                [
                    SetVariable("e1_planted", current_seed),  # Set the planted seed
                    SetVariable("e1_plant_state", 0),  # Reset plant state
                    SetVariable("e1watered", False),  # Reset watered state
                    ToggleVariable("planting_mode"),  # Turn off planting mode after planting
                    Function(inventory.remove, current_seed),
                ]
            ),

            # Watering logic
            If(
                watering_mode and e1_planted and e1_plant_state < required_growth(e1_planted),  # Only if plant is not fully grown
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
                            Function(inventory.append, e1_planted),  # Add the plant to the inventory
                            SetVariable("e1_planted", None),  # Reset planted state
                            SetVariable("e1_plant_state", 0),  # Reset plant state
                            SetVariable("e1watered", False),  # Reset watered state
                        ]
                    ),
                ]
            ),
            # After all actions, show the farming screen
            Show("farming")
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
            # Planting logic
            If(
                planting_mode,  # If planting mode is active
                [
                    SetVariable("f1_planted", current_seed),  # Set the planted seed
                    SetVariable("f1_plant_state", 0),  # Reset plant state
                    SetVariable("f1watered", False),  # Reset watered state
                    ToggleVariable("planting_mode"),  # Turn off planting mode after planting
                    Function(inventory.remove, current_seed),
                ]
            ),

            # Watering logic
            If(
                watering_mode and f1_planted and f1_plant_state < required_growth(f1_planted),  # Only if plant is not fully grown
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
                            Function(inventory.append, f1_planted),  # Add the plant to the inventory
                            SetVariable("f1_planted", None),  # Reset planted state
                            SetVariable("f1_plant_state", 0),  # Reset plant state
                            SetVariable("f1watered", False),  # Reset watered state
                        ]
                    ),
                ]
            ),
            # After all actions, show the farming screen
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("a2_planted", current_seed),
                    SetVariable("a2_plant_state", 0),
                    SetVariable("a2watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and a2_planted and a2_plant_state < required_growth(a2_planted),
                [
                    SetVariable("a2watered", True),
                    SetVariable("a2_plant_state", a2_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and a2_planted,
                [
                    If(
                        a2_plant_state >= required_growth(a2_planted),
                        [
                            Function(inventory.append, a2_planted),
                            SetVariable("a2_planted", None),
                            SetVariable("a2_plant_state", 0),
                            SetVariable("a2watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("b2_planted", current_seed),
                    SetVariable("b2_plant_state", 0),
                    SetVariable("b2watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and b2_planted and b2_plant_state < required_growth(b2_planted),
                [
                    SetVariable("b2watered", True),
                    SetVariable("b2_plant_state", b2_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and b2_planted,
                [
                    If(
                        b2_plant_state >= required_growth(b2_planted),
                        [
                            Function(inventory.append, b2_planted),
                            SetVariable("b2_planted", None),
                            SetVariable("b2_plant_state", 0),
                            SetVariable("b2watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("c2_planted", current_seed),
                    SetVariable("c2_plant_state", 0),
                    SetVariable("c2watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and c2_planted and c2_plant_state < required_growth(c2_planted),
                [
                    SetVariable("c2watered", True),
                    SetVariable("c2_plant_state", c2_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and c2_planted,
                [
                    If(
                        c2_plant_state >= required_growth(c2_planted),
                        [
                            Function(inventory.append, c2_planted),
                            SetVariable("c2_planted", None),
                            SetVariable("c2_plant_state", 0),
                            SetVariable("c2watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("d2_planted", current_seed),
                    SetVariable("d2_plant_state", 0),
                    SetVariable("d2watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and d2_planted and d2_plant_state < required_growth(d2_planted),
                [
                    SetVariable("d2watered", True),
                    SetVariable("d2_plant_state", d2_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and d2_planted,
                [
                    If(
                        d2_plant_state >= required_growth(d2_planted),
                        [
                            Function(inventory.append, d2_planted),
                            SetVariable("d2_planted", None),
                            SetVariable("d2_plant_state", 0),
                            SetVariable("d2watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("e2_planted", current_seed),
                    SetVariable("e2_plant_state", 0),
                    SetVariable("e2watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and e2_planted and e2_plant_state < required_growth(e2_planted),
                [
                    SetVariable("e2watered", True),
                    SetVariable("e2_plant_state", e2_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and e2_planted,
                [
                    If(
                        e2_plant_state >= required_growth(e2_planted),
                        [
                            Function(inventory.append, e2_planted),
                            SetVariable("e2_planted", None),
                            SetVariable("e2_plant_state", 0),
                            SetVariable("e2watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("f2_planted", current_seed),
                    SetVariable("f2_plant_state", 0),
                    SetVariable("f2watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and f2_planted and f2_plant_state < required_growth(f2_planted),
                [
                    SetVariable("f2watered", True),
                    SetVariable("f2_plant_state", f2_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and f2_planted,
                [
                    If(
                        f2_plant_state >= required_growth(f2_planted),
                        [
                            Function(inventory.append, f2_planted),
                            SetVariable("f2_planted", None),
                            SetVariable("f2_plant_state", 0),
                            SetVariable("f2watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("a3_planted", current_seed),
                    SetVariable("a3_plant_state", 0),
                    SetVariable("a3watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and a3_planted and a3_plant_state < required_growth(a3_planted),
                [
                    SetVariable("a3watered", True),
                    SetVariable("a3_plant_state", a3_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and a3_planted,
                [
                    If(
                        a3_plant_state >= required_growth(a3_planted),
                        [
                            Function(inventory.append, a3_planted),
                            SetVariable("a3_planted", None),
                            SetVariable("a3_plant_state", 0),
                            SetVariable("a3watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("b3_planted", current_seed),
                    SetVariable("b3_plant_state", 0),
                    SetVariable("b3watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and b3_planted and b3_plant_state < required_growth(b3_planted),
                [
                    SetVariable("b3watered", True),
                    SetVariable("b3_plant_state", b3_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and b3_planted,
                [
                    If(
                        b3_plant_state >= required_growth(b3_planted),
                        [
                            add_item(b3_planted, 2),
                            If(
                                b3_planted == "blood lotus",
                                [
                                    Function(add_item, b3_planted, 3)
                                ]
                            ),
                            Function(renpy.notify, f"{b3_planted} is harvested"),
                            SetVariable("b3_planted", ""),
                            SetVariable("b3_plant_state", 0),
                            SetVariable("b3watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("c3_planted", current_seed),
                    SetVariable("c3_plant_state", 0),
                    SetVariable("c3watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and c3_planted and c3_plant_state < required_growth(c3_planted),
                [
                    SetVariable("c3watered", True),
                    SetVariable("c3_plant_state", c3_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and c3_planted,
                [
                    If(
                        c3_plant_state >= required_growth(c3_planted),
                        [
                            Function(inventory.append, c3_planted),
                            SetVariable("c3_planted", None),
                            SetVariable("c3_plant_state", 0),
                            SetVariable("c3watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("d3_planted", current_seed),
                    SetVariable("d3_plant_state", 0),
                    SetVariable("d3watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and d3_planted and d3_plant_state < required_growth(d3_planted),
                [
                    SetVariable("d3watered", True),
                    SetVariable("d3_plant_state", d3_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and d3_planted,
                [
                    If(
                        d3_plant_state >= required_growth(d3_planted),
                        [
                            Function(inventory.append, d3_planted),
                            SetVariable("d3_planted", None),
                            SetVariable("d3_plant_state", 0),
                            SetVariable("d3watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("e3_planted", current_seed),
                    SetVariable("e3_plant_state", 0),
                    SetVariable("e3watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and e3_planted and e3_plant_state < required_growth(e3_planted),
                [
                    SetVariable("e3watered", True),
                    SetVariable("e3_plant_state", e3_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and e3_planted,
                [
                    If(
                        e3_plant_state >= required_growth(e3_planted),
                        [
                            Function(inventory.append, e3_planted),
                            SetVariable("e3_planted", None),
                            SetVariable("e3_plant_state", 0),
                            SetVariable("e3watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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
                planting_mode,
                [
                    SetVariable("f3_planted", current_seed),
                    SetVariable("f3_plant_state", 0),
                    SetVariable("f3watered", False),
                    ToggleVariable("planting_mode"),
                    Function(inventory.remove, current_seed),
                ]
            ),
            If(
                watering_mode and f3_planted and f3_plant_state < required_growth(f3_planted),
                [
                    SetVariable("f3watered", True),
                    SetVariable("f3_plant_state", f3_plant_state + 1),
                ]
            ),
            If(
                harvest_mode and f3_planted,
                [
                    If(
                        f3_plant_state >= required_growth(f3_planted),
                        [
                            Function(inventory.append, f3_planted),
                            SetVariable("f3_planted", None),
                            SetVariable("f3_plant_state", 0),
                            SetVariable("f3watered", False),
                        ]
                    ),
                ]
            ),
            Show("farming")
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


# After choosing what to plant, water the plant
label planting:
    window hide
    if not watered:
        "You chose to plant [plant_type]. Now, you can water it."
        
        "Water your plant?"
        menu:
            "Yes":
                $ watered = True
                "You watered the [plant_type] plant."
                jump gardening  # Go back to the main screen after watering

            "No":
                "You decided not to water the plant yet."
                jump gardening  # Go back to the main screen without watering

    else:
        "The plant is already watered, come back tomorrow."
        jump gardening  # Go back to the main screen after checking

# Back to the farming scree