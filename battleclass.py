# ------------------------ Successes
class Success(object):
    def __str__(self, name, description):
        self.name = name
        self.description = description
        self.locked = True

    def unlock_success(self):
        self.locked = False


# --------------------- General statistics
class Stats(object):

    def __str__(self, name, stat):
        self.name = name
        self.stat = stat

    def rise_stat(self):
        self.stat += 1

    def down_stat(self):
        self.stat -= 1


#class Monster(pygame.sprite.Sprite):
#    def __init__(self):
#        self.image = pygame.image.load(“monster.png”)
#        self.rect = self.image.get_rect()
