'''
# Задача 1.
# Реализуйте алгоритм задания случайных чисел без использования генератора псевдослучайных чисел. (time)

from datetime import datetime
def get_random_number(n):
    new = datetime.now()
    random_number = new.time().second * new.time().minute * new.time().microsecond // new.time().minute
    return random_number % 10**n

print(get_random_number(2))
'''

'''
# Задача 2. Присутствует ли в данном списке некое число.

def func():
    list_ = ['21314414', 'fghb3fh', 'gh', '12334578']
    k = int(input('Введите число: '))
    new_list = []
    for i in range(len(list_)):
        if str(k) in list_[i]:
            new_list.append(list_[i])
    return new_list

print(func())
'''


'''
# Задача 3.
# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.
# Пример: 
# -список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# -список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5 
# -список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# -список: ["123", "234", 123, "567"], ищем: "123", ответ: -1 (isinstance())
# -список: [], ищем: "123", ответ: -1

def func(): !!!! дописать !!!!
    list_ = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    k = str(input('Введите строку: '))
    n = 0

    for i in range(len(list_)):
        if k in list_[i]:
            if n == 2:

                break
            else:
                n += 1
    return i
print(func())
'''



    # list_ = ['21314414', 'fghb3fh', 'gh', '12334578']
    # k = int(input('Введите число: '))
    # new_list = []
    # for i in range(len(list_)):
    #     if str(k) in list_[i]:
    #         new_list.append(list_[i])
    # return new_list