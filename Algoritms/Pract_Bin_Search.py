import timeit
import matplotlib.pyplot as plt
# Задание 1
print("Задание 1")
import random
from random import randint
arr = []
for i in range(10):
    arr.append(randint(1,50))
arr.sort()
num = int(12)
first = 0
mid = len(arr) // 2
last = len(arr) -1
while arr[mid] != num and first<= last:
    if num > arr[mid]:
        first = mid +1
    elif num < arr[mid]:
        last = mid -1
    mid = (first + last) // 2
if first > last:
    print(-1)
else:
    print("Индекс:", mid)
# Задание 2
print("Задание 2")
print("При выполнении алгоритма бинарного поиска, происходит более сложный процесс в отличии от линейного поиска"
      "Однако поиск происходит за счет прохода списка с двух сторон, что должно упрощать нахождение исходного числа, но требуется отсортировать список."
      "Применяется такой же подсчет элементов")
# Задание 3
print("Задание 3")
for i in range(100):
    arr.append(randint(1,50))
arr.sort()
def bin_search(num):
    first = 0
    mid = len(arr) // 2
    last = len(arr) - 1
    while arr[mid] != num and first <= last:
        if num > arr[mid]:
            first = mid + 1
        elif num < arr[mid]:
            last = mid - 1
        mid = (first + last) // 2
    if first > last:
        print(-1)
    else:
        print("Индекс:", mid)
bin_search(12)
bin_search(45)
bin_search(22)
bin_search(44)
# Задание 4
print("Задание 4")
n = len(arr)
def linear_search(key):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1
n_l_f = []
t_l_f = []
n_b_f = []
t_b_f = []
time =timeit.timeit (lambda:bin_search, number = 1000)
time1 =timeit.timeit (lambda:linear_search, number = 1000)
n_l_f.append(n)
n_b_f.append(n)
t_l_f.append(time1)
t_b_f.append(time)
time =timeit.timeit (lambda:bin_search, number = 1000)
time1 =timeit.timeit (lambda:linear_search, number = 1000)
n_l_f.append(n)
n_b_f.append(n)
t_l_f.append(time1)
t_b_f.append(time)
time =timeit.timeit (lambda:bin_search, number = 1000)
time1 =timeit.timeit (lambda:linear_search, number = 1000)
n_l_f.append(n)
n_b_f.append(n)
t_l_f.append(time1)
t_b_f.append(time)
time =timeit.timeit (lambda:bin_search, number = 1000)
time1 =timeit.timeit (lambda:linear_search, number = 1000)
n_l_f.append(n)
n_b_f.append(n)
t_l_f.append(time1)
t_b_f.append(time)
plt.plot(t_l_f, n_l_f)
plt.show()
plt.plot(t_b_f, n_b_f)
plt.show()


