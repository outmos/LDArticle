from PublicGoodsGame import PublicGoodsGame


if __name__ == '__main__':

    M = 36
    p = 0.5
    runs = 10**8
    r = 1.5
    c = 1.0
    mu = 10**-4

    game = PublicGoodsGame(M, p, runs, r, c, mu)
    game.two_person_game()