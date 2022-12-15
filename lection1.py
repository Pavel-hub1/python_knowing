# # Проверить, является ли первое число квадратом второго
# a = int(input('a = '))
# b = int(input('b = '))
# if a == b*b:
#     print('Yes')
# elif b == a*a:
#     print('Yes')
# else:
#     print('No')


#     ## Пример 1.
# # Находит максимальное значение из  ЗАДАННОГО списка.
# list = [1,2,9,4,5]
# print(max(list))

#     ## Пример 2.
# # Нахождение максимального значения из ВВОДИМОГО списка. (но ток положительного или равен будет 0)
# num = 0
# maximum = 0
# for _ in range(5):
#     num = int(input("Введите число: "))
#     if num > maximum:
#         maximum = num
# print(maximum)

#     ## Пример 3.
# numbers = []                            # Работа со списком
# for _ in range(5):                      # Ограничиваем список до 5 эл-тов
#     numbers.append(int(input("--> ")))  # Вводим числа по очереди
# max_count = max(numbers)
# print(numbers)
# print(max_count)


# # При вводе числа N выводит числа от -N до N
#       # Вариант 1.
# N = int(input('Введите N = '))
# list_ = list(range(-N, N + 1))
# print(list_)

#     # Вариант 2.
# n = int(input("Введите число "))
# numbers = []
# for i in range(-n, n + 1):       # i принимает значение из range (а не индекс)
#     numbers.append(i)
# print(numbers)


# # Программа, которая принимает дробь на вход и показывает первую цифру дробной части числа
# a = float(input('Введите число '))
# b = (a*10)%10   # -> 7.8
# print(int(b))   # -> 7 , так как выводим ток целую часть


# # На вход принимаем число, проверяем кратно ли 5 и 10 или 15
# a = int(input('Введите число '))
# print(((a % 5 == 0) and (a % 10 == 0)) or (a % 15 == 0))



