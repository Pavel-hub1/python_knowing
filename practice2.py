'''
# Задание 1.
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input('Введите число: '))

def sum_(n):
    numbers = 0
    for i in str(n):
        if i != '.' and i != '-':
            numbers += int(i)
    return numbers
print(sum_(n))
'''
 

'''
# Задание 2.
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
y = 1
numbers = []
for i in range(1, n+1):
    y *= i
    numbers.append(y)
print(numbers)

# k = '{y}*{i}'
# print('{y}*{i}' * n)
'''


'''
# Задание 3.
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# # Решение 1. Без красивого вывода.
# n = int(input('Введите число: '))
# sum_ = 0
# print('{', end='')
# for i in range(1, n+1):
#     k = i
#     y = round((1 + 1/i)**i, 2)
#     sum_ += y
#     print(i, ':', y, end=', ')
# print('}', end=' ')
# print('Сумма', sum_)


# Решение 2. Почти с идеальным выводом.
# Много лишних переменных пришлось ввести....
n = int(input('Введите число: '))
sum_ = 0
print('{', end='')
for i in range(1, n):
    k = i
    y = round((1 + 1/i)**i, 2)
    sum_ += y
    print(i, ':', y, end=', ')
last_ = round((1 + 1/n)**n, 2)
sum_ += last_
print(n, ':', last_, '}', end=' ')
print('Сумма', sum_)
'''




# Задание 4.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

# def prod(val) :
#     res = 1
#     for ele in val:
#         res *= ele
#     return res 


# n = int(input("Введите число эл-тов: "))
# numbers = []
# for i in range(-n, n + 1):     
#     numbers.append(i)
# print(numbers)

# k = str(input('Введите индексы: '))
# index_list = []
# print (str(index_list))
# res_list = prod([numbers[i] for i in index_list])
# print ("Результрующий список : " + str(res_list))



'''
# Задание 5.
# Реализуйте алгоритм перемешивания списка.

import random
list_origin = [random.randint(0,10) for i in range(random.randint(5,20))]
print(list_origin)

def new_list(list_origin):
    list = list_origin[:]
    list_length = len(list)
    for i in range(list_length):
        index_ = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_]
        list[index_] = temp
    return list
print(new_list(list_origin))
'''