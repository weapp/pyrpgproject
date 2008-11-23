from library import core,module,images
from pygame import *

class rectangles(module.Module):
    def __init__(self,surface):
        self.surface=surface
        self.need_update=[surface.get_rect()]
        
    def draw(self,rect):
        self.surface.fill((200,200,200))
        rect=Rect(15,15,100,100) 
        draw.rect(self.surface, (22,22,130), rect , 2 )
        
        z=rect2=rect.move(50,50) #rect.move_ip(20,20) mueve el cuadrado, la otra funcion lo copia
        draw.rect(self.surface, (130,22,22), rect2, 2 )
    
        rect3=rect.inflate(20, 20)
        draw.rect(self.surface, (22,130,22), rect3, 2 )
        
        rect4=rect.inflate(-20, -20)
        draw.rect(self.surface, (22,22,22), rect4, 2 )

        rect.move_ip(200,200)
        draw.rect(self.surface, (22,22,22), rect, 2 )
        
        rect2=rect.move(50,50)
        draw.rect(self.surface, (130,22,22), rect2, 2 )

        rect3=rect.inflate(-30,-30).clamp(rect2)
        draw.rect(self.surface, (22,100,22), rect3)

        rect3=rect.inflate(-40,-40).clamp(rect2.inflate(-90,-90))
        draw.rect(self.surface, (22,130,22), rect3)

        
        rect.move_ip(50,-200)
        draw.rect(self.surface, (22,22,22), rect, 2 )
        
        rect2=rect.move(50,50)
        draw.rect(self.surface, (130,22,22), rect2, 2 )
        
        rect3=rect.clip(rect2)
        draw.rect(self.surface, (22,130,22), rect3)

        boy=images.getImage('boy')
        boy_rect=boy.get_rect()
        boy_rect.move_ip(50,50)
        self.surface.blit(boy,boy_rect)
        
        rect=z
        
        boy2=images.getImage('boy2')
        pos_muneco=boy2.get_rect().move(50,50)
        recorte=rect.move(-pos_muneco[0],-pos_muneco[1])
        
        #draw.rect(self.surface,(255,255,255,125),z)
        
        self.surface.blit(boy2, rect, recorte)

app=core.Dirty_Objects()
core=core.Core(app=app)
app.add(rectangles(core.get_screen()))
core.start()
