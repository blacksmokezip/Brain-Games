from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    question = randint(1, 1000)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
