from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_round():
    operators = ['+', '-', '*']
    operator = choice(operators)
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, str(answer)
