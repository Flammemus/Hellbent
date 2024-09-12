class Player:
    def __init__(self, name, money, stats):
        self.name = name
        self.money = money
        self.stats = stats
        self.equipment = {
            "Weapon": None,
            "Armor": None,
            "Talisman": None
        }
        self.inventory = []
        self.equipmentInventory = []
        self.itemInventory = []
        self.skills = []

    def equipGear(player, item):
        if isinstance(item, Weapon):
            player.equipment["Weapon"] = item
    
        elif isinstance(item, Equipment):
            player.equipment[item.type] = item
        
        player.updateStats()

    def updateStats(self):
        self.stats["HealthMax"] = 100
        self.stats["Health"] = self.stats["HealthMax"]
        self.stats["EnergyMax"] = 50
        self.stats["Energy"] = self.stats["EnergyMax"]
        self.stats["Damage"] = 0
        self.stats["Defence"] = 0
        self.stats["Weight"] = 0
        self.stats["Speed"] = 0
        self.stats["CritChance"] = 5
        self.stats["CritEff"] = 50

        self.stats["Speed"] = (self.stats["Speed"] - (self.stats["Weight"] / 2))

        for _, item in self.equipment.items():
            if item:
                for stat, value in item.stats.items():
                    if value is not None:
                        self.stats[stat] += value
    
    def sortInventory(self):
        self.equipmentInventory.clear()
        self.itemInventory.clear()
        self.inventory.sort(key=lambda item: item.type)

        for item in self.inventory:
            if isinstance(item, Equipment) or isinstance(item, Weapon):
                self.equipmentInventory.append(item)
            elif isinstance(item, Item) or isinstance(item, Treatise):
                self.itemInventory.append(item)
    
    def setup(self):
        self.stats["Health"] = self.stats["HealthMax"]
        self.stats["Energy"] = self.stats["EnergyMax"]

class Enemy:
    def __init__(self, name, image, itemPool, stats):
        self.name = name
        self.image = image
        self.itemPool = itemPool
        self.stats = stats

    def setup(self):
        self.health = self.stats["HealthMax"]
        self.energy = self.stats["EnergyMax"]

class Weapon:
    list = []
    def __init__(self, name, type, worth, description, stats):
        self.name = name
        self.type = type
        self.worth = worth
        self.description = description
        self.stats = stats

class Equipment:
    list = []
    def __init__(self, name, type, worth, description, stats):
        self.name = name
        self.type = type
        self.worth = worth
        self.description = description
        self.stats = stats

        Equipment.list.append(self)

class Item:
    def __init__(self, name, type, worth):
        self.name = name
        self.type = type
        self.worth = worth

class Treatise:
    def __init__(self, name, worth, type, skill, description):
        self.name = name
        self.worth = worth
        self.type = type
        self.skill = skill
        self.description = description

class Area:
    list = []
    def __init__(self, name, actions, enemies):
        self.name = name
        self.actions = actions
        self.enemies = enemies
    
        Area.list.append(self)
    
    def __repr__(self):
        return self.name

class Active():
    def __init__(self, type, name, damage, energyCost, cooldown, bonus):
        self.type = type
        self.name = name
        self.damage = damage
        self.energyCost = energyCost
        self.cooldown = cooldown
        self.bonus = bonus

class Passive():
    def __init__(self, type, name, bonus):
        self.type = type
        self.name = name
        self.bonus = bonus