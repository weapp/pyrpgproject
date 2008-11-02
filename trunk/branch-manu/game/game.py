#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import background,sidebar
import modhero,modchar,rectangle,fond
from library import singleton,core,xmlparser
from rpg import rpg, repetition, character,hero
#import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

class Game():
    __metaclass__ = singleton.Singleton
    def __init__(self):
        self.db=xmlparser.parse_xml(sys.path[0]+'/game/settings.xml')
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


        image=self.db['settings'][0]['hero'][0]['image'][0]['value']
        x=self.db['settings'][0]['hero'][0]['x'][0]['value']
        y=self.db['settings'][0]['hero'][0]['y'][0]['value']
        position=(int(x),int(y))
        self.core.add_object(modhero.Hero(self.core.get_screen(),image,position))
        self.core.add_object(modchar.Hero(self.core.get_screen()))
        
        self.core.add_object(sidebar.Sidebar(self.core.get_screen()))
         
        #self.core.add_object(rectangle.rect(self.core.get_screen()))
    
    def start(self):
        self.core.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Game()
    m.start()
