import pygame
from os import path

SKIN='img'
FORMAT = 'png'

cache={}

def loadImage(name, force=False):
    if force or not cache.has_key(str(name)):
        #fullname = path.dirname(__file__) + path.sep +'..' + path.sep + 'images' + path.sep + name + '.png'
        fullname = path.dirname(__file__) + path.sep + SKIN + path.sep + str(name) + '.' + FORMAT
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image: ' + name
            raise SystemExit, message
        return image.convert_alpha()

def cacheImage(name):
    cache[name] = loadImage(name)
    
    
def getImage(name):
    return cache[name]
