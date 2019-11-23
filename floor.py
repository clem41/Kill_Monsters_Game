import csv
import os
import pygame
from __future__ import with_statement

from consts import *
from character import *

def decrypt(string):
    return string

class Floor(object):
    def __init__(self,floornum):
        self.floornum=floornum
        self.group=pygame.sprite.Group()
        self.loadmap()

    def loadmap(self):
        with open(os.path.join('map', 'floor%03d.dat' % self.floornum)) as f:
            for i, line in enumerate(csv.reader(f)):
                real_line = decrypt(line)
                for j, cell in enumerate(real_line):
                    if cell:
                        loc = (j * CELL_SIZE + CELL_SIZE / 2,
                               i * CELL_SIZE + CELL_SIZE / 2)
                        npc = globals().get(cell)(loc)