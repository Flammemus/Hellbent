import survey
import os
import random
import time

from ascii_magic import from_image # Copyright (c) 2020 Leandro Barone. Usage is provided under the MIT License.
from art import *

from classes import *
from objects import *

print("Playing on ver. 1.05")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# playerName = input("Username: ")
playerName = "Testing"

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

if player.name == "Testing":
    Player.equipGear(player, swordOfPower)
    Player.updateStats(player)

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



def playerDamage(player, selectedSkill):
    damage = player.damage * ((selectedSkill.damage / 100) + 1)

    return damage

def enemyDamage(enemy):
    damage = enemy.damage

    return damage

def playerTurn(player, enemy):

    skillsNames = [item.name for item in player.skills]
    # skillsNames.append("Attempt escape")
    skillsNamesAndTypes = [f"{item.name} - {item.type} - {item.damage}%" for item in player.skills]
    # skillsNamesAndTypes.append("Attempt escape")

    actionIndex = survey.routines.select(f"Actions: ", options = skillsNamesAndTypes)
    selectedSkill = player.skills[actionIndex]
    action = skillsNames[actionIndex]

    print(f"{action} hit for {playerDamage(player, selectedSkill)}")

    enemy.health -= playerDamage(player, selectedSkill)
    if enemy.health <= 0:
        enemy.health = 0

def enemyTurn(player, enemy):
    # print(f"{enemy.name} hits for {enemyDamage(enemy)}")
    player.health -= enemyDamage(enemy)

def battleWon(player, enemy):
    print(f"You defeated {enemy.name}")

def battleLost(player, enemy):
    print(f"You lost to {enemy.name}")


def battle(player, enemy):
    player.setup()
    isPlayerTurn = False

    if player.speed >= enemy.speed:
        isPlayerTurn = True
        print(f"{player.name} is faster and siezes the first attack against {enemy.name}!")
    else:
        isPlayerTurn = False
        print(f"{enemy.name} is faster and siezes the first attack against {player.name}!")

    ongoing = True
    while ongoing:
        clear_console()

        tprint(enemy.name)
        print(f"Health: {enemy.health} / {enemy.healthMax} | Energy: {enemy.energy} / {enemy.energyMax}\n")
        enemyProfileImage = from_image(enemy.image)
        enemyProfileImage.to_terminal(columns=40)
        print()

        tprint(player.name)
        print(f"Health: {player.health} / {player.healthMax} | Energy: {player.energy} / {player.energyMax}\n")

        if enemy.health <= 0:
            battleWon(player, enemy)
            ongoing = False
        
        elif player.health <= 0:
            battleLost(player, enemy)
            ongoing = False

        elif action == "Attempt escape":
            print("You successfully ran away")
            ongoing = False

        if isPlayerTurn:
            playerTurn(player, enemy)
            isPlayerTurn = False
        
        else:
            enemyTurn(player, enemy)
            isPlayerTurn = True

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
        selectedSkill = None
        battle(player, enemy)
    
    elif action == "Stats":
        tprint("Stats:")
        print(f"Health: {player.health} / {player.healthMax} | Energy: {player.energy} / {player.energyMax}\n")

        print(f"Base damage: {player.damage}")
        print(f"Crit chance: {player.critChance}%")
        print(f"Crit efficiency: {player.critEff}%\n")

        print(f"Defense: {player.defense}")
        print(f"Speed: {player.speed}")
    
    elif action == "Travel":
        tprint("Travel")
        travelDestinationIndex = survey.routines.select("Available destinations: ", options = areaNames)
        travelDestination = Area.list[travelDestinationIndex]
        print()

        currentArea = travelDestination
        print("You've arrived at", currentArea)
    
    elif action == "Inventory":
        tprint("Inventory")
        player.equipmentInventory.sort(key=lambda item: item.type)
        inventoryNames = [item.name for item in player.inventory]
        equipmentInventoryNames = [item.name for item in player.equipmentInventory]

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
        
        elif action == 1:
            print("Equipping")

            itemToEquipIndex = survey.routines.select("Equippable gear: ", options = equipmentInventoryNames)
            itemToEquip = player.equipmentInventory[itemToEquipIndex]
            print()

            Player.equipGear(player, itemToEquip)
            Player.updateStats(player)

        elif action == 2:
            print("Returning")