from random import randint
import timeit
import matplotlib.pyplot as plt
# Задание 1
print("Задание 1")
arr =[]
for i in range(10):
    arr.append(randint(0, 50))
print(arr)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr [j+1]:
                arr [j], arr [j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort(arr))
t_b = []
# Задание 2
print("Задание 2")
arr =[]
for i in range(10):
    arr.append(randint(0, 50))
def selected_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selected_sort(arr))
t_s = []
# Задание 3
print("Задание 3")
n_f=[]
arr = [14, 29, 8, 38, 0, 22, 21, 15, 38, 48]
n=len(arr)
arr1 = arr
bubble_sort(arr)
time_bubble = (timeit.timeit(lambda: bubble_sort, number = 1000))
t_b.append(time_bubble)
selected_sort(arr1)
time_selected = (timeit.timeit(lambda: selected_sort, number = 1000))
t_s.append(time_selected)
n_f.append(n)
arr =[49, 17, 24, 31, 13, 24, 5, 6, 33, 14]
arr1 = arr
bubble_sort(arr)
time_bubble = (timeit.timeit(lambda: bubble_sort, number = 1000))
t_b.append(time_bubble)
selected_sort(arr1)
time_selected = (timeit.timeit(lambda: selected_sort, number = 1000))
t_s.append(time_selected)
n_f.append(n)
arr =[12, 39, 33, 10, 38, 43, 5, 14, 27, 36]
arr1 = arr
bubble_sort(arr)
time_bubble = (timeit.timeit(lambda: bubble_sort, number = 1000))
t_b.append(time_bubble)
selected_sort(arr1)
time_selected = (timeit.timeit(lambda: selected_sort, number = 1000))
t_s.append(time_selected)
n_f.append(n)
print("Время выполнения поиска пузырьком -", t_b)
print("Время выполнения поиска методом выбора -", t_s)
plt.plot(t_b ,n_f )
plt.show()
plt.plot(t_s, n_f)
plt.show()