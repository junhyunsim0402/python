# [ Python Practice4 반복문 ]
# [ 제출방법 ] 코드가 작성된 파일이 위치한 깃허브 상세 주소를 제출하시오.

# 문제 1: range와 역순 출력 range() 함수와 reversed() 함수를 사용하여 10부터 1까지의 숫자를 역순으로 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
for i in reversed(range(11,1)):
    print(i)

# 문제 2: 누적 합계 계산 for문과 range()를 사용하여 1부터 100까지 정수 중 5의 배수만 더하여 최종 합계를 출력하시오.
# (출력 예시: 1부터 100까지 5의 배수의 합: 1050)
re=0;
for i in range(5,101,5):
    re+=i
print("1부터 100까지 5의 배수의 합: {}".format(re))

# 문제 3: enumerate 활용 리스트 fruits = ['사과', '바나나', '딸기', '포도']가 있습니다. enumerate()를 사용하여 아래와 같이 출력하시오.
# (출력 예시: 1번 과일: 사과, 2번 과일: 바나나 ...)
fruits = ['사과', '바나나', '딸기', '포도']
for i, fruit in enumerate(fruits, start=1):
    print("{}번 과일: {}".format(i, fruit))

# 문제 4: 리스트 내포(List Comprehension) 1부터 10개까지의 숫자 중 홀수만 골라 그 제곱값을 담는 리스트를 리스트 내포 방식을 사용하여 한 줄로 생성하고 출력하시오.
# (결과 예시: [1, 9, 25, 49, 81])
for i in range(1,11):
    if i%2==1:
        print(i*i)

# 문제 5: continue를 사용한 필터링 1부터 20까지의 숫자 중 2의 배수와 3의 배수를 모두 제외한 숫자만 출력하시오.
# 요구 조건: if문과 continue 문을 반드시 사용하시오.
list_a=[]
for i in range(1,21):
    if i%2==0 or i%3==0:
        continue
    list_a.append(i)
print(list_a)


# 문제 6: while문과 break (무한 루프) while True: 무한 루프를 사용하여 숫자를 계속 입력받으시오. 사용자가 0을 입력하면 "프로그램 종료"를 출력하며 반복을 멈추고, 그 전까지 입력받은 숫자들의 총합을 출력하시오.
count = 0
while True:
    user = int(input("0입력시 종료: "))
    if user == 0:
        print("프로그램 종료")
        break
    else:
        count += user

print("총합 : {}".format(count))

# 문제 7: 중첩 반복문 (구구단) 중첩 for문을 사용하여 구구단 2단부터 9단까지 출력하시오. 각 단의 시작에는 --- [N]단 ---과 같은 구분선을 넣으시오.
for i in range(2,10):
    print("--- {}단 ---".format(i))
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))

# 문제 8: 시각화 보고서 (매출 그래프) 아래 리스트는 4주간의 매출 데이터입니다. for문과 enumerate()를 사용하여 백만원 단위마다 ★ 문자로 시각화하여 보고서를 출력하시오.
# 데이터: sales = [350, 920, 580, 1100] (단위: 만원)
# 요구 조건: 만원 단위를 100으로 나눈 몫만큼 별을 출력하시오.
# (출력 예시: 1주차: ★★★ 350만원)
sales = [350, 920, 580, 1100]
for i,j in enumerate(sales,start=1):
    stars = "★" * (j // 100)
    print("{}주차 {} {}만원".format(i,stars,j))

# 문제 9: 차량별 주차 요금 계산 차량 번호 리스트와 이용 시간(분) 리스트 데이터를 활용하여 요금 규정에 따른 최종 요금을 계산하시오.
# 데이터:
# car_numbers = ["210어7125", "142가7415", "888호8888", "931나8234"]
# usage_minutes = [65, 30, 140, 420]
# 요금 규정:
# 기본 요금: 최초 30분까지 1,000원
# 추가 요금: 30분 초과 시, 매 10분마다 500원씩 추가
# 일일 최대 요금: 20,000원 (최대 요금을 초과할 수 없음)
# 출력 예시: 210어7125: 65분 주차, 최종 요금: 2500원
car_numbers = ["210어7125", "142가7415", "888호8888", "931나8234"]
usage_minutes = [65, 30, 140, 420]
for i in range(len(car_numbers)):
    number = car_numbers[i]
    time = usage_minutes[i]
    
    if time <= 30:
        fee = 1000
    else:
        extra_time = time - 30
        if extra_time % 10 == 0:
            fee = 1000 + (extra_time // 10) * 500
        else:
            fee = 1000 + (extra_time // 10 + 1) * 500
    if fee > 20000:
        fee=20000
    print("{}: {}분 주차, 최종 요금: {}원".format(number, time, fee))
    
# 문제 10: 간단한 ATM 기기 구현 while True 무한 루프를 사용하여 간단한 ATM 기능을 구현하시오.
# 요구 조건:
# 사용자에게 "1:입금 | 2:출금 | 3:잔고 | 4:종료" 메뉴를 보여주고 입력을 받습니다.
# 1번(입금): 입금액을 입력받아 잔고(balance)를 증가시킵니다.
# 2번(출금): 출금액을 입력받아 잔고를 감소시킵니다. (단, 잔고보다 큰 금액은 출금할 수 없다고 안내)
# 3번(잔고): 현재 잔고를 출력합니다.
# 4번(종료): "프로그램을 종료합니다." 메시지를 출력하고 break로 루프를 탈출합니다.
# (초기 잔고는 0으로 시작합니다.)
balance = 0

while True:
    print("---------------------------------------")
    print("1:입금 | 2:출금 | 3:잔고 | 4:종료")
    print("---------------------------------------")
    menu = input("선택> ")
    
    if menu == "1":
        amount = int(input("입금액> "))
        balance += amount
    elif menu == "2":
        amount = int(input("출금액> "))
        if amount > balance:
            print("잔고가 부족하여 출금할 수 없습니다.")
        else:
            balance -= amount
    elif menu == "3":
        print("현재 잔고: {}원".format(balance))
    elif menu == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")