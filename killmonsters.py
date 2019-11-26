from monsterfct import *
from objectsclass import *
from spells_class import *
from character import *
from Intro import *

Intro()

hero = Hero()
print("Name:", hero.name, "\nhp: ", hero.hp)
hero.inventory = []

# player_name = input("Enter your name for the games:")
#
# hero = {"hero": Character(player_name)}
# monster_types = {1: Monster("Goblin", 0, 5), 2: Monster("Giant", 0, 90), 3: Monster("Dragon", 1, 50), 4: Monster("Ghost", 2, 0), 5: Monster("Vampire", 0, 90), 6: Monster("Angry Alien", 3, 2)}
# merchants = {"a": Merchants("Ali Baba"), "b": Merchants("Happy Alien"), "c": Merchants("Archippe"), "d": Merchants("Hippalus")}
# consumables = {Consumables("Energy bar"), Consumables("Beer"), Consumables("Water"), Consumables("Magic Potion")}
# jewels = {Jewels("Pearling necklace"), Jewels("Amethyst ring"), Jewels("Emerald strap")}
# weapons_types = {Weapon("Pike"), Weapon("Knife"), Weapon("Dagger"), Weapon("Sword"), Weapon("Sabre"), Weapon("Grenade"), Weapon("Pistol"), Weapon("Revolver"), Weapon("Bazzoka")}
# armors = {Armor("Helmet"), Armor("Squire suit"), Armor("Knight suit"), Armor("Knee pad"), Armor("Shield"), Armor("Gloves")}
# monsters = {}
# weapons = {}
#
# inventory = Inventory()
# inventory.add_objects(Weapon('Sword', 5))
# inventory.add_objects(Armor('Armor_1', 0))
# TODO link inventory and hero, inventory and merchants
# TODO battle


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    generateMap()
    caseNumber = chooseCase()
    if monster.hp <= 0:
        print("The", monster.name, "is dead.\n")
    if hero.hp <= 0:
        print(hero.name, " , you died with hp=", hero.hp, "!\n")
        print("And ", monster.name, "has ", monster.hp, "hp...\n")
    if hero.hp > 0:
        commands()
    if monster.hp > 0:
        monsterAttack()


alive_monsters = len(monsters)




while alive_monsters > 1:
    for monster_name in sorted(monsters.keys()):
        print(monster_name, monsters[monster_name])

    first = input("Which weapon attacks?").lower()   #raw_input = fct display a prompt until text+enter
    second = input("Who at?").lower()     #lower method convert the string in lowercase

    try:
        weapon_chosen = weapons[first]
        monster_attacked = monsters[second]
    except KeyError as name:
        print("No such weapon!", name)    #handle exceptions
        continue                        #jump back to the top of the innermost loop ignoring the rest of the loop

    if not weapon_chosen.fire_at(monster_attacked):
        if not monster_attacked.alive :
            alive_monsters -=1
            print("*" * 30)

    for hero in hero.values():
        if hero.alive:
            print(hero.name, "is the winner!")
            break                       #end the loop
