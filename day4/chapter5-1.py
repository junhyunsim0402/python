# 함수 만들기 
def 함수명( ) :             # 함수의 정의/만들기 
    print( "안녕하세요")
    print( "안녕하세요")
    print( "안녕하세요")

함수명( )                   # 함수 호출/사용 

# 매개변수 : 함수 호출/사용할 때 인자값 저장하는 변수 
def func2( value , n ) :            # 매개변수 2개 선언 
    for i in range( n ) :           # 매개변수 사용 
        print( value )

func2( "안녕하세요" , 5 )            # 함수에게 인자값 2개 전달

# 가변 매개변수 : 매개변수의 개수가 변할 수 있다.
def func3( n , *values ) :          # 매개변수에 *가변매개변수 사용시 [리스트] 타입 받는다.
    for i in range( n ) : 
        for value in values :       # values = [ "안녕하세요" , "즐거운" , "파이썬 프로그래밍" ]
            print( value )
        print()
func3( 3 , "안녕하세요", "즐거운","파이썬 프로그래밍")

# 기본 매개변수 : 만약에 함수 사용/호출할 때 인자값이 없으면 기본값 대입 
def func4( value , n = 2  ) :        # 매개변수에 변수명=기본값 으로 인자값이 없을때 대입된다.
    for i in range( n ) :
        print( value )

func4( "안녕하세요")

# 키워드 매개변수 : 매개변수 이름을 직접 지정하여 매개변수에 대입하는 방법
def func5( *values , n = 2 ) :
    for i in range( n ) : 
        for value in values :
            print( value )
        print()

func5( "안녕하세요" , "즐거운" , "파이썬 프로그래밍" , 3 ) # n매개변수에 3 대입 안된다.
func5( "안녕하세요" , "즐거운" , "파이썬 프로그래밍" , n = 3 ) # 직접 매개변수명 작성하여 대입하면 된다.

# 리턴 ? 함수 종료시 반환되는 키워드
# 반환값 없는 리턴 
def func6( ):
    return
print( func6() )        # None , 반환값이 없다. 

# 반환값 있는 리턴 
def func7( ) :
    return 100
print( func7() )        # 100



# 확인문제 1 
# (1) 
def f(x) : 
    return 2*x + 1 
print( f(10) )

# (2) 
def f(x) : 
    return x ** 2 + 2 * x + 1

# 확인문제 2 
def mul( *values ) :        # 가변 매개변수는 리스트 타입이다.
    result = 1 ;            # 모두 곱한 결과를 저장하는 변수 
    for value in values :   # 리스트 반복문 
        result *= value     # 하나씩 곱한다. 
    return result           # 함수 종료시 모두 곱한 결과 리턴/반환 
print( mul( 5 , 7 , 9 , 10 ))

# 확인문제 3 : 1.가변매개변수가 일반매개변수보다 뒤에 선언 되어야 한다.