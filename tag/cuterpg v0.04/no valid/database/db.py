import coloreado
from table import table

class Database:
    def __init__(self):
        self.db={}

    def create_new_table(self,name,args):   
        name=str(name)
        self.db[name]=table(args)
            
    
    def __str__(self):
        r=''
        for key in self.db: 
            r += coloreado.subrayado('   ' + key + '(' + str( self.lens[key] ) + ")   \n") 
            r += str(self.db[key])
        return  r
        
        
    def __getitem__(self, key):
        return self.db[key]
        
    def __setitem__(self, key, value):
        print 'no allowed action'
    
    def __delitem__(self, clave):
        del self.db[key]

