import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import csv
import seaborn as sns

df = pd.read_csv(
    './team1/train_HousePrices.csv',
    encoding='utf-8',
    on_bad_lines='warn'
)

df['LotFrontage']=df['LotFrontage'].fillna(df['LotFrontage'].median())
df['MasVnrArea']=df['MasVnrArea'].fillna(df['MasVnrArea'].median())
df['GarageYrBlt']=df['GarageYrBlt'].fillna(df['GarageYrBlt'].median())

df['Alley']  = df['Alley'].fillna('NoAlley')
df['PoolQC'] = df['PoolQC'].fillna('NoPool')
df['Fence']  = df['Fence'].fillna('NoFence')

categories=[
    'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
    'Electrical', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
    'GarageCond', 'MSZoning', 'Functional', 'SaleType',
    'Exterior1st', 'Exterior2nd', 'MasVnrType'
]

for i in categories:
    df[i]=df[i].fillna(df[i].mode()[0])
# 1
sns.histplot(df['SalePrice'],label='주택 판매 가격 분포',kde=True)
plt.show()

# 2
sns.scatterplot( data=df , x='GrLivArea' , y='SalePrice' ,s=30)
plt.title('주거 면적에 따른 가격 분포')
plt.xlabel('주거 면적')
plt.ylabel('판매 가격')
plt.grid()
plt.show()

# 3
sns.boxplot(data=df, x='HouseStyle', y='SalePrice')
plt.title('주택 스타일별 가격 분포와 이상치')
plt.show()

# 4
sns.boxplot(data=df,x='RoofStyle', y='SalePrice')
sns.boxplot(data=df,x='Exterior1st', y='SalePrice')
plt.show()

# 5
matrix = df.corr(numeric_only=True)
plt.figure(figsize=(12, 10))
sns.heatmap(matrix, cmap='coolwarm')
plt.title('수치형 변수 상관관계 히트맵')
plt.show()