from random import randint
# Задание 1
print("Задание 1")
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))
# Задание 2
print("Задание 2")
def sum_list(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_list(arr[1:])
print(sum_list([1, 2, 3, 4, 5]))
# Задание 3
print("Задание 3")
def binary_search(arr, low, high, key):
    if high > low:
        mid = (high+low) //2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid -1, key)
        else:
            return binary_search(arr, mid+1, high,key)
    return -1
arr =[]
for i in range(10):
    arr.append(randint(0, 15))
arr.sort()
print(arr)
print(binary_search(arr, 0, 10, 15))
# Задание 4
print("Задание 4")
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Стек пуст"
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Стек пуст"
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push("test")
    stack.push(True)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
