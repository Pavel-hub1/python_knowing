# # Ввод & вывод
# print('Введите a');     # Просим ввести а
# a = input()   # Вводи руками а
# print('Введите b');
# b = input()
# print(a, b)    # Выводим а и b
# print('{} - {}'.format(a, b))
# print(f'{a} - {b}')


# # Уравнение
# print('Введите a');     # Просим ввести а
# a = int(input())   # Вводи руками а
# print('Введите b');
# b = int(input())
# print(a, ' + ', b, ' = ', a+b)    # Выводим сумму а и b


# # Операции
# # +, -, *, /, %, //, **
# c = a // b  # Деление в целых числах
# с = a % b   # Узнать остаток от деления
# c = a ** b  # Возведение в степень
# c = round(a * b, 5)     # Округление до 5 знаков после запятой


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or
# is, is not, in, not in
#     ## Задача 1.
# f = [1,2,3,4]
# print(f)
# print(2 in f)   # Проверка, есть ли 2 в ф-ции f

#       ## Задача 2.
# f = [1,2,3,4]
# is_odd = not f[0] % 2   # Проверяем, делится ли эл-т с индексом 0 в ф-ции f на 2 без остатка
# print(is_odd)


# Управление конструкциями
# if, if-else
#     ## Задача 1.
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

#     ## Задача 2.
# username = input('Введите имя: ')
# if username == 'Maша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)


# while  и  for
#     ## Задача 1. Число-перевертыш
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

#     ## Задача 2.
# for i in 1,2,3,4,5:
#     print(i**2)

#     ## Задача 2.1.
# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

#     ## Задача 2.2.
# for i in range(5):    # Список от 0 до 4 (из 5 эл-тов)
#     print(i)

# # Строки
# text = 'ааааа еще аааааа ааааааааа аааааа'
# print(len(text))                    # 33
# print('еще' in text)                # True (проверка наличия строки 'еще' в тексте)
# print(text.isdigit())               # False (являются ли все строки в строке числами)
# print(text.islower())               # True (являются ли все строки в строке нижнего регистра)
# print(text.replace('еще', 'ЕЩЕ'))   # Замена 'еще' на 'ЕЩЕ'

# colors = ['red', 'green', 'blue']
# colors.append('gray')   # Добавить в конец списка
# colors.remove('red')    # Удалить эт-т либо del colors[0]

# [].pop(i)             # Удалить эл-т из списка с индексом i

# Функции!!
#     ## Задача 1.
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2
# print(f(arg))           # Возвращает ф-цию f от arg
# print(type(f(arg)))     # Возвращает тип данных arg


# # Тернарный оператор
# a = 50 if True else 70      # если условие True, то а = 50, если нет , то а = 70


# # Срезы в списках
# a = [42, 67, 89, 103, 76]
# a[1:3] -> [67, 89]      # Выводит срез из списка с 1 по 3 индекс, НЕ ВКЛЮЧАЯ 3
# a[2:] -> [89, 103, 76]  # Выводим срез из списка со 2 до конца списка
# a[::2] -> [42, 89, 76]  # Выводит весь список с шагом в два (пропускает каждое второе число)

'''
Пример. Слово наоборот
s = str(input('введите слово: '))
s[::-1]
print(s[::-1])
'''

'''
# Привет из practice3.py с пояснениями.
# Реализуйте алгоритм перемешивания списка.
import random
list_origin = [random.randint(0,10) for i in range(random.randint(5,20))]
print(list_origin)

def new_list(list_origin):
    # Создаем копию, поскольку мы не должны изменять оригинал
    list = list_origin[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        index_ = random.randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_]
        list[index_] = temp
    # Возвращаем список
    return list
print(new_list(list_origin))
'''


# # Метод разбиения строки дополнительно через .split('')
# string = input('Введите дробное число ').split(',')[1][0]   #(разбили строку на до символа ',' и на после. В начала указан
# print(string)                                               # индекс [1], следовательно правая часть после запятой. А потом
#                                                             # индекс [0], следовательно первый индекс этой части.)


# # Файлы
# # Пример 1. Запись данных в файл.
# colors = ['red', 'green', 'blue']   # набор данных - список
# data = open('file.txt', 'a')        # текстовая переменная дата, связаннная с текстовым файлом
# # data.writelines(colors)             # функционал позволяющий записать некоторые данных (разделителей не будет)
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()

# # Пример 2. Запись данных в файл.
# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')

# # Пример 3. Чтение данных в файле.
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:       # цикл для чтения всех строк файла
#     print(line)         # автоматически делает переход на другую строку
# data.close()
# exit()          # Не дает выполняться коду после этой строки

# # Пример 4. Сделать импорт функции из файла
# import practice1 as p   # заменили название на p, чтобы в будущем использовать псевдоним
# print(p.f(1))

