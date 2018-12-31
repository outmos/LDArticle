C = 1
R = 1.5
NB_NEIGHBORS = 4

def get_reward(strat,nbc_0):
	if strat == 0:
		return ((R-1)*nbc_0+((R/2)-1)*(NB_NEIGHBORS-nbc_0))*C/NB_NEIGHBORS
	if strat == 1:#C2
		return R*C*nbc_0/(2*NB_NEIGHBORS)

def get_c0_reward(strat,majority):
	if majority == 0:
		nbc_0 = 4
	else:
		nbc_0 = 1

	if strat == 1:
		nbc_0 -= 1
	return ((R-1)*nbc_0+((R/2)-1)*(NB_NEIGHBORS-nbc_0))*C/NB_NEIGHBORS

def get_c2_reward(strat,majority):
	if majority == 0:
			nbc_0 = 4
	else:
		nbc_0 = 1
	
	if strat == 1:
		nbc_0 -= 1

	return R*C*nbc_0/(2*NB_NEIGHBORS)


print("| Strat | Nb C_0 | Nb C_1 | Majority | ->C_0  | ->C_1  |")
print("--------------------------------------------------------")

for strat in range(2):
	for nbc_0 in range(NB_NEIGHBORS+1):
		for maj in range(2):
			self_reward = get_reward(strat,nbc_0)
			c2_reward = get_c2_reward(strat,maj)
			c0_reward = get_c0_reward(strat,maj)
			p_to = [0,0]
			p_to[1] = (NB_NEIGHBORS-nbc_0)/NB_NEIGHBORS if c2_reward > self_reward else 0
			p_to[0] = nbc_0/NB_NEIGHBORS if c0_reward > self_reward else 0

			p_to[strat] += 1.0-sum(p_to)

			
			print("| C_",strat," |  ",nbc_0,"   |  ",NB_NEIGHBORS-nbc_0,"   |   C_",maj,"  | ",str(p_to[0])," "*(4-len(str(p_to[0]))),"| ",p_to[1]," "*(4-len(str(p_to[1]))),"|")