from random import randint


RULES = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUMBER = 100


def new_game():
    quest = randint(1, MAX_NUMBER)
    if quest % 2 == 0:
        res = 'yes'
    else:
        res = 'no'
    return quest, res
