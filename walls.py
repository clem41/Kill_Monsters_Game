from npc import Npc
from print import *

class Wall(Npc):
    images = load_images(["/Users/loic/PycharmProjects/game_again/images/Wall.png"])

    def do_collide(self, player):
        player.undo()