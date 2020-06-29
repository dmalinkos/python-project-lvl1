import random


RULES = 'What number is missing in the progression?'
MAX_NUMBER = 100


def new_game():
    number_of_members = 10
    step_pr = random.choice(range(1, 11))
    start = random.randint(1, MAX_NUMBER)
    progression = ([str(i) for i in range(start,
                    start + number_of_members * step_pr + 1, step_pr)])
    res_index = random.choice(range(number_of_members))
    result = str(progression.pop(res_index))
    progression.insert(res_index, '..')
    quest = ' '.join(progression)
    return quest, result
