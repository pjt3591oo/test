# 변수 => 데이터를 저장하는 공간 => 메모리에 저장함 => 운영체제


# 데이터 타입 
# 자료구조 => 데이터를 저장하는 방식
#  리스트, 딕셔너리
#  DOM => 트리

# 반복문

# 조건문

asd1 = 10
asd2 = 10.0 # 실수, 고정 소수점, 부동 소수점
asd3 = "10.0" # 아스키 코드나 유티코드 같은 코드로 변환, 다른 메모리 공간에 저장 => 힙 영역
asd4 = "10"

var_list = [] # 엑셀 row, 순서로 데이터 접근 => 순서 0
var_dict = {} # 엑셀 column, 키값을 이용해서 데이터 접근 => 순서 X

# 데이터 삽입
var_list.append(1)
var_list.append(2)
var_list.append(3)
var_list.append(4)
# 데이터 추출
a = var_list.pop()
b = var_list.pop()
c = var_list.pop()
d = var_list.pop()

var_dict = {
  "k1": 1,
  "k2": 2,
  "k3": 3,
  "k4": 4,
  "k5": 5,
}

print(var_dict)