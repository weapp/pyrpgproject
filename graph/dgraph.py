import tarfile
import xml.dom.minidom
from pygame import Color
import pygame
from library.resources import textrect
from library import core
from library.general import bezier

def formatear(string):
    s, i = '', 0
    for c in string:
        if c == ' ': i = 0
        else: s, i = s + c, (i + 1) % 20
        if i == 0: s += ' '
    return s

flags=('warning','bien','idea','requiere trabajo','aclarar','pregunta','basura','reunion','problema')

colores=(
    ( Color('#FFFCD5'), Color('#646D00') ) ,
    ( Color('#ABFBC7'), Color('#035900') ) ,
    ( Color('#FDE1E1'), Color('#930002') ) ,
    ( Color('#FFE8CE'), Color('#563900') ) ,
    ( Color('#D2F1FF'), Color('#03BFEE') ) ,
    ( Color('#EDDFFF'), Color('#000000') ) ,
    ( Color('#FFFFFF'), Color('#000000') ) ,
    ( Color('#000000'), Color('#ECFF19') )
    )
    
colores=(
    ( Color('#FFFCD5FF'), Color('#646D00FF') ) ,
    ( Color('#ABFBC7FF'), Color('#035900FF') ) ,
    ( Color('#FDE1E1FF'), Color('#930002FF') ) ,
    ( Color('#FFE8CEFF'), Color('#563900FF') ) ,
    ( Color('#D2F1FFFF'), Color('#03BFEEFF') ) ,
    ( Color('#EDDFFFFF'), Color('#000000FF') ) ,
    ( Color('#FFFFFFFF'), Color('#000000FF') ) ,
    ( Color('#000000FF'), Color('#ECFF19FF') )
)

omitir=('picurl', 'outlinecolor', 'textcolor', 'piccaption', 'defaultfont', 'comment', 'fillcolor')
"""
                del self.picurl
                del self.outlinecolor
                del self.textcolor
                del self.piccaption
                del self.defaultfont
                del self.comment
                del self.fillcolor
"""

veloc=10

import graph


class ClickableObject:
    def new_event(self,event):
        if hasattr(self,'clickable_zone'):
            area=self.clickable_zone
        else:
            area=self.rect
        if event.type==pygame.MOUSEBUTTONDOWN:
            if area.collidepoint(*event.pos):
                return self.onMouseDown(event)
        elif event.type==pygame.MOUSEBUTTONUP:
            if area.collidepoint(*event.pos):
                return self.onMouseUp(event)
                
    def onMouseDown(self,event):
        pass
        
    def onMouseUp(self,event):
        pass
    

class AppBindGraph (graph.XBindGraph, ClickableObject):
    def __init__(self,start,end,x,y,*args,**kws):
        graph.XBindGraph.__init__(self,start,end,x,y,*args,**kws)
        self.drawlines()
        
    def drawlines(self):
        minx=min(self.start.x,self.end.x,self.x)
        miny=min(self.start.y,self.end.y,self.y)
        maxx=max(self.start.x,self.end.x,self.x)
        maxy=max(self.start.y,self.end.y,self.y)
        w=maxx-minx
        h=maxy-miny
        
        tmp=100 #TODO cambiar el inflate por el tamanyo real que debe de tener
        
        self.rect=pygame.Rect(minx,miny,w,h).inflate(2*tmp,2*tmp)
        self.surface=pygame.Surface(self.rect.size,pygame.SRCALPHA)
        
        p1=(self.start.x-minx+1*tmp,self.start.y-miny+1*tmp)
        p1=bezier.vec2d(*p1)
        p2=(self.x-minx+1*tmp,self.y-miny+1*tmp)
        p2=bezier.vec2d(*p2)
        p3=(self.end.x-minx+1*tmp,self.end.y-miny+1*tmp)
        p3=bezier.vec2d(*p3)
        
        m13 = (p1 + p3) / 2
        vm13_2 = p2 - m13
        vm13_1 = p1 - m13
        p1_1_2 = p1 + vm13_2/2
        p1_2_2 = p2 + vm13_1/2
        
        p2_1_3 = p2 - vm13_1/2
        p2_2_3 = p3 + vm13_2/2

        #lo curvamos un poco mas, para que cuando los nodos esten muy juntos la union sea una curva
        c=min(3,p1.get_distance(p3))
        p2_x = p2 + (vm13_2/c).rotated(-90)
        p2_y = p2 + (vm13_2/c).rotated(+90)
        if p1.get_distance(p2_x)<p1.get_distance(p2_y):
            p1_2_2 += (vm13_2/c).rotated(-90)
            p2_1_3 += (vm13_2/c).rotated(+90)
        else:
            p1_2_2 += (vm13_2/c).rotated(+90)
            p2_1_3 += (vm13_2/c).rotated(-90)
        
        ls=[[p1,p1_1_2,p1_2_2,p2],[p2,p2_1_3,p2_2_3,p3]]
        for l in ls:
            b_points=bezier.calculate_bezier( l )
            
            pygame.draw.lines(self.surface, colores[4][1], False, b_points)
            #pygame.draw.lines(self.surface, colores[4][0], False, l)
        
        sfont=font.render(str(self.label), True, colores[3][1])
        frect=sfont.get_rect()
        frect.center=self.x-minx+1*tmp,self.y-miny+1*tmp
        self.surface.blit(sfont,frect)
        
        self.clickable_zone=frect.inflate(20,20).move(minx-1*tmp,miny-1*tmp)

    def move(self,event):
        self.x, self.y=event.pos
        self.drawlines()
    
    def update_changes(self):
        self.drawlines()
        
    def onMouseDown(self,event):
        if event.button == 1:
            core.Core().get_app().mouse_left_pressed([self],self.move)
        return True
        
