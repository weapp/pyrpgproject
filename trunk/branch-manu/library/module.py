class Module(object) :
    def __init__(self) :
        if type(self) is Module:
            raise AbstractClassException
        else:
            self.need_update=[]
            #constructor por defecto de las subclases
            
    def new_event(self,event):
        return False
        
    def update(self):
        return self.need_update
        
    def draw_surface(self,rect):
        pass
        
class AbstractClassException(Exception) :
    def __str__(self):
        return 'Esta clase es abstracta'
