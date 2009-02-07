#!/usr/bin/python

import random

class Character(object):
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos #Vector de dos valores
        self.life = 20 #Hit Dice
        self.attack = 10
        #self.armor = armor
        #self.weapon = weapon
        self.alive = True
        #self.image = image
        self.state = 'friendly' #friendly, hostile
        self.plot = 0 #Estado en la trama del juego (opcional)

    def causeDamage(self):
        hit = random.randrange(1, self.attack)
        print "Ataque de ", self.name, "puntos de dano: ", hit
        return hit

    def injury(self, hit):
        if self.life <= 0:
            print "Esta muerto"

        elif (self.life - hit) <= 0:
            self.life = 0
            self.alive = False
        else:
            self.life -= hit
        print self.life
            

    def kill():
        if not alive:
            raise SystemExit
        else:
            self.alive = False

class Hero(Character):
    def __init__(self, name, pos):
        Character.__init__(self, name, pos)
        #self.abilities = abilities #Habilidades tipo fuerza, carisma, etc
        self.money = 0

    def addMoney(self, money):
        self.money += money

    
    def movement(self):
        #TODO
        pass
        
