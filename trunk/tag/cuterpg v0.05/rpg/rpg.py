import pygame
from library import images
from library.vector import vector

import os
import sys

class RPG:
    def __init__(self, surface, rpg_map, characters=[]):
        self.rpgmap=rpg_map
        self.surface=surface
        self.contador=0
        #print dir (self.rpgmap)
        #print repr(self.rpgmap)
        
        self.characters=characters
        map(lambda x: x.set_chart(self),self.characters)
        
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
    
    def is_there_character(self, x, y, z):
        r=False
        for character in self.characters:
           r = r or (character.position==[x,y,z])
        return r
    
    def puede_estar(self, x, y, z):
        return self.rpgmap.puede_estar(x, y, z) and not self.is_there_character(x, y, z+1)
        
    def new_event(self,event):
        map(lambda x: x.new_event(event) ,self.characters)
        if event.type in [ pygame.KEYDOWN , pygame.USEREVENT]:
            self.var += event.unicode
            if event.key==pygame.K_UP and self.puede_estar( *vector(self.pos) - vector([0,1,0]) ):
                self.pos[1]-=1
                self.need_update=True
            elif event.key==pygame.K_DOWN  and self.puede_estar( *vector(self.pos) + vector([0,1,0]) ):
                self.pos[1]+=1
                self.need_update=True
            elif event.key==pygame.K_LEFT and self.puede_estar( *vector(self.pos) - vector([1,0,0]) ):
                self.pos[0]-=1
                self.need_update=True
            elif event.key==pygame.K_RIGHT and self.puede_estar( *vector(self.pos) + vector([1,0,0]) ):
                self.pos[0]+=1
                self.need_update=True
            elif event.key == pygame.K_ESCAPE and self.contador<1:
                self.contador+=1
                #return True             
            else:
                #print "-No se hace nada con este evento en rpg.py-   " + event.unicode + " ("+self.var +")" + repr(self.var)
                self.need_update=True #cambia el valor de var que se imprime actualmente por pantalla
                #return False
                            
    

    def update(self):
        map(self.update_object, self.characters)
        self.need_update = self.rpgmap.update() or self.need_update
        if self.need_update:
            self.need_update=False
            return True
        else:
            return False

    def update_object(self,obj):
        self.need_update = obj.update() or self.need_update
               
    def get_position_by_coordinate(self,x,y,z):
        return [self.rpgmap.TILE_WIDTH * (x - self.pos[0]  - 1/2.0)   + self.surface.get_width() / 2 ,
                self.rpgmap.TILE_Y_SPACING * (y - self.pos[1] - 1/2.0) - self.rpgmap.TILE_DEPTH * (z - self.pos[2]) + self.surface.get_height() / 2]
                
    def draw_surface(self,rect=(0,0,0,0)):
        self.surface.fill((251,255,251))
        fondo=images.getImage('fondo')
        fondo=pygame.transform.scale(fondo,( self.surface.get_width(), fondo.get_height() ))
        self.surface.blit( fondo, self.surface.get_rect() )
        for y in range(self.rpgmap.get_y_max()):
            for z in range(self.rpgmap.get_z_max()):
                for x in range(self.rpgmap.get_x_max()):
                    bloq = self.rpgmap.get_block_image ( x,y,z )
                    block_position=self.get_position_by_coordinate(x,y,z)
                    self.surface.blit(bloq,block_position)
                    
                    
                    if False and self.pos == [x,y,z]:
                        pos_protagonista=(self.surface.get_width()-self.rpgmap.TILE_WIDTH)/2, (self.surface.get_height()-self.rpgmap.TILE_HEIGHT)/2
                        self.surface.blit(self.rpgmap.get_character_image(),pos_protagonista)
                        
                    for character in self.characters:
                        if character.position == [x,y,z]:
                            self.surface.blit(images.getImage(character.image),block_position)
                    
        
        fondo=images.getImage('bar_izq')
        fondo=pygame.transform.scale(fondo,( fondo.get_width() *  self.surface.get_width() / self.surface.get_height() , self.surface.get_height() ))
        self.surface.blit( fondo, (0,0, self.surface.get_width(),  self.surface.get_height() ) )
        
    # < pruebas con texto
        text=self.font.render(self.var, True, (255, 255, 255))
        self.surface.blit(text, text.get_rect())
    # > pruebas con texto
