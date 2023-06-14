from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def question():
    operators = ['+', '-', '*']
    operator = choice(operators)
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        correct = num1 + num2
    elif operator == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2
    question_and_answer = [question, str(correct)]
    return question_and_answer
