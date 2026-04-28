# os 모듈

import os
print(os.name)  # nt:윈도우 뜻
print(os.getcwd()) # 현재 최상위 폴더
print(os.listdir()) # 현재 최상위 폴더 내부 요소

os.mkdir('hello') # 폴더 생성
os.rmdir('hello') # 폴더 삭제

with open('./day8/origianl.txt','w') as file:
    file.write( 'hello')

os.rename('./day8/origianl.txt','./day8/new.txt') # 파일명 변경
os.remove( './day8/new.txt') # 파일 삭제

os.system('dir') # 시스템 명령어 실행

# datetime 모듈
import datetime as a

print(a.datetime.now())
now=a.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 형식 : Y 년 m 월 d일 H시 M분 S초
time=now.strftime( '%Y-%m-%d %H:%M:%S') # 형식만들기
print(time)

# 시간 계산
year=now.replace( year=(now.year+1)) # 1년 뒤
print(year)

# item 모듈
import time
print('3초간 일시정지')
time.sleep(3)
print('떙')

# urllib 모듈
from urllib import request # from 이용하여 특정한 함수/변수 만 가져오기
target=request.urlopen("https://google.com")
output=target.read()
print(output)