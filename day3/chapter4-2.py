# 딕셔너리 란? 키를 기반으로 값을 저장하는 것
# vs JS(JSON) vs jAVA(map/dto)

# [1] 선언
dict_a={"name":"어벤져스","type":"히어로무비"}

# [2] 호출
print(dict_a)
# print(dict_a.name) # JS는 가능하지만 오류 발생
print(dict_a["name"])
print(dict_a.get("name")) # JAVA MAP처럼 호출 가능
# print(dict_a["origin"]) # 없는 키 오류 발생

# [3] 딕셔너리 값 추가, 딕셔너리명['key']=value
dict_a["price"]=1000
print(dict_a)
dict_a['price']=2000 # 만약에 존재하면 key이면 value수정 # key는 중복 불가능
# [4] 덱셔너리 키 값 제거
del dict_a['price']
print(dict_a)

# 문제 1
# 1-1
dict_a={}
dict_a['name']='구름'
print(dict_a)
# 1-2
del dict_a['name']
print(dict_a)

# 문제 2
# 2-1
pets=[
    {"name":"구름","age":5},
    {"name":"초코","age":3},
    {"name":"아지","age":1},
    {"name":"호랑이","age":1}
]
for key in pets:
    print(key["name"],key["age"],'살')

# 문제 3
numbers=[1,2,3,4,5,6,4,3,2,5,6,7,8,5,4,3,2,3,6,8]
counter={}
for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1
print(counter)

# 문제 4
character={
    "name":"기사",
    "lever":12,
    "item":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}
for key in character:
    if type(character[key]) is dict:
        for subkey in character[key]:
            print(subkey, ":", character[key][subkey])

    elif type(character[key]) is list:
        for i in character[key]:
            print(key, ":", i)

    else:
        print(key, ":", character[key])