import pygame
import rpg
import sys
import maps

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 860



def main():
    #pygame.init() # >>>>>>  open /dev/sequencer or /dev/snd/seq: No such file or directory

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('CuteRPG')
   
    mapa=__import__('maps.nuevomapa').nuevomapa.mapa()
    
    #RPG=rpg.RPG(pygame.Surface((800, 600), flags=pygame.SRCALPHA, depth=1, masks=None), 'rpgmap', 'pars')
    #RPG=rpg.RPG(screen, __import__('maps.rpgmap').rpgmap)
    RPG=rpg.RPG(screen, mapa)
        
    clock = pygame.time.Clock()
    while 1:
        clock.tick(40) #40 frames por segundo
        
        #control de eventos
        for event in pygame.event.get():
            
            if RPG.new_event(event):
                print "evento terminado por RPG"
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        
        #updates
        if RPG.update():
            #pintando        
            #screen.blit( RPG.surface, (0,0))
            
            pygame.display.flip()

        
        
        
#esto es para que lance el main cuando se ejecute el fichero
if __name__ == "__main__": main()
