import pandas as pd # 판다스 ( 데이터 표 )
import matplotlib.pyplot as plt # 맷플롯립 ( 시각화 )
import koreanfont # 그래프 한글 깨짐 방지
import json # JSON 파일 load용도

# [1] JSON 파일에서 특정한 열('costomer_data')만 가져와서 데이터 구성
with open('./day14/T5_data.json','r',encoding='utf-8') as json_file:
    data_json=json.load(json_file)
df_customer=pd.DataFrame(data_json['customer_data'])
print(df_customer.head())

# [2] 데이터 분석/시각화
# (1) 성별과 연령대로 그룹화, df.groupby(['그룹기준','그룹기준'])
# (2) 통계 df.agg({'열이름':'함수명'})
# (3) 여러 그룹화할 경우에는 .reset_index() 함수 이용하여 행번호 붙인다
newDf=df_customer.groupby(['성별','연령대']).agg({'고객 수':'sum','평균 구매 금액':'mean'}).reset_index()
print(newDf) # 성별 + 연령대 별 총고객수 와 평균구매금액의 평균
print(newDf['연령대'])          # 남성 여성 포함하여 중복된 연령대
print(newDf['연령대'].unique())   # 남성 여성 포함하여 중복제거된 연령대
print(newDf.groupby(['연령대']).agg({'고객 수':'sum'})) # 연령대별 총 고객수

# 1. 연경대별 총 고객수 막대 그래프
# (1) plt.bar(x축값,y축값)
plt.bar(newDf['연령대'].unique(),newDf.groupby('연령대').agg({'고객 수':'sum'})['고객 수'],color='blue')
plt.xlabel('연령대 ')
plt.ylabel('총 고객수')
plt.legend()
plt.title('연령대별 누적 고객 수')
plt.show()

# 2. 성별 + 연령대별 막대 그래프 생성
male_data=newDf[newDf['성별']=='남성']
female_data=newDf[newDf['성별']=='여성']
plt.bar(male_data['연령대'],male_data['고객 수'],label='남자 수',color='blue')
# 만약에 겹쳐 나오는 경우 : 아래 순서로 변경할 막대에 bottom
plt.bar(
    female_data['연령대'],
    female_data['고객 수'],
    label='여자 수',
    color='red',
    bottom=male_data['고객 수']
)
plt.xlabel('연령대 ')
plt.ylabel('총 고객 수')
plt.legend()
plt.title('연령대별 누적 고객 수')
plt.show()

# 3. 연령대별 '평균 구매 금액' 가로막대 그래프
# plt.barh()
plt.barh(newDf['연령대'],newDf['평균 구매 금액'],color='red')
plt.show()