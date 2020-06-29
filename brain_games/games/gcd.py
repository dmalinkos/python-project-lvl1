from random import randint


RULES = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def new_game():
    a, b = randint(1, MAX_NUMBER), randint(1, MAX_NUMBER)
    quest = '{} {}'.format(a, b)
    result = str(gcd(a, b))
    return quest, result
