import survey
import os
import random
import time

from ascii_magic import from_image # Copyright (c) 2020 Leandro Barone. Usage is provided under the MIT License.
from art import *

from classes import *
from objects import *

tprint("\nTbRpg2")
print("Git: https://github.com/Flammemus/TbRpg2")
print("Playing on ver. 0.1.6")

# 1.0.0 = full release
# 0.1.0 = content update
# 0.0.1 = patch

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

testAccount = True

if testAccount:
    playerName = "JohnRPG"
else:
    playerName = input("\nUsername: ")

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

if testAccount:
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

def playerDamage(player, selectedSkill, log):
    damage = player.damage * ((selectedSkill.damage / 100) + 1)
    randomFloat = random.random() * 100
    randomPercent = round(randomFloat, 2)

    isCritical = False
    if player.critChance >= randomPercent:
        damage *= ((player.critEff / 100) + 1)
        isCritical = True

    return damage, isCritical

def enemyDamage(enemy):
    damage = enemy.damage

    return damage

def battleWon(player, enemy, log):
    print(f"You successfully defeated the {enemy.name}")

def battleLost(player, enemy, log):
    print(f"You fell in battle to{enemy.name}")

def battle(player, enemy):
    player.setup()
    enemy.setup()
    isPlayerTurn = False

    log = []
    log.reverse()
    turnCounter = 0

    if player.speed >= enemy.speed:
        isPlayerTurn = True
        log.append(f"{player.name} is faster and siezes the first attack against {enemy.name}")
    else:
        isPlayerTurn = False
        log.append(f"{enemy.name} is faster and siezes the first attack against {player.name}")

    ongoing = True
    while ongoing:
        clear_console()

        if len(log) > 8:
            del log[0]

        tprint(enemy.name)
        print(f"Health: {int(enemy.health)} / {int(enemy.healthMax)} | Energy: {int(enemy.energy)} / {int(enemy.energyMax)}\n")

        enemyProfileImage = from_image(enemy.image)
        enemyProfileImage.to_terminal(columns=40)
        print()

        tprint(player.name)
        print(f"Health: {int(player.health)} / {int(player.healthMax)} | Energy: {int(player.energy)} / {int(player.energyMax)}\n")

        print(f"Log:  |  Turn: {turnCounter}")
        for i in log:
            print(f"- {i}")
        print()

        if enemy.health <= 0:
            battleWon(player, enemy, log)
            ongoing = False
        
        elif player.health <= 0:
            battleLost(player, enemy, log)
            ongoing = False

        if isPlayerTurn:

            skillsNames = [item.name for item in player.skills]
            skillsNamesAndTypes = [f"{item.name} - {item.type} - {item.damage}%" for item in player.skills]

            actionIndex = survey.routines.select(f"Actions: ", options = skillsNamesAndTypes)
            selectedSkill = player.skills[actionIndex] if actionIndex < len(player.skills) else None
            action = skillsNames[actionIndex]

            damageDealt, isCritical = (playerDamage(player, selectedSkill, log))

            if isCritical:
                log.append(f"{player.name} uses {action} and critical hits {enemy.name} for {int(damageDealt)} damage!")
            else:
                log.append(f"{player.name} uses {action} and hits {enemy.name} for {int(damageDealt)} damage")

            enemy.health -= damageDealt
            if enemy.health <= 0:
                enemy.health = 0

            turnCounter += 1

            isPlayerTurn = False
        
        elif not isPlayerTurn:
            log.append(f"{enemy.name} hits {player.name} for {enemyDamage(enemy)} damage")
            player.health -= enemyDamage(enemy)

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