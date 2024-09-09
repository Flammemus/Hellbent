class Player:
    def __init__(self, name, money, stats):
        self.name = name
        self.money = money
        self.stats = {
            "Health": None,
            "HealthMax": None,
            "Energy": None,
            "EnergyMax": None,
            "Damage": None,
            "Defence": None,
            "Weight": None,
            "Speed": None,
            "CritChance": None,
            "CritEff": None
        }
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
        player.equipment[item.type] = item

    def updateStats(self):
        self.stats["HealthMax"] = 0
        self.stats["Defence"] = 0
        self.stats["Weight"] = 0
        self.stats["Speed"] = 10
        self.stats["EnergyMax"] = 50
        self.stats["CritChance"] = 5
        self.stats["CritEff"] = 50

        for _, item in self.equipment.items():
            if item:
                for attr in ['Damage', 'Defence', 'EnergyMax', 'CritChance', 'CritEff', 'Weight']:
                    value = getattr(item, attr, None)
                    if value is not None:
                        setattr(self, attr, getattr(self, attr) + value)
    
    def sortInventory(self):
        self.equipmentInventory.clear()
        self.itemInventory.clear()
        self.inventory.sort(key=lambda item: item.type)

        for item in self.inventory:
            if isinstance(item, Equipment):
                self.equipmentInventory.append(item)
            elif isinstance(item, Item) or isinstance(item, Treatise):
                self.itemInventory.append(item)
    
    def setup(self):
        self.stats["Health"] = self.stats["HealthMax"]
        self.stats["Energy"] = self.stats["EnergyMax"]

class Enemy:
    def __init__(self, name, image, itemPool, stats):
        self.name = name
        self.stats = {
            "Health": None,
            "HealthMax": None,
            "Energy": None,
            "EnergyMax": None,
            "Damage": None,
            "Defence": None,
            "Weight": None,
            "Speed": None,
            "CritChance": None,
            "CritEff": None
        }
        self.image = image
        self.itemPool = itemPool

    def setup(self):
        self.health = self.stats["HealthMax"]
        self.energy = self.stats["EnergyMax"]
        
class Equipment:
    list = []
    def __init__(self, name, type, weaponType, worth, damage, critChance, critEff, defense, speed, energy, description):
        self.name = name
        self.type = type
        self.weaponType = weaponType
        self.worth = worth
        self.damage = damage
        self.critChance = critChance
        self.critEff = critEff
        self.defense = defense
        self.speed = speed
        self.energy = energy
        self.description = description

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