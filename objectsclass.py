# ------------- Objects

class Objects(object):
    def __init__(self,name,gold_value):
        self.name = name
        self.goldValue = gold_value

class Equipments(Objects):
    def __init__(self,lvl):
        Objects.__init__()
        self.lvl = lvl

class Consumables(Objects):
    def __init__(self,use,consu_help,damage):
        Objects.__init__()
        self.use = use
        self.help = consu_help
        self.damage = damage

class Weapon(Objects,Equipments):
    def __init__(self,damage_added,characteristics):
        Objects.__init__()
        Equipments.__init__()
        self.damageAdded = damage_added
        self.characteristics = characteristics
        self.slot = 2   #hand left and hand right
    def increase_damage(self):
        self.damageAdded += 1
    def raise_characteristics(self):
        self.characteristics += 1

class Armor(Objects,Equipments):
    def __init__(self,armor,characteristics):
        Objects.__init__()
        Equipments.__init__()
        self.armor= armor
        self.characteristics = characteristics
        self.slots = 5  #head, chest, pants, arms, legs
    def increase_damage(self):
        self.damageAdded += 1
    def raise_characteristics(self):
        self.characteristics += 1
        self.gold_value += 1

class Jewels(Objects,Equipments):
    def __init__(self):
        Objects.__init__()
        Equipments.__init__()
        self.slots = 2  #hand left and hand right
    def raise_stat(self):
        print("")

    def raise_power(self):
        print("")


# Inventory
class Inventory(object):
   def __init__(self, gold):
       self.objects = {}
       self.consumables = {}
       self.gold = gold
       self.head_cover = False
       self.right_hand_cover = False
       self.left_hand_cover = False
       self.chest_cover = False
       self.pants_cover = False
       self.legs_cover = False
       self.arms_cover = False
       self.jewel_slot1 = False
       self.jewel_slot2 = False

   def __str__(self):
       out = '\t'.join(['Name', 'Value in Gold'])
       for item in self.Objects.values():
           out += '\n' + '\t'.join([str(x) for x in [Objects.name, Objects.gold_value]])
           return out

   def add_consumables(self, consu):
       self.consu[consu.name] = consu

   def equip_weapon(self, weapon):
        self.weapon[weapon.name] = weapon

   def equip_armor(self, armor):
        self.armor[armor.name] = armor
   if not self.right_hand_cover:
        self.right_hand_cover = True
   elif not self.left_hand_cover:
        self.left_hand_cover = False
   else:
        print('Your two hands are already fully equipped')
        remove_armors()

   def equip_jewel(self, jewel):
       self.jewel[jewel.name] = jewel

   def print_objects(self):
       print('\t'.join(['Name', 'Value in Gold']))
       for item in self.objects.values():
           print('\t'.join([str(x) for x in [Objects.name, Objects.gold_value]]))

   def print_consumables(self):
       print('\t'.join(['Name', 'Use', 'Help', 'Damage']))
       for item in self.consumables.values():
           print('\t'.join([str(x) for x in [Consumables.name, Consumables.use, Consumables.help, Consumables.damage]]))

   def print_gold(self):
       print('\t'.join(['Gold']))
       for item in self.gold_value.values():
           print('\t'.join([str(x) for x in [Character.gold_value]]))

   def remove_armors():
       if not Inventory.armors:
           print("You don't wear any armor yet")
       else:
           # print_armor()
           # choice = input('Do you want to remove your armors? [yes/no]').lower()
           try:
               print("")

           except KeyError as name:
               print("No such Armor!", Inventory.armor.name)
