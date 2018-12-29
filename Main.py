from PublicGoodsGame import PublicGoodsGame

if __name__ == '__main__':
	n = 2
	M = 36
	p = 0.5
	runs = 100
	generations = 10000

	r = 1.5
	c = 1.0
	mu = 10**-4
	s = 10**4

	game = PublicGoodsGame(n, M, p, runs, generations, r, c, mu, s)
	game.run_two_person_game()