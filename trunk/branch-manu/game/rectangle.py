from library import module
from library.images import getImage 
import pygame	

class rect(module.Module):
    def __init__(self,surface):
        self.surface=surface
        self.need_update=[]
       
    def draw_surface(self,rect):
        pygame.draw.rect(self.surface, (0,0,0), rect, 1)
