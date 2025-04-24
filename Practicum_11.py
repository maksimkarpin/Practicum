print("Задание 01")#Оркестр животных и их симфония методов
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,name, sound):
        self.name = name
        self.sound = sound
    @abstractmethod
    def  make_sound(self):
        pass
class Mammal(Animal):
    def make_sound(self):
        return self.sound, self.name
    def num_legs(self, legs):
        self.legs = legs
        return self.legs
    def give_legs(self):
        return "Млекопитающее родило потомство"
class Bird(Animal):
    def make_sound(self):
        return self.sound, self.name
    def can_fly(self):
        return "Птица летит"

mammal=Mammal("Котенок", "Мяу")
make_sound = mammal.make_sound()
num_legs=mammal.num_legs("4 лапы")
give_legs = mammal.give_legs()
print(make_sound)
print(num_legs)
print(give_legs)
mammal=Mammal("Дельфин", "УУУУУ")
make_sound = mammal.make_sound()
num_legs=mammal.num_legs("3 ласты")
give_legs = mammal.give_legs()
print(make_sound)
print(num_legs)
print(give_legs)
bird=Bird("Птичка", "Поет")
make_sound=bird.make_sound()
fly=bird.can_fly()
print(make_sound)
print(fly)

print("Задание 02")#Библиотечная
from abc import ABC, abstractmethod
class Book(ABC):
    def __init__(self, title, author, published_year):
        self._title = title
        self._author = author
        self._published_year = published_year
class  Library(Book):
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_published_year(self):
        return self._published_year

    def set_title(self, title):
        self._title = title
    def set_author(self,author):
        self._author = author
    def set_published_year(self, published_year):
        self._published_year = published_year

        print (self._title, self._author, self._published_year)
    def del_title(self):
        del self._title
    def del_author(self):
        del self._author
    def del_published_year(self):
        del self._published_year

    get_title = property(get_title, set_title, del_title)
    get_author = property (get_author, set_author,  del_author)
    get_published_year = property (get_published_year, set_published_year, del_published_year)
library = Library(0, 0,0)
library.get_title = "Дон Кихот"
library.get_author = 'Мигель де Сервантес'
library.get_published_year = "1065"
library.set_author
library.get_title = "Граф Монте-Кристо"
library.get_author = "Александр Дюма"
library.get_published_year = "1846"
library.set_author
library.del_title = "Граф Монте-Кристо"
library.del_author = 'Александр Дюма'
library.del_published_year = "1846"
library.set_author
library.set_author

print("Задание 03")#Калькулятор
class Calculator:
    def __init__(self, number):
        self.number = number
    def set_value(self, number):
        self.number = number
    def get_value(self):
        print(self.number)
    def add(self, n_add):
        self.number = self.number + n_add
    def substract(self, n_substract):
        self.number = self.number - n_substract
    def multiply(self, n_multiply):
        self.number = self.number * n_multiply
    def divide(self, n_divide):
        try:
            self.number = self.number / n_divide
        except ZeroDivisionError:
            print ("Нельзя делить на ноль")

cal = Calculator(0)
cal.set_value(0)
cal.get_value()
cal.add(50)
cal.get_value()
cal.substract(10)
cal.get_value()
cal.multiply(2)
cal.get_value()
cal.multiply(3)
cal.get_value()
cal.divide(2)
cal.get_value()
cal.divide(0)
cal.get_value()
print("Задание 04")#Калькулятор 2.0
class AdvancedCalculator(Calculator):
    def set_value(self, number):
        self.number = number
    def get_value(self):
        print(self.number)
    def power(self, n_power):
        self.number = self.number ** n_power
    def square_root(self, n_square_root):
        if n_square_root<0:
            print("Ведите положительное число")
        else:
            self.number = self.number ** 1/n_square_root
cal = AdvancedCalculator(Calculator)
cal.set_value(5)
cal.power(25)
cal.get_value()
cal.square_root(7)
cal.get_value()
cal.square_root(-1)
cal.get_value()
cal.multiply(4)
cal.get_value()