#!/usr/bin/env python
#-*- coding:utf-8 -*-

from library.stdmodules import module
from library.general.structures import sdwak
from apps import sceneapp
from library.general import xmlconfig

class SceneManager (module.Module):

    def __init__(self, loader):
        module.Module.__init__(self)
        self.scenes=sdwak.SDWAK()
        self.scene=sceneapp.SceneApp()  
        self.loader=loader
        
    def change_scene(self,name_scene):
        self.scene.end_scene()
        self.scene=sceneapp.SceneApp()
        xmlconfig.cargar_estado(self.scenes[name_scene],self.scene.add,self.loader)
        self.scene.start_scene()
        
    def charge_scenes(self,path):
        pass
        
    def charge_scene(self,name_scene ,xmlfilename):
        self.scenes[name_scene]=xmlfilename

    def new_event(self,event):
        return self.scene.new_event(event)
        
    def update(self):
        self.scene.update()
        
    def draw(self):
        self.scene.draw()
        
    def updated(self):
        return True
