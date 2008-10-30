A, B, C, D, E, F, G, H, I, J=10,11,12,13,14,15,16,17,18,20

def puede_estar(x,y,z):
    return pisable[ capas[z-1][y][x] ] and not bloqueable[ capas[z][y][x] ]
relacion={
    0 : None,
    1 : "Water Block",
    2 : "Stone Block Tall",
    3 : "Grass Block",
    4 : "Dirt Block",
    5 : "Stone Block",
    6 : "Wood Block",
    7 : "Shadow North",
    8 : "Tree Tall",
    9 : "Rock",
    A : "Selector",
    #A: "Character Boy",
    B : "Star",
    C : "Ramp North",
    D : "Ramp East",
    E : "Ramp South",
    F : "Ramp West",
    H : "Shadow East",
    I : "Enemy Bug",
    J : "Tree Ugly",
    'personaje': "Character Cat Girl",
    #'personaje':'Selector',
    }
    
pisable={
    0 : False,
    1 : False,
    2 : False,
    3 : True,
    4 : True,
    5 : True,
    6 : True,
    7 : True,
    8 : False,
    9 : False,
    A : True,
    C : False,
    J : False,
    }
    
bloqueable={
    0 : False,
    1 : True,
    2 : True,
    3 : True,
    4 : True,
    5 : True,
    6 : True,
    7 : False,
    8 : True,
    9 : True,
    A : False,
    C : True,
    D : True,
    E : True,
    F : True,
    H : False,
    I : True,
    J : True,
    }
    
matriz=[
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[5,5,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5],
[5,3,3,3,3,3,4,4,4,5,5,4,4,4,4,4,5],
[5,3,3,3,4,4,4,4,5,5,4,4,4,4,4,4,5],
[5,3,3,3,4,4,4,5,5,4,4,4,4,4,4,4,5],
[5,3,3,4,4,4,4,5,5,4,4,4,4,4,3,3,5],
[5,3,3,4,4,4,4,5,5,4,6,6,3,3,3,3,5],
[5,3,3,3,5,5,4,5,4,6,6,6,1,1,1,1,1],
[5,3,3,3,5,4,4,4,4,6,1,1,1,1,1,1,1],
[5,3,3,3,5,4,4,4,4,6,1,1,5,1,1,1,1],
#[5,5,5,5,5,5,5,5,1,1,1,1,1,1,1,1]
]

matriz2=[
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[5,A,0,8,0,0,0,0,0,0,0,0,0,0,5,1,5],
[5,0,0,0,0,0,0,0,0,5,5,0,0,0,5,5,5],
[5,0,0,0,0,0,0,0,5,5,0,0,0,0,0,9,5],
[5,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,5],
[5,I,0,0,0,0,0,5,5,0,0,0,0,0,0,0,5],
[5,J,0,0,0,0,0,5,5,0,0,0,0,0,0,8,5],
[5,0,0,H,5,5,0,5,E,0,0,0,0,0,0,0,0],
[5,0,0,H,5,0,7,0,0,0,0,0,0,0,0,0,0],
[0,0,J,H,5,0,0,0,0,0,0,0,5,0,0,0,0],
#[5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0]
]

matriz3=[
[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
[5,0,0,0,0,0,0,0,0,C,0,0,0,0,0,0,5],
[5,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,5],
[5,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,5],
[5,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,5],
[5,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,5],
[5,0,0,0,5,5,0,5,0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,0,0,0,0,5,0,0,0,0],
#[5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0]
]

matriz4=[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,9,9,0,0,0,0,0,0,0,C],
[5,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,5],
[5,0,0,0,0,0,0,C,0,0,0,0,0,0,0,0,0],
[0,0,0,0,F,5,5,5,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0],
#[5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0]
]
    
capas=[matriz, matriz2, matriz3, matriz4]

pos=[1,1,1]



def puede_estar(x,y,z):
    return pisable[ capas[z-1][y][x] ] and not bloqueable[ capas[z][y][x] ]
    
TILE_WIDTH = 101
TILE_HEIGHT = 171
TILE_Y_SPACING = 82
TILE_DEPTH = 40
SOUTH_SHADOW_HEIGHT=42

#SCREEN_WIDTH, SCREEN_HEIGHT = 80, 80

#SCREEN_WIDTH, SCREEN_HEIGHT = 7*TILE_WIDTH*4/3, 7*TILE_WIDTH

pos_campo=[0,90]

