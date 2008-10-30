import pygame
from library import images

import os
import sys

class RPG:
    def __init__(self, surface, rpg_map):
        self.rpgmap=rpg_map
        self.surface=surface
        self.contador=0
        print dir (self.rpgmap)
        
        print repr(self.rpgmap)
        
        self.pos=self.rpgmap.pos
                
        self.need_update=True
        
        
        self.var=''
        
        # < pruebas con texto
        pygame.font.init()
        self.font = pygame.font.Font( os.path.join(os.path.dirname(sys.argv[0]), "joinpd.ttf" ), 30)
        text=self.font.render("Cargando...", True, (255, 255, 255))
        self.surface.blit(text, text.get_rect())
        # > pruebas con texto
           
    def changue_position(self, x=False,y=False,z=False):
        if not x==False and str(x)=="False":
            self.pos[0]=x
        if not y==False and str(y)=="False":
            self.pos[1]=y
        if not z==False and str(z)=="False":
            pos[2]=z
        self.need_update=True
        
    def new_event(self,event):
        if event.type in [ pygame.KEYDOWN , pygame.USEREVENT]:
            self.var += event.unicode
            if event.key==pygame.K_UP and self.rpgmap.puede_estar(self.pos[0],self.pos[1]-1,self.pos[2]):
                self.pos[1]-=1
                self.need_update=True
            elif event.key==pygame.K_DOWN  and self.rpgmap.puede_estar(self.pos[0],self.pos[1]+1,self.pos[2]):
                self.pos[1]+=1
                self.need_update=True
            elif event.key==pygame.K_LEFT and self.rpgmap.puede_estar(self.pos[0]-1,self.pos[1],self.pos[2]):
                self.pos[0]-=1
                self.need_update=True
            elif event.key==pygame.K_RIGHT and self.rpgmap.puede_estar(self.pos[0]+1,self.pos[1],self.pos[2]):
                self.pos[0]+=1
                self.need_update=True
            elif event.key == pygame.K_ESCAPE and self.contador==0:
                self.contador+=1
                #return True             
            else:
                print "-No se hace nada con este evento en rpg.py-   " + event.unicode + " ("+self.var +")" + repr(self.var)
                self.need_update=True #cambia el valor de var que se imprime actualmente por pantalla
                #return False
                            
        
    def update(self):
        self.need_update = self.rpgmap.update() or self.need_update
        if self.need_update:
            self.need_update=False
            return True
        else:
            return False
            
            
    def draw_surface(self,rect=(0,0,0,0)):
        self.surface.fill((251,255,251))
        fondo=images.getImage('fondo')
        fondo=pygame.transform.scale(fondo,( self.surface.get_width(), fondo.get_height() ))
        self.surface.blit( fondo, self.surface.get_rect() )
        for y in range(self.rpgmap.get_y_max()):
            for z in range(self.rpgmap.get_z_max()):
                for x in range(self.rpgmap.get_x_max()):
                    bloq = self.rpgmap.get_block_image ( x,y,z )
                    posicion_bloque=[0,0]
                    posicion_bloque[0]=self.rpgmap.TILE_WIDTH * (x - self.pos[0]  - 1/2.0)   + self.surface.get_width() / 2
                    posicion_bloque[1]=self.rpgmap.TILE_Y_SPACING * (y - self.pos[1] - 1/2.0) - self.rpgmap.TILE_DEPTH * (z - self.pos[2]) + self.surface.get_height() / 2
                    self.surface.blit(bloq,posicion_bloque)
                    if self.pos == [x,y,z]:
                        pos_protagonista=(self.surface.get_width()-self.rpgmap.TILE_WIDTH)/2, (self.surface.get_height()-self.rpgmap.TILE_HEIGHT)/2
                        self.surface.blit(self.rpgmap.get_character_image(),pos_protagonista)
        
        fondo=images.getImage('bar_izq')
        fondo=pygame.transform.scale(fondo,( fondo.get_width() *  self.surface.get_width() / self.surface.get_height() , self.surface.get_height() ))
        self.surface.blit( fondo, (0,0, self.surface.get_width(),  self.surface.get_height() ) )
        
    # < pruebas con texto
        text=self.font.render(self.var, True, (255, 255, 255))
        self.surface.blit(text, text.get_rect())
    # > pruebas con texto
