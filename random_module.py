# -*- coding: utf-8 -*-

import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

print(random.randint(1, 10)) # 1 ~ 10 사이의 정수 중 하나를 생성

print(random.random()) # 0~1 사이의 난수 생성