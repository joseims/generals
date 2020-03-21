from random import randint

import constants as c
import utils as u
from guy_factory import GuyFactory as gf
import copy

class AmazingWorld:
    '''
    This is where the stuff happens, where people met each other.
    If a mama boy, met mama girl, and like each other very much
    they have a baby.
    '''
    def __init__(self):
        self.guy_factory = gf()
        self.map = self.setup_map()
        self.players = {}
        self.guys = {}
        self.interaction_counter = 0
        self.love_counter = 0

    def setup_game(self):
        initial_guys = c.start_guys
        for _ in range(initial_guys):
            guy = self.guy_factory.create_a_nude_guy()
            x_pos = randint(0,c.map_x-1)
            y_pos = randint(0,c.map_y-1)
            guy.pos_x = x_pos
            guy.pos_y = y_pos
            self.guys[guy.id] = guy
            print("Guy {} at ({},{})".format(guy.id,x_pos,y_pos))
            self.map[x_pos][y_pos].append(guy.id)

    def step(self):
        for guy_id in list(self.guys.keys()): #Moving guys
            guy = self.guys[guy_id]
            if (guy.steps <= 0):
                self.map[guy.pos_x][guy.pos_y].remove(guy_id)
                del self.guys[guy_id]
                continue

            self.move_guy(guy)

        for x in range(c.map_x): #Interacting guys
            for y in range(c.map_y):
                party_people = self.map[x][y]
                if len(party_people) > 1:
                    self.party(party_people, x, y)

    def party(self, guys, x, y):
        mate_score = c.mate_score
        new_guys = []
        interactions = []
        for i in range(len(guys)):
            for j in range(len(guys)):

                interaction_id1 = "#" + str(i) + "#" + str(j)
                interaction_id2 = "#" + str(j) + "#" + str(i)

                
                if (i == j):
                    continue
                if interaction_id1 in interactions or interaction_id2 in interactions:
                    continue

                guy1_id  = guys[i]
                guy2_id = guys[j]

                guy1 = self.guys[guy1_id]
                guy2 = self.guys[guy2_id]
                guy1_2_score = guy1.get_score(guy2)
                guy2_1_score = guy2.get_score(guy1)

                if guy1_2_score >= mate_score and guy2_1_score >= mate_score:
                    new_guy =  self.guy_factory.create_new_guy_from_parents(guy1,guy2)
                    self.guys[new_guy.id] = new_guy
                    new_guys.append(new_guy.id)
                    self.love_counter += 1

                guy2_copy = copy.deepcopy(guy2)
                guy1_copy = copy.deepcopy(guy1)

                guy1.interact(guy2_copy)
                guy2.interact(guy1_copy)

                interactions.append(interaction_id1)
                interactions.append(interaction_id2)
                self.interaction_counter +=1

        for guy in new_guys:
            self.map[x][y].append(guy)




    def move_guy(self, guy):          
        new_guy_pos_x = guy.pos_x + randint(-4,4)
        new_guy_pos_y = guy.pos_y + randint(-4,4)
        new_guy_pos_x, new_guy_pos_y = u.limit_map(new_guy_pos_x, new_guy_pos_y)
        self.map[guy.pos_x][guy.pos_y].remove(guy.id)
        self.map[new_guy_pos_x][new_guy_pos_y].append(guy.id)
        guy.pos_x = new_guy_pos_x
        guy.pos_y = new_guy_pos_y
        guy.steps -=1


    
    def setup_map(self):
        game_map = [[-1]*c.map_y for _ in range(c.map_x)]
        for i in range(c.map_x):
            for j in range(c.map_y):
                game_map[i][j] = []
        return game_map
