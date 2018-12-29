import random
import numpy as np
from Player import Player
import matplotlib.pyplot as plt

NB_GAME = 10  # number of games each player will be playing

class PublicGoodsGame:

	def __init__(self, n, m, p, runs, r, c, mu, s):

		self.n = n
		self.m = m
		self.p = p
		self.runs = runs
		self.r = r
		self.c = c
		self.mu = mu
		self.s = s

		self.players = [Player(random.randint(0, n), i) for i in range(self.m)]
		self.average_payoffs = [0 for i in range(self.m)]
		self.state = []

	def run_two_person_game(self):

		yy = [[] for i in range(self.n+1)]

		time_average_frequency = [0 for i in range(self.n+1)]
		
		for i in range(0, self.runs):

			self.average_payoffs = [0 for i in range(self.m)]

			if i %100 == 0:

				print("runs ",i)

			for game_number in range(NB_GAME):

				# create pairs
				random.shuffle(self.players)

				self.state = [np.random.choice(['C', 'D'], p=[self.p, 1-self.p]) for i in range(self.m)]

				for group in range(self.m//self.n):

					players = self.players[group*self.n:(group+1)*self.n]

					# negotiations stage ------------------------------------------------
					self.negotiations(players)

					# play the game --------------------------------------------------
					self.play_game(players)

				# update process  ------------------------------------------------
				self.update_process()

				# check if all players have the same strategy
				strats = [player.strat for player in self.players]
				if len(set(strats)) == 1:
					time_average_frequency[strats[0]] += 1
				
			count = [0 for i in range(self.n+1)]
			for player in self.players:
				count[player.strat] += 1
			for j in range(self.n+1):
				yy[j].append(count[j])

		xx = np.arange(0,self.runs,1)

		plt.title("Strategies frequencies over generations")
		plt.xlabel("generations")
		plt.ylabel("Strategy frequency")

		for i in range(self.n+1):
			plt.plot(xx, yy[i], label=r"$C_{}$".format(i))

		plt.legend()
		plt.show()

		x = [i+1 for i in range(self.n+1)]
		labels = [r"$C_{}$".format(i) for i in range(self.n+1)]
		time_average_frequency = [(time/self.runs)*100 for time in time_average_frequency]

		plt.title("Time-averaged-frequencies")
		plt.xlabel("Strategies")
		plt.ylabel("Frequency")
		plt.bar(x, time_average_frequency, color="green")
		plt.xticks(x, labels)
		plt.show()

	def negotiations(self, players):

		while not self.is_stationary_state(players):

			player = random.choice(players)

			if player.change_thought(self.state, players):
				player.update_thought(self.state)

	def play_game(self, players):

		k = 0				# number of cooperators
		for player in players:
			if self.state[player.id] == 'C':
				k += 1

		gain = (self.r*self.c*k)/self.n
		for player in players:
			if self.state[player.id] == "C":
				self.average_payoffs[player.id] += (gain-self.c)/NB_GAME
			else:
				self.average_payoffs[player.id] += (gain)/NB_GAME

	def update_process(self):

		player_1, player_2 = self.get_random_players()

		if random.random() < self.mu:

			new_strat = random.choice([i for i in range(self.n+1) if i != player_1.strat])
			player_1.strat = new_strat
		
		else:
			delta =self. average_payoffs[player_2.id] - self.average_payoffs[player_1.id]

			if random.random() < 1/(1+np.exp(-self.s*delta)):
				player_1.strat = player_2.strat

	def get_random_players(self):

		return random.sample(self.players, 2)

	def is_stationary_state(self, players):

		for player in players:

			if player.change_thought(self.state, players):
				return False
		return True