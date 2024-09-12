import os
import sys

from classes import *

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    

# === SKILLS ===

# --- Active ---

basicAttack = Active(type="Active", name="Basic Attack", damage=0, energyCost=0, cooldown=0, bonus=0)
hewingStrike = Active(type="Active", name="Hewing Strike", damage=20, energyCost=15, cooldown=3, bonus=0)

escapeBattle = Active(type="Active", name="Escape Battle", damage=0, energyCost=15, cooldown=0, bonus=0)

# --- Passives ---

resilience = Passive(type="Passive", name="Resilience", bonus="5 Defense")

# === ITEMS ===

ratLeather = Item("Rat Leather", type="Valuable", worth=50)

# --- Treatise ---

hewingStrikeTreatise = Treatise("Manual of Hewing Strike", worth=250, type="Treatise", skill=hewingStrike, description="A strike so hard and hewing..")

# === EQUIPMENT ===

# Stats cheat sheet -  "Health": None, "HealthMax": None, "Energy": None, "EnergyMax": None, "Damage": None, "Defence": None, "Weight": None, "Speed": None, "CritChance": None, "CritEff": None

unarmed = Weapon("Unarmed", type="Fist", worth=0, description="Fuck it, we brawl", stats={"Damage": 6})
nude = Equipment("Nude", type="Armor", worth=0, description="As nude as a newborn child", stats={"Speed": 10})
noTalisman = Equipment("Empty", type="Talisman", worth=0, description="Even a rope would've done something..", stats={})

rustySword = Weapon("Rusty Shortsword", type="Sword", worth=200, description=0, stats={"Damage": 8, "Weight": 10, "CritChance": 2, "CritEff": 10})
swordOfPower = Weapon("Sword Of Power", type="Sword", worth=100, description=0, stats={"EnergyMax": 15, "Damage": 15, "Defence": 5, "Weight": 25, "CritChance": 8, "CritEff": 25})

revealingBikini = Equipment("Revealing Bikini", type="Armor", worth=100, description="The legendary sought after bikini that is a bit too revealing", stats={"Energy": 10, "Defence": 2, "Weight": 2, "Speed": 5, "CritChance": 5})
goblinTrophy = Equipment("Goblin Trophy", type="Talisman", worth=100, description="A goblin trophy in the form of its ear on a necklace chain", stats={"Health": 15, "Weight": 5, "CritEff": 15})

# === ENEMIES ===

placeHolder = get_resource_path("images/mudRat.jpg")
mudRatImage = get_resource_path("images/mudRat.jpg")

mudRat = Enemy(name="Mud Rat", image=mudRatImage, itemPool=[ratLeather], stats={
    "Health": 50,
    "HealthMax": 50,
    "Energy": 30,
    "EnergyMax": 30,
    "Damage": 10,
    "Defence": 5,
    "Weight": 3,
    "Speed": 8,
    "CritChance": 5,
    "CritEff": 50
})
grassHopper = Enemy(name="Grass Hopper", image=placeHolder, itemPool=[hewingStrikeTreatise], stats={
    "Health": 50,
    "HealthMax": 50,
    "Energy": 30,
    "EnergyMax": 30,
    "Damage": 10,
    "Defence": 5,
    "Weight": 3,
    "Speed": 8,
    "CritChance": 5,
    "CritEff": 50
})

# === AREAS ===

wheatField = Area("Wheat Field", actions=["Hunt", "Stats", "Inventory", "Travel"], enemies=[mudRat, grassHopper])
willowForest = Area("Willow Forest", actions=["Hunt", "Stats", "Inventory", "Travel"], enemies=[mudRat, grassHopper])
safeTown = Area("Safe Town", actions=["Stats", "Inventory", "Travel"], enemies=[])