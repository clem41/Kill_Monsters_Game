import random


# choices with magic skill: SPELLS
class Spells:
    def __init__(self, name, price, dmg, hp, sp):
        self.name = name
        self.price = price
        self.hp = hp
        self.sp = sp
        self.dmg = dmg

    # How much the monster will be affected
    def damage(self):
        dmg_low = self.dmg - 4
        dmg_high = self.dmg + 4
        return random.randrange(dmg_low, dmg_high)

    # How much you will protect yourself
    def protect(self):
        if self.hp != 0:
            hp_low = self.hp - 4
            hp_high = self.hp + 4
            return random.randrange(hp_low, hp_high)
        else:
            return 0

    # How much you will protect yourself
    def protect(self):
        if self.sp != 0:
            sp_low = self.sp - 4
            sp_high = self.sp + 4
            return random.randrange(sp_low, sp_high)
        else:
            return 0


# TODO 1 add new spells
# TODO 2 add spells type for color appearance on the screen
# TODO 3 invent real spell names
# Format =            (name,    price,  dmg,    hp, sp)
spell1 = Spells(spell1, 2, 10, 0, 2)
spell2 = Spells(spell2, 3, 12, -2, 2)
spell3 = Spells(spell3, 4, 15, -3, 2)


# If the input is not valid
def error():
    print("Try again with a valid entrance.")


# You can use two spells at a time
def choose_spells(spells_list):
    spells_list = []
    spell_choice_a = 0
    spell_choice_b = 0
    # choose a first spell
    while spell_choice_a != 1:
        try:
            print("It is time to choose your spells\nYou can choose two of them by entering their numbers:"
                  "\n1 for spell1\n2 for spell2\n3 for spell3")
            choice_a = input().lower()
            if choice_a == 1:
                spells_list.append(spell1)
                spell_choice_a += 1
            elif choice_a == 2:
                spells_list.append(spell2)
                spell_choice_a += 1
            elif spell_choice_a == 3:
                spells_list.append(spell3)
                spell_choice_a += 1
            else:
                print(choice_a)
                error()
        except:
            error()
    # choose a second spell
    while spell_choice_b != 1:
        try:
            print("It is time to choose your spells\nYou can choose two of them by entering their numbers:"
                  "\n1 for spell1\n2 for spell2\n3 for spell3")
            choice_b = input().lower()
            if choice_b == 1:
                spells_list.append(spell1)
                spell_choice_b += 1
            elif choice_b == 2:
                spells_list.append(spell2)
                spell_choice_b += 1
            elif spell_choice_b == 3:
                spells_list.append(spell3)
                spell_choice_b += 1
            else:
                print(choice_b)
                error()
        except:
            error()
