import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font',family='Malgun Gothic') # 한글 폰트 설정(윈도우 기준 설치된 폰트)
mpl.rcParams['axes.unicode_minus']=False # 음수 기호 깨짐 방지
# 1
x=[0,1,2,3,4]
y=[10,20,15,25,30]
y2=[5,15,10,20,25]
plt.plot(x,y,label='매출',color='blue',linestyle=':')
plt.plot(x,y2,label='비용',color='red',linestyle='-')
plt.legend()
plt.grid('y2')
plt.show()

# 2
import pandas as pd
import numpy as np
category=['A','B','C']
국어=[80,90,70]
수학=[85,85,95]
x=np.arange(len(category))
plt.bar(x-0.2,국어,width=0.4,label='국어점수')
plt.bar(x+0.2,수학,width=0.4,label='수학점수')
plt.xticks(x, category)
plt.ylabel('점수')
plt.grid(axis='y')
plt.show()

# 3
labels=['스마트폰','태블릿','노트북','기타']
sizes=[45,25,20,10]
explode=[0.1,0,0,0]
plt.pie(sizes,labels=labels,explode=explode,startangle=90,autopct='%1.1f%%')
plt.show()

# 4
x = [1,2,3,4]
y = [10,15,13,18]
plt.scatter(x,y,c='blue',s=100)
plt.show()
plt.grid()
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5, color='skyblue')
plt.show()

# 5
fig,axs=plt.subplots(1,2,figsize=(10,5))
axs[0].plot([1,2,3],[1,2,3])
axs[1].bar([1,2,3],[3,5,2])
plt.savefig('./day13/my_analysis.png')
plt.show()

# 6
import seaborn as sns
data=[
    [50,60,70,80],[10,20,30,40],[90,80,70,60],[30,40,50,60],[20,10,5,0]
]
sns.heatmap(data,cmap='Blues',fmt='d',annot=True)
plt.title('수치 분포 히트맵')
plt.show()

# 7
data = {
    '매출': [100, 200, 150, 300, 250],
    '영업이익': [20, 50, 30, 80, 60]
}
df=pd.DataFrame(data)
sns.boxplot(data=df,gap=0.1,fill=False)
plt.title('주요 경영 지표 분포')
plt.show()

# 8
data={
    '지역': ['서울', '부산', '제주'],
    '영업이익': [17000, 12000, 600],
    '평균연령': [40,42,42]
}
df=pd.DataFrame(data)
number_df=df.set_index('지역').select_dtypes(include=['number'])
sns.heatmap(number_df,cmap='coolwarm',linewidths=0.5,annot=True,fmt='d')
plt.show()

# 9
data = {
    '이름': ['A', 'B', 'C', 'D', 'E', 'F'],
    '선택 메뉴': ['피자', '치킨', '피자', '햄버거', '치킨', '피자']
}
df = pd.DataFrame(data)
sns.countplot(data=df, x='선택 메뉴')
plt.title('메뉴별 주문 빈도')
plt.ylabel('주문 수')
plt.show()