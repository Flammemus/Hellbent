import survey
import os
import random

from ascii_magic import from_image
from art import *

from classes import *
from objects import *

def clear_console():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

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

def printAllEquipment(type):
    if player.equipment[type] != None:
        printEquipment(player.equipment[type], label=f"Equipped {type}: ")
    else:
        print(f"Equipped {type}: None")

def battle(player, enemy):
    tprint(enemy.name)
    enemyProfile = from_image(enemy.image)
    enemyProfile.to_terminal(columns=40)
    print("@=======================================@\n")

    print(f"{player.name} Battling")
    print(f"{enemy.name} {enemy.health}")

gameloop = True
while gameloop:

    player.updateStats()

    print()
    actionIndex = survey.routines.select(f"{currentArea.name} actions: ", options = currentArea.actions)
    action = currentArea.actions[actionIndex]
    print()

    clear_console()
    if action == "Hunt":
        enemy = random.choice(currentArea.enemies)
        battle(player, enemy)
    
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

        printAllEquipment("Weapon")
        printAllEquipment("Armor")
        printAllEquipment("Talisman")

        if not player.inventory:
            print("\nYour inventory is empty.\n")
            continue

        print("\nYour items:\n")
        for item in player.inventory:
            print(f"{item.name} - {item.type}")
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