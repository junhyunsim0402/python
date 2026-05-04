# [1] seaborn 설치 : pip install seaborn
# [2] seaborn 불러오기 : import seaborn as sns
import seaborn as sns
# [*] 차트내 한글 깨짐 방지 코드,(+한글폰트), 항상 차트 사용하는 파일 상단에 복붙
import matplotlib as mpl
mpl.rc('font',family='Malgun Gothic') # 한글 폰트 설정(윈도우 기준 설치된 폰트)
mpl.rcParams['axes.unicode_minus']=False # 음수 기호 깨짐 방지

# day13 sample
import matplotlib.pyplot as plt
#[1] 히트맵, .headmap(2차원 자료,cmap='맵색상',fmt='자료타입')
# 자료타입 : d(정수), .1f(실수), .2%백분율, g자동

data = [  # 히트맵에 사용할 2차원 리스트 데이터 (행렬 형태)
    [100, 150, 200, 120],  # 첫 번째 행 데이터
    [80, 120, 180, 160],   # 두 번째 행 데이터
    [90, 140, 170, 190],   # 세 번째 행 데이터
    [75, 130, 190, 180],   # 네 번째 행 데이터
    [60, 110, 160, 140]    # 다섯 번째 행 데이터
]

# 1. sns(seaborn)
sns.heatmap(data,cmap='Blues',fmt='d',annot=True)
# 2. plot, 주의할점 : seaborn 으로 차트 구성하되 차트 출력은 matplotlib으로 한다
plt.title('히트맵 그래프')
plt.show()

import pandas as pd
#[2] 박스플롯
# 윗선 -> 최댓값, 아랫선 -> 최솟값, 박스안에 선 -> 중앙값,
# 박스가 크면 변동성이 크다(불안정성)/작으면 변동성이 작다(안정성)
# 박스밖에 점 -> 이상치( 특이값/데이터 범위 크게 벗어남 )
# .boxplot(data=지료(pandas))
data = {  # 딕셔너리 형태 데이터 생성
    '수익': [1000, 1500, 1300, 1600, 1700],  # 수익 데이터
    '비용': [800, 1200, 1100, 1300, 1250]   # 비용 데이터
}
df=pd.DataFrame(data)
# 1. 
sns.boxplot(data=df,gap=0.5)
# 2
plt.show()

#[3][4]
data = {  # 지역별 데이터 생성
    '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],  # 지역 이름
    '인구 밀도(명/km²)': [17000, 12000, 8000, 10000, 7000, 6500, 7500, 9000, 11000, 500, 1200, 1300, 800, 700, 1100, 1400, 600],  # 인구 밀도
    '평균 연령': [40, 42, 38, 39, 37, 36, 35, 34, 41, 43, 45, 44, 38, 36, 37, 39, 42]  # 평균 연령
}
df=pd.DataFrame(data) # 1. 데이터프레임 만들기
print(df)
# 2. 해당 지역( 인덱스 )마다의 숫자 데이터만 추출 df.set_index('인덱스').select_dtypes(include=['number'])
number_df=df.set_index('지역').select_dtypes(include=['number']) # 2. 지역
print(number_df)
# 3. 히트맵, .headmap(판다스자료, cmap='색상계열',annot=True/값표기,fmt='d'/정수)
sns.heatmap(number_df,cmap='Blues',annot=True,fmt='d')
# 4. 
plt.show()

df=pd.DataFrame(data)
# 1. 카운트플롯, .countplot(판다스자료, x='x측라벨(열이름)')
sns.countplot(df,x='평균 연령')
# 2. 차트출력
plt.show()