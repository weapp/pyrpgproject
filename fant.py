from library import core,module,images
from pygame import *

images.SKIN='../pruebas'

VELOC=15
ANGLE=4

class rectangle(module.Module):
    def __init__(self,surface):
        self.surface=surface
        
    def draw(self):
            self.surface.fill((200,200,200))

    def update(self):
        pass
    
    
class ghost(module.Module):
    def __init__(self,surface,imgs=[{'img':'a',"giro":-1},{'img':'b',"giro":1}],inicio=[50,50]):
        self.surface=surface
        self.angle=0
        self.position=[Rect(inicio[0],inicio[1],0,0) for x in range(20)]
        self.pos=self.position[0]
        self.f=[images.getImage(img['img']) for img in imgs]
        self.giros=[img['giro'] for img in imgs]
        
    def draw(self):
        for i in range(len(self.position)):
            for cont in range(len(self.f)):
                f=transform.rotozoom(self.f[cont], self.giros[cont]*self.angle - i*4 * ANGLE , ((float(i)+1)/len(self.position))**2 )
                f_rect=f.get_rect()
                f_rect.center=(self.position[i].center)
                self.surface.blit(f,f_rect)

    def update(self):
        self.angle=(self.angle+ANGLE)%360
        del self.position[0]
        self.position.append(self.pos)
            
    def new_event(self,event):
        if event.type == KEYDOWN:
            if   event.key==K_UP:    self.pos=self.position[-1].move(0, -VELOC)
            elif event.key==K_DOWN:  self.pos=self.position[-1].move(0, VELOC)
            elif event.key==K_LEFT:  self.pos=self.position[-1].move(-VELOC, 0)
            elif event.key==K_RIGHT: self.pos=self.position[-1].move(VELOC, 0)
    
app=core.Objects()
core=core.Core(app=app,repeat=(1,0))
app.add(rectangle(core.get_screen()))
app.add(ghost(core.get_screen(),imgs=[{'img':'a',"giro":-1},{'img':'b',"giro":1}],inicio=[50,50]))
app.add(ghost(core.get_screen(),imgs=[{'img':'c',"giro":-1},{'img':'d',"giro":1}],inicio=[50,200]))
core.start()
