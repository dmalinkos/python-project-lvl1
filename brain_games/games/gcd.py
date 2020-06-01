from random import randint


def game_gcd(STEPS, MAX_NUMBER):
    rule = 'Find the greatest common divisor of given numbers.'
    quest = [0 for i in range(STEPS)]
    result = [0 for i in range(STEPS)]
    for step in range(STEPS):
        a, b = randint(1, MAX_NUMBER), randint(1, MAX_NUMBER)
        quest[step] = '{} {}'.format(a, b)
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        result[step] = str(a + b)
    return rule, quest, result
