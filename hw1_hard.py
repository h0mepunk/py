
__author__ = 'Проскурина Мария Дмитриевна'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

a = bool('99999999')
print(a == a**2)
print(a == a*2)
print(a > 999999)
# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)