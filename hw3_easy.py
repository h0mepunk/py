# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    res = str(number)[:ndigits + 2]
    return (res)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    tn = str(ticket_number) # иначе слишком длинно писать
    if (int(tn[0]) + int(tn[1]) + int(tn[2]) == int(tn[3]) + int(tn[4]) + int(tn[5])):
        return(True)
    else:
        return(False)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
