# FastApi : 파이썬 웹 프레임워크
# 특징 : RESTAPI, API문서자동 등등
# 사용처 : 데이터분석, AI모델, (머신러닝, 딥러닝) 서버

# https://fastpi.tiangolo.com/ko
# 1. 설치 :  pip install "fastapi[standard]"
# 2. import : import uvicorn, from fastapi import FastAPI
# 3. app객체 생성, 자바와 다르게 파이썬은 인스턴스 생성시 new 없음
# 4. uvicorn.run('파일명:app',host='로컬ip',port=서버포트번호,reload=자동재실행(True))
# 5. 

import uvicorn                  # 파이썬서버(8000) # 자바의 톰캣 역할
from fastapi import FastAPI     # REST정의        # 자바의 SPRINGWEB역할

# app 객체 생성
app=FastAPI()

# 모듈(.py) 실행 시작점
if __name__=="__main__" : # 자바의 main함수 역할
    # uvicorn.run('파일명:app',host='로컬ip',port=서버포트번호,reload=자동재실행(True))
    uvicorn.run('T8-01:app',host='127.0.0.1',port=8000,reload=True)

