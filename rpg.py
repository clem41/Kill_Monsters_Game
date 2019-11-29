import os, platform, random, inspect


class Character():

    def __init__(self, name, hp, shield, dodge, parry, crit, mp, armor, lvl, xp, minDamage, maxDamage, inventory):
        """
		Create a character
		
		:param      name:       The name
		:type       name:       String
		:param      hp:         Health Points
		:type       hp:         int
		:param      shield:     Shield points
		:type       shield:     int
		:param      dodge:      Dodge percent change in battle
		:type       dodge:      int
		:param      parry:      Parry percent change in battle
		:type       parry:      int
		:param      crit:       Critical Hit change in battle
		:type       crit:       int
		:param      mp:         Magic Points
		:type       mp:         int
		:param      armor:      Armor points
		:type       armor:      int
		:param      lvl:        The level
		:type       lvl:        int
		:param      xp:         Experience Points
		:type       xp:         int
		:param      minDamage:  The minimum damage
		:type       minDamage:  int
		:param      maxDamage:  The maximum damage
		:type       maxDamage:  int
		:param      inventory:  The inventory
		:type       inventory:  Inventory
		"""
        self.name = name
        self.hp = hp
        self.shield = shield
        self.dodge = dodge
        self.parry = parry
        self.crit = crit
        self.mp = mp
        self.armor = armor
        self.lvl = lvl
        self.xp = xp
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.inventory = inventory

    def lvlUp(self):
        """
		Triggers when a character levels up
		"""
        self.xp = 0
        self.lvl += 1
        self.hp += 10
        self.shield += 2
        self.dodge += 2
        self.parry += 2
        self.crit += 2
        self.mp += 7
        self.armor += 3
        self.minDamage += 3
        self.maxDamage += 4
        print("You leveled up!! You stats have increaded!!")

    def displayChar(self, restricted=False):
        """
		Display character statistics, 2 ways possible
		"""
        if restricted:
            # display HP
            print(self.name, " : ")
            print("HP : ", round(self.hp, 2))
            print("--------------------------------")
            print()
        else:
            # when restricted = True: display HP and MP
            print(self.name, " : ")
            print("HP : ", round(self.hp, 2), "\tMP : ", round(self.mp, 2))
            print("--------------------------------")
            print()

    def attack(self):
        # return a random number between min and max damages of the character attacking
        return self.minDamage + (random.random() * (self.maxDamage - self.minDamage))

    def random(self, stat):
        # return a random number for the impact of the battle on stats
        return random.random() <= stat / 100

    def bewitch(self, spell_list):
        # return the cost of the spell
        i = 1
        for spell in spell_list:
            print(str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1


    def fight(self, monster):
        # if both monster and hero are alive, a battle can happen:
        while monster.hp > 0 and self.hp > 0:
            Clean()
            self.displayChar()
            monster.displayChar(True)
            print("Actions : ")
            print("1 - Attack")
            print("2 - Spells")
            choice = input(">")
            # choice to attack or throw a spell
            while choice not in ["1", "2"]:
                choice = input(">")
            Clean()
            # Now that the choice is made, we display some information about the characters to help the player
            self.displayChar()
            monster.displayChar(True)
            if choice == "1":
                message = "You hit " + monster.name
                attack = self.attack()
                if self.random(self.crit):
                    attack = self.attack() * 2
                    message = "You hit " + monster.name + " with a critical hit"
                # parry means you protect yourself but get some damage anyway
                if monster.random(monster.parry):
                    attack *= 0.7
                    message = monster.name + " parried the attack"
                # dodge means you managed to avoid the shot
                elif monster.random(monster.dodge):
                    attack = 0
                    message = monster.name + " dodged the attack"
                print(message)
                print(monster.name, "took", round(attack, 2), "damages\nPress ""enter"" to continue...")
                input()
                # An attack takes 2 hp:
                monster.hp -= round(attack, 2)
            else:
                if choice == "2":
                    flag = 1
                    while flag == 1:
                        message = "You bewitch " + monster.name
                        self.bewitch(spell_list)
                        spell = int(input("Choose your spell:").lower())
                        current_mp = self.mp

                        if spell == "fire" or spell == "1":
                            print("")
                        if spell == "thunder" or spell == "2":
                            print("")
                        else:
                            print("Imagination not enough powerful to throw a spell\nError of typo")
                            flag = 0    # quit while loop so that the hero isn't loosing gold for an error of spelling and no spell
                        print(monster.name, "took", round(spell, 3), "MP damages\nPress ""enter"" to continue...")
                        input()
                        # A spell thrown takes 3 mp:
                        monster.hp -= round(spell, 3)
            if monster.hp <= 0: return 1  # the monster is dead
            message = monster.name + " hit you"  # it's the turn of the monster to show his strength
            attack = monster.attack()
            if monster.random(monster.crit):
                attack = monster.attack() * 2
                message = monster.name + " hit you with a critical hit"
            if self.random(self.parry):
                attack *= 0.7
                message = "You parried the attack"
            elif self.random(self.dodge):
                attack = 0
                message = "You dodged the attack"
            print(message)
            print("You took", round(attack, 2), "damages\nPress ""enter"" to continue...")
            input()
            self.hp -= round(attack, 2)


class Spell():
    def __init__(self, name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmg = dmg


spell_list = [Spell("fire", 3, 8), Spell("thunder", 4, 10)]


class Monster(Character):
    def __init__(self, name, hp, shield, dodge, parry, crit, mp, armor, lvl, xp, minDamage, maxDamage, inventory, gold):
        """
		Create a new monster
		
		:param      gold:       The gold amount the monster gives upon dying
		:type       gold:       int
		"""
        super().__init__(name, hp, shield, dodge, parry, crit, mp, armor, lvl, xp, minDamage, maxDamage, inventory)
        self.gold = gold  # the death of a monster gives gold to the successful killer


def MonstersList():
    monsters = [Monster("Orc", 10, 3, 4, 4, 4, 0, 3, 1, 0, 4, 6, None, 50),
                Monster("goblin",  15, 3, 4, 3, 5, 0, 3, 1, 0, 4, 7, None, 60),
                Monster("giant", 15, 4, 4, 4, 4, 0, 4, 1, 0, 5, 7, None, 70)]

    return random.choice(monsters)


# TODO class Merchant(Character):


class Inventory():
    def __init__(self, objects, gold, head, chest, pants, arms, legs):
        """
		Create a new inventory
		
		:param      objects:  List of objects
		:type       objects:  List
		:param      gold:     Gold amount
		:type       gold:     int
		:param      head:     Equiped armor on head
		:type       head:     Armor
		:param      chest:    Equiped armor on chest
		:type       chest:    Armor
		:param      pants:    Equiped armor on pants
		:type       pants:    Armor
		:param      arms:     Equiped armor on arms
		:type       arms:     Armor
		:param      legs:     Equiped armor on legs
		:type       legs:     Armor
		"""
        self.objects = objects
        self.gold = gold
        self.head = head
        self.chest = chest
        self.pants = pants
        self.arms = arms
        self.legs = legs


# TODO the inventories of the hero and merchants


class Map():
    # a new map is a new floor
    def __init__(self, rooms, floor):
        """
		Create a new map
		
		:param      rooms:  List of rooms on the current floor
		:type       rooms:  List
		:param      floor:  The current floor
		:type       floor:  int
		"""
        self.currentRoom = 1
        self.rooms = rooms
        self.floor = floor  # will display the number of the floor

    def generateRooms(self):
        """
		Create the rooms for the current floor
		"""
        for i in range(0, 5):
            rnd = int(2 * random.random())
            if rnd == 0:
                self.rooms.append(Room(None, None))  # the room is empty
            elif rnd == 1:
                self.rooms.append(Room(MonstersList(), None))  # the room contains a random monster
            else:
                self.rooms.append(Room(None, "Objet aléatoire"))  # the room contains a random object
        # choose between monster, object, nothing
        # with random
        # then choose which monster or which object
        # then add the the room to the list 'rooms'

    # TODO create objects

    def enterRoom(self, player):
        """
		Enters a room.
		"""
        # if all the rooms of the floor haven't been visited
        if self.currentRoom <= len(self.rooms):
            # display the number of the floor and the number of the room
            print("Floor : ", self.floor, " Room : ", self.currentRoom)
            self.rooms[self.currentRoom - 1].roomDialog(player)
            self.currentRoom += 1
        else:
            print("You completed this floor! Well Done!")
            input()
            print("To the next floor then")
            input()
            self.rooms = []
            self.currentRoom = 1
            return 1


class Room():
    def __init__(self, entity, objects):
        """
		Create a new room
		
		:param      entity:   List of entities (monsters or merchants) in the room
		:type       entity:   List
		:param      objects:  List of objects in the room
		:type       objects:  List
		"""
        self.entity = entity
        self.objects = objects

    def roomDialog(self, player):
        """
		Display actions for the room
		"""
        if self.entity is None and self.objects is None:  # = room is empty
            print("There is nothing in this room!\nPress ""enter"" to continue...")
            input()
        elif self.entity is not None and isinstance(self.entity, Monster):  # = surprise there is a monster
            print(self.entity.name, "appeared in the room!\nPress ""enter"" to continue...")
            input()
            if player.fight(self.entity) == 1:
                print(self.entity.name, "died!")
                print("You gained", self.entity.gold, "golds")
                print("You gained 2xp!\nPress ""enter"" to continue...")
                input()

                player.inventory.gold += self.entity.gold
                player.xp += 2


class Object():
    def __init__(self, name, goldValue, stat, effect):
        """
		Create a new object
		
		:param      name:       The name
		:type       name:       String
		:param      goldValue:  The sell value for the object
		:type       goldValue:  int
		:param      stat:       The statistic the object changes
		:type       stat:       String
		:param      effect:     The amount of the change
		:type       effect:     int
		"""
        self.name = name
        self.goldValue = goldValue
        self.stat = stat
        self.effect = effect


class Consumable(Object):
    def __init__(self, name, goldValue, target, stat, effect):
        """
		Create a new consumable
		
		:param      target:     To who the effect goes
		:type       target:     String
		"""
        super().__init__(name, goldValue, stat, effect)
        self.target = target


class Equipment(Object):
    def __init__(self, name, goldValue, lvlMin, slotNumber, stat, effect):
        """
		Create a new equipment
		
		:param      lvlMin:      The minimum level required to equip
		:type       lvlMin:      int
		:param      slotNumber:  The slot number (Head, Legs,...)
		:type       slotNumber:  int
		"""
        super().__init__(name, goldValue, stat, effect)
        self.lvlMin = lvlMin
        self.slotNumber = slotNumber


# TODO assign slotNumber for the character's members

class Armor(Equipment):
    def __init__(self, name, goldValue, lvlMin, slotNumber, armorPoints, stat, effect):
        """
		Create a new armor
	
		:param      armorPoints:  The armor points the armor gives
		:type       armorPoints:  int
		"""
        super().__init__(name, goldValue, lvlMin, slotNumber, stat, effect)
        self.armorPoints = armorPoints


class Weapon(Equipment):
    def __init__(self, name, goldValue, lvlMin, slotNumber, damage, stat, effect):
        """
		Create a new weapon
		
		:param      damage:      How much the weapon increases damages
		:type       damage:      int
		"""
        super().__init__(name, goldValue, lvlMin, slotNumber, stat, effect)
        self.damage = damage


class Jewels(Equipment):
    def __init__(self, name, goldValue, lvlMin, slotNumber, stat, effect):
        super().__init__(name, goldValue, lvlMin, slotNumber, stat, effect)


# TODO create others Jewels
ruby = [Jewels("ruby", 50, 3, 1, "hp", 5) ]


def Intro():
    """
	Intro dialogue
	"""
    print("Welcome to Kill Monsters!!!\nYour goal is clear...\nExit each map "
          "while encountering monsters, merchants and objects.\nLet's try to stay alive!")


def playerName():
    """
	Ask player's name
	"""
    name = input("Enter your name : ")
    return name


def Clean():
    """
	Clear console based on platform
	"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


def main():
    """
	Main function
	"""
    Intro()

    map = Map([], 1)
    map.generateRooms()

    name = playerName()
    player = Character(name, 30, 8, 2, 2, 2, 14, 10, 1, 0, 5, 7, Inventory([], 0, None, None, None, None, None))

# play until you die
    while player.hp > 0:
        Clean()
        player.displayChar()
        if map.enterRoom(player) == 1:
            map.floor += 1
            map.generateRooms();
    print("You Died!")
    print("GAME OVER")
    input()

# if you run python3 rpg.py
if __name__ == '__main__':
    main()
