#name = input('Enter your name')
#print('Hello', name)

#a = int(input())
#print(a*2)

#a = int(input())
#b = int(input())
#print(a * b)

#X = int(input()) задачка про сон Х часов и У минут
#Y = int(input())
#print(X*60 + Y)

#X = int(input())
#print(int(X // 60))
#print(int(X % 60))

# or - или, and - и, not - унарная, по приоритету выполнения - not, and, or
# AND - умножение, таким образом: True*False (1*0) = False, умножение на 0 всегда дает 0
# OR - сложение, таким образом: True+False (1+0) = True, в случае сложения True+True(1+1) - всегда будет True

#x = int(input())                                      #условия
#if x%2 == 0:
#    print('Четное')
#else:
#    print("Нечетное")

#a = int(input())
#b = int(input())
#if b != 0:
#    print(a / b)
#else:
#    print('Деление невозможно')
#    b = int(input('Введите не нулевое значение, '))
#    if b == 0:
#        print('Вы не справились')
#    else:
#        print(a / b)

#a, b, h = [int(input()) for i in range(3)]
#if h >= a and h <= b:
#    print ('Это нормально')
#else:
#    if h < a:
#        print ('Недосып')
#    if h > b:
#        print ('Пересып')

#n = int(input())                                                  #Високосный и не високосный год
#if ((n % 4 == 0) and not (n % 100 == 0)) or (n % 400 == 0):
#    print('Високосный')
#else:
#    print('Обычный')

#a = 'string'                    #работа со строками
#b = 'another string'
#print(a + '\n' + b)

#a = int(input(""))                    #задача про теорему Герома - площадь треугольника
#b = int(input(""))
#c = int(input(""))
#p = (a + b + c) / 2
#x = p*(p-a)*(p-b)*(p-c)
#S = x**0.5
#print(S)

#x = int(input())                             #ввод чисел
#if -15 < x <= 12 or 14 < x < 17 or 19 <= x:
#    print('True')
#else:
#    print('False')

#a = float(input())                             #КАЛЬКУЛЯТОР
#b = float(input())
#c = str(input())
#if c == '+':
#    print (a + b)
#elif c == '-':
#    print (a - b)
#elif c== '*':
#    print (a * b)
#elif c == 'pow':
#    print (a ** b)
#elif (c == 'mod' or c == 'div' or c == '/') and b == 0:
#    print ('Деление на 0!')
#elif c == 'mod':
#    print (a % b)
#elif c == 'div':
#    print (a // b)
#elif c == '/':
#    print (a / b)

x = str(input())
if x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    y = (p*(p-a)*(p-b)*(p-c))
    x = y ** 0.5
    print(x)
elif x == 'прямоугольник':
    a = int(input())
    b = int(input())
    x = a * b
    print(x)
elif x == 'круг':
    r = int(input())
    z = 3.14
    x = z * r ** 2
    print(x)