
class Player:

	def __init__(self, strat, player_number):

		self.player_number = player_number
		self.strat = strat
		self.id = 0

	def __str__(self):

		return "Player {} k : {}".format(self.strat)

	def get_player_number(self):

		return self.player_number

	def get_strat(self):

		return self.strat

	def set_strat(self, strat):

		self.strat = strat

	def get_id(self):

		return self.id

	def set_id(self, ID):

		self.id = ID

	def change_thought(self, state):
		
		if (state[:self.id] + state[self.id+1:]).count("C") < self.strat:

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