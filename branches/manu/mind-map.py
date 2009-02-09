from kdiparser import kdifile
import pygame
from library import core
from library import basicapp
from kdiparser import sideinfo
   
#screen=pygame.display.set_mode((800,500) ,pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SRCALPHA)
class AppMindMap(basicapp.BasicApp):
    def __init__(self):
        global font,antialias,right_margin
        c=core.Core()
        self.screen=c.get_screen()
        self.kdi=kdifile.Kdi('kdiparser/l2.kdi',self.screen)
        self.kdi.render()
        
        self.side=sideinfo.SideInfo(self.screen.subsurface(0,0,150,self.screen.get_height()),self.kdi)
    
    def update(self):
        pygame.event.pump()
        self.kdi.update()
        
    def new_event(self,event):
        if not self.side.new_event(event):
            self.kdi.new_event(event)
        
    def draw(self):
        self.screen.blit(self.kdi.surface,self.kdi.rect)
        self.screen.blit(self.kdi.kdi_selected,self.kdi.rect)
        self.side.draw()
    
c=core.Core()
c.set_app(AppMindMap())
c.start()

