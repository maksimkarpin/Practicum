print("Задание1")   #Вычисление степени без цикла
def power(N,M):
    return N**M
print(power(2,3))
print(power(2,0))
print(power(5,3))

print("Задание2")   #Палиндром без цикла
def is_palindrome(x):
    if x==x[::-1]:
        return "True"
    else:
        return "False"
print(is_palindrome([2, 3, 4, 3, 2]))
print(is_palindrome([2, 3,  3, 2]))
print(is_palindrome([2]))
print(is_palindrome([2, 3, 4, 3, 1]))

print("Задание3")   #Арифметическая прогрессия
def progression(start, step):
    x=start-step
    def inc():
        nonlocal x
        x+=step
        return x
    return inc
f = progression(3, 5)
print(f())
print(f())
print(f())
f = progression(12, -7)
print(f())
print(f())
print(f())
print(f())
f = progression(6, 0)
print(f())
print(f())
print(f())

print("Задание4")   #Аргументирующий декоратор
import functools
def arg_decor(func):
    def some_func(a,b,c):
        print(f"value={a}", type(a))
        print(f"value={b}", type(b))
        print(f"value={c}", type(c))
        r=func(a,b,c)
    return some_func
@arg_decor
def some_func_1(a,b,c):
    print(f'{a}.{b}.{c}')
some_func_1(3, 'Помидор',3.14)
@arg_decor
def some_func_2(*cool_args):
    pass
some_func_2(3, 'Помидор',3.14)

print("Задание5")   #Скобочные последовательности
def bracket_sequences(a):
   result=[]
   x=a*"()"
   result.append(x)
   if a>1:
       y=a * "(" + a * ")"
       result.append(y)
   result.sort()
   return result
print(bracket_sequences(0))
print(bracket_sequences(1))
print(bracket_sequences(2))