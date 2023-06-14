import prompt


ROUNDS = 3


def game_runner(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game.DESCRIPTION}')
    for _ in range(ROUNDS):
        question, corr = game.get_round()
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')

        if ans != corr:
            print(f"""'{ans}' is wrong answer ;(. Correct answer was '{corr}'.
Let's try again, {name}!""")
            return
        else:
            print('Correct!')

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_runner()
