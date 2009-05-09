#from kdiparser import kdifile
import pygame
from library import core
from library.stdmodules.apps import basicapp
#from kdiparser import sideinfo
from graph import dgraph
   
class AppButtonPressed:
    def __init__(self):
        self.__list=[]
        
    def new_event(self, event):
        for elem in self.__list:
            elem.new_event(event)
        
    def mouse_left_pressed(self,*args,**kws):
        self.__list.append(self.MouseLeftPressed(self,*args,**kws))
        
    def mouse_right_pressed(self,*args,**kws):
        self.__list.append(self.MouseRightPressed(self,*args,**kws))

    def get_backups(self):
        return self.__list

    class Backup():
        def __init__(self,parent,l,f=None,arg=[],kw={}):
            self.parent=parent
            self.l=l
            self.f=f
            self.arg=arg
            self.kw=kw
        
        def remove(self,event):
            if self.f: self.f(event,*self.arg,**self.kw)
            self.parent._AppButtonPressed__list.remove(self)
        
        def __repr__(self):
            return "<%s instance at %s: %s>" % (self.__class__,hex(hash(self)),repr(self.l))
        
    class MouseLeftPressed(Backup):
        def new_event(self,event):
            if event.type==pygame.MOUSEBUTTONUP and event.button == 1:
                self.remove(event)
        
    
    class MouseRightPressed(Backup):
        def new_event(self,event):
            if event.type==pygame.MOUSEBUTTONUP and event.button == 3:
                self.remove(event)
    

   
#screen=pygame.display.set_mode((800,500) ,pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.SRCALPHA)
class AppGraph(basicapp.BasicApp,AppButtonPressed):
    def __init__(self): 
        global font,antialias,right_margin
        c=core.Core()
        self.screen=c.get_screen()
        self.g=dgraph.AppGraph(self.screen)
        self.g.render()
        #self.side=sideinfo.SideInfo(self.screen.subsurface(0,0,150,self.screen.get_height()),self.kdi)
        AppButtonPressed.__init__(self)
    
    def update(self):
        pygame.event.pump()
        self.g.update()
        
    def new_event(self,event):
        self.g.new_event(event)
        AppButtonPressed.new_event(self,event)
        
        
    def draw(self):
        self.screen.blit(self.g.surface,self.g.rect)
        
c=core.Core()
c.set_app(AppGraph())
c.start()

