import pygame

import os
import sys

FONT_FAMILY = "joinpd.ttf"
FONT_SIZE = 30

class Repetition:
    def __init__(self, surface=None):
        self.draw=bool(surface)
        self.surface=surface
        self.need_update=self.draw
        self.events=[]
        if self.draw:
            pygame.font.init()
            self.font = pygame.font.Font( os.path.join(os.path.dirname(sys.argv[0]), FONT_FAMILY ), FONT_SIZE )
            
            self.munneco=pygame.Surface((5,5))
            self.munneco.fill((255,0,0))
        
        self.pos=[0,0]  
        self.cont=0
        
        
        self.event_up=pygame.event.Event(pygame.USEREVENT,{"key":pygame.K_UP,"unicode":""})
        self.event_down=pygame.event.Event(pygame.USEREVENT,{"key":pygame.K_DOWN,"unicode":""})
        self.event_left=pygame.event.Event(pygame.USEREVENT,{"key":pygame.K_LEFT,"unicode":""})
        self.event_right=pygame.event.Event(pygame.USEREVENT,{"key":pygame.K_RIGHT,"unicode":""})

    def new_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                self.events.append(event)
                self.cont=0
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                for ev in self.events:
                    print ev.key
                    print event.key
                    if ev.key == event.key:
                        print "borrar"
                        self.events.remove(ev)   
                #self.events.remove(event)
                self.cont=0
        
    def update(self):
        self.cont += 1
        self.cont %= 10
        if True or not self.cont:
            if len(self.events):
                pygame.event.post(self.events[-1])
                """
                if self.events[-1] == pygame.key.name(pygame.K_UP):
                    self.pos[1]-=1
                    pygame.event.post(self.event_up)
                if self.events[-1] == pygame.key.name(pygame.K_DOWN):
                    self.pos[1]+=1
                    pygame.event.post(self.event_down)
                if self.events[-1] == pygame.key.name(pygame.K_LEFT):
                    self.pos[0]-=1
                    pygame.event.post(self.event_left)
                if self.events[-1] == pygame.key.name(pygame.K_RIGHT):
                    self.pos[0]+=1
                    pygame.event.post(self.event_right)
                """
                
        #  self.need_update = self.rpgmap.update() or self.need_update
        #return bool(self.need_update)
            
    def draw_surface(self,rect=(0,0,0,0)):
        if self.draw:
            if len(self.events):
                text=self.font.render(self.events[len(self.events)-1], True, (255, 255, 255))
                self.surface.blit(text, text.get_rect())
            self.surface.blit(self.munneco, (self.pos[0],self.pos[1],5,5))
