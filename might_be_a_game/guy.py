from random import random, randint, sample

from variables import Boolean_ as bo
import constants as c
class Guy:
    '''
    This represents one person.
    It has some traits and interact with other people
    '''

    def __init__(self):
        self.id = None
        self.traits = {}
        self.opinions = {}
        self.pos_x = (-1, -1)
        self.steps = randint(150,300)

        for trait in c.bool_traits:
            self.traits[trait] = -1 if randint(0,1) else 1
            self.opinions[trait] = bo()

        self.heritage = set()

    def get_my_rand_heritage(self):
        inherit_number = c.max_heritage_size//2

        if len(self.heritage) <= inherit_number:
            return self.heritage.copy()

        heritage_copy = self.heritage.copy()
        rand_heritage = set()

        for _ in range(inherit_number):
            heritage_sample = sample(heritage_copy,1)[0]
            heritage_copy.remove(heritage_sample)
            rand_heritage.add(heritage_sample)

        return rand_heritage

    def interact(self, girl):
        for trait in c.bool_traits:
            girl_opinion = girl.traits[trait] #girl trait
            self.opinions[trait].interact(girl_opinion)

    def get_score(self, girl):
        score = 0
        for trait in c.bool_traits:
            girl_trait = girl.traits[trait]
            score += self.opinions[trait].value*girl_trait
        return score

    def __repr__(self):
        rpr = ""
        rpr += "Hey, im {} at ({}, {})\n".format(self.id, self.pos_x, self.pos_y)
        for t in c.bool_traits:
            t_rpr = "" if self.traits[t] else "dont "
            rpr += "I {} have {} and ".format(t_rpr,t)
            rpr += "I think about {}: {}\n".format(t,self.opinions[t].value)
        return rpr