class AppNodeGraph(graph.XNodeGraph, ClickableObject):
    def __init__(self,label,surface,x,y,*args,**kws):
        graph.XNodeGraph.__init__(self,label,x,y,*args,**kws)
        self.surface=surface
        self.radio=15
        self.border=1
        self.color=4
        self.circulo_de_color(colores[self.color])
        self.rect=self.surface.get_rect()
        self.rect.center=self.x,self.y
    
    def circulo_de_color(self,color):
        self.surface=pygame.Surface((self.radio*2, self.radio*2),pygame.SRCALPHA)
        pygame.draw.circle(self.surface, color[0], (self.radio,self.radio), self.radio)
        pygame.draw.circle(self.surface, color[1], (self.radio,self.radio), self.radio, self.border)
        
        sfont=font.render(str(self.label), True, color[1])
        frect=sfont.get_rect()
        frect.center=self.radio,self.radio
        self.surface.blit(sfont,frect)
    
    def move(self,event):
        self.x, self.y=event.pos
        self.rect.center=self.x,self.y
        for bind in self.binds:
            bind.update_changes()
    
    def onMouseDown(self,event):
        if event.button == 1:
            self.color=(self.color+1)%len(colores)
            self.circulo_de_color(colores[self.color])
            core.Core().get_app().mouse_left_pressed([self],self.move)
            
        elif event.button == 3:
            core.Core().get_app().mouse_right_pressed([self])
        return True
        
    def onMouseUp(self,event):
        app=core.Core().get_app()
        if event.button == 3:
            for back in app.get_backups():
                if isinstance(back,app.MouseRightPressed) and isinstance(back.l[0], type(self)):
                    node=back.l[0]
                    print "crear arista desde %s hasta %s" % (node.label, self.label)
                    app.g.add_simple_bind(node.label, self.label, (node.x+self.x)/2, (node.y+self.y)/2-25)
        return True
        
    def draw(self):
        pass
        
class AppGraph(graph.XGraph):
    def __init__(self,back_surface):
        graph.XGraph.__init__(self)
        self.flags=flags
        self.colores=colores
        self.back_surface=back_surface
        self.Node=AppNodeGraph
        self.Bind=AppBindGraph
        
    def render(self):
        global max_x,max_y,min_x,min_y,font
        if self.values():
            max_x=max( map(lambda x:x.x,self.values()) )+100
            min_x=min( map(lambda x:x.x,self.values()) )-100
            max_y=max( map(lambda x:x.y,self.values()) )+100
            min_y=min( map(lambda x:x.y,self.values()) )-100
        else:
            max_x=+100
            min_x=-100
            max_y=+100
            min_y=-100
            

        width=max_x-min_x
        height=max_y-min_y

        pygame.font.init()
        filename=pygame.font.match_font('Sans Serif')
        font=pygame.font.Font(filename, 18)

        self.surface=pygame.Surface((width,height))
        self.surface.fill(Color('#fffde8'))

        for bind in self.get_binds():
            self.surface.blit(bind.surface,bind.rect)
        for node in self.values():
            self.surface.blit(node.surface,node.rect)
        
        self.rect=self.surface.get_rect()
        #self.kdi_selected=pygame.Surface(self.rect.size,pygame.SRCALPHA)        
        return self.surface
        
    def update(self):
        self.render()
        self.rect=self.surface.get_rect()
        rect_back=self.back_surface.get_rect()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:    self.rect.move_ip (+veloc, 0)
        elif keys [pygame.K_RIGHT]: self.rect.move_ip (-veloc, 0)
        elif keys [pygame.K_UP]:    self.rect.move_ip (0, +veloc)
        elif keys [pygame.K_DOWN]:  self.rect.move_ip (0, -veloc)
        
        if self.rect.bottom<rect_back.bottom: self.rect.bottom=rect_back.bottom
        #if self.rect.right<rect2.right-righ_margin: rect.right=rect2.right-righ_margin
        if self.rect.right<rect_back.right: self.rect.right=rect_back.right
        if self.rect.x>0: self.rect.x=0
        if self.rect.y>0: self.rect.y=0
    
    def new_event(self,event):
        res=False
        for node in self.values():
            if not res:
                res = node.new_event(event)
                
        for node in self.get_binds():
            if not res:
                res = node.new_event(event)
                
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if not res:
                self.create_node(-1,self.surface,event.pos[0],event.pos[1])

