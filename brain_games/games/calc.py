from random import randint, choice
from operator import add, sub, mul


RULES = 'What is the result of the expression?' 
MAX_NUMBER = 100

def new_game():
    a, b = randint(1, MAX_NUMBER), randint(1, MAX_NUMBER)
    exps = [('+', add(a, b)), ('-', sub(a, b)), ('*', mul(a, b))]
    operation = choice(exps)
    quest = '{} {} {}'.format(a, operation[0], b)
    result = str(operation[1])
    return quest, result
