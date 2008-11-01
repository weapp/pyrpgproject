from images import getImage
from pygame import K_UP,K_DOWN,K_LEFT,K_RIGHT,KEYDOWN,USEREVENT
import module

class Bg(module.Module):
    def __init__(self,screen):
        self.background=getImage('fondo')
        self.screen=screen
        self.need_update=[self.screen.get_rect()]
       
    def draw_surface(self,rect):
        #for rect in rects:
        self.screen.blit(self.background, rect, rect)
        self.need_update=[]
