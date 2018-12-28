
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

	def change_thought(self, state_class, players, n):
		state = []
		for p in players:
			if p.id != self.id:
				state.append(state_class[p.id])

		if state.count("C") < self.strat:

			if state_class[self.id] == 'D':
				return False
			else:
				return True
		else:
			if state_class[self.id] == 'C':
				return False
			else:
				return True

	def update_thought(self, state):

		state[self.id] = "C" if state[self.id] == "D" else "D"