# [ Python practice3 ]
# [ 제출방법 ] 코드가 작성된 파일이 위치한 깃허브 상세 주소를 제출하시오.

# 문제 1: 인덱싱과 슬라이싱 리스트 list_data = [10, 20, 30, [40, 50, 60], 70]가 있습니다. 슬라이싱과 인덱싱을 사용하여 다음 결과가 나오도록 코드를 작성하시오.
# 출력 결과 1: [20, 30] (슬라이싱 이용)
# 출력 결과 2: 60 (중첩 리스트 인덱싱 이용)
list_data = [10, 20, 30, [40, 50, 60], 70]
print(list_data[1:3])
print(list_data[3][2])

# 문제 2: 리스트 요소 변경 및 역순 출력 리스트 colors = ["red", "green", "blue"]가 있습니다. "green"을 "yellow"로 변경하고,  리스트의 요소를 역순(['blue', 'yellow', 'red'])으로 출력하시오.
colors = ["red", "green", "blue"]
colors[1]="yellow"
print(list(reversed(colors)))

# 문제 3: 요소 추가 및 삽입 빈 리스트 my_list = []를 생성한 후, .append()를 사용하여 숫자 10, 30을 순서대로 추가하고, .insert()를 사용하여 10과 30 사이에 숫자 20을 삽입하여 [10, 20, 30]을 만드시오.
my_list=[]
my_list.append(10)
my_list.append(30)
my_list.insert(1,20)
print(my_list)

# 문제 4: 요소 제거 실습 리스트 nums = [0, 1, 2, 3, 4, 5]에서 다음 지시대로 요소를 제거하고 최종 리스트를 출력하시오.
# del을 사용하여 인덱스 0번 요소 삭제
# .pop()을 사용하여 마지막 요소 삭제
# .remove()를 사용하여 값 3 삭제
nums = [0, 1, 2, 3, 4, 5]
del nums[0]
nums.pop(-1)
nums.remove(3)
print(nums)


# 문제 5: 리스트 정렬과 포함 여부 score = [85, 95, 70, 100] 리스트를 내림차순(큰 숫자부터)으로 정렬하고, 사용자로부터 숫자를 입력받아 해당 숫자가 score 리스트 안에 있는지 in 연산자를 사용하여 True/False로 출력하시오.
score = [85, 95, 70, 100]
score.sort(reverse=True)
print(score)
user=int(input("숫자>"))
print(user in score)

# 문제 6: 딕셔너리 기본 선언 및 호출 다음 정보를 담은 딕셔너리 movie를 선언하고, .get() 메서드를 사용하여 영화의 "감독"을 출력하시오.
# 제목: 파묘
# 감독: 장재현
# 개봉: 2024
movie = {
    "제목": "파묘",
    "감독": "장재현",
    "개봉": 2024
}

print(movie.get("감독"))


# 문제 7: 딕셔너리 값 수정 및 삭제 위 6번에서 만든 movie 딕셔너리에 "장르": "미스터리"를 추가하고, "개봉" 키와 값을 삭제한 후 전체 딕셔너리를 출력하시오.
movie["장르"]="미스터리"
del movie["개봉"]
print(movie)

# 문제 8: 반복문을 이용한 딕셔너리 출력 딕셔너리 fruit_stock = {"apple": 10, "banana": 5, "cherry": 15}가 있습니다. for 반복문을 사용하여 다음과 같은 형식으로 출력하시오.
# 출력 형식: apple의 재고는 10개입니다. (모든 요소 반복)
fruit_stock = {"apple": 10, "banana": 5, "cherry": 15}
for key in fruit_stock:
    print("{}의 재고는 {}개 입니다".format(key,fruit_stock[key]))

# 문제 9: 리스트 내 딕셔너리 순회 아래와 같은 리스트가 있을 때, 반복문을 사용하여 각 학생의 이름과 점수를 출력하시오.
# Python
# students = [
#     {"name": "윤동주", "score": 90},
#     {"name": "백석", "score": 85}
# ]
# # 출력 예시: 윤동주 학생의 점수는 90점입니다.
students = [
    {"name": "윤동주", "score": 90},
    {"name": "백석", "score": 85}
]
for student in students:
    print("{} 학생의 점수는 {}점입니다.".format(student["name"], student["score"]))

# 문제 10: 전개 연산자(*) 활용 list_x = [1, 2, 3]와 list_y = [4, 5]가 있습니다. 전개 연산자를 사용하여 두 리스트의 요소를 하나로 합친 1차원 리스트 [1, 2, 3, 4, 5]를 만들고 출력하시오.
list_x = [1, 2, 3]
list_y = [4, 5]
new = [*list_x, *list_y]

print(new)