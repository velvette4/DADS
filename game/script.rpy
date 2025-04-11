init python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)
    

define v = Character("Varric",callback=speaker("varric"))
define s = Character("Solas")
define f = Character("Felassan")
define c = Character("Cassandra")
define cu = Character("Cullen")
define e = Character("Elgar'nan")
define m = Character("Morrigan")
define h = Character("Harding")
define me = Character("Merrill")
define a = Character("Abelas")
define an = Character("Anders")
define l = Character("Leliana")
define u = Character("???")
define s = Character("[player_name]")

default player_money = 0

image farm = "images/farm.png"
image bb = "images/bg/bb-day.jpg"
image bbnight = "images/bg/bb-night.jpg"

# Varric composed image with base and dynamic mouth (no blinking)
image varric = LiveComposite(
    (628, 1080),  # You can adjust this resolution if needed
    (-50, 0), "images/sprite/varric/SPR-DOLL-VARRIC_Spring.png",
    (-50, 0), WhileSpeaking("varric", "images/sprite/varric/SPR-DOLL-VARRIC_EMOTION-Neutral_mouthopen.png", "images/sprite/varric/SPR-DOLL-VARRIC_EMOTION-Neutral_mouthclosed.png",),
)

image varrichappy = LiveComposite(
    (628, 1080),  # You can adjust this resolution if needed
    (-50, 0), "images/sprite/varric/SPR-DOLL-VARRIC_Spring.png",
    (-50, 0), "images/sprite/varric/SPR-DOLL-VARRIC_EMOTION-Happy.png",
)


image varricblush = "images/sprite/varric/SPR-DOLL-VARRIC_EMOTION-Blush.png"


image solas = "images/sprite/solas/SPR-SOLAS_SPRINGcasual_Neutral-QUIET.png"
image solastalk = "images/sprite/solas/SPR-SOLAS-FACE_SPRINGcasual_Neutral-TALKING.png"
image solasangry = "images/sprite/solas/SPR-SOLAS-FACE_SPRINGcasual_Angry.png"
image solasblush = "images/sprite/solas/SPR-SOLAS-FACE_SPRINGcasual_Blush.png"
image solassad = "images/sprite/solas/SPR-SOLAS-FACE_SPRINGcasual_Sad.png"
image solassurprised = "images/sprite/solas/SPR-SOLAS-FACE_SPRINGcasual_Surprised.png"

    

init python:
    import random
    

default shop_items = {
    "Wheat": {"price": 3},
    "Elfroot": {"price": 4},
    "Blood Lotus": {"price": 5},
    "Tea": {"price": 6},
    "Coffee": {"price": 6},
    "Cheese": {"price": 6},
    "Orange": {"price": 6},
    "Apricot": {"price": 6},
    "Deep Mushroom": {"price": 7},
    "Embrium": {"price": 15},
    "Rose": {"price": 15},
    "Anderfel's Mint": {"price": 15},
    "Royal Elfroot": {"price": 35},
    "Crystal Grace": {"price": 75},
    "Felandaris": {"price": 75},
    "Andraste's Grace": {"price": 75}
}

default varricm1 = False
default varricf1 = False
default varricf2 = False
default varricheart = 0

default planting_mode = False

default harvest_mode = False

default current_seed = ""

default current_fertilizer = ""

default fertilizer_mode = False

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


default a1_fertilized = False
default b1_fertilized = False
default c1_fertilized = False
default d1_fertilized = False
default d2_fertilized = False
default d3_fertilized = False
default e1_fertilized = False
default e2_fertilized = False
default e3_fertilized = False
default f1_fertilized = False
default f2_fertilized = False
default f3_fertilized = False
default a2_fertilized = False
default b2_fertilized = False
default c2_fertilized = False
default a3_fertilized = False
default b3_fertilized = False
default c3_fertilized = False


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

default a1_plant_state = 0
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

default hawkfeather = False

init python:
    def update_inventory(item, amount):
        if item in inventory:
            inventory[item] += amount
        else:
            inventory[item] = amount

    # Function to check if enough money is available
    def can_buy(item, amount, money):
        return money >= shop_items[item] * amount


init python:
    def required_growth(plant):
        if plant == "Cheese":
            return 5
        elif plant == "Elfroot":
            return 10
        elif plant == "Blood Lotus":
            return 13
        elif plant == "Royal Elfroot":
            return 15
        else:
            return 0

screen money_display():
    frame:
        xalign 0.02  # Position the UI (top-left corner)
        yalign 0.02  # Position the UI (top-left corner)
        background "#0008"  # Semi-transparent background
        padding (10, 10)  # Correct padding as a tuple (left, top)
        vbox:
            spacing 5
            text "Money: $[player_money]" color "#fff" xalign 0.5 yalign 0.1  # Position at the top center
            for item_name, quantity in inventory.items():
                text f"{item_name}: {quantity}" color "#fff" xalign 0.5 yalign 0.2
            for gift_name, quantity in giftinventory.items():
                text f"{gift_name}: {quantity}" color "#fff" xalign 0.5 yalign 0.3

screen calendar_ui():
    frame:
        xalign 0.99  # Position the UI (top-left corner)
        yalign 0.02 
        background "#0008"  # Semi-transparent background
        padding (10, 10)  # Correct padding as a tuple (left, top)
        vbox:
            spacing 5
            text "Date: [calendar.get_date()]" color "#fff" size 20
            # Check for special event and display it on the UI
            if calendar.current_day == 3 and calendar.seasons[calendar.current_season_index] == "Spring":
                text "Event: Spring Festival 🎉" color "#ff0" size 18

default inventory = {"Elfroot": 1}
default giftinventory = {}

init python:
    def add_item(item_name, quantity):
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity

    def remove_item(item_name, quantity):
        if item_name in inventory:
            inventory[item_name] -= quantity
            if inventory[item_name] <= 0:
                del inventory[item_name]

init python:
    def add_gift(gift_name, quantity):
        if gift_name in giftinventory:
            giftinventory[gift_name] += quantity
        else:
            giftinventory[gift_name] = quantity

    def remove_gift(gift_name, quantity):
        if gift_name in giftinventory:
            giftinventory[gift_name] -= quantity
            if giftinventory[gift_name] <= 0:
                del giftinventory[gift_name]



init python:
    class Calendar:
        def __init__(self):
            self.seasons = ["Spring", "Summer", "Autumn", "Winter"]
            self.days_per_season = 28
            self.current_day = 1
            self.current_season_index = 0

        def get_date(self):
            season = self.seasons[self.current_season_index]
            return f"{self.current_day} {season}"

        def next_day(self):
            self.current_day += 1
            if self.current_day > self.days_per_season:
                self.current_day = 1
                self.current_season_index += 1
                if self.current_season_index >= len(self.seasons):
                    self.current_season_index = 0

init python:
    calendar = Calendar()

label start:
    show screen money_display
    show screen calendar_ui
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    
    jump show_date