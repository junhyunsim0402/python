# 1. import 가져오기
import uvicorn
from fastapi import FastAPI

# 2. fastapi객체 생성
app=FastAPI()

# 3. 서버 실행
if __name__=="__main__":
    uvicorn.run('T8-02:app',host='127.0.0.1',port=8000,reload=True)

# 4. REST 정의하기
# REST : 자원 주고 받는 상태 구조   # REST API : HTTP로 REST 구현한 아키텍쳐
# 자동으로 jSON타입으로 응답한다 vs @ResponseBody(@RestController)
# GetMapping() vs @app.get()

@app.get('/') # HTTP GET 방식으로 매핑한다 # 주소 정의
async def index():
    return "안녕 파이썬웹"

# 5. 쿼리 파라미터
@app.get('/user')
async def find_user(name,age:int): # URL?변수값=값&변수명=값    # 기본 타입 str # 변수명 : 타입
    return {'name':name,'age':age,'msg':'쿼리스트링예시'}

# 6. 경로 파라미터   # http://localhost:8000/item/준현/25
@app.get('/item/{name}/{age}')
async def find_item(name:str,age:int):
    return {'name':name,'age':age,'msg':'경로파라미터예시'}

# 7. 본문(body)     # POST/PUT
@app.post('/product')
async def find_product(product:dict):   # 변수명:dict # 딕셔너리타입으로 받기
    return product

# RESTAPI 테스트 : [1] TalendAPI [2] Postman [3] FastAPI DOCX(http://localhost:8000/docs)