#!/usr/bin/env python
#-*- coding:utf-8 -*-

import stateloader
from library import core, xmlconfig, singleton

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

class Game():
    __metaclass__ = singleton.Singleton
    def __init__(self):
        self.core=core.Core()
        self.app=self.core.get_app()
        xmlconfig.cargar_estado('game/config.xml',self.app.add,stateloader)
        print self.app
    
    def start(self):
        self.core.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    m=Game()
    m.start()
