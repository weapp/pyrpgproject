#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import background,sidebar
import modhero,modchar,rectangle,fond
from library import singleton,core
from rpg import rpg, repetition, character,hero
#import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

class Game():
    __metaclass__ = singleton.Singleton
    def __init__(self):
        self.core=core.Core()
        #mapa=__import__('maps.nuevomapa').nuevomapa.mapa()
        #heroe=hero.Hero(image='Character Pink Girl')
        #RPG=rpg.RPG(screen, mapa,[personajillo1,heroe])
        
        #core.add_object(__import__('repetition').Repetition())
    
    
        self.screen=self.core.get_screen()
        screen=self.screen
        
        mapa=__import__('maps.nuevomapa').nuevomapa.mapa()
    
        personajillo1=character.Character()
        
        heroe=hero.Hero(image='Character Pink Girl')
        
            
        RPG=rpg.RPG(screen.subsurface((200,200,400,200)), mapa,[heroe,personajillo1])
        
        Repetition=repetition.Repetition()
        
        
        
        #self.core.add_object(fond.rect(self.core.get_screen()))
        
        self.core.add_object(background.Bg(self.core.get_screen()))
        
        #self.core.add_object(RPG)

        self.core.add_object(modhero.Hero(self.core.get_screen()))
        self.core.add_object(modchar.Hero(self.core.get_screen()))
        
        self.core.add_object(sidebar.Sidebar(self.core.get_screen()))
        
        #self.core.add_object(rectangle.rect(self.core.get_screen()))
    
    def start(self):
        self.core.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Game()
    m.start()
