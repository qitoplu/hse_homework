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
    """Приветственная функция,
    которая предлагает участнику запустить викторину"""
    print('Привет, это викторина. Играем?')
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
    """Функция, проверяющая правильность ответа.
    Если ответ верный, в словарь добавляется плюсик."""
    for key, value in correct_answers.items():
        if response.lower() == value:
            correct_answers.pop(key)
            lst_count.append('+')
            return random.choice(right)
        else:
            correct_answers.pop(key)
            return random.choice(wrong)


def check_input(response):
    """Функция, проверяющая корректность ввода ответа на вопрос.
    В зависимости от ввода выкидывает True,
    если ввод неверный и False, если верный."""
    splitted = ''.join(response.lower().split(','))
    for symbol in splitted:
        if symbol in complex:
            return True
        elif symbol not in splitted:
            return False


def counter(listik, counttt):
    """Функция подсчета набранных баллов.
    Обращается к списку и подсчитывает кол-во плюсиков,
    добавленных функцией check_answer()."""
    for i in listik:
        if i == '+':
            counttt += 1
    print(f'Количество баллов: {counttt}.')


def questions_and_answers():
    """Функция, выполняющая полный цикл процедур 'вопрос' - 'ответ'.
    Когда вопросы заканчиваются, выводит завершительное сообщение."""
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


def main():
    """Основная функция, объединяющая работу предыдущих."""
    hello()
    time.sleep(TIMEOUT)
    questions_and_answers()
    counter(lst_count, countt)


main()
