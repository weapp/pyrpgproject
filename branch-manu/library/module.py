import types
import core

def deco_verboso(name,nmethod,method):
    if nmethod == "__init__":
        def method2(*args,**kw):
            print "Creando objeto: %s(%s, %s)" % (str(name), ", ".join(map(repr,args)), repr(kw) )
            return method(*args,**kw)
        return method2
    else:
        def method2(*args,**kw):
            #print "llamando a: ",repr(name)+'.'+repr(nmethod),"(",", ".join(map(repr,args)),repr(kw),")"
            print "Llamando a: %s.%s(%s, %s)" % (str(name) , str(nmethod) , ", ".join(map(repr,args)), repr(kw) )
            #,repr(name)+'.'+repr(nmethod),"(",", ".join(map(repr,args)),repr(kw),")"
            return method(*args,**kw)
        return method2

    #lambda self,*args,**kw: not dct[method](self,*args,**kw)
 
class Meta_Verboso(type):
    def __new__(meta, name, bases, dct):
        print 'Creando la clase', name
        return type.__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print 'Inicializando la clase', name
        type.__init__(cls, name, bases, dct)
        setattr(cls,'app',core.Core().get_app())
    """

        methods = [x for x in dct if isinstance(dct[x], types.FunctionType)] 
        for method in methods:
            if method not in ['update','draw','new_event']:
                setattr(cls, method, deco_verboso(name,method,dct[method]))
    """            
    
    """def __call__(cls,*args,**kw):
        print cls.__name__
        print "args: ",args
        print "kw:   ",kw
        cls.__init__(*args,**kw)""" #no funciona
        
        
class Module(object):
    __metaclass__ = Meta_Verboso
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
        
    def draw(self):
        pass
        
class AbstractClassException(Exception) :
    def __str__(self):
        return 'Esta clase es abstracta'
