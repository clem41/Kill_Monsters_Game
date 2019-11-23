# ------------------- Characters
class Character(object):
    def __init__(self,name, alive, hp, sp, chanceDodge, chanceParry, chanceCriticalHit, MP, damageMin, damageMax, armor,
                 lvl, XP, inventory, lvlNext):
        self.inventory = inventory
        self.name = name
        self.alive = alive
        self.hp = hp    # healthPoints
        self.sp = sp    # shieldPoints block a certain amount of damage and decreased after taking damages
        self.chanceDodge = chanceDodge        # %  to avoid attacks (damages are nullified)
        self.chanceParry = chanceParry       # % to reduce amount of damage by 70%
        self.chanceCriticalHit = chanceCriticalHit  # %  to double the amount of damage inflicted
        self.MP = MP
        self.damageMin = damageMin
        self.damageMax = damageMax
        self.damage = [damageMin, damageMax]
        self.armor = armor              # % reduced incoming damage by a percentage
        self.lvl = lvl
        self.XP = XP                #experience
        self.lvlNext = lvlNext
        self.skill = ["Attack", "Magic"]

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def choose_skill(self):
        x = 1
        print("Skill")
        for skill in self.skills:
            print(str(x) + ";", skill)
            x += 1


    def fire_at(self, enemy):
        if self.armormo >= 1:
            self.armormo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -= 20
        print(self.name, "is hit!")
        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

    def lvl(self):
        hp, sp, MP = 0, 0, 0
        while Character.XP >= Character.lvlNext:
            Character.lvl += 1
            Character.XP += Character.XP - Character.lvlNext
            Character.lvlNext = round(Character.lvlNext * 1.5)
            hp += 1
            sp += 1
            MP += 1
        print("Level: ", Character.lvl)
        print("hp:{}+{} sp:{}+{} MP:{}+{}".format(Character.hp, hp, Character.sp, sp, Character.MP, MP))
        Character.hp += hp
        Character.sp += sp
        Character.MP += MP


class Hero(Character):
    def __init__(self):
        super().__init__(name=input("Enter your name for the games:"), alive=True, hp=20, sp=1,
                         chanceDodge=0, chanceParry=0, chanceCriticalHit=0, MP=2, damageMin=0, damageMax=15,
                         armor="", lvl=1, XP=0, lvlNext = 30)

# ---------------------  Monsters
class Monster(Character):
    def __init__(self, object_dropped, gold_dropped):
        Character.__init__()
        self.object_dropped=object_dropped
        self.gold_dropped=gold_dropped

    def drop_object(self, character):
        print("This Monster attack has a cost in property...")

    def drop_gold(self, character):
        print("This Monster attack has a cost in gold...")

    def draw_monster(self):
        self.screen.blit(source=self.monster_image, dest=self.rect)

    def __exit__(self, *err):
        self.remove(self)

def playerAttack():
    print("You hit")
    print("You missed your attack")

def monsterAttack():
    if(monster.name == "goblin"):
        print("The goblin attacks")
        print("Youn now have", hero.hp, "hp left")
        print("The attack misses")
    elif(monster.name == "giant"):
        print("The GIANT attacks")
        print("Youn now have", hero.hp, "hp left")
        print("The attack misses")

def commands():
    print("press f to fight, press p to pass")
    command = input(">>>>>>>>>>>>").lower()
    if (command == "f"):
        playerAttack()
    elif (command == "p"):
        pass


class Goblin(Monster):
    def __init__(self):
        super().__init__(name="goblin",  alive=True, hp=15, sp=1, chanceDodge=0, chanceParry=0,
                         chanceCriticalHit=0, MP=2, damageMin=0, damageMax=5, armor="", lvl=1, XP=0,
                         object_dropped="", gold_dropped=2)

class Giant(Monster):
    def __init__(self):
        super().__init__(name="giant",  alive=True, hp=25, sp=1, chanceDodge=0, chanceParry=0,
                         chanceCriticalHit=0, MP=2, damageMin=0, damageMax=7, armor="", lvl=1, XP=0,
                         object_dropped="", gold_dropped=3)


# ----------------------- Merchants
class Merchants(Character):
    def __init__(self,inventory_objects):
        Character.__init__()
        self.inventory_objects

    def buy(self, character):
        print("What do you want to sell?")

    def sell(self, character):
        print("What do you want to buy?")


