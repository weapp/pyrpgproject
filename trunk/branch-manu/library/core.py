#!/usr/bin/env python
#-*- coding:utf-8 -*-

import singleton
import pygame
import sys
import basic_app

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860
TICKS = 40 #40 frames por segundo

class Core:
    """
    clase principal encargada de iniciar una ventana de pygame y ponerle titulo.
    Sigue el patron Singleton y por tanto si llamas al constructor, siempre
    te devolvera la misma instancia.
    """
    
    __metaclass__ = singleton.Singleton
    def __init__(self,caption="",app=basic_app.Basic_app(),repeat=(90,90)):    
        self.__app=app
        self.__running=False
        self.__clock = pygame.time.Clock()
        pygame.display.init()
        #self.__screen = pygame.display.set_mode((640,480))#TODO cambiar (esta asi para que me entre en la pantalla)
        self.__screen = pygame.display.set_mode( map(lambda x:int(x/1.5) , pygame.display.list_modes()[0]) )
        
        pygame.display.set_caption(caption)
        if repeat:
            pygame.key.set_repeat(*repeat)
        
        print dir(pygame.time)
        print dir(self.__clock)
    
    def get_app(self): return self.__app
    def get_screen(self): return self.__screen

    def start(self):
        """
        Inicia el bucle. En cada paso se de manejar los ticks y llama en cada paso a:
            app.new_event(event)
            app.update()
            app.draw()
            app.updated()
            y por ultimo actualiza la pantalla si asi lo dice app
        """
        self.__running=True
        while self.__running:
            self.__clock.tick(TICKS)
            
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
            if self.__app.updated():
                pygame.display.flip()

#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Core()
    m.start()
