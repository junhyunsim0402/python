# 넘파이 : 파이썬 언어 기반으로 수치 계산 특화된 라이브러리 ( AI )
# 파이썬에 *리스트*가 존재하는데 굳이 *넘파이배열* 사용하는 이유 ? 수치 관련 기능 차이

# 문제 1: ndarray 생성
import numpy as np  # as 별칭( 아무거나 )
array1 = np.array( [10, 20, 30, 40] )       
array2 = np.array( [[1, 2], [3, 4]] ) 
print( array1 ) 
print( array2 ) 

# 문제 2: 특정 값으로 채워진 배열
print( np.zeros( (3, 4 ) ) )
print( np.ones( (2, 5 ) ) )
print( np.full( (3, 3 ) , 9 ) ) 

# 문제 3: 연속된 수와 균등 간격 배열
print( np.arange( 10, 50+1 , 5 ) )  # [10 15 20 25 30 35 40 45 50]
print( np.linspace( 0 , 10 , 5 ) )  # [ 0.   2.5  5.   7.5 10. ]

# 문제 4: shape와 size 확인
x = np.array([[1, 2, 3], [4, 5, 6]])
print( x.shape )    # ( 행개수 , 열개수 )
print( x.size )     # 배열내 전체 요소 수 반환 

# 문제 5: 차원 확인 (ndim)
x = np.array( [1, 2, 3] )
print( x.ndim ) # 1
x = np.array( [[[1], [2]], [[3], [4]]] )
print( x.ndim ) # 3


# 문제 6: 데이터 타입(dtype) 확인
x = np.array( [1.5, 2.5, 3.5] )
print( x.dtype )    # float64

# 문제 7: 배열 평탄화 순회 (flat)
x  = np.zeros( (2,2) )
for i in x.flat : 
    print( i )

# 문제 8: 타입 지정 생성
x = np.array( [1,2,3] , dtype= np.int32 )
x = np.array( [True, False, True ] , dtype= np.bool_ )  # 파이썬 과 _넘파이 타입 구분 _(언더바) 차이 

# 문제 9: 형변환 (astype)
x = np.array([1.1, 2.9, 3.5])
y = x.astype( np.int32 )
print( y )  

# 문제 10: 바이트 문자열 배열
# 데이터 타입을 np.bytes_로 지정하여 생성하고 결과를 확인하시오.
x = np.array( ['apple', 'banana'] , dtype= np.bytes_ )
print( x.dtype )    # <U6   ---> |S6