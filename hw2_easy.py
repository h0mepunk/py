# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
list_0 = ["яблоко", "банан", "киви", "арбуз"]
n = len(max(list_0))
for i in range(len(list_0)-1):
	print('{} {:>6}'.format(i + 1, list_0[i]))
# не знаю, как подставить n в format, но думаю, что как-то можно

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_1 = [1, 2, 4, 6, 8, 1, 2]
list_2 = [1, 9, 0, 3, 4, 5, 1, 2]

res = set(list_2).difference(set(list_1))
print(list(res))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_3 = [1, 4, 7, 9, 11, 4, 6, 9, 2, 35, 101, 1, 6]
res_list = []
i = 0
for i in range(len(list_3) - 1):
    if list_3[i] % 2 == 0:
        res_list.append(list_3[i] / 4)
        i += 1
    else:
        res_list.append(list_3[i] * 2)
        i += 1
print(res_list)