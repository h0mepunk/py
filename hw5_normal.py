# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
import hw5_easy
import os
import sys

#print('sys.argv =', sys.argv)


def print_help():
    print("help - получение справки")
    print("cr_dir - создание директории")
    print("rm_dir - удаление директории")
    print("change_dir - сменить директорию")
    print("open_dir - посмотреть содержимое директории")


def open_dir():
    cur_path = hw5_easy.show_dir()
    current_dir = os.listdir(cur_path)
    print(current_dir)


def change_dir():
    print("Введите абсолютный путь до директории, которую хотите открыть")
    ch_dir_name = input("Путь до директории: ")
    try:
        os.chdir(ch_dir_name)
        print("Успешно")
    except OSError:
        print("Возникла ошибка")


def create_dir():
    dir_name_ = input("Путь до директории: ")
    hw5_easy.create_dir(dir_name_)
#    print("{} Успешно создана".format(dir_name_))


def remove_dir():
    dir_name_ = input("Путь до директории: ")
    hw5_easy.remove_dir(dir_name_)
#    print("{} Успешно удалена".format(dir_name_))


do = {
    "help": print_help,
    "cr_dir": create_dir,
    "rm_dir": remove_dir,
    "change_dir": change_dir,
    "open_dir": open_dir
}

print_help()
key = input("введите ключ")

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ. Введите help для получения справки")

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
