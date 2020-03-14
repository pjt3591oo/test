var_dict = { 
  "k1": "v1",
  "k2": "v2"
}
k1 = "k2"
print(var_dict[k1]) # equal print(var_dict["k2"])

print(var_dict["k1"])

print(var_dict)
var_dict["k2"] = "v3" # 키-값 쌍을 생성 또는 수정
del var_dict['k1']
print(var_dict)

print(var_dict['no'])