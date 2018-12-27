import random
import numpy as np
from Player import Player

class PublicGoodsGame:

    def __init__(self, m, p, runs, r, c, mu):

        self.m = m
        self.p = p
        self.runs = runs
        self.r = r
        self.c = c
        self.mu = mu
        self.players = [Player(i, random.randint(0, self.m)) for i in range(self.m)]
        self.state = []
        self.players_payoffs = [0 for i in range(self.m)]

        self.payoff_matrix = [[-self.c+self.r*self.c, -self.c+self.r*self.c, -self.c+(1/2)*self.r*self.c],
                              [-self.c+self.r*self.c, self.p*(-self.c+self.r*self.c), 0],
                              [(1/2)*self.r*self.c, 0, 0]]

    def run_two_person_game(self):

        n = 2

        for i in range(self.runs):

            self.state = [np.random.choice(['C', 'D'], p=[self.p, 1-self.p]) for i in range(n)]

            players = self.get_random_players(self.players, n)

            while not self.is_stationary_state():

                player = self.get_random_players(players, 1)[0]

                if player.change_thought(self.state):

                    player.update_thought(self.state)

            # compute payoffs and update strategies


    def get_random_players(self, players, n):

        return random.sample(players, n)


    def is_stationary_state(self):

        for i in range(len(self.players)):

            if self.players[i].change_thought(self.state):
                return False

        return True