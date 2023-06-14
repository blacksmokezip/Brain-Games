from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_round():
    progression = []
    num = randint(1, 100)
    step = randint(2, 10)
    for i in range(10):
        progression.append(num)
        num += step
    missed_num = randint(0, 9)
    answer = progression[missed_num]
    progression[missed_num] = '..'
    question = " ".join(map(str, progression))
    return question, str(answer)
