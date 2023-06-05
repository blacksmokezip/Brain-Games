from random import randint


def task():
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return task


def question():
    question = randint(1, 100)
    counter = 0
    for i in range(2, question // 2+1):
        if (question % i == 0):
            counter += 1
    if (counter <= 0):
        correct = 'yes'
    else:
        correct = 'no'
    question_and_answer = [question, correct]
    return question_and_answer
