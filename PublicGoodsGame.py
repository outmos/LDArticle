import random
import math
import numpy as np
import matplotlib.pyplot as plt

from Player import Player

class PublicGoodsGame:

	def __init__(self, n, m, p, runs, r, c, s, mu):

		self.n = 2
		self.m = m
		self.p = p
		self.runs = runs
		self.r = r
		self.c = c
		self.s = s
		self.mu = mu
		self.players = [Player(random.randint(0, self.n), i) for i in range(self.m)]
		self.state = []
		self.players_payoffs = [0 for i in range(self.m)]


	def negotiations(self, players):

		self.state = [np.random.choice(['C', 'D'], p=[self.p, 1-self.p]) for i in range(self.n)]

		for i in range(self.n):
			players[i].set_id(i)

		while not self.is_stationary_state(players):

			player = self.get_random_players(players, 1)[0]

			if player.change_thought(self.state):

				player.update_thought(self.state)


	def run_two_person_game(self):

		x = [i for i in range(self.runs)]
		results = [[], [], []]

		# run generations
		for i in range(self.runs):
			print("Run {}".format(i))
			self.players_payoffs = [0 for i in range(self.m)]

			# M games
			for j in range(self.m):

				players = self.get_random_players(self.players, self.n)

				self.negotiations(players)
				self.play_two_person_game(players)

			# average payoff
			self.players_payoffs = [payoff/self.runs for payoff in self.players_payoffs]

			self.update_process()

			results[0].append([player.get_strat() for player in self.players].count(0))
			results[1].append([player.get_strat() for player in self.players].count(1))
			results[2].append([player.get_strat() for player in self.players].count(2))

		plt.title("Strategies frequencies over generations")
		plt.xlabel("Generations")
		plt.ylabel("Strategy frequency")

		plt.plot(x, results[0], label="C_0")
		plt.plot(x, results[1], label="C_1")
		plt.plot(x, results[2], label="C_2")

		plt.legend()
		plt.show()

				
	def play_two_person_game(self, players):

		gain = (self.r*self.c*self.state.count('C'))/self.n

		for player in players:

			if self.state[player.get_id()] == "C":
				self.players_payoffs[player.get_player_number()] += gain-self.c
			else:
				self.players_payoffs[player.get_player_number()] += gain

		
	def update_process(self):

		players = self.get_random_players(self.players, self.n)

		strat_player_1 = players[0].get_strat()
		strat_player_2 = players[1].get_strat()

		payoff_player_1 = self.players_payoffs[players[0].get_player_number()]
		payoff_player_2 = self.players_payoffs[players[1].get_player_number()]

		delta = payoff_player_2 - payoff_player_1

		# mutation
		if random.random() < self.mu:

			players[0].set_strat(random.choice([i for i in range(self.n+1) if i != strat_player_1]))
		else:
			# fermi process
			if random.random() < 1./(1 + math.exp(-self.s*delta)):

				players[0].set_strat(strat_player_2)


	def get_random_players(self, players, n):

		return random.sample(players, n)


	def is_stationary_state(self, players):

		for player in players:

			if player.change_thought(self.state):
				return False

		return True