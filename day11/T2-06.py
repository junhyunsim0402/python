import numpy as np
# 1차원 배열 통계 
x = np.array( [1,2,3,4,5] )
print( np.min( x ) )    # 최솟값 
print( np.max( x ) )    # 최댓값 
print( np.argmin( x ) ) # 최솟값 (인덱스)위치
print( np.argmax( x ) ) # 최댓값 (인덱스)위치
print( np.ptp( x ) )    # 최댓값 - 최솟값 
print( np.sum( x ) )    # 합계
print( np.mean( x ) )   # 평균 
print( np.median( x ) ) # 중앙값 
print( np.var( x ) )    # 분산 : 요소들의 흩어짐 정도
print( np.std( x ) )    # 표준편차 : 분산의 양의 제곱근 
print( np.sqrt( x ) )   # 루트

# 사분위수 : 구역을 4개 구역으로 나눠서 데이터 분포 위치 파악  , q1 : 제1사분위수 , 
q1 = np.percentile( x , 25 )    # 1/4 , 25% , 하위 25% 
q3 = np.percentile( x , 75 )    # 3/4 , 75% , 하위 75% 
print( q1 )
print( q3 )
q2 = np.percentile( x , 50 )    # 2/4 , 50% , 중앙값 
print( q2 )
q4 = q3 - q1
print( q4 )

# 2차원 배열 통계  , 통계함수( x , axis = 0 )   0=열기준 1=행기준 
y = np.array( [ [1,2,3], [4,5,6 ] ] )
print( np.min( y ) ) 
print( np.min( y , axis= 0 ) )  # 열개수가 3개이니까 최솟값 3개 
print( np.min( y , axis= 1 ) )  # 행개수가 2개이니까 최솟값 2개 
print( np.max( y ) )            # axis 생략하면 2차원배열 평탄화(1차원으로변경)해서 통계
print( np.argmax( y ) )         # 최댓값 위치
print( np.argmin( y ) )
print( np.sum( y ) )
print( np.mean( y ) )
print( np.median( y ) )
print( np.var( y ) )
print( np.std( y ) )
print( np.sqrt( y ) )