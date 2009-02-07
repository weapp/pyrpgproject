from library.vector import vector
import random
import pygame
from character import Character

class Hero(Character):
        
    def new_event(self,event):
        print event
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
            else:
                #print "-No se hace nada con este evento en rpg.py-   " + event.unicode + " ("+self.var +")" + repr(self.var)
                self.need_update=True #cambia el valor de var que se imprime actualmente por pantalla
                #return False
    
    def update(self):
        pass       

