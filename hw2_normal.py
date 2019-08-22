# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое','одиннадцатое','двенадцатое', 'тринадцатое', 'четырнадцаптое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое','девятнадцатое','двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадцать четвертое', 'двадцать пятое','двадцать шестое','двадцапть седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']
month = ['января', 'первое', 'первое', 'первое', 'первое', 'первое', 'первое', 'первое', 'первое', 'первое','первое','первое',]
incoming_date = input(incoming_date.split('.'))
print(incoming_date)
print('{} {} {}'.format(date[incoming_date[0]], date[incoming_date[1]], incoming_date[2] + 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]