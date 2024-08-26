from classes import *

# === SKILLS ===

# --- Active ---

hewingStrike = Active(bookName="Manual of Hewing Strike", worth=200, type="Active", name="Hewing Strike", damage=20, energyCost=15, cooldown=3, bonus=None)

# === ENEMIES ===

mudRat = Enemy(name="Mud Rat", health=50, healthMax=50, energy=50, energyMax=50, damage=2, defense=0, image="images/mudRat.jpg")
grassHopper = Enemy(name="Grass Hopper", health=25, healthMax=25, energy=50, energyMax=50, damage=1, defense=0, image="images/mudRat.jpg")

# === AREAS ===

wheatField = Area("Wheat Field", actions=["Hunt", "Stats", "Inventory", "Travel"], enemies=[mudRat, grassHopper])
willowForest = Area("Willow Forest", actions=["Hunt", "Stats", "Inventory", "Travel"], enemies=["Bird", "Spider"])
safeTown = Area("Safe Town", actions=["Stats", "Inventory", "Travel"], enemies=[])

# === ITEMS ===

ratLeather = Item("Rat Leather", type="Valuable", worth=50)

# === EQUIPMENT ===

unarmed = Equipment("Unarmed", type="Weapon", damage=1, defense=0, energy=0, worth=0, description="Fuck it, we brawl")
nude = Equipment("Nude", type="Armor", damage=0, defense=0, energy=0, worth=0, description="As nude as a newborn child")
noTalisman = Equipment("None", type="Talisman", damage=0, defense=0, energy=0, worth=0, description="As nude as a newborn child")

rustySword = Equipment("Rusty Shortsword", type="Weapon", damage=5, defense=2, energy=0, worth=100, description=0)
swordOfPower = Equipment("Sword Of Power", type="Weapon", damage=5, defense=0, energy=5, worth=100, description=0)
revealingBikini = Equipment("Revealing Bikini", type="Armor", damage=0, defense=3, energy=15, worth=100, description="The legendary sought after bikini that is a bit too revealing")
goblinTrophy = Equipment("Goblin Trophy", type="Talisman", damage=0, defense=1, energy=5, worth=100, description="A goblin trophy in the form of its ear on a necklace chain")