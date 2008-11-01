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

    def start(self):
        self.running=True
        while self.running:
            self.clock.tick(50) #40 frames por segundo
            
            #control de eventos  (llamar a la funcion new_event de cada objeto y proceder a otros si asi lo dice algun objeto)
            for event in pygame.event.get():
                for obj in self.objects:
                    if obj.new_event(event):
                        print "evento[", repr(event.unicode) ,"]terminado por el objeto de tipo:", obj.__class___, ":",repr(objeto)
                        break
            
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    sys.exit()
                #print "evento[", event ,"] no usado"
                
                         
            #updates (llamar a la funcion update de cada objeto y ver si alguno de ellos se ha cambiado)
            updates=[]
            for obj in self.objects:
                need_update=obj.update()
                if need_update:
                    updates.extend(need_update)
                #print update
                #print dir(update[0])
                
            if updates:
                #pintando        
                #screen.blit( RPG.surface, (0,0))
                for update in updates:
                    for obj in self.objects:
                        obj.draw_surface(update)
                pygame.display.flip()

        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Core()
    m.start()
