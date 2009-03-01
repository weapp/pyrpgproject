import pygame
from library.resources import images
import os
import sys

from library.general.structures.vector import vector
#from numpy import array as vector
#from vector import Vector2 as vector

class RPG:
    def __init__(self, surface, rpg_map, characters=[]):
        self.rpgmap=rpg_map
        self.surface=surface
        self.contador=0

        self.characters=characters
        map(lambda x: x.set_chart(self),self.characters)
        
        #self.pos=vector(self.rpgmap.pos)
        
        self.pos=vector(self.characters[0].get_actual_position())
           
    def change_camera_position(self, x=False,y=False,z=False):
        if type(z) != bool:
            self.pos[0]=x
        if type(y) != bool:
            self.pos[1]=y
        if type(z) != bool:
            self.pos[2]=z
        
    def is_there_character(self, x, y, z):
        return reduce(lambda b,character: b or tuple(character.get_position())==(x,y,z), self.characters ,False)
    
    def puede_estar(self, x, y, z):
        return self.rpgmap.puede_estar(x, y, z) and not self.is_there_character(x, y, z+1)
        
    def new_event(self,event):
        map(lambda x: x.new_event(event) ,self.characters)

    def update(self):
        map(lambda obj:obj.update(), self.characters)
        self.rpgmap.update()
        self.change_camera_position(*self.characters[0].get_actual_position()) #seguir al personaje
                      
    def get_position_by_coordinate(self,x,y,z):
        return [self.rpgmap.TILE_WIDTH * (x - self.pos[0]  - 1/2.0)   + self.surface.get_width() / 2 ,
                self.rpgmap.TILE_Y_SPACING * (y - self.pos[1] - 1/2.0) - self.rpgmap.TILE_DEPTH * (z - self.pos[2]) + self.surface.get_height() / 2]
                
    def draw(self):
        for y in range(self.rpgmap.get_y_max()):
            for z in range(self.rpgmap.get_z_max()):
                for x in range(self.rpgmap.get_x_max()):
                    bloq = self.rpgmap.get_block( x,y,z ).image
                    block_rect=bloq.get_rect().move(self.get_position_by_coordinate(x,y,z))
                    self.surface.blit(bloq,block_rect)
                        
                    for character in self.characters:
                        if tuple(character.get_actual_position_int()) == (x,y,z):
                            char_img=images.getImage(character.image)
                            
                            #print character.image , ' '*(20-len(character.image)) , character.get_position() , character.position
                            
                            char_rect=char_img.get_rect().move(self.get_position_by_coordinate(*character.get_actual_position()  ))
                            self.surface.blit(char_img,char_rect)
