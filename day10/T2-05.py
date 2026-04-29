import numpy as np

# 병합 .concatenate((x,y),axis=0), axis=0( 행기준 ), 1(열기준)
x = np.array([1,2],[3,4])
y = np.array([5,6],[7,8])
print(np.concatenate(x,y),axis=0)

# 정렬, sort(x) : 오름차순, .sort(x)[::-1] : 내림차순정렬 
x=np.array([3,1,2,5,7])
print(np.sort(x))
print(np.sort(x)[::-1])

# 2차원 정렬
x = np.array([[3,1,2],[9,7,6]])
print(np.sort(x,axis=0))