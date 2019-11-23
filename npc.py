import character

from consts import *

class Npc(character.Character):

	def __init__(self, location, realsize=(CELL_SIZE, CELL_SIZE)):
	    super(Npc, self).__init__(location, realsize)

	def do_collide(self, player):
		pass