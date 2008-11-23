import pygame
import sys
import module

class Menu(module.Module):
    def __init__(self, screen, options,margen_sup=0,margen_izq=0,interlineado=20,letra=("Akbar",90,(0,125,255),(0,225,255)),color_base=(113,113,113),color_selec=(213,213,213)):
        pygame.font.init()
        self.options=options
        self.position=0
        self.margen_sup=margen_sup
        self.margen_izq=margen_izq
        self.interlineado=interlineado
        self.screen=screen
        self.color_base=color_base
        self.color_selec=color_selec
        
        #a=hsl2rgb.hsl2rgb(letra[2][0],letra[2][1],letra[2][2])
        
        self.font = pygame.font.SysFont(letra[0],letra[1])
        self.surfont=[]
        self.ancho=0
        self.colorletra=(letra[2],letra[3])
        
        self.activate=False
        
        
        for i in range(len(self.options)):
            self.surfont.append(self.font.render(self.options[i],True,letra[2]))
            if self.ancho<self.surfont[i].get_width():
                self.ancho=self.surfont[i].get_width() 
            
        self.alto=self.surfont[0].get_height()
        
    def update(self):
        #comprobar que no se sale de la lista
        if self.position < 0:
            self.position = 0
        if self.position >= len(self.options):
            self.position = len(self.options)-1
        
    def draw(self):
        if self.activate:
            #mostrar por pantalla en que posicion "se enkuentra el cursor"
            #print self.position , ": " , self.options[self.position]
                
            #pintar todos los rekuadros y el texto de las opciones
            for i in range(len(self.options)):
                rect=pygame.Rect(self.margen_izq, self.margen_sup+self.interlineado*i+self.alto*i, self.ancho, self.alto)
                rect.centerx=self.screen.get_rect().centerx
                
                if i==self.position:
                    pygame.draw.rect(self.screen, self.color_selec, rect)
                    self.surfont[i]=self.font.render(self.options[i],True,self.colorletra[1])
                else:
                    pygame.draw.rect(self.screen, self.color_base, rect)
                    self.surfont[i]=self.font.render(self.options[i],True,self.colorletra[0])

                self.screen.blit(self.surfont[i], rect)
        
            #pintar el rektangulo resaltado
            #pygame.draw.rect(self.screen, self.color_selec, (self.margen_izq,  self.margen_sup+self.interlineado*self.position+self.alto*self.position, self.ancho, self.alto))        
    
    def new_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.activate = not self.activate
                return True
            if self.activate:
                if event.key==pygame.K_UP: self.up()
                elif event.key==pygame.K_DOWN: self.down()
                return True

    def down(self):
        self.position+=1
        self.update()
        
    def up(self):
        self.position-=1
        self.update()
