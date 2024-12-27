define v = Character("Varric")
define u = Character("???")
define s = Character("[player_name]")
define cheese = 0
$ price_per_cheese = 10
default player_money = 0

default cheese_seeds = 1
default elfroot_seeds = 1
default royal_elfroot_seeds = 1
default blood_lotus_seeds = 1

default planting_mode = False

default harvest_mode = False

default current_seed = ""

# Default variables to track the planted seeds for each tile
default a1_planted = ""
default b1_planted = ""
default c1_planted = ""
default d1_planted = ""
default d2_planted = ""
default d3_planted = ""
default e1_planted = ""
default e2_planted = ""
default e3_planted = ""
default f1_planted = ""
default f2_planted = ""
default f3_planted = ""
default a2_planted = ""
default b2_planted = ""
default c2_planted = ""
default a3_planted = ""
default b3_planted = ""
default c3_planted = ""


# Continue for all your tiles...


default watering_mode = False

default a1watered = False
default a2watered = False
default a3watered = False
default b1watered = False
default b2watered = False
default b3watered = False
default c1watered = False
default c2watered = False
default c3watered = False
default d1watered = False
default d2watered = False
default d3watered = False
default e1watered = False
default e2watered = False
default e3watered = False
default f1watered = False
default f2watered = False
default f3watered = False

default a1planted = False
default a2planted = False
default a3planted = False
default b1planted = False
default b2planted = False
default b3planted = False
default c1planted = False
default c2planted = False
default c3planted = False
default d1planted = False
default d2planted = False
default d3planted = False
default e1planted = False
default e2planted = False
default e3planted = False
default f1planted = False
default f2planted = False
default f3planted = False

default a1harvestable = False
default a2harvestable = False
default a3harvestable = False
default b1harvestable = False
default b2harvestable = False
default b3harvestable = False
default c1harvestable = False
default c2harvestable = False
default c3harvestable = False
default d1harvestable = False
default d2harvestable = False
default d3harvestable = False
default e1harvestable = False
default e2harvestable = False
default e3harvestable = False
default f1harvestable = False
default f2harvestable = False
default f3harvestable = False

default a1plant_type = ""
default a2plant_type = ""
default a3plant_type = ""
default b1plant_type = ""
default b2plant_type = ""
default b3plant_type = ""
default c1plant_type = ""
default c2plant_type = ""
default c3plant_type = ""
default d1plant_type = ""
default d2plant_type = ""
default d3plant_type = ""
default e1plant_type = ""
default e2plant_type = ""
default e3plant_type = ""
default f1plant_type = ""
default f2plant_type = ""
default f3plant_type = ""


image farm = "images/farm.png"

default a1_plant_state = 0  # Default growth state for the plant
default b1_plant_state = 0
default c1_plant_state = 0
default d1_plant_state = 0
default d2_plant_state = 0
default d3_plant_state = 0
default e1_plant_state = 0
default e2_plant_state = 0
default e3_plant_state = 0
default f1_plant_state = 0
default f2_plant_state = 0
default f3_plant_state = 0
default a2_plant_state = 0
default b2_plant_state = 0
default c2_plant_state = 0
default a3_plant_state = 0
default b3_plant_state = 0
default c3_plant_state = 0




init python:
    def required_growth(plant):
        if plant == "cheese":
            return 5
        elif plant == "elfroot":
            return 10
        elif plant == "blood lotus":
            return 13
        elif plant == "royal elfroot":
            return 15
        else:
            return 0

# init python:
#     def plant_crop(row, col):
#         # Ensure `isplanted` and `plant_type` are global so they can be accessed
#         global isplanted, plant_type

#         # Check if the tile is already planted
#         if not isplanted[row][col]:
#             isplanted[row][col] = True
#             # Prompt for a crop selection or assign a default crop
#             plant_type[row][col] = renpy.choice(["Cheese", "Elfroot", "Blood Lotus", "Royal Elfroot"])

#         # Restart the interaction to refresh the screen
#         renpy.restart_interaction()


screen money_display():
    frame:
        align (0.95, 0.05)  # Position it in the top-right corner
        padding (10, 10)  # Correct padding as a tuple (left, top)
        background "#0008"  # Semi-transparent background
        text "Money: $[player_money]" size 22 color "#FFFFFF"

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

# Function to add items to the inventory
default inventory = []

init python:
    def add_item(item_name, quantity):
        """Adds an item to the inventory."""
        # Check if the item already exists
        for item in inventory:
            if item["name"] == item_name:
                item["quantity"] += quantity
                return
        # If item doesn't exist, add it to the inventory
        inventory.append({"name": item_name, "quantity": quantity})

    def remove_item(item_name, quantity):
        """Removes an item from the inventory."""
        for item in inventory:
            if item["name"] == item_name:
                item["quantity"] -= quantity
                # Remove item if quantity is 0 or less
                if item["quantity"] <= 0:
                    inventory.remove(item)
                return

init python:
    def get_inventory_string():
        """Returns a string representation of the inventory."""
        if not inventory:
            return "Your inventory is empty."
        return ", ".join([f"{item['name']} x{item['quantity']}" for item in inventory])




init python:
    class Calendar:
        def __init__(self):
            # Define seasons and days per season
            self.seasons = ["Spring", "Summer", "Autumn", "Winter"]
            self.days_per_season = 30
            self.current_day = 1
            self.current_season_index = 0

        def get_date(self):
            # Get the current season and day
            season = self.seasons[self.current_season_index]
            return f"{self.current_day} {season}"

        def next_day(self):
            # Advance the calendar by one day
            self.current_day += 1
            if self.current_day > self.days_per_season:
                self.current_day = 1
                self.current_season_index += 1
                if self.current_season_index >= len(self.seasons):
                    self.current_season_index = 0

# Initialize the calendar globally at the start of the game
init python:
    calendar = Calendar()

label start:
    show screen money_display
    show screen calendar_ui
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    jump show_date
    

    # Return to the main menu
    return
