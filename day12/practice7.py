import pandas as pd

x=[['iponde',120,'apple'],['galaxy',110,'samsung'],['pixel',90,'google']]
df=pd.DataFrame(x,columns=['model','price','company'])
df.info()

data=pd.DataFrame({
    'Name':['Amt','Bee','Cat','Dog'],
    'Age':[24,27,22,32],
    'City':['Seoul','Busan','Incheon','Daejeon']
},index=['A','B','C','D'])
result=data.loc[['B','C'],['Name','Age']]
print(result)
result2=data.iloc[1,2]
print(result2)

data=pd.DataFrame({
    'Name':['Ant','Bee','Cat'],
    'Age':[24,27,22]
})
data['Score']=[85,90,95]
print(data)
data.loc[data['Score']>=90,'Name']='MVP'
print(data)

data=pd.DataFrame({
    'Name':['Ant','Bee','Cat','Dog'],
    'Age':[24,27,22,32],
    'Score':[85,90,95,76]
})
result=data[(data['Age']>=25) & (data['Score']>=80)]
print(result)

df1=pd.DataFrame({
    'ID':[1,2,3],
    'Name':['Ant','Bee','Cat']
})
df2=pd.DataFrame({
    'ID':[2,3,4],
    'Score':[88,92,85]
})
pd.merge(df1,df2,on='ID',how='inner')
pd.merge(df1,df2,on='ID',how='left')

# 6
df1=pd.DataFrame({
    'Name':['Ant','Bee'],
    'Score':[90,80]
})
df2=pd.DataFrame({
    'Name':['Cat','Dog'],
    'Score':[85,75]
})
result=pd.concat([df1,df2],axis=0,ignore_index=True)
print(result)

# 7
data=pd.DataFrame({
    'Name':['Ant','Bee','Cat','Dog'],
    'Age':[27,27,22,32],
    'Score':[88,95,85,90]
})
result=data.sort_values(by=['Age','Score'],ascending=[True,False])
print(result)

# 8
data=pd.DataFrame({
    'Category':['A','B','A','B','A','B'],
      'Values':[10,20,30,40,50,60]
})
result=data.groupby('Category')['Values'].agg(['sum','mean','count'])
print(result)

# 9
data=pd.DataFrame({
    'Category':['A','A','B','B'],
        'Type':['X','Y','X','Y'],
      'Values':[10,20,30,40]
})
result=data.groupby(['Category','Type'])['Values'].mean()
print(result)

# 10
data=pd.DataFrame({
    'Fruit':['Apple','banana','Apple','orange'],
      'Values':['red','yellow','red','orange']
})
print(data['Fruit'].value_counts())
data.columns=['Item','Style']
print(data)