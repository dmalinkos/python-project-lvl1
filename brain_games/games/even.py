import brain_games.cli as cli
import random


def game_even():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = cli.welcome_user()
    step_for_win = 3
    for step in range(step_for_win):
        number = random.randint(0,100)
        print(f'Question: {number}')
        answer =  cli.get_answer()        
        if  number % 2 == 0:
            if answer != 'yes':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again, Bill!")
                return False
            else:
                print('Correct!')
        if  number % 2 == 1:
            if answer != 'no':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(" Let's try again, Bill!")
                return False
            else:
                print('Correct!')
    print(f'Congratulations, {name}!')


