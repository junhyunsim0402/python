import pandas as pd

# [13] 판다스 표 병합 ( SQL JOIN ), .merge( left/right, on='공통컬럼명,how='inner/outer/left/right' )
df_info=pd.DataFrame({
    'ID':[1,2,3],
    'Name':['Ant','Bee','Cat']
})
df_score=pd.DataFrame({
    'ID':[2,3,4],
    'Score':[88,92,85]
})
# 두 판다스 간에 ID가 같은(교집합) 자료 병합
result=pd.merge(df_info,df_score,on='ID',how='inner')
print(result)

result=pd.merge(df_info,df_score,on='ID',how='left')
print(result)

result=pd.merge(df_info,df_score,on='ID',how='outer')
print(result)

# [14] 판다스 합치기, .concat([x,y],axis=0/1,ignore_index=True/False)
result=pd.concat([df_info,df_score],axis=0,ignore_index=True)
print(result) # 세로 연결

result=pd.concat([df_info,df_score],axis=1)
print(result) # 가로 연결

new_score=pd.Series([85,90,88],name='Score') # 새로운 열
df_info['NewScore']=new_score # 새로운 열 대입
print(df_info)

# [15] 정렬, 
# .sort_values(by='정렬기준',ascending=True(오름 / 기본값 )/False(내림))
# .sort_values(by=['정렬기준'],ascending=True(오름 / 기본값 )/False(내림))
# .sort_index(axis=0(행)/1(열),ascending=True(오름 / 기본값 )/False(내림))
x={
    'Name':['Ant','Bee','Cat','Dog'],
    'Age':[27,27,22,32],
    'Score':[88,95,85,90]
}
df=pd.DataFrame(x)

result=df.sort_values(by='Score',ascending=False)
print(result)

result=df.sort_values(by=['Age','Score'],ascending=[True,False]) # 나이기준 오름차순, 점수기준 내림차순
print(result)

# 열이름(라벨) 내림차순으로 정렬
result=df.sort_index(axis=1,ascending=False)
print(result)

# [16] 그룹, .groupby( '그룹기준' )['집게기준'].집계함수()
df=pd.DataFrame({
    'Category':['A','A','B','B','A','B'],
        'Type':['X','Y','X','Y','X','Y'],
      'Values':[10,20,30,40,50,60]
})
result=df.groupby('Category')['Values'].sum() # 카테고리 별 값 합계
print(result)
result=df.groupby('Type')['Values'].mean() # 타입별 값 평균
print(result)

# 다중 그룹
result=df.groupby(['Category','Type'])['Values'].sum()
print(result)

# 다중 집계
result=df.groupby(['Category','Type'])['Values'].agg(['sum','mean','count'])
print(result)

