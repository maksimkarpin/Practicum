print('Задание01')#Анализ данных о космических кораблях
import csv
with open("spaceships.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Название','Тип','Год запуска','Максимальная скорость (км/ч)','Страна производитель'])
    writer.writerow(['Аполлон-11','Лунный модуль',1969 ,39068,'США'])
    writer.writerow(['Союз-ТМ','Космический корабль',2002,27720,'Россия'])
    writer.writerow(['Фалькон-9','Ракета-носитель',2010,27700,'США'])
    writer.writerow(['Юнион-2','Космический корабль',1999,28000,'Россия'])
    writer.writerow(['Ариан-5','Ракета-носитель',1996,40721,'Европейский союз'])
    writer.writerow(['Шаттл "Дискавери"','Космический корабль',1984,27480,'США'])
    writer.writerow(['Тяньгун-1','Космическая станция',2011,28000,'Китай'])
    writer.writerow(['Прогресс-М','Грузовой корабль',2000,28155,'Россия'])
    writer.writerow(['Гагарин-1','Космический корабль',2018 ,30000,'Россия'])
    writer.writerow(['Старшот','Межпланетная зондовая миссия',2022,72000,'США'])
    writer.writerow(['СпейсХоппер','Пилотируемый космический корабль',2020,28000,'США'])
    writer.writerow(['Альфа-Центавр-1','Межзвездный зонд',2030,200000,'Международный проект'])
    writer.writerow(['Сатурн-V','Ракета-носитель',1967,40190,'США'])
    writer.writerow(['Тианьшу-2','Космическая станция',2025,30000,'Китай'])
    writer.writerow(['Дракон','Грузовой космический корабль',2012,28000,'США'])
    writer.writerow(['Восток-1','Космический корабль',1961,27000,'СССР'])
    writer.writerow(['Протон-М','Ракета-носитель',2001,30800,'Россия'])
    writer.writerow(['Арес-1','Ракета-носитель',2030,37000,'США'])
    writer.writerow(['Сентинел','Космический телескоп',2022,65000,'Международный проект'])
    writer.writerow(['Пегас','Грузовой космический корабль',1988,28000,'США'])
with open("spaceships.csv", "r") as f:
    read = csv.reader(f)
    count=-1
    count1=0
    x = []
    l = []
    for i in read:
        try:
            count+=1
            a=int(i[2])
            b=int(i[3])
            c=str(i[0])
            d=str(i[4])
            x.append(b)
            y=max(x)
            if b==y:
                l.append(c)
                l.append(d)
            if a > 2000:
                count1+=1
            else:
                continue
        except Exception:
            pass
    print(count, count1,l[-2],l[-1])

print('Задание02')#Анализ данных о фильмах
with open("movies.csv", "w",  newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Название','Год выпуска','Жанр','Режиссер','Сборы (в миллионах долларов)'])
    writer.writerow(['Звёздные войны: Эпизод IX - Скайуокер. Восход',2019,'Фантастика','Джей Джей Абрамс',1074])
    writer.writerow(['Аватар',2009,'Фантастика','Джеймс Кэмерон',2788])
    writer.writerow(['Темный рыцарь',2008,'Боевик','Кристофер Нолан',1004])
    writer.writerow(['История игрушек 3',2010,'Анимация','Ли Анкрич',1067])
    writer.writerow(['Анна Каренина',2012,'Драма','Джо Райт',684])
    writer.writerow(['Исходный код',2011,'Триллер','Дункан Джонс',147])
    writer.writerow(['Мстители: Финал',2019,'Боевик','Джо Руссо',2798])
    writer.writerow(['Гладиатор',2000,'Боевик','Ридли Скотт',460])
    writer.writerow(['Титаник',1997,'Драма','Джеймс Кэмерон',2208])
    writer.writerow(['Первому игроку приготовиться',2018,'Фантастика','Стивен Спилберг',582])
    writer.writerow(['Бешеные псы',1992,'Криминал','Квентин Тарантино',213])
    writer.writerow(['Храброе сердце',1995,'Эпический фильм','Мэл Гибсон',213])
    writer.writerow(['Хищник',1987,'Фантастика','Джон МакТирнан',98])
    writer.writerow(['Шрек',2001,'Анимация','Эндрю Адамсон',484])
    writer.writerow(['Побег из Шоушенка',1994,'Драма','Фрэнк Дарабонт',142])
    writer.writerow(['Пираты Карибского моря: Проклятие Черной жемчужины',2003,'Приключенческий фильм','Гор Вербински',654])
    writer.writerow(['Матрица',1999,'Научная фантастика','Лана и Лилли Вачовски',463])
    writer.writerow(['Поймай меня если сможешь',2002,'Драма','Стивен Спилберг',352])
    writer.writerow(['Темный рыцарь: Возрождение легенды',2012,'Боевик','Кристофер Нолан',1081])
    writer.writerow(['Гарри Поттер и Дары смерти: Часть 2',2011,'Фэнтези','Дэвид Йэтс',1341])
    writer.writerow(['Бесславные ублюдки',2009,'Вестерн','Квентин Тарантино',321])
    writer.writerow(['Голодные игры',2012,'Фантастика','Гэри Росс',694])
    writer.writerow(['Джанго освобожденный',2012,'Вестерн','Квентин Тарантино',425])
    writer.writerow(['Железный человек',2008,'Боевик','Джон Фавро',585])
    writer.writerow(['Крестный отец',1972,'Криминал','Фрэнсис Форд Коппола',250])
    writer.writerow(['Зеленая миля',1999,'Драма','Фрэнк Дарабонт',286])
    writer.writerow(['Помни',1994,'Драма','Кристофер Нолан',313])
    writer.writerow(['Леон',1994,'Триллер','Люк Бессон',46])
    writer.writerow(['Титаник',1997,'Драма','Джеймс Кэмерон',2208])
    writer.writerow(['Ла Ла Ленд',2016,'Мюзикл','Дэмьен Шазелл',446])

with open("movies.csv", "r") as f:
    read = csv.reader(f)
    count=-1
    count1=0
    list_fee = []
    fee_all= []
    list_print=[]
    for i in read:
        try:
            count+=1
            year=int(i[1])
            fee=int(i[4])
            name_movie=str(i[0])
            director= str(i[3])
            fee_all.append(fee)
            max_fee=max(fee_all)
            if fee == max_fee:
                list_print.append(name_movie)
                list_print.append(year)
                list_print.append(director)
            if year > 2010:
                list_fee.append(fee)
            else:
                continue
        except Exception:
            pass
    summ_fee = sum(list_fee)
    print(count, summ_fee, list_print[-3],list_print[-2],list_print[-1])

print('Задание03')#Вывод загадочных данных
import json
data = {"message":"7h1s_15_4_m3554g3", "code_name":"3xpl0r3r","location":{"latitude":37.7749,"longitude":-122.4194},"data":[42,True,"s3cr37"],"status":"c0d3_und3r_1nv35t1g4710n"}
with open("mysterious_data.json", "w") as f:
    json.dump(data,f)
with open("mysterious_data.json", "r") as f:
    m_d = json.loads(*f)
    for i in m_d:
        print(i, m_d[i])

print('Задание04')#Охота за сокровищами
