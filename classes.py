class Player:
    def __init__(self, name, health, healthMax, energy, energyMax, damage, defense):
        self.name = name
        self.health = health
        self.healthMax = healthMax
        self.energy = energy
        self.energyMax = energyMax
        self.damage = damage
        self.defense = defense
        self.equipment = {
            "Weapon": None,
            "Armor": None,
            "Talisman": None
        }
        self.inventory = []

    def equipGear(player, item):
        player.equipment[item.type] = item

    def updateStats(self):
        self.damage = 0
        self.defense = 0
        self.energyMax = 50

        for _, item in self.equipment.items():
            if item:
                if item.damage is not None:
                    self.damage += item.damage
                if item.defense is not None:
                    self.defense += item.defense
                if item.energy is not None:
                    self.energyMax += item.energy

class Enemy:
    def __init__(self, name, health, healthMax, energy, energyMax, damage, defense):
        self.name = name
        self.health = health
        self.healthMax = healthMax
        self.energy = energy
        self.energyMax = energyMax
        self.damage = damage
        self.defense = defense

class Equipment:
    list = []
    def __init__(self, name, type, damage, defense, energy, worth, description):
        self.name = name
        self.type = type
        self.damage = damage
        self.defense = defense
        self.energy = energy
        self.worth = worth
        self.description = description

        Equipment.list.append(self)

class Item:
    def __init__(self, name, type, worth):
        self.name = name
        self.type = type
        self.worth = worth

class Area:
    list = []
    def __init__(self, name, actions, enemies):
        self.name = name
        self.actions = actions
        self.enemies = enemies
    
        Area.list.append(self)
    
    def __repr__(self):
        return self.name