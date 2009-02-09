#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sortabledict import sortableDict

class SDWAK(sortabledict):

    def __init__(self):
        sortabledict.__init__(self)
        self.last_int=-1

    def __setitem__(self,key,value):
        sortabledict.__setitem__(self,key,value)
        if isinstance(int,key):
            self.last_int=key
            print key
    
    
    
    def append(x):
        self.last_int+=1
        while self.last_int in self:
            self.last_int+=1
        self[self.last_int]=x
    
    
if __name__ == '__main__':
    pass
