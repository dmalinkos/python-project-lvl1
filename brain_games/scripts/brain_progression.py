import brain_games.games.progression as progression
from brain_games.engine import core


STEPS = 3
MAX_NUMBER = 50


def main():
    core(progression.game_progression(STEPS, MAX_NUMBER), STEPS)


if __name__ == '__main__':
    main()
