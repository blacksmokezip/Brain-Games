from random import randint
import prompt


def main():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".''')
	correct_answers = 0
	while correct_answers <= 3:
		number = randint(1, 10000)
		if number % 2 == 0:
			correct = 'yes'
		else:
			correct = 'no'
		print(f'Question: {number}')
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
	main()
