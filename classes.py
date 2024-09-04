class Player:
    def __init__(self, name, money, health, healthMax, energy, energyMax, damage, defense, speed, critChance, critEff):
        self.name = name
        self.money = money
        self.health = health
        self.healthMax = healthMax
        self.energy = energy
        self.energyMax = energyMax
        self.damage = damage
        self.defense = defense
        self.speed = speed
        self.critChance = critChance
        self.critEff = critEff
        self.equipment = {
            "Weapon": None,
            "Armor": None,
            "Talisman": None
        }
        self.equipmentInventory = []
        self.inventory = []
        self.skills = []

    def equipGear(player, item):
        player.equipment[item.type] = item

    def updateStats(self):
        self.damage = 0
        self.defense = 0
        self.speed = 10
        self.energy = 50
        self.energyMax = 50
        self.critChance = 5
        self.critEff = 50

        for _, item in self.equipment.items():
            if item:
                for attr in ['damage', 'defense', 'energyMax', 'critChance', 'critEff', 'speed']:
                    value = getattr(item, attr, None)
                    if value is not None:
                        setattr(self, attr, getattr(self, attr) + value)
    
    def setup(self):
        self.health = self.healthMax
        self.energy = self.energyMax

class Enemy:
    def __init__(self, name, health, healthMax, energy, energyMax, damage, defense, speed, critChance, critEff, image, itemPool):
        self.name = name
        self.health = health
        self.healthMax = healthMax
        self.energy = energy
        self.energyMax = energyMax
        self.damage = damage
        self.defense = defense
        self.speed = speed
        self.critChance = critChance
        self.critEff = critEff
        self.image = image
        self.itemPool = itemPool

    def setup(self):
        self.health = self.healthMax
        self.energy = self.energyMax
        
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