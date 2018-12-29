
class Player:

	def __init__(self, strat, ID):

		self.strat = strat
		self.id = ID

	def change_thought(self, state_class, players):

		state = []
		for player in players:
			
			if player.id != self.id:
				state.append(state_class[player.id])

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