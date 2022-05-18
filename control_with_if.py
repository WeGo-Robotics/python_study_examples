# -*- coding: utf-8 -*-
x = 1
y = 2
if x > y :
    print('x is bigger than y')
elif x == y :
    print('x is same as y')
elif x < y :
    print('x is smaller than y')
else:
    print('Program error happened')

money = 2000
card = 1
if money >= 3000 or card:
    print('Taxi')
else:
    print('Walk')

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c')
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('Taxi')
else:
    print('Walk')

if 'money' in pocket:
    pass
else:
    print('Get the Card')
