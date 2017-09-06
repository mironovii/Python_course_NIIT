import random
import time

# Задание 1
# Функция fio, которая принимает одну строку, состоящую из ФИО (например, "Ladoshkin Nikita Evgenievich") и возвращает
# словарь с ключами name, surname, patronymic (пример, {'name': 'Nikita', 'surname': 'Ladoshkin', 'patronymic': 'Evgenievich'})
def fio(a):
    buf = a.split()
    names = {'name': buf[0], 'surname': buf[1], 'patronymic': buf[2]}
    return names

# Задание 2
# Функция sort_str, которая принимает массив строк (['aaa', 'c', 'qq'])
# и возвращает массив этих строк, отсортированных по длине (['c', 'qq', 'aaa'])
def sort_str(a: list):
    a.sort(key=len)
    print(a)

# Задание 3
# Упрощенная собственная реализация simple_range, которая примимает два числа (1, 5),
# а возвращает массив от первого числа включительно до второго невключительно ([1, 2, 3, 4])
def simple_range(a, b):
    return [i for i in range(a, b)]

# Задание 4
# Функция use_rand без параметров, которая получает результат ф-ии randint библиотеки random c аргументами 1 и 50,
# до тех пор, пока не получите число 42, затем вернете этот результат
def use_rand():
    while 1:
        if random.randint(1, 50) == 42:
            print(42)
            break

# Доп.задания на лекции
# ---------------------
# Создать функцию unic_abs, которая будет принимать любое количество чисел, а вернет массив их модулей
# без повторений (args, abs, set)
def unic_abs(*args):
    buf = set()
    for i in args:
        buf.add(abs(i))
    return buf

# Использовать библиотеку random c методом randint, создать массив из 100 чисел (разброс от -100 до 100),
# прокинуть в unic_abs, вывести
s=[]
for i in range(0, 100):
    s.append(random.randint(-100, 101))


# Создать функцию create_randlist, которая будет создавать этот массив одной строкой
# (lambda, list comprehension, range)
create_randlist = lambda: [random.randint(-100,101) for i in range(0, 10)]

# Создать функцию check_abs, которая будет проверять циклом каждый элемент массива на положительность
def check_abs (u):
    if u > 0:
        return True
    else:
        return False

# Создать эту функцию в одну строчку (lambda, all)
check_abs_l = lambda i: True if i > 0 else False


# Написать декоратор timeit, который с помощью библиотеки time, метода time выдает время исполнения
def timeit(x):
    def wrap(n):
        print("Start: " + time.asctime())
        x(n)
        print("End: " + time.asctime())
    return wrap

# Cоздать функцию run_all, которая массив от create_randlist закинет в unic_abs, а результат в check_abs,
# обернуть это timeit, записать в файл, запустить через консоль
@timeit
def run_all (n):
    print("Исходный массив:")
    print(list(n))
    print("Массив уникальных модулей:")
    print(unic_abs(*n))
    print("Проверка на положительность исходного массива: ")
    print([check_abs_l(n[o]) for o in range(0, len(n))])

run_all(create_randlist())


