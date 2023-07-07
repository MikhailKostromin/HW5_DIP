""" 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def input_str(tmp):
    file_extension = a.split('.')[1]
    file_name = (a.split('/')[-1]).split('.')[0]
    path_file = (a.split('.')[0]).split(file_name)[0]
    return file_extension, file_name, path_file


a = input("Введите путь до файла:  ")
# /home/user_viki/foo/bar.txt

print(input_str(a))
