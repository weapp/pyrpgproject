from library.general.structures import sdwak

class Graph (sdwak.SDWAK):
    def __init__(self):
        sdwak.SDWAK.__init__(self)
        self.Node=NodeGraph
        self.Bind=BindGraph
        self.binds=set()
    
    def create_node(self,label,*args,**kws):
        if label==-1:
            label=self.next_index()
            
        ng=self.Node(label,*args,**kws)
        self[label]=ng
        return ng
        
    def remove_node(self,label,*args,**kws):
        pass
        
    def add_bind(self,n1,n2,*args,**kws):
        return (self.add_simple_bind(n1,n2,*args,**kws),self.add_simple_bind(n2,n1,*args,**kws))
        
    def add_simple_bind(self,n1,n2,*args,**kws):
        bg=self.Bind(self[n1],self[n2],*args,**kws)
        self[n1].add_bind(bg)
        self[n2].add_bind(bg)
        self.binds.add(bg)
        return bg
        
    def get_binds(self):
        return self.binds
        
    def rep(self):
        print "   ",", ".join(self.keys())
        for key in self.keys():
            r=[str(self[key].label)]
            for k in self.keys():
                if self[k] in self[key].get_bind_nodes():
                    r.append('  x')
                else:
                    r.append('   ') 
            print " ".join(r)
            

class BindGraph (object):
    def __init__(self,start,end,label=None):
        self.start=start
        self.end=end
        self.label=label
    
    def get_start(self): return self.start
    def set_start(self, newValue): self.start = newValue
    def get_end(self): return self.end
    def set_end(self, newValue): self.end = newValue
    def get_label(self): return self.label
    def set_label(self, newValue): self.label = newValue
    
    def __str__(self):
        a=self.start.label
        b=self.end.label
        return "%s-%s>%s" % (a,self.label,b) if self.label else "%s->%s" % (a,b) 
        
    def __repr__(self):
        return str(self)
    
class NodeGraph (object):
    def __init__(self,label,info=None):
        self.label=label
        self.info=info
        self.binds=set()

    def get_bind_nodes(self):
        return [bind.start if bind.end==self else bind.end for bind in self.binds]
    
    def add_bind(self,bg):
        self.binds.add(bg)
        
    def __repr__(self):
        return "<%s instance at %s: %s>" % (self.__class__,hex(hash(self)),str(self))
        return "(%s)->%s" % (repr(self.info),", ".join( self.get_bind_nodes() ))
        
    def __str__(self):
        return "#%s(%s) -> %s#" % (str(self.label),str(self.info),", ".join( [str(tupl[1].label) for tupl in self.binds] ))


class XGraph(Graph):
    def __init__(self,*args,**kws):
        Graph.__init__(self,*args,**kws)
        self.Node=XNodeGraph
        self.Bind=XBindGraph
    
class XBindGraph (BindGraph): #las coordenadas seran para el centro de la arista, ya que puede curvarse
    def __init__(self,start,end,x,y,*args,**kws):
        self.x, self.y = x, y
        BindGraph.__init__(self,start,end,*args,**kws)

class XNodeGraph(NodeGraph):
    def __init__(self,label,x,y,*args,**kws):
        self.x, self.y = x, y
        NodeGraph.__init__(self,label,*args,**kws)
    

g=Graph()
g.create_node('v1')
g.create_node('v2')
g.create_node('v3')
g.create_node('v4')
g.create_node('v5')
g.add_bind('v1','v2')
g.add_bind('v5','v1')
g.add_bind('v3','v2')
g.add_bind('v2','v5')
g.add_bind('v4','v4')

g.rep()

print g.get_binds()
        
g=XGraph()
g.create_node('v1',0,0,)
g.create_node('v2',0,0,)
g.create_node('v3',0,0,)
g.create_node('v4',0,0,)
g.create_node('v5',0,0,)
g.add_bind('v1','v2',0,0,)
g.add_bind('v5','v1',0,0,)
g.add_bind('v3','v2',0,0,)
g.add_bind('v2','v5',0,0,)
g.add_bind('v4','v4',0,0,)

g.rep()

print g.get_binds()



