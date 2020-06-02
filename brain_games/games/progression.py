import random


def game_progression(STEPS, MAX_NUMBER):
    rule = 'What number is missing in the progression?'
    number_of_members = 10
    result = [0 for i in range(STEPS)]
    quest = [0 for i in range(STEPS)]
    for step in range(STEPS):
        step_pr = random.choice(range(1, 11))
        start = random.randint(1, MAX_NUMBER)
        progression = ([str(i) for i in range(start,
                        start + number_of_members * step_pr + 1, step_pr)])
        res_index = random.choice(range(10))
        result[step] = str(progression.pop(res_index))
        progression.insert(res_index, '..')
        quest[step] = ' '.join(progression)
    return rule, quest, result
