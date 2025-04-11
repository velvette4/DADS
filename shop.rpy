screen shop_buy():
    frame:
        align (0.5, 0.5)  # Center the frame
        padding (100, 100, 100, 100)  # Correct tuple format for padding
        background "#222"  # Dark background color
        xysize (800, 600)  # Set a specific size for the frame
        
        vbox:
            spacing 20
            text "Shop - Buy Items" size 30 color "#FFF" bold True align (0.5, 0.5)  # Centered title
            viewport:
                scrollbars "vertical"  # Add vertical scrollbar if needed
                draggable True
                vbox:
                    spacing 10
                    for item_name, details in seed_items.items():
                        hbox:
                            spacing 20
                            text f"{item_name}" size 20 color "#FFF"  # Item name
                            text f"Price: {details['price']} G" size 18 color "#AAA"  # Item price
                            textbutton "Buy":
                                action [Function(buy_item, item_name)]  # Call buy function
                                background "#4CAF50"  # Green button
                                hover_background "#45A049"  # Hover effect

            textbutton "Return to Shop" action Jump("shop_menu") align (0.5, 0.5) background "#444" hover_background "#555"  # Centered exit button

# screen shop_sell():
#     frame:
#         align (0.5, 0.5)  # Center the frame
#         padding (100, 100, 100, 100)  # Add padding inside the frame
#         background "#222"  # Dark background color
#         xysize (800, 600)  # Set a specific size for the frame

#         vbox:
#             spacing 20
#             text "Shop - Sell Items" size 30 color "#FFF" bold True align (0.5, 0.5)  # Centered title
#             viewport:
#                 scrollbars "vertical"  # Add vertical scrollbar if needed
#                 draggable True
#                 vbox:
#                     spacing 10
#                     for item_name, value in inventory.items():
#                         hbox:
#                             spacing 20
#                             text f"{item_name}" size 20 color "#FFF"  # Item name
#                             text f"Value: {value} G" size 18 color "#AAA"  # Item value
#                             textbutton "Sell":
#                                 action [Function(sell_item, item_name)]  # Call sell function
#                                 background "#E57373"  # Red button
#                                 hover_background "#D32F2F"  # Hover effect

#             textbutton "Return to Shop" action Jump("shop_menu") align (0.5, 0.5) background "#444" hover_background "#555"  # Centered exit button

# screen shop_sell():
#     frame:
#         align (0.5, 0.5)  # Center the frame
#         padding (100, 100, 100, 100)  # Add padding inside the frame
#         background "#222"  # Dark background color
#         xysize (800, 600)  # Set a specific size for the frame

#         vbox:
#             spacing 20
#             text "Shop - Sell Items" size 30 color "#FFF" bold True align (0.5, 0.5)  # Centered title
#             viewport:
#                 scrollbars "vertical"  # Add vertical scrollbar if needed
#                 draggable True
#                 vbox:
#                     spacing 10
#                     for item_name, details in inventory.items():
#                         hbox:
#                             spacing 20
#                             text f"{item_name}" size 20 color "#FFF"  # Item name
#                             text f"Value: {details['value']} G" size 18 color "#AAA"  # Item value
#                             text f"Amount: {details['amount']}" size 18 color "#AAA"  # Item amount
#                             textbutton "Sell":
#                                 action Show("sell_popup", item_name=item_name, max_quantity=details['amount'])  # Show popup with max quantity
#                                 background "#E57373"  # Red button
#                                 hover_background "#D32F2F"  # Hover effect

#             textbutton "Return to Shop" action Jump("shop_menu") align (0.5, 0.5) background "#444" hover_background "#555"  # Centered exit button

