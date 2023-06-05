from random import randint


def task():
	task ='What number is missing in the progression?'
	return task
def question():
	progression = []
	num = randint(1, 100)
	step = randint(2, 10)
	for i in range (10):
		progression.append(num)
		num += step
	missed_num = randint(0, 9)
	correct = progression[missed_num]
	progression[missed_num] = '..'
	question = " ".join(map(str, progression))
	question_and_answer = [question, str(correct)]
	return question_and_answer
