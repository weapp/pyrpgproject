def recortar(elem):
    elem = elem.replace("\n","")
    elem = elem.replace("\r","")
    while elem.startswith(" "):
        elem = elem[1:]
    while elem.endswith(" "):
        elem = elem[:-1]
    return elem
        
def anyadir(elem):
    return elem+"\n"

class gestor:
    def __init__(self,name):
        self.name = name
        self.file = open (self.name,'r+')
        self.db = map(recortar,self.file)
        self.file.close()
        self.need_save=False
    
    def reload(self):
        self.file = open (self.name,'r+')
        self.db = map(recortar,self.file)
        self.file.close()
        self.need_save=False
        
    def save(self):
        self.file = open (self.name,'w')
        self.file.write("\n".join(self.db))
        self.need_save=False
    
    def append(self,name):
        name = recortar(name)
        if not name in self.db:
            self.db.append(name)
            self.need_save=True
            return name + ' is added'
        else:
            return name +' is not added'
    
    def remove(self,name):
        if name in self.db:
            self.need_save=True
            self.db.remove(name)
            return name + ' is removed'
        
        name=recortar(name)
        if name in self.db:
            self.need_save=True
            self.db.remove(name)
            return name + ' is removed'
            
        return name + ' is not removed'
    
        
    def __str__(self):
        r="\n\nactual db:\n"
        for group in self.db:
            r += group + "\n"
        return r
    
    def omit_the(self,name):
        if name.startswith("the "):
            name = name[4:]
        elif name.startswith("los "):
            name = name[4:]
        elif name.startswith("la "):
            name = name[3:]
        elif name.startswith("el "):
            name = name[3:]
        return name
        
    def sort(self,omit_the=False):
        self.need_save=True
        if omit_the:
            self.db.sort( cmp=lambda x,y: cmp( self.omit_the(x.lower()), self.omit_the(y.lower())) )
        else:
            self.db.sort( cmp=lambda x,y: cmp(x.lower(), y.lower()) )
            
    def delete_duplicates(self):
        self.need_save=True
        s=set()
        s.update(self.db)
        self.db=zip(self.db)
            
    def command(self,command):
        if command.startswith('add:') or command.startswith('add '):
            return self.append(command[4:])
        elif command.startswith('del:') or command.startswith('del ') or command.startswith('rem:') or command.startswith('rem '):
            return self.remove(command[4:])
        elif command =='save':
            self.save()
        elif command =='sort':
            self.sort()
        elif command =='natural sort':
            self.sort(True)
        elif command =='show db':
            return self
        elif command =='delete duplicates':
            self.delete_duplicates()
        elif command =='reload':
            self.reload()
        elif command =='exit':
            return''
        else:
            return 'unknown command or not implemented yet'
        return 'command was executed succesfully'