# Все задачи текущего блока решите с помощью генераторов списков!
import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
list_ = [random.randint(-30, 30) for _ in range(15)]
res_list = []
print(list_)
for _ in list_[:]:
	res_list.append(_ * _)
print(res_list)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
_ = 0
list_1 = []
list_2 = []
fruits = ["яблоко", "банан", "груша", "манго", "ананас", "маракуйя", "виноград", "персик", "абрикос", "мандарин", "слива", "кизил", "арбуз",]
list_1 = [fruits[random.randint(0, len(fruits) - 1)] for _ in range(4)]
list_2 = [fruits[random.randint(0, len(fruits) - 1)] for _ in range(4)]
print(list_1)
print(list_2)
res_list_1 = list(set(list_1) & set(list_2))
print(res_list_1)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
num_list = [random.randint(-30, 30) for _ in range(15)]
_ = 0
list_3 = [_ for _ in num_list if (_ % 3 == 0)]
_ = 0
list_4 = [_ for _ in num_list if (_ >= 0)]
_ = 0
list_5 = [_ for _ in num_list if (_ % 4 != 0)]
print(num_list)
print(list_3)
print(list_4)
print(list_5)
