# PythonML Practice7: 로지스틱 분류
# 데이터 출처: https://www.kaggle.com/code/anshigupta01/iris-flower-classification

# [단계 1] 데이터 로드 및 독립/종속 변수 추출
# 파일명: ./Iris.csv
import pandas as pd
df = pd.read_csv( './pythonML/day5/Iris.csv')
# 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm' 4개 열을 독립 변수 X로,
Iris_input = df[ [ 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm' ] ]

# 'Species' 열을 종속 변수 y로 추출하세요.
Iris_target = df['Species']

# [단계 2] 훈련용 / 테스트용 데이터 분리
from sklearn.model_selection import train_test_split
train_input , test_input , train_target , teset_target = train_test_split( Iris_input , Iris_target , random_state=42)

# [단계 3] 데이터 표준화 (Standardization), 스케일러
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(train_input)
train_scaled=ss.transform(train_input)
test_scaled=ss.transform(test_input)

# [단계 4] 로지스틱 분류 모델 학습 (Logistic Regression)
indexs=(train_target=='Iris-setosa')|(train_target=='Iris-versicolor')
train_setosa_versicolor=train_scaled[indexs]
target_setosa_versicolor=train_target[indexs]
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(train_setosa_versicolor,target_setosa_versicolor)
print(lr.predict(train_setosa_versicolor[:3])) # ['Iris-setosa' 'Iris-setosa' 'Iris-versicolor']
print(lr.predict_proba(train_setosa_versicolor[:3]))
# [[0.98662232 0.01337768]
#  [0.99592095 0.00407905]
#  [0.04295872 0.95704128]]
print(lr.score(test_scaled,teset_target)) # 0.6842105263157895

# [단계 5] 모델 평가 및 분류 정확도(Accuracy) 확인 * 테스트 세트의 정확도가 0.95 이상이 나오도록 설정
lr=LogisticRegression(C=20,max_iter=1000)
lr.fit(train_scaled,train_target)
print(lr.predict(train_setosa_versicolor[:3])) # ['Iris-setosa' 'Iris-setosa' 'Iris-versicolor']
print(lr.predict_proba(train_setosa_versicolor[:3]))
# [[9.99499946e-01 5.00054289e-04 8.31259924e-17]
#  [9.99932713e-01 6.72865907e-05 7.48329179e-19]
#  [3.95912591e-03 9.81411942e-01 1.46289325e-02]]
print(lr.score(test_scaled,teset_target)) # 1.0

# [단계 6] 학습한 종속 변수 출력
from scipy.special import softmax
decision=lr.decision_function(test_scaled[:3])

import numpy as np
print(np.round(softmax(decision),decimals=3))
# [[0.    0.    0.   ]
#  [0.043 0.    0.   ]
#  [0.    0.    0.957]]
print(lr.classes_) # ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

# [단계 7] 테스트 세트의 앞선 5개 샘플 데이터에 대해 모델이 예측한 클래스를 출력하세요.
print(lr.predict(test_scaled[:5])) # ['Iris-versicolor' 'Iris-setosa' 'Iris-virginica' 'Iris-versicolor' 'Iris-versicolor']
print(lr.predict_proba(test_scaled[:5]))
# [[2.92194032e-04 9.89856336e-01 9.85146963e-03]
#  [9.94607367e-01 5.39263257e-03 1.62039313e-15]
#  [5.88779638e-16 1.34966308e-06 9.99998650e-01]
#  [3.75664267e-04 9.55541454e-01 4.40828821e-02]
#  [8.79601187e-06 9.59284369e-01 4.07068352e-02]]