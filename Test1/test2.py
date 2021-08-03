#a = int(input())                         #сортировка чисел
#b = int(input())
#c = int(input())
#s = a + b + c;
#print(max(a,b,c))
#print(min(a,b,c))
#print(s - max(a,b,c) - min(a,b,c))

#n = int(input())
#print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))    #задача про программистов

#x = int(input())                #задача про билет
#a = x % 10
#b = (x // 10) % 10
#c = (x // 100) % 10
#d = (x // 1000) % 10
#e = (x // 10000) % 10
#f = (x // 100000) % 10
#if ((a + b + c) == (d + e + f)):
#    print('Счастливый')
#else:
#    print('Обычный')
                                                                        #WHILE
#a = 5                       #while цикл
#while a > 0:
#    print(a, end='')
#    a -= 1

#a = 5                      #while
#while a <= 55:
#    print(a)
#    a += 2
#
#a = 5                      #while
#while a <= 55:
#    if a % 2 == 1:
#        print(a)
#        a += 1

# i = 0
# while i <= 10:
#    i = i + 1
#    if i > 7:
#        i = i + 2
# print(i)

#n = int(input())
#c = 1
#while c <= n:
#    print('*' * c)
#    c += 1

#n = int(input())
#stars = '*'
#while len(stars) <= n:
#    print(stars)
#    stars += '*'

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1


# a = int(input())
# b = int(input())
# s = 0
# i = a
# while i <= b:
#     s += i
#     i += 1
# print(s)

# #№1
# a = int(input())
# s = a
# while a != 0:
#   a = int(input())
#   s += a
# print(s)
#
# #№2
# s = 0
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     else:
#         s += x
# print(s)

#1
# a = int(input())
# b = int(input())
# c = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# d = c // (a + b)
# print(d)

#2
# a = int(input())
# b = int(input())
# d = a
# while d%b:
#     d += a
# print(d)

                                                        #break continue

# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break # досрочно завершаем цикл
#     if (a == 0) or (b == 0):
#         continue # переходим к следующей итерации
#     print(a*b)
#     i += 1

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a >100:
#         break
#     else:
#         print(a)

                                                       #for
# n = int(input())
# for i in range(n):
#     print('*' * n)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()

                                                #калькулятор
# a =int (input())
# b =int (input())
# c =int (input())
# d =int (input())
# for g in range (c,d+1):
#     print('\t'+str(g),end='')
# print(end='\n')
# for i in range (a,b+1):
#     print(str(i)+'\t',end='')
#     for j in range (c,d+1):
#         print(str(i*j),end='\t')
#     print(end='\n')

#1 variant
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# for i in range(a, b+1):
#     if i % 2 == 1:
#         s += i
# print(s)

#2 variant
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b+1, 2): #с шагом 2
#     s += 1
# print(s)

#3 variant
# a, b = (int(i) for i in input().split())
# s = 0
# if a % 2 == 0:
#     a +=1
# for i in range(a, b+1, 2):
#     s += i
# print(s)
                          #задача вычислить среднее арифметическое
# a = int(input())
# b = int(input())
# s = 0 #сумма чисел
# c = 0 #счетчик чисел, которые делятся на 3
# for j in range (a,b+1):
#     if j%3 == 0:
#         s = s+j
#         c = c+1
# print(s/c)

