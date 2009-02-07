#!/usr/bin/python

"""
codigo base para juego con pygame
author danigm <danigm@gmail.com>
date sab oct 13 14:40:13 CEST 2007
"""

import sys
import pygame
from map import *


TILE_WIDTH = 101
TILE_HEIGHT = 171
TILE_Y_SPACING = 82
TILE_DEPTH = 40
SOUTH_SHADOW_HEIGHT=42

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800

SCREEN_WIDTH, SCREEN_HEIGHT = 7*TILE_WIDTH*4/3, 7*TILE_WIDTH


class escenario(list):
    def __init__(self,arg):
        list.__init__(arg)
        
        
def puede_estar(x,y,z):
    return pisable[ capas[z-1][y][x] ] and not bloqueable[ capas[z][y][x] ]

def obtener_altura(x,y):
    z=0
    for i in range(len(capas)):
        if capas[i][y][x]:
            z=i+1
    return z


def main():
    pos_campo=[0,90]
    posicion=[1,1,1]
    
    
    tamanyo=[TILE_WIDTH , TILE_Y_SPACING ]

    pygame.init()
    #inicializacion
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('CuteRPG')
    

    while 1:
        clock.tick(40) #40 frames por segundo


        #screen.fill((128,128,255))
        screen.fill((251,255,251))
        
        
        fondo=pygame.image.load("img/fondo.png")
        fondo=pygame.transform.scale(fondo,( SCREEN_WIDTH, fondo.get_height() ))
        screen.blit( fondo, (0,0, SCREEN_WIDTH,  SCREEN_HEIGHT ) )
        
        #posicion[2]=obtener_altura(posicion[0],posicion[1])
        posicion_personaje=pos_campo[0]+posicion[0]*TILE_WIDTH + TILE_WIDTH/2 , pos_campo[1]+posicion[1]*TILE_Y_SPACING-TILE_DEPTH*posicion[2] + TILE_HEIGHT/2
        
        
        for y in range(len(matriz)):
            for z in range(len(capas)):
                for x in range(len(matriz[y])):
                    if not capas[z][y][x] == 0:
                        bloq = pygame.image.load("img/" + relacion [ capas[z][y][x] ]+".png")
                        screen.blit(bloq,(pos_campo[0]+TILE_WIDTH*x-posicion_personaje[0]+SCREEN_WIDTH/2,pos_campo[1]+TILE_Y_SPACING*y-posicion_personaje[1]+SCREEN_HEIGHT/2-TILE_DEPTH*z))
                    
                    if posicion == [x,y,z]:
                        screen.blit(pygame.image.load("img/" + relacion['personaje'] + ".png").convert_alpha(),((SCREEN_WIDTH-TILE_WIDTH)/2, (SCREEN_HEIGHT-TILE_HEIGHT)/2))
        
        
        fondo=pygame.image.load("img/bar_izq.png")
        fondo=pygame.transform.scale(fondo,( fondo.get_width() *  SCREEN_WIDTH / float(SCREEN_HEIGHT) , SCREEN_HEIGHT ))
        screen.blit( fondo, (0,0, SCREEN_WIDTH,  SCREEN_HEIGHT ) )

        #control de eventos
        # mousex, mousey = pygame.mouse.get_pos() #posicion del raton
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            # si no es un evento de teclado o raton, lo ignoramos
            if not hasattr(event,'button') and not hasattr(event,'key'):
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                print "boton" + str(event.button)
            if event.type == pygame.KEYDOWN:
                if not event.key == pygame.K_ESCAPE:
                    print pygame.key.name(event.key)
                    
                    if pygame.key.name(event.key)=='up' and not posicion[1]==0 and puede_estar(posicion[0],posicion[1]-1,z):
                        #if not pisable[matriz[posicion[0]][posicion[1]-1]]:
                        posicion[1]-=1
                    if pygame.key.name(event.key)=='down' and not posicion[1]==len(matriz)-1 and puede_estar(posicion[0],posicion[1]+1,z):
                        posicion[1]+=1
                    if pygame.key.name(event.key)=='left' and not posicion[1]==0 and puede_estar(posicion[0]-1,posicion[1],z):
                        posicion[0]-=1
                    if pygame.key.name(event.key)=='right' and not posicion[1]==len(matriz[0])-1 and puede_estar(posicion[0]+1,posicion[1],z):
                        posicion[0]+=1
                        
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

        #pintando el fondo de negro
        #screen.fill((0,5,0))
        #refresco de pantalla
        pygame.display.flip()

#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
