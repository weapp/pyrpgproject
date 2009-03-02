#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sortabledict

class SDWAK(sortabledict.SortableDict):
    """
    Sortable Dict With Autokeys
    """
    def __init__(self):
        sortabledict.SortableDict.__init__(self)
        self.last_int=-1

    def __setitem__(self,key,value):
        sortabledict.SortableDict.__setitem__(self,key,value)
        if isinstance(key,int):
            self.last_int=key
            print key
    
    def append(self,x):
        self.last_int+=1
        while self.last_int in self:
            self.last_int+=1
        self[self.last_int]=x
    
    add=append
    
if __name__ == '__main__':
    pass
