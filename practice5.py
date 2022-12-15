'''
# Задача 1.
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


# Задача 2.
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""




'''
# Задача 3. 
# Создайте программу для игры в ""Крестики-нолики"".

a = [1,2,3,
    4,5,6,
    7,8,9]

win_comb = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[2,4,6],[3,4,5],[6,7,8]]

def printa():
    print(a[0], a[1], a[2])
    print(a[3], a[4], a[5])
    print(a[6], a[7], a[8])
  
def move_(move, el):
    indexx = a.index(move)
    a[indexx] = el
 
def res():
    element = ""
    for i in win_comb:
        if a[i[0]] == "X" and a[i[1]] == "X" and a[i[2]] == "X":
            element = "X"
        if a[i[0]] == "O" and a[i[1]] == "O" and a[i[2]] == "O":
            element = "O"   
    return element

winner = False
player1 = True

while winner == False:
    printa()
    if player1 == True:
        el = "X"
        move = int(input("Ход Х: "))
    else:
        el = "O"
        move = int(input("Ход О: "))
 
    move_(move,el)
    element = res()
    if element != "":
        winner = True
    else:
        winner = False
 
    player1 = not(player1)
  
printa()
print(f'Победил {element}')
'''
'''
# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: qqqqwwwee -> 4q3w2e  &  4q3w2e -> qqqqwwwee

# Сжатие
def compression(n):
    str_ = ''
    i = 0
    while i < len(n):
        numb = 1
        while i + 1 < len(n) and n[i] == n[i+1]:
            numb += 1
            i  += 1
        if numb != 1:
            str_ += str(numb) + n[i]
            i += 1
        else:
            str_ += n[i]
            i += 1
    return str_
print(compression(n='qqqqwwweerrrreeer'))
'''

# Восстановление
def decompression(n):
    str_ = ''
    i = 0
    while i < len(n):
        numb = 0
        while int(n[i]) != int and i + 1 < len(n):
            numb = n[i-1]
            i += 1
        str_ += n[i]*int(numb)
        i += 1
    return str_
print(decompression(n='4q3w2e4r3er'))


