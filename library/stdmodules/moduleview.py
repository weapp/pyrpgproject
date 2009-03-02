#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
from library.general.structures import treenode

class ModuleView (pygame.sprite.Sprite, treenode.TreeNode):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        treenode.TreeNode.__init__(self)
        self.image=None
        self.rect=None
        
    def update(self):
        pygame.sprite.Sprite.update(self)
        
    def draw():
        pass
