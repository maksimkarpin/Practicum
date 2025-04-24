print('Задача 1')
a = int(input())
b = int(input())
c = int(input())
if c > a < b:
    if b < c or b == c:
        print(a, b, c)
    elif c < b:
        print(a, c, b)
elif c > b < a:
    if c < a or c == a:
        print(b, c, a)
    elif c > a:
        print(b, a, c)
else:
    if a > b or a == b:
        print(c, b, a)
    else:
        print(c, b, a)
a = int(input())
b = int(input())
c = int(input())
if c > a < b:
    if b < c or b == c:
        print(a, b, c)
    elif c < b:
        print(a, c, b)
elif c > b < a:
    if c < a or c == a:
        print(b, c, a)
    elif c > a:
        print(b, a, c)
else:
    if a > b or a == b:
        print(c, b, a)
    else:
        print(c, b, a)
a = int(input())
b = int(input())
c = int(input())
if c > a < b:
    if b < c or b == c:
        print(a, b, c)
    elif c < b:
        print(a, c, b)
elif c > b < a:
    if c < a or c == a:
        print(b, c, a)
    elif c > a:
        print(b, a, c)
else:
    if a > b or a == b:
        print(c, b, a)
    else:
        print(c, b, a)
a = int(input())
b = int(input())
c = int(input())
if c > a < b:
    if b < c or b == c:
        print(a, b, c)
    elif c < b:
        print(a, c, b)
elif c > b < a:
    if c < a or c == a:
        print(b, c, a)
    elif c > a:
        print(b, a, c)
else:
    if a > b or a == b:
        print(c, b, a)
    else:
        print(c, b, a)
print('Задание 2')
a = int(input())
b = int(input())
print('Введите знак > или <')
s = input()
if s == '<':
    if a < b:
        print(a, b)
    elif b < a:
        print(b, a)
    else:
        print(a, b)
elif s == '>':
    if a > b:
        print(a, b)
    elif b > a:
        print(b, a)
    else:
        print(a, b)
else:
    print('Ошибка')
a = int(input())
b = int(input())
print('Введите знак > или <')
s = input()
if s == '<':
    if a < b:
        print(a, b)
    elif b < a:
        print(b, a)
    else:
        print(a, b)
elif s == '>':
    if a > b:
        print(a, b)
    elif b > a:
        print(b, a)
    else:
        print(a, b)
else:
    print('Ошибка')
print('Задание 3')
a = int(input())
if a % 2 == 0:
    print("Это четное число")
elif a % 2 != 0:
    print('Это нечетное число')
a = int(input())
if a % 2 == 0:
    print("Это четное число")
elif a % 2 != 0:
    print('Это нечетное число')
a = int(input())
if a % 2 == 0:
    print("Это четное число")
elif a % 2 != 0:
    print('Это нечетное число')
a = int(input())
if a % 2 == 0:
    print("Это четное число")
elif a % 2 != 0:
    print('Это нечетное число')
a = int(input())
if a % 2 == 0:
    print("Это четное число")
elif a % 2 != 0:
    print('Это нечетное число')
print('Задание 4')
a = int(input())
b = int(input())
c = int(input())
if a + b == c or a + c == b or b +c == a:
    print('Ошибка')
elif a + b != c or a + c != b or b +c != a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b !=c or a == c != b or c == b != a:
        print('Равнобедренный треугольник')
    else:
        print('Обычный треугольник')
a = int(input())
b = int(input())
c = int(input())
if a + b == c or a + c == b or b +c == a:
    print('Ошибка')
elif a + b != c or a + c != b or b +c != a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b !=c or a == c != b or c == b != a:
        print('Равнобедренный треугольник')
    else:
        print('Обычный треугольник')
a = int(input())
b = int(input())
c = int(input())
if a + b == c or a + c == b or b +c == a:
    print('Ошибка')
elif a + b != c or a + c != b or b +c != a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b !=c or a == c != b or c == b != a:
        print('Равнобедренный треугольник')
    else:
        print('Обычный треугольник')
a = int(input())
b = int(input())
c = int(input())
if a + b == c or a + c == b or b +c == a:
    print('Ошибка')
elif a + b != c or a + c != b or b +c != a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b !=c or a == c != b or c == b != a:
        print('Равнобедренный треугольник')
    else:
        print('Обычный треугольник')
print('Задание 5')
print('Первый игрок, введите:"камень", "ножницы" или "бумага"')
a = input().lower()
print('Второй игрок, введите:"камень", "ножницы" или "бумага"')
b = input().lower()
if a==b:
    print('Ничья')
elif a!=b:
    if a=='камень' and b == 'ножницы' or a=='бумага' and b=='камень' or a=='ножницы' and b=='бумага':
        print('Победил первый игрок')
    elif b=='камень' and a == 'ножницы' or b=='бумага' and a=='камень' or b=='ножницы' and a=='бумага':
        print('Победил второй игрок')
else:
    print('Ошибка')
print('Первый игрок, введите:"камень", "ножницы" или "бумага"')
a = input().lower()
print('Второй игрок, введите:"камень", "ножницы" или "бумага"')
b = input().lower()
if a==b:
    print('Ничья')
elif a!=b:
    if a=='камень' and b == 'ножницы' or a=='бумага' and b=='камень' or a=='ножницы' and b=='бумага':
        print('Победил первый игрок')
    elif b=='камень' and a == 'ножницы' or b=='бумага' and a=='камень' or b=='ножницы' and a=='бумага':
        print('Победил второй игрок')
else:
    print('Ошибка')
print('Первый игрок, введите:"камень", "ножницы" или "бумага"')
a = input().lower()
print('Второй игрок, введите:"камень", "ножницы" или "бумага"')
b = input().lower()
if a==b:
    print('Ничья')
elif a!=b:
    if a=='камень' and b == 'ножницы' or a=='бумага' and b=='камень' or a=='ножницы' and b=='бумага':
        print('Победил первый игрок')
    elif b=='камень' and a == 'ножницы' or b=='бумага' and a=='камень' or b=='ножницы' and a=='бумага':
        print('Победил второй игрок')
else:
    print('Ошибка')
