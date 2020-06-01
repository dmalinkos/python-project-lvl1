import brain_games.games.even as even
import brain_games.engine as engine


STEPS = 3
MAX_NUMBER = 100


def main():
    engine.core(even.game_even(STEPS, MAX_NUMBER), STEPS)


if __name__ == '__main__':
    main()
