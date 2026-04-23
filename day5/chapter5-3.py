# 튜플 : ( ) 소괄호 이용하여 여러 자료들을 감싼 자료형 , 단*)수정이 안된다.

# 튜플 선언 
tuple_test = ( 10 , 20 , 30 )
print( tuple_test )

# 요소 호출 , 인덱스 사용 
print( tuple_test[0] )

# 주의할점 : 수정 안된다.
# tuple_test[0] = 40      # TypeError: 'tuple' object does not support item assignment

# 주의할점2 : 요소가 1개 인 경우에는 ,쉼표 넣어준다.
tuple_test2 = ( 273, )

# 할당 구문 : 오른쪽에 있는 리스트/튜플 에 자료들을 왼쪽 각 변수에 대입
[ a , b ] = [ 10 , 20 ]
print( a , b )
( c , d ) = ( 10 , 20 )
print( c , d )

# 튜플은  소괄호 생략 해도 된다.
tuple_test = 10 , 20 , 30 , 40
print( tuple_test )

# 튜플 이용한 스왑(교체)
a , b = 10, 20          # 10,20 갖는 튜플을 할당 구문으로 a=10 , b = 20 대입된다. 
a , b = b , a           # 할당 구문 이용한 자료 스왑/교체 
print( a , b )        # 20 10

# 함수 리턴 값 
def test() : 
    return 10,20    # (10,20)  , [ 10, 20 ] , { 'a':10 , 'b':20 }