# 모듈 만들기 : .py 파일 만들기와 같다
# 1. xxx.py 생성한다
# 2. 다른 .py 파일내에서 import 하여 호출한다

import test_module as test
radius=test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# 프로그램의 진입점 : __name__ == __main__
print(__name__) # __main__