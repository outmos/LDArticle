from PublicGoodsGame import PublicGoodsGame


if __name__ == '__main__':
	n = 3
	M = 36
	p = 0.1
	runs = 10**4

	r = 1.2
	c = 1.0
	mu = 10**-4
	s = 10000

	game = PublicGoodsGame(n,M, p, runs, r, c, mu,s)
	game.run_two_person_game()