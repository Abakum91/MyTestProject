                                        #Символы и строки
# genome = 'ATGG'
# genome[0]
# genome[1]
# genome[2]
# genome[3]
#
# genome[-1]
# genome[-2]
# genome[-3]
# genome[-4]

# Полезно будет добавить, что в квадратных скобках может быть два и даже три параметра. Параметры записываются так Var[A:B:C]. эти параметры, если их больше одного, ведут себя как оператор range(). Первый параметр означает с какого индекса начинать, второй означает на каком индексе закончить (не включая этот индекс) и третий - шаг (по умолчанию 1).
#
# Такое обращение со строкой позволяет выбирать не один а несколько символов или часть строки.
# Где А - индекс первого символа. Если его оставить пустым (например, Var[:B]), то перебираться будут все символы с начала строки и до В.
# B - (необязательный) индекс последнего символа. Если его оставить пустым (например, Var[A:]), то перебираться будут все символы начиная от A и до конца строки.
# С - (необязательный) шаг, через который выбираются символы. По умолчанию, если не указать, равен 1 - т.е перебираются все символы по порядку.
#
# Примеры: var="Hello!"
# var[0] -> 'H' - только первый символ
# var[1:] -> 'ello!' - все символы начиная со второго
# var[:3] -> 'Hell' - все символы до четвертого
# var[1:4] -> 'ello' - символы со второго по пятый
# var[::] -> 'Hello!' - выведутся все символы
# var[::2] -> 'Hlo' - здесь выбирается каджый второй символ строки, т.е. 0й 2й и 4й
# var[::-1] -> '!olleH'- выведутся все символы, но с шагом -1 - каждый символ, но в обратном порядке.

# genome = 'ATGG'
# for i in range(4):
#     print(genome[i])

#1v
# genome = input()
# cnt = 0
# for nucl in genome:
#     if nucl == 'C':
#         cnt += 1
# print(cnt)
#2v
# genome = input()
# print(genome.count('C'))

# s = 'agTtcAGtc'
# x = s.upper().count('gt'.upper())
# print(x)

# s = input()
# z = s
# i = 'G'
# j = 'C'
# x = s.upper().count(i) + s.upper().count(j)
# y = 0
# for i in s:
#     y += 1
# print(x/y*100)

# s = input()
# i = 0
# j = len(s) - 1
# is_palindrom = True
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#     i += 1
#     j -= 1
# if is_palindrom:
#     print('YES')
# else:
#     print('NOT')

# a = str(input())                      #Задача про а1б5 и тд
# sum = 1
# x = 1
# y = a[x:x+1]
# for i in a:
#     if i in y:
#         sum += 1
#     else:
#         print(i, end='')
#         print(sum, end='')
#         sum = 1
#     x += 1
#     y = a[x:x+1]

# a = [int(i) for i in input().split()]   #суммирование вводных чисел
# sum = 0
# x = 0
# y = a[x:x+1]
# for i in a:
#     sum += i
#     print(end='')
# print(sum)

# a = [int(item) for item in input().split()]
# b = []
# for i in range(len(a)):
#     if len(a) == 1:
#         print(a[0])
#         break
#     else:
#         if i == 0:
#             b.append(a[-1] + a[i + 1])
#         elif i > 0  and i != len(a) - 1:
#             b.append(a[i - 1] + a[i + 1])
#         else:
#             b.append(a[i - 1] + a[0])
# if b != 0:
#     for i in b:
#         print(i, end=' ')

# numbers = [int(i) for i in input().split(' ')]                   #задача вывести повторяющиеся числа
# numbers.sort()
# final = []
# for i in range(len(numbers)):
#     if len(numbers) == 1:
#         final = [] # при подаче одного элемента не выдает его же в результате
#     elif numbers[i] == numbers[i-1]:
#         if numbers[i] not in final:
#             final.append(numbers[i])
# # if len(final) == 0:
# #     print(' ')
# # else:
# #     for i in final:
# #         print(i, end=' ')
# # этот кусок вставляем если нужен возврат ' ' при отсутствии повторений
#
# for i in final:
#     print(i, end=' ') # если не нужен возврат ' ' при отсутствии повторений

# n = 3
# a = [[0]*n]*n
# a[0][0] = 5
# print(a)
#
# a = [[0]*n for i in range(n)]
# a = [[0 for j in range(n)] for i in range(n)]

# a = b = 0
# while True:
#    n = int(input())
#    a += n
#    b += n ** 2
#    if a == 0:
#        print(b)
#        break

# list, n=[], int(input())
# for i in range(n):
#     count = 0
#     if n == 1:
#         break
#     while count < i + 1:
#         list.append(i + 1)
#         count += 1
#         if len(list) == n:
#             print(*list)
#             break

# dlina = int(input())
# tek_ch = 1   #хранение текущего числа
# i = 1
# kol = 0   #номер позиции в последовательности одного числа
# while i < dlina + 1:
#     if tek_ch == kol + 1:   #условие перехода к след. числу
#         print(tek_ch, end=' ')
#         i += 1
#         kol = 0
#         tek_ch +=1
#         continue
#     else:
#         print(tek_ch, end=' ')
#         kol += 1
#     i += 1

# print('*' * 17, '*               *', '*               *', '*' * 17, sep='\n')

# print('*'*17, end=' ')
# print('*', '*', end=' ', sep='               ',)
# print('*', '*', end=' ', sep='               ')
# print('*', '*', end=' ', sep='               ')
# print('*'*17)

# lst = [int(i) for i in input().split()]   # 2.6
# x = int(input())
#
# indices = [pos for pos, num in enumerate(lst) if num == x]
#
# if indices:
#     for i in indices:
#         print(i, end=' ')
# else:
#     print("Отсутствует")

