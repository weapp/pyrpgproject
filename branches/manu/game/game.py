#!/usr/bin/env python
#-*- coding:utf-8 -*-

import stateloader
from library import core, xmlconfig, singleton

class Game():
    __metaclass__ = singleton.Singleton
    def __init__(self,xml):
        self.core=core.Core()
        self.app=self.core.get_app()
        xmlconfig.cargar_estado(xml,self.app.add,stateloader)
    
    def start(self):
        self.core.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    g=Game('game/config.xml')
    g.start()
