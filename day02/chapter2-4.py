# 문자열의 format( ) 함수  , 자바의 System.out.printf( " %s " , 10 ) 
string_a = "{}".format( 10 )
print( string_a  , type( string_a ) )

format_a = "{}만 원".format( 5000 )
print( format_a )
format_d = "{} {} {}".format( 1 , "유재석" , True ) # {} 개수와 자료개수 일치해야 한다.
print( format_d )

# 특정 칸에 출력하기  , {:자릿수d} , {:0자릿수d}
output_a = "{:5d}".format( 52 ) #   52  { } 안에서 공백 주의 
print( output_a )
output_b = "{:05d}".format( 52 ) # 00052
print( output_b )

# 기호 붙여 출력하기 , {:+d} 
output_c = "{:+d}".format( 52 )
print( output_c )
output_d = "{:+d}".format( -52 )
print( output_d )

# 부동소수점 출력하기
output_e = "{:15f}".format( 52.273 )
print( output_e )
output_f = "{:+015f}".format( 52.273 ) # +기호 , 0으로채움 , 15 자릿수 , f 실수 
print( output_f )
output_g = "{:15.3f}".format( 52.2737 ) # .소수자릿수f , 만약에 잘린 소수점에서 반올림 된다.
print( output_g )

# 의미없는 소수점 제거하기
output_g = "{:g}".format( 52.0 )
print( output_g )

# 대소문자 바꾸기
a = "Hello Python"
print( a.upper() ) # 대문자로 변경 
print( a.lower() ) # 소문자로 변경

# 공백 제거하기 , strip() 양쪽공백 제거 , lstrip() , rstrip()   
b = "        안녕하세요       "
print( b.strip() )

# 문자열 찾기 
out_a = "안녕안녕하세요".find( "안녕" )
print( out_a ) # 0번 인덱스에 "안녕" 존재한다.
out_b = "안녕안녕하세요".rfind( "안녕" )
print( out_b ) # 2번 인덱스에 "안녕" 존재한다.

print( "안녕" in "안녕하세요" ) # True
print( "잘자" in "안녕하세요" ) # False 

# 문자열 자르기 , split( 기준문자 )
out_c = "10 20 30 40 50".split( " " ) 
print( out_c )

# f-문자열 vs .fomat( )
print( f'{ 10 }')       
print( "{}".format(10) )