#!/usr/bin/env python
#-*- coding:utf-8 -*-


import pygame
import sys
#from rpg import rpg, repetition, character,hero
#import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

def main():

    #pygame.init() # >>>>>>  open /dev/sequencer or /dev/snd/seq: No such file or directory
    pygame.display.set_caption('CuteRPG2')
        
    screen = pygame.display.init()
    
    screen = pygame.display.set_mode(  pygame.display.list_modes()[1] )
    
    #mapa=__import__('maps.nuevomapa').nuevomapa.mapa()
        
    #pygame.key.set_repeat(1,1)
    
    personajillo1=__import__('modhero').Hero(screen)
    bg=__import__('background').Bg(screen)
    rp=__import__('repetition').Repetition()
    
    #heroe=hero.Hero(image='Character Pink Girl')
    
        
    #RPG=rpg.RPG(screen, mapa,[personajillo1,heroe])
    
    #Repetition=repetition.Repetition()
    
    objetos=[rp,bg,personajillo1]
        
        
    clock = pygame.time.Clock()
    while 1:
        clock.tick(40) #40 frames por segundo
        
        #control de eventos  (llamar a la funcion new_event de cada objeto y proceder a otros si asi lo dice algun objeto)
        for event in pygame.event.get():
            for objeto in objetos:
                if objeto.new_event(event):
                    print "evento[", repr(event.unicode) ,"]terminado por el objeto de tipo:", objeto.__class___, ":",repr(objeto)
                    break
        
            #print "evento[", event ,"] no usado"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        
        #updates (llamar a la funcion update de cada objeto y ver si alguno de ellos se ha cambiado)
        updates=[]
        for objeto in objetos:
            need_update=objeto.update() 
            if need_update:
                updates.extend(need_update)
            #print update
            #print dir(update[0])
            
        if updates:
            #pintando        
            #screen.blit( RPG.surface, (0,0))
            for update in updates:
                for objeto in objetos:
                    objeto.draw_surface(update)
                pygame.display.flip()


        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
