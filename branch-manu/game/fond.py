from library import module
from library.images import getImage 
import pygame	

class rect(module.Module):
    def __init__(self,surface):
        self.surface=surface
        self.need_update=[]
       
    def draw(self,rect):
        pygame.draw.rect(self.surface, (0,0,255), rect)
