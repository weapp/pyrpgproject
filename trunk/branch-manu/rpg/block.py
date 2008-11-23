from library import images
from flags import *
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,image='None',flags=0):
        pygame.sprite.Sprite.__init__(self)
        self.set_image(image)
        
        self.flags=flags
        self.invisible = bool(INVISIBLE & flags)
        self.tall = bool(TALL & flags)
        self.floor = not bool(NOT_FLOOR & flags)
        self.block = bool(BLOCK & flags)
    
    def get_image(self):
        return images.getImage(self.__image_name)
    
    def set_image(self,image):
        self.__image_name=image
        return images.cacheImage(image)

    image = property(get_image, set_image )
    
    
    def __str__(self):
        r = 'image    :' + str(self.__image_name) + "\n"
        r+= 'invisible:' + str(self.invisible) + "\n"
        r+= 'tall     :' + str(self.tall) + "\n"
        r+= 'floor    :' + str(self.floor) + "\n"
        r+= 'block    :' + str(self.block) + "\n"
        return r
