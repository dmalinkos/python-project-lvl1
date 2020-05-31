import brain_games.cli as cli
import random


def game_even():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = cli.welcome_user()
    step_for_win = 3
    for step in range(step_for_win):
        num = random.randint(0, 100)
        print(f'Question: {num}')
        ans = cli.get_answer()
        if num % 2 == 0:
            if ans != 'yes':
                print(f"'{ans}' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again, Bill!")
                return False
            else:
                print('Correct!')
        if num % 2 == 1:
            if ans != 'no':
                print(f"'{ans}' is wrong answer ;(. Correct answer was 'no'.")
                print(" Let's try again, Bill!")
                return False
            else:
                print('Correct!')
    print(f'Congratulations, {name}!')
