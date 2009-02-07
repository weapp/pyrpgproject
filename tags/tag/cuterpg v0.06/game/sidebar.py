from library import module
from library.images import getImage 
import pygame	

class Sidebar(module.Module):
    def __init__(self,surface):
        self.surface=surface
        self.background=getImage('bar_izq')
        self.background=pygame.transform.scale(self.background,( self.background.get_width() *  self.surface.get_width() / self.surface.get_height() , self.surface.get_height() ))
        self.need_update=[self.surface.get_rect()]
       
    def draw(self,rect=None):
        if not rect:
            rect=self.surface.get_rect()
       # pygame.draw.rect(self.surface, (251,255,251), rect)
        self.surface.blit(self.background, rect, rect)
        self.need_update=[]
