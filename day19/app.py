# app.py : FastAPI 실행하는 파일
# controller : HTTP REST 파일
# service : 로직 파일

# 라우터 : 다른 .py에서 정의한 router 객체를 합치기


# [1] app.py
# (1) import
from fastapi import FastAPI
import uvicorn

# (2) FastAPI 객체
app=FastAPI()

# (3) FastAPI 객체로 uvicorn 서버 실행
if __name__=="__main__":
    uvicorn.run('app:app',host='127.0.0.1',port=8000,reload=True)

# (4) 라우터 연결 : 다른 .py에서 정의한 router객체 합치기
# .include_router(연결할 라우터)
import controller
app.include_router(controller.router)

