from __future__ import absolute_import
import pygame

from npc import Npc
from consts import CELL_SIZE
from print import *

class UpStairs(Npc):
    images=load_images(["/Users/loic/PycharmProjects/game_again/images/Upstairs.png"])

    def do_collide(self, player):
        player.go_upsatirs()

class DownStairs(Npc):
    images = load_images(["/Users/loic/PycharmProjects/game_again/images/Downstairs.png"])

    def do_collide(self, player):
        player.go_downstairs()