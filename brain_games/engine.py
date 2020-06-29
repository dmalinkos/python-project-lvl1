import brain_games.cli as cli


STEPS = 3


def core(game):
    print('Welcome to the Brain Games!')
    print(game.RULES + '\n')
    name = cli.welcome_user()
    print(f'Hello, {name}!')
    for step in range(STEPS):
        quest, res = game.new_game()
        print(f'Question: {quest}')
        ans = cli.get_answer()
        if ans != res:
            print(f"'{ans}' is wrong answer ;(.", end='')
            print(f"Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            return False
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
    return True
