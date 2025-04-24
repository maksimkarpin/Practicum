print('Задание 01')#Подсчет гласных букв
def  count_vowels(x):
    word=list(x.lower())
    Z='eyuioa'
    g_b=[]
    w='qwrtpsdfghjklzxcvbnm'
    for i in word:
        if i in w:
            continue
        if i in Z:
            g_b.append(i)
        else:
            g_b = 'Слово должно состоять только из букв'
            return g_b
    return len(g_b)
print(count_vowels(input()))
print(count_vowels(input()))
print(count_vowels(input()))
print(count_vowels(input()))

print('Задание 02')#Перевод в верхний регистр
def   process_word(x):
    word=list(x.lower())
    Z='eyuioa'
    g_b=[]
    w='qwrtpsdfghjklzxcvbnm'
    for i in word:
        if i in w:
            continue
        if i in Z:
            continue
        else:
            g_b = 'Слово должно состоять только из букв'
            return g_b
    return x.upper()
print( process_word(input()))
print( process_word(input()))
print( process_word(input()))

print('Задание 03')#Путешествие во времени с ошибками
from datetime import  datetime
current_year = datetime.now().year
def time_travel(year):
    if year < current_year:
        raise ValueError("Вы не можете путешествовать в прошлое!")
    if year%2==0:
        raise RuntimeError("Ой, что то пошло не так! Машина времени сломана.")
    if year>current_year+99:
        raise UserWarning("Машина времени предупреждает: выбранный год слишком далеко в будущем.")
    else:
        return "Путешествие во времени прошло успешно!"
print(time_travel(int(input())))
print(time_travel(int(input())))
print(time_travel(int(input())))
print(time_travel(int(input())))

print('Задание 04')#Числовая Головоломка
def  solve_math_puzzle(puzzle):
    try:
        result =eval(puzzle)
        return result
    except NameError:
        return "В головоломке присутствуют некорректные символы или операции."
print(solve_math_puzzle(input()))
print(solve_math_puzzle(input()))
print(solve_math_puzzle(input()))

print('Задание 05')#Операция секретного кода
def process_secret_code(code):
    символы=list(code)
    Z = '%//**'
    for i in символы:
        if i in Z:
            return ("Некорректный формат ввода. Допустимые операторы: +, -, *, /.")
    try:
        result=eval(code)
        return result
    except ZeroDivisionError:
        return ("Некорректный формат кода: Деление на 0 недопустимо.")
    except NameError:
        return ("Некорректный формат ввода. Допустимые операторы: +, -, *, /.")
print(process_secret_code(input()))
print(process_secret_code(input()))
print(process_secret_code(input()))