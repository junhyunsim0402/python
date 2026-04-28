import numpy as np 

# 리스트
print( [1,2,3] + [4,5,6] ) # [1, 2, 3, 4, 5, 6]

# 배열 연산 , 두 배열간의 동일한 위치끼리 연산 수행 
x = np.array( [1,2,3] ) 
y = np.array( [4,5,6] )
print( x + y )  # [5 7 9]           더하기 
print( x - y )  # [-3 -3 -3]        빼기
print( x * y )  # [ 4 10 18]        곱하기 
print( x / y )  # [0.25 0.4  0.5 ]  나누기
print( x % y )  # [1 2 3]           나머지
print( x ** 2 ) # [1 4 9]           제곱 
print( y // x ) # [4 2 2]           몫 

# 비교 연산 
print( x > y )  # [False False False]
print( x == y ) # [False False False]

# 배열 +*/% 숫자 : 자동으로 전체에 적용 
print( x + 10 ) # [11 12 13]
print( y * 2 )  # [ 8 10 12]

# 논리 연산 , .logical_and( x , y ) , .logical_or( x , y ) , .logical_not( x )
x = np.array( [True , False , True ] )
y = np.array( [False, False , True ] )
print( np.logical_and( x , y ) )    # [False False  True] 모두 참이면 참 
print( np.logical_or( x , y ) )     # [ True False  True] 하나라도 참이면 참 
print( np.logical_not( x ) )        # [False  True False] 반대/부정 

# 루트( 수학 ) , sqrt
y = np.array( [ 1, 4 , 9 ] )
print( np.sqrt( y ) )               # float 실수로 반환된다.

# 2차원 비교 
y = np.array( [ [1,2,3] , [4,20,6 ] ]  )
print( y > 3 )
# [[False False False]
#  [ True  True  True]]

x = np.array( [ 1, 10, 3 ] )
print( x > y )              # x 1차원(행1개) , y 2차원(행N개)
# [[False  True False]
#  [False False False]]

# .all( x ) : 모두 참이면 참  , .any( x ) : 하나라도 참이면 참 
x = np.array( [ True , False , True ] )
print( np.all( x ) )    # False
print( np.any( x ) )    # True 

# .array_equal( x , y ) : 두 배열의 요소들이 모두 같으면 True , False 반환 
x = np.array( [1,2,3] )
y = np.array( [1,2,3] )
z = np.array( [1,2,4] )
print( np.array_equal( x , y ) )    # True
print( np.array_equal( x , z ) )    # False