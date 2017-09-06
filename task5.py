# Задание 1.
# Библиотека itertools, реализовать следующие функции:
#   Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])
#   Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращать массив
#     из элементов, у которых длина не меньше пяти (['hello', 'world'])
#   Функция выдает на строку 'password' все возможные комбинации вида ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'), ('p', 'a', 's', 'o'), ...)

import itertools
list(itertools.chain([1, 2], [3, 4], [5, 6]))
list(itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code']))
list(itertools.combinations('password', 4))

# Задание 2.
# Написать консольную утилиту, используя argparse. Она должна принимать позиционный аргумент dirpath - это будет директория,
# внутри которой утилита создаст новую папку. Название новой папки будет зависеть от указанных опций. Если указана опция -y,
# то в назнании присуствует текущий год. Если -m, то номер текущего месяца. Если -d, то номер текущего дня.
# Опции можно комбинировать. Если папка с заданным названием уже существует, то нужно просто выводить предупреждение об этом
# и больше ничего не делать. Если не указано ни одной опции, то утилита должна создать папку с именем 'unknown'.

import argparse, os, itertools
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to folder")
parser.add_argument("-y", "--year", action="store_true", help="year")
parser.add_argument("-m", "--month", action="store_true", help="month")
parser.add_argument("-d", "--day", action="store_true", help="day")
args = parser.parse_args()
buf = "-".join(map(str, list(itertools.compress([datetime.now().year, datetime.now().month, datetime.now().day],
                                                 [args.year, args.month, args.day]))))

name = buf if buf != "" else 'unknown'
if not os.path.exists('{}\\{}'.format(args.path, name)):
    os.mkdir('{}\\{}'.format(args.path, name))
    print("Папка создана!")
else:
    print("Папка уже существует!")
