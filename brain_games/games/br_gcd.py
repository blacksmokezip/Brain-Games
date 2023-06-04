from random import randint
from math import gcd


def task():
	task = 'Find the greatest common divisor of given numbers.'
	return task
def question():
	num1 = randint(1, 100)
	num2 = randint(1, 100)
	question = f'{num1} {num2}'
	correct = gcd(num1, num2)
	question_and_answer = [question, str(correct)]
	return question_and_answer
