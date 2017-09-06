# Задание 7_1
# Напишите программу, которая уничтожает файлы и папки по истечении заданного времени.
# Вы указываете при запуске программы путь до директории, за которой нашему скрипту необходимо следить.
# После запуска программа не должна прекращать работать, пока вы не остановите ее работу с помощью Ctrl+C 
# Программа следит за объектами внутри указанной при запуске папки и удаляет их тогда,
# когда время их существования становится больше одной минуты для файлов и больше двух минуты для папок.
# Ваш скрипт должен смотреть вглубь указанной папки.
 
import os, shutil, argparse, time

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to folder")
my_path = parser.parse_args().path

if not os.path.isdir(my_path):
    print("Folder does not exist!")
    exit(1)

def fun1(path):
    for i in os.listdir(path):
        buf_path = os.path.join(path, i)
        if os.path.isdir(buf_path):
               shutil.rmtree(buf_path) if time.time() - os.path.getctime(buf_path) >= 120 else fun1(buf_path)
        else:
            if time.time() - os.path.getctime(buf_path) >= 60:
                os.remove(buf_path)

while True:
    try:
        fun1(my_path)
    except Exception as e:
        print(e)
