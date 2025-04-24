print("Задание1")   #Генератор квадратов
def square_gen():
    for i in range(100):
        yield i*i
g= square_gen()
print(next(g))
print(next(g))
print(next(g))
g= square_gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("Задание2")   #Генератор календаря
def date_gen(data):
    y=data[0]
    m=data[1]
    d=data[2]
    #data1=(y,m,d)
    while True:
        data1 = (y, m, d)
        if m==11 and d==30:
            next_day=(yield data1)
            d=1
            m+=1
        if m==1 and d==31:
            next_day = (yield data1)
            d = 1
            m += 1
        if y%100==0:
            if y%400==0:
                if m==2 and d==29:
                    next_day = (yield data1)
                    d = 1
                    m += 1
        if y%100!=0:
            if y%4==0:
                if m==2 and d==29:
                    next_day = (yield data1)
                    d = 1
                    m += 1

        if m==2 and d==28:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==3 and d==31:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==4 and d==30:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==5 and d==31:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==6 and d==30:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==7 and d==31:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==8 and d==31:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==9 and d==30:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==10 and d==31:
            next_day = (yield data1)
            d = 1
            m += 1
        if m==12 and d==31:
            next_day = (yield data1)
            d = 1
            m = 1
            y+=1


        data1 = (y, m, d)
        next_day=(yield data1)
        d+=1
g = date_gen((2023, 10, 15))
print(next(g))
print(next(g))
print(next(g))
g = date_gen((2023, 11, 29))
print(next(g))
print(next(g))
print(next(g))
