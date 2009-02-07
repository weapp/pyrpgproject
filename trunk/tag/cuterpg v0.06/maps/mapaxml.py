from rpg.block import *
import xml.dom.minidom
import string
from library import images
import os

def _parsea_tiles(node,dic):
    for tile in node.childNodes:
        if tile.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            assert tile.tagName=="tile"
       
            name=str(tile.attributes.get("name").value)
            image=tile.attributes.get("image").value
            b=str(tile.attributes.get("block").value).lower() not in ('false','f','0') 
            t=str(tile.attributes.get("tall").value).lower() not in ('false','f','0')
            f=str(tile.attributes.get("floor").value).lower() not in ('false','f','0')
            flags=(b*BLOCK) | (t*TALL) | (f*FLOOR)

            dic[name]=Block(image,flags)
            
def _parsea_layers(node,dic):
    layers=[]
    for layer in node.childNodes:
        if layer.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            assert layer.tagName=="layer"
            text=str(layer.firstChild.data.strip())
            text=map(string.split,text.splitlines())
            #text=map(lambda x:map(dic.get,x),text)
            text = [ [ dic[n] for n in line ] for line in text ]
            
            layers.append(text)
    return layers
                   
class mapa:

    
    def __init__(self,xmlfile='maps/pruebas1.xml'):
        
        self.opt={}
        
        config=xml.dom.minidom.parse('images'+os.sep+'tiles.xml')
        tile=config.firstChild
        print tile.tagName
        assert tile.tagName == "tile"
        for op in tile.childNodes:
            if op.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
                self.opt[str(op.tagName)]=int(op.firstChild.data)
        
        print self.opt
        
        """
        self.TILE_WIDTH=101
        self.TILE_Y_SPACING=82
        self.TILE_DEPTH=40
        self.TILE_HEIGHT=171
        """
        self.TILE_WIDTH=self.opt['width']
        self.TILE_Y_SPACING=self.opt['y_spacing']
        self.TILE_DEPTH=self.opt['depth']
        self.TILE_HEIGHT=self.opt['height']

        config=xml.dom.minidom.parse(xmlfile)
        map_=config.firstChild
        assert map_.tagName == "map"
        i=0
        dic={}
        for node in map_.childNodes:
            if node.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
                assert (i==0 and node.tagName == "tiles") or \
                       (i==1 and node.tagName == "layers")
                if i==0:
                    _parsea_tiles(node,dic)
                else:
                    self.caps=_parsea_layers(node,dic)
                i+=1


    def puede_estar(self,x,y,z):
        return self.get_x_max()>x>=0 and self.get_y_max()>y>=0 and self.get_block(x,y,z).floor and not self.get_block(x,y,z+1).block

    def get_block(self,x,y,z):
        try:
            r = self.caps[z][y][x]
        except:
            r = A
        return r

    def get_block_image(self,x,y,z):
        return self.get_block(x,y,z).image

    def get_x_max(self):
        return len(self.caps[0][0])

    def get_y_max(self):
        return len(self.caps[0])

    def get_z_max(self):
        return len(self.caps)

    def update(self):
        pass