'''
# Вариант 1.
f = open('test.txt', 'r')
# 'r' - чтение
# 'w' - перезапись (если файла нет, его создадут)
# 'a' - дозапись
# 'r+' - чтение + запись

# Вариант 2. (открыть и закрыть его)
# file_path = r'file.txt'     # записали имя файла в отдельную переменную, добавили 'r' , чтобы получилось сырая переменная
with open('test.txt', 'r') as f_data:
    print(f_data.read())

# Вариант 3. (для автоматического проставления разделители)
from pathlib import Path

file_path = Path('data', 'test.txt')    # в папке 'data' лежит файл 'test.txt'
with open(file_path, 'r') as f_data:
    print(f_data.read())
'''

# # Функции
#     # Пример 1.
# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # TypeError missing 1 required ...

#     # Пример 2.
# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # !!!
# print(new_string(4))      # 12

#     # Пример 3.
# def concatenatio(*params):
#     res: str = ""           # res - переменная, str - тип данных
#     for item in params:
#         res += item         # склеивание строк
#     return res
# print(concatenatio('a', 's', 'd', 'w'))     # asdw
# print(concatenatio('a', '1'))     # a1

#     # Пример 4. Вычисление числа Фибоначчи
# def fib(n):
#     if n in [1, 2]:     # если n принадлежит [1, 2], то return 1
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)     # 1 1 2 3 5 8 13 21 34

#     # Пример 5. Другой вид ф-ции 1 -> 2
# # 1.
# def f(x, y):
#     return x*y
# print(f(5, 3))
# # 2.
# a = lambda x, y: x*y
# print(a(5, 3))


# # Кортежи
#     # Пример 1.
# a = (3, 1, 41, 4)
# print(a)        # (3, 1, 41, 4)
# print(a[-2])    # 41
# print(a[-1])    # 4  (Последний эл-т)

#     # Пример 2.
# a = (3, 1, 41, 4)
# for item in a:      # Пробежать и вывести все значения кортежа
#     print(item)


# # Словари
#     # Пример 1.
# # dictionary = {}     # доп. вариант вывода
# # \ - для того, чтобы можно было описывать все с новой строки!! (а не в одну строчку)
# dictionary = \
#     {
#         'up': 'вверх',       # up - ключ, вверх - значение
#         'left': 'влево',
#         'down': 'вниз',
#         'right': 'вправо'
#     }
# print(dictionary)           # {'up': 'вверх', 'left': 'влево', 'down': 'вниз', 'right': 'вправо'}
# print(dictionary['left'])   # влево
# # типы ключей могут отличаться

#     # Пример 2.
# dictionary = \
#     {
#         'up': 'вверх',       # up - ключ, вверх - значение
#         'left': 'влево',
#         'down': 'вниз',
#         'right': 'вправо'
#     }
# for k in dictionary.keys():      # Вывод ключей с помощью цикла, values() - для конкретных значений
#     print(k)

#     # Пример 3. get
# my_dict.get('key_100', '?')  # если нет ключа_100, то он выдаст '?'

#     # Пример 4. Добавить новое значение в словарь
# my_dict['key_5'] = 76


# # Множества
# set:
# - ток уникальные значения содержит
# - не индексируются эл-ты
# -
#     # Пример 1. Базовые операции
# colors = {'red', 'green', 'blue'}
# print(colors)   # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)   # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)   # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors)   # {'green', 'blue', 'gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red')   # ok
# print(colors)   # {'green', 'blue', 'gray'}
# colors.clear()      # { }
# print(colors)   # set()

#     # Пример 2. Операции со множествами. БЕЗ ВЫВОДА.
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                # c = {1, 2, 3, 5, 8}
# u = a.union(b)              # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)       # i = {8, 2, 5}
# dl = a.difference(b)        # dl = {1, 3}
# dr = b.difference(a)        # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s = frozenset(a)     # неизменяемые множества


# # Списки
#     # Пример 1. Удаление последнего эл-та
# list1 = [1,2,3,4,5]
# print(len(list1))
# print(list1.pop())  # удаляем последний эл-т списка
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

#     # Пример 2. Удаление определенного эл-та
# list1 = [1,2,3,4,5]
# print(list1.pop(2))     # Удаление эл-та с индексом 2
# print(list1)

#     # Пример 3. Вставить определенный эл-т на определенную позицию
# list1 = [1,2,3,4,5]
# print(list1.insert(4, 11))     # Вставка элемента 11 на место перед эл-том с индексом 2
# print(list1)


'''
# Моржовый оператор (:=)
while k:=int(input('--> ')) <= 0:   # цикл, который будет отрабатывать, пока не выполнится результат.
    pass        # или print('ERROR')
'''


#     # включения, filter, map
# # Пример 1. map
# numbs = ['20', '50', '15']
# res = list(map(int, numbs))     # преобразуем с помощью map все значения в int и представляем их в виду списка
# print(res)

# # Пример 2. filter
# numbs = ['20', '50', '15']
# res = tuple(filter(lambda x: int(x) > 19, numbs))   # фильтруем эл-ты из numbs по ф-ции lambda, такой что Int(x) > 19. И создаем кортеж.
# print(res)

