import random
import time
import string
import sys

from additional import dictionary, correct_answers
from trashbox import add_string, wrong, right, CONST

TIMEOUT = 0  # константа для задержки инструкции пользователя
PAUSE = 0  # константа для задержки вопроса после ответа
ALPHABET = 'йцукенгшщзхъфывапролджэячсмитьбюё'
complex = (
    ALPHABET + string.punctuation
    + string.whitespace + string.digits
)  # комплексная строка невозможных символов ввода
lst_count = []  # лист для плюсиков (правильных ответов)
countt = 0  # переменная для подсчета правильных ответов


def hello():
    """Приветственная функция,
    которая предлагает участнику запустить викторину"""
    print('Привет, это викторина. Играем?')
    while True:  # цикл While, чтобы ввод не прерывался в случае ошибки.
        agree = input('Да / Нет \n')
        if agree == 'Да' or agree == 'Нет':
            break  # если ввод корректный, останавливаем цикл
        else:
            print('Неверный ввод, попробуйте еще раз. \n')
            # если ввод некорректный, то ввод обнулится
    if agree == 'Да':
        print(add_string)
    elif agree == 'Нет':
        # если пользователь играть не хочет, то увы, выходим.
        print(':(')
        sys.exit()


def check_answer(response):
    """Функция, проверяющая правильность ответа.
    Если ответ верный, в словарь добавляется плюсик."""
    for key, value in correct_answers.items():
        if response.lower() in value:
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
    добавленных функцией check_answer().
    Печатает количество набранных пользователем баллов."""
    for i in listik:
        if i == '+':
            counttt += 1
    print(f'Количество баллов: {counttt}.')


def questions_and_answers():
    """Функция, выполняющая полный цикл процедур 'вопрос' - 'ответ'.
    Когда вопросы заканчиваются, выводит завершительное сообщение."""
    while True:
        with open('result.txt', 'a', encoding='utf-8') as f:
            for key, value in dictionary.items():
                print(key)
                f.write(f'Вопрос: {key} \n')
                print(f'Возможные ответы: {value} \n')
                f.write(value)
                dictionary.pop(key)
                break
            while True:
                answer = input('Введите ответ: \n')
                if check_input(answer):
                    print(
                        'Неверный формат ввода! \n'
                        'Введите ответ на латинице '
                        'без символов, цифр и пробелов. \n'
                    )
                    time.sleep(PAUSE)
                else:
                    f.write(f'Ответ пользователя: {answer} \n\n')
                    break
            print(check_answer(answer))
            time.sleep(PAUSE)
            print(f'{"-" * CONST}\n')
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
