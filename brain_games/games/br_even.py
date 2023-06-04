from random import randint


def task():
	task = 'Answer "yes" if the number is even, otherwise answer "no".'
	return task
def question():
	question = randint(1, 1000)
	if question % 2 == 0:
		correct = 'yes'
	else:
		correct = 'no'
	question_and_answer = [question, correct]
	return question_and_answer
