# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math

def fibonacci(n, m):
    def f_n(p):
        res = ((((1 + math.sqrt(5)) / 2) ** p) * ((((1 - math.sqrt(5)) / 2) ** p)/math.sqrt(5)))
        return res


#   где-то ошиблась, не могу понять, где
    a = []
    for i in range(n, m):
        a.append(f_n(i))
        i += 1
    return(a)

print(fibonacci(3, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = len(origin_list)
    a = origin_list
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return(a)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def f(q):
    return(q ** 2)


def filter_1(f, iterator_1):
    res = []
    for i in range(len(iterator_1)):
        if f(iterator_1[i]):
            res.append(iterator_1[i])
            i+=1
        else:
            i+=1
    return(res)

print(filter_1(f, [0, 2, 4, 2, 9, 10]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def prllgrmm(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x3 - x2 == x4 - x1) and (y2 == y3) and (y1 == y4):
        return(True)
    else:
        return(False)

print(prllgrmm(0, 0, 2, 4, 8, 4, 6, 0)) # является
print(prllgrmm(0, 0, 2, 4, 8, 4, 6, 1)) # не является