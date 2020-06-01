import brain_games.cli as cli


def core(game, STEPS):
    rule = game[0]
    quest = game[1]
    res = game[2]
    print('Welcome to the Brain Games!')
    print(rule + '\n')
    name = cli.welcome_user()
    for step in range(STEPS):
        print(f'Question: {quest[step]}')
        ans = cli.get_answer()
        if ans != res[step]:
            print(f"'{ans}' is wrong answer ;(.", end='')
            print(f"Correct answer was '{res[step]}'.")
            print(f"Let's try again, {name}!")
            return False
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
    return True
