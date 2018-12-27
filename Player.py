
class Player:

    def __init__(self, id, strat):

        self.id = id
        self.strat = strat

    def __str__(self):

        return "Player {} k : {}".format(self.id+1, self.strat)

    def get_strat(self):

        return self.strat

    def change_thought(self, state):

       if (state[0:self.id]+state[self.id:-1]).count("C") < self.strat:

           if state[self.id] == 'D':
                return False
           else:
               return True
       else:
           if state[self.id] == 'C':
               return False
           else:
               return True

    def update_thought(self, state):

        state[self.id] = "C" if state[self.id]=="D" else "D"