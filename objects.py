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

unarmed = Equipment("Unarmed", type="Weapon", weaponType="Fist", worth=0, damage=5, critChance=0, critEff=0, defense=0, speed=2, energy=0, description="Fuck it, we brawl")
nude = Equipment("Nude", type="Armor", weaponType=0, worth=0, damage=0, critChance=0, critEff=0, defense=0, speed=2, energy=0, description="As nude as a newborn child")
noTalisman = Equipment("Empty", type="Talisman", weaponType=0, worth=0, damage=0, critChance=0, critEff=0, defense=0, speed=0, energy=0, description="Even a rope would've done something..")

rustySword = Equipment("Rusty Shortsword", type="Weapon", weaponType="Sword", worth=200, damage=8, critChance=2, critEff=10, defense=2, speed=0, energy=0, description=0)
swordOfPower = Equipment("Sword Of Power", type="Weapon", weaponType="Sword", worth=100, damage=20, critChance=10, critEff=5, defense=0, speed=0, energy=5, description=0)
revealingBikini = Equipment("Revealing Bikini", type="Armor", weaponType=0, worth=100, damage=0, critChance=0, critEff=0, defense=3, speed=0, energy=15, description="The legendary sought after bikini that is a bit too revealing")
goblinTrophy = Equipment("Goblin Trophy", type="Talisman", weaponType=0, worth=100, damage=0, critChance=0, critEff=12, defense=1, speed=0, energy=5, description="A goblin trophy in the form of its ear on a necklace chain")

# === ENEMIES ===

placeHolder = get_resource_path("images/mudRat.jpg")
mudRatImage = get_resource_path("images/mudRat.jpg")

mudRat = Enemy(name="Mud Rat", itemPool=[ratLeather], image=mudRatImage, stats={
    "Health": None,
    "HealthMax": 50,
    "Energy": None,
    "EnergyMax": 30,
    "Damage": 10,
    "Defence": 5,
    "Weight": 3,
    "Speed": 8,
    "CritChance": 5,
    "CritEff": 50
})
grassHopper = Enemy(name="Grass Hopper", itemPool=[hewingStrikeTreatise], image=placeHolder, stats={
    "Health": None,
    "HealthMax": 50,
    "Energy": None,
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