import images
from flags import *

class Block:
    def __init__(self,image='Stone Block',flags=0):
        self.image_name = image
        self.image = images.loadImage(image)
        self.flags=flags
        self.invisible = bool(INVISIBLE & flags)
        self.tall = bool(TALL & flags)
        self.floor = not bool(NOT_FLOOR & flags)
        self.block = bool(BLOCK & flags)
        

    def __str__(self):
        r = 'image    :' + str(self.image_name) + "\n"
        r+= 'flags    :' + str(self.flags) + "\n"
        r+= 'invisible:' + str(self.invisible) + "\n"
        r+= 'tall     :' + str(self.tall) + "\n"
        r+= 'floor    :' + str(self.floor) + "\n"
        r+= 'block    :' + str(self.block) + "\n"
        return r
