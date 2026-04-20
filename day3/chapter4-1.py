# 리스트란? 여러 자료들을 모아 하나의 자료로 구성
# [ 요소, 요소, 요소, 요소, 요소 ]
# 인덱스란? 자료가 저장된 순서 , 0번 시작

list_a = [ 273, 32 , "문자열" , True ]
print( list_a[0] )          # 273 
# 슬라이싱
print( list_a[ 1 : 3 ] )    # [32, '문자열']
# print( list_a[4] ) # 없는 인덱스는 에러 발생 

# 요소값 변경 
list_a[1] = "변경값"
print( list_a )             # 변경값 

# 뒤에서부터 요소 선택 
print( list_a[-2] )         # 문자열

# 리스트 안에 리스트 사용 가능
print( list_a[2][1] )       # list_a[2] => "문자열"[1] => 자

list_a[1] = [ '변경값1' , '변경값2' ]
print( list_a[1][1] )       # 변경값2


# 리스트 연산
list_a = [ 1, 2, 3 ]
list_b = [ 4, 5, 6 ]
# [1] + 연결 
print( list_a + list_b )    # [1, 2, 3, 4, 5, 6]
# [2] * 반복 
print( list_a * 3 )         # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# [3] len 길이
print( len(list_a) )        # 3

# 리스트에 요소 추가
# [4] 요소 추가하기  , .append( 자료 )
list_a.append( 4 )
print( list_a )             # [1, 2, 3, 4]
# [5] 중간에 요소 추가하기 , .insert( 위치 , 자료 )
list_a.insert( 1 , 1.5 )    
print( list_a )             # [1, 1.5, 2, 3, 4]

# 리스트에 요소 제거
list_a = [ 0, 1, 2, 3, 4, 5 ]

# [6] del 리스트명[인덱스]
del list_a[1]
print( list_a ) # [0, 2, 3, 4, 5]

# [7] 리스트명.pop( 인덱스 ) 
list_a.pop( 2 )
print( list_a ) # [0, 2, 4, 5]
list_a.pop()
print( list_a ) # [0, 2, 4]

# [*] 슬라이싱 이란? 인덱스로 구성된 자료들(문자열/리스트)의 요소 선택 기능
# [ 시작인덱스 : 끝인덱스 : 단계 ]
print( list_a[ : : -1 ] )       # [4, 2, 0] # 역순 
print( list_a[ 0 : : 2] )       # [0, 4] # 0부터 마지막인덱스까지 2칸씩 이동 

# [8] 리스트명.remove( 자료 ) , 해당 자료가 존재하면 삭제 
list_a.remove( 2 )
print( list_a )                 # [0, 4]

# [9] 리스트명.clear() 
list_a.clear()
print( list_a )                 # []

# [10] .sort() 리스트 정렬  , .sort( reverse=True )
list_a = [ 52 , 273 , 103 , 32 ]
list_a.sort()                   # 오름차순( 파괴적 )
print( list_a )                 # [32, 52, 103, 273]

list_a.sort( reverse=True )     # 내림차순 
print( list_a )                 # [273, 103, 52, 32]

# [11] in , 내부에 있는지 확인 
print( 103 in list_a )          # True
print( 250 in list_a )          # False
print( 103 not in list_a )      # True -> False

# 리스트와 반복문 ,
# for 반복변수 in 반복할수있는자료 :
#   코드 

리스트명 = [ 273, 32, 103, 57, 52 ]
for 요소 in 리스트명 : 
    print( 요소 )

for 요소 in "안녕하세요" :
    print( 요소 )

# 중첩 리스트 # 중첩 반복문 # 2차원 리스트 
list_of_list = [ 
    [ 1, 2, 3 ],        # 1행 3열
    [ 4, 5, 6, 7],      # 2행 4열 
    [ 8, 9]             # 3행 2열 
]

for row in list_of_list : 
    print( row )        # 각 행 출력 
    for col in row : 
        print ( col )   # 각 행의 열 출력  

# 전개 연산자 , *
list_a = [ 1 , 2 , 3 ]
print( list_a ) # [1, 2, 3] # 리스트 그자체 
print( *list_a ) # 리스트 그자체가 아닌 , 1 2 3 # 리스트는 첫번째 인덱스를 참조한다.

print( [ list_a , list_a ] )    # 2차원 리스트 구성 
print( [ *list_a , *list_a ] )  # 1차원 리스트 구성

# p.213 확인문제

# 1. 
list_a = [0, 1, 2, 3, 4, 5, 6, 7 ]
list_a.extend( list_a ) 
print( list_a ) # [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]

list_a = [0, 1, 2, 3, 4, 5, 6, 7 ]
list_a.append( 10 )
print( list_a ) # [0, 1, 2, 3, 4, 5, 6, 7, 10]

list_a = [0, 1, 2, 3, 4, 5, 6, 7 ]
list_a.insert( 3, 0 )
print( list_a ) # [0, 1, 2, 0, 3, 4, 5, 6, 7]

list_a = [0, 1, 2, 3, 4, 5, 6, 7 ]
list_a.remove( 3 )
print( list_a ) # [0, 1, 2, 4, 5, 6, 7]

list_a = [0, 1, 2, 3, 4, 5, 6, 7 ]
list_a.pop( 3 )
print( list_a ) # [0, 1, 2, 4, 5, 6, 7]

list_a = [0, 1, 2, 3, 4, 5, 6, 7 ]
list_a.clear()
print( list_a ) # []

# 2. number >= 100 

numbers = [ 273, 103, 5, 32, 65, 9, 72, 800, 99 ]
# 3-1
for 요소 in numbers : 
    if 요소 % 2 == 1 : 
        print( 요소 , "는 홀수 입니다.")
    else :
        print( 요소 , "는 짝수 입니다.")

# 3-2 
for 요소 in numbers :
    요소 = str( 요소 ) # 숫자 자료 -> 문자 자료 변경 
    문자열길이 =  len( 요소 )   # 문자열 길이  = 자릿수 검사 
    # 결론 
    print( 요소 , "는" , 문자열길이 ,"자릿수 입니다.")

# 4. number % 3 -1   # 3구역 나누기 위해서 % 3   # -1 이유는 인덱스 0부터 표현하기위해서

# 5. i*2 + 1