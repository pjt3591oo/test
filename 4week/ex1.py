# 변수 => 데이터가 저장되는 공간
# 데이터 타입 => 데이터의 성질 => 문자열, 숫자, 리스트(자료구조), 딕셔너리(자료구조)
# 반복문
# 조건문 

# 배열, 리스트
# 배열 var[0] var[1] var[2] => 인덱싱이 가능 => 연속된 공간에서 데이터 저장
# 리스트 인덱싱이 안됨 => 연속된 공간에서 데이터 저장이 아님
# 딕셔너리

import json

var_list = [] # array
var_dict = {}
var_int = 1
var_float = 2.0
var_string1 = '1'
var_string2 = '1.0'

var_dict = {
  "k1": "v1",
  "k2": "v2",
  "k3": "v3",
  "k4": "v4",
  "k5": "v5"
}
# print(json.loads(json.dumps(var_dict)))
# json.dumps : dict, list => string
# json.loads : string => dict, list
# print(json.loads(json.dumps([1,2,3,45,6,7,8,]))[0])
origin_arr = [1,2,3,45,6,7,8]
# List Comprehension 조건문을 2개 이상 안써야 가독성이 좋아짐.
result = [{"key": item} for item in origin_arr if not item % 2] 

for idx, item in enumerate(origin_arr): # 제너레이터(generator)
  print(idx, item)