import numpy as np

# 문제 1: 배열의 병합 (Concatenate)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print( np.concatenate( ( x , y ) , axis= 0 ) )
print( np.concatenate( ( x , y ) , axis= 1 ) )

# 문제 2: 배열 정렬 (Sorting)
x = np.array([3, 1, 2, 5, 4])
print( np.sort( x ) )
print( np.sort( x )[ : : -1 ] )
a = np.array([[3, 1, 2], [9, 8, 7]])
print( np.sort( a , axis= 0 ) )
print( np.sort( a , axis= 1 ) )

# 문제 3: 다중 조건 정렬 (lexsort)
y = np.array( ["철수", "영희", "민수", "영희"] )
x = np.array( [25, 30, 22, 24] )
result = np.lexsort( (x  , y) )     # ( 2차정렬기준 , 1차정렬기준 ) , 결과 인덱스 반환 
print( result  )
print( y[result] , x[result] )      # '영희'만 2차 정렬 

# 문제 4: 조건 검색과 필터링 (Boolean Indexing)
x = np.array([10, 20, 30, 40, 50])
print( x[ x > 30 ] )        # [ ] 안에는 인덱스가 들어가는 자리 인데 조건 필터링 가능하다.
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print( x[ x > 5 ] )

# 문제 5: np.where를 이용한 조건 처리
x = np.array([10, 20, 30, 40, 50])
print( np.where( x > 25 , x , -1 ) )
y = np.where( x < 30 )
print( y )  # [ 0 , 1 ]

# 문제 6: 마스크 배열 (Masked Array)
x = np.array([1, 2, 3, 4, 5])
cont1 = x % 2 == 1  # 마스크(가리기) 처리할 조건 
result = np.ma.array( x , mask= cont1 ) 
print( result ) # 짝수 
print( np.ma.sum( result ) )   # 짝수만 합계 

# 문제 7: 비트 연산자를 이용한 복합 조건 검색
x = np.array([10, 20, 30, 40, 50, 60, 70, 80])
y = np.array([15, 22, 35, 45, 55, 65, 75, 85])
print( x[ (x > 30) & (y < 50) ] )
print( x[ ~(y<50) ] )

# 문제 8: 기본 통계 함수 (Min, Max, Sum, PTP)
x = np.array([1, 2, 3, 4, 5])
print( np.min( x ) , np.max( x ) )
print( np.sum( x ) )
print( np.ptp( x ))

# 문제 9: 평균, 중앙값, 분산, 표준편차
x = np.array([[1, 2, 3], [4, 5, 9]])
print( np.mean( x ) , np.median( x ) )
print( np.std( x , axis= 0 ) , np.var( x , axis= 1 ) )

# 문제 10: 사분위수와 IQR 계산
x = np.array([10, 20, 30, 40, 50])
print( np.percentile( x , 25 ) , np.percentile( x , 75 ) )
print( np.percentile( x , 75 ) - np.percentile( x , 25 ) )