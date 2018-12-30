import networkx as nx
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np

NB_NODE = 20

P = 0.2
R = 1.5
C = 1.0
MU = 10**-2

G = nx.barabasi_albert_graph(NB_NODE,4)

#PART 2

def change_thought(t_p1,s_p1,t_p2):
	if t_p2 < s_p1:
		if t_p1 == 0:
			return False
		else:
			return True
	else:
		if t_p1 == 1:
			return False
		else:
			return True

def is_stationary_state(t_p1,s_p1,t_p2,s_p2):
	return (not (change_thought(t_p1,s_p1,t_p2) or change_thought(t_p2,s_p2,t_p1)) )

NB_ROUNDS = 100
COLOR = ['g','b','r']
#s->inf
#'C' = 1 and 'D'=0
strategies = []


xx = list(range(NB_ROUNDS))
yy = [[] for i in range(3)]

for j in range(G.number_of_nodes()):
	strategies.append(randint(0,2))

for rounds in range(NB_ROUNDS):
	thought = [np.random.choice([1,0], p=[P, 1-P]) for i in range(NB_NODE)]
	payoffs = [[-1 for i in range(NB_NODE)] for j in range(NB_NODE)]
	av_payoffs = []

	#On fait jouer tout le monde
	for p1 in range(NB_NODE):
		for p2 in G.neighbors(p1):
			if payoffs[p1][p2] == -1:
				
				#negotiation
				while not is_stationary_state(thought[p1],strategies[p1],thought[p2],strategies[p2]):
					if randint(1,2) == 1:
						if change_thought(thought[p1],strategies[p1],thought[p2]):
							thought[p1] = 1 if thought[p1] == 0 else 0
					else:
						if change_thought(thought[p2],strategies[p2],thought[p1]):
							thought[p2] = 1 if thought[p2] == 0 else 0

				#jeu
				nb_cooperator = thought[p1] + thought[p2]
				
				payoffs[p1][p2] = nb_cooperator*R*C/2
				if thought[p1] == 1:
					payoffs[p1][p2] -= C
				
				payoffs[p2][p1] = nb_cooperator*R*C/2
				if thought[p2] == 1:
					payoffs[p2][p1] -= C
				
	#Calcule average payoff
	for p1 in range(NB_NODE):
		av_payoffs.append((sum(payoffs[p1])+NB_NODE-G.degree[p1])/G.degree[p1])

	n_color = []
	lbl = {}
	for i in range(NB_NODE):
		n_color.append(COLOR[strategies[i]])
		lbl[i] = str(i)+": "+str(av_payoffs[i])[:5]

	nx.draw(G, labels=lbl, node_size = 800, node_color=n_color)
	plt.show()


	#On les fait changer de strat
	for p1 in range(NB_NODE):
		p2 = list(G.neighbors(p1))[randint(0,G.degree[p1]-1)]
		if av_payoffs[p1] < av_payoffs[p2]:
			strategies[p1] = strategies[p2]

	if random()<MU:
		p1 = randint(0,NB_NODE-1)
		new_strat = random.randint(0,1)
		if new_strat >= strategies[p1]:
			new_strat += 1
		strategies[p1] = new_strat

	for i in range(3):
		yy[i].append(strategies.count(i))

"""


for i in range(3):
	plt.plot(xx,yy[i],COLOR[i],label="C"+str(i))
plt.legend()
plt.show()"""