# Popup for selling quantity
screen shop_sell():
    frame:
        align (0.5, 0.5)  # Center the frame
        padding (100, 100, 100, 100)  # Correct tuple format for padding
        background "#222"  # Dark background color
        xysize (800, 600)  # Set a specific size for the frame
        
        vbox:
            spacing 20
            text "Shop - Sell Items" size 30 color "#FFF" bold True align (0.5, 0.5)  # Centered title

            # Scrollable area for items using a viewport
            viewport:
                scrollbars "vertical"  # Add vertical scrollbar if needed
                draggable True
                vbox:
                    spacing 10
                    for item_name, amount in inventory.items():
                        if amount > 0:  # Only show items that the player has
                            hbox:
                                spacing 20
                                text f"{item_name.capitalize()}: {amount} available" size 20 color "#FFF"  # Item name
                                textbutton "Sell" action [SetVariable("selected_item", item_name), Show("amount_input")]  # Button to select item

            # When an item is selected, show the amount input UI
screen amount_input:
    # Center the window using xalign and yalign
    window:
        xalign 0.5
        yalign 0.5

        frame:
            background "#333"  # Background color for the frame
            padding (20, 20)  # Padding inside the frame for spacing

            vbox:
                spacing 20
                align (0.5, 0.5)  # This centers the contents within the vbox

                # Title text
                text f"How many {selected_item} do you want to sell?" size 20 color "#FFF" align (0.5, 0.5)

                # Quantity selector
                hbox:
                    spacing 20
                    align (0.5, 0.5)

                    textbutton "−" action [SetVariable("amount_to_sell", max(0, amount_to_sell - 1))]  # Decrease by 1 (can't go below 0)
                    text f"{amount_to_sell}" size 20 color "#FFF"  # Show the selected amount
                    textbutton "＋" action [SetVariable("amount_to_sell", min(inventory[selected_item], amount_to_sell + 1))]  # Increase by 1 (can't go above inventory amount)

                # Buttons at the bottom
                hbox:
                    spacing 30
                    align (0.5, 0.5)

                    # Sell button with styled text
                    textbutton "Sell" action [Function(sell_item, selected_item, amount_to_sell), Hide("amount_input")] background "#44AA44" hover_background "#66BB66" style "button_style"

                    # Cancel button with styled text
                    textbutton "Cancel" action Hide("amount_input") background "#AA4444" hover_background "#BB6666" style "button_style"

    # Return to Shop button
    textbutton "Return to Shop" action Jump("shop_menu") align (0.5, 0.5) background "#444" hover_background "#555" style "button_style"

# Define a custom style for buttons
style button_style:
    size 18
    font "fonts/YourFont.ttf"  # Replace with your font file, if necessary
    color "#FFF"  # Text color




# screen shop_sell():
#     tag shop
#     frame:
#         xalign 0.5
#         yalign 0.5
#         padding (20, 20, 20, 20)
#         background "#222"  # Dark gray background
#         vbox:
#             spacing 10
#             text "Shop - Sell Items" size 30 color "#FFF" xalign 0.5  # White text
#             viewport:
#                 draggable True
#                 mousewheel True
#                 scrollbars "vertical"
#                 vbox:
#                     spacing 5
#                     for item_name, quantity in inventory.items():
#                         if quantity > 0:  # Only show items the player owns
#                             hbox:
#                                 spacing 10
#                                 text f"{item_name} - Quantity: {quantity} | Sell Price: {seed_items[item_name]['price'] // 2} G" size 20 color "#FFF"  # White text
#                                 textbutton "Sell" action Function(sell_item, item_name) background "#4CAF50" foreground "#FFF" hover_background "#45A049"  # Green button with white text
#             textbutton "Back" action Jump("shop_menu") background "#f44336" foreground "#FFF" hover_background "#e41e10" xalign 0.5  # Red button with white text

screen shop_navigation():
    tag shop
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20, 20, 20)
        background "#222"  # Dark gray background
        vbox:
            spacing 20
            text "Welcome to the Shop!" size 35 color "#FFF" xalign 0.5  # White text
            textbutton "Buy Items" action Show("shop_buy") background "#2196F3" hover_background "#1976D2"  # Blue button with white text
            textbutton "Sell Items" action Show("shop_sell") background "#4CAF50" hover_background "#45A049"  # Green button with white text
            textbutton "Exit Shop" action Jump("show_date") background "#f44336" hover_background "#e41e10"  # Red button with white text



label shop_menu:
    call screen shop_navigation