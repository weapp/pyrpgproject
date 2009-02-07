#!/usr/bin/env python
#-*- coding:utf-8 -*-

from library import core
import background as bg
import sidebar as sidebar_
from rpg import rpg as rpg_
from rpg import hero as hero_
from rpg import character as character_
from library import menu as menu_
from library import toogle_fullscreen as toogle_fullscreen_
from library import fps as fps_

core=core.Core()
screen=core.get_screen()

def background(image,r=0,g=0,b=0):
    #print "\n\n\n\n\n\n\n\n\n\n-->",dir(__import__('game.background').background) ,"<--\n\n\n\n\n\n\n\n\n\n"
    return bg.Bg(screen,image,int(r),int(g),int(b))
    
def rpg(rpg_map,characters):
    return rpg_.RPG(screen,rpg_map,characters)

def mapa(name):
    return getattr(__import__('maps.'+name),name).mapa()

def list(*arg):
    return arg

def hero(image):
    return hero_.Hero(image=image)

def character():
    return character_.Character()
    
def sidebar():
    return sidebar_.Sidebar(screen)

def menu(options):
    return menu_.Menu(screen,options)

def toogle_fullscreen():
    return toogle_fullscreen_.Toogle()
    
def fps():
    return fps_.Fps(screen,core.clock)
