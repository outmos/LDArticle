
class Player:

	def __init__(self, strat):

		self.strat = strat
		self.id = 0

	def __str__(self):

		return "Player {} k : {}".format(self.strat)

	def get_strat(self):

		return self.strat

	def set_id(self, ID):

		self.id = ID

	def change_thought(self, state):
		
		if (state[0:self.id] + state[self.id%2:-1]).count("C") < self.strat:

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

		state[self.id] = "C" if state[self.id] == "D" else "D"