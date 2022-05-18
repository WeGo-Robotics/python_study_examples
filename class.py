# -*- coding: utf-8 -*-
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


class Simple:
    pass

a = Simple()

class FourCal:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.result = 0
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        self.result = self.first + self.second
        return self.result

    def sub(self):
        self.result = self.first - self.second
        return self.result

    def mul(self):
        self.result = self.first * self.second
        return self.result

    def div(self):
        self.result = self.first / self.second
        return self.result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
print(b.sum())
print(b.mul())
print(b.sub())
print(b.div())

class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'
    
    def show(self):
        print('국가 클래스의 메소드입니다')

    def show_name(self):
        print('국가의 이름을 알려줍니다')

class Korea(Country):
    """Sub Class"""

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'국가 이름은 : {self.name}')

tmp = Country()
tmp.show()
tmp.show_name()
print(tmp.capital)
print(tmp.population)
print(tmp.name)
a = Korea('대한민국')
a.show()
a.show_name()
print(a.capital)
print(a.population)
print(a.name)

class NumBox:
    def __init__(self, num):
        self.Num = num
    def __add__(self, num):
        self.Num += num
    def __sub__(self, num):
        self.Num -= num

n = NumBox(40)
n + 100
print(n.Num)
n - 110
print(n.Num)

