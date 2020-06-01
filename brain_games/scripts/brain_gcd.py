import brain_games.games.gcd as gcd
from brain_games.engine import core


STEPS = 3
MAX_NUMBER = 100


def main():
    core(gcd.game_gcd(STEPS, MAX_NUMBER), STEPS)


if __name__ == '__main__':
    main()
