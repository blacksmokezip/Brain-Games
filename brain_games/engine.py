import prompt


def engine(logic):
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print(f'''Hello, {name}!
{logic.task()}''')
	correct_answers = 0
	while correct_answers <= 3:
		question_and_correct = logic.question()
		question = question_and_correct[0]
		correct = question_and_correct[1]
		print(f'Question: {question}')
		answer = prompt.string('Your answer: ')
		if answer == correct:
			print('Correct!')
			correct_answers += 1
		else:
			print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct}'.
Let's try again, {name}!""")
			break
		if correct_answers == 3:
			print(f'Congratulations, {name}!')
			break


if __name__ == '__main__':
	engine()
