from PublicGoodsGame import PublicGoodsGame


if __name__ == '__main__':

	n = 2
	M = 1000
	p = 1
	runs = 1000
	r = 1.5
	c = 1.0
	s = 10
	mu = 10**-4

	game = PublicGoodsGame(n, M, p, runs, r, c, s, mu)
	game.run_two_person_game()