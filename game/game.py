#!/usr/bin/env python
#-*- coding:utf-8 -*-

import stateloader
from library import core
from library.general import xmlconfig, singleton
from library.stdmodules import scenemanager

class Game():
    __metaclass__ = singleton.Singleton
    def __init__(self,xml):
        self.core=core.Core()
        #self.app=self.core.get_app()
        #xmlconfig.cargar_estado(xml,self.app.add,stateloader)
        sm=scenemanager.SceneManager(stateloader)
        sm.charge_scene('ppal' ,xml)
        sm.change_scene('ppal')
        self.core.set_app(sm)
    
    def start(self):
        self.core.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__":
    g=Game('game/config.xml')
    g.start()
