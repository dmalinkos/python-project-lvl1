import brain_games.games.prime as prime
from brain_games.engine import core


STEPS = 3
MAX_NUMBER = 10000


def main():
    core(prime.game_prime(STEPS, MAX_NUMBER), STEPS)


if __name__ == '__main__':
    main()
