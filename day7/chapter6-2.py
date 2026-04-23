# 예외 겍체 : Excepotion 클래스
# 1] try ~ except 예외클래스명 as 변수명 ~ except 예외클래스명 as 변수명
# 2] 모든 예외잡기 : *마지막에 except Exception 클래스 사용
# 3] 강제 예외 발생 : 1) 미구현 2) 웹/앱 프레임워크(유효성검사/트랜젝션)
list_number=[52,321,321,432,100]
try:
    number_input_a=int(input("정수입력>"))    # int() 에서 예외 발생 경우
    print(list_number[number_input_a])       # [] 에서 예외발생 경우
    raise NotImplementedError                # 강제 예외 발생
    예외.발생해주세요()                        # 예상치 못한 예외는 Exception
except ValueError as e:
    print("정수만 입력해주세요.")
except IndexError as e:
    print("인덱스를 벗어났어요")
except Exception as e:
    print(e)

