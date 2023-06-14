from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round():
    question = randint(0, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(num):
    if num <= 1:
        return False
    num_sqrt = int(sqrt(num))
    div = range(2, (num_sqrt + 1))
    for elem in div:
        if num % elem == 0:
            return False
    return True
