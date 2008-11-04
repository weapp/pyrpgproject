#!/usr/bin/env python
#-*- coding:utf-8 -*-

import singleton
import pygame
import sys
#from rpg import rpg, repetition, character,hero
#import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

class Core:
    __metaclass__ = singleton.Singleton
    def __init__(self,caption=""):    
        self.objects=[]
    
        #pygame.init() # >>>>>>  open /dev/sequencer or /dev/snd/seq: No such file or directory    
        pygame.display.set_caption(caption)
        pygame.display.init()
        pygame.key.set_repeat(1,0)
        self.screen = pygame.display.set_mode((640,480))#TODO cambiar (esta asi para que me entre en la pantalla)
        #print pygame.display.list_modes()[1]
        self.running=False
        self.clock = pygame.time.Clock()
                
    def add_object(self,obj):
        self.objects.append(obj)

    def top(self,x):
        obj=self.objects.pop(x)
        self.objects.reverse()
        self.objects.append(obj)
        self.objects.reverse()
        
    def bottom(self,x):
        obj=self.objects.pop(x)
        self.objects.append(obj)
        
    def up(self,x):
        if x<len(self.objects)-1:
            self.objects[x+1],self.objects[x]=self.objects[x],self.objects[x+1]
        
    def down(self,x):
        if x>0:
            self.objects[x-1],self.objects[x]=self.objects[x],self.objects[x-1]
        
    
    def get_screen(self):
        return self.screen

    def start(self):
        self.running=True
        while self.running:
            self.clock.tick(40) #40 frames por segundo
            
            #control de eventos  (llamar a la funcion new_event de cada objeto y proceder a otros si asi lo dice algun objeto)
            
            self.objects.reverse()
            for event in pygame.event.get():
                for obj in self.objects:
                    if obj.new_event(event):
                        print "evento[", repr(event.unicode) ,"]terminado por el objeto de tipo:", obj.__class___, ":",repr(objeto)
                        break
            
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    sys.exit()
                #print "evento[", event ,"] no usado"
            self.objects.reverse()
                         
            #updates (llamar a la funcion update de cada objeto y ver si alguno de ellos se ha cambiado)
            updates=[]
            for obj in self.objects:
                need_update=obj.update()
                if need_update and hasattr(need_update,'__iter__'):
                    updates.extend(need_update)
            
            updates = filter(lambda x: type(x) is pygame.Rect, updates)
            if updates:
                update=reduce(lambda x,y:pygame.Rect.union(x,y),updates)
                #pintando 
                #for update in updates:
                map(lambda obj:obj.draw_surface(update),self.objects)
                pygame.display.flip()

        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Core()
    m.start()
