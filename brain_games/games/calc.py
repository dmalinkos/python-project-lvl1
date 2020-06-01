from random import randint, choice


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def game_calc(STEPS, MAX_NUMBER):
    rule = 'What is the result of the expression?'
    quest = [0 for i in range(STEPS)]
    result = [0 for i in range(STEPS)]
    for step in range(STEPS):
        a, b = randint(1, MAX_NUMBER), randint(1, MAX_NUMBER)
        exps = [('+', plus(a, b)), ('-', minus(a, b)), ('*', multi(a, b))]
        operation = choice(exps)
        quest[step] = '{} {} {}'.format(a, operation[0], b)
        result[step] = str(operation[1])
    return rule, quest, result
