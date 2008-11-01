#!/usr/bin/env python
#-*- coding:utf-8 -*-

import singleton
import sys
#from rpg import rpg, repetition, character,hero
#import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

class Game():
    __metaclass__ = singleton.Singleton
    def __init__(self):
        self.core=__import__('core').Core()
        #mapa=__import__('maps.nuevomapa').nuevomapa.mapa()
        #heroe=hero.Hero(image='Character Pink Girl')
        #RPG=rpg.RPG(screen, mapa,[personajillo1,heroe])
        
        self.core.add_object(__import__('background').Bg(self.core.screen))
        self.core.add_object(__import__('modhero').Hero(self.core.screen))
        #core.add_object(__import__('repetition').Repetition())
    
    def start(self):
        self.core.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Game()
    m.start()
