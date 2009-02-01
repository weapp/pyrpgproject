#!/usr/bin/python
# Nombre : xml5.py
import xml.dom.minidom

"""
el parser ejecutaria una simulacion de:

#cabecera, siempre igual
import stateload as s
import core
c=core.Core()
m=c.get_app().get_model()

#cuerpo
#lo que se nombra como objetos en el xml, simplemente pueden ser funciones que parseen de alguna manera los datos
#y que llamen a un constructor para que devuelvan un objeto

m.add(s.personaje(position=s.point(x="45",y="25"),name="Aaron",money="50"))
m.add(s.enemy(position=s.point("70","20"),ia="lala",destiny=s.point("20",y="45")))
m.add(s.place(----))


-------------modulo stateload--------------------------
#la funcion personaje podria ser algo asi:
def personaje(position,name,money):
    p=rpg.personaje(name)
    p.set_position(position)
    p.set_money(money)
    return p
    
def point(x=0,y=0):
    return ModuloNoseke.Vector2D(int(x),int(y))
"""

class stateload (object):
    """
    esta clase no es mas que para que no de error al ejecutar el codigo
    simula al modulo que contendra las funciones para cargar los objetos
    """
    def __init__(self):
        pass

    def __getattr__(self,attr):
        """
        simula las funciones que devolveran los objetos dentro del modulo.
        No tendrna por que ser necesariamente constructores.
        Los objetos que devuelven dichas funciones seran cadenas, que contienen
        el nombre y los parametros con que fue llamado.
        """
        def x (*args,**dic):
            return "<<"+attr + "("  + str(args) + str(dic) + ")"+">>"
        return x
        
    def add(self,attr):
        print "anyadiendo:"+attr
        
s=stateload()
m=stateload()

def main():
    cargar_estado("./xml1.xml")
            
def cargar_estado(xmlfile):
    config=xml.dom.minidom.parse(xmlfile)
    state=config.firstChild
    assert state.tagName == "state"
    for obj in state.childNodes:
        if obj.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            m.add(parsear_objeto(obj))
            
def parsear_parametro(elem):
    assert elem.tagName == "param"
    if hasElementNodes(elem):#si el parametro es un objeto,seguir profundizando
        for obj in elem.childNodes:
            if obj.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
                return parsear_objeto(obj)
    else:
        return elem.firstChild.data.strip()
    
def parsear_objeto(obj):
    assert obj.tagName == "obj"
    assert obj.attributes.has_key("type")
    args=[]
    dic={}
    for elem in obj.childNodes:
        if elem.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            parametro=parsear_parametro(elem)
            if elem.attributes.has_key("name"):
                dic[str(elem.attributes.get("name").value)]=parametro
            else:
                args.append(parametro)
    constructor=getattr(s,obj.attributes["type"].value)
    return constructor(*args,**dic)

def hasElementNodes(node):
    for elem in node.childNodes:
        if elem.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            return True
    return False

if __name__ == "__main__": main()
