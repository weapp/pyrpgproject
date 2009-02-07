from library.vector import vector
import random

class Character:

    def __init__(self,chart=None,image='Character Horn Girl'):
        self.position=[2,0,2]
        self.image=image
        self.contador=0
        self.chart=chart
        
    def set_chart(self,chart):
        self.chart=chart
        
    def update(self):
        self.contador += 1
        self.contador %= 10
        
        if not self.contador:
            vectores = [vector([1,0,0]), vector([-1,0,0]), vector([0,1,0]), vector([0,-1,0])]            
            random.shuffle(vectores)
            movido=False
            while not movido and len(vectores):
                t_vector=vectores.pop(0)
                if self.chart.puede_estar(*vector(self.position)+t_vector+vector([0,0,-1])):
                    self.position = vector(self.position)+t_vector
                    return True
                    
    
    def new_event(self,event):
        pass
