from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 100

def isprime(n):
    d = 2
    while (n // 2) % d != 0:
        d += 1
    return d == n


def new_game():
    quest = randint(1, MAX_NUMBER)
    result = 'yes' if isprime(quest) else 'no'
    return quest, result
