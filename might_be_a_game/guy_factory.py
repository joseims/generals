from guy import Guy
import constants as c

class GuyFactory:
    '''
    This is guy factory, it makes guys, it makes guy's
    by it's own, but it also allow's lovely couple's
    to make their own guys
    '''

    def __init__(self):
        self.count = 0


    def create_a_nude_guy(self):
        new_guy = Guy()
        new_guy.id = self.count
        self.count += 1
        return new_guy

    def create_new_guy_by_magic(self, god=None, traits=None):
        new_guy = self.create_a_nude_guy()

        if traits:
            new_guy.traits = traits

        new_guy.heritage.add(god)

        return new_guy

    def create_new_guy_from_parents(self, mom1, mom2):
        new_guy = self.create_a_nude_guy()


        mom1_heritage = mom1.get_my_rand_heritage()
        mom2_heritage = mom2.get_my_rand_heritage()

        new_guy.heritage = mom1_heritage.union(mom2_heritage)

        for _ in range(c.mom_son_bond_iterations): #Making mother son bond
            new_guy.interact(mom1)
            new_guy.interact(mom2)

        new_guy.pos_x = mom1.pos_x
        new_guy.pos_y = mom1.pos_y
        
        return new_guy