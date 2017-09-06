# Задание 1.
# Реализуем один из известных паттернов проектирования. Этим паттерном будет Компоновщик.
# Cоздайте текстовое отображение папок и вложенных файлов в содержащихся каталоге.
class BaseNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass

class File(BaseNode):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return 'file: "{}"'.format(self.name)

class Dir(BaseNode):
    def __init__(self, name):
        super().__init__(name)
        self.listOfDir = []

    def __repr__(self):
        if len(self.listOfDir) == 0:
            return 'directory: {} (empty)'.format(self.name)
        else:
            return 'directory: {} ({})'.format(self.name, ', '.join(list(map(repr, self.listOfDir))))

    def add(self, n):
        self.listOfDir.append(n)

    def remove(self, n):
        self.listOfDir.remove(n)


# Задаине 2.
# Напишите реализацию класса WrapStrToFIle, по следующему шаблону.
# class WrapStrToFile:
#     def __init__(self):
#         # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
#     @property
#     def content(self):
#         # попытка чтения из файла, в случае успеха возвращаем содержимое
#         # в случае неудачи возращаем 'Файл еще не существует'
#     @content.setter
#     def content(self, value):
#         # попытка записи в файл указанное содержимого
#     @content.deleter
#     def content(self):
#         # удаляем файл

import tempfile, os

class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            temp_file = open(self.filepath)
            buf = temp_file.read()
            temp_file.close()
            return buf
        except IOError:
            return ('Файл не существует!')

    @content.setter
    def content(self, value):
        try:
            temp_file = open(self.filepath, 'w')
            temp_file.write(value)
            temp_file.close()
        except IOError:
            print('Error!')

    @content.deleter
    def content(self):
        try:
            os.unlink(self.filepath)
        except Exception:
            print('Error!')
