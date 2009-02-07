#!/usr/bin/python

"""
codigo base para juego con pygame
author danigm <danigm@gmail.com>
date sab oct 13 14:40:13 CEST 2007
"""

import sys
import pygame


def main():

    matriz=(
    ("c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"),
    ("c","e","e","d","d","d","a","a","d","d","d","d","d","d","d","c"),
    ("c","e","e","d","d","d","d","d","c","c","d","d","d","d","d","c"),
    ("c","e","d","d","d","d","d","c","c","d","d","d","d","d","d","c"),
    ("c","d","d","d","d","d","c","c","d","d","d","d","d","d","d","c"),
    ("c","d","d","d","d","d","c","c","d","d","d","d","d","d","d","c"),
    ("c","d","d","d","d","d","c","c","d","d","d","d","d","d","d","c"),
    ("c","d","d","c","c","c","c","d","d","d","d","b","b","b","b","b"),
    ("c","d","d","c","d","d","d","d","d","b","b","b","b","b","b","b"),
    ("c","d","d","c","d","d","d","d","d","b","b","b","b","b","b","b"),
    ("c","c","c","c","c","c","c","c","b","b","b","b","b","b","b","b"),    
    )
    
    pos_campo=[0,90]
    posicion=[1,1]
    
    tamanyo=[50,42]

    pygame.init()
    #inicializacion
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    pygame.display.set_caption('pypong')
    
    screen.fill((128,128,255))

    
    print2=""
    i=0
    for fila in matriz:
        j=0
        for elem in fila:
            print2+=elem
            bloq = pygame.image.load(elem+".png")
            screen.blit(bloq,(pos_campo[0]+tamanyo[0]*j,pos_campo[1]+tamanyo[1]*i))
            
            j=j+1            
        print2+="\n"
        i=i+1   
    print print2
    
    screen.blit(pygame.image.load("boy.png").convert_alpha(),(pos_campo[0]+tamanyo[0],pos_campo[1]+tamanyo[1]))

    while 1:
        clock.tick(40) #40 frames por segundo

        #control de eventos
        # mousex, mousey = pygame.mouse.get_pos() #posicion del raton
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            # si no es un evento de teclado o raton, lo ignoramos
            if not hasattr(event,'button') and not hasattr(event,'key'):
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                print _("boton") + str(event.button)
            if event.type == pygame.KEYDOWN:
                if not event.key == pygame.K_ESCAPE:
                    print event.key
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

        #pintando el fondo de negro
        #screen.fill((0,0,0))
        #refresco de pantalla
        pygame.display.flip()

#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
