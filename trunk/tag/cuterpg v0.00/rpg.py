from __future__ import with_statement
import coloreado


with open("hello.txt") as f:
    #f =  open("hello.txt")
    
    fil=[]
    for line in f:
        line=line[:-1]
        print coloreado.red_bold ( ">>> " ) + coloreado.red ( line )
        line=line.split(":")
        if len(line)>1:
            for i in range(len(line) - 1):
                line[i+1]=line[i+1].split(",")
        print coloreado.bonito("   " + str(line) + "\n")
        fil.append(line)

print "--"    
print coloreado.bonito (str(fil))

print "--"    

keys={}
for line in range(len(fil)):
    print coloreado.bonito('line '+ str(line) +" :" + str(fil[line]))
    if len(fil[line])==1:
        keys[fil[line][0]]=True
    else:
        keys[fil[line][0]]=fil[line][1:]
        

print coloreado.bonito(str(keys))
    
    
#archivo = file('nivel4.txt', 'rt')
#contenido = archivo.readlines()

print  coloreado.color('red')

#x='toostis'
#print x.replace('toostis', '\033[0;31mtoostis\033[m')

g=l=f=''

keys=__import__('hello',g,l,f)

print keys
print g,l,f


options  = dir(keys)
print "\n\n--\n\n"
for option in options:
   print '\n'+ coloreado.red(str(option)) + ':\n'+ coloreado.bonito(str(getattr(keys,option)))
   

print coloreado.azul("-------------------------------alalallalala-------------------")

for opt in keys.__builtins__.keys():
    print coloreado.red(str(opt)) + ":"
    print coloreado.bonito(str(keys.__builtins__[opt]))


print dir(keys.__builtins__['id'])
