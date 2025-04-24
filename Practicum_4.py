print('Задание 1')# Фильтр конвейра с батончиками
x = int(input())
list1=[]
while x != 0:
    while  40<=x<=50:
        list1.append(x)
        x=int(input())
        if x == 0:
            break
    else:
        x=int(input())
if x == 0:
    print( list1 )
x = int(input())
list1=[]
while x != 0:
    while  40<=x<=50:
        list1.append(x)
        x=int(input())
        if x == 0:
            break
    else:
        x=int(input())
if x == 0:
    print( list1 )

print('Задание 2')# Возврат бракованных батончиков

x = int(input())
list1=[]
while x != 0:
    while  40<=x<=50:

        x=int(input())
        if x == 0:
            break
    else:
        list1.append(x)
        x=int(input())
if x == 0:
    list1.reverse()
    print(list1)

x = int(input())
list1=[]
while x != 0:
    while  40<=x<=50:

        x=int(input())
        if x == 0:
            break
    else:
        list1.append(x)
        x=int(input())
if x == 0:
    list1.reverse()
    print(list1)

print('Задание 3')# Список цифр числа
x=int(input())
list1=[]
while x >0:
    t=x%10
    list1.append(t)
    y = x//10
    x=y
    while x==0:
        list1.reverse()
        print(list1)
        break

x=int(input())
list1=[]
while x >0:
    t=x%10
    list1.append(t)
    y = x//10
    x=y
    while x==0:
        list1.reverse()
        print(list1)
        break

print('Задание 4')# странный регулировщик
z=int(input())
x=int(input())
list1=[]
list2=[]

while len(list1) + len(list2)!=z:
    while x%2==0:
        list1.append(x)
        if len(list1) + len(list2) == z:
            break
        x = int(input())
    else:
        list2.append(x)
        if len(list1) + len(list2) == z:
            break
        x = int(input())
if len(list1) + len(list2)==z:
    list2.sort(reverse=True)
    list1.sort(reverse=False)
    print(list1)
    print(list2)

z=int(input())
x=int(input())
list1=[]
list2=[]

while len(list1) + len(list2)!=z:
    while x%2==0:
        list1.append(x)
        if len(list1) + len(list2) == z:
            break
        x = int(input())
    else:
        list2.append(x)
        if len(list1) + len(list2) == z:
            break
        x = int(input())
if len(list1) + len(list2)==z:
    list2.sort(reverse=True)
    list1.sort(reverse=False)
    print(list1)
    print(list2)

print('Задание 5')# Порядочные списки

z=int(input())
z1=int(input())
x=int(input())
list1=[]
while len(list1) !=z+z1:
    list1.append(x)
    if len(list1) ==z+z1:
        break
    x = int(input())
else:
    x = int(input())
if len(list1) ==z+z1:
    list1.sort(reverse=False)
    print(list1)

z=int(input())
z1=int(input())
x=int(input())
list1=[]
while len(list1) !=z+z1:
    list1.append(x)
    if len(list1) ==z+z1:
        break
    x = int(input())
else:
    x = int(input())
if len(list1) ==z+z1:
    list1.sort(reverse=False)
    print(list1)


