list_dict = [
  {"a": 12},
  {"a": 11},
  {"a": 13},
  {"b": 14},
  {"a": 15},
  {"a": 16},
  {"a": 17},
]

# for item in list_dict:
#   # key check
#   # 전처리
#   pass

for item in list_dict:
  print(item['a'])
  print(item.get('a', 1))