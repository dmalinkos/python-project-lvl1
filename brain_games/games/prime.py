from random import randint


def isprime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def game_prime(STEPS, MAX_NUMBER):
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    quest = [0 for i in range(STEPS)]
    result = [0 for i in range(STEPS)]
    for step in range(STEPS):
        quest[step] = randint(1, MAX_NUMBER)
        result[step] = 'yes' if isprime(quest[step]) else 'no'
    return rule, quest, result
