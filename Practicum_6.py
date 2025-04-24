print('Задание 1') #Квадратный стиль
list=[1,2,3,4,5,6,7,8,9,10]
x=[i*i for i in list if i%2==0]
print(x)

print('Задание 2')  #Списковый синхрон
list1 = [1, 2, 3, 4, 5]
list2 = [10, 9, 8, 7, 6]
min_count = 4
a=[]
if len(list1) >= min_count and len(list2) >= min_count:
   for x in list1[:min_count:]:
       for y in list2[:min_count:]:
           a.append(x*y)
   print(a[0::min_count + 1])
elif  len(list1) < min_count or len(list2) < min_count:
    X=len(list1)
    Y=len(list2)
    if X>=Y:
        for x in list1[:X:]:
            for y in list2[:X:]:
                a.append(x * y)
        print(a[0::X+1])
    else:
        for x in list1[:Y:]:
            for y in list2[:Y:]:
                a.append(x * y)
        print(a[0::Y+1])

print('Задание 3')  #Буквы любят цифры
list1=['a', 2, 'b', 4, 'c', 5, 'd', 8, 'e', 9]
s=list1
a=list1[1::2]
A=[]
b=[]
for x in a:
    while x%2==0:
        A.append(x)
        break
    else:
        continue
X=A
B=[]
if len(X)>=2:
    for i in X:
        b.append(i*i)
    while len(X) >= 2:
      B.append(X[0]*X[1])
      X.pop(0)
    b.extend(B)
    print(b)
elif len(X)<2:
    print(*list1, sep='-')

list1=['a', 2, 'b', 3, 'c', 5, 'd', 7, 'e', 11]
s=list1
a=list1[1::2]
A=[]
b=[]
for x in a:
    while x%2==0:
        A.append(x)
        break
    else:
        continue
X=A
B=[]
if len(X)>=2:
    for i in X:
        b.append(i*i)
    while len(X) >= 2:
      B.append(X[0]*X[1])
      X.pop(0)
    b.extend(B)
    print(b)
elif len(X)<2:
    print(*list1, sep='-')
print('Задание 4')  #Генератор
a=[1, 2, 3, 4, 5]
b=[10, 9, 8, 7, 6]
c=[3, 6, 9, 12, 15]
list_1=[]
list_2=[]
list_1.append(a)
list_1.append(b)
list_1.append(c)
A=[]
A1=[]
for x in a:
    if x%2==0:
        A.append(x*x)
        A1.append(x)
    else:
        continue
A.append(sum(A1))
B=[]
B1=[]
for x in b:
    if x%2==0:
        B.append(x*x)
        B1.append(x)
    else:
        continue
B.append(sum(B1))
C=[]
C1=[]
for x in c:
    if x%2==0:
        C.append(x*x)
        C1.append(x)
    else:
        continue
C.append(sum(C1))
list_2.append(A)
list_2.append(B)
list_2.append(C)
print(list_2)
print('Задание 5')  #Сортировка
a=[15, 7, 42, 3, 8]
a.sort()
print(a)
print('Задание 6')  #Фруктам нужен порядок
a=["orange", "grape", "strawberry", "banana", "kiwi"]
print(a)
b=[]
print('Ожидаемые выходные данные:')
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if len(a[j+1])< len(a[j]):
            a[j+1], a[j]=a[j], a[j+1]
    print(a)
print('Отсортированный результат')
print(a)