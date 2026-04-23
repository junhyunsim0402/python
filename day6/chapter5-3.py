
# 콜백함수 : 함수의 매개변수에 사용하는 함수
def call_10_items( func ) : #매개변수로 받는 함수 
    for i in range( 10 ) :
        func()

def print_hello():
    print("안녕하세요")

call_10_items( print_hello )        # 함수자체 
# call_10_items( print_hello( ) )      # 함수실행 # 예외 발생 

# map() , filter() 함수
# map( 함수 , 리스트 )  :  리스트의 요소를 *하나씩* 함수매개변수에 대입하여 *새로운리스트* 반환 
# filter( 함수 , 리스트 ) : 리스트의 요소를 *하나씩* 함수매개변수에 대입하여 참(True)인 경우 *새로운리스트* 반환 

def power( item ) : 
    return item * item  # 제곱 반환 
def under_3( item ) :
    return item < 3     # 3미만 True 반환 

list_input_a = [ 1 , 2 , 3 , 4 , 5 ] #
# JAVA : list_input_a.stream.map( 함수 ).toList()          
# JS : list_input_a.map( 함수 )                            
# PY : map( 함수 , list_input_a )

output_a = map( power , list_input_a )
print( list( output_a ) )               # [1, 4, 9, 16, 25]

output_b = filter( under_3 , list_input_a )
print( list(output_b) )                 # [1, 2]

# 제너레이터 : 함수 내부에 yield 키워드를 사용하며 next()함수를 외부에서 호출하여 yield 키워드 까지 실행한다.
def test() : 
    print( "A 지점 통과")
    yield 1 
    print( "B 지점 통과")
    yield 2

test()              # 함수 호출시 실행이 안된다.
output = test()     # (1) 함수 반환값을 변수에 저장 
a = next( output )  # (2) 함수 반환값이 저장된 변수를 next 에 대입한다.
print( a )          # (3) yield 까지 실행되고 yield 반환값이 반환된다. 

b = next( output )
print( b )

# c = next( output )  # 다음 yield 가 없으므로 예외발생 
# print( c )

# 람다 : 함수 선언 간단하게 하는 문법 
# lambda 매개변수 : 반환값 

# JS 방법1 선언적함수 콜백
# funciton 함수명(){}   ,    const 함수명 = ( ) => { }
# <button onClick = { 함수명  } >

# JS 방법2 람다(화살표) 콜백 
# <button onClick = { () => {} } >

# 방법1 : 재사용 가능하다.
power = lambda x : x * x 
output_a = map( power , list_input_a )
print( list(output_a) )

# 방법2 : 재사용 안된다. 
output_a = map( lambda x : x * x , list_input_a )
print( list(output_a) )

# 파일처리 
# open( 파일경로 , 읽기모드 ) , file객체가 반환된다. 
# 읽기모드 : w새로쓰기 a이어쓰기 r읽기모드 
# (1) .open() 함수 이용하여 지정한 경로의 파일 쓰기 
file  = open( './day06/basic.txt' , 'w')    # 현재 .py 파일 폴더내 basic.txt 생성 
# (2) .write( 출력할내용 ) 함수 이용한 내보내기  
file.write( '안녕 파이썬 프로그래밍..!')
# (3) .close() 함수 이용한 안전하게 스트림 닫기 
file.close()

# (4) with 키워드 이용한 .close() 자동 닫기 
with open( './day06/basic2.txt' , 'w' ) as file :
    file.write( '안녕 파이썬 프로그래밍2..!')

# 스트림이란? 데이터가 흐르는 길 , 바이트단위 , 프로그래밍언어가 외부 자료와 연결(파일,JDBC,네트워크 등)

# (5) .read() 함수 이용한 파일 읽어오기 
with open( './day06/basic.txt' , 'r' ) as file : 
    contents = file.read( )
print( contents )           # 안녕 파이썬 프로그래밍..!

# 확인문제1 
numbers = [1, 2, 3, 4, 5, 6]
# print( "::".join( numbers ) )   # .join( [문자열 리스트] ) 이므로 오류 발생 

# 방법1) 일반for
new_numbers = []
for i in numbers : 
    a = str( i )                    # 리스트 내 요소 하나씩 문자열 타입변환 
    new_numbers.append( a )         # 타입변환 한 문자열을 리스트에 대입 
print( new_numbers )                # ['1', '2', '3', '4', '5', '6']
print( "::".join( new_numbers ) )   # 1::2::3::4::5::6

# 방법2) map
print( "::".join( map( str , numbers) ) )         # map( 함수 , 리스트 )    #1::2::3::4::5::6

# 확인문제2
numbers = list( range(1, 10+1) ) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print( list( filter( lambda x : x % 2 == 1  , numbers) )) # lambda 매개변수 : 반환값 
print( list( filter( lambda x : 3 <= x < 7 , numbers ) )) 
print( list( filter( lambda x : x*x < 50 , numbers ) ))