#from library.vector import vector
import random
import pygame
from character import Character

from library.general.structures.vector import vector
#from numpy import array as vector
#from vector import Vector2 as vector

class Hero(Character):
        
    def new_event(self,event):
        if event.type in [ pygame.KEYDOWN , pygame.USEREVENT]:
            if event.key==pygame.K_UP:self.move_up()
            elif event.key==pygame.K_DOWN:self.move_down()
            elif event.key==pygame.K_LEFT:self.move_left()
            elif event.key==pygame.K_RIGHT:self.move_right()
    
    def update(self):
        self.update_movement()

