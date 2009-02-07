from block import *
import pygame
from time import time
import coloreado

import xml


screen = pygame.display.set_mode((60,60))

bloque=Block(flags=NOT_FLOOR | BLOCK )

print bloque

a=file('def.txt')

"""
t=time()
state=[]
count=0

Map=[]
Def=[]

for line in a.readlines():
    if count>0 and len(state):
        if state[0]=='Map':
            Map.append(line)
        if state[0]=='Def':
            Def.append(line)    
            
    if line.find('Map[')!=-1:
        state.append('Map')
        count=1
    elif line.find('Character[')!=-1:
        state.append('Character')
        count=1 
    elif line.find('Object[')!=-1:
        state.append('Object')
        count=1 
    elif line.find('Tile[')!=-1:
        state.append('Tile')
        count=1 
    elif line.find('Def[')!=-1:
        state.append('Def')
        count=1 
    elif line.count('['):
        count+=line.count('[')
    elif line.count(']'):
        count-=line.count(']')
        if count==0:
            state=[]
        
print '-----------------Def: '
for line in Def[:-1]:
    print line[:-1]
    
print '-----------------Map: '
for line in Map:
    print line[:-1]

"""



palabra=""

zeta=[]

def evaluar():  
    #print palabra
    #palabra=""
    if palabra!="":
        zeta.append(palabra)

for linea in a.readlines():
    for letra in linea[:-1]:
        if letra==" " or letra==":":
            evaluar()
            palabra=""
        else:
            palabra += letra
    
    evaluar()
    palabra=""



#for line in zeta:
#    print coloreado.bonito(str(line))


#print xml

#print xml.__doc__
#print dir(xml)

import marshal

print coloreado.bonito(str(dir(marshal)))
print marshal.__doc__
#print "----------------------------------------------------"
#print dir(marshal.dump.__init__)

#dump1=marshal.dump('a','a')

arch=file('ze.xml','rw')


def listar(modulo):
    puede = dir(modulo)

    for x in puede:
        space=[]
        for i in range(25-len(str(x))):
            space.append(' ') 
        print str(x) + "".join(space) + ": " + str(getattr(marshal.load,x))
    
    return puede

p=listar(marshal.load)

for text in p:
    try:
        print "\n>>" + text + ""
        listar(getattr(marshal.load,text))
    except:pass


#print archivo
