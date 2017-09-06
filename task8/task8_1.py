# Задание 8_1
# Напишите функцию odd_primes(end, start), которая ищет все простые числа в диапазоне от
# заданного числа start (по умолчанию 3) до заданного числа end. Запустите ее:
# Три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Также запустите ее три раза с теми же аргументами, но каждую в отдельной потоке с помощью
# threading.Thread. Забудьте стартануть треды и дождаться их окончания.
# Также запустите ее три раза с теми же аргументами, но каждую в отдельной потоке с помощью
# multiprocessing.Process. Забудьте стартануть процессы и дождаться их окончания.

import threading
from datetime import datetime
from multiprocessing import Process


def odd_primes(end, start=3):
    if (type(end) is int and end > 0) and (type(start) is int and start > 0):
        result = []
        for i in range(start, end + 1):
            if all(i % j for j in range(2, int(i ** 0.5) + 1)):
                result.append(i)
        return result
    else:
        raise ValueError


if __name__ == '__main__':

    # First test in single thread
    start = datetime.now()
    odd_primes(300000)
    odd_primes(600000, 300001)
    odd_primes(900000, 600001)
    print("Total time in single thread:\t\t {} sec.".format((datetime.now() - start).total_seconds()))

    # Second test in 3 parallel thread
    start = datetime.now()
    init_data = [(300000, 3), (600000, 300001), (900000, 600001)]
    threads = []
    for i in range(3):
        thr = threading.Thread(target=odd_primes, args=(init_data[i][0], init_data[i][1]))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()
    print("Total time in 3 parallel thread:\t {} sec.".format((datetime.now() - start).total_seconds()))

    # Third test in 3 parallel Process
    start = datetime.now()
    init_data = [(300000, 3), (600000, 300001), (900000, 600001)]
    my_procs = []
    for i in range(3):
        proc = Process(target=odd_primes, args=(init_data[i][0], init_data[i][1]))
        proc.start()
        my_procs.append(proc)

    for proc in my_procs:
        proc.join()
    print("Total time in 3 parallel process:\t {} sec.".format((datetime.now() - start).total_seconds()))

# Вывод: вычисления математических операций выполняется быстрее в разных процесссах.
# Время выполнения в одном потоке и несколиких не отличается.