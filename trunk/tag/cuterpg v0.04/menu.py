import pygame
import sys
from rpg import rpg, repetition, character
import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 860

def main():
    #pygame.init() # >>>>>>  open /dev/sequencer or /dev/snd/seq: No such file or directory

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('CuteRPG')
   
    mapa=__import__('maps.nuevomapa').nuevomapa.mapa()
    
    personajillo1=character.Character()
    
    
    RPG=rpg.RPG(screen, mapa,[personajillo1])
    
    Repetition=repetition.Repetition()
    
    objetos=[RPG,Repetition]
        
    clock = pygame.time.Clock()
    while 1:
        clock.tick(40) #40 frames por segundo
        
        #control de eventos  (llamar a la funcion new_event de cada objeto y proceder a otros si asi lo dice algun objeto)
        for event in pygame.event.get():
            for objeto in objetos:
                if objeto.new_event(event):
                    print "evento terminado por algun objeto"
                    break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        
        #updates (llamar a la funcion update de cada objeto y ver si alguno de ellos se ha cambiado)
        update=False
        for objeto in objetos:
            update = objeto.update() or update
            
        if update:
            #pintando        
            #screen.blit( RPG.surface, (0,0))
            
            for objeto in objetos:
                objeto.draw_surface()
            
            pygame.display.flip()


        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
