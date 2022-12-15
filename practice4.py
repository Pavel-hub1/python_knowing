'''
# Задание 1. Вычислите число с заданной точностью.

import math
def func():
    pi = math.pi
    k = input('Введите десятичное число ').split('.')[1]
    x = str(round(math.pi, len(k)))
    return x

print(func())
'''


'''
# Задание 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def func():
   k = int(input('Введите число: '))
   i = 2
   func = []
   while i * i <= k:
       while k % i == 0:
           func.append(i)
           k = k / i
       i = i + 1
   if k > 1:
       func.append(int(k))
   return func
print(func())
'''


'''
# Задание 3. 
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# Примечание:
def func():
    list_ = list(input('Введите список: '))
    new_list = []
    for i in range(len(list_)):
        for j in range(len(list_)):
            if i != j and list_[i] == list_[j]:
                break
        else:
            new_list.append(list_[i])
    return new_list        
print(func())
'''


'''
# Задача 4.
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

def polynom(*args, pow_sign: str = '^') -> str:
    if not args:
        return ""
    first_not_null_index = 0
    for index, arg in enumerate(args):
        if arg:
            first_not_null_index = index
            break
    coeffs = args[first_not_null_index:]
    res_items = []
    length = len(coeffs)
    pow = length - 1
    for index, coeff in enumerate(coeffs):
        if index == 0:
            sing = "" if coeff > 0 else "-"
        else:
            sing = "+" if coeff > 0 else "-"
        coeff = abs(coeff)
        x = "x" if index < length - 1 else ""
        str_pow = f"{pow_sign}{pow}" if pow > 1 else ""
        if not coeff:
            curr_val = ""
        elif coeff == 1 and index < length - 1:
            curr_val = f"{sing}{x}{str_pow}"
        else:
            curr_val = f"{sing}{coeff}{x}{str_pow}"
        res_items.append(curr_val)
        pow -= 1
    return "".join(res_items)

from random import randint
from pathlib import Path
file_path = Path('practice4_2.txt')

for _ in range(1):
    test_coeffs = [randint(-10, 10) for x in range(randint(0, 15))]
    # print(polynom(*test_coeffs))

with open(file_path, 'a') as f_new:
    f_new.write(f'{polynom(*test_coeffs)} = 0 \n')
'''


# Задача 5.
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

from pathlib import Path
file_path = Path('practice4_2.txt')

with open(file_path, 'a') as f_new:
    f_new.write(f'{polynom(*test_coeffs)} = 0 \n')
