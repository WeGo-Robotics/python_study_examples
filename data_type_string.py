# -*- coding: utf-8 -*-

#문자열
a = "Hello World"
b = 'Python is Fun'
c = '''life is too short, you need python.'''
d = """Life is too short, You need python."""

e = "Hello \n World"
f = "Hello \t World"
g = "Hello \\ World"
h = "Hello \' World"
i = "Hello \" World"
j = "Hello \a World"

print(a), print(b), print(c), print(d),print(e), print(f), print(g), print(h), print(i), print(j)

# 문자열 포매팅
a = 'I eat %d apples.'%3
tmp = 'world'
b = 'Hello {}'.format(tmp)
c = f'Hello {tmp}'
print(a)
print(b)
print(c)

# 문자열 관련 함수
a = 'hobby'
print(a.count('b')) # 2
a = 'Python is best choid'
print(a.find('b')) # 10
print(a.find('k')) # -1
print(a.index('b')) # 10
#print(a.index('k')) # error
a = ','
print(a.join('abcd')) #a,b,c,d
a = 'hi'
print(a.upper()) # HI
a = 'HI'
print(a.lower()) # hi
a = ' hi'
print(a.strip()) # hi
a = "New world"
print(a.replace('New', 'old')) # old world
a = 'a:b:c:d'
print(a.split(':')) # ['a', 'b', 'c', 'd']