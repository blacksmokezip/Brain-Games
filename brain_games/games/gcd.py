from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num2


def get_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    answer = find_gcd(num1, num2)
    return question, str(answer)
