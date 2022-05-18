# -*- coding: utf-8 -*-

# 정수형
a = 123
b = -178
c = 0

# 실수형
a = 1.2
b = -3.45
c = 4.24E10
d = 4.24e-10

# 8진수
a = 0o177
b = 0O177

#16진수
a = 0x8ff
b = 0xABC

#복소수
a = 1+2j
b = 3-4J

print(a.imag) # 2
print(a.real) # 1
print(a.conjugate()) # 1-2j
print(abs(a)) # 2.23606
