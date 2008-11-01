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

        self.characters=characters
        map(lambda x: x.set_chart(self),self.characters)
        
        self.pos=self.rpgmap.pos
        
        self.pos=self.characters[0].position
                
        self.need_update=[]
           
    def changue_position(self, x=False,y=False,z=False):
        if not x==False and str(x)=="False":
            self.pos[0]=x
        if not y==False and str(y)=="False":
            self.pos[1]=y
        if not z==False and str(z)=="False":
            pos[2]=z
        self.need_update=self.need_update.append(self.surface.get_rect())
        self.pos=self.characters[0].position
        
    def is_there_character(self, x, y, z):
        r=False
        for character in self.characters:
           r = r or (character.position==[x,y,z])
        return r
    
    def puede_estar(self, x, y, z):
        return self.rpgmap.puede_estar(x, y, z) and not self.is_there_character(x, y, z+1)
        
    def new_event(self,event):
        map(lambda x: x.new_event(event) ,self.characters)

    def update(self):
        map(self.update_object, self.characters)
        self.rpgmap.update()
        return self.need_update
        
    def update_object(self,obj):
        self.need_update.extend(obj.update())
               
    def get_position_by_coordinate(self,x,y,z):
        return [self.rpgmap.TILE_WIDTH * (x - self.pos[0]  - 1/2.0)   + self.surface.get_width() / 2 ,
                self.rpgmap.TILE_Y_SPACING * (y - self.pos[1] - 1/2.0) - self.rpgmap.TILE_DEPTH * (z - self.pos[2]) + self.surface.get_height() / 2]
                
    def draw_surface(self,rect=(0,0,0,0)):
        #self.surface.fill((0,0,0))
        self.pos=[2,2,2]
        #self.pos=self.characters[0].position   #seguir a un personaje
        for y in range(self.rpgmap.get_y_max()):
            for z in range(self.rpgmap.get_z_max()):
                for x in range(self.rpgmap.get_x_max()):
                    bloq = self.rpgmap.get_block_image ( x,y,z )
                    block_position=self.get_position_by_coordinate(x,y,z)
                    self.surface.blit(bloq,block_position)
                        
                    for character in self.characters:
                        if character.position == [x,y,z]:
                            self.surface.blit(images.getImage(character.image),block_position)
        self.need_update=[]

