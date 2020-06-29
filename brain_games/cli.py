import prompt


def welcome_user():
    return prompt.string('May I have your name? ') 


def get_answer():
    return prompt.string('Your answer: ')
