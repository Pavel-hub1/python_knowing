'''
# Задача. Список находится в другом файле, создание нового списка из индекса переменной и квадрата этой переменной
f = open(file, 'r')
data = f.read() + ' '                       # Считываю все строчки и искусственно добавляю туда пробел
f.close()

numbers = []

while data != '':                           # пробегаюсь по всей строку, накладываю условие, пока моя строка не пустая
    space_pos = data.index(' ')             # нахожу первую позицию пробела 
    numbers.append(int(data[:space_pos]))   # беру все, что находится слева до первого пробела, превращаю в int и добавляю в список
    data = data[space_pos+1:]               # обновляем строку, все что мы ток что использовали, нам не нужно

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)
'''


'''
# Задача 1.
# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Вариант 1.
from pathlib import Path
file_path = Path('txt', 'lect5.txt')

with open(file_path, 'r') as f_news:    
    line_ = f_news.read().split(' ')

numbers = []
for i in range(len(line_)):
    line_[i] = int(line_[i])
    if line_[i]-1 != 0 and line_[i] - 1 != line_[i-1]:
        numbers.append((line_[i] - 1))
print(line_)
print(numbers)

# Вариант 2.
string_ = '1 2 3 4 5 6 8 9'
li = set(map(int, string_.split()))
li_1 = set(i for i in range(1, len(li)+1))
dif li_1-li
print(int(dif))
'''


'''
# Задача 2.
# Дан список числе. Создайте список, в который попадают числа, описываемые возрастающую послед-ть. Порядок эл-тов менять нельзя.
# [1, 5, 2, 3, 4, 6, 2, 7] => [1, 5, 6, 7] и т.д.

list_ = [1, 1, 2, 1, 0, 5, 2, 3, 4, 6, 2, 7]
list_new = []
number_max = 0
for i in range(len(list_)):
    if list_[i] > list_[i-1] or list_[i] > 0:
        if list_[i] > number_max:
            number_max = list_[i]
            list_new.append(list_[i])
print(list_new)
'''



'''
# Задача 3.
# Напишите программу, удаляющую из текста все слова,содержащие "абв".
# --> 'Я люблю абвЖаву иабв Питон'
# --> 'Я люблю Питон'

str_ = 'Я люблю абвЖаву иабв Питон'
remote_str = 'абв'

str_new = str_.split()
final_list = list(filter(lambda el: not remote_str in el, str_new))
final_string = ' '.join(final_list)

print(str_new)
print(final_string)
'''

'''
# Задача. Вывод КАК БУДТО матрица
a = [
    [1, 2, 3],
    [4, 5, 6]
]
for i in a:
    print(i)
'''