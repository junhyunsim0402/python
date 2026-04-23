# [ Python Practice: 함수1 ]
# [ 제출방법 ] 코드가 작성된 파일이 위치한 깃허브 상세 주소를 제출하시오.

# 문제 1: 성인 인증 함수 (is_adult)
# 나이(age)를 일반 매개변수로 받아 20세 이상이면 True, 미만이면 False를 반환하는 함수를 작성하시오.
# age=int(input("나이 입력>"))
# def is_adult(a):
#     if a>=20:
#         return True
#     else:
#         return False
# print(is_adult(age))

# 문제 2: 인사말 출력 함수 (say_hello)
# 이름(name)과 인사말(message) 두 개의 매개변수를 받는 함수를 작성하시오. 이때 message는 기본 매개변수로 설정하여 값이 입력되지 않으면 "안녕하세요"가 출력되도록 하시오.
# 호출 예시: say_hello("홍길동") -> 결과: 홍길동님, 안녕하세요.
# name=input("이름:")
# msg=input("인사말:")
# def say_hello(a, b="안녕하세요"):
#     if b=="":
#         return "{}님, 안녕하세요".format(a)
#     return "{}님, {}".format(a,b)
# print(say_hello(name,msg))


# 문제 3: 삼각형의 넓이 계산 (get_triangle_area)
# 밑변(width)과 높이(height)를 매개변수로 받아 삼각형의 넓이를 반환하는 함수를 작성하시오.
# width=int(input("밑변:"))
# height=int(input("높이:"))
# def get_triangle_area(a, b):
#     return a * b / 2
# print(get_triangle_area(width,height))

# 문제 4: 입장료 계산 함수 (get_ticket_price)
# 나이(age)를 매개변수로 받아 입장료를 반환하는 함수를 작성하시오. (8세 미만: 무료, 8~19세: 5,000원, 20세 이상: 10,000원)
# age=int(input("나이 입력: > "))
# def get_ticket_price(a):
#     if a < 8:
#         return "무료"
#     elif a <= 19:
#         return "5,000원"
#     else:
#         return "10,000원"
# print(get_ticket_price(age))

# 문제 5: 가변 인자 합계 구하기 (sum_all)
# 가변 매개변수(*args) 를 사용하여 전달받는 숫자의 개수에 상관없이 모든 숫자의 합계를 반환하는 함수를 작성하시오.
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# 문제 6: 가장 긴 단어 찾기 (find_longest)
# 여러 개의 단어를 전개 매개변수로 입력받아 그중 가장 길이가 긴 단어를 반환하는 함수를 작성하시오.
# 호출 예시: find_longest("apple", "strawberry", "kiwi") -> 결과: strawberry
def find_longest(*words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# 문제 7: 최고 점수 학생 찾기 (get_top_student)
# 학생 정보(이름, 점수)가 담긴 딕셔너리들이 포함된 리스트를 매개변수로 받아 가장 높은 점수를 받은 학생의 이름을 반환하는 함수를 작성하시오.
# 데이터: [{'name': 'A', 'score': 80}, {'name': 'B', 'score': 95}]
def get_top_student(students):
    top_name = ""
    max_score = 0
    
    for student in students:
        if student["score"] > max_score:
            max_score = student["score"]
            top_name = student["name"]
    
    return top_name

# 문제 8: 리스트 요소 합계 (sum_list)
# 숫자로 이루어진 리스트 하나를 매개변수로 받아 for문을 사용하여 모든 요소의 합계를 구한 뒤 반환하는 함수를 작성하시오.
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# 문제 9: 전역 변수 점수 관리
# 전역 변수 current_score = 0을 선언하고, 점수를 추가하는 add_score(n) 함수와 감점하는 sub_score(n) 함수를 작성하시오. (함수 내에서 global 키워드를 사용하여 전역 변수 값을 수정하시오.)
current_score = 0

def add_score(n):
    global current_score
    current_score += n

def sub_score(n):
    global current_score
    current_score -= n

# 문제 10: 상품 결제 시스템 (calculate_payment)
# 상품 가격(price)과 수량(count)은 일반 매개변수로 받고, 할인율(discount)은 기본 매개변수 0.1(10%)로 설정하시오. (최종 결제 금액 = 가격 * 수량 * (1 - 할인율)) 결과는 정수형으로 반환하시오.
def calculate_payment(price, count, discount=0.1):
    return int(price * count * (1 - discount))