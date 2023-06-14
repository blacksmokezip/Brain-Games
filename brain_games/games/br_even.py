from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    question = randint(1, 1000)
    if question % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    question_and_answer = [question, correct]
    return question_and_answer
