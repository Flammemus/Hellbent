import survey
import os
import random

from ascii_magic import from_image # Copyright (c) 2020 Leandro Barone. Usage is provided under the MIT License.
from art import *

from classes import *
from objects import *

tprint("\nTbRpg2")
print("Github: https://github.com/Flammemus/TbRpg2")
print("Playing on ver. 0.1.6")

# 1.0.0 = full release
# 0.1.0 = content update
# 0.0.1 = patch

# TODO

# item-drops from enemies with rarity
# usable treatises
# inventory revamp | one main inventory where a for loop sorts items in its respected inventory i.e equipment inv, item inv, consumable inv dependant on item type

# shops and reputation
# bounties
# dungeons

testAccount = True

if testAccount:
    playerName = "JohnRPG"
else:
    playerName = input("\nUsername: ")

currentArea = wheatField
areaNames = [area.name for area in Area.list]

player = Player(name=playerName, money=20, stats={
    "Health": 100,
    "HealthMax": 100,
    "Energy": 50,
    "EnergyMax": 50,
    "Damage": 0,
    "Defence": 10,
    "Weight": 0,
    "Speed": 10,
    "CritChance": 5,
    "CritEff": 50
})

player.equipGear(unarmed)
player.equipGear(nude)
player.equipGear(noTalisman)

player.inventory.append(rustySword)
player.inventory.append(swordOfPower)
player.inventory.append(revealingBikini)
player.inventory.append(goblinTrophy)

player.inventory.append(ratLeather)
player.inventory.append(hewingStrikeTreatise)

player.skills.append(basicAttack)
player.skills.append(hewingStrike)
player.skills.append(escapeBattle)

if testAccount:
    Player.equipGear(player, swordOfPower)
    Player.updateStats(player)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    damage = player.stats["Damage"] * ((selectedSkill.damage / 100) + 1)
    randomFloat = random.random() * 100
    randomPercent = round(randomFloat, 2)

    isCritical = False
    if player.stats["CritChance"] >= randomPercent:
        damage *= ((player.stats["CritEff"] / 100) + 1)
        isCritical = True

    return damage, isCritical

def enemyDamage(enemy):
    damage = enemy.damage

    return damage

def battleWon(player, enemy, log):
    print(f"You successfully defeated the {enemy.name}")

def battleLost(player, enemy, log):
    print(f"You fell in battle to{enemy.name}")

# ==================== BATTLE ====================

def battle(player, enemy):
    player.setup()
    enemy.setup()
    isPlayerTurn = False

    log = []
    log.reverse()
    turnCounter = 0

    if player.stats["Speed"] >= enemy.stats["Speed"]:
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
        print(f"Health: {int(enemy.stats["Health"])} / {int(enemy.stats["HealthMax"])} | Energy: {int(enemy.stats["Energy"])} / {int(enemy.stats["EnergyMax"])}\n")

        print(f"{enemy.name} item pool:")
        for i in enemy.itemPool:
            print(f"- {i.name}")

        print()

        enemyProfileImage = from_image(enemy.image)
        enemyProfileImage.to_terminal(columns=40)
        print()

        tprint(player.name)
        print(f"Health: {int(player.stats["Health"])} / {int(player.stats["HealthMax"])} | Energy: {int(player.stats["Energy"])} / {int(player.stats["EnergyMax"])}\n")

        print(f"Log:  |  Turn: {turnCounter}\n")
        for i in log:
            print(f"- {i}")
        print()

        if enemy.health <= 0:
            battleWon(player, enemy, log)
            ongoing = False
        
        elif player.health <= 0:
            battleLost(player, enemy, log)
            ongoing = False

        # ==== Player turn ====

        if isPlayerTurn:

            skillsNames = [item.name for item in player.skills]
            skillsNamesAndTypes = [f"{item.name} - {item.type} - {item.damage}%" for item in player.skills]

            actionIndex = survey.routines.select(f"Actions: ", options = skillsNamesAndTypes)
            selectedSkill = player.skills[actionIndex]
            action = skillsNames[actionIndex]

            if action == "Escape Battle":
                ongoing = False

            damageDealt, isCritical = (playerDamage(player, selectedSkill, log))

            if isCritical:
                log.append(f"{player.name} uses {action} and critical hits {enemy.name} for {int(damageDealt)} damage!")
            else:
                log.append(f"{player.name} uses {action} and hits {enemy.name} for {int(damageDealt)} damage")

            enemy.health -= damageDealt
            if enemy.stats["Health"] <= 0:
                enemy.stats["Health"] = 0

            turnCounter += 1

            isPlayerTurn = False
        
        elif not isPlayerTurn:
            log.append(f"{enemy.name} hits {player.name} for {enemyDamage(enemy)} damage")
            player.stats["Health"] -= enemyDamage(enemy)

            isPlayerTurn = True

gameloop = True
while gameloop:

    player.updateStats()
    player.sortInventory()

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
        print(f"Health: {player.stats["Health"]} / {player.stats["HealthMax"]} | Energy: {player.stats["Energy"]} / {player.stats["EnergyMax"]}\n")

        print(f"Base damage: {player.stats["Damage"]}")
        print(f"Crit chance: {player.stats["CritChance"]}%")
        print(f"Crit efficiency: {player.stats["CritEff"]}%\n")

        print(f"Defense: {player.stats["Defence"]}")
        print(f"Speed: {player.stats["Speed"]}")
    
    elif action == "Travel":
        tprint("Travel")
        travelDestinationIndex = survey.routines.select("Available destinations: ", options = areaNames)
        travelDestination = Area.list[travelDestinationIndex]
        print()

        currentArea = travelDestination
        print("You've arrived at", currentArea)
    
    elif action == "Inventory":
        tprint("Inventory")

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

        print("Items:\n")
        print(f"Tones: {player.money}\n")
        for item in player.itemInventory:
            print(f"{item.name} - {item.type}")
        print()

        action = survey.routines.select("Available action:", options = ("Inspect", "Equip", "Unequip", "Back"))

        if action == 0:
            itemToInspectIndex = survey.routines.select("Your items: ", options = inventoryNames)
            itemToInspect = player.inventory[itemToInspectIndex]

            print()
            printEquipment(itemToInspect)

        elif action == 1:
            itemToEquipIndex = survey.routines.select("Equippable gear: ", options = equipmentInventoryNames)
            itemToEquip = player.equipmentInventory[itemToEquipIndex]

            Player.equipGear(player, itemToEquip)
            Player.updateStats(player)
        
        elif action == 2:
            itemToUnequipList = []
            itemToUnequipList.append(f"Weapon: {player.equipment["Weapon"].name}")
            itemToUnequipList.append(f"Armor: {player.equipment["Armor"].name}")
            itemToUnequipList.append(f"Talisman: {player.equipment["Talisman"].name}")

            itemToUnequipIndex = survey.routines.select("Unequip gear: ", options = itemToUnequipList)

            if itemToUnequipIndex == 0:
                Player.equipGear(player, unarmed)
            if itemToUnequipIndex == 0:
                Player.equipGear(player, nude)
            if itemToUnequipIndex == 0:
                Player.equipGear(player, noTalisman)
            
            Player.updateStats(player)

        elif action == 3:
            print("Returning")