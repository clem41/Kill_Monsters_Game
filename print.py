import pygame
import os
from consts import *

def load_images(imagefiles):
    return [pygame.image.load(os.path.join("images",imagefile)) for imagefile in imagefiles]

class Print(pygame.sprite.Sprite):

    def __init__(self,location,realsize):
        super(Print,self).__init__()
        self.size=realsize
        self.image_no=0
        self.image=pygame.transform.scale(self.images[self.image_no],realsize)
        self.update_counter=10
        self.rect=self.image.get_rect()
        self.rect.left=location[0]-self.rect.width/2
        self.rect.top = location[1] - self.rect.height/2

        def flash_image(self, image_file, delaytime):
            save = self.image
            self.image = pygame.image.load(image_file)
            self.image = pygame.transform.scale(self.image, self.size)
            self.gameboard.blit(self.image, self.rect)
            pygame.display.update()
            pygame.time.delay(delaytime)
            self.image = save

        def animate(self):
            self.update_counter -= 1
            if self.update_counter == 0:
                self.image = self.next_image()
                self.update_counter = 10

        def next_image(self):
            if self.image_no + 1 < len(self.images):
                self.image_no += 1
            else:
                self.image_no = 0
            return pygame.transform.scale(self.images[self.image_no], self.size)