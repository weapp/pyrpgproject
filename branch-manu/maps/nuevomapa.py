from rpg.block import *

A=Block('None',NOT_FLOOR)

class mapa:
    def __init__(self):
        self.pos=[0,1,1]
        self.pos_campo=[0,0]
        self.TILE_WIDTH=101
        self.TILE_Y_SPACING=82
        self.TILE_DEPTH=40
        self.TILE_HEIGHT=171
        
        A=Block('None',NOT_FLOOR)        
        B=Block('Stone Block',BLOCK)   
        C=Block('Grass Block',BLOCK)     
        D=Block('Dirt Block',BLOCK)
        
        
        
        self.caps=[
        [
        [A,D,D,D,D,D,A,A,A,A,A,A,A,A,D,D,D,D],
        [D,D,D,A,D,A,A,A,A,A,A,A,D,D,D,D,D,D],
        [D,D,D,A,D,D,D,D,D,D,D,D,D,D,D,D,D,D],
        [A,A,A,A,A,D,A,A,A,A,A,A,A,A,D,D,D,D],
        ],
        
        [
        [A,A,C,C,C,C,A,A,A,A,A,A,A,A,C,C,C,C],
        [C,C,C,A,C,A,A,A,A,C,C,C,C,C,C,C,C,C],
        [A,C,C,A,C,C,C,C,C,C,C,C,C,C,C,C,C,C],
        [A,A,A,A,A,A,A,A,A,A,A,A,A,A,C,C,C,C],
        ],
        
        [
        [A,A,A,A,A,B,A,A,A,A,A,A,A,A,A,A,A,B],
        [],
        [A,B]
        ],
        
        []
        ]
        
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
        
    def get_character_image(self):
        return Block('Character Cat Girl').image
        
    def get_x_max(self):
        return len(self.caps[0][0])
        
    def get_y_max(self):
        return len(self.caps[0])
        
    def get_z_max(self):
        return len(self.caps)
        
    def update(self):
        pass
