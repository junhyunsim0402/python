import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

book_list=[]
for page in range(1,10):
    url=f'https://www.yes24.com/product/category/daybestseller?pageNumber={page}&pageSize=100'

    response=requests.get(url)

    soup=BeautifulSoup(response.text,'html.parser')
    
    books=soup.select('#yesBestList > li')
    for book in books:
        gd_name=book.select_one('.gd_name')
        yes_b=book.select_one('.yes_b')
        saleNum=book.select_one('.saleNum')
        info_date=book.select_one('.info_date')
        book_list.append({
            "제목":    gd_name.get_text(strip=True),
            "가격":    yes_b.get_text(strip=True),
            "판매지수": saleNum.get_text(strip=True),
            "출판년월": info_date.get_text(strip=True),
        })
    time.sleep(3)
    
df=pd.DataFrame(book_list)
df['가격'] = df['가격'].str.replace(',', '').str.replace('원', '').astype(int)
df['출판년월']=pd.to_datetime(df['출판년월'],format='%Y년 %m월')
df['연도']=df['출판년월'].dt.year
df['월']=df['출판년월'].dt.month
df.to_csv('./yes24/yes24_900.csv',index=True,encoding='utf-8')
print(df)
print(df['연도'])
print(df['월'])