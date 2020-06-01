from random import randint


def game_even(STEPS, MAX_NUMBER):
    rule = 'Answer "yes" if number even otherwise answer "no".'
    quest = [0 for i in range(STEPS)]
    result = [0 for i in range(STEPS)]
    for step in range(STEPS):
        quest[step] = randint(1, MAX_NUMBER)
        if quest[step] % 2 == 0:
            result[step] = 'yes'
        else:
            result[step] = 'no'
    return rule, quest, result
