#!/usr/bin/env python
#-*- coding:utf-8 -*-

from game.game import Game
import pygame
import sys
#from rpg import rpg, repetition, character,hero
#import maps

def main():
    #m=Menu()
    #m.start()
    m=Game('game/config.xml')
    m.start()
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
