A, B, C, D, E, F, G, H, I, J, K, L, M=10,11,12,13,14,15,16,17,18,20,21,22,23

relacion={
    0 : None,
    1 : "Dirt Block",
    2 : "Grass Block",
    3 : "Stone Block",
    4 : "Water Block",
    5 : "",
    6 : "Wood Block",
    9 : "Rock",
    A : "Selector",
    #A: "Character Boy",
    B : "Star",
    C : "Brown Block",
    D : "Ramp East",
    E : "Ramp South",
    F : "Ramp West",
    G : "Roof West",
    H : "Roof East",
    J : "Tree Short",
    K : "Key",
    L : "Door Tall Closed",
    M : "Window Tall",
    'personaje': "Character Boy",
    #'personaje':'Selector',
    }
    
_pisable={
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
    
_bloqueable={
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
class verdad:
    def __getitem__(self, clave):
        return True
class falso:
    def __getitem__(self, clave):
        return False
        
bloqueable = falso()
pisable = verdad()
    
matriz=[
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
]

matriz2=[
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[2,2,2,3,3,1,1],
]

matriz3=[
[3,4,4,3,3,3,3],
[3,4,4,3,3,3,3],
[3,4,4,3,3,3,E],
[2,4,4,2,3,0,0],
[2,4,4,2,3,K,0],
]

matriz4=[
[0,0,0,0,M,L,M],
[F,3,3,3,D,0,0],
[0,3,A,0,0,9,0],
[0,3,0,0,0,0,0],
[0,0,0,3,3,0,0],
]

matriz5=[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,3,0,0,0,0,0],
[0,0,0,0,3,0,0],
]

matriz6=[
[0,0,0,0,6,6,6],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,3,0,0,0,0,0],
[0,0,0,0,J,0,0],
]
matriz7=[
[0,0,0,0,G,C,H],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
]
matriz0=[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
]
matriz9=[
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,3,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
]
    
capas=[matriz, matriz2, matriz3,matriz4,matriz5,matriz6,matriz7,matriz0,matriz0,matriz0,matriz9]

