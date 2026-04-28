# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 
#       - 로그인
#       - 로그아웃
#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력

def signin():
    with open("./day9/user.txt", "a") as file:
        user_id = input("아이디 입력 >")
        user_pw = input("비밀번호 입력 >")
        name = input("닉네임 입력 >")
        file.write(f"{user_id}, {user_pw}, {name}\n")

def login():
     with open("./day9/user.txt", "r") as file:
        user_id = input("아이디 입력 >")
        user_pw = input("비밀번호 입력 >")
        for line in file:
            read_user_id, read_user_pw, read_name = line.strip().split(", ")
            if not read_user_id or not read_user_pw:
                continue
            elif read_user_id == user_id and read_user_pw == user_pw:
                print("로그인 성공")
                print(read_name,"님 환영합니다")
                return True
        print("로그인 실패")
        return False


state = False # 유저 로그인 상태를 표시하는 변수

while True:
    if state == False:
        print("""
              비로그인 메뉴
              1. 회원가입
              2. 로그인
              3. 종료
              """)
        try:
            menu_num = int(input("메뉴 번호를 선택 >"))
        except:
            print("메뉴 숫자를 입력")
            continue

            
        if menu_num == 1:
            print("회원가입")
            signin()
        elif menu_num == 2:
            print("로그인")
            
            state = login()
        elif menu_num == 0:
            break
        else:
            print("올바른 메뉴 번호를 입력")

    else:
        with open("./day9/아파트.csv", "r") as file:
            data = []
            header = None
            value = None
            for line in file:
                if "NO" in line:
                    header = [h.strip('"') for h in line.strip().split(",")]
                    break
                else:
                    continue
            for line in file:
                if line.strip():
                    first = line.strip().split(",")[0].strip('"')
                    if first.isdigit():
                        value = [v.strip('"') for v in line.strip().split(",")]
                        row_dict = {}
                        for i in range(len(header)):
                            row_dict[header[i]] = value[i]
                        data.append(row_dict)
            while state == True:
                print("""
                    로그인 메뉴
                    1. 지역명 검색
                    2. 금액 범위 검색
                    3. 전체 통계 조회
                    0. 로그아웃
                    """)
                try:
                    menu_num = int(input("메뉴 번호를 선택하세요 >"))
                except:
                    print("메뉴 숫자를 입력해 주세요")
                    continue
                
                if menu_num == 1:
                    keyword = input("검색할 지역명 >")
                    for row in data:
                        if keyword in row["시군구"]:
                            print(row)
                elif menu_num == 2:
                    min_price = int(input("최소금액 입력 >"))
                    max_price = int(input("최대금액 입력 >"))
                    for row in data:
                        price_str = row["거래금액(만원)"].strip()
                        price = float(price_str.replace(",", ""))
                        if min_price <= price <= max_price:
                            print(row)
                elif menu_num == 3:
                    total = 0
                    count = 0

                    for row in data:
                        price_str = row["거래금액(만원)"].strip()
                        price = float(price_str.replace(",", ""))
                        total += price
                        count += 1

                    if count > 0:
                        avg = total / count
                        print(f"전체 평균 거래금액: {int(avg)}만원")
                    else:
                        print("데이터 없음")
                elif menu_num == 0:
                    print("로그아웃")
                    state = False
                else:
                    print("올바른 메뉴 번호를 입력해 주세요")