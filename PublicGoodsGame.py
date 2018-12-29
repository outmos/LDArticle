import random
import numpy as np
from Player import Player
import matplotlib.pyplot as plt

NB_GAME = 10  #nb de game pour un joueur

class PublicGoodsGame:

	def __init__(self, n, m, p, runs, r, c, mu,s):
		self.n = n
		self.m = m
		self.p = p
		self.runs = runs
		self.r = r
		self.c = c
		self.mu = mu
		self.s = s

		self.players = [Player(random.randint(0,n)) for i in range(self.m)]
		for i in range(m):
			self.players[i].set_id(i)

		self.state = []



	def run_two_person_game(self):
		n = self.n

		xx = np.arange(0,self.runs,1)

		yy = [[] for i in range(n+1)]
		
		for i in range(0,self.runs):

			average_payoffs = [0 for i in range(self.m)]
			if i %100 == 0:
				print("runs ",i)

			for game_number in range(NB_GAME):
				#create pair
				random.shuffle(self.players)

				self.state = [np.random.choice(['C', 'D'], p=[self.p, 1-self.p]) for i in range(self.m)]

				for group in range(self.m//n):
					players = self.players[group*n:(group+1)*n]

					# negociations-----------------------------------------------------

					while not self.is_stationary_state(players):
						j = random.randint(0,n-1)
						if players[j].change_thought(self.state, players,n):
							players[j].update_thought(self.state)

					# compute payoffs--------------------------------------------------
					nb_cooperators = 0
					for p in players:
						if self.state[p.id] == 'C':
							nb_cooperators += 1

					gain = (self.r*self.c*nb_cooperators)/n
					for p in players:
						if self.state[p.id] == "C":
							average_payoffs[p.id] += (gain-self.c)/NB_GAME
						else:
							average_payoffs[p.id] += (gain)/NB_GAME

				# update strategies------------------------------------------------

				p1 = random.randint(0,self.m-1)
				p2 = random.randint(0,self.m-2)
				if p2 >= p1:
					p2 += 1

				if random.random() < self.mu:
					new_strat = random.randint(0,n-1)
					if new_strat >= self.players[p1].strat:
						new_strat += 1
					self.players[p1].strat = new_strat
				
				else:
					delta = average_payoffs[self.players[p2].id] - average_payoffs[self.players[p1].id]
					if random.random() < 1/(1+np.exp(-self.s*delta)):
						self.players[p1].strat = self.players[p2].strat

			count = [0 for j in range(n+1)]
			for p in self.players:
				count[p.strat] += 1
			for j in range(n+1):
				yy[j].append(count[j])

		for i in range(n+1):
			plt.plot(xx,yy[i],label="C"+str(i))
		plt.legend()
		plt.show()


	def get_random_players(self, players):
		return random.sample(players, self.n)


	def is_stationary_state(self,players):
		for i in range(self.n):
			if players[i].change_thought(self.state,players,self.n):
				return False
		return True