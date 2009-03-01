from library import core,module,images
from pygame import *
from time import sleep

images.SKIN='../pruebas'

VELOC=15
ANGLE=4

class rectangle(module.Module):
    def __init__(self,surface):
        self.surface=surface
        self.x=3325
        
    def draw(self):
            self.surface.fill((200,200,200))

    def update(self):
        sleep(0.5)
        self.x = ((self.x+1)%100*27)%100
        
    def __str__(self):
        return "el valor actual es %s" % self.x
    
    def __repr__(self):
        return str(self)
    
    
class ghost(module.Module):
    def __init__(self,surface,_dic={}):
        self.surface=surface
        self.dic=_dic
        
    def draw(self):
        print self.dic

    def update(self):
        pass
                    
    def new_event(self,event):
        pass
        
core=core.Core()
app=core.get_app()
core.set_repeat(1,0)
r=rectangle(core.get_screen())
app.add(r)
z=ghost(core.get_screen())
app.add(z)
z.dic['p']='lala'
z.dic['rect']=r
r.x=4
core.start()
