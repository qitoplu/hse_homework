import sys
import time
import random
import string
from additional import dictionary, correct_answers
from additional import add_string, wrong, right

TIMEOUT = 0


def hello():
    while True:
        agree = input('Да / Нет \n')
        if agree == 'Да' or agree == 'Нет':
            break
        else:
            print('Неверный ввод, попробуйте еще раз. \n')
    if agree == 'Да':
        return add_string
    elif agree == 'Нет':
        sys.exit()


def check_answer(response):
    for key, value in correct_answers.items():
        if response == value:
            correct_answers.pop(key)
            return random.choice(right)
        else:
            correct_answers.pop(key)
            return random.choice(wrong)


"""def check_input(answer):
    while True:
        if answer not in SYMBOLS or answer not in ALPHABET:
            return answer
        else:
            'Неверный ввод'
        break
"""


def main():
    while True:
        if __name__ == '__main__':
            for key, value in dictionary.items():
                print(key)
                print(value)
                dictionary.pop(key)
                break
            answer = input()
            print(check_answer(answer))
            if not dictionary:
                print('Больше вопросов нет!')
                break


print('Привет, это викторина. Играем?')
print(hello())
time.sleep(TIMEOUT)
main()
