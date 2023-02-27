import sys
import time
import random
import string
from additional import dictionary, correct_answers
from trashbox import add_string, wrong, right

TIMEOUT = 0
ALPHABET = 'йцукенгшщзхъфывапролджэячсмитьбюё'
complex = ALPHABET + string.punctuation + string.whitespace
lst_count = []
countt = 0


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
            lst_count.append('+')
            return random.choice(right)
        else:
            correct_answers.pop(key)
            lst_count.append('-')
            return random.choice(wrong)


def check_input(response):
    splitted = ''.join(response.lower().split(','))
    for symbol in splitted:
        if symbol in complex:
            return True
        elif symbol not in splitted:
            return False


def count(listik, counttt):
    for i in listik:
        if i == '+':
            counttt += 1
    print(f'Количество баллов: {counttt}.')


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
            if not dictionary:
                print('Больше вопросов нет!')
                break


print('Привет, это викторина. Играем?')
print(hello())
time.sleep(TIMEOUT)
main()
print(count(lst_count, countt))
