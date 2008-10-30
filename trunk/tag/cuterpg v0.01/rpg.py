import pygame
import images

class RPG:
    def __init__(self, surface, rpg_map):
        self.rpgmap=rpg_map
        self.surface=surface
        self.contador=0
        self.pos=self.rpgmap.posicion_inicial
        images.cacheImage('fondo')
        images.cacheImage('bar_izq')
        for elem in self.rpgmap.relacion.values():
            images.cacheImage(elem)
        self.need_update=True
           
    def changue_position(self, x=False,y=False,z=False):
        if not x==False and str(x)=="False":
            self.pos[0]=x
        if not y==False and str(y)=="False":
            self.pos[1]=y
        if not z==False and str(z)=="False":
            pos[2]=z
        self.need_update=True
            
        
    def new_event(self,event):
        if event.type == pygame.KEYDOWN:
            #if pygame.key.name(event.key)=='up' and not self.pos[1]==0 and self.rpgmap.puede_estar(self.pos[0],self.pos[1]-1,1):
            if event.key==pygame.K_UP and not self.pos[1]==0 and self.rpgmap.puede_estar(self.pos[0],self.pos[1]-1,1):
                self.pos[1]-=1
                self.need_update=True
            elif event.key==pygame.K_DOWN and not self.pos[1]==len(self.rpgmap.capas[0])-1 and self.rpgmap.puede_estar(self.pos[0],self.pos[1]+1,1):
                self.pos[1]+=1
                self.need_update=True
            elif event.key==pygame.K_LEFT and not self.pos[0]==0 and self.rpgmap.puede_estar(self.pos[0]-1,self.pos[1],1):
                self.pos[0]-=1
                self.need_update=True
            elif event.key==pygame.K_RIGHT and not self.pos[0]==(len(self.rpgmap.capas[0][0])-1) and self.rpgmap.puede_estar(self.pos[0]+1,self.pos[1],1):
                self.pos[0]+=1
                self.need_update=True
            elif event.key == pygame.K_ESCAPE and self.contador==0:
                self.contador+=1
                #return True             
            else:
                print "-No se hace nada con este evento en rpg.py-"
                return False
        
    def update(self):
        if self.need_update:
            self.surface.fill((251,255,251))
            
            fondo=images.getImage('fondo')  
            fondo=pygame.transform.scale(fondo,( self.surface.get_width(), fondo.get_height() ))
            self.surface.blit( fondo, self.surface.get_rect() )
            
            pos_personaje=[]
            pos_personaje.append(self.rpgmap.pos_campo[0]+self.pos[0]*self.rpgmap.TILE_WIDTH + self.rpgmap.TILE_WIDTH/2)
            pos_personaje.append(self.rpgmap.pos_campo[1]+self.pos[1]*self.rpgmap.TILE_Y_SPACING-self.rpgmap.TILE_DEPTH*self.pos[2] + self.rpgmap.TILE_HEIGHT/2)
            
            
            for y in range(len(self.rpgmap.capas[0])):
                for z in range(len(self.rpgmap.capas)):
                    for x in range(len(self.rpgmap.capas[1][y])):
                        if not self.rpgmap.capas[z][y][x] == 0:
                            #bloq = pygame.image.load("img/" + self.rpgmap.relacion [ self.rpgmap.capas[z][y][x] ]+".png")
                            bloq = images.getImage( self.rpgmap.relacion [ self.rpgmap.capas[z][y][x] ] )
                            posicion_bloque=[0,0]
                            posicion_bloque[0]=self.rpgmap.pos_campo[0]+self.rpgmap.TILE_WIDTH*x-pos_personaje[0]+self.surface.get_width()/2
                            posicion_bloque[1]=self.rpgmap.pos_campo[1]+self.rpgmap.TILE_Y_SPACING*y-pos_personaje[1]+self.surface.get_height()/2-self.rpgmap.TILE_DEPTH*z
                            
                            self.surface.blit(bloq,posicion_bloque)
                        
                        if self.pos == [x,y,z]:
                            pos_protagonista=(self.surface.get_width()-self.rpgmap.TILE_WIDTH)/2, (self.surface.get_height()-self.rpgmap.TILE_HEIGHT)/2
                            #self.surface.blit(pygame.image.load("img/" + self.rpgmap.relacion['personaje'] + ".png").convert_alpha(),pos_protagonista)
                            self.surface.blit(images.getImage(self.rpgmap.relacion['personaje']),pos_protagonista)
            
            #fondo=pygame.image.load("img/bar_izq.png")
            fondo=images.getImage('bar_izq')
            fondo=pygame.transform.scale(fondo,( fondo.get_width() *  self.surface.get_width() / self.surface.get_height() , self.surface.get_height() ))
            self.surface.blit( fondo, (0,0, self.surface.get_width(),  self.surface.get_height() ) )

            self.need_update=False
            
            return True
        else:
            return False
