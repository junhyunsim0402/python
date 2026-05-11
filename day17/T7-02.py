import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# [1] 크롤링 주소 확인 : https://www.yes24.com/product/category/daybestseller?categoryNumber=001
url="https://www.yes24.com/product/category/daybestseller?categoryNumber=001"

# [2] 주소의 매개변수 분석 https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=1&pageSize=24&type=day
# 1~3페이지 크롤링 예
book_list=[]
for page in range(1,4):
    url=f'https://www.yes24.com/product/category/daybestseller?pageNumber={page}'
    # f'문자열{변수/계산식}문자열{변수/계산식}'

    # [3] url요청
    response=requests.get(url)

    # [4] 요청한 URL 의 성공했을때 html로 파싱
    soup=BeautifulSoup(response.text,'html.parser')
    
    # [5] 가져올 식별자
    # 책여러개 : #yesBestList 여러게 첵 정보, li(책하나)
    books=soup.select('#yesBestList > li')
    # 책 하나당 : .gd_name 책 이름, yes_b 가격, .info_auth 저자
    for book in books:
        gd_name=book.select_one('.gd_name')
        yes_b=book.select_one('.yes_b')
        info_auth=book.select_one('.info_auth')
    
    # [6] 리스트[]에 딕셔너리{} 포함하기
    book_list.append({"제목":gd_name,"가격":yes_b,"저자정보":info_auth})
    # [7] import time, time.sleep(초), 지정한 초 만큼 코드(스레드)가 대기상태, 즉] 여러개 크롤링 할때 서버 과부화 방지
    time.sleep(2)

# [8] 확인
print(book_list)
df=pd.DataFrame(book_list)
print(df)