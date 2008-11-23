#!/usr/bin/env python
#-*- coding:utf-8 -*-

import singleton
import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860
class list(list):
    def add(self,x):
        self.append(x)
        
    def top(self,x):
        self.append(self.pop(x))
        
    def bottom(self,x):
        self.insert(0,self.pop(x))
        
    def up(self,x):
        self.insert(x+1,self.pop(x))
        
    def down(self,x):
        if x>0:
            self.insert(x-1,self.pop(x))
    
class Dirty_Objects(list):
    def new_event(self,event):        
        b=False
        self.reverse()
        for obj in self:
            if obj.new_event(event):
                b=True
                #print "evento[", repr(event.unicode) ,"]terminado por el objeto de tipo:", obj.__class___, ":",repr(objeto)
                break
        self.reverse()
        return b
    
    def update(self):
        updates=[]
        for obj in self:
            need_update=obj.update()
            if need_update and hasattr(need_update,'__iter__'):
                updates.extend(need_update)
        self.updates = filter(lambda x: type(x) is pygame.Rect, updates)
        return self.updates
    
    def draw(self):
        if self.updates:
            update=reduce(lambda x,y:pygame.Rect.union(x,y),self.updates)
            map(lambda obj:obj.draw(update),self)

class Objects(list):
    def new_event(self,event):        
        b=False
        self.reverse()
        for obj in self:
            if obj.new_event(event):
                b=True
                #print "evento[", repr(event.unicode) ,"]terminado por el objeto de tipo:", obj.__class___, ":",repr(objeto)
                break
        self.reverse()
        return b
    
    def update(self):
        map(lambda x: x.update(),self)
    
    def draw(self):
        for obj in self:
            obj.draw()
            """try:
                obj.draw()
            except:
                raise Exception("Draw method of " + repr(obj) + " is not avalible")
            """    
        #map(lambda x: x.draw(),self)
        
class Core:
    __metaclass__ = singleton.Singleton
    def __init__(self,caption="",app=Objects(),repeat=(1,0)):    
        self.__app=app
        self.__running=False
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((640,480))#TODO cambiar (esta asi para que me entre en la pantalla)
        #print pygame.display.list_modes()[1]
        
        pygame.display.set_caption(caption)
        pygame.display.init()
        if repeat:
            pygame.key.set_repeat(*repeat)
        
        print dir(pygame.time)
        print dir(self.__clock)
    
    def get_app(self): return self.__app
    def get_screen(self): return self.__screen

    def start(self):
        self.__running=True
        while self.__running:
            self.__clock.tick(20) #40 frames por segundo
            
            #control de eventos
            for event in pygame.event.get():
                if self.__app.new_event(event):
                    continue
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    sys.exit()
            
            #actualizado
            self.__app.update()
                        
            #pintado
            self.__app.draw()
            pygame.display.flip()

#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Core()
    m.start()
