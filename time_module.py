# -*- coding: utf-8 -*-

import time

print(time.time()) # 1970년 1월 1일 0시 0분 0초를 기준으로 경과한 Time을 초단위로 리턴
print(time.localtime(time.time())) # time.time를 입력으로 받아서, 이를 연도, 월, 일, 시, 분 초의 형태로 변환해준다.
print(time.asctime(time.localtime(time.time()))) # 날짜와 time을 알아보기 쉬운 형태로 리턴하는 함수
print(time.ctime()) # 항상 현재 time을 리턴하는 함수
time.sleep(10) # 코드를 10초 동안 정지 시키는 함수
