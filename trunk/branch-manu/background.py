from images import getImage
from pygame import K_UP,K_DOWN,K_LEFT,K_RIGHT,KEYDOWN,USEREVENT


class Bg:
    def __init__(self,screen):
        self.background=getImage('fondo')
        self.screen=screen
        self.need_update=[self.screen.get_rect()]
        
    def new_event(self,event):
        return False
        
    def update(self):
        return self.need_update
        
    def draw_surface(self,rect):
        #for rect in rects:
        self.screen.blit(self.background, rect, rect)
        self.need_update=[]
