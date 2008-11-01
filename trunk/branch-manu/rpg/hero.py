from library.vector import vector
import random
import pygame
from character import Character

class Hero(Character):
        
    def new_event(self,event):
        if event.type in [ pygame.KEYDOWN , pygame.USEREVENT]:
            if event.key==pygame.K_UP and self.chart.puede_estar( *vector(self.position) - vector([0,1,1]) ):
                self.position[1]-=1
                self.need_update=True
            elif event.key==pygame.K_DOWN  and self.chart.puede_estar( *vector(self.position) + vector([0,1,-1]) ):
                self.position[1]+=1
                self.need_update=True
            elif event.key==pygame.K_LEFT and self.chart.puede_estar( *vector(self.position) - vector([1,0,1]) ):
                self.position[0]-=1
                self.need_update=True
            elif event.key==pygame.K_RIGHT and self.chart.puede_estar( *vector(self.position) + vector([1,0,-1]) ):
                self.position[0]+=1
                self.need_update=True
    
    def update(self):
        return []

