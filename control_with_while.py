# -*- coding: utf-8 -*-
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

while True:
    if a > 50:
        break
    print(a)
    a += 1