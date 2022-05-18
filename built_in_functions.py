# -*- coding: utf-8 -*-
print(abs(3))
print(abs(-3))
print(abs(-1.2))

print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

print(any([1, 2, 3, 0]))
print(any([0, ""]))

print(chr(97))
print(chr(48))

print(dir([1, 2, 3]))
print(dir({'1':'a'}))

print(divmod(7, 3))
print(divmod(1.3, 0.2))

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(hex(234))
print(hex(3))

a = 3
print(id(3))
print(id(a))
b = a
print(id(b))

a = input()
print(a)
b = input('Enter: ')
print(b)

print(int('3'))
print(int(3.3))
print(int('11', 2))
print(int('1A', 16))

class Person: pass

a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))

sum = lambda a, b: a + b
print(sum(1, 2))
mul = lambda a, b: a * b
print(mul(10, 20))

print(len('python'))
print(len([1, 2, 3]))
print(len((1, 'a')))

print(list('python'))
print(list((1, 2, 3)))

def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))

print(max([1, 2, 3]))

print(min([1, 2, 3]))

print(oct(34))
print(oct(12345))

print(ord('a'))
print(ord('0'))

print(pow(2, 4))
print(pow(3, 3))

print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))

print(str('hi'))
print(str(3))
print(str('HI'))

print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

print(type('abc'))
print(type([]))
print(type(tuple('abc')))

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip('abc', 'def')))