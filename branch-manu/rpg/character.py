from library.images import getImage
import random

from library import vector as Vector
from library.vector import vector
#from numpy import array as vector
#from vector import Vector2 as vector

from library import module



class Character(module.Module):
    def verboso(fun, *args,**kw):
        def func(*args,**kw):
            print 'llamando a:',fun.__name__,'con los parametros', args, kw
            return fun(*args,**kw)
        func.__name__=fun.__name__
        func.func_name=fun.func_name
        return func

    def __init__(self,chart=None,image='Character Horn Girl'):
        self.__position = vector([2,0,2])
        self.image=image
        self.contador=0
        self.chart=chart
        self.FACTOR=[0,0,0]
        
        self.__actual=self.get_position()
    
    def set_position(self, newValue):self.__position = newValue
    
    def get_position(self): return self.__position
    
    def set_actual(self, newValue): self.__actual = newValue
    
    def get_actual_position(self): return self.__actual
    
    def get_actual_position_int(self):
        act=list(self.get_actual_position())
        act[1]=act[1]+1
        act[0]=act[0]-1
        act=map(lambda x: int(x), act)
        return vector(act)
        
        
        #if self.__position==self.__actual:
        
    def fin_mov(self):
        b=True
        for i in range(3):
            b= b and abs(self.__position[i]-self.__actual[i])<float(self.FACTOR[i])/1000
        return b
        
        return reduce(lambda b,x: b and -0.2<x<0.2 , (self.get_actual_position() - self.get_position()) , True)
        
    #@Character.verboso
    def move_up(self):
    
        if self.fin_mov() and self.chart.puede_estar( *vector(self.get_position()) - vector([0,1,1]) ):
            self.__position[1]-=1
            return True
        
    def move_down(self):
        if self.fin_mov() and  self.chart.puede_estar( *vector(self.get_position()) + vector([0,1,-1]) ):
            self.__position[1]+=1
            return True
        
    def move_left(self):
        if self.fin_mov() and  self.chart.puede_estar( *vector(self.get_position()) - vector([1,0,1]) ):
            self.__position[0]-=1
            return True
        
    def move_right(self):
        if self.fin_mov() and  self.chart.puede_estar( *vector(self.get_position()) + vector([1,0,-1]) ):
            self.__position[0]+=1
            return True
    
    
    def set_chart(self,chart):
        self.chart=chart
        self.FACTOR=map(lambda x:float(x),[chart.rpgmap.TILE_WIDTH,chart.rpgmap.TILE_Y_SPACING,chart.rpgmap.TILE_DEPTH])
        
    def update_movement(self):
        """
        norm=list( self.get_position() - self.get_actual_position() )
        a=vector(norm[0:1])
        Vector.norm( a )
        norm[0:1]=a
        
        self.set_actual(self.get_actual_position() + 0.1 * vector(norm) )
        """
        self.set_actual(self.get_actual_position() + 0.0 * self.get_actual_position() )
        
        for i in range(3):
            if abs(self.__position[i]-self.__actual[i])>=float(self.FACTOR[i])/1001:
                if self.__position[i]>=self.__actual[i]:
                    self.__actual[i]+=float(self.FACTOR[i])/1000
                elif self.__position[i]<=self.__actual[i]:
                    self.__actual[i]-=float(self.FACTOR[i])/1000
        
        
    def update(self):
        self.update_movement()
        self.contador += 1
        self.contador %= 10
        
        if not self.contador:
            movs = [self.move_up, self.move_down, self.move_left, self.move_right]            
            random.shuffle(movs)
            movido=False
            while not movido and len(movs):
                mov=movs.pop(0)
                if mov():
                    break
        
    def new_event(self,event):
        pass
