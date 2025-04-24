print('Задание 1')  #Высокостный год
def year_is_leap(n):
    if n%100==0:
        if n%400==0:
            return "LEAP"
        else:
            return "IS NOT LEAP"
    elif n%100!=0:
        if n%4==0:
            return "LEAP"
        else:
            return "IS NOT LEAP"
print(year_is_leap(2003))
print(year_is_leap(2004))
print(year_is_leap(2000))

print("Задание 2")  #Неравенство треугольника
def triangle_exists(a, b ,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'False'
    else:
        return 'True'
print(triangle_exists(2,3,4))
print(triangle_exists(2,3,5))
print(triangle_exists(2,3,6))

print("Задание 3")  #Квадрат наибольшего числа
def  max_square(*numbers):
    m_s=0
    for _ in numbers:
        m_s=max(numbers)**2
    return m_s
print(max_square(3))
print(max_square(3,7,0,1))
print(max_square(5,3,4,9))

print("Задание 4")  #Очень четные элементы
def very_even(*x):
    ve=[]
    for y in x:
        ve=y[1::2]
    ve2 = []
    for y2 in ve:
        if y2 % 2 == 0:
            ve2.append(y2)
    return ve2
print(very_even([2, 3, 4, 11, 3,  6, -4, 0]))
print(very_even([]))
print(very_even([2,1]))

print("Задание 5")  #Сладкий бизнес
def profit(days, num_pay, k_CB):
    profit1=((num_pay*2)*k_CB)-30*num_pay
    if days == 'Sunday' or days== 'Saturday':
        return profit1-500
    else:
        return profit1
print(profit('Wednesday', 13, 41))
print(profit('Saturday', 17, 70))
print(profit('Sunday', 1,50))