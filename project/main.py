import sys
import time
import random
import string
from additional import dictionary, correct_answers
from trashbox import add_string, wrong, right

TIMEOUT = 0
ALPHABET = 'йцукенгшщзхъфывапролджэячсмитьбюё'
complex = ALPHABET + string.punctuation + string.whitespace


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
        print(':(')
        sys.exit()


def check_answer(response):
    for key, value in correct_answers.items():
        if response.lower() == value:
            correct_answers.pop(key)
            return random.choice(right)
        else:
            correct_answers.pop(key)
            return random.choice(wrong)


def check_input(response):
    a = ''.join(response.lower().split(','))
    for i in a:
        if i in complex:
            return True
        elif i not in a:
            return False


"""def count():
    if check_answer:
        counter += 1
    elif not check_answer:
        counter -= 0.5
    return counter
"""


def main():
    while True:
        if __name__ == '__main__':
            for key, value in dictionary.items():
                print(key)
                print(value)
                dictionary.pop(key)
                break
            while True:
                answer = input('Введите ответ: \n')
                if check_input(answer):
                    print(
                        'Неверный формат ввода! \n'
                        'Введите ответ на латинице без символов и пробелов. \n'
                    )
                    time.sleep(3)
                else:
                    break
            print(check_answer(answer))
            # print(count())
            if not dictionary:
                print('Больше вопросов нет!')
                break


print('Привет, это викторина. Играем?')
print(hello())
time.sleep(TIMEOUT)
main()
