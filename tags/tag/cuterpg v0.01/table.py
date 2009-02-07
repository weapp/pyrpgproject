import coloreado

class table:
    def __init__(self,keys):
        #self.keys=set().update(keys).add('id')
        l=['id']
        l.extend(keys)
        self.keys=l
        self.values=[]
        self.id=0
        
    def add(self,*args):
        l = [self.id]
        l.extend(args)
        
        if len(self.keys) == len (l):
            self.values.append(l)
            self.id+=1
        
        
        
    def __str__(self):

        r=''
        width={}
        tmp=[]
        tmp.append(self.keys)
        tmp.extend(self.values)
        tmp=map(lambda row: map(repr,row),tmp)
        for row in tmp:
            for index in range(len(row)):
                if index not in width:
                    width[index]=len(row[index])
                elif width[index]<len(row[index]):
                    width[index]=len(row[index])
        
        #for rowk in self.values:
        #    print ' |'.join ( map(lambda value: " " + str(value).center(width[rowk.index(value)]), rowk) )
        
        for index in range(len(self.keys)):
            r += coloreado.rojo_subrayado_negrita(" " + self.keys[index].center(width[index]) + " |")
        r += "\n"

        tmp.pop(0)                
        for row in tmp:
            for index in range(len(row)):
                r += " " + (row[index]).center(width[index]) + " |"
            r += "\n"
        
        return  r
            
    def get_row(self,index):
        return self.values[index]
        
    def get(self,*args):
        r=self.values
        keys=list(args[::2])
        values=list(args[1::2])

        
        for key in keys:
            if key in self.keys:
                self_index = self.keys.index(key) #columna en la que hay que buscar
                key_index = keys.index(key) #key para buscar en los valores
                r=filter(lambda vector: vector[self_index]==values[key_index],r)
        return r    
        
    #def get row
