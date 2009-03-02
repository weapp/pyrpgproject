#!/usr/bin/env python
#-*- coding:utf-8 -*-
import module

class MVCModule (module.Module):
    def __init__(self,ModuleData=None,ModuleView=None,ModuleController=None):
        m=ModuleData
        v=ModuleView
        c=ModuleController
        if not m is None:
            m.add_parent(self)
        if not v is None:
            v.add_parent(self)
        if not c is None:
            c.add_parent(self)
        
    def new_event(self,event):
        if not c is None:
            return self.c.new_event(event)

    def update(self):
        if not m is None:
            self.m.update()
        if not c is None:
            self.c.update()
   
    def draw(self):
        if not v is None:
            self.v.draw()
