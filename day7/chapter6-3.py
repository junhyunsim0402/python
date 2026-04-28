# 모듈 호출 하기
# 표준 모듈 : 파이썬 내장 라이브러리
# 외부 모듈 : 설치형 라이브러리
# import 모듈명
# 특정한변수/함수 가져오기 : from 모듈명 import 가져오고싶은 함수 또는 변수
# 모두 가져오기           : from 모듈명 import *
# 식별자부여            : import 모듈명 as 식별자명

import math # import 모듈명
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

from math import sin,cos,tan,floor,ceil

import math as m
print(m.sin(1))

# random 모듈
import random

print(random.random())          # 0~1까지 난수 생성
print(random.uniform(10,20))    # uniform(시작값,끝값), 실수
print(random.randrange(1,10))   # randrange(시작값,끝값) 정수
print(random.choice([10,20,30,40])) # choice([리스트]), 리스트내 랜덤요소 1개 반환
print(random.shuffle([1,2,3,4,5]))  # shuffle([리스트]), 리스트내 요소들을 랜덤으로 섞는다
print(random.sample([1,2,3,4,5],k=3)) # sample([리스트],k=개수) 리스트내 k개 랜덤 요소 반환
