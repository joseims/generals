from random import random,randint
import utils as u

class Boolean_:
    '''
    this names are horrible, i need better names.
    A regular boolean it's a variable that it might be positive or negative taste for a trait.
    '''

    def __init__(self):
        self.value = random()*5*self.get_mutate_sign()

    def interact(self, another_bool_value):
        self.value += another_bool_value*5/20
        self.__mutate()

        self.value = u.limit_trait(self.value)

    def __mutate(self):
        mutate_chance = randint(0,100)
        if mutate_chance <= 2:
            self.value += self.get_mutate_sign()*random()*1

    def get_mutate_sign(self):
        mutate_signal = -1 if randint(0,1) else 1
        return mutate_signal


class SimpleMulti:
    ''' 
    A simple multi it's a variable that you either like, or dislike a few set of traits
    #TODO: Develop this
    '''