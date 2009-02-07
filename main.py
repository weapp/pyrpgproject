#!/usr/bin/python

import pygame
from pygame.locals import *
from sys import exit
from characters import Character, Hero

SCREEN_SIZE = (800,600)

def main():

    #Inicializacion Pygame
    pygame.init()

    if not pygame.font:
        print "Warning: Fonts disabled"
    if not pygame.mixer:
        print "Warning: Sound disabled"

    pygame.display.set_caption("Role Game")
    screen = pygame.display.set_mode(SCREEN_SIZE)

    dragon = Character("Peter",[0,0])

    hero = Hero("Shin",[0,2])
    
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    exit()
                    
        dragon.causeDamage()
        dragon.injury(3)
        dragon.injury(hero.causeDamage())
        #dragon.injury(hero.causeDamage())
        
        #print repr(dragon.alive)
        
        if not dragon.alive:
            print "salir"
            exit()

if __name__ == '__main__': main()

