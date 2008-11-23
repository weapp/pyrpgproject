from library import module
from library.images import getImage 
import pygame	

class Bg(module.Module):
    def __init__(self,surface):
        self.surface=surface
        self.background=getImage('fondo')
        self.background=pygame.transform.scale(self.background,( self.surface.get_width(), self.background.get_height() ))
        self.need_update=[self.surface.get_rect()]
       
    def draw(self,rect=None):
        if not rect:
            rect=self.surface.get_rect()
        pygame.draw.rect(self.surface, (251,255,251), rect)
        self.surface.blit(self.background, rect, rect)
        self.need_update=[]
