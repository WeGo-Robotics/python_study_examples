# -*- coding: utf-8 -*-

#리스트 인덱싱 및 슬라이싱
a = [1, 2, 3]
print(a[0])
print(a[0] + a[2])
print(a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1]) # ['a', 'b', 'c']
print(a[-1][0]) # 'a'
a = [1, 2, 3, 4, 5]
print(a[0:2]) # [1, 2]

#리스트 연산자
a = [1, 2, 3]
b = [4, 5]
print(a + b) # [1, 2, 3, 4, 5]
a = [1, 2, 3]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 변경
a = [1, 2, 3]
a[2] = 4
print(a) # [1, 2, 4]
a[1:2] = ['a', 'b', 'c']
print(a) # [1, 'a', 'b', 'c', 4]
a[1:3] = []
print(a) # [1, 'c', 4]
del a[1]
print(a) # [1, 4]

#리스트 내장함수
a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]
a.append([5, 6])
print(a) # [1, 2, 3, 4, [5, 6]]
a = [1, 4, 3, 2]
a.sort()
print(a) # [1, 2, 3, 4]
a = [1, 3, 2]
a.reverse()
print(a) # [2, 3, 1]
a = [1, 2, 3]
a.insert(0, 4)
print(a) # [4, 1, 2, 3]
a.insert(3, 5)
print(a) # [4, 1, 2, 5, 3]
a = [1, 2, 1, 2]
a.remove(2)
print(a) # [1, 1, 2]
a = [1, 2, 3]
a.pop()
print(a) # [1, 2]
a = [1, 2, 3]
a.pop(1)
print(a) # [1, 3]
a = [1, 2, 3, 1]
print(a.count(1)) # 2
a = [1, 2, 3]
a.extend([4, 5])
print(a) # [1, 2, 3, 4, 5]