from library import images
from flags import *

class Block:
    def __init__(self,image='None',flags=0):
        self.__image_name = image
        self.save_cache(image)
        
        self.flags=flags
        self.invisible = bool(INVISIBLE & flags)
        self.tall = bool(TALL & flags)
        self.floor = not bool(NOT_FLOOR & flags)
        self.block = bool(BLOCK & flags)
    
    def getcache(self):
        return images.getImage(self.__image_name) 
    
    def save_cache(self,image):
        self.__image_name=image
        return images.cacheImage(image)

    image  = property(getcache, save_cache )
    
    def __str__(self):
        r = 'image    :' + str(self.__image_name) + "\n"
        r+= 'invisible:' + str(self.invisible) + "\n"
        r+= 'tall     :' + str(self.tall) + "\n"
        r+= 'floor    :' + str(self.floor) + "\n"
        r+= 'block    :' + str(self.block) + "\n"
        return r
