print("Задача 1") # Список имен
x=input()
y=x.split(None)
y.sort()
print(y)

x=input()
y=x.split(None)
y.sort()
print(y)

print("Задача 2") #Маркировка батончиков
N = int(input())
count = 1
z = {}
if count != N:
    x = input().split(None)
    Y = list(map(int, x))
    Z = {Y[0]: Y[1]}

    count = 1
    while count != N:
        while 40 <= Y[1] <= 50:
            Z[Y[0]] = "GOOD"
            z.update(Z)

            count += 1
            x = input().split(None)
            if count == N:
                break
        else:
            Z[Y[0]] = "BAD"
            z.update(Z)

            count += 1
            x = input().split(None)
            continue

if count == N:
    print(z)
    """ Не могу заставить накапливать список"""
print("Задача 3") #Список уникальных цифр числа
x=int(input())
list1=[]
while x >0:
    t=x%10
    list1.append(t)
    y = x//10
    x=y
    while x==0:
        list1.reverse()
        Eq=set(list1)
        EQ=list(Eq)
        print(EQ)
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
        Eq=set(list1)
        EQ=list(Eq)
        print(EQ)
        break

print("Задача 4") #Самая популярная цифра
N=int(input())
count=0
list1=[]
while count != N:
    x = int(input())
    count += 1
    while x >0:
        t=x%10
        list1.append(t)
        y = x//10
        x=y
    while x==0:
        break
    if count == N:
        break
if count==N:

    count2=0
    z=list1
    for i in list1:
        list2=list1.count(i)
        if list2>count2:
            count2=list2
            z=i
print(z)

print("Задача 5") #Два водителя
x=input()
z=input()
X=x.split(None)
Z=z.split(None)
y=set(X)&set(Z)
Y=list(y)
Y.sort()
print(Y)