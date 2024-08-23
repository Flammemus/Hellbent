from classes import *
from objects import *
import survey

# playerName = input("Username: ")
playerName = "Flabbe"

currentArea = wheatField
areaNames = [area.name for area in Area.list]

player = Player(name=playerName, health=100, healthMax=100, energy=50, energyMax=50, damage=0, defense=0)
player.equipGear(unarmed)
player.equipGear(nude)
player.equipGear(noTalisman)

player.inventory.append(rustySword)
player.inventory.append(swordOfPower)
player.inventory.append(revealingBikini)
player.inventory.append(goblinTrophy)
player.inventory.append(ratLeather)

def printEquipment(equipment, label=""):

    basicInfo = f"{label}{equipment.name}"
    attributeDetails = [f"{attr.capitalize()}: {value}" for attr, value in vars(equipment).items() if value != 0 and attr not in ['name']] # Thank you, ChatGPT
    allDetails = [basicInfo] + attributeDetails

    print(" - ".join(allDetails))

def battle(enemy):
    print("Battling")
    print(enemy)
    print(f"{enemy.name} {enemy.health}")

gameloop = True
while gameloop:

    player.updateStats()

    print()
    actionIndex = survey.routines.select(f"{currentArea.name} actions: ", options = currentArea.actions)
    action = currentArea.actions[actionIndex]
    print()

    if action == "Hunt":
        battle(mudRat)
    
    if action == "Stats":
        print("Stats:")
        print(f"Health: {player.health} / {player.healthMax} | Energy: {player.energy} / {player.energyMax}")
        print(f"Base damage: {player.damage} | Base defense: {player.defense}")
    
    if action == "Look Around":
        print("Looking around")
    
    if action == "Travel":
        travelDestinationIndex = survey.routines.select("Available destinations: ", options = areaNames)
        travelDestination = Area.list[travelDestinationIndex]
        print()

        currentArea = travelDestination
        print("You've arrived at", currentArea)
    
    if action == "Inventory":
        inventoryNames = [item.name for item in player.inventory]
        equipmentInventoryNames = [item.name for item in player.inventory if isinstance(item, Equipment)]

        if player.equipment["Weapon"] != None:
            printEquipment(player.equipment["Weapon"], label="Equipped Weapon: ")
        else:
            print(f"Equipped weapon: None")
        if player.equipment["Armor"] != None:
            printEquipment(player.equipment["Armor"], label="Equipped Armor: ")
        else:
            print(f"Equipped Armor: None")
        if player.equipment["Talisman"] != None:
            printEquipment(player.equipment["Talisman"], label="Equipped Talisman: ")
        else:
            print(f"Equipped Talisman: None\n")

        if not player.inventory:
            print("\nYour inventory is empty.\n")
            continue

        print("\nYour items:\n")
        for item in player.inventory:
            printEquipment(item)
        print()

        action = survey.routines.select("Available action:", options = ("Inspect", "Equip", "Back"))

        if action == 0:
            print("Inspecting")

            itemToInspectIndex = survey.routines.select("Your items: ", options = inventoryNames)
            itemToInspect = player.inventory[itemToInspectIndex]
            print()

            printEquipment(itemToInspect)
        
        if action == 1:
            print("Equipping")

            itemToEquipIndex = survey.routines.select("Equippable gear: ", options = equipmentInventoryNames)
            itemToEquip = player.inventory[itemToEquipIndex]
            print()

            Player.equipGear(player, itemToEquip)
            Player.updateStats(player)

        if action == 2:
            print("Returning")