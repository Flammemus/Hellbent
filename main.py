import survey
import os
import random

from ascii_magic import from_image # Copyright (c) 2020 Leandro Barone. Usage is provided under the MIT License.
from art import *

from classes import *
from objects import *

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# playerName = input("Username: ")
playerName = "Flabbe"

currentArea = wheatField
areaNames = [area.name for area in Area.list]

player = Player(name=playerName, health=100, healthMax=100, energy=50, energyMax=50, damage=0, defense=0, speed=10, critChance=5, critEff=50)
player.equipGear(unarmed)
player.equipGear(nude)
player.equipGear(noTalisman)

player.equipmentInventory.append(rustySword)
player.equipmentInventory.append(swordOfPower)
player.equipmentInventory.append(revealingBikini)
player.equipmentInventory.append(goblinTrophy)

player.inventory.append(ratLeather)
player.inventory.append(hewingStrikeTreatise)

player.skills.append(basicAttack)
player.skills.append(hewingStrike)

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

def playerTurn(player, enemy):
    print(f"{player.name} is faster and siezes the first attack against {enemy.name}!")
    skillsNames = [item.name for item in player.skills]
    actionIndex = survey.routines.select(f"Actions: ", options = skillsNames)
    selectedSkill = player.skills[actionIndex]
    action = skillsNames[actionIndex]

    print(f"{action} hit for {player.damage * selectedSkill.damage}")

def enemyTurn(player, enemy):
    print(f"{enemy.name} is faster and siezes the first attack against {player.name}!")

def battle(player, enemy):

    tprint(enemy.name)
    print(f"Health: {enemy.health} | Energy: {enemy.energy}\n")
    enemyProfile = from_image(enemy.image)
    enemyProfile.to_terminal(columns=40)
    print()

    if player.speed >= enemy.speed:
        playerTurn(player, enemy)
    
    else:
        enemyTurn(player, enemy)

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
        tprint("Stats:")
        print(f"Health: {player.health} / {player.healthMax} | Energy: {player.energy} / {player.energyMax}\n")

        print(f"Base damage: {player.damage}")
        print(f"Crit chance: {player.critChance}%")
        print(f"Crit efficiency: {player.critEff}%\n")

        print(f"Defense: {player.defense}")
        print(f"Speed: {player.speed}")
    
    if action == "Travel":
        tprint("Travel")
        travelDestinationIndex = survey.routines.select("Available destinations: ", options = areaNames)
        travelDestination = Area.list[travelDestinationIndex]
        print()

        currentArea = travelDestination
        print("You've arrived at", currentArea)
    
    if action == "Inventory":
        tprint("Inventory")
        player.equipmentInventory.sort(key=lambda item: item.type)
        inventoryNames = [item.name for item in player.inventory]
        equipmentInventoryNames = [item.name for item in player.equipmentInventory]
        # equipmentInventoryNames = [item.name for item in player.equipmentInventory if isinstance(item, Equipment)]

        printAllEquipment("Weapon")
        printAllEquipment("Armor")
        printAllEquipment("Talisman")

        if not player.inventory:
            print("\nYour inventory is empty.\n")
            continue

        print("\nEquipment items:\n")
        for item in player.equipmentInventory:
            print(f"{item.name} - {item.type}")
        print()

        player.inventory.sort(key=lambda item: item.type)
        print("Items:\n")
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
            itemToEquip = player.equipmentInventory[itemToEquipIndex]
            print()

            Player.equipGear(player, itemToEquip)
            Player.updateStats(player)

        if action == 2:
            print("Returning")