# -*- coding: utf-8 -*-
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60 : continue
    print(f'{number} student is passed')

a = range(10)
print(a)
sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)

