
# customer_purchase_data.csv 다운로드 받아서 현재 py 파일과 같은 폴더에 저장 
import numpy as np

# 1. .csv( ,쉼표로 구분한 자료의 형식 ) 파일 가져오기 
# data = np.genfromtxt( "파일경로" , delimiter='구분문자' , skip_header=제외할헤더(행)수)
data = np.genfromtxt( 
    "./day11/customer_purchase_data.csv" , 
    delimiter=',' , 
    skip_header=1 )
# 2. 가져온 데이터의 넘파이 형식 확인 
print( data.shape )

# [1-1] 특정 열 / 행 추출  , 배열[ : , 열번호 ] , 배열[ 행번호 , : ]
sales = data[ : , 4 ] 
print( sales )
# [1-2] 평균 
print( '평균 : ' , np.mean( sales ) , '총매출액 : ' , np.sum( sales ) )

# [2] 조건 필터링 , [ ] 안에 인덱스 대신에 논리조건식 가능하다.
cont1 = data[ : , 1 ] >= 20 
cont2 = data[ : , 4 ] >= 2000
result = data[ cont1 & cont2 ]
print( result[ : , 0] )

# [3-1] 통계 , max( )  , argmax( )
# --------------------------------------------- # 
x = np.array( [ 3 , 3 , 3 ] )
y = np.array( [ 10 , 10 , 10 ] )
print( x / y )  # [0.3 0.3 0.3] 주의할점 : 배열 연산시 동일한 위치끼리 연산 
# --------------------------------------------- # 
arpv = data[ : , 4 ] / data[ : , 1 ]
print( np.max( arpv )  )                # 최댓값 # 525.0
findIndex = np.argmax( arpv )           # 최댓값 인덱스 위치 
print( data[ findIndex , 0 ] )          

# [4-1] 전체에서 몇명 인지 <---> 조건 True 개수  
cont1 = (data[ : , 1 ] <= 3 ) & ( data[ : , 3 ] <= 1 )      # 조건에 따른 True만 추출  
print( np.sum( cont1 ) )                                    # 배열에 전체 True 합계 = 23
print( len( data[cont1] ) )

# [5] 정규화, 공식 : ( 값 - 최솟값 ) / ( 최댓값 - 최소값 ) 
# 어떠한 자료들을 0과 1 사이의 값으로 만들어서 ( 백분율 0:0% ~ 1:100% ) , 비교가 쉽다(용이하다)
# 0.9 : 90% 위치한 구매가격 가진 고객들 
data_min = np.min( data[ : , 4 ] )
print( data_min )
data_max = np.max( data[ : , 4 ] )
print( data_max )
norm_data = ( sales - data_min ) / ( data_max - data_min ) 
vip_data = norm_data >= 0.9
print( vip_data )
print( data[ vip_data ] )
print( len( data[vip_data] ) )
# ------------------------------------- # 
x = np.array( [ True , False , True ] )
y = np.array( [ 1 , 2 , 3 ] ) 
print( y[x] )   # [1 3]