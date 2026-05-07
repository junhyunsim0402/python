import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

# [1] T5_data.json 파일 내 'risk_return_data'
with open('./day14/T5_data.json','r',encoding='utf-8') as json_file:
    data_json=json.load(json_file)
df=pd.DataFrame(data_json['risk_return_data'])

# [2] 산점도 : 리스크 대비 수익률, 값에 따른 계산식별로 원형크기 조절
# .scatter(x축,y축,c='색상',s=점 크기,alpha=투명도)
plt.scatter(df['리스크'],df['수익률(%)'],c='red',s=100*df['수익률(%)'],alpha=0.5)
plt.grid()
plt.title('리스크 대비 수익률')
plt.xlabel('리스크')
plt.ylabel('수익률')
plt.show()

# [3] 산점도 : 자산(유형)별 리스크 대비 수익률
categories=df['자산'].unique() # 중복제거된 자산 리스트
for i,category in enumerate(categories): # enumerate(리스트) 반복순회자 으로 인덱스와 요소값 하나씩 반환
    sub=df[df['자산']==category] # 동일한 자산 정보 불러오기
    print(sub)
    plt.scatter(sub['리스크'],sub['수익률(%)'],label=category)
plt.legend()
plt.show()

