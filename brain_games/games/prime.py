from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    counter = 0
    for i in range(2, num // 3):
        if (num % i) == 0:
            counter += 1
    if counter <= 0:
        return True
    return False


def get_round():
    question = randint(2, 100)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
