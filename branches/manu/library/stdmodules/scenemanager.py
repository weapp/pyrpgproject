#!/usr/bin/env python
#-*- coding:utf-8 -*-

from library.stdmodules import module
from library.general.structures.sdwak

class SceneManager (module.Module):

    def __init__(self):
        self.scenes=sdwak.SDWAK
        self.scene
        
    def change_scene(name_scene):
        self.scene.end_scene()
        self.scene=self.scenes[name_scene]
        self.scene.start_scene()
        
    def charge_scene(path):
        pass
        
    def change_scene(name_scene ,xmlfilename):
        pass

    def new_event(self,event):
        return self.scene.new_event(event)
        
    def update(self):
        self.scene.update()
        
    def draw(self):
        self.scene.draw()
