from library.images import getImage 
from pygame import K_UP,K_DOWN,K_LEFT,K_RIGHT,KEYDOWN,USEREVENT
from library import module
import pygame

VELOC=2

class Hero (module.Module):
    def __init__(self,surface):
        self.player=getImage('Character Cat Girl')
        self.surface=surface
        self.position = self.player.get_rect().move(300, 300)
        self.need_update=[self.player.get_rect()]
        
    def new_event(self,event):
        if event.type in [KEYDOWN, USEREVENT] and event.key in [K_UP,K_DOWN,K_LEFT,K_RIGHT]:
            self.need_update.append(self.position)
            if event.key==K_UP:
                self.position = self.position.move(0, -VELOC)
            elif event.key==K_DOWN:
                self.position = self.position.move(0, VELOC)
            elif event.key==K_LEFT:
                self.position = self.position.move(-VELOC,0)
            elif event.key==K_RIGHT:
                self.position = self.position.move(VELOC,0)    
            self.need_update.append(self.position)
        return False
        
    def draw(self,rect=None):
        if not rect:
            rect=self.surface.get_rect()
        #self.surface.blit(self.player, pygame.Rect.clip(self.position,rect))
        
        pos_muneco=self.player.get_rect().move(self.position[0],self.position[1])
        recorte=rect.move(-pos_muneco[0],-pos_muneco[1])
        self.surface.blit(self.player, rect, recorte)

        self.need_update=[]
        
        
"""
>>> screen = create_screen()
>>> player = load_player_image()
>>> background = load_background_image()
>>> screen.blit(background, (0, 0))       #draw the background
>>> position = player.get_rect()PL
>>> screen.blit(player, position)         #draw the player
>>> pygame.display.update()               #and show it all
>>> for x in range(100):                  #animate 100 frames
...    screen.blit(background, position, position) #erase
...    position = position.move(2, 0)     #move player
...    screen.blit(player, position)      #draw new player
...    pygame.display.update()            #and show it all
...    pygame.time.delay(100)             #stop the program for 1/10 second
"""