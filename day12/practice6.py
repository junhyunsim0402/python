import pandas as pd 

# 문제 1: Series 생성 및 인덱스 올바르게 변경하기
sales = {'mon': 100, 'tue': 200, 'wed': 300}    # 딕셔너리 데이터
x = pd.Series( sales )# Series로 변환한 후
x = x.rename( { 'mon' : '월' , 'tue' : '화' , 'wed' : '수'   } )    # 인덱스 변경하는 코드
print( x )

# 문제 2: 슬라이싱을 이용한 부분 수정
data = pd.Series([10, 20, 30, 40, 50],index=['a', 'b', 'c', 'd', 'e'])
data.iloc[ 1 : 4 ] = data.iloc[ 1 : 4 ] * 2     # 1. iloc을 사용하여 인덱스 *번호* 로 조회 
data.loc['d'] = 100                             # 2. loc을 사용하여 인덱스 *라벨명* 으로 'd'의 값 
print( data )   

# 문제 3: Series 연결과 중복 인덱스 조회
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([3, 4], index=['a', 'c'])
result = pd.concat( [ s1, s2 ])# pd.concat을 사용하여 연결(result)하고, 
print( result['a'] )# 인덱스 'a'를 loc으로 조회했을 때의 결과를 출력하시오.
print( result.loc['a'] )

# 문제 4: 복합 조건을 활용한 데이터 변경
data = pd.Series([15, 25, 35, 45, 55])
x = data[ ( data > 30 ) & ( data < 50 ) ] + 5  # 값이 30보다 크고 50보다 작은 요소들만 필터링하여 기존 값에 5를 더한 뒤, 최종 배열의 상태를 출력하시오.
print( x )

# 문제 5: 범주형 데이터의 빈도수 및 비율 분석
grade = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B'])
print( grade.value_counts() ) # 1. 각 알파벳별 빈도수(value_counts)를 출력하시오.
print( grade.value_counts( normalize=True ) ) # 2. 각 알파벳이 차지하는 상대적 비율을 소수점 형태로 출력하시오. (normalize 인자 활용)

# 문제 6: 산술 연산에서의 인덱스 정렬(Alignment) , numpy/pandas 연산시 에는 같은 위치끼리 연산 
s1 = pd.Series([10, 20], index=['a', 'b'])
s2 = pd.Series([30, 40], index=['b', 'c'])
result = s1 + s2 # 두 Series를 더한(s1 + s2) 결과를 출력하고 
print( result ) # 결측치(NaN)가 발생한 위치와 이유를 설명하시오.( a , c 는 짝이 없으므로 NaN 발생했다. )

# 문제 7: 다중 정렬 구현 (Values & Index)
data = pd.Series([20, 10, 20, 30], index=['d', 'c', 'a', 'b'])
# 1차정렬 이후에 유지 하기 위해서 , 1차정렬에 kind속성에 'stable' 적용하여 유지할 수 있다.
# sort( 2차 정렬 ).sort( 1차 정렬 )
result3 = data.sort_index( ).sort_values( ascending= False , kind='stable')
print( result3 )

# 정렬 따로 하는 경우에는 1차 정렬 과 2차 정렬 유지 불가능 # 
# result = data.sort_values( ascending=False )
# result2 = result.sort_index()
# print( result2 ) # 데이터 값(Values)은 내림차순으로 정렬하고, 값이 같을 경우 인덱스(Index)를 오름차순으로 정렬한 최종 결과를 출력하시오.

# 문제 8: 그룹화 및 다중 집계 함수 적용
data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'A', 'B']) 
print( data.groupby(level=0).agg( [ 'sum', 'mean'] ) ) # 인덱스 레벨(level=0) 기준으로 그룹화하여, 합계(sum)와 평균(mean)을 동시에 구하고 출력하시오.

# 문제 9: 가중 평균(Weighted Average) 계산
score = pd.Series([80, 90, 70], index=['math', 'eng', 'sci'])       # 점수 
weight = pd.Series([0.4, 0.3, 0.3], index=['math', 'eng', 'sci'])   # 가중점수 
x = ( score * weight ).sum() # 각 과목의 가중 점수를 합산한 최종 총점을 브로드캐스팅 연산을 통해 구하시오.
print( x )

# 문제 10: 필터링 및 인덱스 재설정 (Reset Index)
data = pd.Series([10, 30, 20, 40], index=['a', 'b', 'c', 'd'])
x = data[ data > 25 ]   # 1. 값이 25보다 큰 데이터만 추출하여 새로운 Series를 만드시오.
print( x )
y = x.reset_index( drop= True ) # 2. 추출된 Series의 기존 문자 인덱스를 제거하고 0부터 시작하는 숫자 인덱스로 재설정하시오.
print( y )