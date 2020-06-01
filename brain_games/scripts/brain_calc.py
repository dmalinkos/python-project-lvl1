import brain_games.games.calc as calc
from brain_games.engine import core


STEPS = 3
MAX_NUMBER = 100


def main():
    core(calc.game_calc(STEPS, MAX_NUMBER), STEPS)


if __name__ == '__main__':
    main()
