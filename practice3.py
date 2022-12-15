'''
# Задача 1.
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах

list = [1, 2, 3, 4, 5, 10, 12]
sum_ = 0
for i in range(1, len(list) + 1):
    if i % 2 == 0:
        sum_ += list[i-1]
print(sum_)
'''

'''
# Задача 2.
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [1, 5, 8, 3, 7, 9]
numbers = []
for i in range(0, len(list)//2):
    if i == 0:
        ab = list[i] * list[-1]
        numbers.append(ab)
    else:
        ab = list[i] * list[-(i+1)]
        numbers.append(ab)
print(list)
print(numbers)
'''


'''
# Задача 3.
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

list_ = [1.23, 1.01, 2.32, 0.64]
numbers = []
for i in range(len(list_)):
    numbers.append(round((list_[i]%1), 2))

def diff(numbers):
    y = max(numbers) - min(numbers)
    return y

print(list_)
print(numbers)
print(diff(numbers))
'''

'''
# Задача 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

str_ = ''
n = int(input('введите число: '))
while n != 0:
    str_ = str(n % 2) + str_
    n //= 2
print(str_)
'''

'''
# Задача 5.
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
def fib(n):
    numbers = []
    x = 1
    y = 1
    for i in range(n-1):
        numbers.append(x)
        x, y = y, x + y
    x = 0
    y = 1
    for i in range(n):
        numbers.insert(0, x)
        x, y = y, x - y
    return numbers
print(fib(n))
'''

