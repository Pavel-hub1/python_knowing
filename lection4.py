'''
Задача 1.
# Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат запишите в исходный файл (minn maxx)

from pathlib import Path
file_path = Path('lect4.txt')

with open(file_path, 'r') as f_data:
    line_ = f_data.read().split(' ')

for i in range(len(line_)):
    line_[i] = int(line_[i])

minmax_line = [min(line_), max(line_)]

with open(file_path, 'a') as f_new:    # запись в файл
    f_new.writelines(f'\n{minmax_line}')

with open(file_path, 'r') as f_news:    # чтение файла
    print(f_news.read())
'''


'''
# Задача 2.
# Найдите корни квадратного уравнения Ax^2 + Bx + C = 0 двумя способами:
# 1)с помощью математических формул
# 2) с помощью доп библиотеки scipy


a = 9
b = -11
c = 3
discr = b*b - 4*a+c

if discr == 0:
    my_tuple = (-b / (2 * a), )
elif discr > 0:
    my_tuple = ((-b + discr ** 0.5) / (2 * a), (-b - discr ** 0.5) / (2 * a))
else:
    my_tuple = ("Нет корней", )

print(my_tuple)
'''



# Задача 3.



