print('Задание1') # Автомат с газировкой
x = float(input())
while x>=0.2:
    print('OK')
    x=x-0.2
else:
    print('Error: lack of water')
x = float(input())
while x>=0.2:
    print('OK')
    x=x-0.2
else:
    print('Error: lack of water')
print('Задание 2') # Счетчик бракованных батончиков
x = int(input())
count = 0
count1= 0
while x != 0:

    while  40<=x<=50:
        print('GOOD')
        x=int(input())
        count += 1
        if x == 0:
            break
    else:
        print('BAD')
        x=int(input())
        count1 += 1

    Scount = count + count1
if x == 0:
    print( count1/Scount )

x = int(input())
count = 0
count1= 0
while x != 0:

    while  40<=x<=50:
        print('GOOD')
        x=int(input())
        count += 1
        if x == 0:
            break
    else:
        print('BAD')
        x=int(input())
        count1 += 1

    Scount = count + count1
if x == 0:
    print( count1/Scount )

print('Задание 3') #Star stair
h = int(input())
for l in range(1, h+1):
    print('*' * l )

h = int(input())
for l in range(1, h+1):
    print('*' * l )

print('Задание 4') # Счетчик счастливых чисел Тома
a=int(input())
b=int(input())
count = -1
for x in range(0,b+1,77):
    if x <= a :
        count = 0
        continue

    count += 1
print(count)

a=int(input())
b=int(input())
count = -1
for x in range(0,b+1,77):
    if x <= a :
        count = 0
        continue

    count += 1
print(count)

a=int(input())
b=int(input())
count = -1
for x in range(0,b+1,77):
    if x <= a :
        count = 0
        continue

    count += 1
print(count)

print('Задание 5') #Квадраты в диапозоне
a = int(input())
b= int(input())
for x in range(a, b+1):
    for y in range(0, b+1):
        u=y**2
        if x==u:
            print(u)
            continue

a = int(input())
b= int(input())
for x in range(a, b+1):
    for y in range(0, b+1):
        u=y**2
        if x==u:
            print(u)
            continue

a = int(input())
b= int(input())
for x in range(a, b+1):
    for y in range(0, b+1):
        u=y**2
        if x==u:
            print(u)
            continue
